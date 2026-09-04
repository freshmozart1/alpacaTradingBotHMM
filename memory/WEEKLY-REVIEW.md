# Weekly Review

Friday reviews appended here. Template for each entry:

## Week ending YYYY-MM-DD

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $X |
| Ending portfolio | $X |
| Week return | ±$X (±X%) |
| S&P 500 week | ±X% |
| Bot vs S&P | ±X% |
| Trades | N (W:X / L:Y / open:Z) |
| Win rate | X% |
| Best trade | SYM +X% |
| Worst trade | SYM -X% |
| Profit factor | X.XX |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |

### What Worked

- ...

### What Didn't Work

- ...

### Key Lessons

- ...

### Adjustments for Next Week

- ...

### Overall Grade: X

## Week ending 2026-07-07 (partial — Day 2 of challenge)

Note: bot launched Mon 2026-07-06. This review fired 2 trading days into
the challenge, not a full week. Metrics below cover Mon-Tue only;
re-baseline against a full Mon-Fri week starting next Friday.

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 |
| Ending portfolio | $100,000.00 |
| Week return | $0 (0.00%) |
| S&P 500 week | ~-0.7% (Mon close ~7537 -> Tue ~7483) |
| Bot vs S&P | ~+0.7% (by default, zero deployment) |
| Trades | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
| — | — | — | — | No trades placed yet |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
| — | — | — | — | No open positions |

### What Worked

- Buy-side gate held firm on Day 1 — no catalyst met the bar, so no forced trade.
- Pre-market research pipeline (account snapshot, oil/VIX/futures, sector rotation) ran cleanly.
- Zero deployment meant zero drawdown while S&P dipped ~0.7% over the same two days.

### What Didn't Work

- Two days in and still fully in cash — sector watchlist (XLI, XLB, Energy) hasn't converted to a name-level idea yet.
- Too early to call this a failure, but patience needs to turn into action once a real catalyst appears.

### Key Lessons

- "Patience > activity" is working as designed on Day 1-2 — no false-positive trades.
- Need at least one full Mon-Fri week of data before the stats table (win rate, profit factor) is meaningful.

### Adjustments for Next Week

- No rule changes — sample size is zero trades, too early to tune anything.
- Keep scanning the leading-momentum sectors (XLI, XLB, Energy) for a name-level entry that clears the buy-side gate.

### Overall Grade: Incomplete (insufficient data — 2 days, 0 trades)

## Week ending 2026-07-10

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 |
| Ending portfolio | $100,000.00 |
| Week return | $0 (0.00%) |
| S&P 500 week | +1.02% |
| Bot vs S&P | -1.02% |
| Trades | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades) |
| Best trade | N/A |
| Worst trade | N/A |
| Profit factor | N/A |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
| — | — | — | — | No trades placed this week |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
| — | — | — | — | No open positions |

### What Worked

- Buy-side gate held the line for a full 5-day week — zero forced or marginal trades despite an active US-Iran war/oil shock (Jul 8-9) that would tempt a chase entry.
- Watchlist discipline: dropped CENX same-day on a fresh Strong Sell downgrade instead of holding a stale idea.
- Correctly treated the live Hormuz/Iran oil spike as un-tradeable event risk rather than a momentum entry — avoided buying an Energy top right before the ceasefire-unwind reversal hit XLE technicals by Friday.
- Research pipeline (account, macro, sector rotation, HMM regime, named-catalyst scan) ran cleanly all 5 days with no gaps.

### What Didn't Work

- Zero trades in a full 5-day week — 0/3 weekly trade cap used. S&P gained +1.02% while the bot sat flat; patience produced a -1.02% relative drag with no offsetting risk avoided (no crash occurred this week).
- Same four watchlist names (KALU, GRC, CENX, FTAI) recycled all week with no dated catalyst — the gate's "catalyst documented today" bar is filtering out every name-level idea, and the sector-momentum names on it (XLI) never converted to an entry.
- Semiconductor rally (MU, Philly Semi +3%) on Jul 10 was flagged watch-only same-day; correct per the gate (needs multi-session confirmation) but highlights the gate structurally can't catch single-day breakouts even when real.
- No fallback process for "sector in momentum but no single name clears gate" — five days running the same scan without adapting the search (e.g., screening a wider name list within XLI/XLB, not just 4 fixed tickers).

### Key Lessons

- One full week of zero trades is not yet a strategy failure — the gate did its job of avoiding a bad entry into a volatile war/oil-driven tape — but a second consecutive flat week would be a signal the watchlist itself is the bottleneck, not market conditions.
- Watching only 4 fixed tickers per leading sector for 5 straight days produced 5 straight non-catalysts; the sample of names being screened may be too narrow rather than the market lacking opportunities.
- Geopolitical-shock weeks (Iran/Hormuz) are exactly when the buy-side gate is most valuable — several tempting entries (Energy breakout, oil spike) would have been immediately underwater by Friday's reversal.

### Adjustments for Next Week

- No rule changes yet — 0 trades means there's nothing in the stats to validate a rule change against.
- Widen the name-level scan within leading sectors (XLI, XLB, Energy) beyond the same 4 recycled tickers, to raise the odds of finding a fresh dated catalyst.
- If next week also closes with 0 trades, treat it as a signal to revisit the catalyst-sourcing process (not the gate criteria itself) at the following weekly review.

### Overall Grade: C (capital preservation intact, but 5/5 days flat while S&P ran +1.02% — full first week, no trades to show for it)

## Week ending 2026-07-24

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $100,000.00 |
| Ending portfolio | $98,809.91 |
| Week return | -$1,190.09 (-1.19%) |
| S&P 500 week | -0.59% (SPY 743.28 -> 738.90, Jul 17 close -> Jul 24 close via alpaca.sh bars; Perplexity's weekly-recap figures were internally inconsistent/stale this session, cross-checked against ground-truth market data instead) |
| Bot vs S&P | -0.60% |
| Trades | 1 (W:0 / L:1 / open:0) |
| Win rate | 0% (0 of 1 closed trades) |
| Best trade | KALU -6.01% (only trade) |
| Worst trade | KALU -6.01% |
| Profit factor | 0.00 (no winners; $0 / $1,190.08 losses) |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| KALU | $176.79 (Jul 23, avg fill) | $166.16 (Jul 24, avg fill) | -$1,190.08 (-6.01%) | 10% GTC trailing stop (HWM $186.50, stop $167.85) triggered automatically, filled through the stop on a gap. Catalyst (record Q2 earnings + raised FY26 guidance) not invalidated — Wells Fargo downgrade to Underweight ($158 PT), same-day ex-dividend ($0.77), and post-earnings profit-taking cited as proximate causes. Stop mechanics functioned exactly as designed. |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| — | — | — | — | Flat — 0 positions, 0 open orders |

### Skip Scoreboard

Rows >= 5 sessions old scored this week (Ref -> +5 trading-session close, via `alpaca.sh bars`):

| Ticker | Ref (date) | +5d close | +5d % | Verdict |
|--------|------------|-----------|-------|---------|
| KALU | 178.81 (Jul 6) | 157.92 (Jul 13) | -11.68% | avoided-loss |
| GRC | 84.84 (Jul 6) | 78.48 (Jul 13) | -7.50% | avoided-loss |
| FTAI | 241.45 (Jul 6) | 209.84 (Jul 13) | -13.09% | avoided-loss |
| MU | 979.36 (Jul 10) | 849.46 (Jul 17) | -13.26% | avoided-loss |

Verdict counts: missed 0, skip-right 0, avoided-loss 4. Total missed gains: 0.00%. Total avoided losses: -45.53% (sum of the four). Missed:avoided ratio: 0:4 — **gate calibration verdict: sound.** Every scored skip this week would have lost money if bought; zero evidence the buy-side gate is too tight. (LNG/FANG/VMC/FCX/XOM/CVX/ECL/GEV all still under the 5-session threshold, not yet scored.)

### What Worked

- Buy-side gate finally converted a name-level idea (KALU, Jul 23) after 14 consecutive no-trade days, ending the stall without forcing a marginal entry — the catalyst (record Q2 earnings, raised FY26 guidance) was genuine and independently confirmed.
- Trailing-stop mechanics worked exactly as designed: the 10% GTC stop ratcheted up with the high-water mark (never moved down) and triggered automatically pre-scan, with zero manual intervention needed.
- Skip-scoreboard evidence this week is unusually clean: all 4 scored rows (KALU/GRC/FTAI from Jul 6, MU from Jul 10) were avoided-loss verdicts, each down 7.5-13.3% at +5 sessions — strong evidence the catalyst-freshness bar is correctly calibrated, not too tight.
- Data-quality discipline (L-001/L-002) held up all week: repeated stale VIX/XLE/GRC/oil fabrications were caught and discounted every session without ever being acted on.

### What Didn't Work

- The one trade taken this week was a loss (-6.01%), leaving the bot -0.60% behind the S&P for the week.
- KALU's entry had almost no room to breathe: a Wells Fargo downgrade, a same-day ex-dividend, and post-earnings profit-taking all hit within 24 hours of the fill, well before the thesis itself broke.
- GRC's Jul 24 earnings print stayed data-quality-unconfirmed all session (Perplexity misattributed a 2025-dated print as today's result) — a gap in exactly the pipeline stage covering today's dated catalyst.
- Oil/WTI source dispersion blew out to an extreme this session ($70-71 vs. $86-90 logged two sessions prior) with no clean resolution — undermines the Energy/Materials momentum thesis behind several watchlist names (LNG, FANG, VMC, FCX, XOM, CVX) without a trustworthy read.

