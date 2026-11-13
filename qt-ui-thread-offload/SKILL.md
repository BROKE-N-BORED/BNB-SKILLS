# Qt UI-thread offload (worker thread + debounce)

Move blocking work off the Qt UI thread so the window never freezes,
and debounce rapid control changes so one user gesture does one job.
Use this skill whenever a review or a user report names a UI freeze,
a lock-up on import/load/generate, or a control that re-runs expensive
work on every keystroke or slider tick.

## Find the freeze first

- Time the slow path instead of guessing: measure the blocking call on
  realistic input (a 1024×1024 photo, a 4000×3000 photo, a long video)
  and record the before numbers. A freeze the user reports is real
  until measured otherwise.
- Name the exact call that blocks: the pixelize core, a texture load,
  a video extraction, a capture poll — the worker wraps that call, not
  the whole tab.

## Cap the work before you move it

- If the work scales with input size, cap the input first: downscale
  to a fixed maximum dimension on the longest side, keeping the aspect
  ratio, before the expensive core runs. Pick the cap from what the
  feature actually needs (512 px on the longest side was the cap for
  texture import — enough for the pixelize core, cheap to process).
- Keep the capped path byte-identical to the old path for inputs at or
  under the cap, so existing behaviour and tests do not change.
- Tell the user when a cap bit: the info line and the status bar both
  state the downscale (e.g. "downscaled from 1024 x 1024 to 512 x
  512"), so a smaller result is never a silent surprise.

## Move the work to a worker thread

- Put the blocking call in a QThread worker, following the app's
  existing worker pattern (one worker class per job; the prompt worker
  is the usual template). The UI thread only starts the worker, shows
  progress, and receives the result.
- Guard against stale signals: if the user starts a second job while
  the first is still running, the first job's result must not
  overwrite the second job's state. Drop or ignore results from a
  superseded job.
- Keep the parts that must stay synchronous on the UI thread (a skin
  load that is already fast, a small lookup) — do not move work that
  does not block.
- Show progress and offer cancel where the job can take seconds: a
  progress indicator plus a cancel path, not a silent wait.

## Debounce rapid control changes

- When a control (slider, spinner, text field) re-runs expensive work
  on every change, debounce it: wait ~300 ms after the last change
  before running, so one drag does one job instead of dozens.
- Debounce is per-control and per-job: a debounced control must still
  run immediately when the user commits (Enter, release, Apply).

## Verify the offload

- Re-run the same measurements after the change and report before/after
  timings: a 1024×1024 texture import went from a 21.8 s UI freeze to
  a 1.62 s background import (1920×1080: 33 s → 1.00 s; 4000×3000:
  208.8 s → 0.70 s), with the window responsive throughout.
- Prove the results are unchanged: at/under-cap inputs produce
  byte-identical output to the old synchronous path; run the full
  suite from a fresh unzip (the texture-cap change shipped with
  359/359 green, 5 of them new).
- Check the worker returns promptly: the load call itself should
  return in well under a second once the work is async (0.04–0.10 s
  measured), and the UI must stay usable while the job runs.

## Where this comes from

- Pixel Forge v0.8 (2026-11-12): texture import capped at 512 px and
  moved to a TextureWorker (QThread, PromptWorker pattern, stale-signal
  guards), verified from a fresh unzip and shipped as v0.8. The same
  pattern was then applied to the Video tab (extraction + re-pixelize
  off the UI thread, ~300 ms debounce) in v0.9, and the MIMIK v0.2
  review named the same fix for its GUI (worker threads +
  progress/cancel) as a ranked improvement. Recorded as a delta-scan
  finding, 2026-11-12.

## Available connectors

- Use `muse.connector_search` to find other connectors and
  `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP
  server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md),
  or build a custom connector.

## Alternatives for better results

- When the blocking call is a poll that re-fetches everything every
  few seconds, fix the poll first (incremental fetch, cache the
  results) — a worker around a wasteful poll still wastes the work.
- Offer the cap as a user-visible setting only if the user asks for
  it; the default cap ships fixed.
