# S86 - Dogfood review: run the app as a user and report what is actually wrong with it

Run the built app on your own system as a user, and look for what is
actually wrong with it: errors, flaws, inconvenient and cluttered UI,
functions and features that are missing or need improvement, and gaps.
Report it as a numbered review with counts. This is a drive of the real
app by a real user, not a read of the code and not a test suite.

## When to use

- Use this skill when the user orders a run-as-user review, or when
  a build has reached a point where the next question is "does it
  actually work for a person" rather than "does the suite pass".
- Use it for a second review after fixes land: the round-2 review
  checks the fixes held, not just that they were written.
- Do NOT use it as a substitute for the test suite: the suite proves
  the code, the review proves the experience. Both run; neither
  replaces the other.
- Do NOT use it to review code you have not run: a review written
  from reading the tree is a product review (see
  [full-product-review](../full-product-review/SKILL.md)), not a
  dogfood review. The difference is the driving.

## Drive the app the way he will

- Run the app on your own system, as a user, through the same paths
  he will take: open it, use every screen and every function, do
  the jobs the app exists to do.
- Look for errors first: crashes, hangs, functions that fail, and
  functions that silently do nothing. A function that runs for a
  while and then does nothing is an error, not a slow function.
- Look for flaws next: things that work but work wrong - wrong
  results, lost work, state that lies about itself.
- Look at the UI as a user: inconvenient and cluttered elements,
  things that are hard to find, things that are hard to read, and
  things that cannot be closed, opened, or reached. Count the
  controls when clutter is the finding, so the claim carries a
  number.
- Look for what is missing: functions and features the app should
  have and does not, and gaps between what it promises and what it
  does.
- Drive it at the widths he will use. For a web app, that means
  phone width from the start, not as a later pass: ARCHIVE FLIX's
  first review found the phone gap late because the drive ran at
  desktop width only.

## Report it as Review N, with counts

- Number the review: Review 1, Review 2, and so on, per project.
  The number is what the round-2 re-review refers back to.
- Report the findings as a numbered list with counts: how many
  findings, how many high, how many in each area. A review with no
  counts cannot be checked later for whether the fixes held.
- Each finding says what is wrong, where it is, and what a user
  hits when they meet it. A finding with no user-visible symptom
  is a code note, not a review finding.
- Fold the findings into the project's task list in priority order
  (see [audit-findings-task-list-merge](../audit-findings-task-list-merge/SKILL.md)
  and [plain-text-task-lists](../plain-text-task-lists/SKILL.md)),
  and let him direct the fixes from the list.

## Round 2: check the fixes held

- After the fixes ship, run the review again on the new version
  and check each fix from the last review: held or not. Report
  the hold count plainly: "46 of 47 fixes hold" is the shape.
- A fix that does not hold goes back on the list as its own item,
  with what the re-review actually saw. Do not re-report it as
  fixed because the code changed.
- A round-2 review also looks for new findings the first review
  missed: the second drive is not only a re-check, it is a fresh
  drive of the new version.

## Where this comes from

- Joshua's order, sent verbatim to 10+ threads in 13+ sends across
  2026-11-16 and 2026-11-17: "Ok when you have the compute on
  your end run it on your system as a user and look for any
  errors flawss, inconvenient and cluttered uibelemts, see ehat
  functions and features are missing or need improvements, any
  gaps etc etc". Threads: DUO (2026-11-16 13:04), HICKSFIELD
  (2026-11-16 13:05, 2026-11-17 12:38), OST (2026-11-16 13:09),
  FORGE BROWSER (2026-11-16 14:38, 2026-11-17 12:41), SKULLPT
  (2026-11-16 18:30), ACR (2026-11-16 18:42, 2026-11-17 16:11),
  GUIFX (2026-11-17 07:22, UI only), STEMLAB (2026-11-17 07:23),
  QWKHND (2026-11-17 07:32), FYRN (2026-11-17 07:50), WINLINX
  (2026-11-16 13:43, 2026-11-17 07:33), DATAPACKR (2026-11-16
  14:33, 2026-11-17 14:34), GITDATA (2026-11-16 18:41), ARCHIVE
  FLIX (2026-11-16 13:09, 2026-11-17 12:39), SHELFLIFE
  (2026-11-16 13:06, 2026-11-17 15:56), SOLDAR (2026-11-17 07:21).
- Round-2 hold counts from the same window: HICKSFIELD Review 4
  found 46 of 47 fixes hold; FYRN's re-review found 28 fixes
  held; ACR's audit found all four v0.10 blocks genuinely fixed,
  checked live.
- ARCHIVE FLIX phone width: the round-1 review ran at desktop
  width and the phone gap was noted late; round 2 ran both widths
  from the start (desktop passed 12 of 20, phone all but one).
- Found in the seventh BNB delta scan (2026-11-17). The most
  repeated order of the delta after the update check.
