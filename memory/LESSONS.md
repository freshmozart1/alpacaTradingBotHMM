# Lessons & Decision Scoreboard

Read every pre-market and market-open session. Active directives are
BINDING — each pre-market entry must confirm compliance per lesson.
Keep small: max ~7 active lessons, ~15 open scoreboard rows. Weekly
review retires/promotes/prunes (see weekly-review STEP 4.5).

## Active Lessons

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

### L-044 — Execute a -7% breach the session it is found
- Date: 2026-11-06 | Source: WEEKLY-REVIEW 2026-11-06 (MLM -7.17% at
  Nov 5 EOD marks, cut deferred "EOD = no trades", filled -8.66% Nov 6
  open — ~$143 extra; Nov 5 midday missing)
- Lesson: "Close immediately" was treated as "close next session".
- Directive: Any routine (midday, EOD, ad-hoc) that finds a position at
  -7% or worse while the market is open (EOD fires ~20:14 UTC, close
  21:00 UTC) cancels its GTC stop, market-sells, verifies via
  `orders`/`positions`, and sends a same-session ClickUp alert.
- Status: active | Review-by: 2026-11-20

### L-043 — Throttle entries in a Bear/High-Vol regime
- Date: 2026-11-06 | Source: WEEKLY-REVIEW 2026-11-06 (NVO Nov 4, MLM
  Nov 5 both -7% cut within 2 sessions, -$1,528.55; HMM Bull 93% -> 72%
  Nov 2, flipped Bear/High-Vol 100% Nov 6; VIX ~26; S&P -4.4% Nov 5)
- Lesson: Fresh earnings entries in a decaying/flipped regime get
  stopped out before the thesis can work.
- Directive: While HMM regime is Bear/High-Vol or VIX >= 25, allow at
  most 1 new entry per session, only after SPY's first 30 min trades
  above its prior close; log regime/VIX/SPY check at every gate check.
  Tightening only — the gate still decides.
- Status: active | Review-by: 2026-11-20

Template:

### L-NNN — <short title>
- Date: YYYY-MM-DD | Source: <WEEKLY-REVIEW date / RESEARCH-LOG date / manual>
- Lesson: <what was observed>
- Directive: <one concrete, checkable instruction>
- Status: active | Review-by: YYYY-MM-DD

## Retired Lessons

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
| 2026-11-02 | IDXX | HOLD — slot-blocked (L-040, 6/6); stall-breaker refresh add (Health Care), Q3 beat + FY26 EPS raise today (two-source: Perplexity + SEC 8-K), pre-mkt ~-1.3% (Perplexity, bars unconfirmed); Nov 3 dropped as chase skip (+21.86%), skip px $672.06 (L-039) | 551.48 | +28.24% (vs skip px $672.06: +5.23%) | missed (slot-blocked, then chase) |
| 2026-11-02 | ET | HOLD — stall-breaker refresh add (Energy), Q3 Nov 3 hard-dated, no catalyst yet; 3rd Energy (L-030) | 20.92 | -8.56% | avoided-loss |
| 2026-11-02 | MLM | HOLD — stall-breaker refresh add (Materials, 3rd leg), Q3 Nov 4 BMO hard-dated, no catalyst yet | 540.425 | -1.78% | n/a — entered Nov 5 (-7% cut) |
| 2026-11-03 | PFE | HOLD — stall-breaker refresh add (Health Care), Q3 beat + FY26 guide raise today, single-source (WebSearch unconfirmed, no bars print); conditional next-slot candidate | 30.71 | -4.40% | avoided-loss |
| 2026-11-03 | AMGN | HOLD — stall-breaker refresh add (Health Care), Q3 AMC Nov 3 hard-dated, no catalyst yet | 465.45 | -0.09% | skip-right |
| 2026-11-03 | MPC | HOLD — stall-breaker refresh add (Energy), Q3 beat today, single-source; concentration-blocked as 3rd Energy (L-030) | 430.48 | -9.48% | avoided-loss |
| 2026-11-04 | NVO | HOLD pre-market — stall-breaker refresh add (Health Care), Q3 beat + FY26 outlook raise today (two-source: Perplexity + SEC 6-K), ~+6% early (Perplexity, bars unconfirmed); flagged for market-open hard-check (L-041 candidate) | 40.21 | +2.21% | n/a — entered Nov 4 (-7% cut) |
| 2026-11-04 | CVS | HOLD — stall-breaker refresh add (Health Care), Q3 beat + FY26 EPS raise + split plan today, single-source; pre-mkt weak (MA stars) | 91.45 | -2.17% | skip-right |
| 2026-11-04 | CVE | HOLD — stall-breaker refresh add (Energy), Q3 BMO today, result not yet indexed; hard-check at open | 30.72 | -7.52% | avoided-loss |
| 2026-11-04 | WLK | HOLD — stall-breaker refresh add (Materials, 3rd leg, loosened floor), Q3 adj EPS miss today, single-source; +3% pre-mkt (Perplexity) | 68.50 | -6.80% | avoided-loss |
| 2026-11-05 | APD | HOLD — new watchlist add (Materials), FY Q4 BMO today: adj EPS $3.61 vs $3.60 in-line, FY27 guide "growth" (vague), single-source; not gate-clearing | 318.885 | -0.86% | skip-right |
| 2026-11-09 | CEG | HOLD pre-market — new watchlist add (Utilities/IPP), Q3 beat + FY26 guide raise today (Perplexity; WebSearch 2nd source unconfirmed), weak sector momentum (XLU -0.7% 5-sess); flagged for market-open hard-check, entry ≤$270 / -7% cut / target ~$324 | 249.77 | | |
| 2026-11-09 | NRG | HOLD — new watchlist add (Utilities/IPP), Q3 today, FY26 reaffirmed + 2027 guide initiated (no raise), single-source | 88.42 | | |
| 2026-11-09 | B | HOLD — new watchlist add (Materials, gold), Q3 today: adj EPS beat / rev miss / FY26 reaffirmed, single-source | 40.56 | | |
| 2026-11-10 | TDG | HOLD — new watchlist add (A&D), FQ4 BMO today: adj EPS $12.44 +15% / sales +23% (SEC 8-K), FY27 EPS guide below consensus (Perplexity), pre-mkt ~-1.4%; not gate-clearing | 1221.06 | | |
| 2026-11-12 | BN | HOLD — new watchlist add (Financials), Q3 BMO today: DE $0.73/sh +16% y/y, $900M YTD buybacks, single-source; no pre-mkt print, Financials not leading | 42.05 | | |
