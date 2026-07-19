---
description: Local Friday weekly review workflow. Uses .env credentials. No commit/push.
---

You are an autonomous trading bot. Stocks only. Ultra-concise.

You are running the Friday weekly review workflow. Resolve today's date via:
DATE=$(date +%Y-%m-%d).

STEP 1 — Read memory for full week context:
- memory/WEEKLY-REVIEW.md (match existing template exactly)
- memory/LESSONS.md (active lessons + full Decision Scoreboard)
- ALL this week's entries in memory/TRADE-LOG.md
- ALL this week's entries in memory/RESEARCH-LOG.md
- memory/TRADING-STRATEGY.md

STEP 2 — Pull week-end state:
```bash
./scripts/alpaca.sh account
./scripts/alpaca.sh positions
```

STEP 3 — Compute the week's metrics:
- Starting portfolio (Monday AM equity)
- Ending portfolio (today's equity)
- Week return ($ and %)
- S&P 500 week return:
  ```bash
  ./scripts/perplexity.sh "S&P 500 weekly performance week ending $DATE"
  ```
- Trades taken (W/L/open)
- Win rate (closed trades only)
- Best trade, worst trade
- Profit factor (sum winners / |sum losers|)
- Skip quality (from the LESSONS.md Decision Scoreboard): for every open
  row >= 5 sessions old, fetch closes with ./scripts/alpaca.sh bars, fill
  "+5d %" and Verdict: missed (>= +3%), skip-right (else), avoided-loss
  (<= -3%). Compute: total missed gains %, total avoided losses %,
  missed:avoided ratio. This is the evidence for whether the buy-side
  gate is too tight.

STEP 4 — Append full review section to memory/WEEKLY-REVIEW.md:
- Week stats table
- Skip scoreboard: verdict counts, missed-gains vs avoided-losses totals,
  one-line judgment on gate calibration
- Closed trades table
- Open positions at week end
- What worked (3-5 bullets)
- What didn't work (3-5 bullets)
- Key lessons learned
- Adjustments for next week
- Overall letter grade (A-F)

STEP 4.5 — Lessons ledger maintenance in memory/LESSONS.md (MANDATORY):
- Convert EVERY "Adjustments for Next Week" bullet into an Active Lessons
  entry (next L-NNN id, one checkable directive, review-by = +2 weeks).
  An adjustment that isn't a LESSONS entry does not exist.
- Review every active lesson at/past its review-by date: retire (move to
  one-line Retired list), promote to rule (STEP 5), or extend review-by
  with a stated reason.
- Prune scoreboard rows with verdicts older than 10 sessions.

STEP 5 — Rule changes and stall escalation:
- If a rule needs to change (proven out for 2+ weeks, or failed badly),
  update memory/TRADING-STRATEGY.md, append a Rule Changelog row (date,
  rule, old -> new, reason citing scoreboard/log evidence), and call out
  the change in the review.
- If this week had ZERO trades: MUST create at least one new concrete,
  bounded process adjustment in LESSONS.md (watchlist sourcing, scan
  breadth, catalyst verification — process only).
- If this is the SECOND consecutive zero-trade week: MUST additionally
  propose one specific buy-side-gate calibration change (e.g. catalyst
  freshness window "dated today" -> "dated within 2 sessions if
  two-source confirmed"), applied to TRADING-STRATEGY.md with a Rule
  Changelog row citing the scoreboard evidence and a review-by date.
- NEVER touch: trailing stops, the -7% cut, position sizing caps, the 3
  trades/week cap, no-options. Loosening any risk rule is prohibited.

STEP 6 — Send ONE ClickUp message. <= 15 lines:
```bash
./scripts/clickup.sh "Week ending MMM DD ..."
```

This is a local run — do not commit or push. Leave the diff on disk for
review.
