# Deep research into report and interactive artifact

## When to use

- Use this skill when the user asks a comparison or research question that needs real figures, such as a product against its competitors or a set of models against each other.
- Use it when the answer deserves a lasting report and a page the user can search and filter, not just a chat reply.
- Pick the comparison variant for ranked choices and the catalog variant for a sourced reference list.

## Research into a report

- Write the research into `research_notes/<topic>/report.md` as the single source of truth for the findings.
- Source every figure from an index or a primary source and record the date it was true, because figures go stale.
- Label vendor claims separately from independent checks, and never present a vendor number as if it were independently verified.
- Flag conflicts between sources as conflicts, and flag items you could not verify instead of filling them in.
- Never invent a value. A blank with a caveat beats a plausible-looking guess.

## Give the headlines in chat

- Lead with the headlines in chat: the top findings, the best-for picks, and anything that changes a decision.
- Keep the chat short and point at the report for the detail.

## Build the interactive artifact page

- Build an interactive page from the report with a searchable and filterable table, expandable profiles, and ranked scores for the comparison variant.
- For the catalog variant, include the sourced values, plausibility gates for items that need a special deposit, a copyable JSON data schema, and an explicit caveats section for unverifiable values.
- Probe-verify the page before you hand it over: exercise the filters, confirm there are no console errors, and confirm there is no overflow at phone width.
- Fix what the probe finds and probe again, instead of handing over a page you have not exercised.

## Where this comes from

- This shape was used for Code Forge against 20 competitors with a valuation, 34 free-tier Groq and Gemini models scored, the model sweeps, the Pixel Forge competitive research, Reblend against Blender across 163 capabilities, the 106-record Meridian ground-resources catalog, and the Code Forge logo research with 45 sources. It is recorded in the BNB audit as S11.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to re-run the research for a single entry when one figure looks stale, instead of redoing the whole report.
- Offer a comparison variant first when the user has not said whether they want a ranking or a catalog, and build the catalog only if they ask.