### Key Lessons

- A statistically clean gate (4/4 avoided-loss scored skips) can still coexist with a losing trade — the gate filters entries, not exit risk; the trailing stop is the actual loss-limiter, and it worked.
- A single-trade week isn't enough sample to trust win-rate/profit-factor as anything but directional.
- Perplexity's GRC earnings misattribution today mirrors the same failure mode already tracked for XLE/MU under L-001 (stale source presented as today's data) — the directive should cover any earnings-print claim, not just XLE/MU price claims.

### Adjustments for Next Week

- Extend L-001's second-source verification requirement to any earnings-print claim (not just XLE/MU), given GRC's Jul 24 misattribution matches the same failure pattern.
- When oil/WTI cross-source dispersion exceeds ~10% intraday, require an explicit `alpaca.sh bars`-based cross-check (e.g., USO/XLE) before using either cluster as the operative read.
- Flag same-week ex-dividend dates and pending/recent analyst actions explicitly at market-open re-validation for any new entry — not just the headline catalyst — given how quickly they compounded against KALU.

### Rule Change This Week

- L-003 ("widen watchlist beyond recycled tickers") hit its Jul 24 review-by date having been complied with every session for 2 straight weeks (Jul 10-24), directly sustaining the pipeline that surfaced KALU's catalyst. Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate section) — see Rule Changelog. Retired from Active Lessons as promoted, not just complied-with.

### Overall Grade: B- (risk management worked exactly as designed — 10% trailing stop capped the loss at -6.01%/-1.19% of equity, and the skip-scoreboard evidence continues to validate the buy-side gate — but the week still nets a loss and lags the S&P by 0.60%)

## Week ending 2026-07-31

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $98,809.88 |
| Ending portfolio | $98,790.93 |
| Week return | -$18.95 (-0.02%) |
| S&P 500 week | +1.07% (SPY 738.90 -> 746.79, Jul 24 close -> Jul 31 close via `alpaca.sh bars`, ground-truth cross-check per established methodology) |
| Bot vs S&P | -1.09% |
| Trades | 2 (W:0 / L:0 / open:2) |
| Win rate | N/A (no closed trades this week) |
| Best trade | N/A (no closed trades; CVX unrealized +1.53%) |
| Worst trade | N/A (no closed trades; ECL unrealized -1.53%) |
| Profit factor | N/A (no closed trades) |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No trades closed this week |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CVX | $193.860947 (95 sh, Jul 31 blended fill) | $196.83 | +$282.06 (+1.53%) | Two 10% trailing GTC orders, 7f5acb83 (54 sh) + e328a200 (41 sh), stop $177.79725, HWM $197.5525 |
| ECL | $281.93 (70 sh, Jul 28 fill) | $277.63 | -$301.00 (-1.53%) | 10% trailing GTC, order 64b1066c, stop $257.112, HWM $285.68 |

### Skip Scoreboard

Rows >= 5 sessions old scored this week (Ref -> +5 trading-session close, via `alpaca.sh bars`):

| Ticker | Ref (date) | +5d close | +5d % | Verdict |
|--------|------------|-----------|-------|---------|
| LNG | 262.60 (Jul 20) | 255.98 (Jul 27) | -2.52% | skip-right |
| FANG | 195.55 (Jul 20) | 195.80 (Jul 27) | +0.13% | skip-right |
| VMC | 288.17 (Jul 20) | 284.41 (Jul 27) | -1.30% | skip-right |
| FCX | 58.37 (Jul 20) | 62.69 (Jul 27) | +7.40% | missed |
| XOM | 148.40 (Jul 21) | 153.20 (Jul 28) | +3.23% | missed |
| CVX | 189.25 (Jul 21) | 187.69 (Jul 28) | -0.82% | skip-right |
| ECL | 268.66 (Jul 21) | 282.95 (Jul 28) | +5.32% | missed (but bot independently bought ECL same-day Jul 28 at $281.93 once the earnings catalyst confirmed — gate delayed, did not forfeit, most of this move) |
| GEV | 1077.75 (Jul 22) | 899.81 (Jul 29) | -16.51% | avoided-loss |

Verdict counts (new rows this week): missed 3, skip-right 4, avoided-loss 1. Total missed gains: +15.95%. Total avoided losses: -16.51%. Missed:avoided ratio: 3:1 — a clear reversal from last week's 0:4 all-avoided-loss result. **Gate calibration verdict: watch, not yet act.** One week of a missed-skewed mix isn't a trend by itself (L-007 opened to track this), and the largest "miss" (ECL) was substantially recaptured by the bot's own later entry, so the net cost of the tight gate this week is smaller than the raw ratio suggests. GRC (Jul 30 row) not yet 5 sessions old — carried forward. KALU/GRC(Jul 6)/FTAI(Jul 6) rows pruned (verdicts >10 sessions old); MU (Jul 10, verdict exactly 10 sessions old) retained one more week per the "older than 10" threshold.

### What Worked

- Buy-side gate converted two genuine, bars-confirmed catalysts this week — ECL (Jul 28, Q2 earnings beat) and CVX (Jul 31, Q2 beat, highest quarterly profit in 6 years) — both entered only after live post-open confirmation, not on pre-market headline claims alone.
- Correctly held off XOM/CVX/FANG on Jul 28 despite a bars-confirmed oil-momentum pop, because the 2pm ET FOMC decision was a same-day event risk stacked on top; re-evaluated and entered CVX cleanly three sessions later once its own Q2 print (not the oil move) was the live catalyst.
- L-001/L-002/L-004/L-005/L-006 all held up under real triggers this week (stale VIX print flagged repeatedly, XOM/CVX earnings-print dating cross-checked via bars per L-004, no same-week ex-div/analyst-action risk found for either new entry per L-006).
- Neither open position needed a manual intervention — both trailing stops ratcheted mechanically and stayed clear of the -7% cut and +15%/+20% tighten thresholds all week.

### What Didn't Work

- Zero closed trades and a net -0.02% week left the bot -1.09% behind the S&P, which had a strong up week (+1.07%).
- Portfolio ended just 38.6% deployed ($38,132.95 of $98,790.93) versus the 75-85% target band — 2 of 3 weekly trade slots used but still well under-deployed, with room for 3-4 more positions before the 5-6 cap.
- Skip-scoreboard mix flipped to 3 missed / 1 avoided-loss this week (from 0 missed / 4 avoided-loss last week) — FCX (+7.40%) and XOM (+3.23%) were genuine misses with no offsetting entry; ECL's miss was largely recaptured by the bot's own later buy, but the raw scoreboard still counts it as missed at the +5d mark.
- CVX's stop-order mechanics recreated two separate trailing-stop legs (7f5acb83/e328a200) from the two-tranche fill, both correctly resting at the same stop/HWM — functional, but worth watching for any drift between the legs as HWM ratchets going forward.

