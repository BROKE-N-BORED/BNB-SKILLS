# S69 — Restart recovery

When a runtime restart kills a builder mid-task, the builder is dead
even if its status still says otherwise — and a resume that produces
nothing is dead too. Recover by checking output, not status; dispatch a
fresh finisher onto the orphaned artifact; verify the artifact yourself;
tell the user plainly.

## When to use

- A builder (or auditor, or any long-running worker) was running when a
  runtime restart happened, and the task is now silent.
- A builder errored out mid-task (coordinator_completion with status
  errored, not a restart) — the same recovery applies: check what it
  changed before starting it again. (Forge Browser v0.9, 2026-11-13
  23:01–23:03: the first builder errored ~10 minutes in with two
  failed execs and no work done; the copy was untouched, a fresh
  builder was dispatched, and the user got a plain flag.)
- A resumed worker has been running but has produced no output for a
  long stretch.
- A user asks why nothing is happening ("y r u not working?") — that
  question is itself the signal the recovery has already failed once.

## How to tell a builder is dead

- Judge liveness by OUTPUT, not by status. A builder that is "running"
  but has written nothing, reported nothing, and produced no artifact
  for an hour is dead. Stella v0.3's builder was killed at 10:03 by a
  restart, left a built zip (381 KB, 53 files) with no verification and
  no report, and sat silent until the user asked "y r u not working?" at
  10:56 — nearly an hour of dead time nobody noticed.
- A resume that produces nothing is dead. Do NOT resume twice. The
  Stella v0.3 resume "didn't take" — it wrote nothing after the restart —
  and the fix was a fresh finisher, not a second resume. Same for the
  Stella audit #7 resume (wrote nothing after 09:40) and the MIMIK v0.3
  restart (the resume "didn't take" at 10:06; a fresh builder was
  dispatched at item 16, items 1–15 safe).
- Check the artifact first, before dispatching anyone. The dead
  builder may have left usable work: the Stella v0.3 zip existed and was
  the right size, but nobody had verified it. The fresh finisher's job
  starts with verifying the orphaned artifact, not rebuilding it.

## The recovery

- Dispatch a fresh finisher with a bounded brief: verify the artifact
  the dead builder left (or pick up from the last verified item), finish
  the remaining steps, and report. The Stella v0.3 finisher verified the
  zip, ran the checks, and shipped at 11:12 — sixteen minutes after the
  user asked what was happening.
- Tell the user plainly, in one sentence, what happened: the restart
  killed the builder, the resume didn't take, a fresh finisher is on it.
  Do not dress the dead time up as process, and do not blame the user
  for asking.
- Record the restart as a known failure mode in the thread's notes: the
  builder was killed by a restart, not by its own error. The next
  restart will do the same thing to the next builder — the recovery
  pattern is the fix, not a one-off.
