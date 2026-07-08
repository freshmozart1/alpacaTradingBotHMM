"""Tests for scripts/regime_hmm.py — pure stdlib, no numpy/hmmlearn.

Run: python3 -m unittest discover tests
"""

import math
import os
import random
import sys
import unittest
from itertools import product
from unittest.mock import patch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import regime_hmm as rh  # noqa: E402


def gaussian_pdf(x, mu, var):
    return (1.0 / math.sqrt(2.0 * math.pi * var)) * math.exp(
        -((x - mu) ** 2) / (2.0 * var)
    )


class BruteForceGroundTruthTest(unittest.TestCase):
    """Brute-force enumeration of all 2^T state paths for a tiny toy HMM,
    compared against the DP (forward-backward/Viterbi) implementation."""

    def setUp(self):
        self.pi = [0.6, 0.4]
        self.A = [[0.7, 0.3], [0.2, 0.8]]
        self.mu = [-0.01, 0.01]
        self.var = [0.0004, 0.0009]
        self.returns = [0.005, -0.008, 0.012, -0.002, 0.007]
        self.T = len(self.returns)

        self.log_pi = [math.log(p) for p in self.pi]
        self.log_A = [[math.log(a) for a in row] for row in self.A]
        self.log_b = rh.emission_log_probs(self.returns, self.mu, self.var)

    def _brute_force(self):
        b = [
            [gaussian_pdf(self.returns[t], self.mu[i], self.var[i]) for t in range(self.T)]
            for i in range(rh.N_STATES)
        ]
        path_probs = {}
        for path in product(range(rh.N_STATES), repeat=self.T):
            prob = self.pi[path[0]] * b[path[0]][0]
            for t in range(1, self.T):
                prob *= self.A[path[t - 1]][path[t]] * b[path[t]][t]
            path_probs[path] = prob

        total_likelihood = sum(path_probs.values())
        best_path = max(path_probs, key=path_probs.get)

        gamma_bf = [[0.0] * rh.N_STATES for _ in range(self.T)]
        for path, prob in path_probs.items():
            for t, state in enumerate(path):
                gamma_bf[t][state] += prob / total_likelihood

        return total_likelihood, best_path, gamma_bf

    def test_log_likelihood_matches_brute_force(self):
        total_likelihood, _, _ = self._brute_force()
        _, _, log_likelihood = rh.forward_backward(self.log_pi, self.log_A, self.log_b)
        self.assertAlmostEqual(log_likelihood, math.log(total_likelihood), places=6)

    def test_viterbi_path_matches_brute_force_map(self):
        _, best_path, _ = self._brute_force()
        path = rh.viterbi(self.log_pi, self.log_A, self.log_b)
        self.assertEqual(tuple(path), best_path)

    def test_posterior_gamma_matches_brute_force(self):
        _, _, gamma_bf = self._brute_force()
        gamma, _, _ = rh.forward_backward(self.log_pi, self.log_A, self.log_b)
        for t in range(self.T):
            for i in range(rh.N_STATES):
                self.assertAlmostEqual(gamma[t][i], gamma_bf[t][i], places=6)


class LogSpaceVsNaiveSpaceTest(unittest.TestCase):
    """Log-space forward algorithm must agree with a plain (non-log)
    forward algorithm on a moderate-length sequence with no underflow risk."""

    def test_log_and_naive_forward_agree(self):
        pi = [0.55, 0.45]
        A = [[0.85, 0.15], [0.25, 0.75]]
        mu = [-0.005, 0.006]
        var = [0.0002, 0.0003]

        rng = random.Random(42)
        returns = [rng.gauss(0.0, 0.01) for _ in range(30)]
        T = len(returns)

        log_pi = [math.log(p) for p in pi]
        log_A = [[math.log(a) for a in row] for row in A]
        log_b = rh.emission_log_probs(returns, mu, var)
        _, _, log_likelihood = rh.forward_backward(log_pi, log_A, log_b)

        b = [[gaussian_pdf(returns[t], mu[i], var[i]) for t in range(T)] for i in range(2)]
        alpha = [[0.0, 0.0] for _ in range(T)]
        for i in range(2):
            alpha[0][i] = pi[i] * b[i][0]
        for t in range(1, T):
            for j in range(2):
                alpha[t][j] = sum(alpha[t - 1][i] * A[i][j] for i in range(2)) * b[j][t]
        naive_log_likelihood = math.log(sum(alpha[T - 1]))

        self.assertAlmostEqual(log_likelihood, naive_log_likelihood, places=6)