### Key Lessons

- The buy-side gate's FOMC-driven delay on Jul 28 (skipping XOM/CVX/FANG same-day) and its clean Jul 31 CVX entry days later demonstrate the gate doing exactly what "patience > activity" intends: waiting out a stacked-event-risk day, then acting once the position-specific catalyst was live.
- A "missed" skip-scoreboard verdict doesn't always mean a forfeited move — ECL was scored missed but the bot captured most of the same move via its own later entry; verdicts should be read alongside the trade log, not in isolation.
- Two straight weeks of clean data-quality-lesson compliance (L-001, L-002) with no fresh incidents is enough evidence to promote both from active lessons to permanent process rules — see Rule Changelog.

### Adjustments for Next Week

- Track the skip-scoreboard verdict mix again next week (L-007): if it stays missed-skewed (missed > avoided-loss), escalate to a buy-side-gate calibration review per STEP 5 rather than waiting for a third week.
- With 2 of 3 weekly trade slots already used and the portfolio under-deployed (38.6% vs 75-85% target), keep actively scanning for 1-2 more name-level catalysts next week rather than letting the remaining slot go unused by default.
- Watch the two CVX trailing-stop legs (7f5acb83/e328a200) for any HWM/stop drift between them as the position moves; consolidate manually only if they diverge (never move a stop down).

### Rule Changes This Week

- L-001 ("XLE/MU Perplexity output unreliable") hit its Jul 31 review-by date having been complied with every session since 2026-07-15 (2+ weeks) with zero fresh incidents. Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate section) — see Rule Changelog. Retired from Active Lessons as promoted.
- L-002 ("Verify suspect repeated macro prints") hit its Jul 31 review-by date having been complied with every session since 2026-07-17 (2+ weeks) — the stale VIX print recurred repeatedly and was correctly flagged/discounted each time. Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate section) — see Rule Changelog. Retired from Active Lessons as promoted.
- New lesson L-007 opened to track the Jul 31 skip-scoreboard shift toward "missed" (see LESSONS.md).

### Overall Grade: C+ (two clean, well-reasoned entries following the gate's discipline and zero forced/marginal trades, but the week nets essentially flat, lags the S&P by 1.09%, and ends materially under-deployed against the 75-85% target)

## Week ending 2026-08-07

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $98,790.93 |
| Ending portfolio | $97,790.18 |
| Week return | -$1,000.75 (-1.01%) |
| S&P 500 week | +3.53% (SPY 746.79 -> 773.16, Jul 31 close -> Aug 7 close via `alpaca.sh bars`; Perplexity again returned dispersed/incomplete week-ending figures — cross-checked against ground-truth SPY bars per established methodology) |
| Bot vs S&P | -4.54% |
| Trades | 1 (W:0 / L:0 / open:1) |
| Win rate | N/A (no closed trades this week) |
| Best trade | N/A (no closed trades this week) |
| Worst trade | N/A (no closed trades this week; LNG, the only trade placed, unrealized -2.83% as of Aug 7) |
| Profit factor | N/A (no closed trades this week) |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No trades closed this week |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CVX | $193.860947 (95 sh) | $186.5589 | -$693.69 (-3.77%) | Two 10% trailing GTC orders, 7f5acb83 (54 sh) + e328a200 (41 sh), stop $177.79725, HWM $197.5525 |
| ECL | $281.93 (70 sh) | $285.17 | +$226.80 (+1.15%) | 10% trailing GTC, order 64b1066c, stop $259.6005, HWM $288.445 |
| LNG | $263.63 (74 sh) | $256.16 | -$552.78 (-2.83%) | 10% trailing GTC, order 974c3bfc, stop $239.283, HWM $265.87 |

### Skip Scoreboard

Rows >= 5 sessions old scored this week (Ref -> +5 trading-session close, via `alpaca.sh bars`):

| Ticker | Ref (date) | +5d close | +5d % | Verdict |
|--------|------------|-----------|-------|---------|
| GRC | 78.46 (Jul 30) | 84.61 (Aug 6) | +7.84% | missed |

Verdict counts (new rows this week): missed 1, skip-right 0, avoided-loss 0. Total missed gains: +7.84%. Total avoided losses: 0.00%. Missed:avoided ratio: 1:0 — **L-007 triggered**: missed count (1) > avoided-loss count (0) for the second consecutive scored week (3:1 last week, 1:0 this week). Per L-007's binding directive, escalated to a buy-side-gate calibration review this session — see Rule Change below. FANG (Aug 4 gate-fail row) and VMC (Aug 5 gate-fail row) are not yet 5 sessions old, carried forward. MU (Jul 10 row, verdict filled Jul 24) pruned — its scoring reference point (Jul 17 +5d close) is now 15 trading sessions old, past the 10-session retention threshold.

### What Worked

- LNG (Aug 6) was a clean, well-confirmed entry: Cheniere's Q2 beat was today-dated, and the bars-confirmed reaction held a sustained +3.3-3.5% through midday (vs a +5.14% opening high) rather than fading to flat like VMC's Aug 5 gate-fail — the gate correctly distinguished a genuine sustained reaction from a fade.
- L-004/L-005/L-006 all held up under real triggers again this week (GRC's earnings-print dating correctly stayed unconfirmed, oil dispersion cross-checked via XLE/USO bars on Aug 7, LNG's same-week ex-dividend flagged non-blocking at entry) — each has now run 2+ full weeks with zero fresh incidents, qualifying all three for promotion to permanent process rules (see Rule Changes).
- FANG (Aug 4) and VMC (Aug 5) gate-fails continue to hold correct as of today's re-check (-4.52% and -1.29% vs their gate-fail Ref prices) — the gate is correctly filtering fade/negative reactions, not just requiring a catalyst to exist.
- No risk-rule breaches all week: CVX's -3.77% unrealized drawdown (the week's largest) stayed well clear of the -7% cut, and no position hit the +15%/+20% tighten thresholds; all four resting GTC stops (2x CVX, 1x ECL, 1x LNG) confirmed unchanged/correctly ratcheted via `alpaca.sh orders`.

### What Didn't Work

- The bot lost -1.01% in a week the S&P gained +3.53% (its best week since mid-April per WSJ/CNBC) — a -4.54% relative gap, the largest of the challenge so far. Only 1 of 3 weekly trade slots was used, and being ~58% deployed for most of the week meant the bot captured little of a broad, strong up-move.
- GRC's Jul 30 gate-fail is now confirmed "missed" (+7.84% by Aug 6) — the root cause was not catalyst staleness but thin liquidity: `alpaca.sh bars` returned zero prints for ~17 minutes post-open on a low-volume name (~5-10k shares/day), so L-004's bars-confirmation clause couldn't be satisfied even though the underlying Q2 beat catalyst was real and today-dated.
- CVX continued to drift lower (-3.77% unrealized, its worst mark since entry) on the ongoing Hormuz de-escalation narrative pressuring oil — not a thesis break and nowhere near the -7% cut, but the largest single-position drag on the week's return.
- Second consecutive week where the skip-scoreboard mix skewed missed > avoided-loss (3:1 last week, 1:0 this week), triggering L-007's escalation directive — see Rule Change.

### Key Lessons

