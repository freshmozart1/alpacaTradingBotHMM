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
