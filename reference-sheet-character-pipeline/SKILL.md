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

## A measurement MATCH is not the look

- A model can match every measurement and still not look like the character. Victor v2 Phase 2 matched on all six views by the overlay bands — and Joshua's verdict was "Brother this looks fucjing terrible": flat disc eyes, no smile, small ears, blob shoes. The silhouette matched the measurements; the character did not read.

- Build cartoon features to how they READ at phone size, not to scale. The sheet is a cartoon with huge features; building them to scale makes them too small to read on his phone. The Phase 3 fix was ears twice as big, eyes twice as big, smile twice as wide with brighter teeth, wider head — judged by eye at phone size, not by the overlay numbers. Tighten the shots too, so the character fills the frame instead of sitting in the middle of an empty floor.

- Check the PROFILE closeup, not just the front: the Phase 3 profile view caught the eye whites bulging 8 cm proud of the skull like golf balls — invisible from the front, obvious from the side. The whole eye assembly had to be set back into the skull.

- Revert dead geometry instead of keeping it: a brow-tail extension was tried and reverted when a byte-identical render proved the tail points land inside the ear ellipsoid and are invisible.

- His bar, in his words: "Make it look like the picture I gave you or it's not done yet. It's that simple." A piece or assembly the measurements call MATCH is still not done until his eyes say it looks like the picture.

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
- The measurement-vs-look lesson and the image-to-3D notes come from Victor v2 Phases 2–3 and the Hi3D round (2026-11-12–13): two measurement-MATCH rounds rejected on sight, the phone-size judging fix, and the free-plan download trap.

## Alternatives for better results

- Ask the user for one more view of a piece when the sheet leaves a dimension unreadable, instead of inventing the missing dimension.

- Offer to tighten proportions in a finishing pass once all sheets have landed, rather than reworking proportions after every single piece.

- If the user tries an image-to-3D service himself, tell him first: upload ONE clean single-figure image, not the multi-figure sheet — Hi3D made 7 models from a 7-figure sheet, one per figure. And check the download terms BEFORE he generates: Hi3D's free plan is preview-only in the browser, downloads are Pro-only ($19.90/month).

- Test any service link yourself before sending it. An untested hi3d.pro link redirected to a completely different service and wasted his credits.
