# S66 — Atomic file saves: temp file first, rename last

## When to use

- Use this skill for every file an app writes that the user
  depends on: saved settings, provider keys, batch files,
  session state, transcripts. If a failure mid-save could leave
  a half-written file, the save must be atomic.
- Use it when a review, an audit, or a crash report names a
  corrupt or half-written file — the fix is this pattern, not a
  better error message after the damage.

## Write temp, then rename

- Write the new content to a temp file in the SAME directory as
  the target (same filesystem, so the rename is atomic), then
  replace the target with one atomic rename (`os.replace`).
- If the write fails partway, the previous file stays intact —
  the temp file is discarded and the user keeps the last good
  version. Say plainly that the save failed; never leave a
  half-written target in place.
- For a file holding secrets, set the temp file's permissions
  BEFORE any secret bytes are written (0600), then rename — the
  secrets never sit in a world-readable file, even briefly.
- Keep the save interface unchanged: the caller still calls the
  same save function. Atomicity is inside the write path, not a
  new user-visible step.

## Prove it

- Test the failure path, not just the happy path: fail the write
  mid-save (a mock, a full disk, a killed process) and confirm
  the previous file is byte-identical afterwards.
- A corrupt existing file still gets a plain error naming the
  file instead of a crash — atomic saves prevent new corruption;
  they do not repair a file corrupted before the pattern landed.

## Where this comes from

- DUO v0.18 (thread 284b2ad4, 2026-11-13 ~08:20 EST): every file
  DUO writes now saves to a temp file first and only replaces
  the old one once the write is complete; a failed save leaves
  the previous file intact and says plainly it failed.
- Pixel Forge v0.15 (thread b2e2291b, 2026-11-12 ~21:40 EST):
  saves are atomic so a failure mid-save cannot leave a
  half-written file, shipped alongside a plain error for a
  corrupt batch.json naming the file instead of crashing.
- OLLAMA SYSTEM TEST v6, task P0 #2 (thread 662fb3aa,
  2026-11-12 ~21:07 EST): providers.json is written to a temp
  file chmodded 0600 before any key bytes, then atomically
  renamed; shipped inside the cumulative v9 (2026-11-13).
- Found in the second BNB delta scan (2026-11-13).
