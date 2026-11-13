# Cross-thread dispatch and report-back

## When to use

- Use this skill whenever work belongs to a thread other than the one you are in, such as a DEV thread, a review thread, or the main chat.
- Use it to send a build, a review, a trial, or a merge note to its owning thread, and to report a completion back to the thread that asked for it.
- Keep each thread to its one subject and route off-topic items to their own threads instead of working them where they landed.

## Write a self-contained brief

- Send a brief the receiving thread can act on without reading your thread: what to do, why it matters, the constraints it must respect, and what to report back.
- State the constraints explicitly, including the hardware limits, the hard $0 rule, and any rule the work must not break.
- Name exactly what the report-back must contain, such as file paths, byte sizes, counts, and orientation.
- Name the held build path and attach the battery receipt when the brief is a merge note, so the receiving thread can delta-port it (see isolated-copy-build-merge).
- Keep the brief to the one task and leave the next item out until this one is done.
- Under the no-stalling rule, a handoff to the owning thread carries the ship order with the port spec: port it, merge it, push it — no waiting on a merge order. The receiving thread confirms the queue position back to the sender. In a thread that never touches the shared tree, handing over the port spec plus ship order IS the ship step.

## Broadcast a standing rule

- When the user sets a rule that applies to every thread ("send that to every chat thread"): record it in memory first, then send the same brief to every build thread it applies to — 27 threads for the no-stalling rule and the mandatory gate (2026-11-12). Skip threads it does not apply to (non-build threads: elder report, medical).
- Each thread records the rule as standing and, for the no-stalling rule, ships anything finished that was sitting unshipped.
- Report-backs from dispatched work no longer wait for the user's approval before the next item starts — the no-stalling cycle applies to dispatched work too.

## Report completions with verified facts only

- Report back only facts you verified yourself, with the file path, size, count, or measurement that proves each one.
- Say plainly what is still unverified or still needs the user's own PC instead of filling the gap with a guess.
- Send the completion report to the thread that asked for the work, not to a third thread.
- Keep the report short: what was done, where it lives, what the checks showed, and what is still open.

## Where this comes from

- This is the constant coordination pattern across the main chat and every DEV thread, used for the MIMIK and Reblend bridge, the Blender MCP wiring, the Raon trial, the Yahtzee die, the Victor reference sheets, and DEV to GITHUB merge notes, and is recorded in the BNB audit as S3.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to forward a reference file or screenshot with the brief when the receiving thread needs to see it rather than read about it.
- Offer to split a brief into two dispatches when it covers two owning threads, instead of sending one brief to the wrong place.