class PersistencePriorTest(unittest.TestCase):
    """The Dirichlet-style transition prior should pull the estimated
    diagonal (self-transition) probability toward persistence much more
    for a fast-flipping sequence than for an already-persistent one."""

    @staticmethod
    def _one_hot_gamma_xi(path):
        T = len(path)
        gamma = [[0.0] * rh.N_STATES for _ in range(T)]
        for t, s in enumerate(path):
            gamma[t][s] = 1.0
        xi = [[[0.0] * rh.N_STATES for _ in range(rh.N_STATES)] for _ in range(T - 1)]
        for t in range(T - 1):
            xi[t][path[t]][path[t + 1]] = 1.0
        return gamma, xi

    def _diagonal_transition(self, path, returns, with_prior):
        gamma, xi = self._one_hot_gamma_xi(path)
        if with_prior:
            _, A, _, _ = rh.m_step(returns, gamma, xi, var_floor=1e-8)
        else:
            with patch.object(rh, "DIAG_PSEUDOCOUNT", 0.0), patch.object(
                rh, "OFFDIAG_PSEUDOCOUNT", 0.0
            ):
                _, A, _, _ = rh.m_step(returns, gamma, xi, var_floor=1e-8)
        return A[0][0]

    def test_prior_effect_stronger_on_fast_flipping_sequence(self):
        rng = random.Random(1)
        fast_flip_path = [t % 2 for t in range(20)]
        persistent_path = [0] * 10 + [1] * 10
        returns_flip = [rng.gauss(0.0, 0.01) for _ in fast_flip_path]
        returns_persist = [rng.gauss(0.0, 0.01) for _ in persistent_path]

        flip_no_prior = self._diagonal_transition(fast_flip_path, returns_flip, with_prior=False)
        flip_with_prior = self._diagonal_transition(fast_flip_path, returns_flip, with_prior=True)
        persist_no_prior = self._diagonal_transition(
            persistent_path, returns_persist, with_prior=False
        )
        persist_with_prior = self._diagonal_transition(
            persistent_path, returns_persist, with_prior=True
        )

        # Perfectly alternating path has zero observed self-transitions;
        # the prior must pull the estimate up off the floor.
        self.assertAlmostEqual(flip_no_prior, 0.0, places=6)
        self.assertGreater(flip_with_prior, flip_no_prior)

        # An already highly persistent path barely moves under the prior.
        self.assertGreater(persist_no_prior, 0.85)
        self.assertGreater(persist_with_prior, 0.75)

        flip_delta = flip_with_prior - flip_no_prior
        persist_delta = abs(persist_with_prior - persist_no_prior)
        self.assertGreater(flip_delta, persist_delta)


class VarianceFloorTest(unittest.TestCase):
    """A state with very few, nearly-identical observations must have its
    variance clamped at the floor instead of collapsing toward zero."""

    def test_variance_floor_applied(self):
        # State 0: three near-identical observations -> near-zero raw variance.
        # State 1: a normal spread of observations.
        returns = [0.001, 0.0010001, 0.0009999, 0.02, -0.015, 0.01, -0.02, 0.005]
        gamma = [
            [1.0, 0.0],
            [1.0, 0.0],
            [1.0, 0.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
            [0.0, 1.0],
        ]
        xi = [
            [[gamma[t][i] * gamma[t + 1][j] for j in range(2)] for i in range(2)]
            for t in range(len(returns) - 1)
        ]

        var_floor = 1e-6
        _, _, _, var = rh.m_step(returns, gamma, xi, var_floor)

        self.assertEqual(var[0], var_floor)
        self.assertGreater(var[1], var_floor)


class ConfidenceThresholdTest(unittest.TestCase):
    """Heavily overlapping synthetic state distributions must yield
    'Mixed/Uncertain', never a confident Bull/Bear label."""

    def test_overlapping_states_yield_mixed_uncertain(self):
        rng = random.Random(7)
        returns = [rng.gauss(0.0, 0.01) for _ in range(150)]

        # Force fit_best to return two virtually indistinguishable,
        # non-persistent states — isolates the threshold branch in
        # classify() from EM's inherent fitting variance.
        overlapping_fit = (
            [0.5, 0.5],
            [[0.5, 0.5], [0.5, 0.5]],
            [0.0, 0.00001],
            [0.0001, 0.0001],
        )
        with patch.object(rh, "fit_best", return_value=overlapping_fit):
            result = rh.classify(returns)

        self.assertEqual(result["regime"], "Mixed/Uncertain")
        self.assertLess(result["confidence"], rh.CONFIDENCE_THRESHOLD)

    def test_insufficient_history_below_min_obs(self):
        returns = [0.001] * (rh.MIN_OBS - 1)
        result = rh.classify(returns)
        self.assertEqual(result["regime"], "Insufficient History")
        self.assertEqual(result["n_obs"], rh.MIN_OBS - 1)


if __name__ == "__main__":
    unittest.main()
