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

### L-012 — Monitor widened catalyst-freshness window for false positives
- Date: 2026-08-21 | Source: WEEKLY-REVIEW 2026-08-21 (2nd consecutive
  zero-trade week; skip-scoreboard scored COP +8.18% and NEM +15.23% as
  "missed" this review, both passed over solely for lacking a same-day-
  dated catalyst despite genuine, still-live multi-session catalysts;
  missed:avoided ratio 2:1, total missed gains 23.41% vs avoided losses
  10.60%)
- Lesson: The Buy-Side Gate's catalyst-freshness requirement ("dated
  today") was too tight — it left COP and NEM off the book despite real,
  still-live theses, at a combined missed-gains cost of 23.41% this
  review alone. Widened to admit catalysts dated within the prior 2
  trading sessions if two-source confirmed (TRADING-STRATEGY.md, this
  week).
- Directive: At each of the next 2 weekly reviews, note whether any entry
  made under the widened 2-session/two-source catalyst window held up or
  reversed shortly after fill, and whether deployment moves toward the
  75-85% band.
- Status: active | Review-by: 2026-09-04

### L-013 — Broaden stall-breaker sector screen beyond Energy/Materials
- Date: 2026-08-21 | Source: WEEKLY-REVIEW 2026-08-21 (Energy/Materials
  have supplied all 8 watchlist names across the last two stall-breaker
  refresh cycles — Aug 14: MPC/COP/NEM/NUE, Aug 19: XOM/PSX/STLD/MLM —
  with the sector pool showing signs of running out of fresh, undated
  names)
- Lesson: Repeatedly screening only the top-2 YTD sectors risks recycling
  the same names/coverage across refresh cycles rather than surfacing
  genuinely new catalysts.
