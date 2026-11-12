# Trace-and-overlay verification

Verify a 3D model against its reference sheet by measurement, not by eyeballing. Use this skill whenever a sheet-built piece or character needs a verdict, and whenever a previous eyeball check was wrong.

## Set the reference image up as a backdrop

- Load the reference sheet image as a viewport backdrop, so the model is judged against the sheet in the same view instead of from memory.

- Start with the orthographic front view, then the orthographic side view, and align the backdrop size to the model scale before you compare anything.

- Match a three-quarter view by setting the viewport camera to the same angle as the sheet, estimating the angle from the sheet and refining it by matching landmarks until the view lines up.

- Lock the backdrop once it is aligned, so it cannot drift while you measure.

## Measure dimensions off the image

- Measure the key dimensions of the piece directly off the reference image, in the model's own units, before you judge the model.

- Measure each subpart too, such as the width and height of a buckle frame, the height of a pouch, and the thickness of a strap, because a piece can read right overall while one subpart is wrong.

- Check what each view actually shows before you model from it, since a shape seen from the side can be mistaken for a shape on the back, and a part that exists in one view may be absent in another.

- Rebuild a piece from the measured dimensions when the measurements show the current build is wrong, instead of nudging the old build toward the sheet.

## Overlay the render on the sheet at the same scale

- Render the model from the same view as the sheet, at the same scale, and lay the render over the sheet so the two silhouettes can be compared directly.

- Match silhouettes and outlines view by view, and check every view the sheet provides, not just the front.

- Report the residual offset for each view in real units, such as a vertical offset of about 1 to 2 cm that remains after the rebuild, and say plainly that it remains instead of rounding it to zero.

- Name every other honest gap in the same report, such as a color that reads darker than the sheet, a missing detail like stitching, or a subpart that is a plain solid where the sheet shows more shape.

## Give a verdict grounded in the measurements

- State the verdict as a match or a mismatch per view, with the measured deltas behind it, so the user can see what was checked and what the numbers said.

- Never call a model verified from a look alone, and never present an eyeball judgment as a measurement.

- Say which views were checked and which were not, when a view could not be matched, and name the check that still needs the user's own eyes on the render.

- Keep the overlay images or renders with the report, so the user can see the comparison instead of taking the verdict on trust.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Ask the user for a straighter or higher-resolution view when the sheet image is too skewed or too small to measure from.

- Offer a second overlay pass after a rework, so a fix is proven by the same measurement that found the fault.
