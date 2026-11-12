# Phone-first crash course

Teach one concept per lesson, grounded in the user's own hardware and their own project, honest about what their PC can and cannot do, delivered one lesson at a time. Use this skill whenever the user asks for a crash course, a lesson series, or to learn a topic step by step.

## Teach one concept per lesson

- Give one concept per lesson, and stop after that lesson, because the course is delivered one lesson per turn.

- Never dump the whole course at once, even when the user is keen, because a wall of lessons teaches nothing.

- Use the lesson template in `references/lesson-template.md` so every lesson has the same shape.

- End each lesson by naming the next lesson, and wait for the user to ask for it before teaching it.

## Ground every lesson in their hardware and project

- Ground each concept in the user's own hardware, naming what their PC can do with it and what it cannot.

- Ground each concept in the user's own project, using an analogy from work they already know, so the new idea lands on something familiar.

- Be honest about the limits, such as small models, LoRA and PEFT, and CPU training of tiny models being in reach, while bigger training needs a free cloud GPU.

- Say plainly when a step needs something the user does not have, and name the free route around it when one exists.

- Never promise a result the hardware cannot deliver, and never hide a hardware limit behind vague wording.

## Give short single-line commands only

- Give short single-line commands only, because the user hand-types them from their phone screen.

- Never give a multi-line block, a heredoc, or a long quoted string, because pastes flatten into one line on the user's end and leave their shell stuck.

- Give one command, state what it should show when it works, and wait for the user's report before giving the next one.

- Prefer the GUI text editor for creating or editing file contents, and reserve the terminal for short commands.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to recap the previous lesson in two lines before starting the next one, when lessons are days apart.

- Ask the user what they want to build with the concept when they stall, and tie the next lesson to that build.
