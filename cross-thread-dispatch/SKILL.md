# S3 — Cross-thread dispatch and report-back

## When to use

- Use this skill whenever work belongs to a thread other than the one you are in, such as a DEV thread, a review thread, or the main chat.
- Use it to send a build, a review, a trial, or a merge note to its owning thread, and to report a completion back to the thread that asked for it.
- Keep each thread to its one subject and route off-topic items to their own threads instead of working them where they landed.

## Write a self-contained brief

- Send a brief the receiving thread can act on without reading your thread: what to do, why it matters, the constraints it must respect, and what to report back.
- Use the [dispatch brief template](references/brief-template.md) for the brief and the completion report.
- State the constraints explicitly, including the hardware limits, the hard $0 rule, and any rule the work must not break.
- Name exactly what the report-back must contain, such as file paths, byte sizes, counts, and orientation.
- Name the held build path and attach the battery receipt when the brief is a merge note, so the receiving thread can delta-port it (see [isolated-copy-build-merge](../isolated-copy-build-merge/SKILL.md)).
- Keep the brief to the one task and leave the next item out until this one is done.
- Under the no-stalling rule, a handoff to the owning thread carries the ship order with the port spec: port it, merge it, push it — no waiting on a merge order. The receiving thread confirms the queue position back to the sender. In a thread that never touches the shared tree, handing over the port spec plus ship order IS the ship step.
- If the owning thread is paused when the merged tree goes green, the thread holding the merged tree ships it itself (push + Release) rather than letting the build stall behind a paused thread. (DEV 2026-11-13 14:05: "the Manus thread's paused, so I'm shipping this build myself once it's green." Single instance — stated as the standing call, not a proven pattern.)

## Broadcast a standing rule

- When the rule is a LIST to compile (not a single sentence), mine it from chat history first: scan each dev/UI thread for rules that are consistent across builds, compile them into one list with the source thread cited for each rule, then broadcast. The design-rules list (main chat, 2026-11-13 14:41–14:47) was mined from 23 threads by 3 subagents reading recent turns only, and delivered to all 29 dev/UI threads as U1–U33 + D1–D2 with 17 project entries.
- When the user sets a rule that applies to every thread ("send that to every chat thread"): record it in memory first, then send the same brief to every build thread it applies to — 27 threads for the no-stalling rule and the mandatory gate (2026-11-12). Skip threads it does not apply to (non-build threads: elder report, medical).
- Paused threads still get the broadcast: a pause stops work, not one-way delivery. Joshua, main chat 2026-11-13 14:42: paused dev/UI threads get the list anyway — delivery does not reopen the thread. Mark the delivery one-way and leave the pause standing.
- Each thread records the rule as standing and, for the no-stalling rule, ships anything finished that was sitting unshipped.
- When the rule requires work in each thread (not just recording), each thread audits its own tree and repo and fixes in place with its next build — the secrets rule rolled out that way to all 19 build threads (main chat, 2026-11-13 10:04). Anything already committed to GitHub history gets flagged to the main chat instead of fixed by rewriting history; history is never rewritten unasked.
- Report-backs from dispatched work no longer wait for the user's approval before the next item starts — the no-stalling cycle applies to dispatched work too.
- Never cite a rule as immutable unless it is in the master rules file — check first. Your own notes, another project's rules, and a techniques file's filter are not his rules: "no decoration for its own sake" was Arlo's own note elevated into a rule and had to be struck from the charter, the techniques file, and a build brief after his correction (2026-11-13 19:40). Grep the rules file before citing; if it is not there, it is not a rule.

## Report completions with verified facts only

- Report back only facts you verified yourself, with the file path, size, count, or measurement that proves each one.
- When work sits with another thread, say plainly which thread pushes and where the work is. "It's with DEV" with no explanation reads as stalling — the user cannot tell waiting from stuck. (SECURITY thread 2026-11-13 14:12: Joshua — "Push it and uodate the goddammit realeae alrwady why the fuci Atwater you doing yhat?"; the assistant's own admission: "I should've made that clearer instead of just saying 'it's with DEV.'")
- Say plainly what is still unverified or still needs the user's own PC instead of filling the gap with a guess.
- Send the completion report to the thread that asked for the work, not to a third thread.
- Keep the report short: what was done, where it lives, what the checks showed, and what is still open.

## Where this comes from

- This is the constant coordination pattern across the main chat and every DEV thread, used for the MIMIK and Reblend bridge, the Blender MCP wiring, the Raon trial, the Yahtzee die, the Victor reference sheets, and DEV to GITHUB merge notes, and is recorded in the BNB audit as S3.

## Alternatives for better results

- Offer to forward a reference file or screenshot with the brief when the receiving thread needs to see it rather than read about it.
- Offer to split a brief into two dispatches when it covers two owning threads, instead of sending one brief to the wrong place.
