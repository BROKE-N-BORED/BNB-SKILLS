# S12 — External-tool adaptation study into tiered build queue

## When to use

- Use this skill when the user wants to learn from an external product or tool and bring its good ideas into their own project.
- Use it before any building starts, so the user picks from a tiered list instead of from a pile of notes.
- Frame the study as gap-finding and inspiration, not copying.

## Research the external product

- Deep-research the product's features, how they work, and what they are for, and write the full report to `research_notes/<slug>/report.md`.
- Source the claims and flag vendor claims separately from independent checks, as in [deep-research-artifact](../deep-research-artifact/SKILL.md).
- Keep the report as the record the tiered list is drawn from, so any item can be traced back to its source.

## Map its features onto the user's project

- Map each feature onto the user's own project as a tiered list: Tier 1 to integrate now, Tier 2 to adapt at the project's scale, and a skip list with a reason for each skip.
- Name the system each item integrates into, so nothing is bolted on beside the project instead of built into it.
- Judge each item against the user's real limits: the hardware it must run on, the hard $0 rule, and the systems that already exist.
- Suggest a build sequence for the tiered list, with a done-means line for each item so its finish is recognisable.

## Let the user pick, then build one at a time

- Present the tiered list and let the user pick the items, in their order.
- Build each picked item one at a time in an isolated copy (see [isolated-copy-build-merge](../isolated-copy-build-merge/SKILL.md)), verified and held for the merge order.
- Never start the next picked item until the current one is finished, verified, and reported.

## Where this comes from

- This shape was used for CodeRabbit (Tier 1 CR1 to CR10, Tier 2 adapt items, skip list), Manus (Tier 1 M1 to M8, Tier 2 M9 to M13), the Forge Browser AI research (22-item improvements document), and the sellable-ads research. It is recorded in the BNB audit as S12.

## Alternatives for better results

- Offer to study a second product in the same space when the first study leaves a Tier 1 item with no clear design.
- Offer to fold a picked item into an existing queued build when it touches the same code, instead of building it as a separate item.
