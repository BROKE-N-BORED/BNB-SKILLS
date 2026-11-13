# S57 — BNB repo manager delta scan

## When to use

- Use this skill when you are the manager thread for the BNB
  repos and it is time for a delta scan: find what is new or
  changed in the chat threads since the last scan, and turn it
  into new repo items or updates to existing ones.
- Use it on a schedule the owner sets, or when he orders a scan —
  never as an unsolicited sweep outside the manager thread.
- This skill covers the scan itself. Building the items it finds
  follows the normal build discipline (see
  [isolated-copy-build-merge](../isolated-copy-build-merge/SKILL.md) and [ship-pipeline](../ship-pipeline/SKILL.md)).

## Read the baseline before you read any thread

- Read the master audit (`AUDIT.md`: the skill and tool master
  lists, the already-built list, the per-thread notes) and the
  build report with its honest gaps.
- Read every repo's current index: the skills and tools README
  indexes, the presets README, the roles README, the plugins
  README and spec. A candidate that is already in a repo is not
  a candidate — dedupe against the baseline, do not re-propose.
- Note the open flags the baseline carries (unverified v1 gaps,
  unchecked external repos) so the scan can close them when
  evidence appears — and can say plainly when it does not.

## Scan from the watermark, newest first

- The watermark is the last scan's time. Read each assigned
  thread newest-first, back to the watermark — usually 1-3 pages
  per thread. A thread created after the watermark gets read
  fully, not sampled.
- Check the curated memory file and the daily memory notes for
  the same window: they carry state (what shipped, what is still
  building, what changed) that the raw turns do not summarise.
- Read-only on other chats. No pushing, no messaging the user,
  no writing into another worker's staging area.

## Find four kinds of thing

- New repeatable workflows, worth a new skill or tool. Judge
  honestly whether the workflow repeats: a one-off fix, a single
  correction, or a feature of one product is not a skill. A
  pattern proven across two or more projects, or designed from
  the start to recur, is.
- New presets, roles, or plugins with real content — copied from
  a real source, never invented, never a stub. Pending content
  goes in a PENDING note, not in the repo as an item.
- Updates to existing items: a workflow changed, a standing rule
  superseded part of a skill, a correction landed, a new version
  shipped, or a v1 gap is now provable. Updates are described in
  an UPDATES file (file, what changes, why, evidence) — never
  edited into the live builds in place.
- Re-check existing skills on every scan: a skill whose workflow
  no longer exists — the app changed, the feature was removed,
  the pattern was superseded — gets flagged for refresh or
  retirement, never silently left stale.
- Threads checked with nothing new. Record them. "Checked,
  nothing new" is a result, and it stops the next scan from
  re-reading the same turns wondering whether they were covered.

## Ground everything, stage cleanly

- Every item carries its evidence: a quoted turn or message, or
  a file path. No invented items, no items grounded in "probably".
- Stage accepted additions under a dated delta directory, one
  folder per worker, one folder per repo inside it. New files
  only — never edit the live local builds.
- Use descriptive slugs for new items. Do not number them: the
  coordinator assigns the next S/T numbers when merging, so two
  workers never collide on a number.
- Skills follow the repo format (SKILL.md + skill.yaml, no
  frontmatter). Tools are real working code with a smoke test
  you actually run. Presets, roles, and plugins follow their
  repos' v1 layouts.
- Write per-thread notes as you go, and hand back counts of new
  items and updates, the staged paths, and the headline items
  with their sources. The coordinator merges, numbers, and
  pushes under the no-stalling rule.

## Where this comes from

- Ordered by Joshua on 2026-11-12 in thread 089d9759: "your job
  for this chat thread is to manage all of these repos, you scan
  every chat thread and find new ones and ways to update and
  upgrade them". The first delta scan ran the same day against
  the ~17:54 EST audit watermark, with workers staging into a
  dated delta directory, one folder per worker.

## Alternatives for better results

- Offer a full re-audit instead of a delta scan when the baseline
  itself is stale or the repo structure has changed.
- Offer to close a named v1 gap as its own item when the scan
  turns up the machine or evidence that was missing.
