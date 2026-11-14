# S70 — UI design source library: study live software, write up what works, keep the repo every app pulls its feel from

## When to use

- Use this skill when the user wants a standing library of UI design
  source material — techniques gathered from real shipping software
  that every project in the family can pull from.
- Use it to seed a new library repo (charter + first file) and to
  maintain it afterwards: new techniques in, uploads diffed before
  they are added, wording reconciled, nothing duplicated, nothing
  stale.
- Do not use it for a one-off study of a single product: that is
  [external-tool-adaptation-study](../external-tool-adaptation-study/SKILL.md),
  one product into a tiered build queue for one project. This skill is
  continuous, multi-product, and cross-project — the library is the
  deliverable, not the queue.

## Lock the charter and the bar first

- Write the charter before the first file: what the library is (the
  source every app pulls its feel from), what it holds (techniques
  from real shipping software — games, apps, websites, phones,
  tablets, gadgets), and how it is kept (sourced, dated, organized
  for fast lookup).
- Set the bar a technique must pass before it goes in, in the user's
  own terms: the toy test (a child could pick it up and use it), it
  runs on his 8 GB no-GPU Mint PC (cheap motion only), it does
  something real, and it fits the design rules. The identity question
  is "Does it make the app feel like itself?" — decoration that gives
  an app its identity is fine; what fails is motion or styling that
  fights readability or costs frames.
- Never write a rule into the charter that the user did not set.
  "No decoration for its own sake" was Arlo's own note dressed up as
  a rule in the first charter draft, and it had to be struck after
  his correction (2026-11-13 19:40): creativity is wanted, and
  "everything looks the same" is a named problem, not a preference to
  guess at. Grep the master rules file before citing any rule as
  immutable — if it is not there, it is not a rule.
- Get the charter locked in by the user before seeding the repo.

## Study live products, write each technique up properly

- Scour the web and study real software that is shipping right now —
  not textbook patterns or decade-old listicles. The technique has to
  be modern, simple, satisfying, and not run-of-the-mill.
- Write each technique up with the same shape: what it is, why it
  feels good, the exact numbers (timings, sizes, easing), which apps
  it fits, and what to watch out for.
- Source and date every file, so nothing goes stale silently.
- Keep the repo organized like an encyclopedia, for fast lookup: one
  entry per file under `entries/`, each self-contained with its own
  sources and See also cross-references; permanent numbers (001–048
  and on) that are never renumbered or reused; an INDEX.md that is
  alphabetical first, then by topic, then by app; a CHANGELOG.md, a
  queue.md for held items and gaps, a verdicts.md for the feedback
  loop, and an entry template. The filter lives in one place only,
  the README. The master rules file stays at the root as the source
  of truth — from 2026-11-13, ALL UI-related design rules and material
  get pulled from this repo, not from scattered local copies. Batch
  files (many techniques in one file) were the seed shape; the
  encyclopedia layout replaced them once the library passed two
  batches, because one technique is one readable page on the phone
  and adding one never touches another file.

## Gap-audit the library before every sweep

- Before each research sweep, check what the library is missing
  first, so the sweep fills what the library needs as well as
  finding new material (standing rule from Joshua, 2026-11-13
  ~20:22).
- The audit covers: entries with no attributable source, batch-level
  sources never attributed to an entry, queue.md items (held entries
  and source gaps), and non-technique entry types the library does
  not cover yet.
- The sweep then does gap-filling first and new entries second —
  Drop 3 opened with the audit (five sourceless entries, two
  unattributed roundups, the queue) before researching new entries.

## Rule repos sit alongside the library repo

- The library repo is the source of truth for his rules. Alongside it,
  three outside repos are rule repos for UI design work (Joshua, main
  chat, 2026-11-13 23:00): bradtraversy/design-resources-for-developers
  (67k stars — the master list: graphics, fonts, colors, icons, stock,
  templates, CSS frameworks, animation and chart libraries, UI
  components and kits, design systems, tools), VoltAgent/awesome-design-md
  (127k stars — DESIGN.md files analyzing popular brand design systems
  by category), and gztchan/awesome-design (17.8k stars — stock, color,
  icons, typography, toolkits, prototyping, testing, styleguides,
  tutorials, books). Every UI task pulls from them as outside
  references; his own rules in the library repo win on any conflict,
  and brand material is inspiration, never a straight copy.
- The same pattern holds for the game-design library, which has its
  own rule repos (magictools for resources and tools,
  awesome-game-design for learning and design documents — Joshua,
  main chat, 2026-11-13 22:52 and 22:54). A library's rule repos are
  set by him, named in its charter and README, and checked first for
  every resource in their subject.

## Apply the library to a product: audit its UI against the repo

- When the user sends the library link to a product thread with
  an audit order, audit that product's actual UI code against
  the repo — the master rules (U1–U39, D1–D3) and the entries —
  not against a local copy: read the repo fresh, because
  entries land by the drop and a stale local copy misleads
  (Syllaport caught its rules copy stale; QWKHND's stale copy
  flagged a rules inconsistency that did not exist in the repo;
  Yahtzee's count went 24 → 48 across Drops 3 and 4 in one
  evening).
