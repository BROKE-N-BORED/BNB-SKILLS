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

## The comparison step is mandatory

- A dogfood review must include, as a mandatory step, a
  comparison against (a) the stated reference or competitor for
  a clone or replacement project, and (b) the plan's full
  promised scope for any project. The comparison lists what is
  missing, not only what is broken.
- A review that only checks what shipped will catch symptoms and
  miss the gap list. The SOLDAR user audit checked what shipped
  but never compared against n8n, so it missed the full gap list.
  Joshua: "I asked tou to run it like a user and you sod you did
  amd I sont grt how yku didnt flag almthose gaps".
- Name the exact failure mode: scoping missing features out of
  the audit is the defect. The earlier SOLDAR audits explicitly
  classed triggers, credentials, and AI as "not yet due - not
  findings". A missing feature is a finding, whatever the plan
  says about when it is due.
- The full SOLDAR n8n audit (2026-11-18): 54 gaps, P0 6, P1 22,
  P2 13, P3 13 (audit 502 lines, task list 543 lines, in the
  soldar-review folder in the workspace). Top 10: Schedule
  Trigger plus scheduler; Webhook Trigger plus routes; Respond to
  Webhook; working Active; webhook auth; missed-schedule
  behaviour ("PC was off at 9am"); encrypted credentials store
  plus UI (keys today sit in workflow JSON and run history);
  OAuth2; HTTP node using stored credentials; Switch node.

## Check against his own stated ease bar

- The review checks function against the ease bar he stated for
  the project, not only against whether the function works. The
  STELLA profile-window usability failures (the child-easy test:
  "easy enough for [a] child to use") were never caught by the
  thread's own verification, because the review checked function,
  not the ease bar.

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

## What a good audit looks like: FYRN v0.5

- The FYRN v0.5 audit (2026-11-18) is the exemplar: 8 phases
  driven as a user, 84 screenshots, 18 findings (0 blockers,
  9 flaws, 6 inconveniences, 1 gap, 2 improvements), each with
  what-was-done, what-happened, what-should-happen, evidence,
  and likely cause, plus 6 non-findings each debunked with a
  minimal test. The shipped tree was never modified.
- The audit worker died after phase 1 and the audit was
  restarted from where it stopped, not from scratch: resume,
  do not redo.

## A graceful failure message is not a fix for a core function

- Do not ship a nicer error as the answer when the function
  itself is broken. FYRN v0.6 shipped LFM3 "failing plainly
  instead of blaming the file"; Joshua ordered the real fix
  instead: "Fix it the model shkuld load dude thats nkt
  something t just glaze over". The real fix was the engine
  bump to 0.3.37, built from source.

## A greyed-out button with no explanation reads as dead

- When a control is disabled by background state, the screen
  must say why. A greyed-out button with no explanation reads
  as a dead button. FYRN instance: the Unload button did
  nothing with no reason given. Fix in v0.7: the Models tab
  says a reply is in progress, and Unload tells you to wait
  instead of silently doing nothing.

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
- Eighth BNB delta scan (2026-11-18): the mandatory comparison
  step and the SOLDAR n8n audit (54 gaps), the ease-bar check
  (STELLA), the FYRN v0.5 audit as exemplar, the graceful
  failure message rule (FYRN LFM3), and the greyed-out button
  rule (FYRN Unload).
