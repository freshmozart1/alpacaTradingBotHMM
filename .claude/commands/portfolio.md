---
description: Read-only snapshot of account, positions, open orders, and stops
---

Print a clean ad-hoc snapshot. No state changes, no orders, no file writes.

1. bash scripts/alpaca.sh account
2. bash scripts/alpaca.sh positions
3. bash scripts/alpaca.sh orders

Format the output as a single concise summary:

Portfolio — <today's date>
Equity: $X | Cash: $X (X%) | Buying power: $X
Daytrade count: N/4 | PDT: <bool>

Positions:
  SYM | Sh | Entry -> Now | Unrealized P&L | Stop

Open orders:
  TYPE | SYM | qty | trail/stop | order_id

No commentary unless something is broken (position without a stop, or a
stop below current price).
