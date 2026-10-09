# Lessons & Decision Scoreboard

Read every pre-market and market-open session. Active directives are
BINDING — each pre-market entry must confirm compliance per lesson.
Keep small: max ~7 active lessons, ~15 open scoreboard rows. Weekly
review retires/promotes/prunes (see weekly-review STEP 4.5).

## Active Lessons

### L-034 — Track sector-momentum skips that lack a company catalyst
- Date: 2026-10-09 | Source: WEEKLY-REVIEW 2026-10-09 (MPC +10.24%
  missed, VLO +9.48% vs Ref by Oct 8 — Energy #1 refiners running on
  sector-level crack-spread drivers with no company-specific dated
  catalyst)
- Lesson: The gate is blind to sector-wide moves; misses cluster in
  top-sector names with no dated company catalyst.
- Directive: Tag every new scoreboard row lacking a company-specific dated
  catalyst "[no-cat]"; at each weekly review report missed:avoided for the
  [no-cat] subset. Process/measurement only — no gate change.
- Status: active | Review-by: 2026-10-23

### L-033 — Monitor the tightened 2-session freshness window
- Date: 2026-10-09 | Source: WEEKLY-REVIEW 2026-10-09 (L-025 false
  positive: BMY 3-session extension entry cut -7.51%; NTRA -4.62%, AVGO
  add -1.18%; window reverted 5 -> 2 sessions)
- Lesson: Catalysts 3-5 sessions old produced 0 winners in 3 entries.
- Directive: When a two-source catalyst is 3-5 sessions old and would
  have cleared the old window, log it as a HOLD scoreboard row tagged
  "[3-5s]"; at review report its +5d verdicts. Gate stays at 2 sessions.
- Status: active | Review-by: 2026-10-23

### L-032 — Cap combined single-sector exposure at 40% of equity
- Date: 2026-10-09 | Source: WEEKLY-REVIEW 2026-10-09 (AVGO+MRVL ~36%
  of equity in AI semis; Oct 8 sector selloff cost -$1,336.81 in one
  session — L-030's 2-position count didn't capture size)
- Lesson: Position-count caps miss dollar concentration in one theme.
- Directive: At every new-entry/add gate check, log post-fill sector
  exposure as % of equity; if it would exceed 40%, size the order down to
  fit or skip and log a concentration skip.
- Status: active | Review-by: 2026-10-23

### L-031 — Renew expiring GTC trailing stops mechanically
- Date: 2026-10-02 | Source: WEEKLY-REVIEW 2026-10-02 (ECL stop expires
  Oct 26, CVX stops Oct 29 — tracked only as EOD heads-up lines)
- Lesson: GTC orders expire; an expired trail leaves a position
  unprotected silently.
- Directive: At every EOD, list GTC stop expiries within 5 trading
  sessions; renew at the next market-open (cancel + re-place at the
  same or higher stop, never lower) and verify via `alpaca.sh orders`.
- Status: active | Review-by: 2026-10-16

### L-030 — Cap single-sector concentration at 2 positions
- Date: 2026-10-02 | Source: WEEKLY-REVIEW 2026-10-02 (both week-13
  entries, NTRA and BMY, came from the 3rd-sector Health Care leg — 2 of
  4 positions in one non-top-2 sector)
- Lesson: The stall-breaker's 3rd-sector leg can supply the whole refill,
  concentrating the book outside the momentum sectors.
- Directive: At every new-entry gate check, log the post-fill sector
  count; if the entry would put a 3rd position in one sector, skip and
  log it as a concentration skip.
- Status: active | Review-by: 2026-10-16

### L-029 — Dividend-adjust the pre-catalyst base around ex-div dates
- Date: 2026-10-02 | Source: WEEKLY-REVIEW 2026-10-02 (BMY ex-div $0.63
  Oct 2 pushed it nominally below its $61.18 pre-catalyst base; div-
  adjusted it was ~at base)
