# Guided in-tool build walkthrough

## When to use

- Use this skill when the user performs a multi-step build or install on their own PC and you walk them through it.
- Use the planned form when the steps are known up front, and the reactive form when the user arrives with an error screenshot.
- Work one step at a time and wait for the user's pass or fail report before giving the next step.

## Give the map first, then one step at a time

- Give the user the full map up front with the step names only, so they can see the whole journey before it starts.
- Deliver one step at a time with the exact mode, settings, and prompt for that step, and state the pass criteria for it in plain words.
- Wait for the user's pass or fail report before giving the next step, and never hand over two steps at once.
- Set the model map once at the start (fixed seats plus the driver swapped per step) and re-check it when the build underfoot changes.

## Keep every command hand-typeable

- Give one short single-line command per turn, because the user hand-types commands from their phone screen.
- Never send a multi-line paste, because multi-line pastes collapse into one line on the user's end, and never send a heredoc, because a collapsed heredoc strands the shell at the continuation prompt.
- Prefer the GUI text editor for creating or editing file contents, and reserve the terminal for short commands.
- Spell out lookalike characters in tags and commands, such as letter L against the digit 1, because they look identical in the user's terminal font.

## Run the reactive variant from a screenshot

- Read the user's screenshot, diagnose the exact error, and give one short single-line hand-typeable command, then repeat.
- Name the error in the user's own words and say what the command is meant to change, so they know what a pass looks like.
- Diagnose the next screenshot before giving the next command, instead of guessing a chain of commands up front.

## Where this comes from

- The planned form walked the Ember Break build in Code Forge, and the reactive form ran through the whole Design Shell thread (Unreal download, extraction, first launch, Blender setup) and the Whisper error diagnosis. It is recorded in the BNB audit as S14.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to switch to the reactive form when a planned step fails twice, instead of repeating the same step with the same words.
- Offer to check a screenshot of the result before calling a step passed, when the user's report leaves the outcome unclear.
