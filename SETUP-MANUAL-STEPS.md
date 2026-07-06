# Setup — Manual Steps

Everything in this file has to be done by you. Claude can help you fill in
prompts and review commits, but it cannot sign up for accounts, click
buttons in web UIs, or set routine-level environment variables and model
selections on your behalf.

## 1. Accounts

- [ ] **Alpaca** — sign up at alpaca.markets. Start with a **paper trading**
      account (recommended — this scaffold defaults to paper). Note your
      `ALPACA_API_KEY` and `ALPACA_SECRET_KEY`.
- [ ] **Perplexity** — sign up for API access at perplexity.ai. Note your
      `PERPLEXITY_API_KEY`.
- [ ] **ClickUp** — sign up at clickup.com. Create a **Chat channel**
      dedicated to bot notifications. Note:
      - `CLICKUP_API_KEY` (personal API token)
      - `CLICKUP_WORKSPACE_ID` (numeric)
      - `CLICKUP_CHANNEL_ID` (format `4-XXXXXXX-X`)

## 2. GitHub repository

- [ ] Create a new **private** GitHub repository.
- [ ] Push this scaffold to it:
      ```
      cd "~/Claude Workspace/alpacaTradingBot"
      git remote add origin <your-repo-url>
      git push -u origin main
      ```

## 3. Local smoke test

- [ ] Copy `env.template` to `.env` and fill in your **paper** credentials.
      Never commit `.env` — it's gitignored.
- [ ] Open this repo in Claude Code, run `/portfolio`. You should see
      account and positions print cleanly with $0 in positions and your
      starting paper balance.

## 4. Install the Claude GitHub App

- [ ] Visit the Claude GitHub App install page, select **only this repo**
      (least privilege), and grant access. This lets the cloud container
      clone and push to your repo.
- [ ] Alternative: run `/web-setup` inside Claude Code to sync your `gh` CLI
      token — same effect.

## 5. Create the five cloud routines

Repeat for each of the five files in `routines/` (full walkthrough also in
`routines/README.md`):

- [ ] In Claude Code cloud: **Routines → New Routine**.
- [ ] Name it (e.g. "Trading bot pre-market").
- [ ] Select this repository and branch `main`.
- [ ] **Model: select Claude Sonnet 5 (`claude-sonnet-5`).** This is the key
      change from the original Opus 4.7 blueprint — do this for all five
      routines, not just one.
- [ ] Add all environment variables from step 1 above (as routine env vars,
      **not** a `.env` file).
- [ ] Toggle on **"Allow unrestricted branch pushes"** in the routine's
      environment settings. Skipping this is the #1 reason first-time
      setups break (`git push` fails silently with a proxy error).
- [ ] Set the cron schedule + timezone `America/Chicago` (see
      `routines/README.md` for the five expressions).
- [ ] Paste the corresponding `routines/*.md` file verbatim into the prompt
      field.
- [ ] Save, then click **"Run now"** once to verify it works before relying
      on the schedule.

## 6. First week

- [ ] Watch every "Run now" test and read the logs.
- [ ] Confirm each run's expected memory file was written, committed, and
      pushed (`git log origin/main`).
- [ ] Keep watching daily for the first week. Read every commit the agent
      makes.

## 7. Going live (optional, later)

Only after you're confident in paper-trading behavior:

- [ ] In `.env` (local) and in each routine's environment variables
      (cloud), change `ALPACA_ENDPOINT` from
      `https://paper-api.alpaca.markets/v2` to
      `https://api.alpaca.markets/v2`, and swap in your **live** Alpaca API
      key/secret (paper and live use different key pairs).
- [ ] This is a deliberate, manual switch — nothing in this scaffold
      escalates to live trading on its own.
