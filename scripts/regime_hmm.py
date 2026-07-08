#!/usr/bin/env python3
"""Gaussian HMM market-regime classifier, pure stdlib (no numpy/hmmlearn).

Reads an Alpaca `bars` JSON response from stdin, writes one line of JSON to
stdout describing the current SPY regime (Bull vs. Bear/High-Vol) decoded
from a 2-state Gaussian HMM over daily log returns. See
docs/hmm-regime-plan.md for the full design rationale.
"""

import json
import math
import random
import sys

N_STATES = 2
MIN_OBS = 100
CONFIDENCE_THRESHOLD = 0.65
N_RESTARTS = 8
BASE_SEED = 1729
MAX_ITERS = 100
LL_TOL = 1e-6
VARIANCE_FLOOR_FRACTION = 0.05
DIAG_PSEUDOCOUNT = 8.0
OFFDIAG_PSEUDOCOUNT = 1.0


def log_gaussian_pdf(x, mu, var):
    return -0.5 * math.log(2.0 * math.pi * var) - ((x - mu) ** 2) / (2.0 * var)


def logsumexp(values):
    m = max(values)
    if m == -math.inf:
        return -math.inf
    return m + math.log(sum(math.exp(v - m) for v in values))


def log_returns_from_bars(bars_json):
    bars = bars_json.get("bars")
    if bars is None:
        raise ValueError("no 'bars' field in input JSON")
    closes = [b["c"] for b in bars]
    returns = []
    for prev, cur in zip(closes, closes[1:]):
        if prev <= 0 or cur <= 0:
            continue
        returns.append(math.log(cur / prev))
    return returns


def emission_log_probs(returns, mu, var):
    T = len(returns)
    log_b = [[0.0] * T for _ in range(N_STATES)]
    for i in range(N_STATES):
        for t in range(T):
            log_b[i][t] = log_gaussian_pdf(returns[t], mu[i], var[i])
    return log_b


def forward_backward(log_pi, log_A, log_b):
    T = len(log_b[0])
    log_alpha = [[0.0] * N_STATES for _ in range(T)]
    log_beta = [[0.0] * N_STATES for _ in range(T)]

    for i in range(N_STATES):
        log_alpha[0][i] = log_pi[i] + log_b[i][0]
    for t in range(1, T):
        for j in range(N_STATES):
            log_alpha[t][j] = logsumexp(
                [log_alpha[t - 1][i] + log_A[i][j] for i in range(N_STATES)]
            ) + log_b[j][t]

    for i in range(N_STATES):
        log_beta[T - 1][i] = 0.0
    for t in range(T - 2, -1, -1):
        for i in range(N_STATES):
            log_beta[t][i] = logsumexp(
                [
                    log_A[i][j] + log_b[j][t + 1] + log_beta[t + 1][j]
                    for j in range(N_STATES)
                ]
            )

    log_likelihood = logsumexp([log_alpha[T - 1][i] for i in range(N_STATES)])

    gamma = [[0.0] * N_STATES for _ in range(T)]
    for t in range(T):
        for i in range(N_STATES):
            gamma[t][i] = math.exp(log_alpha[t][i] + log_beta[t][i] - log_likelihood)

    xi = [[[0.0] * N_STATES for _ in range(N_STATES)] for _ in range(T - 1)]
    for t in range(T - 1):
        for i in range(N_STATES):
            for j in range(N_STATES):
                xi[t][i][j] = math.exp(
                    log_alpha[t][i]
                    + log_A[i][j]
                    + log_b[j][t + 1]
                    + log_beta[t + 1][j]
                    - log_likelihood
                )

    return gamma, xi, log_likelihood


def viterbi(log_pi, log_A, log_b):
    T = len(log_b[0])
    log_delta = [[0.0] * N_STATES for _ in range(T)]
    psi = [[0] * N_STATES for _ in range(T)]

    for i in range(N_STATES):
        log_delta[0][i] = log_pi[i] + log_b[i][0]
    for t in range(1, T):
        for j in range(N_STATES):
            best_prev, best_val = 0, -math.inf
            for i in range(N_STATES):
                val = log_delta[t - 1][i] + log_A[i][j]
                if val > best_val:
                    best_val, best_prev = val, i
            log_delta[t][j] = best_val + log_b[j][t]
            psi[t][j] = best_prev

    path = [0] * T
    path[T - 1] = max(range(N_STATES), key=lambda i: log_delta[T - 1][i])
    for t in range(T - 2, -1, -1):
        path[t] = psi[t + 1][path[t + 1]]
    return path


