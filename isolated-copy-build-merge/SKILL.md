# S2 — Isolated-copy build and delta-port merge with batteries

Executable twin in BNB-TOOLS: [T2 delta-port-diff-verify](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/delta-port-diff-verify).

## When to use

- Use this skill whenever a feature or fix is built for a project that has a live tree other work may also be touching.
- Use it for every queued build item, one item at a time. A finished item no longer waits for a merge order to ship (see "Hold, report, and ship" below); "hold for merge order" only orders parallel held builds, never holds a finished build waiting for a push approval.
- Do not build directly in the live tree while other lines of work are running.

## Build in an isolated copy

- Copy the live tree to an isolated directory and build the feature there, leaving the shared tree untouched.
- Run the lead battery in the isolated copy: the new test classes plus the neighbouring test sets the change could affect.
- Check the diff yourself in the isolated copy and confirm it holds exactly the intended changes, nothing more.
- Re-run the new test classes independently and check the diff and marker counts yourself, never trusting the builder's word alone.
- Write a port spec naming the copy path, the exact delta, and any base-tree caveats the merge must respect.
- Name tree-side noise in the port spec: a fresh diff against the current tree shows content merged after the copy was taken. Name that content explicitly as tree-side movement, NOT part of the delta, so the porter ports only the delta.
- When a later item needs a hook into an earlier item that was not in its base, the follow-up hunk (code plus test) rides in the later item's port spec and is applied when the earlier item has landed.
- Re-check the live tree before porting a ship order: a ship order can arrive after the item is already merged. Grep the live tree first; if the hooks are in, say so and do not port twice.
- If the source tree must be fetched file-by-file (no clone access — e.g. a private repo pulled through the API), fetch with a resumable script that records progress per file. On a rate limit, STOP — do not hammer — and resume from where it stopped. (STEMLAB: the fetch hit GitHub rate-limiting at 54 of 120 files; the resume script picked up at file 55 and finished 120/120 clean. Most of `src/`, the configs, docs, and tests were still missing at the stop, so the rebuild could not start until the resume finished.)

## Back up, then port only the delta

- Back up the live tree before you touch it for the merge. Back up with `cp -r`, not `cp -a` (`cp -a` fails on ownership in this environment), and verify the backup by recursive diff outside `__pycache__`.
- Port only the delta from the isolated copy into the live tree, by anchor port of the named paths. Port by anchor or string match, not by a recorded line number: a line number from a merge note goes stale as other items land.
- Preserve any live-tree work that landed while the build was held, such as inbox items or hotfixes.
- Check the merged diff and confirm it equals exactly the intended changes.

## Verify the merge before you call it clean

- Verify the merged tree against the source copy with marker counts and byte-identical file comparisons before you call the merge clean.
- Never trust a patch tool report of already applied on its own, because a patch tool once silently reverted about 1,260 lines across 19 files while reporting exactly that.
- Run the merged-tree battery: the targeted classes first, then the full suite.
- Compare the full-suite failure set against the baseline (see [post-merge-battery](../post-merge-battery/SKILL.md)) and reproduce any new failure on the pre-merge backup before you claim anything about it.
- Run only one suite at a time. When a suite is already running, wait for its window instead of starting a second one.
- Keep any wait-for-window watchdog in a script file, because a watchdog command line that names the test string matches itself forever.

## Merge several items through one dependency-ordered queue

- When several items land at once, run them through one coordinator in dependency order, anchor-port plus battery each, lead verifies plus full suite before the push.
- Name the hard dependencies explicitly in the queue: an item that needs another item's code lands after it.

## Hold, report, and ship

- A merged and verified tree ships immediately under the no-stalling rule (see [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md)): push, Release, then start the next item. One item at a time still applies (no parallel builds in one tree); only the waiting between items is gone. No email step — GitHub-only is the standing rule (2026-11-13).
- Run the mandatory gate as a pre-ship check (see [pre-delivery-enhancement-gate](../pre-delivery-enhancement-gate/SKILL.md)): if it finds something missing, enhance it, then ship — the gate never stalls shipping.
- Report the merged tree path, the battery receipts, and the backup path.
- Close the task with a task receipt (see [task-receipt-format](../task-receipt-format/SKILL.md)) and ship through the ship pipeline (see [ship-pipeline](../ship-pipeline/SKILL.md)).

## Where this comes from

- This is the dominant build pattern across Code Forge DEV, GUIFX, Security, CodeRabbit, Manus, Forge Browser, MIMIK, Pixel Forge, Reblend, Design Shell, Model Research, Groq/Gemini, and Prompts work, and is recorded in the BNB audit as S2.

## Available connectors

- [GitHub](../CONNECTORS.md) for pushing the merged tree once the user approves.

## Alternatives for better results

- Offer to run the targeted battery again after a fix lands on the merged tree, instead of trusting the pre-fix receipt.
- Offer to keep the isolated copy until the user confirms the merge on their own PC, so a revert stays cheap.
