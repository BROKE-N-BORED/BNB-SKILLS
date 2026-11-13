# S62 — Un-stall sweep: when the user returns, find the stuck pushes and retry them

## When to use

- Use this skill when the user comes back after being away, or asks
  to check that no thread is stalled — the moment he is at his phone
  again is when timed-out approval cards can be retried.
- Use it across all active build threads, not one thread at a time:
  the point is the sweep, finding every verified-but-unshipped build
  in one pass.
- Do not use it as a reason to re-push something that already
  shipped. Verify live state first (below) — a sweep that retries a
  shipped push reports a stall that never existed.

## Sweep every active build thread

- List the active build threads and check each one's newest state:
  what is the latest verified build, and is it pushed with a live
  Release, or sitting behind an approval card that timed out?
- An approval card expires after 30 minutes. A push attempted while
  he was away is almost certainly an expired card, not a failed
  build — the build is still verified and waiting.
- Collect the genuinely stuck pushes into one list before retrying
  anything, so the user gets one short report, not a drip of
  single-thread updates.

## Verify live state before retrying

- For each candidate stuck push, check the live state first: the
  repo's head commit and the Release page. A push can land between
  the sweep's check and the retry, or the thread's own record can
  be stale.
- If the commit is live and the Release is up, the item was never
  stalled — close it out, report it as already shipped, and do not
  retry. A false stall in the report costs the user's trust more
  than a missed stall costs time.
- Only the pushes that are genuinely missing from the live repo go
  on the retry list.

## Retry the stuck pushes, then report once

- Retry each stuck push in its owning thread (see
  [cross-thread-dispatch](../cross-thread-dispatch/SKILL.md)): the
  owning thread runs the push, the card pops, he taps, the Release
  follows. Push + Release only, no zip emails (see
  [ship-pipeline](../ship-pipeline/SKILL.md)).
- Do NOT pre-warn him about each card before it pops. The cards
  happen automatically; warnings about them are stalling (see
  [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md)).
- Report once, briefly: which pushes were retried and landed, which
  were already shipped (with the live Release link), and what is
  still genuinely blocked and why. A build chain can run ahead of
  the ship chain — several versions may be verified and staged
  behind one stuck push, and they ship in order once it lands.

## Where this comes from

- Main chat, 2026-11-13 ~09:47 EST: Joshua said "Make sure none of
  the threads are stalled please", and the sweep found four stuck
  pushes being retried now that he was at his phone — Pixel Forge
  v0.17–v0.20, Forge Browser v0.2, BNB-ROLES, and Ollama Test v9.
- BNB repos thread (089d9759), 2026-11-13 ~09:49–09:52: the ROLES
  audit-fix push, whose approval card had timed out twice overnight
  (~22:32 and ~23:33 on 2026-11-12), was retried on the un-stall
  order and landed as commit 815c27d3.
- OLLAMA SYSTEM TEST thread (662fb3aa), 2026-11-13 ~09:50: the
  sweep listed v9 as stalled, but the push had gone through at
  07:52 that morning after he tapped the card — the thread
  re-verified the Release page live and corrected the sweep. This
  is the false positive the live-state check exists to prevent.
- PIXEL FORGE DEVELOPMENT thread (b2e2291b), 2026-11-13 08:08–
  10:03: v0.17–v0.30 shipped in a chain once the stuck push moved,
  with v0.47/v0.48 already verified and v0.49 building behind
  them — the build chain running ahead of the ship chain.
- Found in the second BNB delta scan (2026-11-13).

## Available connectors

- [GitHub](../CONNECTORS.md) for checking live repo heads and
  Release pages before retrying a push.

## Alternatives for better results

- Offer to run the sweep as a standing check whenever he returns
  after a long absence, rather than waiting for him to ask — the
  cards expire on their own schedule, not his.
