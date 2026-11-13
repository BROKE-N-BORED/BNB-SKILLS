# S8 — Post-merge battery and baseline failure-set comparison

Executable twin in BNB-TOOLS: [T3 post-merge-battery-runner](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/post-merge-battery-runner).

## When to use

- Use this skill after every merge into a live tree, and after any change whose effect on the suite must be proven.
- Run it against the merged tree, read-only, and hold it while the tree is still changing mid-merge.
- Run only one suite at a time, and wait for a quiet window instead of starting a second suite.

## Run the full suite before and after

- Record the baseline failure list from a full-suite run on the tree before the change.
- Run the full suite again on the merged tree, and compare the failure lists, not just the pass counts.
- Call the change clean only when the failure set is byte-identical to the baseline, or differs only by failures the change was meant to fix.
- Diagnose any new failure against the pre-merge backup before you claim anything about it.
- When batch-run failures cluster in port-binding tests (deck or server tests), confirm the port race before calling them failures: re-run each failing class on its own. If every class passes alone, it is the known port race — deck tests stepping on each other in a batch — not a defect in the change. Only a failure that reproduces solo counts against the merge.

## Hold while the tree is changing

- Watch the tree for stability before you start, and hold the battery while a merge is still landing files.
- Discard partial results from a run that overlapped a change, and re-run the battery from scratch once the tree is stable.
- Keep any wait-for-window watchdog in a script file, because a watchdog command line that names the test string matches itself forever.

## Check the merge itself, not just the suite

- Verify the merged tree against the source copy with marker counts and byte-identical file comparisons.
- Never trust a patch tool report of already applied on its own, because a patch tool once silently reverted about 1,260 lines across 19 files while reporting exactly that.
- Run the targeted test classes for the merged change, read-only against the merged tree.
- Apply the deck served-page rule whenever the change touches a served page: extract the served page's script element and syntax-check it with node, because the source can look fine while the served page is corrupt.
- Run a phone smoke of the merged build where the user will use it on a phone.

## Relay defects with exact locations

- Report each defect to the DEV thread with the exact file and line, and re-verify each fix by re-running the affected classes yourself.
- Report the verdict as a pass or as the exact defects, with the failure diff attached.
- Close the battery with a task receipt (see [task-receipt-format](../task-receipt-format/SKILL.md)).

## Where this comes from

- This battery ran on every GUIFX task (failure set byte-identical to baseline on every receipt) and on every Code Forge merge, and twice on the merged Security tree, where the merge verification caught the silent 1,260-line revert. It is recorded in the BNB audit as S8.

## Alternatives for better results

- Offer to re-run the battery once more after the last fix lands, instead of letting the verdict describe the pre-fix tree.
- Offer to run the targeted classes first for a fast signal, then the full suite for the verdict.
