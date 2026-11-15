# S81 — Destructive-action defaults: safe subset by default, dangerous subset needs opt-in

A delete, purge, or overwrite must default to the safe subset of items.
The dangerous subset is named, excluded by default, and only runs when
the user opts in explicitly and confirms a second time.

## When to use

- Any feature that deletes, purges, or overwrites user data — in any tool,
  on any platform.
- Any time a destructive action can touch two kinds of items: ones that
  are already safe (copied, backed up, transferred) and ones that are not.
- Do NOT use this to decide whether a destructive feature should exist at
  all — that is the user's call. This skill only governs how the feature
  behaves once it exists.

## Default to the safe subset

- Split the items into two named sets before the action runs: the safe
  subset (already copied, backed up, or transferred — destroying the
  original loses nothing) and the dangerous subset (not yet copied,
  backed up, or transferred — destroying the original loses the only
  copy).
- The default action covers the safe subset only. The user does not have
  to think, check, or uncheck anything to stay safe — doing nothing is
  the safe path.
- Name the dangerous subset in plain words in the UI, and say it is
  excluded: for example, "Items not yet transferred to the PC are NOT
  deleted." Never hide the exclusion in a tooltip or a log line.

## The dangerous subset needs opt-in plus a second confirmation

- Touching the dangerous subset requires two deliberate steps, not one:
  first an explicit opt-in (a checkbox the user ticks, unchecked by
  default), then a second confirmation (a separate confirm dialog that
  names what will be destroyed).
- The second confirmation must state the loss in plain words — what is
  being deleted and why it cannot be recovered — not just "Are you sure?"
- Never pre-tick the opt-in, never remember it across runs as the new
  default, and never bundle it with an unrelated setting. Each run starts
  safe again.

## Worked example

- The Android photo transfer tool's Delete fix: Delete defaults to
  on-PC items only — photos and videos already transferred, where
  deleting the phone copy loses nothing. Untransferred items are named
  and excluded from the default delete. Deleting untransferred items
  needs a checkbox plus a second confirmation, because that destroys the
  only copy.

## Where this comes from

- Fix Android Photo Transfer connection thread (8d9a5654, 2026-11-14
  EST): Joshua ordered "Build the Linux port" (~20:08 EST) and "Ship it
  to GitHub" (~21:17 EST), and the Delete safety fix landed in that
  build — Delete defaults to on-PC items only, untransferred items are
  named and excluded, and deleting them needs a checkbox plus a second
  confirmation. Release v0.1.0 went live 2026-11-14 21:21 EST.
- Found in the sixth BNB delta scan (2026-11-15). One in-window instance;
  the pattern is stated as written and should be re-checked against a
  second use before it is treated as proven.
