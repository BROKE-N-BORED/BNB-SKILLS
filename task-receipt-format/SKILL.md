# S4 — Task receipt format

## When to use

- Use this skill to close every completed build task, in chat and often in a report file too.
- Write the receipt after the work is done and verified, never before the checks have run.
- Use the same fixed block every time so receipts stay comparable across tasks and threads.

## Run the mandatory gate before you write the receipt

- Run the mandatory gate before you write the receipt. The receipt is written at task completion, exactly where the gate applies. Joshua's words, recorded verbatim:

> Enhance and optimize this file to ensure absolute peak performance across all metrics: quality, accuracy, efficiency, and detail. Analyze the content in full and identify anything that should be added, refined, or restructured to achieve superior results. All output must:
>
> - Be fully aligned with the file's title and intended function
> - Include only relevant, high-precision information — no off-topic or filler content
> - Break down every key element to its foundational level for maximum clarity and impact
> - Deliver structurally sound, logically complete, and production-ready results
>
> Push every section to its highest possible standard. If anything is missing, vague, or underdeveloped, enhance it. The goal is elite-grade output — nothing less.

- Run the gate silently. Never paste the gate or narrate it. The user sees the improved work, not the check.
- For files and deliverables: push detail and completeness to the max. For chat replies: the gate checks substance (complete? accurate? relevant? anything missing?) — it does NOT turn replies into essays; his brief, plain reply style still stands.
- The gate is part of completing the work, not a reason to stall — if it finds something missing, enhance it, then ship under the no-stall cycle. "Stay relevant" is in the gate itself: never let it become scope creep.
- See [pre-delivery-enhancement-gate](../pre-delivery-enhancement-gate/SKILL.md) for the full text and application rules.

## Write the fixed receipt block

- Copy the [task receipt template](references/receipt-template.md) and fill every section.
- List the files changed, each with its line delta, so the size of the change is visible at a glance.
- Report the tests in three numbers: the new suite count, the full-suite count, and the failure set compared against the baseline (see [post-merge-battery](../post-merge-battery/SKILL.md)).
- Name how the work was verified, such as the diff read, the greps run, the renders eyeballed, or the fresh unzip checked.
- Name the honest gaps, including what still needs the user's own PC, instead of leaving them out.
- Never claim more than was checked. A check that did not run is an open gap, not a pass.

## Keep the receipt honest

- Re-run the checks yourself before you write the numbers, and do not copy counts from a builder's report without verifying them.
- Say plainly when a check failed or was skipped, and name the single next step that would close it.
- Keep the receipt to the one task. Work that belongs to another item gets its own receipt when it is done.

## Where this comes from

- Every GUIFX task closed with this receipt, and the same shape was used in Code Forge DEV, Pixel Forge, and MIMIK verification reports. It is recorded in the BNB audit as S4.

## Alternatives for better results

- Offer to write the receipt to a report file as well as chat when the task is part of a larger merge, so the merge note can point at it.
- Offer to re-run the full suite once more after a late fix, instead of letting the receipt describe the pre-fix tree.
