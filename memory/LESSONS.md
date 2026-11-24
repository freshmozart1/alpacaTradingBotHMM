# Lessons & Decision Scoreboard

Read every pre-market and market-open session. Active directives are
BINDING — each pre-market entry must confirm compliance per lesson.
Keep small: max ~7 active lessons, ~15 open scoreboard rows. Weekly
review retires/promotes/prunes (see weekly-review STEP 4.5).

## Active Lessons

### L-049 — Utilities blocked after 2 consecutive failures; defined re-entry
- Date: 2026-11-20 | Source: WEEKLY-REVIEW 2026-11-20 (NRG -7% cut Nov
  17 -$651.15, CEG trail stop Nov 19 -$141.05 → Utilities sector exit;
  strategy rule has no stated re-entry condition)
- Lesson: "Exit a sector after 2 failed trades" lacked a re-entry bar.
- Directive: No new Utilities entry before 2026-12-04; after that, only
  if XLU 5-session momentum is positive AND the catalyst is two-source
  dated. Every gate check on a Utilities name logs "L-049 blocked/pass".
- Status: active | Review-by: 2026-12-04

### L-048 — Score skips vs SPY as well as absolute
- Date: 2026-11-20 | Source: WEEKLY-REVIEW 2026-11-20 (SPY -7.98% week;
  absolute avoided-loss verdicts in a broad selloff are mostly beta)
- Lesson: Absolute +5d verdicts can't separate selection from market drift.
- Directive: Each weekly review logs every scored row's SPY +5d % over
  the same window and a relative verdict (rel = row % - SPY %; missed
  >= +3, avoided <= -3) next to the absolute verdict. Measurement only.
- Status: active | Review-by: 2026-12-04

### L-047 — One position per theme while regime is Bear/High-Vol
- Date: 2026-11-20 | Source: WEEKLY-REVIEW 2026-11-20 (CEG+NRG AI-power
  pair, 18.8% < 25% theme cap, both failed Nov 17/19 → forced Utilities
  exit, -$792.20 combined)
- Lesson: Two same-theme names are one correlated bet with double
  sector-exit risk.
- Directive: While HMM regime is Bear/High-Vol or VIX >= 25, an entry
  that would hold a 2nd position in the same sub-industry/theme is a
  concentration skip; log the theme count at every gate check.
  Tightening only.
- Status: active | Review-by: 2026-12-04

### L-046 — Verify routine commits on main at EOD; alert same session
- Date: 2026-11-13 | Source: WEEKLY-REVIEW 2026-11-13 (Nov 10 midday
  left on unmerged branch, noted at EOD, alerted next pre-market; Nov 13
  pre-market missing at open, market-open fired ~2h late; supersedes
  L-042: 4 incidents / 4 alerts over 2 weeks, 2 one session late)
- Lesson: Gaps found at EOD were deferred to the next pre-market alert.
- Directive: Every EOD runs `git log origin/main` for today's 4 routine
  commits (pre-market, market-open, midday, EOD-in-progress); any
  missing, off-main, or >30 min late run gets one ClickUp alert that
  session, logged "alerted" in the EOD notes.
- Status: active | Review-by: 2026-11-27

### L-045 — Forward candidate pipeline while deployment <50%
- Date: 2026-11-13 | Source: WEEKLY-REVIEW 2026-11-13 (deployment
  28-38% all week; only 5 names reached a gate in 5 sessions; Nov 12-13
  one candidate each, both failed; 1 weekly slot + 2 position slots
  unused; -1.75% vs S&P on 62% cash)
- Lesson: Under-deployment is candidate supply, not gate tightness
  (scoreboard 8 avoided : 3 missed over 2 weeks).
- Directive: While deployment <50%, every pre-market lists >=3 named
  candidates from >=2 sectors, each with a hard-dated catalyst (earnings
  / event) today or in the next 2 sessions; market-open logs pass/fail
  per name. If <3 exist, log the calendar scan used. Process only — gate
  unchanged.
- Status: active | Review-by: 2026-11-27

Template:

### L-NNN — <short title>
- Date: YYYY-MM-DD | Source: <WEEKLY-REVIEW date / RESEARCH-LOG date / manual>
- Lesson: <what was observed>
- Directive: <one concrete, checkable instruction>
- Status: active | Review-by: YYYY-MM-DD

