# Lessons & Decision Scoreboard

Read every pre-market and market-open session. Active directives are
BINDING — each pre-market entry must confirm compliance per lesson.
Keep small: max ~7 active lessons, ~15 open scoreboard rows. Weekly
review retires/promotes/prunes (see weekly-review STEP 4.5).

## Active Lessons

Template:

### L-020 — Partial TRADE-LOG gap (EOD-only day)
- Date: 2026-09-11 | Source: WEEKLY-REVIEW 2026-09-11 (Sep 10 has only an
  EOD Snapshot entry — no Market-Open Check or Midday Scan logged — a
  distinct failure from L-018's full-day/zero-entries criterion, first
  flagged for awareness at Sept 11 pre-market)
- Lesson: A partial gap (EOD-only) is a separate failure mode from a full
  day gap and won't be caught by L-018's "3rd full-day gap" threshold.
- Directive: Before logging the day's first TRADE-LOG entry, verify the
  previous trading session's log has all three expected entries
  (Market-Open, Midday, EOD); if any are missing, log a one-line
  retroactive gap note rather than letting it pass silently.
- Status: active | Review-by: 2026-09-25

### L-019 — Empty stall-breaker sector leg (any leg, not just Materials)
- Date: 2026-09-11 | Source: WEEKLY-REVIEW 2026-09-11 (generalizes retired
  L-016: Materials came up empty Aug 28, Technology came up empty Sep 11 —
  two different legs, several successful cycles apart, so L-016's literal
  "same leg twice" trigger was never met, but the underlying "a leg runs
  dry of fresh catalysts" pattern has now recurred on a 2nd sector)
- Lesson: An empty sector leg on a stall-breaker refresh isn't specific to
  Materials — it can happen to any leg in the current top-N screen when
  that sector's recent movers have already fully realized their catalysts
  or are trending negative.
- Directive: At each stall-breaker refresh, note whether any leg comes up
  empty. If the *same* leg comes up empty on 2 consecutive refresh cycles,
  propose adding a 4th sector or loosening the liquidity/market-cap floor
  for that leg specifically.
- Status: active | Review-by: 2026-09-25

### L-NNN — <short title>
- Date: YYYY-MM-DD | Source: <WEEKLY-REVIEW date / RESEARCH-LOG date / manual>
- Lesson: <what was observed>
- Directive: <one concrete, checkable instruction>
- Status: active | Review-by: YYYY-MM-DD

### L-018 — Recurring full-day TRADE-LOG gap
- Date: 2026-09-04 | Source: WEEKLY-REVIEW 2026-09-04 (Sept 2 has zero
  TRADE-LOG.md entries — Market-Open/Midday/EOD all missing — the 2nd
  full-day logging gap of the challenge after Aug 18; held-position
  quantities confirmed unchanged the next session, so no trade was
  missed, but the logging gap itself recurred)
- Lesson: A full-day gap with no TRADE-LOG entries at all is a distinct
  failure mode from the balance_asof-lag issue L-011 already covers —
  this is the 2nd occurrence (Aug 18, Sept 2), both so far confirmed
  benign against live account state.
- Directive: If a 3rd full-day TRADE-LOG gap occurs, treat it as a
  process problem needing a structural fix (e.g., an explicit
  end-of-day gap-check step comparing today's date against the last
  logged entry) rather than another one-off flag-and-continue.
- Status: active | Review-by: 2026-09-18

### L-017 — Verify company/project ownership before adding a shared-coverage catalyst name
- Date: 2026-09-04 | Source: WEEKLY-REVIEW 2026-09-04 / RESEARCH-LOG
  2026-09-01 (the Aug 28 stall-breaker refresh attributed the Hugh
  Brinson Pipeline Phase 1 full-capacity-by-Sept-1 catalyst to WMB
  (Williams Companies); Sept 1 research corrected this to Energy
  Transfer (ET) — WMB has no connection to the project. The error
  persisted 3 sessions (Aug 28, 31, Sept 1) on an open Decision
  Scoreboard row before being self-caught pre-execution; no trade was
  placed on the false premise)
- Lesson: A catalyst can be genuinely dated and independently confirmed
  by multiple outlets while still being attributed to the wrong ticker,
  when coverage involves a shared pipeline/JV/multi-company project —
  this is a distinct data-quality failure mode from L-001/L-002's
  numeric-print issues.
- Directive: When a watchlist catalyst involves a pipeline, joint
  venture, or multi-company project, explicitly verify which company
  owns/operates the specific asset (via the company's own investor
  materials, not just news aggregator coverage) before adding the name
  to the watchlist or counting the catalyst toward the buy-side gate.
- Status: active | Review-by: 2026-09-18

## Retired Lessons

- L-015, "Track whether chase-risk/deployment cap is the binding
  constraint on deployment", retired 2026-09-11 (hit review-by, not
  promoted). Resolved by evidence, not a rule change: CRWD's Aug 28 skip
  scored avoided-loss (-6.55%, confirmed Sep 4) and IONQ's Sep 8 skip has
  fallen -6.71% (Sep 10 close vs Ref) — two-for-two, both cap-blocked
  names would have lost money if forced through. The 75-85% deployment
  cap is validated as a genuine risk control; hold it as-is with no
  further monitoring needed unless a future cap-blocked, thesis-intact
  setup scores a wide "missed" verdict. No TRADING-STRATEGY.md change —
  the standing deployment band already covers this.
