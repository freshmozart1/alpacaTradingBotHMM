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

### L-004 — Widen earnings-print verification beyond XLE/MU
- Date: 2026-07-24 | Source: WEEKLY-REVIEW 2026-07-24 Adjustments (GRC Jul 24 earnings misattribution)
- Lesson: Perplexity misattributed a 2025-dated GRC earnings print as
  today's Jul 24 2026 result — the same stale-source-as-fresh-data failure
  mode already tracked for XLE/MU under L-001, just on a different ticker.
- Directive: No earnings-print claim (any ticker) counts toward the
  buy-side gate unless the source snippet's own date matches today, or the
  print is confirmed via `alpaca.sh bars`/quote post-release.
- Status: active | Review-by: 2026-08-07

### L-005 — Cross-check extreme oil/WTI source dispersion
- Date: 2026-07-24 | Source: WEEKLY-REVIEW 2026-07-24 Adjustments (Jul 24 WTI $70-71 vs Jul 22-23 $86-90 dispersion)
- Lesson: Oil price reads swung >15% across sources/sessions with no
  resolution, undermining the Energy/Materials sector-momentum thesis
  behind several watchlist names.
- Directive: When WTI/Brent cross-source dispersion exceeds ~10% in a
  single session, cross-check via `alpaca.sh bars` on a liquid oil proxy
  (USO/XLE) before treating either cluster as the operative read.
- Status: active | Review-by: 2026-08-07

### L-006 — Flag same-week ex-div/analyst-action risk at entry
- Date: 2026-07-24 | Source: WEEKLY-REVIEW 2026-07-24 Adjustments (KALU stopped out after downgrade + ex-div + profit-taking stacked within 24h of entry)
- Lesson: KALU's entry had three negative-for-price events land within a
  day of the fill (Wells Fargo downgrade, ex-dividend, profit-taking) —
  none were flagged at entry because the checklist only checks the
  headline catalyst.
- Directive: At market-open re-validation for any new entry, explicitly
  check for a same-week ex-dividend date or a recent/pending analyst
  action and note it in the trade log, even if it doesn't block entry.
- Status: active | Review-by: 2026-08-07

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
- Status: active | Review-by: 2026-08-14

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
| 2026-07-10 | MU | HOLD — single-day breakout, gate needs dated catalyst | 979.36 | -13.26% | avoided-loss |
| 2026-07-20 | LNG | HOLD — Qatar supply-shock claim uncorroborated | 262.60 | -2.52% | skip-right |
| 2026-07-20 | FANG | HOLD — Mizuho PT unconfirmed as today-dated | 195.55 | +0.13% | skip-right |
| 2026-07-20 | VMC | HOLD — dated reaction negative (-2.5%), not a buy trigger | 288.17 | -1.30% | skip-right |
| 2026-07-20 | FCX | HOLD — no dated catalyst, awaiting Jul 23 earnings | 58.37 | +7.40% | missed |
| 2026-07-21 | XOM | HOLD — oil-driven momentum, no fresh dated catalyst | 148.40 | +3.23% | missed |
| 2026-07-21 | CVX | HOLD — oil-driven momentum, no fresh dated catalyst | 189.25 | -0.82% | skip-right |
| 2026-07-21 | ECL | HOLD — no dated catalyst, awaiting Jul 28 earnings | 268.66 | +5.32% | missed (recaptured by later ECL buy Jul 28) |
| 2026-07-22 | GEV | HOLD — reports before today's open, not buyable pre-print | 1077.75 | -16.51% | avoided-loss |
| 2026-07-30 | GRC | HOLD — Q2 beat catalyst, source dating unconfirmed (L-004), pending bars re-check at open | 78.46 | | |
| 2026-08-04 | FANG | gate-fail: Q2 EPS beat ($6.48 vs $5.96 est) but bars-confirmed NEGATIVE reaction at open (-3.87%, $198.53 -> $190.85) | 198.53 | | |
| 2026-08-05 | VMC | gate-fail: Q2 EPS beat ($2.59 vs $2.50 est) but bars-confirmed reaction faded from +1.47% intraday high ($289.285, 10:15am ET) to +0.49% ($286.47, 2:15pm ET) and still declining — not a clean sustained positive reaction to trade against | 285.08 | | |