## Retired Lessons

- L-044, "Execute a -7% breach the session it is found", retired
  2026-11-20, promoted to a permanent Sell-Side Rule after 2 straight
  weeks of compliance (Nov 6-20): NRG cut same session Nov 17 at -7.21%
  mark, slippage -0.45% vs cut line.
- L-043, "Throttle entries in a Bear/High-Vol regime", retired
  2026-11-20, promoted to a permanent Buy-Side Gate rule after 2 straight
  weeks of compliance (Nov 6-20): Nov 17 entries blocked, Nov 18 capped
  at 1 (TGT), Nov 20 checked; SPY -7.98% week.

- L-036, "Log gap-through slippage on every exit", retired 2026-11-13,
  promoted to a permanent Operational Rule (measurement only) — logged
  on all 6 exits Nov 3-6 (total -$388.70), reported in 2 reviews.
- L-041, "Keep a fully-specified next-slot candidate while 6/6",
  retired 2026-11-13 (hit review-by, not promoted): never fired since
  Nov 3 (book 2-4/6). Pipeline need moved to L-045.
- L-042, "Alert every missing or late routine run the same session",
  retired 2026-11-13, superseded by L-046: 4 incidents / 4 alerts over
  Oct 30-Nov 13, but Nov 5 and Nov 10 midday gaps alerted a session late.

- L-039, "Score chase/fade skips from the skip-time price", retired
  2026-11-06, promoted to a permanent Operational Rule after 2 straight
  weeks of compliance (Oct 23-Nov 6; CLF/IRON scored, IDXX logged).
- L-040, "Log slot-blocked candidates while the book is full", retired
  2026-11-06, promoted to a permanent Buy-Side Gate rule after 2 straight
  weeks of compliance (LLY, ABBV, IDXX logged; zero forced rotations).
