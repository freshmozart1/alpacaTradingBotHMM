# Trading Strategy

## Mission

Beat the S&P 500 over the challenge window. Stocks only — no options, ever.

## Capital & Constraints

- Starting capital: ~$100,000.00
- Platform: Alpaca
- Instruments: Stocks ONLY
- PDT limit: 3 day trades per 5 rolling days (account < $25k)

## Core Rules

1. NO OPTIONS — ever
2. 75-85% deployed
3. 5-6 positions at a time, max 20% each
4. 10% trailing stop on every position as a real GTC order
5. Cut losers at -7% manually
6. Tighten trail: 7% at +15%, 5% at +20%
7. Never within 3% of current price; never move a stop down
8. Max 3 new trades per week
9. Follow sector momentum
10. Exit a sector after 2 consecutive failed trades
11. Patience > activity

## Buy-Side Gate

Before placing any buy order, every single one of these checks must pass.
If any fail, the trade is skipped and the reason is logged.

- Total positions after this fill will be no more than 6.
- Total trades placed this week (including this one) is no more than 3.
- Position cost is no more than 20% of account equity.
- Position cost is no more than available cash.
- Pattern day trader day-trade count leaves room (under 3 on a sub-$25k
  account).
- A specific catalyst is documented in today's research log entry, dated
  today OR dated within the prior 5 trading sessions if (a) confirmed by a
  second independent source (WebSearch, or a distinct outlet from the
  original), (b) ./scripts/alpaca.sh bars show the prior session's close
  above the close immediately before the catalyst date, and (c) the
  realized reaction is below the 15% chase-risk bar.
- The instrument is a stock (not an option, not anything else).
- If the no-trade streak has reached 3+ consecutive sessions (stall-breaker
  armed), the day's pre-market research MUST include a watchlist refresh
  (drop stale/unverifiable names, add fresh candidates from a broadened
  sector screen) before the gate is evaluated — a refresh is not optional
  while the stall-breaker is armed.
- No XLE or MU catalyst counts toward the buy-side gate unless confirmed
  by a second independent source (WebSearch, or ./scripts/alpaca.sh
  quote/bars for any price claim).
- Any macro print (VIX, futures, oil, or any other recurring data point)
  that exactly matches the prior session's logged value must be flagged
  suspect and cross-checked before being used in Risk Factors or the gate.
- No earnings-print claim (any ticker) counts toward the buy-side gate
  unless the source snippet's own date matches today, or the print is
  confirmed via ./scripts/alpaca.sh bars/quote post-release.
- When WTI/Brent cross-source dispersion exceeds ~10% in a single
  session, cross-check via ./scripts/alpaca.sh bars on a liquid oil proxy
  (USO/XLE) before treating either cluster as the operative read.
- At market-open re-validation for any new entry, explicitly check for a
  same-week ex-dividend date or a recent/pending analyst action and note
  it in the trade log, even if it doesn't block entry.
- For watchlist names with average daily volume under ~50,000 shares, the
  market-open bars-confirmation window extends to up to 60 minutes
  post-open (from the standard ~15-20 minutes) before ruling a catalyst
  reaction unconfirmed — thin liquidity can produce zero bars prints well
  into the session.
- When a refreshed watchlist completes a full re-arm cycle (per the
  3-session stall-breaker trigger) without producing a gate-clearing
  catalyst, the next refresh's sector screen includes a 3rd sector
  (next-highest YTD momentum) alongside the top-2, to avoid recycling the
  same names/coverage across cycles.
- When a watchlist catalyst involves a pipeline, joint venture, or
  multi-company project, explicitly verify which company owns/operates
  the specific asset (via the company's own investor materials, not just
  news aggregator coverage) before adding the name to the watchlist or
  counting the catalyst toward the buy-side gate.
