# Task receipt format

## When to use

- Use this skill to close every completed build task, in chat and often in a report file too.
- Write the receipt after the work is done and verified, never before the checks have run.
- Use the same fixed block every time so receipts stay comparable across tasks and threads.

## Write the fixed receipt block

- List the files changed, each with its line delta, so the size of the change is visible at a glance.
- Report the tests in three numbers: the new suite count, the full-suite count, and the failure set compared against the baseline (see post-merge-battery).
- Name how the work was verified, such as the diff read, the greps run, the renders eyeballed, or the fresh unzip checked.
- Name the honest gaps, including what still needs the user's own PC, instead of leaving them out.
- Never claim more than was checked. A check that did not run is an open gap, not a pass.

## Keep the receipt honest

- Re-run the checks yourself before you write the numbers, and do not copy counts from a builder's report without verifying them.
- Say plainly when a check failed or was skipped, and name the single next step that would close it.
- Keep the receipt to the one task. Work that belongs to another item gets its own receipt when it is done.

## Where this comes from

- Every GUIFX task closed with this receipt, and the same shape was used in Code Forge DEV, Pixel Forge, and MIMIK verification reports. It is recorded in the BNB audit as S4.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to write the receipt to a report file as well as chat when the task is part of a larger merge, so the merge note can point at it.
- Offer to re-run the full suite once more after a late fix, instead of letting the receipt describe the pre-fix tree.
