# S92 - How-to-manual: a verified A4 PDF manual in plain words, with the source beside it

Executable twin in BNB-TOOLS: [T41 manual-pdf-builder](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/manual-pdf-builder).

When Joshua orders a how-to manual, build it as an A4 PDF from a
verified source doc. Write the manual in plain words, verify every
claim against the real project tree, render the PDF through headless
Chromium, check there are no em-dashes, and deliver the PDF plus its
source. Anything not verified gets named in the manual, not smoothed
over.

## When to use

- Use this skill when Joshua asks for a how-to manual, a user
  guide, or an easy-to-read manual for a project.
- Use it for any project, app, or tool: every BNB tool and every
  Joshua project eventually needs one of these.
- Do NOT use it as a substitute for making the app usable on its
  own. The manual explains the app; it does not excuse a design
  that needs explaining first (see
  [pick-it-up-and-it-works](../pick-it-up-and-it-works/SKILL.md)).

## The playbook

1. Write MANUAL.md in plain words. Short sentences, no jargon, no
   unexplained numbers. The reader is Joshua, reading on his phone
   or his PC.
2. Verify every claim against the real tree. Every path, name,
   version, and step the manual cites must exist in the project
   tree or be checked against the real thing. A claim that cannot
   be checked is not written as fact.
3. Render the PDF via headless Chromium. MANUAL.md goes to styled
   HTML, then to an A4 PDF. (The SOLDAR manual used Playwright
   headless Chromium.)
4. Check no em-dashes. The manual carries no em-dashes anywhere, in
   the source or the PDF. Check with a byte search, not by eye.
5. Deliver PDF plus source. He gets the PDF to read and the
   MANUAL.md source to keep and change.

## Name what is not verified

- Unverified items must be named, not smoothed over. If a claim
  could not be checked, the manual says so plainly, in the manual
  itself.
- The SOLDAR manual shipped with three named unverified items: the
  live v0.3.0 release link, port-in-use behavior, and a Code
  example that was not executed. Naming them is part of the
  delivery, not a failure of it.
- Never write an unverified claim as if it were checked. A gap
  named is honest; a gap hidden is a defect.

## Worked example: the SOLDAR manual

- Ordered 2026-11-18 ~13:56 EST: "Create an easy to read how to
  use manual for me please."
- Delivered same day ~13:58: 8 pages, A4, 156 KB PDF, source
  MANUAL.md beside it, in the soldar-manual folder in the
  workspace (workspace/soldar-manual/Soldar-Manual.pdf).
- Built via Playwright headless Chromium, verified against the
  tree, no em-dashes.
- Three unverified items named in the delivery: the live v0.3.0
  release link, port-in-use behavior, the Code example not
  executed.

## What to check

- Every path and name in the manual exists in the real tree.
- Every step in the manual was checked against the real program or
  the real tree.
- The PDF is A4, readable, and matches the source.
- No em-dashes in the source or the PDF (byte check).
- Unverified items are named in the manual, not hidden.
- Both files are delivered: the PDF and the MANUAL.md source.

## Where this comes from

- SOLDAR thread, 2026-11-18 ~13:56 EST. Joshua: "Create an easy
  to read how to use manual for me please." Delivered ~13:58 the
  same day.
- Found in the eighth BNB delta scan (2026-11-18).
  Assistant-inferred from a Joshua-ordered instance; the
  executable twin is T41 manual-pdf-builder in BNB-TOOLS.