- If the same stall-breaker sector leg comes up empty on 2 consecutive
  refresh cycles, the next refresh for that leg loosens its
  liquidity/market-cap floor (screening smaller-cap/thinner-liquidity
  names, still subject to the existing thin-liquidity 60-minute
  bars-confirmation window) rather than leaving the leg empty again.
- A catalyst's already-realized price reaction of 15% or more since its
  own date is chase risk and excluded from the gate; a reaction below 15%
  does not by itself disqualify an otherwise-clearing catalyst.
  The reaction is measured from the close immediately before the
  catalyst's own date (not from an earlier pre-event reference).

## Sell-Side Rules

Evaluated at the midday scan and opportunistically:

- If unrealized loss is -7% or worse, close immediately.
- If the thesis has broken (catalyst invalidated, sector rolling over,
  news event), close, even if not yet at -7%.
- If position is up +20% or more, tighten trailing stop to 5%.
- If position is up +15% or more, tighten trailing stop to 7%.
- If a sector has two consecutive failed trades, exit all positions in
  that sector.

## Entry Checklist

(agent documents all of these before placing)

- What is the specific catalyst today?
- Is the sector in momentum?
- What is the stop level (7-10% below entry)?
- What is the target (minimum 2:1 risk/reward)?

## Operational Rules

- Before logging any EOD snapshot, check the account's `balance_asof`
  field; if it doesn't match today's date, label the entry explicitly as
  provisional/live-pulled rather than committing it as today's official
  settled EOD close.
- Before logging the day's first TRADE-LOG entry, verify the previous
  trading session has all three expected entries (Market-Open, Midday,
  EOD); if any are missing (partial or full-day gap), log a one-line
  retroactive gap note rather than letting it pass silently.

## Rule Changelog

Every change to this file must be recorded here by the weekly review,
citing scoreboard/log evidence (memory/LESSONS.md, TRADE-LOG,
RESEARCH-LOG). Risk rules (trailing stops, -7% cut, position sizing caps,
max 3 trades/week, no options) may be tightened but NEVER loosened.

