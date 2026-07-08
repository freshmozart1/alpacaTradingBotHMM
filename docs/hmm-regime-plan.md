# Implementation Plan: HMM Market-Regime Classification

Status: **plan only — not implemented.** This document records the agreed
design for adding a Hidden Markov Model (HMM) market-regime classifier to the
bot. Nothing in this plan has been built yet; it exists so the eventual
implementation follows a reviewed design instead of ad-hoc choices.

## Context

The bot currently has no quantitative market-context signal beyond what
Perplexity research returns as prose (a VIX level, sector-momentum commentary).
The goal is an additional, statistically grounded context filter: a daily
classification of the SPY market regime (Bull/Calm vs. Bear/High-Vol) via a
Hidden Markov Model, fed into the pre-market routine and — after an observation
period — allowed to *tighten* (never loosen) the existing strategy rules as
advisory context, never as a standalone entry/exit trigger.

The core constraint shaping this whole design: the execution environment is a
container that clones the repo fresh on every routine run. There is no Python
application code in the repo today (only `scripts/*.sh` wrappers), no package
manager (no `requirements.txt`, no pip-install step in any routine), and
`numpy`/`hmmlearn` are confirmed not preinstalled. Installing compiled Python
extensions fresh on every run, or vendoring a prebuilt binary, was already
rejected as fragile (network/time overhead, platform/glibc mismatch risk).
Instead: a hand-written, pure Python stdlib implementation of a Gaussian HMM
(Baum-Welch + Viterbi) that runs with zero install step in any Python 3
container.

Main risk: a noisy regime signal (frequent flip-flopping, low confidence,
sensitivity to single-day outliers) could provoke whipsaw-like behavior and
undermine the "patience > activity" rule. The design counters this with a
persistence prior in the transition matrix, a minimum-confidence threshold
before reporting any non-neutral regime, and a hard separation between (a)
logging/shadow mode and (b) actually influencing trading rules — Phase B is
only unlocked after several weeks of observing Phase A.

Decisions already made: 2 hidden states, output as a bullet in
`RESEARCH-LOG.md` (no new memory file), purely qualitative (non-numeric)
strategy influence, and the plan covers both phases (logging now, gating
strategy rules later) but Phase B is explicitly gated behind a shadow-mode
observation period rather than shipped in the same change as Phase A.

---

## Phase A — data pipeline, model, logging (buildable now)

### A1. New `bars` subcommand in `scripts/alpaca.sh`

Follows the existing case-statement pattern (reuses `$DATA`/`$H_KEY`/`$H_SEC`),
inserted before the `*)` fallback case:

```bash
  bars)
    sym="${1:?usage: bars SYM [TIMEFRAME] [START] [END]}"
    timeframe="${2:-1Day}"
    start="${3:-}"
    end="${4:-}"
    url="$DATA/stocks/$sym/bars?timeframe=$timeframe&limit=10000&adjustment=all&feed=iex"
    [[ -n "$start" ]] && url="$url&start=$start"
    [[ -n "$end" ]] && url="$url&end=$end"
    curl -fsS -H "$H_KEY" -H "$H_SEC" "$url"
    ;;
```

- Update the usage line in the `*)` fallback case to include `bars`.
- `adjustment=all` for split-/dividend-adjusted closes.
- `feed=iex` assumed for now (free/paper data plan) — verify against the
  actual Alpaca data plan before going live.
- Lookback capped at **504 trading days (~2 calendar years)** — long enough to
  very likely contain a real drawdown/vol episode (2018 Q4, 2020, and 2022 all
  fall within a 2-year lookback from any later point), short enough to stay
  within a single Alpaca bars response (no pagination handling needed) and to
  avoid baking in stale regime statistics (e.g. 2008-era volatility).

### A2. New module `scripts/regime_hmm.py`

Pure stdlib Python (only `math`, `json`, `random`, `sys`), ~100-150 lines.
Reads Alpaca `bars` JSON from stdin, writes a single line of JSON to stdout.

**Feature:** univariate log returns `r_t = ln(c_t / c_{t-1})` from the closes.
No second feature (volatility) in v1 — the per-state variance of the Gaussian
emission model already implicitly captures volatility clustering; a 2D
feature would require covariance-matrix handling (inversion, determinant,
positive-definiteness) in pure Python with no clear benefit for what is meant
to be a pure context signal.

**States:** 2 (higher mean = "Bull", lower/more negative = "Bear/High-Vol").

**Core building blocks:**
- Log-space forward-backward (log-sum-exp trick) — needed to avoid underflow
  over ~500 observations without numpy.
- M-step transition-matrix update with a Dirichlet-style pseudo-count prior
  (diagonal pseudo-count ≈ 8, off-diagonal ≈ 1) — the concrete persistence
  mechanism against whipsaw/flip noise.
- Variance floor (≈5% of global variance) against variance collapse under EM
  degeneracy.
