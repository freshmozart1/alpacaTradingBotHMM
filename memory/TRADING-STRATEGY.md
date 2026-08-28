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
  today OR dated within the prior 2 trading sessions if confirmed by a
  second independent source (WebSearch, or a distinct outlet from the
  original).
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
