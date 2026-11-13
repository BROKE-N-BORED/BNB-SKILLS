# Org repo audit queue

## When to use

- Use this skill when the user asks you to review every repo in
  their GitHub account or org — one repo at a time, in an agreed
  order, each with the same fixed report shape.
- Use it for the queue management around the reviews, not for a
  single product review (see full-product-review for one codebase
  reviewed on its own).
- Audits are read-only. No pushes, no releases, no edits — and
  per-repo fixes only when the user asks about that repo.

## Start from a live listing, never from memory

- List the repos live on GitHub first (see the
  org-repo-inventory tool). Audit ONLY repos that exist live.
  Never audit a repo from conversation history: a repo named in
  an old conversation may not exist, may have been renamed, or
  may have been deleted — auditing it anyway is the failure this
  rule was written from.
- Re-list when the queue is refreshed. Repos appear during the
  day: this account went from 17 to 24 to 25 to 27 live repos
  across one day as new projects were created. New repos get
  appended to the queue in their order slot, never skipped.
- Note private repos in the list (they exist but show less
  without a token) and never claim a private repo is empty from
  a public-only listing.

## Keep a queue file

- One queue file per audit cycle, with one repo per line: order
  number, name, creation date, and state — DONE + DELIVERED with
  the report path and time, IN PROGRESS, or pending.
- The order is the owner's pick. Oldest-first by creation date
  is one valid order; newest-first is another. If a repo is
  already being audited when the order changes, let it finish
  and report it out of order — the new order decides everything
  after it.
- Record the standing rules in the queue file header: live-only,
  read-only, no pushes or releases, fixes only on his ask, and
  which thread owns pushes for a repo (audit here, pushes
  elsewhere).
- Under the no-stalling rule, roll straight from one repo to the
  next: verify each report, deliver it, immediately start the
  next repo. Stop when the list is done.

## Use the fixed report shape

- Every report covers the same ground: what the repo is,
  features, functions, strengths, weaknesses, gaps, UI flaws,
  innovation suggestions, design suggestions, anything new or
  needing improvement, update, or upgrade — and a ranked top-5
  recommendation list.
- Ground the "what it is" in facts read live: file count and
  sizes, commit count and head, last push date, open issues and
  PRs, license, .gitignore, description. Read the decisive files
  yourself (a main.js with every import commented out, a 0-byte
  manifest) instead of trusting the README's claims about them.
- Say plainly when there is no UI ("No UI exists, so nothing to
  review there") instead of inventing UI flaws.
- End every report with a "could not verify" section: branch
  lists, topics, release state, and anything the read tools
  cannot reach. A gap in the tools is a gap in the report, not a
  finding.
- Write the full report to a file in the audit directory and
  deliver the headlines in chat. Reports are NOT pushed to
  GitHub — no repo or release step exists for an audit.

## Verify metadata live at delivery time

- Repo descriptions and topics change during the day. Never trust
  an earlier listing or an audit brief for metadata — re-check
  the description live at the moment you deliver, and strike a
  claim that went stale rather than reporting it twice.
- GitHub code search returns zero results for these repos. Never
  claim a repo-wide count (TODOs, occurrences of a name) from it.
  Every count comes from directory listings and files actually
  read.
- Verify any claimed typo byte-for-byte against the live file
  before reporting it. A typo claim from a stale draft is a false
  finding.

## Name placeholders plainly

- A placeholder repo gets a short, honest verdict: one file, N
  bytes, one commit, untouched for X months. No padding, no
  invented potential.
- The top recommendation for a placeholder is a decision: build
  it or delete it. Deletion is the owner's call — recommend it,
  never do it.
- If a placeholder is kept, the first work is a real README (one
  paragraph: what it is, what it does, where it runs) plus
  LICENSE and .gitignore, before any code lands.

## Where this comes from

- Run in thread b074e650 on 2026-11-12 for BROKE-N-BORED: 27
  repos queued oldest-first in
  `~/workspace/github-audit/queue-2026-11-12.md`, six reports
  delivered the same day (CODE-FORGE, ChatBridgev1.0,
  MTAmorphai, K.ai-, FRIDAY, OpenRealism). The live-only rule
  came from Joshua's correction the same day, after a repo from
  conversation history (WinTux) was audited that does not exist
  live.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for the live
  repo listing and file reads.
- Use `muse.connector_search` to find other connectors and
  `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or
  MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer a different order (newest-first, most-active-first) when
  the owner has not picked one, instead of assuming oldest-first.
- Offer to re-run the queue later as a second cycle once fixes
  have landed, rather than re-auditing a repo mid-cycle.
