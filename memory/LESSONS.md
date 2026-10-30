# Lessons & Decision Scoreboard

Read every pre-market and market-open session. Active directives are
BINDING — each pre-market entry must confirm compliance per lesson.
Keep small: max ~7 active lessons, ~15 open scoreboard rows. Weekly
review retires/promotes/prunes (see weekly-review STEP 4.5).

## Active Lessons

### L-042 — Alert every missing or late routine run the same session
- Date: 2026-10-30 | Source: WEEKLY-REVIEW 2026-10-30 (Oct 26 midday
  missing — Oct 27 pre-market logged "no alert needed"; Oct 27
  pre-market late; Oct 30 pre-market committed after market-open)
- Lesson: The Operational Rule alert was skipped once and late runs were
  absorbed inline without escalation.
- Directive: Whenever any routine finds a prior/same-day routine commit
  missing or out of order, send one ClickUp alert naming it that session
  and log "alerted" in the entry; review counts incidents vs alerts.
- Status: active | Review-by: 2026-11-13

### L-041 — Keep a fully-specified next-slot candidate while 6/6
- Date: 2026-10-30 | Source: WEEKLY-REVIEW 2026-10-30 (zero-trade week,
  book full all 5 sessions; LLY slot-blocked +9.79% Oct 28->30; LMT stop
  cushion ~2.1%)
- Lesson: A stop-out frees a slot with no pre-vetted refill; the
  research burden lands on one rushed market-open.
- Directive: At every pre-market while at 6 positions, name one
  next-slot candidate with two-source dated catalyst, base/chase %,
  sector + theme post-fill caps, entry, stop, size; if none qualifies,
  log why. Process only — no rotation (L-040), gate still decides.
- Status: active | Review-by: 2026-11-13

### L-040 — Log slot-blocked candidates while the book is full
- Date: 2026-10-23 | Source: WEEKLY-REVIEW 2026-10-23 (6/6 positions,
  84.56% deployed after DGX Oct 23; no rotation rule exists)
- Lesson: A full book can hide gate-clearing ideas and invite forced
  rotation.
- Directive: While at 6 positions, log any gate-clearing candidate as a
  "slot-blocked" HOLD scoreboard row; never exit a held name to make
  room unless it hits a sell-side rule (-7%, thesis break, sector exit,
  stop).
- Status: active | Review-by: 2026-11-06

### L-039 — Score chase/fade skips from the skip-time price
- Date: 2026-10-23 | Source: WEEKLY-REVIEW 2026-10-23 (CLF +14.37% and
  IRON +31.13% vs Ref interim, but -2.66% / -5.53% from the price
  available at the skip)
- Lesson: Ref-based scoring counts the pre-skip move as a miss.
- Directive: For every chase or fade skip, log the skip-time price in
  the scoreboard Decision cell; at review report +5d % from both Ref and
  skip price.
- Status: active | Review-by: 2026-11-06

### L-038 — Shadow-score the [no-cat] sector-momentum spec
- Date: 2026-10-23 | Source: WEEKLY-REVIEW 2026-10-23 (L-037 draft:
  1/2 historical misses captured, 0 triggers in 5 daily re-scores Oct
  19-23; VLO reversed -5.70% this week)
- Lesson: n=2 is too thin to add an entry path; refiners rolled over
  right after the misses.
- Directive: At every pre-market, run the L-037 spec (RESEARCH-LOG Oct
  19) on each open [no-cat] row and the top-2 sector leaders; log
  trigger/no-trigger and, for triggers, the +5d result from trigger
  close. No live entries. Adopt only with >=4 triggers and hits >
  losses at a review.
- Status: active | Review-by: 2026-11-06

### L-036 — Log gap-through slippage on every exit
- Date: 2026-10-16 | Source: WEEKLY-REVIEW 2026-10-16 (MRVL cut at
  -10.14% vs -7% line; AVGO trail filled ~$337.13 vs $342.756 stop —
  both gapped overnight on AI-semis selloff)
- Lesson: Overnight gaps in correlated selloffs turn -7% into -10%.
- Directive: For every exit, log fill vs. cut/stop level (% slippage)
  in TRADE-LOG; at each review report total slippage. Measurement only —
  no change to the -7% cut or trails.
- Status: active | Review-by: 2026-11-13 (extended 2026-10-30: zero
  exits Oct 16-30, no slippage data; LMT 5% trail ~2.1% cushion — first
  exit likely soon)

Template:

### L-NNN — <short title>
- Date: YYYY-MM-DD | Source: <WEEKLY-REVIEW date / RESEARCH-LOG date / manual>
- Lesson: <what was observed>
- Directive: <one concrete, checkable instruction>
- Status: active | Review-by: YYYY-MM-DD

## Retired Lessons

- L-035, "Cap same-theme (sub-industry) exposure at 25% of equity",
  retired 2026-10-30, promoted to a permanent Buy-Side Gate rule after 2
  straight weeks of compliance (Oct 16-30; RTX sized, NOC/XOM blocked).