- A "missed" skip-scoreboard verdict can stem from a confirmation-mechanism limitation (thin liquidity producing no bars prints) rather than the catalyst-freshness window itself being miscalibrated — GRC's Q2 beat was genuine and today-dated; the gate correctly required bars confirmation per L-004, but the standard confirmation window wasn't built for illiquid names. Fixing the actual mechanism (confirmation window for thin-liquidity names) is more precise than loosening the freshness bar broadly, which risked admitting stale/unconfirmed catalysts more generally.
- A strong, broad up-week (S&P's best in ~4 months) is exactly when being under-deployed costs the most in relative terms — the -4.54% gap this week is a direct function of ~58% deployment plus only 1 trade, not any single bad decision.
- Two full weeks (Jul 24 - Aug 7) of clean L-004/L-005/L-006 compliance with zero fresh incidents is enough evidence to promote all three to permanent process rules, following the same bar used for L-001/L-002/L-003.

### Adjustments for Next Week

- Track whether the new thin-liquidity bars-confirmation window (60 min for sub-~50k-volume names, added to TRADING-STRATEGY.md this week) changes gate outcomes on future low-volume watchlist names, without producing false-positive entries on names whose "reaction" only appears after a long delay.
- With 1 of 3 weekly trade slots used and the portfolio still under the 75-85% deployment target after a week the S&P ran +3.53%, keep actively widening the name-level scan next week — current watchlist (GRC/FANG/VMC/FCX/XOM/GEV) is entirely stale or already-actioned.

### Rule Changes This Week

- L-004 ("widen earnings-print verification beyond XLE/MU") hit its Aug 7 review-by date having been complied with every session since 2026-07-24 (2+ weeks) with zero fresh incidents. Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate section) — see Rule Changelog. Retired from Active Lessons as promoted.
- L-005 ("cross-check extreme oil/WTI source dispersion") hit its Aug 7 review-by date having been complied with every session since 2026-07-24 (2+ weeks), correctly resolving oil-price dispersion via XLE/USO bars each time it triggered. Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate section) — see Rule Changelog. Retired from Active Lessons as promoted.
- L-006 ("flag same-week ex-div/analyst-action risk at entry") hit its Aug 7 review-by date having been complied with every session since 2026-07-24 (2+ weeks), checked at every new entry (ECL, CVX, LNG) with zero misses. Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate section) — see Rule Changelog. Retired from Active Lessons as promoted.
- New Buy-Side Gate calibration rule added per L-007's escalation directive (2nd consecutive missed-skewed skip-scoreboard week): for watchlist names with average daily volume under ~50,000 shares, the market-open bars-confirmation window extends to up to 60 minutes post-open (from the standard ~15-20 minutes) before ruling a catalyst reaction unconfirmed. Evidence: GRC (Jul 30, Ref $78.46) gate-failed on zero bars prints ~17 minutes post-open despite a genuine, today-dated Q2 beat, and was confirmed "missed" at +7.84% by Aug 6. Trailing stops, the -7% cut, position sizing caps, the 3-trades/week cap, and no-options remain untouched. Review-by 2026-08-21 (2 weekly reviews out) to check for false-positive entries introduced by the wider window.
- New lesson L-008 opened to monitor the new thin-liquidity confirmation window's effect on gate outcomes; L-009 opened to track continued under-deployment against the 75-85% target (see LESSONS.md).

### Overall Grade: C- (risk management held — no rule breaches, one clean well-confirmed entry (LNG) — but the bot lagged the S&P by 4.54% in the index's best week since mid-April, driven mainly by persistent under-deployment rather than any bad decision)

## Week ending 2026-08-14

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $97,790.18 |
| Ending portfolio | $99,587.90 |
| Week return | +$1,797.72 (+1.84%) |
| S&P 500 week | +0.41% (SPY 773.16 -> 776.30, Aug 7 close -> Aug 14 close via `alpaca.sh bars`; Perplexity again returned internally inconsistent figures — CNBC "+0.4%" vs WSJ's own Thursday "+0.65%"/Friday "-0.17%" reads, SPX close cited as both 7,798.99 and 7,785.76 — cross-checked against SPY ground-truth bars per established methodology) |
| Bot vs S&P | +1.43% |
| Trades | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades this week) |
| Best trade | N/A (no closed trades this week; CVX unrealized +3.22% strongest mover) |
| Worst trade | N/A (no closed trades this week; ECL unrealized -2.06% weakest mover) |
| Profit factor | N/A (no closed trades this week) |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No trades closed this week |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CVX | $193.860947 (95 sh) | $200.10 | +$592.71 (+3.22%) | Two 10% trailing GTC orders, 7f5acb83 (54 sh) + e328a200 (41 sh), stop $181.467, HWM $201.63 |
| ECL | $281.93 (70 sh) | $276.11 | -$407.40 (-2.06%) | 10% trailing GTC, order 64b1066c, stop $259.6005, HWM $288.445 |
| LNG | $263.63 (74 sh) | $271.64 | +$592.74 (+3.04%) | 10% trailing GTC, order 974c3bfc, stop $245.259, HWM $272.51 |

### Skip Scoreboard

Rows >= 5 sessions old scored this week (Ref -> +5 trading-session close, via `alpaca.sh bars`):

| Ticker | Ref (date) | +5d close | +5d % | Verdict |
|--------|------------|-----------|-------|---------|
| FANG | 198.53 (Aug 4) | 200.55 (Aug 11) | +1.02% | skip-right |
| VMC | 285.08 (Aug 5) | 279.86 (Aug 12) | -1.83% | skip-right |

Verdict counts (new rows this week): missed 0, skip-right 2, avoided-loss 0. Total missed gains: 0.00%. Total avoided losses: 0.00%. Missed:avoided ratio: 0:0 — the first non-missed-skewed read since the Aug 7 escalation (1:0 that week, 3:1 the week before). L-007's escalation threshold (missed count > avoided-loss count) is not met (0 = 0), so no further gate-calibration escalation this week — see Rule Change note below on L-007's disposition. GRC (Jul 30 row, scored "missed" +7.84% at the Aug 7 review) is 6 sessions past its scoring point, not yet past the 10-session retention threshold — retained one more review. MPC/COP/NEM/NUE (Aug 14 stall-breaker refresh rows) not yet 5 sessions old — carried forward. Pruned this review: LNG/FANG/VMC/FCX (Jul 20 rows) and XOM/CVX/ECL (Jul 21 rows) and GEV (Jul 22 row) — all verdicts scored at the Jul 31 review, whose scoring reference points are now 12-14 trading sessions old, past the 10-session retention threshold (this pruning was overdue by one review; the Jul 31 batch should have been pruned Aug 7 using the scoring-reference-point convention established by the MU precedent, not the verdict-fill date — corrected here).

### What Worked

- The bot beat the S&P this week (+1.84% vs +0.41%, +1.43% relative) with zero new trades — pure mark-to-market gains on CVX and LNG, both riding continued post-earnings strength, show the hold/trail discipline on existing positions can outperform the index even with the buy-side gate fully closed to new entries.
- Skip-scoreboard mix flipped back to non-missed-skewed this week — FANG and VMC (the Aug 4/Aug 5 gate-fails) both scored skip-right (+1.02%/-1.83%, 0 missed, 0 avoided-loss), reversing the two-review missed-skewed trend that triggered the Aug 7 thin-liquidity rule change. No further gate-tightening evidence needed right now.
- The stall-breaker correctly fired on Day 5 (today) and refreshed a genuinely stale watchlist — dropped GRC/FANG/VMC/FCX/XOM/GEV (all >=7 sessions stale with zero fresh catalysts), added MPC/COP/NEM/NUE from the two leading YTD sectors (Energy, Materials).
- Risk mechanics held clean all week: trailing stops on CVX and LNG mechanically ratcheted up multiple times with zero manual intervention, no position came within range of the -7% cut or the +15%/+20% tighten thresholds, and L-004/L-005/L-006 were checked every session with zero triggers or incidents.

### What Didn't Work

- Zero trades placed this week — the 3rd consecutive weekly-review close under the 75-85% deployment target (38.60% Jul 31, ~58% Aug 7, 58.68% Aug 14), with 0/3 weekly trade slots used. (Note: daily pre-market entries this week referred to this as the "5th/6th consecutive week/session" under-deployed — that count does not reconcile against the weekly-review record itself; flagged for correction, see Rule Change note.)
- The stall-breaker's fixed 5-consecutive-no-trade-day trigger meant today's watchlist refresh (MPC/COP/NEM/NUE) landed on the week's last session — zero trading days remained to act on it before this review, so the refresh structurally could not help this week's deployment.
- A third distinct EOD-snapshot data-integrity incident in two weeks: Aug 7's EOD entry was never logged, Aug 13's EOD entry was mislabeled with Aug 12's data (self-flagged same day), and Aug 10/13/14 all noted a logged-vs-Alpaca `last_equity` mismatch for the same `balance_asof` date — a recurring pattern, not isolated noise.
- ECL remains the week's laggard (-2.06% unrealized), the only position showing meaningful drawdown, though nowhere near the -7% cut.