- Multiple random restarts (e.g. 8) with a **fixed seed** (not wall-clock) —
  deterministic output for identical input, important for debugging/tests in
  a setup that refits from scratch every run.
- Viterbi decoding over the entire lookback window; "current regime" and
  "days in current regime" are read off the tail of the decoded path.
- **No parameter persistence between runs.** Every run refits completely over
  the full lookback window — matches the stateless-container model, no risk
  of stale/drifting parameters.
- Confidence = posterior probability (gamma) of the MAP state at the final
  time step. Threshold **0.65**: below it, output `"Mixed/Uncertain"` instead
  of a regime label.
- Minimum data requirement (`MIN_OBS ≈ 100`): below it, `"Insufficient
  History"`.
- All three "no clear signal" cases (`Unavailable` on fetch failure,
  `Insufficient History`, `Mixed/Uncertain`) are treated identically
  downstream as neutral — a single fail-open path.

Example output (stdout, one line of JSON):
```json
{"regime": "Bull", "confidence": 0.78, "days_in_regime": 12, "n_obs": 504}
```

### A3. Integration into `routines/pre-market.md` and `.claude/commands/pre-market.md`

New **STEP 3.5** in both variants, between the Perplexity research (STEP 3)
and writing the research-log entry (STEP 4):

```
STEP 3.5 — Market regime classification (HMM, SPY, 2y daily):
END=$(date +%Y-%m-%d)
START=$(date -d "730 days ago" +%Y-%m-%d)
BARS_JSON=$(./scripts/alpaca.sh bars SPY 1Day "$START" "$END") || BARS_JSON=""
if [[ -n "$BARS_JSON" ]]; then
  REGIME_OUT=$(echo "$BARS_JSON" | python3 scripts/regime_hmm.py) || REGIME_OUT='{"regime":"Unavailable"}'
else
  REGIME_OUT='{"regime":"Unavailable"}'
fi
```

- Runs in **both** variants (cloud routine and local command) — read-only,
  same risk profile as the Perplexity calls the local command already runs.
  The local command doesn't commit anything anyway; the regime bullet is just
  one more line in the uncommitted `RESEARCH-LOG.md` draft left on disk for
  review.
- Error handling: an `alpaca.sh` failure (network, auth, rate limit) →
  `Unavailable`; too little history → `Insufficient History` (detected by
  `regime_hmm.py` itself); low confidence → `Mixed/Uncertain`. None of these
  cases abort the routine — STEP 4 simply logs the neutral status.

