# Model sweep and roster audit

## When to use

- Use this skill when a new model appears and needs judging, when a roster seat opens, or when the installed roster needs an audit.
- Use it before any model is pulled or trialled, so the trial order is ranked and the rejects are named.
- Re-check against a fresh `ollama list` every time, and never trust a stale roster.

## Grade candidates against the machine

- Grade each candidate against the real hardware: the RAM ceiling, CPU-only running, the quant size, the licence, and runtime compatibility.
- Prefer the best smallest model that runs comfortably on the machine, and count speed as part of the grade.
- Treat abliteration as preferred, not gating, and treat any cloud option as hard $0 with no card, or not an option at all.
- Flag vendor benchmarks as unreproduced wherever they are the only evidence, and never present a vendor number as a measured result.

## Judge against the incumbent roster seats

- Judge each candidate against the incumbent roster seats: driver, reviewer, vision, tool, and fast.
- Write an incumbent verdict for each seat, naming whether the candidate beats the incumbent, ties it, or loses to it.
- Produce ranked trials with exact pull tags, a watchlist, a rejects-with-reasons list saved as do-not-re-propose, cloud picks, and an unverified list.
- Audit the installed roster per seat as well, naming the cheapest wins (such as a Q8_0 to Q4_K_M re-pull) and the dead weight to cut.
- See references/roster-audit-template.md for the audit layout.

## Run the trials in order

- Give the user hand-typeable `ollama pull` commands in trial order, one short single-line command at a time (see guided-build-walkthrough).
- Test each trial model on the same task so the results are comparable, and take the pass or fail verdict from the user's screenshot.
- Record each trial verdict with the evidence, and fold the winner into the roster only after it passes the same-task test.

## Where this comes from

- This shape graded the roughly 40-model Hugging Face 2B sweep, the Model Research sweeps 1 and 2, the Forge roster audit, and the Stella roster corrections from a fresh `ollama list`. It is recorded in the BNB audit as S13.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to run an A/B trial between two close candidates on the same task when the grades tie.
- Offer to re-audit the roster after a trial lands, instead of letting the old audit describe a changed roster.