- Map entries to the app and apply the filter in the open:
  entries that fail it are ruled OUT in the report with the
  reason (STELLA: 17 of 24 entries in, 7 out — liquid glass
  costs frames on his PC, pie menus fail the toy test), not
  silently skipped.
- Write the findings as redesign tasks, merge them into the
  product's current task list (see
  [audit-findings-task-list-merge](../audit-findings-task-list-merge/SKILL.md)),
  and reorder the full list highest to lowest on his order.
  Report the entry count as of the audit — the library can grow
  mid-audit (Drop 3 landed while STELLA's audit #9 was running;
  the audit covered the 24 entries present when it started and
  offered a follow-up pass on the new ones).
- Thirteen product threads ran this same shape the night of
  2026-11-13 (REBLEND, STELLA, DUO, Pixel Forge, OLLAMA System
  Test, StemLab, QWKHND, Yahtzee, Syllaport, FYRN, HICKSFIELD,
  ACR, MIMIK), each from the same order text, each landing its
  audit and redesign list the same evening.

## Seed the repo, then diff every upload before adding it

- Seed with the charter README plus the first technique file, push,
  and verify by read-back (git blob SHA, see
  [ship-pipeline](../ship-pipeline/SKILL.md)).
- When the user uploads files to add, DIFF them against what the repo
  already holds before adding anything:
  - Byte-identical to a file already in the repo → already in, nothing
    to add.
  - Word-for-word inside the master doc → already in, nothing to add.
  - A pre-removal snapshot carrying content he ordered removed → stays
    out. Do not re-add removed content because an old file still has
    it.
- Reconcile duplicate wording: when the same rule or filter exists in
  two files with different words, make them match, so the repo does
  not carry two versions of the same thing.
- Report what was added and what was skipped, with the reason for each
  skip. Nothing duplicated is the goal.

## Where this comes from

- BNB UI design library thread, 2026-11-13 19:38–19:52 EST: Joshua set
  the thread ("you scour the internet and study real software and find
  real up-to-date and modern tips tirrcks and techniques ... and you
  upload and manag the github repo BNB UI DESIGN SOURCE FILE LIBRARY"),
  locked the charter in at 19:45, created the repo himself at 19:46
  (https://github.com/BROKE-N-BORED/BNB-UI-DESIGN-SOURCE-FILE-LIBRARY-),
  and sent three files at 19:48 ("Add these files first I guess"). Two
  pushes, both verified by read-back: the seed (README charter + file
  001, the 12-technique Modern UI file researched in main chat the
  same day) and the foundation (the combined master design-rules.md at
  the root — philosophy, all 39 rules, techniques drawer — 001
  reconciled to the new Q4, README updated). The three uploads were
  diffed first: 42 byte-identical to 001, 44 word-for-word inside the
  master, 43 the pre-removal STELLA snapshot that stays out.
- The library grew past the batch shape the same evening. Drop 2
  (games, editors, gadgets — 12 more techniques, all sources
  spot-checked against the live pages) landed ~20:02–20:06, and
  Joshua then asked for the repo run "like an encyclopedia library
  on ui design" (~20:08). The rebuild split both batches into 24
  entries under `entries/` (001–012 Drop 1, 013–024 Drop 2), added
  INDEX.md, CHANGELOG.md, verdicts.md, queue.md, templates/entry.md,
  and the MIT LICENSE, moved the filter to the README alone, and
  retired the old batch files; pushed 20:20 and verified by script
  (all entry bodies verbatim vs the batch sources, all links
  resolve). Drop 3 ("Input, feedback, and forgiveness", entries
  025–036) landed 21:05 (commit 36f7c94d, 44 files, SHA read-back
  verified) — it filled all five source gaps first, so no entry in
  the library is sourceless anymore. Drop 4 ("Seeing, learning, and
  responding", entries 037–048) landed 22:29, taking the library to
  48 entries; its gap audit found no sourceless entries, lifted the
  three thin themes from 2 to 4 entries each, and landed all four
  Drop 3 holds (coach marks, live presence, sound, diff views). Drop
  5 opened ~22:57 under the same rule, starting with strengthening
  the 10 entries that still have only one source each. The same
  library shape is being applied a second time for game design:
  Joshua locked that charter in 23:07–23:09 the same night
  (encyclopedia from day one, gap audit before every sweep,
  magictools + awesome-game-design as its rule repos) — its repo
  does not exist yet and Drop 1 is not pushed, so this is a second
  application of the pattern, not a second proof of it.
- The source-of-truth order is main chat, 2026-11-13 19:47: "For now
  on all ui reacted design rules and stuff get pulled from this repo".

## Alternatives for better results

- Offer to pull a technique into a specific app's build brief when a
  build starts, instead of leaving the library as reference only —
  the techniques file already maps techniques to projects.
- Offer a periodic staleness pass: re-check the oldest files against
  what is shipping now, and mark or replace anything the field has
  moved past.
