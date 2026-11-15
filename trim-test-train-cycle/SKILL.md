# S77 — Trim-test-train cycle: shrink a model on a small PC without losing its one job

Shrink a model on an 8 GB PC while keeping it good at its one job —
by running a fixed sequence where OST measures and STELLA acts, with
a results step passing between them every time.

## When to use

- The user wants a model trimmed, quantized, distilled, or fine-tuned
  to run on his own PC.
- The user wants a smaller model trained up for one specific job
  instead of a big model forced onto small hardware.
- Do NOT use this to pick which model to start from — grading models
  against the machine is the pick step that comes before the cycle.
  Do NOT let STELLA act without an OST test on both sides of it: an
  action with no measurement before and after cannot prove it did
  no harm.

## The sequence: OST measures, STELLA acts, results pass between them

- The cycle is one fixed sequence, in this exact order:

  OST test > results > STELLA trim > OST test > results >
  STELLA train > OST test > results

- OST is the measurer. It runs the test items and produces the
  results — pass/fail per job, plus peak RAM and time per step.
  STELLA is the actor. It trims and trains, and it works from the
  results OST just produced — never from a guess about what needs
  cutting or teaching.
- The results step is what passes between them. Every STELLA action
  is both preceded and followed by an OST test with results in
  between: the test before shows the starting point, the test after
  shows what the action did. No STELLA step runs without results
  on both sides.
- The cycle repeats — the user named it with "repeat" at the end —
  each round running the same sequence above.
- This sequence is the gist for now. More detail lands when Joshua
  gives it; nothing here is padded out beyond what he stated.

## Define "good" before the first trim

- Before the first STELLA trim, write down what "good" means for
  this model's one job: a small set of real jobs with pass/fail
  answers. Real jobs, not benchmarks — the actual tasks the model
  will do in the app it serves.
- Agree the no-regression line up front, with the user: how much
  worse is allowed on the baseline set, if any. The trim mission
  rests on proving "no worse", and that proof does not exist until
  the line is agreed and the baseline is measured.
- Test all candidate models first, on the same baseline set, before
  trimming any of them. The baseline run is what every later round
  is compared against — and it can also kill a candidate outright,
  for example a model trained to refuse the very job it would do.
- Use the SAME test items before and after every STELLA action, not
  a fresh set. Same items on both sides is what makes "no worse" a
  provable claim instead of a feeling. If a run regresses past the
  agreed line, the action is rejected, not shipped.

## Prefer the smaller model that is already close

- When the choice is between shrinking a big model and training a
  smaller one, prefer the smaller model that is already trained for
  some of what is needed. Trimming and training a big model on a
  small PC costs more time and RAM than training a small model
  that starts most of the way there.
- Check a model's training constraints before picking it: a model
  trained to never do signups or submit forms cannot do a job that
  is signups and forms, however good its scores look.
- Prove the mechanics with a tiny run first: a small dataset, peak
  RAM and time per step measured, and the export path back to the
  model runner checked — before committing to the big run.
- Leave the original model untouched at every step, so any round
  can always be re-run from the same starting point.

## Worked example

- ShelfLife needed a model to do the human work of listing items:
  signups, listing forms, managing listings. The 7B candidate was
  out on three counts, and the killer one was new: it was trained
  to never do signups or submit forms, so it literally could not do
  ShelfLife's job. The pick was the 4B model, already close to the
  job, to be trimmed and trained instead of forcing the big model
  onto the PC.
- The cycle was named by the user in the same thread — Test, then
  Trim, then Test, then Train, then repeat — with "good" defined
  before the first trim as a small set of real ShelfLife jobs with
  pass/fail. Joshua then fixed the exact sequence: OST tests and
  produces results, STELLA trims from those results, OST tests
  again, STELLA trains from those results, OST tests again.
- In the parallel model-testing thread, the proof rule was stated
  the same way: the same test items before and after the trim, and
  the no-regression line agreed up front. A requant there proved
  the shape: 1.04 GB down to 718 MB, loads and answers, original
  untouched.

## Where this comes from

- SHELFLIFE DEV thread (2b9eeac3, 2026-11-15 ~10:07–10:11 EST):
  Joshua named the cycle — "Test > Trim > Test > Train > repeat"
  — and asked the smaller-model question: "start with a smaller
  model thats already trained for some of what we need and then
  train it instead of doing all that to such a big model on my
  pc?" The baseline-first rule came from the same turns: "Define
  'good' before the first trim. A small set of real ShelfLife jobs
  with pass/fail." The 4B-over-7B pick and the 7B's signup refusal
  are from the same thread. Joshua's correction fixing the exact
  sequence — OST test, results, STELLA trim, OST test, results,
  STELLA train, OST test, results — came after the first draft of
  this skill and is written in as the sequence above.
- Arlo-OST model testing thread (5dd38ce4, 2026-11-14 22:05–23:20
  EST): "test them all first" before trimming; "Same test items
  before and after the trim, and you agree the no-regression line
  up front"; the requant proof (1.04 GB to 718 MB, original
  untouched) and the tiny-probe run (small dataset, RAM and time
  per step measured, export path checked).
- STELLA Development thread (2d7b2739, 2026-11-15 ~00:27 EST):
  "Everything about trimming rests on being able to prove 'no
  worse,' and right now that proof doesn't exist in the harness"
  — the gap this cycle's baseline-first rule closes.
- Found in the sixth BNB delta scan (2026-11-15). Three in-window
  instances, one user-named; the cycle is the workflow STELLA's
  trim mission runs on. The sequence above is the gist as Joshua
  stated it; further detail lands when he gives it.
