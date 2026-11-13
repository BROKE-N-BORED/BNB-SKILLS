# S17 — Reference-sheet character pipeline

Build a 3D character from multi-view reference sheets by making every piece separately, then assembling the pieces and saving the whole character as a reusable preset.

## When to use

- The user sends a character reference sheet, or a sheet for one piece of a character, and wants the character modeled.

## Itemize the sheet before you model anything

- Read every view on the character sheet and list each separate piece the character wears or carries, such as hoodie, shorts, belt, phone, shoes, tools, and backpack.

- Treat the body itself as its own set of parts, such as head, ears, eyes, snout, arms, legs, feet, and tail, and keep each part a separate object so the finished character can be posed and animated part by part.

- Present the itemized piece list to the user and wait for approval before modeling starts, because this is the first of three approval gates and a wrong split costs more to fix later.

- Ask for a dedicated reference sheet for each piece, and build each piece only from its own sheet, so a hoodie is judged against the hoodie sheet and a belt against the belt sheet.

- Keep a running list of which sheets have arrived and which are still outstanding, and say plainly which pieces are blocked on a missing sheet instead of guessing them.

## Model each piece separately from its own sheet

- Build one piece at a time, as its own asset, with its own materials and its own dimensions measured from its sheet.

- Model exactly what the piece is, not what the sheet happens to show next to it, so a belt sheet that shows tools tucked in the belt still means modeling the belt empty, because the tools are their own piece with their own sheet coming.

- Keep a piece's subparts separate too, such as a belt strap, buckle frame, prong, and pouches as distinct objects, so each can be adjusted without rebuilding the piece.

- Verify each finished piece against its own sheet view by view, using the [trace-and-overlay-verification](../trace-and-overlay-verification/SKILL.md) skill, and report the measured result for that piece.

- Present each finished piece to the user for approval before moving on, because this is the second approval gate, and hold the next piece until the user signs off or says what is wrong.

- When the user rejects a piece, ask what specifically is wrong before reworking it, and rework only the named problem instead of rebuilding the piece from scratch on a guess.

## Assemble the character and save it as a preset

- Assemble the approved pieces onto the body in the order they layer, such as body, then clothing, then belt, then carried items, checking that each piece sits where the character sheet puts it.

- Verify the assembled character view by view against the full character sheet, checking proportions against the sheet, and name any proportion that still reads off instead of calling the assembly done.

- Present the assembled character for approval, because this is the third approval gate, and keep any downstream work on hold until the user signs off.

- Export the finished character in the format the next step needs, such as a .glb file, and record the export path, the part count, the triangle count, the height, and the facing direction alongside it.

- Save the character as a reusable preset or template that holds the part list, the materials, and the assembly, so the character can be loaded, varied, or reused without rebuilding it.

- Store the preset in the place the user chose for it, and say where it lives, because a preset nobody can find is not a preset.

## Report only what was built and checked

- Report the piece count, the triangle count, and the export path from the actual build, never from an estimate.

- Name every gap honestly, such as a detail the modeling tool cannot do, for example text or decals on clothing, and say which parts of the sheet the build does not carry.

- Name every sheet still outstanding and every piece still unbuilt, so the user can see exactly where the character stands.

- Say plainly when a piece or the assembly is still waiting on the user's verdict, and do not call it done until the user says so.

## Where this comes from

- Built from the Victor character work in the EVERY MOUSE thread (5bb9ed96) and the REBLEND DEV thread (2a82689c): the v2 rebuild from the six-view character sheet, with a dedicated sheet per piece (hoodie, shorts, belt) and the belt-only rule, and the preset direction — Victor saved as a reusable preset, on GitHub and built into Reblend. Recorded in the BNB audit as S17.

## Alternatives for better results

- Ask the user for one more view of a piece when the sheet leaves a dimension unreadable, instead of inventing the missing dimension.

- Offer to tighten proportions in a finishing pass once all sheets have landed, rather than reworking proportions after every single piece.