- L-016, "Materials leg empty on stall-breaker refresh", retired
  2026-09-11 (hit review-by, not promoted). Its literal trigger (the
  *same* leg empty on 2 consecutive refresh cycles) was never met —
  Materials recovered by Sep 1 (CRH added), and Sep 11's empty leg was
  Technology instead, a different sector several cycles later. Superseded
  by new lesson L-019, which generalizes the same tracking logic to any
  leg. No TRADING-STRATEGY.md change.
- L-014, "Re-evaluate CRM/CRWD for a pullback entry", retired 2026-09-08
  (hit review-by, directive fully executed, not promoted). Neither name
  set up the called-for clean pullback/consolidation entry across the
  full 5-session window (Sep 1, 2, 3, 4, 8): CRM extended further above
  its $250-253 zone with no pullback, and CRWD fell below its $225-230
  zone on continued chop (Sept 2-4 range $203.405-$218.295) rather than
  tightening into it. Per the lesson's own directive, both were dropped
  from the watchlist at the Sept 8 stall-breaker refresh. No
  TRADING-STRATEGY.md change — this was a one-off name-specific watch,
  not a process rule candidate.

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
- L-010, "Stall-breaker refresh timing too late in the week", retired
  2026-08-28, promoted to a permanent process rule (TRADING-STRATEGY.md
  Buy-Side Gate, re-arm trigger 5+ -> 3+ sessions) after 2 straight weeks
  of compliance (2026-08-14 to 2026-08-28) with zero fresh incidents —
  correctly re-armed and refreshed the watchlist 3 times this cycle
  (Aug 24, 26, 28).
- L-011, "EOD snapshot balance_asof/settlement mismatches", retired
  2026-08-28, promoted to a permanent process rule (TRADING-STRATEGY.md,
  new Operational Rules section) after 2 straight weeks of compliance
  (2026-08-14 to 2026-08-28) with zero fresh mislabeling/mismatch
  incidents.
- L-013, "Broaden stall-breaker sector screen beyond Energy/Materials",
  retired 2026-09-04, promoted to a permanent process rule
  (TRADING-STRATEGY.md Buy-Side Gate) after 2+ straight weeks of
  compliance (2026-08-21 to 2026-09-04) — every refresh cycle (Aug 24,
  26, 28, Sept 1) screened a 3rd sector alongside Energy/Materials,
  surfacing AMAT, MRVL, and CRH, with zero fresh incidents.
- L-009, "Track persistent under-deployment against 75-85% target",
  retired 2026-09-04 (hit review-by, not promoted). Deployment reached
  and held the 75-85% band for 5 straight sessions (Sept 1-4,
  78.75%-78.94%), resolving the tracking question well inside the
  2026-09-11 deadline. No TRADING-STRATEGY.md change — the 75-85% band
  is already a standing rule; only the monitoring lesson retires.