- After recovery, check whether anything else died in the same restart.
  A restart kills every running worker at once; the one the user noticed
  is rarely the only one. (In the 10:03 restart, the Stella v0.3 builder,
  the Stella audit #7 resume, and the MIMIK v0.3 builder all died.)

## More recovery shapes (Delta 6, 2026-11-14–15)

- Validate a watchdog verdict is fresh before trusting it: a verdict
  must be timestamped after the last restart, not stale from before
  it. (CODE FORGE battery waiter, thread 94792a18, overnight
  2026-11-14: the waiter died in a VM restart and its stale verdict
  was re-read as if fresh.)
- Builder-hit-limit finisher: when a builder dies mid-task, check the
  on-disk work first — a near-complete tree gets finished by a
  finisher, not rebuilt. (HICKSFIELD v0.1, thread c3656ead,
  2026-11-14 00:37: the builder stopped ~5h in, right near the end;
  the finisher checked the on-disk work itself, finished it, and
  verified v0.1 at 01:20.)
- Recover dead work from the working copy yourself: the copy may hold
  usable work even with no report. (GUIFX elision fix, thread
  dfc78d3f, 2026-11-14: the builder "died mid-flight, probably the VM
  restart, no report. I pulled the work out of the copy myself.")
- Orphaned-job pickup: re-verify it yourself — checkers + probe +
  eyeball — do not redo it. (Reblend V4 die, thread 1c1928e9,
  2026-11-14: "picked up the orphaned job, verified it, and delivered
  it... No redo needed. I re-ran every checker and the probe myself:
  zero buried samples out of 282,240, all checks green. And I looked
  at the renders with my own eyes.")
- Empty-failure retry: when an attempt fails with nothing changed,
  retry fresh — the empty failure is the signal, not the work.
  (ARCHIVEFLIX, thread e5374055, twice; SHELFLIFE, thread 2b9eeac3,
  twice — in each case the retry worked.)
- Re-run clean under contention: do not trust a failure set from a
  run under shared-resource contention. (STELLA, thread 2d7b2739,
  2026-11-14: the first suite run showed 93 failures, but that was
  the shared temp space filling up from all the other threads
  building at once, not the code. Re-ran clean.)
- Checkpoint per unit of work, so a restart loses at most one unit.
  (Arlo–OST model testing, thread 5dd38ce4, 2026-11-14: 11 models x
  108 prompts, each model's results saved before the next starts.)
- Run a hours-long pass in small restart-resilient chunks. (Code
  Forge PC test suite, thread 9b47e1cc, 2026-11-15: "a full pass
  takes hours on CPU and this VM restarts without warning", so
  live-model batches run in small chunks.)
- Clean up dead copies left by a failed build: a failed build that
  leaves an empty copy behind, plus a rebuild's second copy, leaves
  the user staring at two copies unable to tell which works.
  (SHELFLIFE, thread 2b9eeac3, 2026-11-14.)
- Reword and retry after a block, rather than repeating the blocked
  wording. (ARCHIVEFLIX, thread e5374055, 2026-11-14: "I've sent it
  through again with the request worded differently.")

## More recovery shapes (Delta 7, 2026-11-15-17)

- Coordinators die in VM restarts, in every shape: the Reblend
  Uahztee v6 coordinator died before writing its final reports,
  and its replacement died the same way 13 minutes later
  (thread 1c1928e9, 2026-11-16 ~19:33-20:50); the Code Forge PC
  test suite lost 2 full runs of about 2 hours each with no
  summary (thread 9b47e1cc); the SOLDAR helper route failed twice
  on startup (thread 6b040c11); the Android updater worker died
  partway through (thread 8d9a5654); the QWKHND first builder was
  lost before it started (thread a7e37553); the CODE FORGE DEV
  suite driver died in a restart at about 20:00 on 2026-11-16
  (thread 94792a18). All of these were runtime failures, not
  build failures.
- The pattern that works is parent-picks-up-and-finishes: when
  the coordinator is dead, the parent checks the on-disk work,
  finishes what is left, verifies it, and delivers it - instead
  of dispatching another coordinator into the same restart.
  (Reblend v6: "V6 is done, verified, and delivered to the
  Yahtzee thread", 2026-11-16 ~20:50.)
- Work must be resumable from saved state, not from a dead
  worker's memory: a builder that dies with its progress only in
  its own head leaves nothing to pick up. Save progress to disk
  as the work goes - chunks banked, results written, artifacts
  in place - so a fresh finisher can start from the last saved
  state. (Code Forge PC test suite: 27 small chunks, 18 of 26
  survived a restart, 701 tests banked - the chunked run is what
  survived where two full runs died.)
- Writes can be blocked without a restart: the machine can stop
  letting programs write files, and the block can clear on its
  own hours later. A write failure is not proof the work is
  wrong - check whether writes are blocked, wait for the
  recovery, and resume. (OST, thread 662fb3aa, 2026-11-15 ~22:22:
  "The machine I build on has stopped letting programs write
  files"; recovery caught at 06:12 on 2026-11-16.)
- Resume, do not restart: when a build is interrupted, restart
  from where it got to instead of starting over. (DUO launcher
  build glitch, 2026-11-16; PIXEL FORGE v0.75 builder, 2026-11-15:
  restarted from where it left off after a mid-suite hiccup.)

## What this is not

- This is not [un-stall-sweep](../un-stall-sweep/SKILL.md): that skill
  recovers stuck PUSHES by checking live state and retrying. This skill
  recovers dead BUILDERS by checking output and dispatching a fresh
  worker. Different trigger (runtime restart vs user return), different
  object (a worker vs a push), different remedy (fresh finisher vs
  retry).
- Do not "resume" a builder that has been silent for an hour and then
  wait another hour to see if it works. The resume is the thing that
  failed; the fresh finisher is the recovery.

## Where this comes from

- STELLA ✨ Development thread (2d7b2739), 2026-11-13 10:03–11:12 EST:
  the v0.3 builder was killed by a restart at 10:03, leaving a built
  zip (381 KB, 53 files) with no verification and no report; the user
  asked "y r u not working?" at 10:56; the resume didn't take; a fresh
  finisher was dispatched, verified the zip, and shipped Release v0.3
  at 11:12. The audit #7 resume wrote nothing after 09:40 and was
  replaced by a fresh auditor the same morning.
- MIMIK Dev thread (d22a66c0), 2026-11-13 ~10:06 EST: the v0.3 restart
  "didn't take" — a fresh builder was dispatched at item 16, items 1–15
  safe, and the build shipped at 11:35.
- FORGE BROWSER DEV thread (611e974d), 2026-11-13 23:01–23:03 EST: the
  v0.9 builder errored ~10 minutes in (two failed execs, no work
  done, copy untouched) — not a restart. Same recovery: the copy was
  checked first, a fresh builder was dispatched, and the user got a
  plain flag ("the first builder died about ten minutes in without
  doing any work").
