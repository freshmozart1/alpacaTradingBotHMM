# Alpaca Trading Bot — Sonnet 5 Edition

A fully autonomous swing-trading agent that runs on a daily schedule. Five cron
jobs fire throughout each weekday, each one spinning up a fresh Claude Code
cloud container that clones this repo, reads memory, pulls live account
state, decides on action, places real orders if warranted, writes new memory,
commits everything back to Git, and sends a chat notification.

There is no separate Python bot process. Claude is the bot. Every scheduled
run is a fresh LLM invocation reading a well-defined prompt.

This is an adaptation of Nate Herk's original "Opus 4.7 Trading Bot" blueprint,
updated to run on **Claude Sonnet 5** (`claude-sonnet-5`) instead of Opus 4.7.
See [Why Sonnet 5](#why-sonnet-5) below for what changed and why.

## The five daily jobs at a glance

- **Pre-market** (early morning): research catalysts, write today's trade
  ideas to the research log.
- **Market-open** (shortly after the bell): execute planned trades, set
  trailing stops on every new position.
- **Midday**: scan open positions, cut losers, tighten stops on winners.
- **Daily summary** (late afternoon): snapshot portfolio state, send chat
  recap.
- **Weekly review** (Friday afternoon): compute weekly stats, grade
  performance, update the strategy if needed.

## Why this design

- **Stateless runs** — each firing is independent; failures self-heal on the
  next tick.
- **Git as memory** — every piece of state is a markdown file committed to
  `main`. Free versioning, diffs, rollback, human-readable audit trail.
- **Hard rules as gates** — strategy discipline is enforced programmatically
  before every order, not left to interpretation.

## Why Sonnet 5

This bot never calls the Anthropic API directly from the wrapper scripts —
Claude Code itself _is_ the trading agent. So "migrating" this blueprint to
Sonnet 5 is really about which model powers the Claude Code sessions and
routines, not any SDK code.

- **Model ID:** `claude-sonnet-5` (no date suffix). Pinned locally in
  `.claude/settings.json`; must be selected explicitly on each cloud routine
  (see [SETUP-MANUAL-STEPS.md](./SETUP-MANUAL-STEPS.md)).
- **Pricing:** $3 / $15 per million input/output tokens (introductory $2 / $10
  through 2026-08-31), versus $5 / $25 for Opus-tier. At five runs per weekday,
  this is meaningfully cheaper while reaching near-Opus quality on the
  agentic/coding-shaped work this bot does (reading logs, calling wrappers,
  writing structured markdown).
- **Behavior notes baked into the prompts below:**
  - Sonnet 5 follows instructions more literally than Opus 4.7 — the routine
    prompts spell out scope explicitly (e.g. "for **every** open position")
    rather than relying on the model to generalize.
  - Sonnet 5 is more agentic by default and handles self-verification loops
    well, so every routine now confirms an order landed against live Alpaca
    state (via `scripts/alpaca.sh orders`/`positions`) before logging or
    announcing it — closing a partial-failure gap in the original blueprint.
  - Claude Code defaults Sonnet 5 to `xhigh` effort, which is the right
    setting for the order-gating logic in market-open and midday.

## Repository layout

```
alpacaTradingBot/
├── CLAUDE.md              # Agent rulebook (auto-loaded every session)
├── README.md              # This file
├── SETUP-MANUAL-STEPS.md  # Steps only you can do (accounts, GitHub App, routines)
├── env.template           # Template for local .env file
├── .gitignore             # Excludes .env and the ClickUp fallback file
├── .claude/
│   ├── settings.json      # Pins the model to claude-sonnet-5
│   └── commands/          # Ad-hoc slash commands for local use
│       ├── portfolio.md
│       ├── trade.md
│       ├── pre-market.md
│       ├── market-open.md
│       ├── midday.md
│       ├── daily-summary.md
│       └── weekly-review.md
├── routines/               # Cloud routine prompts (the prod path)
│   ├── README.md
│   ├── pre-market.md
│   ├── market-open.md
│   ├── midday.md
│   ├── daily-summary.md
│   └── weekly-review.md
├── scripts/                 # API wrappers (the only way to touch the outside world)
│   ├── alpaca.sh
│   ├── perplexity.sh
│   └── clickup.sh
└── memory/                   # Agent's persistent state (committed to main)
    ├── TRADING-STRATEGY.md
    ├── TRADE-LOG.md
    ├── RESEARCH-LOG.md
    ├── WEEKLY-REVIEW.md
    └── PROJECT-CONTEXT.md
```

Two parallel execution modes share this codebase:

- **Local mode**: you invoke slash commands like `/pre-market` manually inside
  Claude Code. Credentials come from a local `.env` file. Good for testing and
  ad-hoc runs.
- **Cloud mode**: Claude's cloud routines fire each `routines/*.md` prompt on
  a cron. Credentials come from the routine's environment variables. No
  `.env` file. This is the production path.

## Paper trading by default

Unlike the original blueprint (which defaulted straight to a live account),
`env.template` here defaults to **Alpaca paper trading**
(`https://paper-api.alpaca.markets/v2`). The live endpoint is included but
commented out with a warning. Switching to live trading is a deliberate,
manual step — see `env.template`.

## Trading strategy — hard rules (non-negotiable)

- No options. Ever. Stocks only.
- Maximum 5-6 open positions at a time.
- Maximum 20% of equity per position.
- Maximum 3 new trades per week.
- Target 75-85% of capital deployed.
- Every position gets a 10% trailing stop placed as a real GTC order. Never
  mental.
- Cut any losing position at -7% from entry. Manual sell. No hoping, no
  averaging down.
- Tighten the trailing stop to 7% when a position is up +15%. Tighten to 5%
  when up +20%.
- Never tighten a stop to within 3% of current price. Never move a stop down.
- Exit an entire sector after 2 consecutive failed trades in that sector.
- Follow sector momentum. Don't force a thesis if the whole sector is rolling
  over.
- Patience beats activity. A week with zero trades can be the right answer.

Full strategy detail, the buy-side gate, and the sell-side rules live in
[memory/TRADING-STRATEGY.md](./memory/TRADING-STRATEGY.md).

## Memory model

Five markdown files, all committed to `main`, are the agent's only state
between runs.

| File                  | Purpose                                        | Write Cadence                                  |
| --------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `TRADING-STRATEGY.md` | The rulebook. Every workflow reads this first. | Only updated Friday if a rule proves out/fails |
| `TRADE-LOG.md`        | Every trade + daily EOD snapshot               | Every trade, every EOD                         |
| `RESEARCH-LOG.md`     | One dated entry per day                        | Every pre-market, optional midday addendum     |
| `WEEKLY-REVIEW.md`    | Friday recaps with letter grade                | Weekly                                         |
| `PROJECT-CONTEXT.md`  | Static background, mission, platform           | Rarely updated                                 |

## Replication checklist

- [ ] Create a new private GitHub repository, push this scaffold to `main`.
- [ ] Run `chmod +x scripts/*.sh` (already done in this scaffold, verify with
      `ls -l scripts/`).
- [ ] Copy `env.template` to `.env` locally. **Never commit a real `.env`.**
- [ ] Sign up for Alpaca (paper to start), Perplexity, ClickUp.
- [ ] Create a ClickUp chat channel for bot notifications. Note the workspace
      ID and channel ID.
- [ ] Local smoke test: fill in `.env`, open this repo in Claude Code, run
      `/portfolio`. You should see account and positions print cleanly.
- [ ] Install the Claude GitHub App on your repo (see
      `SETUP-MANUAL-STEPS.md`).
- [ ] Create the first cloud routine (pre-market) per `SETUP-MANUAL-STEPS.md`.
      **Select Sonnet 5 as the routine's model.**
- [ ] Hit "Run now" and watch the logs. Verify research log entry written,
      committed, pushed.
- [ ] If that works, create the other four routines with the same pattern.
- [ ] Monitor the first week closely. Read every commit the agent makes.

See [SETUP-MANUAL-STEPS.md](./SETUP-MANUAL-STEPS.md) for the full step-by-step
walkthrough of everything only you (the human) can do.

## Cron schedule (`America/New_York` — market-anchored)

| Routine       | Cron (America/New_York) | America/New_York time           |
| ------------- | ----------------------- | ------------------------------- |
| Pre-market    | `20 9 * * 1-5`          | 9:20 AM weekdays                |
| Market-open   | `25 9 * * 1-5`          | 9:25 AM weekdays (market open)  |
| Midday        | `00 12 * * 1-5`         | Noon weekdays                   |
| Daily-summary | `0 16 * * 1-5`          | 4:00 PM weekdays (market close) |
| Weekly-review | `0 17 * * 5`            | 5:00 PM Fridays only            |

> **Not in the `America/New_York` timezone?** These cron expressions are
> written for the `America/New_York` timezone because the bot's schedule is
> anchored to US market hours. If you don't live in New York, adjust the cron
> expressions to match your local time, but make sure they run at `America/New_York` local time.

## First-run troubleshooting

| Symptom                                      | Cause                                                          | Fix                                                                                              |
| -------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| "Repository not accessible" / clone fails    | Claude GitHub App not installed                                | Install it, grant access to the specific repo                                                    |
| `git push` fails with proxy/permission error | "Allow unrestricted branch pushes" toggle is off               | Enable it in the routine's environment                                                           |
| `ALPACA_API_KEY` not set in environment      | Env var missing from routine env                               | Add it in the routine config, not the repo's `.env`                                              |
| Agent creates a `.env` file anyway           | Prompt was paraphrased and lost the "DO NOT create .env" block | Re-paste prompt from `routines/*.md` exactly                                                     |
| Yesterday's trades missing from today's run  | Previous run didn't commit+push                                | Check `git log origin/main`. Re-verify the commit-and-push step of the prompt                    |
| Push fails "fetch first" / non-fast-forward  | Another run pushed between this one's clone and push           | The prompt handles this with `git pull --rebase`. If looping, check for an actual merge conflict |
| ClickUp message didn't arrive                | One of the three `CLICKUP_*` vars is missing                   | Script silently falls back to a local file. Add the missing vars                                 |
| Perplexity calls didn't happen               | `PERPLEXITY_API_KEY` missing                                   | Script exits 3, agent falls back to WebSearch. Add the key or accept fallback                    |
| Alpaca rejects stop with PDT error           | Same-day stop on same-day buy                                  | Prompt's fallback ladder handles this. If not cascading, re-paste that step verbatim             |

## Notification philosophy

Most bots are chatty. This one is not.

- **Pre-market**: silent unless something is genuinely urgent.
- **Market-open**: only if a trade was placed.
- **Midday**: only if action was taken (a sell, a stop tightened, a thesis
  exit).
- **Daily-summary**: always sends, one message, under 15 lines.
- **Weekly-review**: always sends, one message, headline numbers.

The cost of a missed notification is low (you can always check the portfolio
ad-hoc). The cost of a chatty bot is high (you stop reading the messages, and
then you miss the one that mattered).

## International Wire Transfers

To save fees of international wire transfers from banks to Alpaca, it is recommended to transfer
the money through a Wise account, because Wise participates in the ACH network.
