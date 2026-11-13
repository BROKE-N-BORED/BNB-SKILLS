# S56 — Org repo audit queue

## When to use

- Use this skill when the user asks you to review every repo in
  their GitHub account or org — one repo at a time, in an agreed
  order, each with the same fixed report shape.
- Use it for the queue management around the reviews, not for a
  single product review (see [full-product-review](../full-product-review/SKILL.md) for one codebase
  reviewed on its own).
- Audits are read-only. No pushes, no releases, no edits — and
  per-repo fixes only when the user asks about that repo.

## Start from a live listing, never from memory

- List the repos live on GitHub first (see the
  [org-repo-inventory tool](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/org-repo-inventory) (T20, BNB TOOLS)). Audit ONLY repos that exist live.
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

## After delivery: turn the audit into tasks (owning thread only)

- An audit becomes work only when the owner pastes it into the
  owning thread and asks for tasks. An audit sitting in the audit
  thread is a report, not a work order — never apply one
  unprompted.
- Verify the big claims before writing the list: reproduce the
  headline bug, or read the code the claim names. The DUO list
  was written only after the agreement bug was reproduced live
  ("I disagreed" ending a relay); the OLLAMA list opened with two
  corrections to its audit (Release v5 did exist; the detail view
  never showed the model's words); the Pixel Forge list checked
  `add_sheet` in code before writing the sheet-meta task. A task
  built on an unverified claim is rework waiting to happen.
- Top 5 first: the audit's ranked top-5 recommendations become
  the first tasks, in the audit's order. If the owner says to
  pull the Top 5 forward, they jump the existing queue — that is
  a reorder, not a rewrite.
- Append to the mounting task list in the audit's order, in a new
  audit section, and state the count: 25 tasks plus 2 ideas
  (DUO), 14 tasks (OLLAMA), 13 tasks numbered 62–74 (Pixel
  Forge), 21 tasks (getcompute). Ideas stay separate from tasks.
- Size each task (Small / Medium) and rank P0/P1 where the thread
  uses it, so the no-stall cycle can run the list without
  re-planning it.

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
  repos queued oldest-first in the live queue file for
  2026-11-12, 24 reports delivered the same day by ~22:08
  (the first six: CODE-FORGE, ChatBridgev1.0, MTAmorphai,
  K.ai-, FRIDAY, OpenRealism). The live-only rule
  came from Joshua's correction the same day, after a repo from
  conversation history (WinTux) was audited that does not exist
  live.
- The audit-to-task-list conversion ran four times the same
  evening the queue finished (2026-11-12): DUO (25 tasks + 2
  ideas), OLLAMA-SYSTEM-TEST (14 tasks, built as v6–v9),
  PIXEL-FORGE (13 tasks, Top 5 pulled forward), getcompute (21
  tasks). Each list verified the audit's big claims first.

## Available connectors

- [GitHub](../CONNECTORS.md) for the live repo listing and file reads.

## Alternatives for better results

- Offer a different order (newest-first, most-active-first) when
  the owner has not picked one, instead of assuming oldest-first.
- Offer to re-run the queue later as a second cycle once fixes
  have landed, rather than re-auditing a repo mid-cycle.