- Directive: When a refreshed watchlist completes a full re-arm cycle
  (per L-010's 3-session trigger) without producing a gate-clearing
  catalyst, include a 3rd sector (next-highest YTD momentum) in the next
  refresh's screen alongside the top-2.
- Status: active | Review-by: 2026-09-04

### L-009 — Track persistent under-deployment against 75-85% target
- Date: 2026-08-07 | Source: WEEKLY-REVIEW 2026-08-07 Adjustments (portfolio ~58% deployed in a week the S&P gained +3.53%, 4th straight week below the 75-85% band)
- Lesson: The bot has now been below the 75-85% deployment target for 6
  consecutive weeks (Jul 14 - Aug 21). This week's 6-consecutive-week
  checkpoint triggered the L-012 catalyst-freshness gate widening
  (WEEKLY-REVIEW 2026-08-21) — extending this lesson rather than closing
  it out, to track whether deployment actually moves toward the band now
  that the gate calibration has changed.
- Directive: At each weekly review, report consecutive weeks under the
  75-85% deployment band. If deployment has not improved within 3 weeks
  of the L-012 gate change (by 2026-09-11), treat that as evidence the
  gate was not the binding constraint and reconsider watchlist breadth
  or position-sizing pacing instead.
- Status: active | Review-by: 2026-09-04

### L-010 — Stall-breaker refresh timing too late in the week
- Date: 2026-08-14 | Source: WEEKLY-REVIEW 2026-08-14 (zero trades this
  week; the Aug 14 stall-breaker fired on the week's last session, leaving
  zero remaining sessions to act on the refreshed MPC/COP/NEM/NUE
  watchlist)
- Lesson: The stall-breaker's fixed 5-consecutive-no-trade-day trigger
  routinely lands a watchlist refresh on a Thursday/Friday, giving fresh
  names no runway within the same week to clear the buy-side gate.
- Directive: Lower the stall-breaker trigger from 5 to 3 consecutive
  no-trade sessions, so a broadened watchlist screen has more of the week
  left to convert into an entry.
- Status: active | Review-by: 2026-08-28

### L-011 — EOD snapshot balance_asof/settlement mismatches
- Date: 2026-08-14 | Source: WEEKLY-REVIEW 2026-08-14 (recurring pattern:
  Aug 7 missing EOD entry, Aug 13 EOD entry mislabeled with Aug 12 data,
  Aug 10/13/14 logged-vs-Alpaca last_equity discrepancies)
- Lesson: The EOD-snapshot routine has produced three distinct
  data-integrity incidents in two weeks, all traceable to the same root
  cause — the routine reading account state before Alpaca's
  `balance_asof`/`last_equity` has settled to the current session's close.
- Directive: Before logging any EOD snapshot, check the account's
  `balance_asof` field; if it doesn't match today's date, label the entry
  explicitly as provisional/live-pulled rather than committing it as
  today's official settled EOD close.
- Status: active | Review-by: 2026-08-28

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
- L-007, "Monitor skip-scoreboard shift toward missed", retired
  2026-08-14 (hit review-by, not promoted). Already delivered its one
  intended escalation (2026-08-07, leading to the thin-liquidity
  bars-confirmation-window rule), and the 2026-08-14 review's newly-scored
  rows (FANG, VMC) came back skip-right/skip-right with zero missed
  verdicts — no continuation of the trend it tracked. Its monitoring
  function is subsumed by the weekly review's standing skip-scoreboard
  computation (STEP 3) and rule-change escalation path (STEP 5).
- L-008, "Monitor thin-liquidity bars-confirmation window", retired
  2026-08-21 (hit review-by, not promoted). Zero new entries were made
  under the extended 60-minute thin-liquidity window since the original
  Jul 30 GRC case across the full 2-review monitoring cycle — nothing
  further to report, no false-positive evidence either way. The
  underlying TRADING-STRATEGY.md rule (added 2026-08-07) stands
  unchanged; only the monitoring lesson is retired.

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
| 2026-08-04 | FANG | gate-fail: Q2 EPS beat ($6.48 vs $5.96 est) but bars-confirmed NEGATIVE reaction at open (-3.87%, $198.53 -> $190.85) | 198.53 | +1.02% | skip-right |
| 2026-08-05 | VMC | gate-fail: Q2 EPS beat ($2.59 vs $2.50 est) but bars-confirmed reaction faded from +1.47% intraday high ($289.285, 10:15am ET) to +0.49% ($286.47, 2:15pm ET) and still declining — not a clean sustained positive reaction to trade against | 285.08 | -1.83% | skip-right |
| 2026-08-14 | MPC | HOLD — stall-breaker refresh add (Energy), no fresh Aug 14-dated catalyst, recycled Aug 4 Q2 beat/Mizuho pick | 356.67 | +1.10% | skip-right |
| 2026-08-14 | COP | HOLD — stall-breaker refresh add (Energy), no fresh Aug 14-dated catalyst, recycled Q2 beat/CEO transition | 124.72 | +8.18% | missed |
| 2026-08-14 | NEM | HOLD — stall-breaker refresh add (Materials), no fresh Aug 14-dated catalyst, Aug 10 Nevada settlement 4 sessions stale | 114.18 | +15.23% | missed |
| 2026-08-14 | NUE | HOLD — stall-breaker refresh add (Materials), no fresh Aug 14-dated catalyst, recycled Q2 beat/KeyBanc upgrade | 272.49 | -10.60% | avoided-loss |
| 2026-08-19 | XOM | HOLD — stall-breaker refresh add (Energy), no fresh Aug 19-dated catalyst, recycled Q2 beat/Mozambique LNG investment | 165.61 | | |
| 2026-08-19 | PSX | HOLD — stall-breaker refresh add (Energy), no fresh Aug 19-dated catalyst, diesel-margin narrative recycled, same-day insider sale flagged negative | 243.475 | | |
| 2026-08-19 | STLD | HOLD — stall-breaker refresh add (Materials), no fresh Aug 19-dated catalyst, recycled Q2 beat/2026 outlook | 249.85 | | |
| 2026-08-19 | MLM | HOLD — stall-breaker refresh add (Materials), no fresh Aug 19-dated catalyst, recycled Lhoist NA combination/dividend raise | 522.88 | | |
| 2026-08-24 | VST | HOLD — stall-breaker refresh add (Energy), no fresh Aug 24-dated catalyst, recycled Aug 7 Q2 EBITDA beat/AI-power thesis | 136.21 | | |
| 2026-08-24 | CEG | HOLD — stall-breaker refresh add (Energy), no fresh Aug 24-dated catalyst, recycled Aug 6 Q2 beat-and-raise/nuclear PPA wins | 272.83 | | |
| 2026-08-24 | MP | HOLD — stall-breaker refresh add (Materials), no fresh Aug 24-dated catalyst, recycled Aug 6 Q2 beat/gadolinium deal | 60.02 | | |
| 2026-08-24 | AMAT | HOLD — stall-breaker refresh add (Technology, L-013 3rd-sector broadening), no fresh Aug 24-dated catalyst, recycled Aug 13 Q3 beat | 492.12 | | |
| 2026-08-26 | ET | HOLD — stall-breaker refresh add (Energy), no fresh Aug 26-dated catalyst, recycled Aug 6-7 Q2 beat/guidance raise, Mizuho top-midstream-pick call | 21.03 | | |
| 2026-08-26 | FCX | HOLD — stall-breaker refresh add (Materials), no fresh Aug 26-dated catalyst, recycled copper-rally/Q2-beat momentum | 79.895 | | |
| 2026-08-26 | MRVL | HOLD — stall-breaker refresh add (Technology, L-013 3rd-sector), no catalyst yet, reports Thu Aug 27 AMC | 240.38 | | |
| 2026-08-28 | WMB | HOLD — stall-breaker refresh add (Energy), no fresh Aug 28-dated catalyst, Hugh Brinson Phase 1 in-service Sept 1 is a forward event only | 74.19 | | |
| 2026-08-28 | CRM | HOLD — stall-breaker refresh add (Technology), Aug 26-dated Q2 beat/Anthropic-partnership catalyst confirmed but +22.6% Aug 27 reaction already fully realized, chase risk into weekend gap, no clean entry | 252.19 | | |
| 2026-08-28 | CRWD | HOLD — stall-breaker refresh add (Technology), Aug 26-dated Q2 beat catalyst (+fresh Aug 28 Telkom MoU) confirmed but +20.3% Aug 27 reaction already fully realized, chase risk into weekend gap, no clean entry | 227.99 | | |
