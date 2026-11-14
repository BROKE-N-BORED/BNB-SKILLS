# S69 — Restart recovery

When a runtime restart kills a builder mid-task, the builder is dead
even if its status still says otherwise — and a resume that produces
nothing is dead too. Recover by checking output, not status; dispatch a
fresh finisher onto the orphaned artifact; verify the artifact yourself;
tell the user plainly.

## When to use

- A builder (or auditor, or any long-running worker) was running when a
  runtime restart happened, and the task is now silent.
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
