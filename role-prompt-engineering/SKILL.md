# Role prompt engineering

Write assistant role instructions as a 12-section master pack, under a hard character limit, verified by exact count. Use this skill whenever a new Forge role or assistant role needs writing, and whenever an existing role needs rebuilding under a limit.

## Write the 12-section master pack

- Use the template in `references/role-pack-template.md`, and keep the same skeleton for every role, swapping only the domain.

- Write the identity section first, naming what the role is and what it is for, in plain language.

- State the core objectives as the outcomes the role exists to produce, and name the systems the role covers.

- Write the architecture rules, including the resource-first rule and the rule that authoritative state stays separate from the render mesh.

- Write the interaction and transformation rules, saying how the role changes state and how it responds to input.

- State the realism levels the role works at, such as visual, interactive, resource simulation, and physical simulation, and state each level plainly, never faking a level the build does not have.

- Write the engineering standards, the persistence rules, and the validation invariants, so the role has something to check itself against.

- Close with the response contract, saying what the role returns and in what shape.

- Write fundamental rules as an engineer, not as a guide, stating what the role does and what it must not do.

## Hold the hard character limit

- Treat the character limit as HARD, such as 8,000 characters, and never deliver a pack over it.

- Run a pre-output length audit before you present any draft, and compress during drafting when the draft runs near the limit.

- Verify the final length with an EXACT character count, using a tool such as `wc -m`, and never estimate the count.

- Report the verified count with the draft, so the user can see the number the tool returned.

- Write plain instructions only, with no redundant metadata, because a pack padded with metadata instead of instructions gets rejected.

- Attach the governing source files as references when the role has them, and save the finished pack to `~/workspace/role-engineering/`.

## Rebuild on rejection without the bloat

- Rebuild a rejected pack as plain instructions only, cutting the metadata the user called out, instead of defending the draft.

- Re-verify the character count after every rebuild, and report the new count.

- Keep the version history, so a v1.0 draft, a v3.0 rebuild, and a v3.1 revision are each named and each counted.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to compress a draft in stages, showing the count after each stage, when a draft lands far over the limit.

- Ask the user which sections matter most when the limit forces a real cut, instead of cutting a load-bearing section on a guess.