### Key Lessons

- A zero-trade week is not automatically a losing week — this week's +1.43% relative outperformance came entirely from letting winning positions (CVX, LNG) run under their trailing stops, not from new activity.
- The stall-breaker's trigger timing is structurally mistimed: firing at exactly 5 no-trade days puts the refresh on a Thursday/Friday most weeks, leaving no runway in the same week to convert it into a trade.
- Three EOD-logging incidents in two weeks (missing, mislabeled, and value-mismatched entries) share one root cause — the routine reading account state before Alpaca's `balance_asof` has settled to the current session — and need an explicit guard rather than a fresh flag-and-continue each time.

### Adjustments for Next Week

- Lower the stall-breaker's watchlist-refresh trigger from 5 to 3 consecutive no-trade sessions, so a broadened screen has more of the week left to convert into an entry (L-010).
- Before logging any EOD snapshot, check the account's `balance_asof` field against today's date; if it lags, label the entry as provisional/live-pulled rather than committing it as the day's settled EOD close (L-011).
- Continue L-008's 2-review thin-liquidity-window check and L-009's deployment tracking (both already active, not yet due) — no new entries needed for these.

### Rule Change This Week

- L-007 ("monitor skip-scoreboard shift toward missed") hit its Aug 14 review-by date. Retired rather than extended: it already delivered its one intended escalation (Aug 7, leading to the thin-liquidity bars-confirmation-window rule change), and this week's newly-scored rows (FANG, VMC) came back skip-right/skip-right with zero missed verdicts — no continuation of the trend it was tracking. Its monitoring function is subsumed by the weekly review's standing skip-scoreboard computation (STEP 3) and rule-change escalation path (STEP 5), so no standalone lesson is needed going forward. No TRADING-STRATEGY.md change — this is a LESSONS.md-only retirement, not a promoted rule.
- No TRADING-STRATEGY.md rule changes this week. Trailing stops, the -7% cut, position sizing caps, the 3-trades/week cap, and no-options remain untouched.

## Week ending 2026-08-21

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $99,748.44 (Aug 17 Market-Open equity) |
| Ending portfolio | $100,920.73 (live pull; `balance_asof` 2026-08-20, one session lagged per L-011 — provisional) |
| Week return | +$1,172.29 (+1.18%) |
| S&P 500 week | -1.37% (SPY 776.30 -> 765.64, Aug 14 close -> Aug 21 close via `alpaca.sh bars`; Perplexity again returned dispersed reads — FRED -1.9%, ChartRow -1.1% for a "week ending Aug 18" row, Morningstar/WSJ tables inconsistent — cross-checked against SPY ground-truth bars per established methodology) |
| Bot vs S&P | +2.55% |
| Trades | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades this week) |
| Best trade | N/A (no closed trades this week; CVX unrealized +6.00% strongest mover) |
| Worst trade | N/A (no closed trades this week; ECL unrealized -0.11% weakest mover) |
| Profit factor | N/A (no closed trades this week) |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No trades closed this week |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CVX | $193.860947 (95 sh) | $205.49 | +$1,104.76 (+6.00%) | Two 10% trailing GTC orders, 7f5acb83 (54 sh) + e328a200 (41 sh), stop $188.082, HWM $208.98 |
| ECL | $281.93 (70 sh) | $281.63 | -$21.00 (-0.11%) | 10% trailing GTC, order 64b1066c, stop $259.6005, HWM $288.445 |
| LNG | $263.63 (74 sh) | $277.51 | +$1,027.12 (+5.27%) | 10% trailing GTC, order 974c3bfc, stop $253.56591, HWM $281.7399 |

### Skip Scoreboard

Rows >= 5 sessions old scored this week (Ref -> +5 trading-session close, via `alpaca.sh bars`):

| Ticker | Ref (date) | +5d close | +5d % | Verdict |
|--------|------------|-----------|-------|---------|
| MPC | 356.67 (Aug 13) | 360.595 (Aug 21) | +1.10% | skip-right |
| COP | 124.72 (Aug 13) | 134.92 (Aug 21) | +8.18% | missed |
| NEM | 114.18 (Aug 13) | 131.57 (Aug 21) | +15.23% | missed |
| NUE | 272.49 (Aug 13) | 243.61 (Aug 21) | -10.60% | avoided-loss |

Verdict counts (new rows this week): missed 2, skip-right 1, avoided-loss 1. Total missed gains: 23.41%. Total avoided losses: 10.60%. Missed:avoided ratio: 2:1 — the most missed-skewed read of the challenge so far, driven by COP (Q2 beat/CEO-transition thesis kept running) and especially NEM (Nevada Gold Mines settlement + gold-price rally, +15.23%), both skipped solely for lacking a same-day-dated catalyst. One-line judgment: the buy-side gate's catalyst-freshness requirement is now demonstrably too tight — half of this week's scored rows were missed gains more than double the one avoided loss — see Rule Change below. GRC (Jul 30 row, scored "missed" +7.84% at the Aug 7 review) is now 10 sessions past its scoring point — pruned this review per the 10-session retention threshold. FANG/VMC (Aug 4/Aug 5 rows, scored skip-right/skip-right at the Aug 14 review) are 5 sessions past their scoring point, not yet past the 10-session threshold — retained. XOM/PSX/STLD/MLM (Aug 19 refresh rows) are only 2 sessions old — not yet 5, carried forward.

### What Worked

- The bot beat the S&P this week (+1.18% vs -1.37%, +2.55% relative) with zero new trades — pure mark-to-market gains on CVX (+6.00% unrealized) and LNG (+5.27% unrealized) carried the week, echoing the Aug 14 review's pattern: hold/trail discipline on existing winners outperforming a down index even with the buy-side gate fully closed to new entries.
- Risk mechanics held clean all week: CVX and LNG trailing stops mechanically ratcheted up multiple times (stop-only-up, zero manual intervention), no position came within range of the -7% cut or the +15%/+20% tighten thresholds (max unrealized gain CVX +7.42% intraday Thursday, closed the week at +6.00%), and L-004/L-005/L-006 equivalents (now permanent Buy-Side Gate rules) plus L-008/L-009/L-010/L-011 were checked every session with zero fresh incidents.
- The Aug 18 full-day gap (no pre-market/market-open/midday/EOD entries logged at all) was correctly root-caused at the Aug 19 pre-market session — a Claude Code weekly usage-limit exhaustion, not a missed risk event or a commit/push failure — and confirmed benign against live account state (positions/stops unchanged, `balance_asof` advanced normally). No further action needed beyond the record noted here.

### What Didn't Work

- Zero trades placed this week — the 2nd consecutive zero-trade week (Week 6 Aug 10-14, Week 7 Aug 17-21) and the 6th consecutive weekly-review close under the 75-85% deployment target (~58.6% Aug 14, ~59.3% Aug 21), with 0/3 weekly trade slots used both weeks.
- The skip-scoreboard flipped hard missed-skewed this week (2 missed / 1 avoided-loss / 1 skip-right, vs 0/0/0 the prior review) — COP and NEM both cleared +3% within 5 sessions of being passed over, with NEM's +15.23% the single largest missed-gain read of the challenge so far. This is the concrete cost of the catalyst-freshness gate finally showing up in the numbers, not just a deployment-percentage abstraction.
- The Aug 18 full-day logging gap (pre-market/market-open/midday/EOD all missing) is a fourth distinct data-integrity incident of the challenge (after the Aug 7 gap and the two Aug-13-area EOD mislabeling/mismatch incidents) — this one has a confirmed benign external cause (usage-limit exhaustion), but the pattern of gaps in the persisted record continues.
- ECL remains the week's laggard (-0.11% unrealized, essentially flat), with a CEO insider sale (Aug 20) noted as informational-only but worth continued monitoring.

### Key Lessons