No `bars`/HMM call in `weekly-review.md` — that would only add ~5 more trading
days to a 2-year window (marginal) and would be redundant since the week has
already been logged daily; the weekly-review prose sections ("What
Worked"/"Adjustments") can instead reference the already-logged daily bullets
(e.g. "regime flipped 3x this week, mostly below the confidence threshold").

### A4. New bullet in `memory/RESEARCH-LOG.md`

In both the template block and STEP 4 of both `pre-market.md` variants: a new
bullet line in the existing `### Market Context` section, right after
`- Sector momentum:` (matches the existing `VIX:` bullet convention — no new
table, no new file):

```
- Market regime (HMM): Bull (confidence 78%, day 12 of run; SPY, 2y lookback)
```
or, in the neutral case:
```
- Market regime (HMM): Mixed/Uncertain (confidence 54%) — treated as neutral, no rule adjustment
```

Since no new file is introduced, **no** changes are needed to
`memory/PROJECT-CONTEXT.md`'s "Key Files" list or `CLAUDE.md`'s
"Read-Me-First" list.

### A5. Tests

New `tests/test_regime_hmm.py` (stdlib `unittest`, run via
`python3 -m unittest discover tests`), dev-time only — no routine runs tests:
- Hand-built toy HMM (2 states, T=4-6 observations), ground truth via
  brute-force enumeration of all 2^T paths (log-likelihood, Viterbi MAP path,
  posterior gammas) — compared against the DP implementation.
- Log-space vs. naive-space agreement on a moderate-length synthetic sequence.
- Persistence-prior effect: fast-flipping vs. persistent synthetic state
  sequence, comparing the estimated diagonal transition probability with and
  without the prior.
- Variance-floor safeguard for a state with very few, nearly identical
  observations.
- Confidence-threshold branch: heavily overlapping synthetic state
  distributions → output must be `Mixed/Uncertain`.

A one-off, non-recurring cross-check against a reference implementation:
locally, in a throwaway venv, `pip install numpy hmmlearn`, fit on the same
SPY returns, compare decoded state sequences/log-likelihoods against the
hand-rolled implementation. Development-time only — never runs in the routine
container, never becomes a repo dependency.

### A6. Historical sanity check (one-off, manual)

Pull 15-20 years of SPY history via the new `bars` subcommand (a one-off local
scratch run, not a routine), run the decoder, and visually check whether
High-Vol/Bear states line up with known windows: Sep 2008-Mar 2009, Aug 2011,
Aug 2015-Feb 2016, Q4 2018, Feb-Mar 2020, 2022. Qualitative, not automated.

### A7. Shadow-mode period

After A1-A6 ship: **3-4 full trading weeks (15-20 trading days)** of
observation. The regime classifier runs and logs, but has **no** connection to
the buy-side gate or the deployment target. This aligns with 3-4
weekly-review cycles as natural checkpoints: is the label stable (no daily
flipping)? Does confidence usually clear or usually miss the threshold? Does
the label look plausible in hindsight against that week's actual price
action?

---

## Phase B — activating it as a strategy filter (after the shadow-mode gate)

**Precondition:** Phase A must have run for at least 3-4 weeks without
noticeable whipsaw behavior before this step is implemented. This is a
separate implementation step, not an automatic follow-on to Phase A.

New subsection in `memory/TRADING-STRATEGY.md`, inserted after "Core Rules"
and before "Buy-Side Gate" — deliberately **not** a new numbered Core Rule and
**not** a new Buy-Side Gate check, so it doesn't imply the same mechanical
force:

```markdown
## Market Regime Filter (Advisory)

A daily HMM-based regime read (SPY, log-return, 2-state) is logged each
morning in RESEARCH-LOG.md's Market Context section. It is a contextual
filter only — it never overrides, bypasses, or loosens any Core Rule or
Buy-Side Gate check above. Apply it as follows:

- Regime = Bull, confidence >= 65%: no adjustment. Rules apply as written.
- Regime = Bear/High-Vol, confidence >= 65%:
  - Treat the 75-85% deployment band (Core Rule #2) as a ceiling to lean
    away from, not a target to fill — prefer the low end of the range
    rather than stretching toward the high end. This never raises the
    ceiling and never forces deployment below what existing positions
    and their stops already require.
  - Raise the bar for what counts as a "specific catalyst" in the
    Buy-Side Gate and Entry Checklist: a broad sector-momentum or
    macro-only catalyst is not sufficient in this regime — require a
    company-specific, dated catalyst (earnings, guidance change,
    regulatory event, M&A, etc.). This is a qualitative judgment the
    agent applies when documenting the catalyst; it does not add,
    remove, or change any of the 7 existing Buy-Side Gate checks.
- Regime = Mixed/Uncertain, Insufficient History, or Unavailable
  (confidence < 65%, or the classifier could not run): no adjustment.
  Fail open — behave exactly as if this section did not exist.

This filter never: increases the position or trade-count caps (Core
Rules 3, 8), forces a trade, bypasses any Buy-Side Gate check, loosens
the -7% stop-loss rule (Core Rule 5), or overrides trailing-stop
mechanics (Core Rules 4, 6, 7).
```

Purely qualitative/advisory (per user decision) — no hard numeric deployment
cap. No change needed to `market-open.md`/`midday.md` control flow; the agent
reads this subsection while checking the buy-side gate (STEP 1 of every
routine already reads all of `TRADING-STRATEGY.md`).

---

## Files affected

**Phase A:**
- `scripts/alpaca.sh` — new `bars` subcommand
- `scripts/regime_hmm.py` — new, pure Python stdlib implementation
- `routines/pre-market.md` — new STEP 3.5
- `.claude/commands/pre-market.md` — new STEP 3.5
- `memory/RESEARCH-LOG.md` — template block extended with the new bullet
- `tests/test_regime_hmm.py` — new, dev-time only

**Phase B (separate, after the shadow-mode gate):**
- `memory/TRADING-STRATEGY.md` — new "Market Regime Filter (Advisory)" subsection

---

## Open points to fine-tune before/during implementation

These are defaults with a stated rationale, but genuinely tunable — not
blockers to starting, but points to revisit during/after shadow mode against
real data:

- Exact confidence threshold (default 0.65).
- Exact lookback length (default 504 trading days / ~2 years; 3 years would be
  a defensible alternative but would require pagination handling in the
  `bars` subcommand).
- Retrain cadence (default: refit completely on every pre-market run, no
  persistence; an alternative would be a less frequent refit, e.g. Mondays
  only).
- Persistence-prior strength (diagonal pseudo-count ≈8, off-diagonal ≈1) and
  variance floor (≈5% of global variance) — plausible starting values without
  a principled derivation.
- Exact shadow-mode window length (default 3-4 weeks) — can be extended if the
  first weeks still look unstable.

## Verification after implementation

- `python3 -m unittest discover tests` must be green (Baum-Welch/Viterbi
  against toy ground truth).
- Manual run: `./scripts/alpaca.sh bars SPY 1Day <start> <end> | python3
  scripts/regime_hmm.py` returns valid JSON with a plausible label.
- A local `/pre-market` run (`.claude/commands/pre-market.md`) produces an
  uncommitted `RESEARCH-LOG.md` diff containing the new regime bullet,
  correctly formatted, in the `### Market Context` section — check the diff
  manually, then discard it (a local run never commits).
- The one-off historical sanity check (A6) against known bear/vol periods
  performed and documented before the end of the shadow-mode phase.
