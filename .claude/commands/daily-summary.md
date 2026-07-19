---
description: Local daily summary workflow. Uses .env credentials. No commit/push.
---

You are an autonomous trading bot. Stocks only. Ultra-concise.

You are running the daily summary workflow. Resolve today's date via:
DATE=$(date +%Y-%m-%d).

STEP 1 — Read memory for continuity:
- tail of memory/TRADE-LOG.md (find most recent EOD snapshot -> yesterday's
  equity, needed for Day P&L)
- Count TRADE-LOG entries dated today (for "Trades today")
- Count trades Mon-today this week (for 3/week cap)

STEP 2 — Pull final state of the day:
```bash
./scripts/alpaca.sh account
./scripts/alpaca.sh positions
./scripts/alpaca.sh orders
```

STEP 3 — Compute metrics:
- Day P&L ($ and %) = today_equity - yesterday_equity
- Phase cumulative P&L ($ and %) = today_equity - starting_equity
- Trades today (list or "none")
- Trades this week (running total)

STEP 4 — Append EOD snapshot to memory/TRADE-LOG.md:
### MMM DD — EOD Snapshot (Day N, Weekday)
**Portfolio:** $X | **Cash:** $X (X%) | **Day P&L:** ±$X (±X%) | **Phase P&L:** ±$X (±X%)
| Ticker | Shares | Entry | Close | Day Chg | Unrealized P&L | Stop |
**Notes:** one-paragraph plain-english summary. MUST state the
consecutive no-trade-day count ("Nth consecutive no-trade day") or
"streak reset — trade(s) placed today". Pre-market's stall-breaker reads
this counter.

STEP 5 — Send ONE ClickUp message (always, even on no-trade days). <= 15
lines:
```bash
./scripts/clickup.sh "EOD MMM DD ..."
```

This is a local run — do not commit or push. Leave the diff on disk for
review.
