# Debug sweep with repair authorized

## When to use

- Use this skill when the user says a bare debug it, with no symptom named, and repair is expected.
- Use it when a suite has failures to fix or an app misbehaves and nobody knows why yet.
- Use the diagnose-only form (see full-product-review) when the user asked for a review or a list, not for fixes.

## Inspect the whole thing first

- Run a full inspection of the app and the code before you fix anything, covering the entry points, the state handling, the callbacks, and the rendering.
- Exercise the app the way the user uses it, and read the code behind anything that looks wrong.
- List every real fault you find, each with the file and line and the evidence that shows it, before you start fixing.

## Fix the faults in place

- Fix each real fault in place, changing only the fault and the lines the fix needs, and leaving working parts around it alone.
- Re-run the check that found each fault and the tests that cover the changed area, and do not call a fix done until those checks pass.
- Fix a defect found inside the assigned job then and there instead of filing it as a future item, and present a defect outside the job as its own item before you touch it.
- Run the full suite at the end and compare the failure set against the baseline (see post-merge-battery).

## Report what was found, fixed, and checked

- Report the faults found, the fixes made, and the checks that now pass, with the numbers.
- Name anything still unchecked or still needing the user's own PC, instead of describing the sweep as finished.
- Close the sweep with a task receipt (see task-receipt-format).
- Never call a fix closed until the user has run it on their own PC and confirmed it.

## Where this comes from

- A bare debug it on Yahtzee found and fixed a bot soft-lock plus four more faults, and a fix-the-failures order on Code Forge diagnosed six failures and fixed four, taking the suite to 2,435 out of 2,435 green. It is recorded in the BNB audit as S15.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to run the wider test suite once at the end when a targeted fix touches shared code.
- Offer to file a defect found outside the assigned job as a separate item, instead of fixing it unasked.