- A zero-trade week can still beat the index on pure hold/trail discipline (+2.55% relative this week), but that is not evidence the buy-side gate is correctly calibrated — this week's skip-scoreboard scoring shows the gate is leaving real money on the table (23.41% combined missed gains vs 10.60% avoided losses) by requiring same-day-dated catalysts on names whose theses (Q2 beats, a legal-overhang settlement) were genuine and still live 5+ sessions later.
- Two consecutive zero-trade weeks plus a 6th consecutive week under the deployment band plus a 2:1 missed-skewed skip-scoreboard is a convergence of three independent signals pointing at the same root cause — the catalyst-freshness window, not watchlist breadth or position sizing, is now the binding constraint on deployment.
- An external infrastructure gap (Claude Code usage-limit exhaustion) can silently take an entire trading day offline with zero risk-management exposure if positions/stops are already GTC and self-managing — the resilience of GTC trailing stops is what made the Aug 18 gap a non-event rather than an incident.

### Adjustments for Next Week

- Widen the buy-side gate's catalyst-freshness requirement from "must be dated today" to "dated today OR dated within the prior 2 trading sessions if confirmed by a second independent source" (L-012) — applied to TRADING-STRATEGY.md this week, see Rule Change below. Monitor at the next 2 weekly reviews for false-positive entries (a catalyst admitted under the wider window that reverses shortly after fill).
- Broaden the stall-breaker's sector screen beyond the current top-2 YTD sectors (Energy/Materials have now supplied 8 of the last 8 watchlist names across two refresh cycles) to include a 3rd sector when a refreshed watchlist goes through its first full re-arm cycle without producing a gate-clearing catalyst, so repeated refreshes stop recycling within the same two sectors (L-013).
- L-009 (track persistent under-deployment): extended rather than closed out — this week's 6-consecutive-week checkpoint was the trigger for this week's gate-calibration change (L-012); keep tracking consecutive under-deployed weeks post-change to see whether the wider catalyst-freshness window actually moves the deployment number.

### Rule Change This Week

- L-008 ("monitor thin-liquidity bars-confirmation window") hit its Aug 21 review-by date. Retired: zero new entries were made under the extended 60-minute window since the original Jul 30 GRC case across the full 2-review monitoring cycle, so there was nothing further to report and no false-positive evidence either way. No TRADING-STRATEGY.md change — the underlying rule (added Aug 7) stands; this is a LESSONS.md-only retirement of the monitoring lesson.
- New Buy-Side Gate calibration rule: catalyst-freshness requirement widened from "dated today" to "dated today OR dated within the prior 2 trading sessions if confirmed by a second independent source" — promoted from this week's LESSONS.md L-009 escalation (6th consecutive week under the 75-85% deployment target) and this week's skip-scoreboard evidence: COP (+8.18%) and NEM (+15.23%) both scored "missed" this review, passed over solely for lacking a same-day-dated catalyst despite genuine, still-live multi-session catalysts (Q2 beat/CEO transition; Nevada Gold Mines settlement + gold rally) — missed:avoided ratio 2:1, total missed gains 23.41% vs avoided losses 10.60%, the most missed-skewed read of the challenge. Also satisfies STEP 5's second-consecutive-zero-trade-week requirement (Week 6 Aug 10-14, Week 7 Aug 17-21). Process/gate calibration only — trailing stops, the -7% cut, position sizing caps, the 3-trades/week cap, and no-options all remain untouched. Review-by 2026-09-04 (LESSONS.md L-012) to check for false-positive entries introduced by the wider window.

### Overall Grade: B- (beat the S&P by 2.55% this week purely on existing-position mark-to-market gains and kept risk management perfectly clean, but a 2nd consecutive zero-trade week and a hard missed-skewed skip-scoreboard (23.41% missed vs 10.60% avoided) quantified, for the first time, a real cost to the catalyst-freshness gate's tightness — addressed this week with a bounded calibration change, not yet proven out)

### Overall Grade: B (beat the S&P by 1.43% and kept risk management clean with zero rule breaches, but zero trading activity for the third straight under-deployed week and a recurring EOD-logging data-integrity gap keep this from a higher grade)

## Week ending 2026-08-28

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $100,920.73 (Aug 21 close) |
| Ending portfolio | $101,290.96 |
| Week return | +$370.23 (+0.37%) |
| S&P 500 week | +0.48% (SPY 765.64 -> 769.28, Aug 21 close -> Aug 28 close via `alpaca.sh bars`; Perplexity again returned a higher, dispersed read (+0.7% per FRED) — cross-checked against SPY ground-truth bars per established methodology) |
| Bot vs S&P | -0.11% |
| Trades | 0 (W:0 / L:0 / open:0) |
| Win rate | N/A (no closed trades this week) |
| Best trade | N/A (no closed trades this week; LNG unrealized +7.09% strongest mover) |
| Worst trade | N/A (no closed trades this week; ECL unrealized +1.71% weakest mover, still positive) |
| Profit factor | N/A (no closed trades this week) |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No trades closed this week |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CVX | $193.860947 (95 sh) | $201.86 | +$759.91 (+4.13%) | Two 10% trailing GTC orders, 7f5acb83 (54 sh) + e328a200 (41 sh), stop $188.082, HWM $208.98 |
| ECL | $281.93 (70 sh) | $286.75 | +$337.40 (+1.71%) | 10% trailing GTC, order 64b1066c, stop $265.797, HWM $295.33 |
| LNG | $263.63 (74 sh) | $282.33 | +$1,383.80 (+7.09%) | 10% trailing GTC, order 974c3bfc, stop $256.068, HWM $284.52 |

### Skip Scoreboard

Rows >= 5 sessions old scored this week (Ref -> latest close as of this review, via `alpaca.sh bars`):

| Ticker | Ref (date) | +5d close | +5d % | Verdict |
|--------|------------|-----------|-------|---------|
| XOM | 165.61 (Aug 19) | 156.695 (Aug 28) | -5.38% | avoided-loss |
| PSX | 243.475 (Aug 19) | 244.095 (Aug 28) | +0.25% | skip-right |
| STLD | 249.85 (Aug 19) | 234.745 (Aug 28) | -6.05% | avoided-loss |
| MLM | 522.88 (Aug 19) | 530.91 (Aug 28) | +1.54% | skip-right |
| VST | 136.21 (Aug 21) | 137.10 (Aug 28) | +0.65% | skip-right |
| CEG | 272.83 (Aug 21) | 276.84 (Aug 28) | +1.47% | skip-right |
| MP | 60.02 (Aug 21) | 56.12 (Aug 28) | -6.50% | avoided-loss |
| AMAT | 492.12 (Aug 21) | 461.50 (Aug 28) | -6.22% | avoided-loss |

Verdict counts (new rows this week): missed 0, skip-right 4, avoided-loss 4. Total missed gains: 0.00%. Total avoided losses: -24.15% (sum of the four). Missed:avoided ratio: 0:4 — the most gate-favorable read since the Aug 21 catalyst-freshness widening (2:1 that week, 0:0 the week before), and a sharp reversal from the missed-skewed evidence that drove L-012. **Gate calibration verdict: sound this week — zero evidence the gate is too tight; if anything, every scored skip this week would have lost money or gone nowhere if bought.** ET/FCX/MRVL (Aug 26 refresh rows) are only 3 sessions old — not yet 5, carried forward. WMB/CRM/CRWD (Aug 28 refresh rows) are 1 session old — carried forward. Pruned this review: FANG (Aug 4 row, scored skip-right at the Aug 14 review, now 13 sessions past its scoring reference) and VMC (Aug 5 row, scored skip-right at the Aug 14 review, now 12 sessions past its scoring reference) — both past the 10-session retention threshold.

### What Worked

