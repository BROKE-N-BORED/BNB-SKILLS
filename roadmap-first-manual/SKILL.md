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

- RIZA thread, 2026-11-13 18:15–20:20 EST: Joshua ordered "the full
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
- Three chapters are done so far, all in the same shape: chapter 1
  (19:49), chapter 2, "The core idea" (~20:06, just under 4,700
  words, all 5 subsections, worked arithmetic re-checked by script),
  and chapter 3, "Rules and limits for this build" (~20:20, just over
  3,100 words, all 3 subsections, machine specs matched to his PC).
  Each was verified by the author (0 em-dashes, all planned
  subsections, numbers checked) and pushed with a blob SHA read-back.
  The workflow is confirmed end-to-end three times over, not once.
- Each chapter starts on the user's go-ahead — a one-word "Go" in the
  thread — one chapter at a time. Do not chain chapters without it.

## Alternatives for better results

- Offer to re-verify a chapter's numbers when the machine or the
  sources change, instead of letting a measured table go stale.
- Offer a consistency pass across chapters once several exist, so a
  number in chapter 1 and the same number in chapter 5 cannot drift
  apart (see [living-document-build](../living-document-build/SKILL.md)
  for the audit shape).
