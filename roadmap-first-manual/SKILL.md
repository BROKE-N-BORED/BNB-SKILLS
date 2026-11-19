# S71 — Roadmap-first manual: table of contents as the roadmap, chapters written one at a time, every number verified before it ships

## When to use

- Use this skill when the user wants a full manual written from
  scratch — a long technical document that will grow chapter by
  chapter over many sessions and live in its own repo.
- Use it when the user asks for the table of contents first as a real
  roadmap: sections, subsections, chapters, subchapters. The roadmap
  is the plan the chapters are written against.
- Do not use it for a one-off write-up, or for a single document that
  absorbs corrections over time — that is
  [living-document-build](../living-document-build/SKILL.md), one
  master doc with an audit trio. This skill is a multi-chapter manual
  built chapter by chapter from a pushed roadmap, with per-chapter
  verification of every number.

## Write the roadmap first and push it as a reference document

- Write the full table of contents first: parts, chapters,
  subchapters, appendices. It is the roadmap the whole manual follows.
- Present it to the user and wait for their go-ahead on the shape
  before writing chapters — the roadmap is cheap to change, chapters
  are not.
- Push the roadmap to the repo as a reference document (ROADMAP.md
  plus a short README) and verify by read-back (git blob SHA, see
  [ship-pipeline](../ship-pipeline/SKILL.md)). The roadmap lives in
  the repo from the start so the plan is public and stable.

## Write one chapter at a time, and verify every number yourself

- Write one chapter at a time, in roadmap order, as its own file
  (for example `manual/chapter-01-wasted-effort.md`). Finish the
  chapter, verify it, push it, then start the next one.
- Lead as the expert: do not wait for per-step direction on content.
  The user set the roadmap; the chapter's substance is the author's
  job.
- Verify every number in the chapter yourself before pushing:
  - Cited numbers get checked against their source (a paper's figures
    against the paper, a benchmark against its published page).
  - Measurable claims get measured on the machine at hand (binary
    sizes, memory use, startup timings) — do not quote a number from
    memory when it can be measured in a minute.
  - When a re-measurement under load comes back slower than the
    chapter's table, say so: the order and the gap are what matter,
    and the chapter discloses its method and machine so a reader can
    judge the numbers.
- Check the chapter against the house style before pushing (for
  example: no em-dashes, all planned subsections present).
- Push the chapter and verify by read-back. Report it live with the
  link, the word count, and what was verified — briefly, one chapter
  at a time.

## Where this comes from

- RIZA thread, 2026-11-13 18:15–22:58 EST: Joshua ordered "the full
  manual on building this from scratch start with the table of
  contents so we have a real road map" for the better-way-to-compute
  project. The roadmap (7 parts, 34 chapters, appendices A–F) was
  delivered 18:17 and pushed to BROKE-N-BORED/RIZA as ROADMAP.md +
  README at 19:39 (commit 7cab77f7), verified by blob SHA read-back.
  At 19:43 he set the expert framing ("you are a computer science
  expert with a leading degree in ai and software engineering" — lead,
  do not wait for per-step direction). Chapter 1, "Where today's
  computing wastes effort" (5,071 words, all 5 subsections), was
  pushed at 19:49 (commit 037e3779), blob SHA verified. The author
  verified it himself: 0 em-dashes, Lemire GC numbers confirmed from
  lemire.me, VS Code under-500 MB confirmed, Node 121 MB / Python 8 MB
  / stdlib 55 MB / C hello 16 KB all confirmed by measurement;
  startup timings re-measured under load came back slower than the
  chapter's table (sandbox load), order and gap hold, chapter
  discloses method + machine.
- Five chapters are done so far, all in the same shape: chapter 1
  (19:49), chapter 2, "The core idea" (~20:06, just under 4,700
  words, all 5 subsections, worked arithmetic re-checked by script),
  chapter 3, "Rules and limits for this build" (~20:20, just over
  3,100 words, all 3 subsections, machine specs matched to his PC),
  chapter 4, "The dictionary: short codes for common work" (~22:20,
  just over 5,400 words, all 4 sections, first chapter of Part 2,
  worked example re-run from scratch — text 68 bytes against dense
  37), and chapter 5, "Types and data" (~22:58, just over 5,100
  words, all 4 sections, cache sizes confirmed against AMD's own page
  for his chip — L1 192 KB, L2 1 MB, L3 4 MB — sizes and load counts
  only, no timings). Each was verified by the author (0 em-dashes,
  all planned subsections, numbers checked) and pushed with a blob
  SHA read-back. The workflow is confirmed end-to-end five times
  over, not once.
- Chapters 6–13 all landed in-window, 2026-11-13 ~23:59 through
  2026-11-14 ~11:48, each ~4,500–5,500 words, parent-read and
  read-back verified, each starting on his one-word "Go": ch6
  "Memory without a garbage collector" (2026-11-13 ~23:59), ch7
  "Functions, flow, and errors", ch8 "The human view", ch9 "The
  binary format" (first of Part 3), ch10 "The shared middle form",
  ch11 "The bootstrap compiler", ch12 "The optimizer", ch13 "Self
  hosting" (2026-11-14 ~11:48). The manual is now through chapter
  13, Part 3 underway — the workflow is confirmed end-to-end
  thirteen times over. (RIZA thread 9aa4d5d7.)
- Chapters 14-22 all landed in-window, 2026-11-15 ~23:18 through
  2026-11-17, each starting on his one-word "Go": ch14 "Build
  tool and packages" (last of Part 3, 2026-11-15 ~23:18), ch15
  "Startup and shutdown" (first of Part 4, 2026-11-16 ~00:49),
  ch16-18 (2026-11-16 daytime), ch19 "Text tools", ch20
  "Developer tools", ch21 "The shell" (last of Part 5), ch22
  "Kernel design" (first of Part 6). The manual was then through
  chapter 22, Part 6 underway - the workflow was confirmed
  end-to-end twenty-two times over. (RIZA thread 9aa4d5d7.)
- Chapters 23-25 all landed in-window, 2026-11-17 18:48:51
  through 2026-11-18 ~20:50, each starting on his one-word
  "Go": ch23 "Boot: from power on to prompt" (live 2026-11-18
  ~13:13, just under 5,500 words, 27 steps power-on to prompt),
  ch24 "Processes and scheduling" ("Go" 2026-11-18 14:06, live
  the same day, just over 5,400 words; fixes the naming ch22
  left open: PIDs from 1, the shell is 1, 0 means no program,
  4 bytes, ~136 years at one start per second), and ch25
  "Memory in the kernel" ("Go" 2026-11-18 20:50, live the same
  evening, just under 5,500 words, 21 bytes per run, hello loop
  12 to 16 entries). The manual is now through chapter 25,
  Part 6 - the workflow is confirmed end-to-end twenty-five
  times over. (RIZA thread 9aa4d5d7.)
- Each chapter starts on the user's go-ahead — a one-word "Go" in the
  thread — one chapter at a time. Do not chain chapters without it.

## Alternatives for better results

- Offer to re-verify a chapter's numbers when the machine or the
  sources change, instead of letting a measured table go stale.
- Offer a consistency pass across chapters once several exist, so a
  number in chapter 1 and the same number in chapter 5 cannot drift
  apart (see [living-document-build](../living-document-build/SKILL.md)
  for the audit shape).