- L-038, "Shadow-score the [no-cat] sector-momentum spec", retired
  2026-11-06 (hit review-by, not promoted): 1 trigger (LLY Oct 29) / 0
  hits (-0.45% +5d). Adoption bar (>=4 triggers, hits > losses) unmet.

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
| 2026-11-09 | CEG | HOLD pre-market — new watchlist add (Utilities/IPP), Q3 beat + FY26 guide raise today (Perplexity; WebSearch 2nd source unconfirmed), weak sector momentum (XLU -0.7% 5-sess); flagged for market-open hard-check, entry ≤$270 / -7% cut / target ~$324 | 249.77 | +11.20% | n/a — entered Nov 9 (trail stop -1.55%) |
| 2026-11-09 | NRG | HOLD — new watchlist add (Utilities/IPP), Q3 today, FY26 reaffirmed + 2027 guide initiated (no raise), single-source | 88.42 | +6.30% | n/a — entered Nov 11 (-7% cut) |
| 2026-11-09 | B | HOLD — new watchlist add (Materials, gold), Q3 today: adj EPS beat / rev miss / FY26 reaffirmed, single-source | 40.56 | -10.03% | avoided-loss |
| 2026-11-10 | TDG | HOLD — new watchlist add (A&D), FQ4 BMO today: adj EPS $12.44 +15% / sales +23% (SEC 8-K), FY27 EPS guide below consensus (Perplexity), pre-mkt ~-1.4%; not gate-clearing | 1221.06 | -2.78% | skip-right |
| 2026-11-12 | BN | HOLD — new watchlist add (Financials), Q3 BMO today: DE $0.73/sh +16% y/y, $900M YTD buybacks, single-source; no pre-mkt print, Financials not leading | 42.05 | -7.37% | avoided-loss |
| 2026-11-16 | ARMK | HOLD pre-market — new watchlist add (Disc), FQ4 BMO today, print not yet indexed; flagged for market-open hard-check, entry ≤$57.50 / -7% cut / target $66.10 | 53.89 | | |
| 2026-11-16 | ACM | HOLD — new watchlist add (Industrials, leader), FQ4 AMC today hard-dated, no catalyst yet; Nov 17 hard-check, entry ≤$75 / -7% cut / target ~$86 | 70.53 | | |
| 2026-11-16 | TGT | HOLD — new watchlist add (Staples), Q3 BMO Nov 18 hard-dated, no catalyst yet; +70% YTD chase-sensitive | 161.44 | | |
| 2026-11-16 | WWD | HOLD — new watchlist add (Industrials/A&D), FQ4 AMC Nov 18 hard-dated, no catalyst yet | 329.82 | | |
| 2026-11-16 | TSN | HOLD — new watchlist add (Staples), FQ4 BMO today, print not yet indexed; consensus EPS -43% y/y, weak setup | 58.86 | | |
| 2026-11-17 | ENR | HOLD — stall-breaker refresh add (Staples), FQ4 BMO today: adj EPS $1.37 vs $1.31 beat / rev miss / FY27 organic flat-to-down, single-source; mixed | 24.365 | | |
| 2026-11-17 | WMT | HOLD — stall-breaker refresh add (Staples, leader), Q3 BMO Nov 19 hard-dated, no catalyst yet; Nov 19 hard-check | 128.44 | | |
| 2026-11-17 | CVI | HOLD — stall-breaker refresh add (Energy), Mizuho Underperform→Neutral Nov 16 w/ PT cut $52→$47 — weak, thin vol | 39.14 | | |
| 2026-11-17 | GLNG | HOLD — stall-breaker refresh add (Energy), Q3 Nov 18 hard-dated, no catalyst yet | 41.39 | | |
| 2026-11-19 | PANW | HOLD pre-market — new watchlist add (Tech), FQ1 AMC Nov 18 beat + FY27 rev/EPS guide raise (two-source: Perplexity + SEC 8-K), pre-mkt ~+9.6%; XLK weakest sector; secondary market-open hard-check, entry ≤$380 / -7% cut / target ~$437 | 339.68 | | |
| 2026-11-19 | WSM | HOLD — new watchlist add (Disc), Q3 BMO today, print not yet indexed | 259.94 | | |
| 2026-11-19 | ROST | HOLD — new watchlist add (Disc), Q3 AMC today hard-dated, no catalyst yet; Nov 20 hard-check | 227.61 | | |
| 2026-11-19 | BJ | HOLD — new watchlist add (Staples), Q3 BMO Nov 20 hard-dated, no catalyst yet | 110.90 | | |
| 2026-11-20 | DLTR | HOLD — new watchlist add (Staples/Disc), Q3 BMO Nov 24 hard-dated, no catalyst yet (L-045 pipeline) | 140.285 | | |
| 2026-11-20 | MDT | HOLD — new watchlist add (Health Care), FQ2 BMO Nov 24 hard-dated, no catalyst yet (L-045 pipeline) | 100.63 | | |
| 2026-11-20 | A | HOLD — new watchlist add (Health Care), FQ4 AMC Nov 23 hard-dated, no catalyst yet (L-045 pipeline) | 175.415 | | |
| 2026-11-23 | SJM | HOLD — stall-breaker refresh add (Staples/packaged foods), FQ2 BMO Nov 24 hard-dated, no catalyst yet | 133.68 | | |
| 2026-11-23 | UNH | HOLD pre-market — stall-breaker refresh add (HC/managed care), TD Cowen Hold→Buy PT $455 dated Nov 20, single-source (WebSearch unconfirmed); market-open hard-check, entry ≤$355 / -7% cut / target ~$398 | 340.03 | | |
| 2026-11-23 | BURL | HOLD — stall-breaker refresh add (Disc/off-price), Q3 BMO Nov 24 hard-dated, no catalyst yet | 245.43 | | |
| 2026-11-24 | BBY | HOLD pre-market — stall-breaker refresh add (Disc, leader), Q3 FY27 beat + FY27 guide raise today (two-source: Perplexity + CNBC/8-K); alternate market-open hard-check, entry ≤$106 / -7% cut / target +15% | 97.01 | | |
| 2026-11-24 | DELL | HOLD — stall-breaker refresh add (Tech), FQ3 AMC today hard-dated, no catalyst yet; Nov 25 hard-check | 335.46 | | |
| 2026-11-24 | DE | HOLD — stall-breaker refresh add (Industrials), FQ4 BMO Nov 25 hard-dated, no catalyst yet | 633.255 | | |
| 2026-11-24 | DKS | HOLD — chase skip (Disc), Q3 beat + FY EPS raise Nov 24 (Perplexity), pre-mkt +16.40% vs Nov 23 base $133.58 ≥15% bar; skip px $155.49 | 133.58 | | |
