# S21 — Brand-matched logo design

Design a logo or glyph that matches an already-established product or brand, using one of three methods under one anti-slop discipline.

Companion tool: [T8 logo-test-battery](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/logo-test-battery) — runs the 12-test battery: renders the mark at 16/32/48px, silhouette, grayscale, invert, crops, and pasted into a real product screenshot, pass/fail per test.

## When to use

- A project needs a mark, a sigil, or a glyph.
- An existing mark needs to be judged or rebuilt.

## Start with the brand, never with the mark

- Audit the product UI first, looking at its real screens, and extract its palette, type, and material as a closed set of tokens before you draw anything.

- Write a one-page Brand DNA brief from that audit, using the [Brand DNA brief template](references/brand-dna-brief-template.md), and treat the brief as the gate, so no concept work starts until the brief exists.

- Generate concepts from product-specific ideas only, drawn from what the product actually is and does, and write down the banned generic nouns the concepts must not use, copying them verbatim into the brief.

- Never ship generated lettering, and redraw any mark as a human vector on a grid before it goes anywhere near the product.

## Pick the method that fits the job

- Use the brand-matched method when the product already has an established look, and judge every concept against the Brand DNA brief.

- Use the sigil and glyph method when the job is a mark from a name, by reducing the name first, removing vowels and repeated letters, then merging the remaining letters plus the key symbols into ONE glyph, with a documented mapping that says what each stroke of the glyph stands for.

- Use the code-built method when the mark must be exact, by writing the geometry by hand as SVG, building 3 genuinely different concepts per round, and never using image generation for a mark.

- Deliver a variant set for a glyph, such as black on cream, gold on black, and a transparent version for stamps, overlays, and stencils.

## Run every mark through the 12-test battery

- Run every mark through the 12-test pass or fail battery in the [logo test battery](references/logo-test-battery.md), and record a pass or fail per test, with no test skipped.

- Render the mark at 16, 32, and 48 pixels for real, and judge it at each size, because a mark that only works large is not a mark.

- Check the solid-black silhouette, the grayscale version, and the inverted version, and check the mark inside a circle crop and a squircle crop.

- Paste the mark into a real screenshot of the product, and put it on a competitor wall next to the marks it will sit beside, so the judgment is made in context.

- Audit the letterforms and the grid, and iterate one variable at a time when a test fails, so each change can be judged on its own.

## Handle rejection by asking, not guessing

- Stop guessing when the user rejects a mark, and ask what specifically is wrong, offering direction choices when that helps, instead of producing another round on a guess.

- Rebuild to the direction the user picks, and run the rebuilt mark through the battery again.

- Retire a rejected direction outright when the user rejects it, and do not re-present it in a later round.

- Withhold a round you judge not good enough, and say so, instead of showing work you would not stand behind.

## Where this comes from

- From the Code Forge logo research (983a94e7 — Brand DNA brief and 12-test battery), the RICH$XPRNC8 sigil thread (527e8c07 — letter-reduction method), the Reblend logo rounds in REBLEND DEV (2a82689c — code-built SVG), and the LA logo merch thread (7580cc0c — rejection data point). Recorded in the BNB audit as S21.

## Alternatives for better results

- Offer to draw the mark deterministically cell by cell on one pixel grid when letterforms keep mangling, so the geometry is exact.

- Ask the user for the product screenshots the audit needs when none are on hand, instead of designing from a description alone.