- The buy-side gate's discipline was fully vindicated this week: 0 missed / 4 skip-right / 4 avoided-loss on the newly-scored rows (XOM, PSX, STLD, MLM, VST, CEG, MP, AMAT) — a sharp reversal from the Aug 21 review's missed-skewed read that triggered the L-012 catalyst-freshness widening, with no evidence the gate is too tight this cycle.
- CRM and CRWD (Aug 28) were correctly identified as having genuine, well-confirmed, gate-clearing catalysts (Q2 beats, raised guidance, both independently confirmed by 4+ outlets) — and correctly NOT chased after already-realized +22.6%/+20.3% single-session moves, avoiding a same-day entry with real stop-out/give-back risk into a weekend gap. Flagged for a Tuesday Sept 1 pullback re-check (L-014) rather than abandoned.
- L-010's lowered stall-breaker trigger (5 -> 3 sessions) ran a full 2-week validation cycle cleanly: it correctly re-armed and refreshed the watchlist three separate times this week alone (Aug 24, 26, 28), giving each cycle more of the week's runway to convert, with zero fresh incidents — promoted to a permanent rule (see Rule Changes).
- Risk mechanics held clean all week: CVX/ECL/LNG all stayed positive (+4.13%/+1.71%/+7.09% unrealized at week end), no position came within range of the -7% cut or the +15%/+20% tighten thresholds (LNG's +7.09% is the closest, still well below +15%), and every L-011 EOD balance_asof check this week correctly flagged provisional snapshots with zero mislabeling incidents — promoted to a permanent Operational Rule (see Rule Changes).

### What Didn't Work

- Zero trades placed this week — the 3rd consecutive zero-trade week (Aug 10-14, Aug 17-21, Aug 24-28) and the 9th straight weekly-review close under the 75-85% deployment target (~59.37% today), despite the Aug 21 L-012 gate-widening intended to address exactly this.
- Unlike the Aug 21 review, this week's inaction wasn't a gate-calibration failure — CRM/CRWD cleared the widened L-012 window on catalyst grounds but were skipped on chase-risk/extension grounds instead, a distinct problem the gate was never designed to solve (opened as L-015 to track going forward).
- The Aug 28 stall-breaker refresh's Materials leg came up empty (recycled MP coverage, an illiquid micro-cap, a stale Aug 10 settlement) — the first time one of L-013's three sector legs has failed to produce a usable name, worth watching for recurrence (L-016).
- The bot finished the week -0.11% behind the S&P (+0.37% vs +0.48%) — essentially flat, tracking the index closely on existing-position mark-to-market gains alone, in a week the index itself was only modestly positive.

### Key Lessons

- A fully vindicated skip-scoreboard (0 missed, 4 avoided-loss) in the same week the bot also correctly passed on two genuinely gate-clearing catalysts (CRM/CRWD, on chase-risk grounds) shows two different mechanisms can both be working correctly at once while the deployment number still doesn't move — the binding constraint has shifted from "no catalyst" toward "catalyst confirmed but the move already happened," which needs a different fix (a pullback-entry process, not further gate widening).
- Two full weeks (Aug 14 - Aug 28) of clean L-010/L-011 compliance with zero fresh incidents is enough evidence to promote both to permanent rules, following the same bar used for L-001 through L-006.
- A single empty sector leg in an otherwise-working 3-sector screen (L-013) is not yet a pattern — worth tracking for a second consecutive occurrence before treating it as a screen-design problem.

### Adjustments for Next Week

- Re-check CRM (would-be entry ~$250-253, stop ~$232-235) and CRWD (would-be entry ~$225-230, stop ~$207-209) at the next session (Tue Sep 1, after the Labor Day close) and through the following 2-3 sessions for a clean pullback/consolidation entry; take it if the range tightens and the gate still clears (L-014).
- Track at the Sept 4 and Sept 11 reviews whether zero-trade weeks are being driven by "no catalyst" (would support further gate widening) or "catalyst confirmed but already realized" (would support building a bounded pullback-entry rule instead) (L-015).
- Watch whether the Materials leg of the L-013 3-sector screen comes up empty again on the next refresh cycle; if so on 2 consecutive cycles, propose a 4th sector or a loosened liquidity/market-cap floor for that leg (L-016).
- Continue L-009's deployment tracking (9th straight under-deployed week, checkpoint due 2026-09-04) and L-012's false-positive monitoring (review-by 2026-09-04) — both already active, not yet due for a decision.

### Rule Changes This Week

- L-010 ("lower stall-breaker re-arm trigger to 3 consecutive no-trade sessions") hit its Aug 28 review-by date having been complied with every session since 2026-08-14 (2 straight weeks) with zero fresh incidents — correctly re-armed and refreshed the watchlist 3 times this week alone (Aug 24, 26, 28). Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate, re-arm trigger 5+ -> 3+ sessions) — see Rule Changelog. Retired from Active Lessons as promoted.
- L-011 ("check EOD balance_asof before logging a snapshot") hit its Aug 28 review-by date having been complied with every EOD session since 2026-08-14 (2 straight weeks) with zero fresh mislabeling/mismatch incidents. Promoted to a permanent process rule in TRADING-STRATEGY.md (new Operational Rules section) — see Rule Changelog. Retired from Active Lessons as promoted.
- New lessons opened: L-014 (re-evaluate CRM/CRWD for a pullback entry), L-015 (track whether chase-risk has replaced catalyst-freshness as the binding deployment constraint), L-016 (watch for a 2nd consecutive empty Materials leg in the L-013 screen) — see LESSONS.md. No risk-rule changes — trailing stops, the -7% cut, position sizing caps, the 3-trades/week cap, and no-options remain untouched.

### Overall Grade: B- (buy-side gate discipline fully vindicated this week — 0 missed / 4 avoided-loss on the skip-scoreboard, and CRM/CRWD correctly not chased after already-realized 20%+ moves — but the 3rd consecutive zero-trade week and 9th straight under-deployed week, in a week the S&P edged higher, show the Aug 21 gate-widening hasn't yet moved deployment, with the evidence now pointing at chase-risk/entry-timing rather than catalyst-freshness as the real constraint)

## Week ending 2026-09-04

### Stats

