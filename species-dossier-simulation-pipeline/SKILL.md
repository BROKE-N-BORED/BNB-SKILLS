# Species dossier simulation pipeline

Turn a real species into a buildable simulation entity, starting from research, through a fixed-template dossier and a gap register, to a pilot build verified numerically and visually. Use this skill whenever a species, or a set of species, needs to become a sim entity.

## Research the species and write the dossier

- Research the species deeply, or work from a research report the user supplies, and keep the research grounded in real sources.

- Write the dossier on the fixed template in `references/species-dossier-template.md`, so every species gets the same sections in the same order.

- Fill in the form and 3D spec, the phenology, the habitat rules, the life cycle, the food web, the manipulation responses, and the simulation parameter table.

- Label every assumption as an assumption, and keep conflicting sources as conflicts, naming both sides, instead of picking one silently.

- Never invent a literature gap, and leave a value blank when the literature does not give it, such as a hide thickness nobody has measured.

## Audit the gaps and keep a gap register

- Run a gap audit on the finished dossier, asking what is still missing to recreate this animal.

- Sort every gap into the gap register, using the template in `references/gap-register-template.md`, with four buckets, already filled, derivable, needs research, and unknowable.

- Label a derivable value as *derived*, and never dress a derived number as a measured one.

- Leave an unknowable gap blank in the dossier, and say it is blank, instead of filling it with a plausible guess.

- Run targeted research rounds for the gaps that need research, and fold each round back into the dossier, keeping the dossier as the single source of truth.

## Pilot build in a sandbox and verify

- Build a pilot of the species in a standalone sandbox, using only the dossier's numbers, before the species goes anywhere near the main sim.

- Verify the pilot numerically, measuring the sim behavior against the dossier parameters, and verify it visually with screenshots of the actual pilot file.

- Report the numeric results and the screenshots together, and name any behavior that does not match the dossier.

- Fold a verified pilot back into the main build only after the verification passes, and keep the dossier, the gap register, and the pilot file together as the species record.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to run the dossier step for a whole catalog at once, such as a berry catalog or a fish list, when the user needs many species to the same standard.

- Ask the user for their own research files or photos when the public literature leaves a key value blank.