- Lesson: A mechanical ex-div drop can make the follow-through/thesis
  base test misfire.
- Directive: When a held or candidate name has an ex-div date inside its
  follow-through/thesis window, compare price to the dividend-adjusted
  pre-catalyst base and log both the nominal and adjusted figures.
- Status: active | Review-by: 2026-10-16

Template:

### L-NNN — <short title>
- Date: YYYY-MM-DD | Source: <WEEKLY-REVIEW date / RESEARCH-LOG date / manual>
- Lesson: <what was observed>
- Directive: <one concrete, checkable instruction>
- Status: active | Review-by: YYYY-MM-DD

## Retired Lessons

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
| 2026-09-23 | META | HOLD — stall-breaker refresh add (Technology), Connect 2026 keynote today (Sept 23) is a hard-dated event but stock already +10.8% since Sept 18 ahead of it, no post-event reaction yet to confirm | 736.595 | -1.54% | skip-right |
| 2026-09-23 | TXN | HOLD — stall-breaker refresh add (Technology), 7% dividend hike/Q2 beat/data-center revenue doubled YoY, dividend-hike date not confirmed as today-dated | 271.405 | +3.19% | missed |
| 2026-09-23 | XOM | HOLD — stall-breaker refresh add (Energy), record oil output/revenue + dismissed Michigan climate lawsuit, but pressured by the ~10% oil-price drop this week, no fresh Sept 23-dated catalyst | 158.68 | +2.67% | skip-right |
| 2026-09-23 | LNG | HOLD — stall-breaker refresh re-add (Energy, prior position exited via mechanical stop Sept 16), Corpus Christi Stage 3 completion + 5,000th cargo milestone, no fresh Sept 23-dated catalyst | 273.02 | -1.47% | skip-right |
| 2026-09-28 | INTC | HOLD — stall-breaker refresh add (Technology), AI turnaround/SK Hynix talks/CPU price hike rally (Sep 21-22), +13.17% from pre-catalyst base, PT hikes dateless (L-021), chase-adjacent | 122.98 | -5.46% | avoided-loss |
| 2026-09-28 | AVGO | HOLD — stall-breaker refresh add (Technology), AI capex/custom-silicon narrative, no dated catalyst | 352.72 | +2.78% | skip-right |
| 2026-09-28 | MPC | HOLD — stall-breaker refresh add (Energy), Zacks Sept best-energy list, no dated catalyst (Q3 call Nov 3) | 393.26 | +10.24% | missed |
| 2026-09-28 | NTRA | HOLD pre-market — stall-breaker refresh add (Health Care, 3rd sector), Sep 22 Japan PMDA Signatera CDx approval (two-source), +11.28% from Sep 21 base; flagged for market-open hard-check | 412.35 | +3.21% | n/a — entered Sep 28 (closed -4.62%) |
| 2026-09-28 | BMY | HOLD — stall-breaker refresh add (Health Care, 3rd sector), Sep 25 EXCALIBER-RRMM Ph3 presentation, single-source only | 62.89 | -6.50% | n/a — entered Sep 29 (cut -7.51%) |
| 2026-10-01 | UEC | HOLD — conditional replacement idea (Energy), Sep 29 FY26 print now two-source (+2.72% vs Sep 28 base), gate-clearing but capacity-blocked (78.68% deployed, new ~19% -> ~98%) | 9.43 | -2.97% | skip-right |
| 2026-10-05 | MRVL | HOLD — stall-breaker refresh add (Technology), Investor Day Oct 6 hard-dated (two-source), no reaction yet | 272.33 | | |
| 2026-10-05 | VLO | HOLD — stall-breaker refresh add (Energy), refining-margin upgrade coverage, no company-specific dated catalyst | 405.66 | | |
| 2026-10-05 | LMT | HOLD — stall-breaker refresh add (Industrials, 3rd sector), $94.2M Navy AEGIS award undated, Q3 Oct 22 | 506.25 | | |