| Metric | Value |
|--------|-------|
| Starting portfolio | $101,290.96 (Aug 28 close) |
| Ending portfolio | $102,030.13 (live pull; `balance_asof` 2026-09-03, one session lagged — provisional per Operational Rules) |
| Week return | +$739.17 (+0.73%) |
| S&P 500 week | +0.12% (SPY 769.28 -> 770.18, Aug 28 close -> Sep 4 close via `alpaca.sh bars`; Perplexity again returned partial/dispersed reads — FRED's weekly series had no Sep 4 print yet, ChartRow showed a Sep 3-dated "+0.5%" row — cross-checked against SPY ground-truth bars per established methodology) |
| Bot vs S&P | +0.61% |
| Trades | 1 (W:0 / L:0 / open:1 — ET) |
| Win rate | N/A (no closed trades this week) |
| Best trade | N/A (no closed trades this week; LNG unrealized +11.07% strongest mover) |
| Worst trade | N/A (no closed trades this week; ECL unrealized -0.94% weakest mover) |
| Profit factor | N/A (no closed trades this week) |

### Closed Trades

| Ticker | Entry | Exit | P&L | Notes |
|--------|-------|------|-----|-------|
| — | — | — | — | No trades closed this week |

### Open Positions at Week End

| Ticker | Entry | Close | Unrealized | Stop |
|--------|-------|-------|------------|------|
| CVX | $193.860947 (95 sh) | $208.60 | +$1,400.21 (+7.60%) | Two 10% trailing GTC orders, 7f5acb83 (54 sh) + e328a200 (41 sh), stop $191.87964, HWM $213.1996 |
| ECL | $281.93 (70 sh) | $279.28 | -$185.50 (-0.94%) | 10% trailing GTC, order 64b1066c, stop $265.797, HWM $295.33 |
| ET | $21.68 (900 sh) | $21.51 | -$153.00 (-0.78%) | 10% trailing GTC, order f900c3f3, stop $19.539, HWM $21.71 |
| LNG | $263.63 (74 sh) | $292.80 | +$2,158.58 (+11.07%) | 10% trailing GTC, order 974c3bfc, stop $269.253, HWM $299.17 |

### Skip Scoreboard

Rows >= 5 sessions old scored this week (Ref -> +5 trading-session close, via `alpaca.sh bars`):

| Ticker | Ref (date) | +5d close | +5d % | Verdict |
|--------|------------|-----------|-------|---------|
| ET | 21.03 (Aug 26) | 21.525 (Sep 2) | +2.35% | skip-right (moot — bot independently bought ET Sep 1 once the correctly-attributed Hugh Brinson catalyst confirmed) |
| FCX | 79.895 (Aug 26) | 73.945 (Sep 2) | -7.45% | avoided-loss |
| MRVL | 240.38 (Aug 26) | 206.57 (Sep 2) | -14.06% | avoided-loss |
| WMB | 74.19 (Aug 28) | 74.17 (Sep 4) | -0.03% | skip-right |
| CRM | 252.19 (Aug 28) | 259.30 (Sep 4) | +2.82% | skip-right |
| CRWD | 227.99 (Aug 28) | 213.045 (Sep 4) | -6.55% | avoided-loss |

Verdict counts (new rows this week): missed 0, skip-right 3, avoided-loss 3. Total missed gains: 0.00%. Total avoided losses: -28.06% (sum of FCX/MRVL/CRWD). Missed:avoided ratio: 0:3 — the 2nd straight gate-favorable read (0:4 last week, 0:3 this week), zero evidence the gate is too tight. **Notably, CRWD's Aug 28 skip scored avoided-loss (-6.55%)** — this is the same name whose Sept 2-4 pullback setup was independently blocked from a *new* entry purely by the 75-85% deployment cap (see What Worked); the cap's caution on CRWD this week is now doubly vindicated by both the original Aug 28 skip and the Sept 2-4 re-entry hold. MPC/COP/NEM/NUE (Aug 14 rows) are exactly 10 sessions past their Aug 21 scoring reference point — retained one more review per the "older than 10" threshold (MU precedent). XOM/PSX/STLD/MLM and VST/CEG/MP/AMAT (both scored at the Aug 28 review) are 5 sessions past their scoring reference point, not yet past 10 — retained. TRGP/AAPL/CRH (Sept 1 rows) are only 3 sessions old — carried forward.

### What Worked

- The 17-day no-trade streak (Aug 7-31) ended cleanly Sept 1 with ET: a hard-dated, multi-source-confirmed operational milestone (Hugh Brinson Pipeline Phase 1 full capacity), after the desk caught and corrected its own 3-session catalyst misattribution (the milestone had been wrongly credited to WMB, Aug 28-Sept 1) *before* placing the order — self-caught data-quality discipline working as intended, with zero capital ever at risk on the wrong premise.
- Deployment reached the 75-85% target band for the first time in the challenge and held there for all 5 sessions this week (78.75%-78.94%, Sept 1-4) — directly resolves L-009's multi-week tracking question, achieved via one clean trade (ET) plus existing-position appreciation, not by forcing extra entries.
- The skip-scoreboard came back gate-favorable for the 2nd straight review (0 missed / 3 skip-right / 3 avoided-loss this week, following 0/4/4 last week) — continued strong evidence against further gate-loosening.
- CRWD's deployment-cap-blocked non-entry (3 consecutive sessions, Sept 2-4 — thesis-intact, catalyst-cleared, but a standard-sized 5th position would have pushed deployment to ~97-99%) scored avoided-loss on its original Aug 28 skip (-6.55% by Sept 4) — the first direct evidence this challenge that the 75-85% cap itself, not just the catalyst gate, is correctly filtering risk rather than only costing missed gains.
- Risk mechanics held clean all week: no position came within range of the -7% cut or the +15%/+20% tighten thresholds (LNG's +12.45% Sept 3 high was the closest, pulling back to +11.07% by week end); CVX and LNG stops ratcheted mechanically, stop-only-up, with zero manual intervention.

### What Didn't Work

- Only 1 of 3 weekly trade slots used despite reaching the deployment band — the CRWD setup (thesis-intact, catalyst-cleared pullback) sat unexecuted for 3 straight sessions purely on the 75-85% deployment cap, an unresolved policy question (L-015) that now has real evidence on both sides of the ledger (this week's Sept 2-4 hold scored favorably; earlier "missed" reads like COP/NEM in August argued the opposite direction on the catalyst-freshness side specifically, a related but distinct constraint).
- An operational gap recurred: no TRADE-LOG.md entries exist for Sept 2 (Market-Open/Midday/EOD all missing) — a repeat of the Aug 18/Aug 25 gap pattern; held-position quantities confirmed unchanged the next session, so no trade was missed, but this is now the 5th distinct data-integrity incident of the challenge and the 2nd full-day logging gap specifically (after Aug 18).
- ECL and ET both closed the week modestly negative (-0.94%/-0.78% unrealized) — no thesis break in either, but neither position added value this week; ET's first week held was flat-to-down consolidation after its Sept 1 entry.
- The Sept 1 WMB->ET catalyst misattribution (a 3-session error, Aug 28-Sept 1) is a new failure mode distinct from L-001/L-002's numeric-print issues — a company/project-ownership attribution error on a real, dated project, not previously covered by any lesson or gate check.

### Key Lessons

- The 75-85% deployment cap, carried since inception purely as a hard risk constraint, showed its first real cost-benefit trade-off this week: it blocked a genuinely gate-clearing CRWD entry for 3 straight sessions, and that blocked entry would have gone on to lose money (Aug 28 Ref -6.55% by Sept 4) — direct evidence the cap is not simply leaving free money on the table right now, whatever the deployment-percentage optics suggested at the Aug 21/Aug 28 reviews when the book was under-deployed.
- Reaching and holding the 75-85% band for 5 straight sessions (Sept 1-4) resolves L-009's core tracking question: deployment did move into the target band within days of the Aug 21 gate-widening, though the mechanism was one clean same-day-catalyst trade (ET, which didn't actually need the widened window) plus mark-to-market appreciation on existing winners, not a wave of newly-admitted catalysts.
- A catalyst-attribution error (crediting a real, dated project milestone to the wrong ticker in a shared-pipeline/JV-style situation) is a distinct data-quality failure mode from anything L-001/L-002 cover — it was self-caught before any capital was risked this time, but the underlying research process should explicitly verify company/project ownership, not just catalyst date and independent confirmation, before adding a name to the watchlist under this kind of coverage.

### Adjustments for Next Week

- Track the L-015 deployment-cap question with this week's new evidence in hand (CRWD's cap-block scored avoided-loss): continue holding the cap as-is (no loosening) unless a future cap-blocked, thesis-intact setup scores "missed" by a wide margin — reconvene at the Sept 11 review per L-015's existing schedule (L-015 stays active).
- New process check: before adding a name to the watchlist under a shared pipeline/JV/multi-company-coverage catalyst, explicitly verify which company owns the project (not just that a catalyst is dated and independently confirmed), given the WMB->ET 3-session misattribution (L-017).
- Watch for a repeat of the Sept 2-style full-day TRADE-LOG gap — this is the 2nd full-day gap of the challenge (after Aug 18); if it recurs a 3rd time, treat it as a process problem needing a structural fix (e.g., an explicit end-of-day gap-check step) rather than another one-off flag (L-018).

### Rule Change This Week

- L-013 ("broaden stall-breaker sector screen beyond Energy/Materials") hit its Sept 4 review-by date having been complied with every refresh cycle since 2026-08-21 (2+ straight weeks: Aug 24, 26, 28, Sept 1 refreshes all screened a 3rd sector alongside Energy/Materials, surfacing AMAT, MRVL, and CRH) with zero fresh incidents. Promoted to a permanent process rule in TRADING-STRATEGY.md (Buy-Side Gate section) — see Rule Changelog. Retired from Active Lessons as promoted.
- L-009 ("track persistent under-deployment") and L-012 ("monitor widened catalyst-freshness window for false positives") both hit their Sept 4 review-by dates and are retired (not promoted) — see LESSONS.md for reasoning. No TRADING-STRATEGY.md changes from either; the underlying Aug 21 catalyst-freshness rule and the 75-85% deployment band both stand unchanged. No risk-rule changes this week — trailing stops, the -7% cut, position sizing caps, the 3-trades/week cap, and no-options remain untouched.

### Overall Grade: B+ (the 17-day no-trade streak ended on a clean, self-corrected catalyst; deployment reached the 75-85% target band for the first time this challenge and held all week; the skip-scoreboard came back gate-favorable for a 2nd straight review, with the CRWD case now directly vindicating the deployment cap itself — held back only by a recurring TRADE-LOG logging gap and a self-caught but real catalyst-attribution near-miss)
