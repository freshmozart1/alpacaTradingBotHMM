# Lessons & Decision Scoreboard

Read every pre-market and market-open session. Active directives are
BINDING — each pre-market entry must confirm compliance per lesson.
Keep small: max ~7 active lessons, ~15 open scoreboard rows. Weekly
review retires/promotes/prunes (see weekly-review STEP 4.5).

## Active Lessons

Template:

### L-NNN — <short title>
- Date: YYYY-MM-DD | Source: <WEEKLY-REVIEW date / RESEARCH-LOG date / manual>
- Lesson: <what was observed>
- Directive: <one concrete, checkable instruction>
- Status: active | Review-by: YYYY-MM-DD

### L-007 — Monitor skip-scoreboard shift toward missed
- Date: 2026-07-31 | Source: WEEKLY-REVIEW 2026-07-31 skip scoreboard (3
  missed / 4 skip-right / 1 avoided-loss this week, vs 0 missed / 4
  avoided-loss the prior week)
- Lesson: This week's newly-scored skips shifted meaningfully toward
  "missed" (FCX +7.40%, XOM +3.23%, ECL +5.32%) versus last week's
  all-avoided-loss result, though ECL's move was independently recaptured
  by a same-week buy.
- Directive: At the next weekly review, if the skip-scoreboard verdict mix
  again skews toward missed (missed count > avoided-loss count), escalate
  to a buy-side-gate calibration review per weekly-review STEP 5
  (catalyst-freshness window).
- Status: active | Review-by: 2026-08-14 | Note: triggered 2026-08-07 (1
  missed / 0 avoided-loss, 2nd consecutive missed-skewed week) — escalated
  per directive; see TRADING-STRATEGY.md Rule Changelog for the resulting
  thin-liquidity bars-confirmation-window rule.

### L-008 — Monitor thin-liquidity bars-confirmation window
- Date: 2026-08-07 | Source: WEEKLY-REVIEW 2026-08-07 Adjustments (GRC Jul 30 gate-fail confirmed "missed" +7.84%, root cause was zero bars prints on a thin-liquidity name, not catalyst staleness)
- Lesson: The new 60-minute bars-confirmation window for sub-~50k-volume
  names (TRADING-STRATEGY.md) needs to be checked for false positives —
  a longer window could admit a reaction that later reverses, not just
  catch genuine slow-to-print moves.
- Directive: At each of the next 2 weekly reviews, note whether any entry
  made under the extended thin-liquidity window held up or reversed
  shortly after fill.
- Status: active | Review-by: 2026-08-21

### L-009 — Track persistent under-deployment against 75-85% target
- Date: 2026-08-07 | Source: WEEKLY-REVIEW 2026-08-07 Adjustments (portfolio ~58% deployed in a week the S&P gained +3.53%, 4th straight week below the 75-85% band)
- Lesson: The bot has been below the 75-85% deployment target for 4
  consecutive weeks (Jul 28 - Aug 7), and this week's -4.54% relative gap
  vs the S&P was driven mainly by that under-deployment, not by any bad
  individual decision.
- Directive: At each weekly review, report consecutive weeks under the
  75-85% deployment band; if it reaches 6 consecutive weeks, treat it as
  a signal to review whether the buy-side gate itself (not just watchlist
  breadth) is too conservative.
- Status: active | Review-by: 2026-08-21

## Retired Lessons

- L-001, "XLE/MU Perplexity output unreliable", retired 2026-07-31,
  promoted to a permanent process rule (TRADING-STRATEGY.md Buy-Side Gate)
  after 2+ straight weeks of compliance (2026-07-15 to 2026-07-31) with
  zero fresh incidents.
- L-002, "Verify suspect repeated macro prints", retired 2026-07-31,
  promoted to a permanent process rule (TRADING-STRATEGY.md Buy-Side Gate)
  after 2+ straight weeks of compliance (2026-07-17 to 2026-07-31), with
  the stale VIX print recurring and being correctly flagged every time.
- L-003, "Widen watchlist beyond recycled tickers", retired 2026-07-24,
  promoted to a permanent process rule (TRADING-STRATEGY.md Buy-Side Gate)
  after 2 straight weeks of compliance sustaining the pipeline that
  surfaced KALU's catalyst.
