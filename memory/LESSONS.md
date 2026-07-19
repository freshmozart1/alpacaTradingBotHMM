# Lessons & Decision Scoreboard

Read every pre-market and market-open session. Active directives are
BINDING — each pre-market entry must confirm compliance per lesson.
Keep small: max ~7 active lessons, ~15 open scoreboard rows. Weekly
review retires/promotes/prunes (see weekly-review STEP 4.5).

## Active Lessons

Template:

### L-NNN — <short title>
- Date: YYYY-MM-DD | Source: <WEEKLY-REVIEW date / RESEARCH-LOG date / manual>
- Lesson: <what was observed>
- Directive: <one concrete, checkable instruction>
- Status: active | Review-by: YYYY-MM-DD

### L-001 — XLE/MU Perplexity output unreliable
- Date: 2026-07-15 | Source: RESEARCH-LOG 2026-07-15..17 data-quality flags
- Lesson: Perplexity repeatedly returned fabricated/stale figures for XLE
  and MU (invented geopolitical narratives, MU quoted at ~10x its real
  price, verbatim-repeated prints), recurring across sessions.
- Directive: No XLE or MU catalyst counts toward the buy-side gate unless
  confirmed by a second independent source (WebSearch, or
  ./scripts/alpaca.sh quote/bars for any price claim).
- Status: active | Review-by: 2026-07-31

### L-002 — Verify suspect repeated macro prints
- Date: 2026-07-17 | Source: RESEARCH-LOG 2026-07-17 (VIX verbatim repeat)
- Lesson: Macro quotes (VIX, futures) sometimes return the prior session's
  print as "today"; futures also produced a contract-rollover artifact.
- Directive: If any macro print exactly matches the prior session's logged
  value, flag it suspect and cross-check before using it in Risk Factors.
- Status: active | Review-by: 2026-07-31

### L-003 — Widen watchlist beyond recycled tickers
- Date: 2026-07-10 | Source: WEEKLY-REVIEW 2026-07-10 Adjustments (not acted on wk of Jul 13)
- Lesson: 4 fixed tickers scanned 5+ days produced 0 dated catalysts; the
  name pool, not the market, is the bottleneck.
- Directive: When the stall-breaker in pre-market STEP 3 is armed (>= 5
  consecutive no-trade days), the watchlist refresh is mandatory, not
  optional.
- Status: active | Review-by: 2026-07-24

## Retired Lessons

- (none yet — one line each: L-NNN, title, retired YYYY-MM-DD, reason)

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
| 2026-07-06 | KALU | HOLD — no dated catalyst | backfill | | |
| 2026-07-06 | GRC | HOLD — no dated catalyst | backfill | | |
| 2026-07-06 | FTAI | HOLD — no dated catalyst | backfill | | |
| 2026-07-10 | MU | HOLD — single-day breakout, gate needs dated catalyst | backfill | | |

Backfill note (first live session with Alpaca access): replace each
"backfill" with the ticker's close on the row's Date via
`./scripts/alpaca.sh bars SYM 1Day <date> <date>`, then delete this note.
