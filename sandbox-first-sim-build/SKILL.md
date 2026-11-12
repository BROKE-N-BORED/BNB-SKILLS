# Sandbox-first sim build

Build a simulation as a standalone sandbox file first, with the core sim separate from the rendering, and verify it with a screenshot rig and numeric measurement before it touches the game file. Use this skill whenever a sim feature needs building, and whenever a visual result needs proving instead of assuming.

## Build in a sandbox, game file untouched

- Build the feature as a standalone sandbox test file first, and leave the game file untouched until the sandbox build is verified.

- Keep the core simulation separate from the rendering, so the sim parts can be lifted into the game later without dragging the sandbox rendering along.

- Build on the dossier numbers when a dossier exists, and say which dossier the numbers came from.

- Keep the sandbox file as the proof of the feature, even after the parts are lifted in.

## Verify with a screenshot rig, never blind

- Render the actual sandbox file with a screenshot rig, and look at the screenshots yourself before you deliver anything, because no more blind builds.

- Check every relevant pose and state in screenshots, such as standing, bedded, and freeze poses for an animal, since a fault can hide in one pose while the others look fine.

- Measure numerically instead of eyeballing, such as a leg ground-penetration measurement per pose, or a ball rest position and launch height for a physics feature.

- Report the measurement, the conditions, and the screenshot behind each claim, and name any check that still needs the user's own eyes.

## Test interactions the way a person aims

- Test interactions the way a person aims on a phone, with human-style aims at varied points and distances, not machine sweeps.

- Re-sync the camera or view state after every aim change before you measure the result, so one stale ray cannot masquerade as many trials.

- Run automated suites for the sim itself, including save and load round-trips and long runs, such as hundreds of simulated births, and report the pass counts.

- Treat a target that only works on exact aim as unusable, even when the exact aim test passes.

## Keep the reference list verified

- Expand the reference-image list for a build, and check every URL live before you rely on it.

- Exclude dead or hotlink-blocked images from the list, and say which ones were excluded and why.

- Note honest gaps where no usable photo exists, such as a moment nobody has photographed, instead of substituting a wrong image.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to run the verification at phone viewport sizes, such as 360 by 800, when the user will judge the build on their phone.

- Pair this skill with verify_like_the_user, which says what to verify, while this skill is the executable way to do it.
