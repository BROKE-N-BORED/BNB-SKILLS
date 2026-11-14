# S65 — Audit-findings task-list merge

Fold a new audit's or verdict's findings into an existing prioritized task list instead of starting a new list: overlaps fold into existing tasks, genuinely new findings get their own tasks with continued IDs, and a script verifies every finding is covered before the merged list is reported.

Executable twin in BNB-TOOLS: [T23 task-list-coverage-check](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/task-list-coverage-check) — checks a task list's coverage map mechanically.

## When to use

- Use this skill when a second (or later) audit, verdict, or review lands on a project that already has a prioritized task list.
- Use it when the user says "update your task list to fix these weaknesses" or "create its task list and merge it to the existing task list" after a new round of findings.
- Do not start a fresh list when one already exists — two lists for one project drift, and findings fall between them.
- Do not use it for the first audit of a project; that list is built by [full-product-review](../full-product-review/SKILL.md). This skill starts where that one leaves off.
- Do not use it to combine several audits into a FIRST list — that is [audit-each-one-combine](../audit-each-one-combine/SKILL.md). The combine skill builds the first list; this skill folds later findings into one that exists.

## Fold overlaps into existing tasks, give new findings their own

- Read the new findings against the existing list task by task before writing anything.
- A finding that matches an existing task's problem folds into that task — extend the task's scope, do not duplicate it. (Stella's verdict fold: import weights, the "full" method, and zip export all folded into tasks that already covered them.)
- A finding with no matching task gets its own new task, with the next free ID in the existing sequence — never renumber the old tasks, because the user may already be referring to them by number. The one exception is a reorder the USER orders: when he says to re-rank the list, renumbering in the new order is the job — but then every cross-reference and the coverage map must be remapped to the new numbers, and the user must be told up front that task numbers will move (Stella, 2026-11-13 11:15: T1–T125 renumbered in the new rank order, cross-references and coverage map remapped).
- Keep the priority tiers honest: a new finding can be a P0 even late in the process (Stella's verdict added exactly one new P0 — the probe loading the base model twice — and it went to the top of the list, not the bottom).
- Keep the merged list in one file, in priority order, with the same per-task shape as the original list: problem, fix, what "done" looks like, effort size.

## Verify the merge by script, not by eye

- Count by script, never by hand: total findings in, findings folded, findings that became new tasks, tasks before, tasks after. The counts must reconcile — findings in equals findings folded plus findings that became new tasks.
- Write the reconciliation into the report: "91 tasks covering all 214 findings (181 from audits #1–#4 plus 33 from the verdict, verified by script)" is the shape, with the real numbers from the run.
- Check the IDs mechanically: task IDs unique and contiguous in their sequence, every finding ID referenced by exactly one task (or explicitly marked as folded into a named task).
- Use the twin tool (task-list-coverage-check) for the mechanical part: it reports findings with no covering task, tasks referencing unknown findings, and duplicate task IDs.
- If the counts do not reconcile, the merge is not done — find the dropped finding before reporting, do not report around it.

## Carry a coverage map that proves nothing was dropped

- End the merged list with a coverage map: every finding ID mapped to the task that covers it, grouped by the audit it came from.
- The map is the proof the user can check: "every single finding from the audit covered, each with the problem, the fix, what 'done' looks like, and an effort size. There's a coverage map at the end of the file proving nothing got dropped."
- When a later audit lands, its findings extend the same map — the map grows, it is never rewritten from scratch.

## Report the merged list and stop

- Report the new totals (tasks, findings covered, P0 count) and the one or two most important new items, in chat.
- Name any new P0 plainly — it changes what gets built first.
- Build nothing from the merged list until the user picks: the merge is a list for the user to direct from, not a build order. (Under the no-stalling rule, once the user says "build the whole list, P0 first," the cycle runs — see [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md).)

## Where this comes from

- STELLA ✨ Development thread (2d7b2739), 2026-11-12 ~20:50–21:20 EST: an external verdict on Stella v0.2 landed (33 findings); the assistant folded it into the existing list — overlaps folded into existing tasks (import weights, "full" method, zip export), new findings got their own tasks (probe double-load, maternion typo, torch.load pickle, auto-select, LICENSE/CI) — and reported "91 tasks: 11 P0, 29 P1, 31 P2, 20 P3, covering all 214 findings (181 from audits #1–#4 plus 33 from the verdict, verified by script)", with one new P0 (T11 — probe loads the base model twice). Audit #6 (installer + icon, 56 findings) then merged the same way, taking the list to 123 tasks. Merges continued 2026-11-13: audit #7 (MetaMorphAi hooks, 40 findings) → 125 tasks / 310 findings (11:12); audit #5 (18 tasks) → 142 tasks / 357 findings (11:58); audit #8 (training engine, 55 findings) → 168 tasks (14 P0 / 53 P1 / 62 P2 / 39 P3) / 412 findings (12:20), each merge script-verified with its coverage map. The 168-task list was then grouped into 11 areas as a view (12:29) without touching the merged list itself.
- STUDY DASHBOARD DEV thread (dc0566e7), 2026-11-12 ~19:00–20:15 EST: after the Study Shell audit, "Create a task list of improvement and everything from the audit to fix all gaps and weaknesses" produced 23 tasks (P0 data-integrity first), each with problem, fix, done-criteria, and effort size, with a coverage map at the end of the file proving nothing got dropped. Joshua ordered "Build the whole list P0 first"; all 23 shipped as v1.3/v1.4/v1.5, verified 74/74 green.
- MIMIK Dev thread (d22a66c0), 2026-11-12 ~20:46 EST: after the v0.2 deep-audit verdict landed, "Create a task list to fix the weaknesses" produced a 16-item list — and the assistant checked the audit's big claims against the tree first before trusting them ("They hold").
- Found in the second BNB delta scan (2026-11-13), product threads; not in the 2026-11-12 audit because the merge pattern only emerged once second audits started landing.

## Alternatives for better results

- Offer to re-verify the new audit's big claims against the tree before folding them in, when the audit came from outside the thread — a wrong finding folded in becomes a wrong task built later.
- Offer to split the merged list by version (P0s as the next release, P1s after) when the user wants the build order as well as the list.