| Date | Rule | Old -> New | Reason / Evidence |
|------|------|------------|-------------------|
| 2026-07-06 | (baseline) | — -> v1 scaffold ruleset | Initial rules; no changes yet |
| 2026-07-24 | Buy-Side Gate | (none) -> mandatory watchlist refresh when stall-breaker armed (>=5 no-trade sessions) | Promoted from LESSONS.md L-003 (2026-07-10), complied with every session for 2 straight weeks (Jul 10-24), directly sustaining the pipeline that surfaced KALU's catalyst. Process addition only, not a risk-rule change. |
| 2026-07-31 | Buy-Side Gate | (none) -> no XLE/MU catalyst counts without second-source confirmation | Promoted from LESSONS.md L-001 (2026-07-15), complied with every session for 2+ straight weeks (Jul 15-31) with zero fresh fabricated-data incidents. Process addition only, not a risk-rule change. |
| 2026-07-31 | Buy-Side Gate | (none) -> any macro print matching the prior session's value must be flagged suspect and cross-checked | Promoted from LESSONS.md L-002 (2026-07-17), complied with every session for 2+ straight weeks (Jul 17-31); the stale VIX print recurred repeatedly and was correctly flagged/discounted each time. Process addition only, not a risk-rule change. |
| 2026-08-07 | Buy-Side Gate | (none) -> no earnings-print claim counts unless today-dated or bars/quote-confirmed post-release | Promoted from LESSONS.md L-004 (2026-07-24), complied with every session for 2+ straight weeks (Jul 24-Aug 7) with zero fresh incidents. Process addition only, not a risk-rule change. |
| 2026-08-07 | Buy-Side Gate | (none) -> WTI/Brent dispersion >10% requires a USO/XLE bars cross-check before use | Promoted from LESSONS.md L-005 (2026-07-24), complied with every session for 2+ straight weeks (Jul 24-Aug 7), correctly resolving oil-price dispersion via bars each time it triggered. Process addition only, not a risk-rule change. |
| 2026-08-07 | Buy-Side Gate | (none) -> flag same-week ex-div/analyst-action risk at every new entry | Promoted from LESSONS.md L-006 (2026-07-24), complied with every session for 2+ straight weeks (Jul 24-Aug 7), checked at every new entry (ECL, CVX, LNG) with zero misses. Process addition only, not a risk-rule change. |
| 2026-08-07 | Buy-Side Gate | bars-confirmation window ~15-20 min post-open -> up to 60 min for sub-~50k-avg-volume names | Escalation per LESSONS.md L-007 (2nd consecutive missed-skewed skip-scoreboard week, missed 1 / avoided-loss 0 on 2026-08-07 vs missed 3 / avoided-loss 1 on 2026-07-31). Evidence: GRC (2026-07-30 gate-fail, Ref $78.46) returned zero bars prints ~17 min post-open on ~5-10k avg daily volume despite a genuine, today-dated Q2 beat, and was confirmed "missed" at +7.84% by Aug 6. Targets the actual confirmation-mechanism failure rather than loosening the catalyst-freshness window broadly. Process/gate calibration only — trailing stops, -7% cut, position sizing caps, 3-trades/week cap, and no-options all untouched. Review-by 2026-08-21 (LESSONS.md L-008) to check for false-positive entries introduced by the wider window. |
| 2026-08-21 | Buy-Side Gate | catalyst must be dated today -> dated today OR within the prior 2 trading sessions if confirmed by a second independent source | Escalation per LESSONS.md L-009 (6th consecutive week under the 75-85% deployment target, 2026-08-21) and this review's skip-scoreboard evidence: COP (+8.18%) and NEM (+15.23%) both scored "missed", passed over solely for lacking a same-day-dated catalyst despite genuine, still-live multi-session catalysts (Q2 beat/CEO transition; Nevada Gold Mines settlement + gold rally) — missed:avoided ratio 2:1, total missed gains 23.41% vs avoided losses 10.60%, the most missed-skewed read of the challenge so far. Also satisfies STEP 5's 2nd-consecutive-zero-trade-week requirement (Week 6 Aug 10-14, Week 7 Aug 17-21). Process/gate calibration only — trailing stops, -7% cut, position sizing caps, 3-trades/week cap, and no-options all untouched. Review-by 2026-09-04 (LESSONS.md L-012) to check for false-positive entries introduced by the wider window. |
| 2026-08-28 | Buy-Side Gate | stall-breaker re-arm trigger 5+ consecutive no-trade sessions -> 3+ | Promoted from LESSONS.md L-010 (2026-08-14), complied with every session for 2 straight weeks (Aug 14-28) with zero fresh incidents — correctly re-armed and refreshed the watchlist 3 times this cycle (Aug 24, 26, 28), giving each refresh more of the week's runway to convert into an entry. Process addition only, not a risk-rule change. |
| 2026-08-28 | Operational Rules (new section) | (none) -> check `balance_asof` before logging any EOD snapshot; label provisional if it lags today's date | Promoted from LESSONS.md L-011 (2026-08-14), complied with every EOD session for 2 straight weeks (Aug 14-28) with zero fresh mislabeling/mismatch incidents (the three-incident pattern that spawned this lesson did not recur). Process addition only, not a risk-rule change. |
| 2026-09-04 | Buy-Side Gate | (none) -> stall-breaker refresh screens a 3rd sector (next-highest YTD momentum) after a full re-arm cycle produces no gate-clearing catalyst | Promoted from LESSONS.md L-013 (2026-08-21), complied with every refresh cycle for 2+ straight weeks (Aug 21-Sept 4: Aug 24, 26, 28, Sept 1 refreshes all screened a 3rd sector alongside Energy/Materials, surfacing AMAT, MRVL, and CRH) with zero fresh incidents. Process addition only, not a risk-rule change. |
| 2026-09-18 | Buy-Side Gate | (none) -> verify company/project ownership before counting a shared pipeline/JV/multi-company catalyst | Promoted from LESSONS.md L-017 (2026-09-04), complied with every session for 2+ straight weeks (Sept 4-18) with zero fresh misattribution incidents since the original Sept 1 WMB->ET correction. Process addition only, not a risk-rule change. |
| 2026-09-18 | Buy-Side Gate | (none) -> a stall-breaker sector leg empty 2 consecutive refresh cycles gets its liquidity/market-cap floor loosened on the next refresh | Promoted/generalized from LESSONS.md L-019 (2026-09-11), triggered ahead of its 2026-09-25 review-by: Materials came up empty on both the Sept 11 and Sept 16 refresh cycles (2 consecutive), meeting L-019's own escalation trigger. Process addition only, not a risk-rule change. |
| 2026-09-18 | Buy-Side Gate | "chase risk" excluded by subjective judgment, no numeric bar -> a catalyst reaction of >=15% already realized is chase risk and excluded; a reaction below 15% does not by itself disqualify an otherwise-clearing catalyst | Escalation per STEP 5 (2nd consecutive zero-new-trade week: Sept 8-11, Sept 14-18). Evidence: GEV's Sept 16-dated Vineyard Wind/Nantucket settlement cleared every other gate check but was excluded citing "the same chase-risk pattern that sidelined CRM/CRWD" despite only a +4.90% realized reaction (Sept 17 close) vs. CRM/CRWD's +20.3%/+22.6% reactions that legitimately justified the Aug 28 chase-risk exclusion — conflating a modest, still-live reaction with an already-blown-out one likely cost a trade this week (GEV extended to +4.82% Sept 17, +8.19%-range peers BE/MU also extending). Process/gate calibration only — trailing stops, the -7% cut, position sizing caps, the 3-trades/week cap, and no-options all remain untouched. Review-by 2026-10-02 (LESSONS.md L-022) to check for false-positive entries admitted under the new 15% bar. |
| 2026-09-25 | Operational Rules | (none) -> verify the prior session has Market-Open/Midday/EOD TRADE-LOG entries before the day's first entry; log a retroactive gap note if any are missing | Promoted from LESSONS.md L-020 (2026-09-11), complied with every session for 2 straight weeks (Sept 11-25); its check surfaced the full Sep 21-22 automation gap on Sep 23. Process addition only, not a risk-rule change. |
| 2026-09-25 | Buy-Side Gate | catalyst dated today OR within prior 2 sessions if two-source confirmed -> dated today OR within prior 5 sessions if two-source confirmed AND bars show prior close above the pre-catalyst close AND realized reaction <15% | Escalation per STEP 5 (3rd consecutive zero-new-trade week: Sept 8-11, 14-18, 21-25) and L-024 (deployment 40.29%). Evidence: skip scoreboard 3:0 missed this week (GEV +7.84%, BE +6.14%, MU +15.62%; +29.60% missed vs 0% avoided); GEV's two-source-confirmed Sep 16 Vineyard Wind settlement (+4.9% initial reaction) was dropped Sep 23 as stale while trending to +8.47% by Sep 25. Follow-through and chase-bar conditions keep the widening bounded. Process/gate calibration only — trailing stops, -7% cut, position sizing caps, 3-trades/week cap, and no-options untouched. Review-by 2026-10-09 (LESSONS.md L-025). |
| 2026-09-25 | Buy-Side Gate (clarification) | 15% chase bar "since its own date" (base unspecified) -> measured from the close immediately before the catalyst's own date | Removes ambiguity, not a loosening: META's Sep 25 exclusion used the Sep 18 pre-event close (+16.97%) instead of the Sep 22 pre-catalyst close (+5.58%) for its Sep 23-dated catalyst. Monitored under LESSONS.md L-022/L-026. |