- L-031, "Renew expiring GTC trailing stops mechanically", retired
  2026-10-30, promoted to a permanent Operational Rule (fired once: ECL
  renewal Oct 20; all stops now exp Jan 2027).

- L-032, "Cap combined single-sector exposure at 40% of equity",
  retired 2026-10-23, promoted to a permanent Buy-Side Gate rule after 2
  straight weeks of compliance (Oct 9-23; CLF, RTX, HAL, DGX checks).
- L-034, "Track sector-momentum skips that lack a company catalyst",
  retired 2026-10-23, promoted to a permanent Operational Rule ([no-cat]
  tag) after 2 weeks of compliance; subset 2 missed : 0 avoided.
- L-033, "Monitor the tightened 2-session freshness window", retired
  2026-10-23 (hit review-by, not promoted). One [3-5s]-type case (NOC,
  +8.05% interim) — blocked by L-030/L-035 regardless. Window stays 2.
- L-037, "Draft a bounded [no-cat] sector-momentum entry path", retired
  2026-10-23 — draft written/scored (1/2 captured, 0 FP, n=2); no gate
  change. Shadow-tracked under L-038.

- L-029, "Dividend-adjust the pre-catalyst base around ex-div dates",
  retired 2026-10-16, promoted to a permanent Buy-Side Gate rule after 2
  straight weeks of compliance (Oct 2-16; BMY, MRVL, LMT checks).
- L-030, "Cap single-sector concentration at 2 positions", retired
  2026-10-16, promoted to a permanent Buy-Side Gate rule after 2 straight
  weeks of compliance; the 2 Tech names it allowed (AVGO, MRVL) both
  failed within 3 sessions — sub-industry follow-up under L-035.

- L-025, "Monitor the widened 5-session freshness window for false
  positives", retired 2026-10-09 — its own trigger fired: BMY (3-session
  extension entry) cut at -7.51% inside its 5-session window; NTRA (4
  sessions) -4.62%, AVGO add (3 sessions) -1.18%. Window tightened back
  5 -> 2 sessions in TRADING-STRATEGY.md; follow-up under L-033.
- L-026, "Measure the 15% chase bar from the pre-catalyst close",
  retired 2026-10-09, promoted to a permanent Buy-Side Gate rule after 2
  straight weeks of compliance (Sep 25-Oct 9; NTRA, BMY, AVGO, MRVL).
- L-027, "Force a fully-specified candidate while under-deployed",
  retired 2026-10-09, promoted to a permanent Buy-Side Gate rule after 2
  straight weeks of compliance; produced NTRA (Sep 28) and the AVGO add
  (Oct 6, deployment 66.65% -> 78.9%).
- L-028, "Alert on missing routine commits", retired 2026-10-09,
  promoted to a permanent Operational Rule after 2 straight weeks of
  compliance; caught the missing Oct 8 midday run (alerted Oct 9).

- L-021, "Verify analyst PT/rating actions have a findable dated
  source", retired 2026-10-02, promoted to a permanent Buy-Side Gate
  rule (TRADING-STRATEGY.md) after 2+ straight weeks of compliance
  (Sept 18-Oct 2) — dateless PTs (CVX, ECL, META, INTC, MPC, AVGO)
  consistently excluded; only dated actions used as support.
- L-022, "Monitor the new 15% chase-risk threshold", retired 2026-10-02
  (hit review-by, not promoted). One entry admitted under the sub-15% bar
  (NTRA +11.15%) — no prompt reversal (-0.36% after 4 sessions). Rule
  stands; entry tracking continues under L-025/L-026.
- L-023, "Monitor loosened stall-breaker liquidity floor", retired
  2026-10-02 (hit review-by, not promoted). No loosened-floor name added
  across the window — no evidence either way. Rule stands.
- L-024, "Track deployment following LNG's Sept 16 exit", retired
  2026-10-02 (resolved). NTRA/BMY entries restored deployment 40.29% ->
  78.65%, in band 4 straight sessions (Sep 29-Oct 2).

- L-020, "Partial TRADE-LOG gap (EOD-only day)", retired 2026-09-25,
  promoted to a permanent Operational Rule (TRADING-STRATEGY.md) after 2
  straight weeks of compliance (Sept 11-25). Its prior-session check is
  what surfaced the full Sep 21-22 automation gap on Sep 23; the rule now
  covers partial and full-day gaps. Commit-level alerting continues under
  L-028.
- L-019, "Empty stall-breaker sector leg (any leg, not just Materials)",
  retired 2026-09-18, promoted/generalized to a permanent process rule
  (TRADING-STRATEGY.md Buy-Side Gate) ahead of its 2026-09-25 review-by —
  its own trigger (same leg empty 2 consecutive refresh cycles) fired
  this cycle: Materials came up empty on both the Sept 11 and Sept 16
  refreshes. The gate now loosens a leg's liquidity/market-cap floor
  automatically after 2 consecutive empty cycles, so standalone
  monitoring is no longer needed (see LESSONS.md L-023 for false-positive
  monitoring of the new rule itself).
