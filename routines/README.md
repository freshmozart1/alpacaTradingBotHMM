# Cloud Routines

These five files are the prompts you paste verbatim into Claude Code cloud
routines. This is the production path — each firing is an ephemeral
container: clone, run, destroy.

**Do not paraphrase these prompts.** The environment-variable check and the
commit-and-push step are load-bearing — Claude skips the final push in
roughly 10% of runs without the loud persistence reminder.

## Setting up a routine

For each of the five files below:

1. In Claude Code cloud, go to **Routines → New Routine**.
2. Name the routine (e.g. "Trading bot pre-market").
3. Select this repository (requires the Claude GitHub App — see
   `../SETUP-MANUAL-STEPS.md`).
4. Select branch: `main`.
5. **Model: select `claude-sonnet-5`** (Claude Sonnet 5). This is a routine
   setting in the UI, not something the prompt text controls — do this
   explicitly for every one of the five routines.
6. Add all environment variables listed in `env.template` (as routine
   environment variables, never a `.env` file — see `../CLAUDE.md` and each
   prompt's ENVIRONMENT VARIABLES block for why).
7. Toggle on **"Allow unrestricted branch pushes"**. Without this, `git push
origin main` silently fails with a proxy error — the #1 reason first-time
   setups break.
8. Set the cron schedule and timezone (see table below).
9. Paste the prompt from the matching file below into the prompt field.
   Copy everything verbatim — do not paraphrase.
10. Save, then click **"Run now"** once to test. Don't wait until tomorrow
    morning to discover it's broken.

## The five cron schedules (`America/New_York`)

| Routine            | Cron           | America/New_York time                       |
| ------------------ | -------------- | ------------------------------------------- |
| `pre-market.md`    | `0 6 * * 1-5`  | 6:00 AM weekdays                            |
| `market-open.md`   | `30 8 * * 1-5` | 8:30 AM weekdays (market opens 8:30 AM ET)  |
| `midday.md`        | `0 12 * * 1-5` | Noon weekdays                               |
| `daily-summary.md` | `0 15 * * 1-5` | 3:00 PM weekdays (market closes 3:00 PM ET) |
| `weekly-review.md` | `0 16 * * 5`   | 4:00 PM Fridays only                        |

**Not in the `America/New_York` timezone?** See the main [README.md](../README.md) for details.