def m_step(returns, gamma, xi, var_floor):
    T = len(returns)
    pi = [gamma[0][i] for i in range(N_STATES)]

    A = [[0.0] * N_STATES for _ in range(N_STATES)]
    for i in range(N_STATES):
        denom = sum(xi[t][i][j] for t in range(T - 1) for j in range(N_STATES))
        prior_denom = DIAG_PSEUDOCOUNT + (N_STATES - 1) * OFFDIAG_PSEUDOCOUNT
        for j in range(N_STATES):
            numer = sum(xi[t][i][j] for t in range(T - 1))
            prior = DIAG_PSEUDOCOUNT if i == j else OFFDIAG_PSEUDOCOUNT
            A[i][j] = (numer + prior) / (denom + prior_denom)

    mu = [0.0] * N_STATES
    var = [0.0] * N_STATES
    for i in range(N_STATES):
        weight_sum = sum(gamma[t][i] for t in range(T))
        mu[i] = sum(gamma[t][i] * returns[t] for t in range(T)) / weight_sum
        raw_var = (
            sum(gamma[t][i] * (returns[t] - mu[i]) ** 2 for t in range(T)) / weight_sum
        )
        var[i] = max(raw_var, var_floor)

    return pi, A, mu, var


def init_params(returns, rng, var_floor):
    assignments = [rng.randrange(N_STATES) for _ in returns]
    if len(set(assignments)) < N_STATES:
        assignments = [i % N_STATES for i in range(len(returns))]
        rng.shuffle(assignments)

    mu = [0.0] * N_STATES
    var = [0.0] * N_STATES
    for i in range(N_STATES):
        group = [r for r, a in zip(returns, assignments) if a == i]
        mu[i] = sum(group) / len(group)
        var[i] = max(
            sum((r - mu[i]) ** 2 for r in group) / len(group), var_floor
        )

    pi = [1.0 / N_STATES] * N_STATES
    A = [[0.0] * N_STATES for _ in range(N_STATES)]
    for i in range(N_STATES):
        for j in range(N_STATES):
            base = 0.9 if i == j else 0.1
            jitter = (rng.random() - 0.5) * 0.05
            A[i][j] = base + jitter
        row_sum = sum(A[i])
        A[i] = [v / row_sum for v in A[i]]

    return pi, A, mu, var


def fit_one_restart(returns, seed, var_floor):
    rng = random.Random(seed)
    pi, A, mu, var = init_params(returns, rng, var_floor)

    prev_ll = -math.inf
    for _ in range(MAX_ITERS):
        log_pi = [math.log(p) for p in pi]
        log_A = [[math.log(a) for a in row] for row in A]
        log_b = emission_log_probs(returns, mu, var)

        gamma, xi, log_likelihood = forward_backward(log_pi, log_A, log_b)
        pi, A, mu, var = m_step(returns, gamma, xi, var_floor)

        if abs(log_likelihood - prev_ll) < LL_TOL:
            prev_ll = log_likelihood
            break
        prev_ll = log_likelihood

    return pi, A, mu, var, prev_ll


def fit_best(returns, var_floor):
    best = None
    for r in range(N_RESTARTS):
        result = fit_one_restart(returns, BASE_SEED + r, var_floor)
        if best is None or result[-1] > best[-1]:
            best = result
    return best


def classify(returns):
    n_obs = len(returns)
    if n_obs < MIN_OBS:
        return {"regime": "Insufficient History", "n_obs": n_obs}

    global_mean = sum(returns) / n_obs
    global_var = sum((r - global_mean) ** 2 for r in returns) / n_obs
    var_floor = max(global_var * VARIANCE_FLOOR_FRACTION, 1e-12)

    pi, A, mu, var = fit_best(returns, var_floor)[:4]

    log_pi = [math.log(p) for p in pi]
    log_A = [[math.log(a) for a in row] for row in A]
    log_b = emission_log_probs(returns, mu, var)

    gamma, _, _ = forward_backward(log_pi, log_A, log_b)
    path = viterbi(log_pi, log_A, log_b)

    bull_state = max(range(N_STATES), key=lambda i: mu[i])
    current_state = path[-1]
    confidence = gamma[n_obs - 1][current_state]

    days_in_regime = 1
    for t in range(n_obs - 2, -1, -1):
        if path[t] == current_state:
            days_in_regime += 1
        else:
            break

    if confidence < CONFIDENCE_THRESHOLD:
        return {
            "regime": "Mixed/Uncertain",
            "confidence": round(confidence, 4),
            "n_obs": n_obs,
        }

    label = "Bull" if current_state == bull_state else "Bear/High-Vol"
    return {
        "regime": label,
        "confidence": round(confidence, 4),
        "days_in_regime": days_in_regime,
        "n_obs": n_obs,
    }


def main():
    raw = sys.stdin.read()
    bars_json = json.loads(raw)
    returns = log_returns_from_bars(bars_json)
    result = classify(returns)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
