# S79 — Living user test suite: stable IDs, append-only results, and a compare loop

A definitive, updatable user test suite for a whole app — every test
with a stable ID that never gets reused, results saved per model per
machine in folders that never get overwritten, and a compare script
that diffs a later run against the baseline test by test.

## When to use

- The user wants a definitive test suite for an app on his PC,
  covering every function, that stays usable across versions and
  across models.
- The user wants to prove a fine-tune, a trim, or a new version is
  "no worse" than the baseline — the suite is what the proof runs
  on.
- Do NOT use this for a one-off drive of the app — a single pass
  with no stable IDs and no saved baseline is a check, not a
  suite. A one-off drive as a user is a different method: the
  dogfood review (see [dogfood-review](../dogfood-review/SKILL.md)).
  Do NOT reuse a retired test's ID: results stay comparable
  over time only because an ID always means the same test.

## Every test has a stable ID that never gets reused

- Give every test a stable ID, grouped by area (one group per
  screen, feature, or job). The ID is permanent: if a test is
  retired, its ID retires with it and is never handed to a new
  test, so results from any run can always be matched test by
  test against any earlier run.
- Keep a machine-readable copy of the suite alongside the human
  doc, so runs can be driven and scored by tooling instead of by
  hand. The human doc is for reading; the machine copy is for
  running.
- Pin known bugs as regression tests with their own pin IDs, so a
  fixed bug can never quietly come back: each pin re-checks one
  known failure on every run, and a pin that fails again is a
  regression, not a new bug.

## Save results append-only, per model per machine

- Save each run's results in its own folder, per model per machine,
  and never overwrite an earlier run. Old results are the baseline
  — overwriting them destroys the comparison.
- Use the same fixed test IDs and subjects every run, with content
  generated fresh from templates each run: the subjects stay the
  same, the content changes, so a retest measures learning instead
  of memorization. (v1.1.0, 2026-11-15: fresh-content templates
  prevent test contamination - see
  [trim-test-train-cycle](../trim-test-train-cycle/SKILL.md) for
  why fresh content matters across trim and train rounds.)
- Every test gets a real score: no "no scoring" cop-outs. Speed,
  like every other subject, gets a score of its own. (OST,
  2026-11-15 11:54-11:58: "Also why does it say no scoring for
  speed thats ricukousb" - "Give speed a real score too".)
- Run a test several times as one run and take the average with
  the spread, instead of scoring from a single run: one run is a
  sample, three runs are a score. (v1.1.0: repeat 3x, average +
  spread.)
- Resume an interrupted run where it left off; never restart a
  failed or interrupted test from scratch. The resume rule is
  Joshua's order, 2026-11-15 12:26: "Also there needs to be a way
  to resume the testing for ones that fill where it left off that
  is extremely important and helpful so im notneadting time
  starting fiskedntestsnover again !!!"
- Gather usage data on every run and roll it up into one file:
  decode speed, load time, time to first token, RAM, and tool calls
  made and dropped. Speed and resource use are part of the result,
  not an afterthought — a model that passes slower or hungrier has
  still changed.
- Run long live-model passes in small chunks: a full pass takes
  hours on CPU and the machine can restart without warning, so a
  pass that cannot survive a restart will never finish. Save each
  chunk's results before the next starts.
- Keep setup work out of the timings: model pulls and other setup
  run between batches, never inside a timed run, so pulls never
  skew the numbers.

## Compare every later run against the baseline, test by test

- A compare script diffs a later run against the baseline test by
  test and reports each test as improved, regressed, or unchanged,
  with speed and RAM deltas alongside. The verdict is per test, not
  one overall number — one overall number hides the regressions.
- A fine-tune or trim run is judged by the same compare: the fixed
  prompts, the same test IDs, the same baseline. That is how the
  suite feeds the trim-train work — the compare is the proof of
  "no worse" the trim mission rests on.
- When the compare shows a regression, the test ID names exactly
  what broke, and the append-only history shows when it last
  passed. Fix the regression, re-run, and compare again.

## Test together: the VM and his real PC, side by side

- Joint testing runs the same version, the same models, the same
  everything, on the VM and on his real PC at the same time, both
  testing as users together. Same version on both sides is the
  rule: a compare across different versions proves nothing.
  (Joshua-ordered, 2026-11-16 13:49: "Ok you can start whenever
  maybe we should use the exact same processes together you use
  the latest version of code forge and ill use the same version
  we both use the same models same everything so we can work this
  out together and test everything as a user..."; joint thread
  created 13:52.)
- The joint run's baseline is the built-in suite on both trees:
  B01 on the new tree, 2026-11-16 20:01, ran 2,983 tests with
  2,972 passing (99.63%), 11 real failures, all reproducing solo.
  The joint numbers are the baseline the live-model batches are
  judged against.

## Worked example

- Code Forge got a definitive user test suite in one session: v1.1.0,
  152 tests in 16 groups, every test with a stable ID that never gets
  reused, a machine-readable copy alongside the human doc, and 14
  regression pins for known bugs (twelve from the live-model test
  run the same day, two from earlier ruptures). Results save per
  model per machine in folders that never get overwritten, usage
  data rolls up into one file, and the compare script diffs a
  fine-tune run against the baseline test by test — improved,
  regressed, or unchanged, with speed and RAM deltas. v1.1.0 added
  fresh-content templates (same subjects, fresh content each run),
  repeat-3x scoring with average + spread, the resume rule, and
  the A12 installer-launcher test. Agent testing and a
  missing-subjects review were folded in the same day as
  confirmation the suite is a real full suite. (OST, 2026-11-15
  13:19-13:20: "You need to add agent testing toobman there is a
  lot of stuff missing" - "Please gonovwr what subjects are
  missing to test for".)
- The suite systematizes the live-model test that came before it:
  one of the user's own models driven through every function of
  Code Forge for real, 42 checks, 20 fails found — including the
  finding that Code mode could use no tools at all. The suite turns
  that one-off test into a repeatable loop that runs the same way
  on every model and every machine.

## Where this comes from

- Create Code Forge PC test suite thread (9b47e1cc, 2026-11-15
  ~11:10–11:26 EST): Joshua ordered a definitive, updatable user
  test suite for Code Forge on his PC, using his 11 models and
  feeding OST and STELLA. Built in the same session: v1.0.0, 151
  tests in 16 groups, stable IDs that never get reused, the
  machine-readable copy, per-model per-machine append-only result
  folders, the compare script, per-run usage data rolled up into
  one file, and 14 regression pins.
- The suite went to v1.1.0 the same day (2026-11-15 ~12:41), 152
  tests: fresh-content templates to prevent test contamination,
  repeat 3x with average + spread, the resume rule (Joshua's
  12:26 order), and the A12 installer-launcher test. The joint
  testing protocol (same version, same models, same everything,
  VM and his real PC side by side) came 2026-11-16 13:49, with
  the joint thread created 13:52.
- MAIN CHAT thread (c6ee49a6, 2026-11-14 ~20:16 EST): Joshua
  ordered the live-model test this suite systematizes — "You need
  to use one good model to test every function of code forge to
  ensure everything is worked correctly and to find gaps in
  performance and results and whatever else bugs come up please
  use a model that I have so I know its legit." The test ran on
  one of his own models, local only: 42 checks, 7 pass, 8 partial,
  20 fail, 7 untested.
- Found in the sixth BNB delta scan (2026-11-15). Two in-window
  instances: the live-model test and the suite built to repeat it.
