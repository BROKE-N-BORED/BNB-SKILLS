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
- Keep the repo organized for fast lookup: numbered technique files,
  a README that says what the library is and how to find things, and
  the master rules file at the root as the source of truth — from
  2026-11-13, ALL UI-related design rules and material get pulled from
  this repo, not from scattered local copies.

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
- The source-of-truth order is main chat, 2026-11-13 19:47: "For now
  on all ui reacted design rules and stuff get pulled from this repo".

## Alternatives for better results

- Offer to pull a technique into a specific app's build brief when a
  build starts, instead of leaving the library as reference only —
  the techniques file already maps techniques to projects.
- Offer a periodic staleness pass: re-check the oldest files against
  what is shipping now, and mark or replace anything the field has
  moved past.
