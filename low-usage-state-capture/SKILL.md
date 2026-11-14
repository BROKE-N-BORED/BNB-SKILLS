# S67 — Low-usage state capture: when the meter is nearly out, get every thread's task list into its own thread

## When to use

- Use this skill when the user says usage is nearly out (a low
  percentage left, a reset days away) and asks for the state to be
  captured — or when you can see the meter is about to run out and the
  work across many threads would otherwise be lost to the gap.
- Use it across all work threads, not one at a time: the point is the
  capture, every open list written down in its own thread in one pass.
- Do not use it as a reason to start new work. The capture produces
  lists only — no verification runs, no builds, no fixes to produce
  them. What a thread already knows is what goes in the list; what it
  does not know stays marked unknown.

## Send the same capture order to every work thread

- List the work threads: every thread with a task list, a build, a
  queue, or an open item. In the first run this was 53 threads (main
  chat, 2026-11-13 11:32).
- Skip the one-offs with no task list: recipes, errands, Q&A threads,
  the medical record, stopped studies, notes. Say which ones you
  skipped, in one line, so the user can add any back.
- Send the same brief to each one (see
  [cross-thread-dispatch](../cross-thread-dispatch/SKILL.md)): write
  out this thread's current task list in this thread, ordered highest
  priority to lowest. Mark each item done / open / blocked (and what
  blocks it). List only — do not start new work or verification runs
  to produce it. If the list is complete or nothing is open, say so in
  one line. Keep it short.
- Paused threads get the order too: writing the list is a one-way
  delivery, not a reopening (see
  [cross-thread-dispatch](../cross-thread-dispatch/SKILL.md)).
- Run the capture while usage is still available, not at the last
  minute: a thread that runs out mid-list leaves the worst of both
  worlds — a half-frozen list and no capacity to finish it.

## The list format (each thread writes its own)

- Ordered highest priority to lowest.
- Every item marked done, open, or blocked — and a blocked item
  names what blocks it (his decision, his PC, his account action,
  another thread's delivery).
- If the list is complete or nothing is open, say so in one line.
  A thread with nothing open gets one line, not a padded list.
- Standing items stay standing: an item that is open only in the
  sense of "waiting for him to speak" is listed as such, not
  dressed up as active work.

## Write the main chat's own list the same way

- The main chat writes its own list in the main chat, same shape:
  highest priority first, done / open / blocked, one line per item.
- The main-chat list covers what lives nowhere else: money, housing,
  account deadlines, cross-thread items waiting on the user.

## Report once, briefly

- Report once when the orders are sent: how many threads got the
  order, which one-offs were skipped, and the main chat's own list.
- Do not chase the threads for their lists. Each thread writes its
  list in its own thread; the lists are there when the user comes back
  to them, and the next session starts from written state instead of
  from memory.
- If a thread reports its list is complete with nothing open, that is
  a result, not a failure — record it and move on.

## After the capture

- The threads go quiet until he reopens them. Nothing goes in or
  out in the meantime — no follow-ups, no nudges, no background
  work landing in a paused thread.
- On return, the lists are the resume point: the un-stall sweep
  (see [un-stall-sweep](../un-stall-sweep/SKILL.md)) picks up
  where these lists left off. Capture and un-stall are a pair —
  this skill freezes state on the way out, S62 thaws it on the
  way back in.

## Where this comes from

- Main chat, 2026-11-13 11:32 EST: Joshua said "Ok we have 10% usage
  left twll every chat thread to write out there currenr task lists
  ordered from highest priority to lowest priority please", and the
  order went to all 53 work threads with the list-only instruction.
  The BNB repos thread's capture (11:34) shows the shape: Open items
  (standing management, V1 tool gaps, BNB-RESEARCH suggestion),
  Blocked items with the blocker named (TOOLS audit unpasted, trim
  decision, billing lock, Victor preset), Done items. The audit thread
  (11:34) reported "Task list complete — all 29 repos audited and
  delivered, nothing open or blocked." The main chat wrote its own
  12-item list the same turn.
- Five more instances in the same sweep, all in the same format:
  Flea bomb prep checklist (11:34:58 — flea round 2 ~Nov 26 open,
  Nov 12 fogging done); Account security (11:34:43 — Mint PC login
  blocked on age verification, nothing open); Report caregiver
  neglect in Delaware (11:34:43 — Section 10 addendum and
  submit-the-report both blocked on his call); Winterize a sealed
  room in Meridian (11:34:58 — measurement-dependent rebuild blocked
  on his numbers, guide itself done); Tavus connector (11:34:43 —
  PAL-purpose pick blocked on him, Connectors-launch check his open
  action).
- 2026-11-13 ~11:58–12:01 EST: Joshua then paused each thread
  himself — "Pause this chat thread untill further notice nothing
  in or out untill i reopen it no need to reply" — and each thread
  answered "Paused." and went quiet. The capture is what makes the
  pause safe: nothing was mid-flight with its state only in a
  worker's head.
- Distinct from [un-stall-sweep](../un-stall-sweep/SKILL.md): that
  skill runs when the user RETURNS and retries stuck pushes; this one
  runs when the user is about to LEAVE (usage nearly out) and captures
  state. Different trigger, different action, no overlap.
- Found in the third BNB delta scan (2026-11-13, evening window).

## Available connectors

- None. This skill is lists in threads; no external service is
  involved.

## Alternatives for better results

- Offer to fold the captured lists into the next delta scan's input,
  so the scan starts from written state instead of re-reading every
  thread cold.
- Offer to pause the heavy scheduled sweeps until the reset, keeping
  the inbox scans and briefings running, when the remaining usage has
  to last days.
