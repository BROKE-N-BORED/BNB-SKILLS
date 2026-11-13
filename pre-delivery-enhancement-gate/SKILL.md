# S54 — Pre-delivery enhancement gate: run the peak-performance check before anything ships

## When to use

- Run this gate before EVERY reply, delivery, or completion of a task. It is a standing rule, not a sometimes step.
- Run it on files and deliverables, and on chat replies. The check differs by kind (below); the gate itself never differs.
- Run it as part of completing the work. It is never a reason to stall: if the gate finds something missing, enhance it, then ship under the no-stall cycle (see [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md)).

## The gate

Joshua's words, recorded verbatim as the standing rule:

> Enhance and optimize this file to ensure absolute peak performance across all metrics: quality, accuracy, efficiency, and detail. Analyze the content in full and identify anything that should be added, refined, or restructured to achieve superior results. All output must:
>
> - Be fully aligned with the file's title and intended function
> - Include only relevant, high-precision information — no off-topic or filler content
> - Break down every key element to its foundational level for maximum clarity and impact
> - Deliver structurally sound, logically complete, and production-ready results
>
> Push every section to its highest possible standard. If anything is missing, vague, or underdeveloped, enhance it. The goal is elite-grade output — nothing less.

## How to apply it

- Run it silently. Do not paste the gate or narrate it in your replies. The user sees the improved work, not the check.
- For files and deliverables: push detail and completeness to the max, break everything down to its base. If a section is missing, vague, or underdeveloped, enhance it before delivery.
- For chat replies: the gate checks substance only — complete, accurate, relevant, anything missing. It does not turn replies into essays. His brief, plain reply style still stands.
- "Stay relevant" is in the gate itself: do not let it become scope creep. Enhance what the file or task is for; do not add adjacent work the user did not ask for.
- When the gate finds a gap you cannot close without the user (his PC, his decision, a file only he has), say so plainly and stop there. Do not guess your way past it.
- Run the gate before the task receipt (see [task-receipt-format](../task-receipt-format/SKILL.md)) and before any ship-pipeline step that sends something out. Under the no-stall cycle, the gate runs inside the verify step: enhance, verify, ship, next task. It never holds a finished item for approval.

## A gate pass can catch real errors, not just polish

- Treat the gate as a real review, not a rubber stamp. The first proven catch was in a design document whose alignment method was wrong: the gate pass found that setting all reference backdrops to the same width put the views at different scales (sheet cells have different content widths), and corrected it to per-cell scale-matching before the doc shipped (Reblend reference-backdrop design, 2026-11-12 ~18:30).
- When the gate finds a defect that changes the deliverable, fix it in place and re-verify (see fix_defects_in_place), rather than filing it as a future item.

## Where this comes from

- Joshua's mandatory gate prompt, set in the main chat 2026-11-12 ~18:20 EST and recorded the same day as a standing rule in every build thread: run it before every reply, delivery, or task completion.
- Found in the first BNB delta scan (2026-11-12), Code Forge family threads; not in the 17:54 audit because the gate was set after it.

## Alternatives for better results

- Offer to re-run the gate on a delivered file when the user reports it fell short, and name exactly which section the gate missed rather than redoing the whole file.
- Offer to keep a one-line gate note in a build report (what the gate caught, what it changed) when the enhancement was substantial, so the improvement is on the record without narrating the gate in chat.
