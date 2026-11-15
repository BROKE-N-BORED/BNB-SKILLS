# S76 — AI code review loop: set up an AI reviewer, verify its findings, roll it out repo by repo

Set up an AI reviewer on a repo (config file, test PR, trigger the review,
verify each finding against the official schema and docs before fixing,
merge), then roll it out repo by repo — and use the CLI for repos with no
PRs. The point is token savings: the reviewer reads the diff and reports,
so the agent fixes findings instead of burning tokens reading whole diffs
looking for problems.

## When to use

- A repo has AI-generated code and no second pair of eyes on it.
- You are setting up automated review on a new repo, or rolling an
  existing setup out to more repos.
- A repo pushes straight to main and has no PRs for the reviewer to look
  at — that is the CLI case, not a reason to skip the review.
- Do NOT use this to replace reading the reviewer's findings yourself —
  the loop is review, verify, fix, merge. Skipping the verify step ships
  fixes for findings that were wrong.

## Set it up on one repo first

- Add the reviewer's config file to the repo (for CodeRabbit, a
  `.coderabbit.yaml` at the repo root) with the review profile and path
  filters set — the CODE-FORGE config used the Assertive profile and 16
  path-filter patterns.
- Open a test PR on that repo, trigger the review, and read the findings.
  The first PR is the proof the loop works end to end, not just that the
  config file exists.
- Verify each finding against the official schema and docs before fixing
  it. Third-party guides and docs-page labels are not authoritative —
  they have been wrong about real setting names (see below). Fix what
  checks out, then merge.
- Worked example: CODE-FORGE, PR #1 — 4 reviews, 7 findings, all
  resolved, merged as commit 2dfbd93d. "So the loop is live on
  CODE-FORGE now: branch, PR, trigger the review, I fix what checks out,
  merge."

## Verify every config key and command against the official schema

- `reviews.instructions` is not a real V2 setting — it came from a
  third-party guide trusted over the official reference.
- `incremental: true` is not real either — the real key is
  `auto_incremental_review`. It was guessed from the docs page's label
  instead of the actual schema.
- The schema does not reject unknown keys under `auto_review`, so a bad
  key fails silently instead of erroring — a config that "works" can
  still be wrong. Check each key against the official schema by hand.
- `@coderabbitai review` only requests one review; it does not restart
  automatic reviews. `@coderabbitai resume` is the command that restarts
  them, confirmed in the official docs.

## Roll it out repo by repo, and change the flow

- Prove the loop on one repo first, then roll the config out to the next
  repos one at a time — REBLEND first after CODE-FORGE, then the rest.
  One repo at a time keeps a bad config from landing everywhere at once.
- New work goes through PRs from here on: branch, PR, review, merge.
  That replaces push-straight-to-main, because the reviewer only looks
  at PRs — a repo with zero PRs gets zero reviews on its actual code,
  however good its config is.
- Run the same review pass on each repo's recent work as it comes
  online, so the rollout is not just config files — it is findings fixed
  on real code.

## Repos with no PRs: use the CLI

- The CLI can review a repo with no PR at all: it compares the recent
  work on main against an older point and hands back findings made for
  an agent to work from. Nothing touches main, and on a repo with a live
  config it reads that config.
- It cannot charge silently: it uses the included allowance first and
  needs an explicit opt-in to spend anything.
- In a sandboxed or headless environment, browser OAuth is a dead end:
  the localhost callback goes to the browser's machine, not the CLI's,
  and the 5-minute auth window runs out while a human approves. Do not
  keep retrying the browser road — use the Agentic API key instead.
  The key comes from the reviewer's dashboard and goes into the secure
  vault; it is never written into a file, a chat message, or a skill.

## Where this comes from

- CODE RABBIT ACCOUNT thread (9b85439d, Sat 2026-11-14 12:16–17:39
  EST): the full setup — free trial (33 of 36 repos public, free
  forever; trial ends ~Nov 28), Assertive profile, config file with 16
  path filters, PR #1 on CODE-FORGE, 4 reviews, 7 findings, all
  resolved, merged as 2dfbd93d. The schema-verification lessons above
  (reviews.instructions, incremental vs auto_incremental_review,
  resume vs review) all came out of this thread.
- Free AI trials thread (3720590d, Sat 2026-11-14 10:50 EST): Joshua's
  token-saving insight that started the whole setup — "Whoa i can save
  your age tkens by having code rabit review code and report to you
  instead right?" — with the honest catch that the flow would change to
  branch, PR, review, merge, since most projects push straight to main.
- Check CodeRabbit repo updates thread (a2d60e0a, Sat 2026-11-14
  21:34–23:30 EST): the CLI path and the sandbox auth lesson — "right
  now the bot has nothing to review. It only looks at PRs, and
  everything goes straight to main" — plus the browser-OAuth dead end
  (localhost callback to the wrong machine, 5-minute window expired)
  and the Agentic API key fallback. Joshua: "I am trying to use code
  rabbit to review my code in all yhebrepos in brike n bored jot just
  code firge dude". Rollout order set: CODE-FORGE first, then REBLEND,
  then the rest one at a time; "New work goes through PRs from here, so
  reviews keep flowing."
- Found in the sixth BNB delta scan (2026-11-15). Three in-window
  threads; the loop is proven on one repo and the rollout is still
  pending.
