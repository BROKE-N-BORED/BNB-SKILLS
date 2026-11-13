# S35 — UI direction-finding via mockup rounds

## When to use

- Use it when a product needs a visual direction and guessing once is not good enough.

- Use it when the user can judge pictures faster than they can describe what they want in words.

- Do not use it to write the build spec; spec-writing belongs to the dev thread only, after the direction is locked.

## Round 1: four directions in a named aesthetic

- Generate four distinct mockup directions inside one named aesthetic, so the round compares directions, not aesthetics.

- Present all four together and let the user judge them side by side.

- Keep each direction genuinely different; four near-identical mockups waste the round.

## Take one-line verdicts

- Ask for a one-line verdict per direction and record the user's own words.

- A verdict names what stays and what goes, such as "colors stay, game goes" or "too generic, like a PowerPoint slide".

- Do not argue with a verdict or re-pitch a rejected direction.

## Re-dose a single variable across a range

- When one variable is the question, generate a range that varies only that variable, lightest to heaviest, labelled A–D.

- Change nothing else between the variants; the user must be judging the one variable.

- Record which dose the user picks before moving on.

## Mix directions at explicit ratios

- When two directions both have something worth keeping, mix them at explicit ratios, such as one direction dominant, the other dominant, or maximum workspace.

- Name the ratio for each mix so the user knows what they are judging.

- Keep the mixes to a small set; three mixes is enough to find the balance.

## Lock the winner as a standing reference

- Lock the winning direction as a standing reference with scope rules attached.

- The reference upgrades what exists; it is not a layout to copy over the existing UI.

- Nothing existing is replaced by the reference; it guides new and changed surfaces only.

- Write the scope rules down with the reference so a later session cannot misread it.

## Hand spec-writing to the dev thread only

- Hand the locked direction to the dev thread to write the spec.

- Never run a second spec in parallel; two specs drift apart and the build follows the wrong one.

- Your job ends at the locked direction; the dev thread owns the spec and the build.

## Iteration rule throughout

- Fix the one named thing; do not redo everything.

- When the user names one problem, change only that problem and show the result.

- When the user rejects a round without naming what is wrong, ask what specifically is wrong before changing anything.

- The same one-variable iteration rule appears in the [brand-matched-logo-design](../brand-matched-logo-design/SKILL.md) workflow.

## Standing rules

- Native Linux desktop window, never a web UI, unless the user explicitly says otherwise.

- Nothing selected by default; the user picks the direction, the dose, and the mix.

- Never claim more than was checked; a mockup is a direction, not a built UI.

## Where this comes from

- Proven in the Pixar-inspired Code Forge UI thread; locked direction: Future 3 Dark Glass Minimal, no ring gauges — recorded in the BNB audit as S35.