- L-012, "Monitor widened catalyst-freshness window for false
  positives", retired 2026-09-04 (hit review-by, not promoted). Zero new
  entries were made under the widened 2-session/two-source window across
  the full 2-review monitoring cycle (Sept 1's ET was same-day-dated and
  didn't need the widening) — nothing to report, no false-positive
  evidence either way. The underlying TRADING-STRATEGY.md rule (added
  2026-08-21) stands unchanged; only the monitoring lesson retires.

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
| 2026-08-19 | XOM | HOLD — stall-breaker refresh add (Energy), no fresh Aug 19-dated catalyst, recycled Q2 beat/Mozambique LNG investment | 165.61 | -5.38% | avoided-loss |
| 2026-08-19 | PSX | HOLD — stall-breaker refresh add (Energy), no fresh Aug 19-dated catalyst, diesel-margin narrative recycled, same-day insider sale flagged negative | 243.475 | +0.25% | skip-right |
| 2026-08-19 | STLD | HOLD — stall-breaker refresh add (Materials), no fresh Aug 19-dated catalyst, recycled Q2 beat/2026 outlook | 249.85 | -6.05% | avoided-loss |
| 2026-08-19 | MLM | HOLD — stall-breaker refresh add (Materials), no fresh Aug 19-dated catalyst, recycled Lhoist NA combination/dividend raise | 522.88 | +1.54% | skip-right |
| 2026-08-24 | VST | HOLD — stall-breaker refresh add (Energy), no fresh Aug 24-dated catalyst, recycled Aug 7 Q2 EBITDA beat/AI-power thesis | 136.21 | +0.65% | skip-right |
| 2026-08-24 | CEG | HOLD — stall-breaker refresh add (Energy), no fresh Aug 24-dated catalyst, recycled Aug 6 Q2 beat-and-raise/nuclear PPA wins | 272.83 | +1.47% | skip-right |
| 2026-08-24 | MP | HOLD — stall-breaker refresh add (Materials), no fresh Aug 24-dated catalyst, recycled Aug 6 Q2 beat/gadolinium deal | 60.02 | -6.50% | avoided-loss |
| 2026-08-24 | AMAT | HOLD — stall-breaker refresh add (Technology, L-013 3rd-sector broadening), no fresh Aug 24-dated catalyst, recycled Aug 13 Q3 beat | 492.12 | -6.22% | avoided-loss |
| 2026-08-26 | ET | HOLD — stall-breaker refresh add (Energy), no fresh Aug 26-dated catalyst, recycled Aug 6-7 Q2 beat/guidance raise, Mizuho top-midstream-pick call | 21.03 | +2.35% | skip-right (moot — bot independently bought ET Sept 1) |
| 2026-08-26 | FCX | HOLD — stall-breaker refresh add (Materials), no fresh Aug 26-dated catalyst, recycled copper-rally/Q2-beat momentum | 79.895 | -7.45% | avoided-loss |
| 2026-08-26 | MRVL | HOLD — stall-breaker refresh add (Technology, L-013 3rd-sector), no catalyst yet, reports Thu Aug 27 AMC | 240.38 | -14.06% | avoided-loss |
| 2026-08-28 | WMB | HOLD — stall-breaker refresh add (Energy), no fresh Aug 28-dated catalyst, Hugh Brinson Phase 1 in-service Sept 1 is a forward event only | 74.19 | -0.03% | skip-right |
| 2026-08-28 | CRM | HOLD — stall-breaker refresh add (Technology), Aug 26-dated Q2 beat/Anthropic-partnership catalyst confirmed but +22.6% Aug 27 reaction already fully realized, chase risk into weekend gap, no clean entry | 252.19 | +2.82% | skip-right |
| 2026-08-28 | CRWD | HOLD — stall-breaker refresh add (Technology), Aug 26-dated Q2 beat catalyst (+fresh Aug 28 Telkom MoU) confirmed but +20.3% Aug 27 reaction already fully realized, chase risk into weekend gap, no clean entry | 227.99 | -6.55% | avoided-loss |
| 2026-09-01 | ET | TRADE FLAGGED — stall-breaker refresh re-add (Energy), Hugh Brinson Pipeline Phase 1 full-capacity milestone target-dated today (Sept 1), correctly re-attributed from WMB; entry ~$21.55/stop ~$19.61/target ~$25.43; flagged for market-open re-validation, not yet executed | 21.51 | | |
| 2026-09-01 | TRGP | HOLD — stall-breaker refresh add (Energy), Permian NGL-export/volume-growth coverage, no fresh Sept 1-dated catalyst | 294.22 | -0.92% | skip-right |
| 2026-09-01 | AAPL | HOLD — stall-breaker refresh add (Technology), CEO transition to John Ternus effective today but well-telegraphed/orderly, not clearly directional; Sept 9 iPhone event is the more meaningful forward catalyst | 317.14 | -0.54% | skip-right (mechanical +5-session window closed same-day as the Sept 9 event, before its reaction showed up Sept 10-11 — see WEEKLY-REVIEW 2026-09-11 note) |
| 2026-09-01 | CRH | HOLD — stall-breaker refresh add (Materials, L-013 3-sector screen), Wells Fargo Buy reiterated $135 PT but recycled from a June-dated note, no fresh Sept 1-dated catalyst | 94.33 | -5.29% | avoided-loss |
| 2026-09-08 | IONQ | HOLD — stall-breaker refresh add (Technology), Investor Day today (Sept 8) is a genuine, hard-dated, gate-clearing catalyst, but blocked purely by the 75-85% deployment cap at 78.68% deployed (L-015) | 39.52 | | |
| 2026-09-08 | NEE | HOLD — stall-breaker refresh add (Energy), Dominion merger shareholder approval/DOE Duane Arnold loan both recycled, no fresh Sept 8-dated catalyst | 83.42 | | |
| 2026-09-08 | UEC | HOLD — stall-breaker refresh add (Energy), Burke Hollow/Sweetwater/Christensen Ranch coverage all recycled from late Aug, no fresh Sept 8-dated catalyst | 11.515 | | |
| 2026-09-11 | COP | HOLD — stall-breaker refresh add (Energy), 52-week high/+45% YTD momentum, Goldman dividend-energy mention, no fresh Sept 11-dated catalyst | 137.07 | | |
| 2026-09-11 | VLO | HOLD — stall-breaker refresh add (Energy), Zacks top-oil-stock screen, refining-margin momentum, no fresh Sept 11-dated catalyst | 385.37 | | |
| 2026-09-11 | PARR | HOLD — stall-breaker refresh add (Energy), high-beta systematic-ranking pick, thin liquidity (~25-45k avg daily volume), no fresh Sept 11-dated catalyst | 83.63 | | |