- L-004, "Widen earnings-print verification beyond XLE/MU", retired
  2026-08-07, promoted to a permanent process rule (TRADING-STRATEGY.md
  Buy-Side Gate) after 2+ straight weeks of compliance (2026-07-24 to
  2026-08-07) with zero fresh incidents.
- L-005, "Cross-check extreme oil/WTI source dispersion", retired
  2026-08-07, promoted to a permanent process rule (TRADING-STRATEGY.md
  Buy-Side Gate) after 2+ straight weeks of compliance (2026-07-24 to
  2026-08-07), correctly resolving oil dispersion via XLE/USO bars each
  time it triggered.
- L-006, "Flag same-week ex-div/analyst-action risk at entry", retired
  2026-08-07, promoted to a permanent process rule (TRADING-STRATEGY.md
  Buy-Side Gate) after 2+ straight weeks of compliance (2026-07-24 to
  2026-08-07), checked at every new entry (ECL, CVX, LNG) with zero
  misses.

## Decision Scoreboard

One row per skipped opportunity: a NEW watchlist name (Ref = prior-session
close when added), a trade idea with entry/stop/target that ended HOLD, or
a market-open gate rejection. One row per ticker per watchlist streak, not
per day. Rows are append-once; never rewrite a Ref close. Ref prices from
./scripts/alpaca.sh bars ONLY — never Perplexity. "+5d %" and Verdict are
filled by the weekly review: missed (>= +3% within 5 sessions) /
skip-right (between) / avoided-loss (<= -3%). Rows with verdicts older
than 10 sessions are pruned.

| Date | Ticker | Decision | Ref close | +5d % | Verdict |
|------|--------|----------|-----------|-------|---------|
| 2026-07-20 | LNG | HOLD — Qatar supply-shock claim uncorroborated | 262.60 | -2.52% | skip-right |
| 2026-07-20 | FANG | HOLD — Mizuho PT unconfirmed as today-dated | 195.55 | +0.13% | skip-right |
| 2026-07-20 | VMC | HOLD — dated reaction negative (-2.5%), not a buy trigger | 288.17 | -1.30% | skip-right |
| 2026-07-20 | FCX | HOLD — no dated catalyst, awaiting Jul 23 earnings | 58.37 | +7.40% | missed |
| 2026-07-21 | XOM | HOLD — oil-driven momentum, no fresh dated catalyst | 148.40 | +3.23% | missed |
| 2026-07-21 | CVX | HOLD — oil-driven momentum, no fresh dated catalyst | 189.25 | -0.82% | skip-right |
| 2026-07-21 | ECL | HOLD — no dated catalyst, awaiting Jul 28 earnings | 268.66 | +5.32% | missed (recaptured by later ECL buy Jul 28) |
| 2026-07-22 | GEV | HOLD — reports before today's open, not buyable pre-print | 1077.75 | -16.51% | avoided-loss |
| 2026-07-30 | GRC | HOLD — Q2 beat catalyst, source dating unconfirmed (L-004), pending bars re-check at open | 78.46 | +7.84% | missed |
| 2026-08-04 | FANG | gate-fail: Q2 EPS beat ($6.48 vs $5.96 est) but bars-confirmed NEGATIVE reaction at open (-3.87%, $198.53 -> $190.85) | 198.53 | | |
| 2026-08-05 | VMC | gate-fail: Q2 EPS beat ($2.59 vs $2.50 est) but bars-confirmed reaction faded from +1.47% intraday high ($289.285, 10:15am ET) to +0.49% ($286.47, 2:15pm ET) and still declining — not a clean sustained positive reaction to trade against | 285.08 | | |
| 2026-08-14 | MPC | HOLD — stall-breaker refresh add (Energy), no fresh Aug 14-dated catalyst, recycled Aug 4 Q2 beat/Mizuho pick | 356.67 | | |
| 2026-08-14 | COP | HOLD — stall-breaker refresh add (Energy), no fresh Aug 14-dated catalyst, recycled Q2 beat/CEO transition | 124.72 | | |
| 2026-08-14 | NEM | HOLD — stall-breaker refresh add (Materials), no fresh Aug 14-dated catalyst, Aug 10 Nevada settlement 4 sessions stale | 114.18 | | |
| 2026-08-14 | NUE | HOLD — stall-breaker refresh add (Materials), no fresh Aug 14-dated catalyst, recycled Q2 beat/KeyBanc upgrade | 272.49 | | |