- L-018, "Recurring full-day TRADE-LOG gap", retired 2026-09-18 (hit
  review-by, not promoted). Zero 3rd full-day gap occurred across the
  full monitoring window (Sept 4-18) — every session logged all three
  expected entries or was individually flagged (Sept 10's partial gap,
  covered separately by L-020). Its conditional directive ("if a 3rd gap
  occurs...") never fired; ongoing gap-checking is already covered by
  L-020's partial-gap directive. No TRADING-STRATEGY.md change.
- L-017, "Verify company/project ownership before adding a
  shared-coverage catalyst name", retired 2026-09-18, promoted to a
  permanent process rule (TRADING-STRATEGY.md Buy-Side Gate) after 2+
  straight weeks of compliance (Sept 4-18) with zero fresh misattribution
  incidents since the original Sept 1 WMB->ET correction.

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
| 2026-10-19 | CLF | HOLD pre-market — stall-breaker refresh add (Materials, 3rd leg), Q3 beat + Q4/2027 EBITDA guide today (two-source: PR + SEC 8-K), +13.5% premarket vs Oct 16 base; flagged for market-open hard-check | 12.145 | +10.09% (skip px ~$14.27: -6.31%) | missed by Ref / avoided-loss by skip px (L-039) |
| 2026-10-19 | IRON | HOLD — stall-breaker refresh add (Health Care), Phase 3 APOLLO win today, +26-28% premarket vs Oct 16 base = chase risk (>=15%) | 56.94 | +36.61% (skip px $79.04: -1.59%) | missed by Ref / skip-right by skip px (L-039) |
| 2026-10-19 | STLD | HOLD — stall-breaker refresh add (Materials), Q3 AMC Oct 19 hard-dated, no catalyst yet | 240.35 | -1.15% | skip-right |
| 2026-10-19 | TMO | HOLD — stall-breaker refresh add (Health Care), Q3 Oct 21 hard-dated, no catalyst yet | 690.125 | -0.77% | skip-right |
| 2026-10-19 | XOM | HOLD — stall-breaker refresh add (Energy), refining-margin Q3 uplift 8-K undated, theme-blocked by CVX (L-035) [no-cat] | 179.01 | +3.09% | missed [no-cat] |
| 2026-10-20 | RTX | HOLD pre-market — stall-breaker refresh add (Industrials, 3rd sector), Q3 beat + FY26 raise today (two-source: Perplexity + SEC 8-K), +2.2% premarket vs Oct 19 base; flagged for market-open hard-check (47 sh, L-035 theme cap) | 192.085 | +1.25% | n/a — entered Oct 20 |
| 2026-10-20 | HAL | HOLD pre-market — stall-breaker refresh add (Energy), Q3 EPS/revenue beat + buyback today (two-source: Perplexity + SEC 8-K), mixed (EBITDA miss); flagged for market-open hard-check | 33.00 | +7.94% | n/a — entered Oct 20 |
| 2026-10-20 | NOC | HOLD — stall-breaker refresh add (Industrials), Q3 EPS beat + FY26 EPS raise today, single-source; blocked as 3rd Industrials / A&D theme with LMT+RTX (L-030/L-035) | 510.53 | +7.95% | missed (concentration-blocked) |
| 2026-10-20 | DGX | HOLD — stall-breaker refresh add (Health Care), Q3 Oct 22 hard-dated, no catalyst yet | 234.82 | +3.30% | n/a — entered Oct 23 |
| 2026-10-23 | HCA | HOLD — new watchlist add (Health Care), Q3 print date unconfirmed (Oct 23 vs Oct 27 BMO), no catalyst yet | 467.02 | +1.33% | skip-right |
| 2026-10-29 | LLY | HOLD — slot-blocked (L-040, 6/6); stall-breaker refresh add (Health Care), Q3 beat + FY26 rev guide raise today (two-source: Perplexity + SEC 8-K), +7.33% pre-mkt vs Oct 28 base | 1290.67 | | |
| 2026-10-29 | MRK | HOLD — stall-breaker refresh add (Health Care), Q3 beat + EPS guide raise today, single-source (WebSearch unconfirmed), +4.78% pre-mkt | 141.09 | | |
| 2026-10-29 | FTI | HOLD — stall-breaker refresh add (Energy), Q3 beat + subsea guide raise today, single-source; pre-mkt -3.29% (bars) conflicts; concentration-blocked as 3rd Energy (L-030) | 71.46 | | |
| 2026-10-30 | ABBV | HOLD — slot-blocked (L-040, 6/6); stall-breaker refresh add (Health Care), Q3 beat + FY26 EPS guide raise + div hike today (Perplexity; bars confirm +2.28% vs Oct 29 base) | 290.75 | | |
| 2026-10-30 | LNG | HOLD — stall-breaker refresh add (Energy), Q3 beat (print date unconfirmed, ~Oct 29), single-source, +9.89% vs Oct 28 base; concentration-blocked as 3rd Energy (L-030) | 318.90 | | |
| 2026-10-30 | OKE | HOLD — stall-breaker refresh add (Energy), Q3 beat + EBITDA guide raise Oct 27 AMC; follow-through fails (Oct 29 $95.79 < Oct 27 $95.95); 3rd Energy (L-030) | 95.79 | | |
