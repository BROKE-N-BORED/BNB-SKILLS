# S12 — External-tool adaptation study into tiered build queue

## When to use

- Use this skill when the user wants to learn from an external product or tool and bring its good ideas into their own project.
- Use it before any building starts, so the user picks from a tiered list instead of from a pile of notes.
- Frame the study as gap-finding and inspiration, not copying.

## Research the external product

- Deep-research the product's features, how they work, and what they are for, and write the full report to `research_notes/<slug>/report.md`.
- Source the claims and flag vendor claims separately from independent checks, as in [deep-research-artifact](../deep-research-artifact/SKILL.md).
- Keep the report as the record the tiered list is drawn from, so any item can be traced back to its source.
- When the source is a video, check the repos it names for the real cost and hardware footnote before judging fit: "free" can mean a free front end over a paid API, or genuinely local but far above his hardware. HICKSFIELD (2026-11-13 19:13–19:16): Open-Higgsfield-AI is MIT and free as a studio, but every generation is a paid Muapi.ai call through his own key (credits bought in advance; the "small free credit allocation" has no published amount); Imagination Studio is genuinely local and Apache-2.0 but wants 48 GB RAM for pictures, 96 GB for video, and a Mac M5 or DGX Spark, with no CPU-only mode. Neither runs free on his 8 GB PC — the $0 shape that does (FastSD CPU stills + ffmpeg motion + narration) had to be built from different pieces, each verified real.

## Map its features onto the user's project

- Map each feature onto the user's own project as a tiered list: Tier 1 to integrate now, Tier 2 to adapt at the project's scale, and a skip list with a reason for each skip.
- Name the system each item integrates into, so nothing is bolted on beside the project instead of built into it.
- Judge each item against the user's real limits: the hardware it must run on, the hard $0 rule, and the systems that already exist.
- Suggest a build sequence for the tiered list, with a done-means line for each item so its finish is recognisable.
- Check the source product's licence before anything is built from the study. When the code is under a non-permissive licence (enterprise/EE, source-available, or any licence that forbids copying), reimplement the IDEA from scratch in the user's own code — never copy, port, or adapt the source's code. Record the licence and the reimplement decision in the study report so a later reader knows the line was drawn deliberately.

## Let the user pick, then build one at a time

- Present the tiered list and let the user pick the items, in their order.
- When the study covers several tools, the pick can be one best idea from each instead of everything from one: DATAPACKR v0.2 (2026-11-13 19:45) took one idea from each of six studied tools (readers + chunking + exports; provenance + checksums; RAG export; numeric integrity; pack validation + dedupe; exclusion reasons) while keeping its own verbatim promise — no LLM generation anywhere.
- Build each picked item one at a time in an isolated copy (see [isolated-copy-build-merge](../isolated-copy-build-merge/SKILL.md)), verified and held for the merge order.
- Never start the next picked item until the current one is finished, verified, and reported.

## Refresh the study file after the queue ships

- Once the picked items are built and shipped, refresh the study file so it describes what actually happened, not what was planned: current status up front, every feature mapped to the item that implements it, and each item broken down the same way (what was built, the verification numbers, strengths, weaknesses, gaps, UI notes).
- Add a before/after table of what the project had vs what the study line added, the full ship record, and the open remainders listed plainly instead of hidden.
- Keep the original study file untouched as a backup, and fix any stale headers in the working files (a "nothing built yet" header on a shipped list is a lie the next reader will trust).

## Where this comes from

- This shape was used for CodeRabbit (Tier 1 CR1 to CR10, Tier 2 adapt items, skip list), Manus (Tier 1 M1 to M8, Tier 2 M9 to M13), the Forge Browser AI research (22-item improvements document), and the sellable-ads research. The OpenWork borrowables (MCP gateway, usage ledger, scheduled tasks, queued 2026-11-13) are the same shape with the licence gate applied: ideas borrowed, EE-licensed code reimplemented, never copied. The Kitesurf borrowables are a second observed instance: built into Forge Browser v0.8 (verified 493/493 in the merged tree, Release live 2026-11-13 12:16). It is recorded in the BNB audit as S12.

## Alternatives for better results

- Offer to study a second product in the same space when the first study leaves a Tier 1 item with no clear design.
- Offer to fold a picked item into an existing queued build when it touches the same code, instead of building it as a separate item.
