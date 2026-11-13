# S64 — Audit each one, then combine into one verified list

Executable twin in BNB-TOOLS: [T22 task-list-combine-verify](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/task-list-combine-verify).

## When to use

- Use this skill when the user orders an audit of a list of items — security clusters, product features, study items — one at a time, and wants one prioritized task list out of it.
- Use it when the items are too many to hold in one report and too connected to leave as separate lists.
- Do not use it for a single audit of one thing: that is a [full-product-review](../full-product-review/SKILL.md) or a [read-only-security-audit](../read-only-security-audit/SKILL.md), not a combine.
- Do not use it to fold a LATER audit into an EXISTING list — that is [audit-findings-task-list-merge](../audit-findings-task-list-merge/SKILL.md). This skill builds the first combined list; the merge skill updates one.

## Audit one item at a time, same report shape each

- Fix the item list and its order before the first audit starts, and run the audits strictly one at a time in that order.
- Give every item the same report shape: what it does, strengths, weaknesses, gaps, UI flaws, innovation and design suggestions, and its own prioritized task list.
- Verify each item's decisive claims yourself before reporting it: re-run its tests, read the code behind the top findings, probe the sharp ones live. An audit that relays another agent's word unchecked is a rumour, not a report.
- Report each item when it is done and verified, then start the next one. Do not hold finished audits for a batch report, and do not ask the user whether to continue between items — the order already covers the whole list.

## Combine the per-item lists into one prioritized list

- Merge all per-item task lists into one list: dedupe entries that say the same thing, re-tier everything onto one scale (P0/P1/P2), and re-number contiguously (C1–CN).
- Keep the trace: every combined entry names the source task(s) it came from, so any entry can be followed back to the audit that produced it.
- State the statuses plainly (in flight, queued, not started) and make them add up to the combined total.

## Verify the combine by script before reporting it

- Verify the combined list mechanically, never by eyeballing it: run [task-list-combine-verify](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/task-list-combine-verify) (or the equivalent checks by hand when the tool is unavailable) and report only a combine that passes.
- The checks are: every combined ID present exactly once with no gaps, tiers contiguous, every source task traced to exactly one combined entry, no combined entry covering nothing, and the status counts adding up.
- If the check fails, fix the list and re-run the check. Never report a combine whose verification failed, and never silently drop a source task to make the numbers fit.

## Hand the list to the build phase, then stop

- Present the combined list with its counts (source tasks in, combined entries out, tier split, status split) and the verification result.
- The user directs the build order from the list. Building the items is the [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md), not this skill — do not start building inside the audit.
- Keep the per-item audit reports on file: they are the evidence behind the combined list, and a later reader needs them to judge a combined entry.

## Where this comes from

- This shape ran twice in one evening, 2026-11-12. The Code Forge security thread audited clusters S2–S7 one at a time (each re-verified by the lead: tests re-run, code read, top findings probed live) and combined 121 tasks into 117 (17 P0, 39 P1, 61 P2), verified by script — IDs C1–C117 all present exactly once, tiers contiguous, every source task traced, statuses adding up (4 in flight, 4 queued, 109 not started). The Forge Browser thread audited all 22 of its features the same way (#1–#3 in chat, #4–#22 from a background run, 19 write-ups, 2,529 lines) and merged 183 new tasks into a master list of 239 across sections A–AB. The same "audit each one" order also drove the Manus study audit (M1–M13, F1–F7) in the Code Forge improvement thread.

## Alternatives for better results

- Offer to run the later audits as a background batch once the first two or three have proven the report shape, instead of doing all of them in chat.
- Offer to split the combined list into build batches by section once the user has picked the order, instead of handing over one flat list.
