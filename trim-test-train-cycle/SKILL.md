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
- The analyzer role sits between OST results and STELLA actions:
  the OST report-card analyzer reviews the report cards OST
  produces and configures exactly what needs trimming and
  training, and what data packs or data STELLA needs to do that
  with. Joshua defined the role 2026-11-16 ~18:21; the lock-in
  as a standing job was unconfirmed at the Delta 7 close, so it
  is noted here as pending, not as settled.
- The cycle repeats — the user named it with "repeat" at the end —
  each round running the same sequence above.
- The results step must separate grader bugs from model failures
  before any trim or train decision. First classify each failure
  as a grader bug or a real model miss; a trim or train step
  taken on grader bugs wastes the cycle. Worked example: the
  LFM3 card (2026-11-18 16:12-17:15) showed 23 failures, 22 of
  which were OST bugs (13 empty-with-tokens, 2 exact
  long-context codes with a different hyphen, 3 sensible
  planning answers failed on exact-phrase matching, role tests
  wanted magic words); the real score was 87.7, best of three
  models, not second; the one real miss was long context (the
  model could not find a meeting password in 8k of filler).
- Empty answers must never count as passes. On the same card,
  Refusal 100% was unmeasured because all 5 answers were empty
  and the checker passed them.
- Conditional-train rule, from the same analysis: only train if
  the v21 re-run still shows long context under 60% with no lost
  answers, then a small LoRA on long-context retrieval,
  Forge-style data, never OST test prompts.
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

## Fresh content per round, same items within a round

- Same items on both sides of ONE action; fresh content when the
  cycle repeats to the next round. The two rules serve different
  ends and both stand: same items make "no worse" provable for
  one action, and fresh content per round keeps the cycle honest
  across rounds.
- The reason, stated explicitly: if the same test content is
  reused across trim and train rounds, the model can learn to
  answer or complete those tasks by mimicking instead of
  actually learning - it gets desensitized to the tests instead
  of learning the job. Fresh content every run is what keeps a
  retest measuring learning instead of memorization. (OST,
  2026-11-15 12:23, Joshua's question: "if I am testing a model
  right and then I trim it or train it on something and then test
  it aga8n couldn't potentially just learn how to answer or
  complete those tasks by mimik8ng instead of actually whatbinmean
  is whoudthey ve dessentised to the tests instead of actually
  learning etc etc". The design answers it with fresh-content
  templates in the suite - see
  [living-user-test-suite](../living-user-test-suite/SKILL.md).)
- Scores are only comparable within one grader version: OST v21
  fixed 13 grader bugs, so pre-v21 scores are NOT comparable with
  v21 scores. Empty answers now fail instead of being excluded,
  and planning scores partial credit. The v21 re-grade of five
  stored result sets came out lower than the detector-corrected
  numbers by design: qwen3-vl 87.2, bonsai-uncensored 85.0,
  qwen-coder 80.5, lfm3 78.2, bonsai-2:4b 75.7. Never compare a
  pre-v21 score against a v21 score as if they measured the same
  thing.

## Result-file rule and thin-evidence rule (Delta 8)

- Result-file rule: after every pair, verify a result file was
  written before marking the pair done; never trust exit 0
  alone. The OST driver trusted exit code 0 and never checked a
  result file was written; six qwen3.5:2b templates vanished
  silently this way (server killed, OST printed the failure,
  exited 0, `run_pair()` marked the pairs done). Done-pairs.txt
  is not proof a pair ran. The defect is the 13th item for the
  v21 re-run. (Arlo-OST, 2026-11-18 00:17; sleep-05,
  2026-11-18 ~03:20.)
- Thin-evidence rule: a corrected score resting on fewer than
  about half the original tasks must carry its kept-task count
  next to the score wherever the score is ranked or headlined.
  Corrected 100.0 scores rest on thin evidence (qwen3.5:2b: 8
  kept tasks; qwen3.5:4b: 20 questions). The cards disclose
  this, but ranking by corrected score still puts the thinnest
  first. (sleep-05, 2026-11-18 ~03:20.)
- Benchmark completion, 2026-11-18 12:09: all 11 models,
  209/209 tests. Scores (official / corrected): qwen3-vl
  80.0/85.3, granite 79.7/87.9, bonsai-uncensored 73.1/85.8,
  phi4-mini 71.7/83.7, lfm3 70.0/87.7, qwen-coder 65.3/81.5,
  minicpm5 62.0/70.4, bonsai-2:4b 51.3/97.7, dolphin 49.7/66.9,
  qwen3.5:4b 35.0/100.0, qwen3.5:2b 32.0/100.0. Speeds are not
  comparable across models (different machine load per run).

## Bench of specialists + autoswitch (framing, not a project)

- Joshua, 2026-11-18 20:51: "I want to have a bunch of models but trimmed, trained, and fine tuned and them have it be able to autoswitch and use those models for what I jeed, does this make sense?"
- The shape: a bench of trimmed experts, one per Forge seat,
  not one Wonder-class model. Per-seat loop: pick one job, then
  the smallest base that can almost do it, gather 50-200
  examples, hold 10-20 back for testing, LoRA train in STELLA
  (checkpoints; an overnight-type job on his PC; 2B+ wants a
  free cloud GPU like Colab or Kaggle), merge, shrink to GGUF,
  quantize Q4_K_M, load into Ollama, test before vs after on
  the held-back set, plug into Forge autoswitch, then repeat
  for the next seat.
- His personal role: pick the job, check the examples, judge
  before-and-after; STELLA and Forge do the heavy lifting, all
  by clicking.
- Status: brainstorm only, no build ordered. Record this as
  the framing, not a project.

## The Fara loop is not this cycle

- Do not confuse the Fara loop with the OST/STELLA sequence
  above. In the Fara loop, the trim step is a quant download -
  bartowski already ships every quant - not STELLA compute. The
  Fara loop downloads a smaller ready-made quant; this cycle has
  OST measure and STELLA act, with results passing between them.
  (Delta 6 near-miss, pre-window: the Fara Phase 1 completion
  report and the "Test > Trim > Test > Train > repeat" wording
  landed 2026-11-15 ~10:47-11:38, inside Delta 6's window but
  after Delta 6's scan ran, so Delta 6 never recorded them.)

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
