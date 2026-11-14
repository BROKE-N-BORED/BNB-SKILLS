# S5 — Full product review

## When to use

- Use this skill when the user asks for a review of a whole product, with its strengths and weaknesses and gaps and what is missing.
- Use it before a fix plan is drawn up, so the user can direct from a ranked list instead of from a guess.
- Do not change any code during a review. An audit is a list for the user to direct from, and the fixes come later as their own items.

## Read the whole codebase

- Read the codebase end to end, including the parts that look finished, before you write a word of the review.
- Open every tab and every screen of the built app and take a screenshot of each one, then look at the screenshots yourself.
- Time the slow paths with real measurements instead of guessing which part is slow.
- Probe a suspected defect live, in the running app, rather than guessing from the code alone.
- Work the [review checklist](references/review-checklist.md) in order; every finding in the report traces to a checked box.

## Deliver strengths, weaknesses, gaps, and ranked improvements

- Report the strengths first, naming what is genuinely good with the evidence that shows it.
- Report the weaknesses and gaps next, each grounded in the code or the screenshot that shows it, with the file and line where it lives.
- Name what is missing outright, not just what is weak.
- Rank the improvements so the user can pick from the top: group them in tiers or in a P0 to P4 phased plan with a concrete task list, and include an avoid list for ideas that look tempting but would break the hardware limits or the hard $0 rule. When a LATER audit lands on the same project, fold its findings into this list instead of starting a new one (see [audit-findings-task-list-merge](../audit-findings-task-list-merge/SKILL.md)).
- Keep every claim tied to something you read, measured, or screenshotted, and flag anything you could not verify instead of dressing it up as a finding.

## Verify before you claim

- GitHub code search returns ZERO results for these repos — never claim a repo-wide count (TODOs, tests, typos) from it. Counts come only from listings and files actually read.
- Verify a claimed typo byte-for-byte before writing it in a report: quote the file, the line, and the exact bytes. A draft report once falsely claimed a model-tag typo and zero TODOs from the code search — both were struck before delivery.
- Re-verify descriptions and topics live at delivery time, not from the listing you started from — metadata changes during the day (two repo descriptions changed on 2026-11-12 between the morning listing and the evening audits).
- A report covers what was actually read; anything not checked goes in a "could not verify" section, never in the findings.

## Audit-series variant

- The same verbatim per-item ask can run as a series across a list: one item at a time, each item getting its own report (features, functions, strengths, weaknesses, gaps, UI flaws, innovation/design suggestions) plus its own prioritized task list, delivered one at a time and rolling to the next item under the no-stalling rule.
- The ask text: "audit each one one at a time, report features functions, strengths, weaknesses, gaps, ui flaws or innovation time suggestions, design suggestions, anything new or needs improvement or updated or upgraded... make a task list".

## Parallel cluster variant

- For a large codebase, split the audit into clusters (by subsystem), one worker per cluster, read-only, every finding grounded in file:line. Merge the raw findings and dedupe cross-cluster duplicates before reporting: the Code Forge audit (main chat, 2026-11-13 17:03–17:18) ran 7 clusters, 185 raw findings, 3 cross-cluster duplicates merged, 181 unique (2 P0, 51 P1, 128 P2).
- Reuse the audits already done instead of redoing them: the Forge audit reused the S2–S7 security audits and found no unlisted security issue. A prior list is a starting point, not a thing to re-derive.
- Mark findings already covered by in-flight work so they do not come back as missing: the DATAPACKR audit (2026-11-13 19:51) marks anything v0.2 already covers as covered, not as a gap.

## Report the review and stop

- Deliver the review in chat with the headlines and the ranked list, and write the full report to a file for the record.
- Change no code, file no fixes, and start no build item. The user directs the next step from the list.
- Offer to build the picked items one at a time (see [isolated-copy-build-merge](../isolated-copy-build-merge/SKILL.md)) once the user has chosen.

## Where this comes from

- The same review shape was delivered for OLLAMA System Test, MIMIK, Pixel Forge (24 improvements in 3 tiers plus an avoid list), Yahtzee (P0 to P4 phased plan plus a 25-item task list), WinLinx, Forge Browser, and the repo audit thread, from the same verbatim ask in four threads on 2026-11-12. It is recorded in the BNB audit as S5.

## Alternatives for better results

- Offer to time a slow path again on the user's own PC when the sandbox numbers do not match what the user sees.
- Offer a narrow follow-up review of one screen or subsystem when the full review surfaces a deep problem in one place.
