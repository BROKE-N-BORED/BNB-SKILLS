# S80 — Sweep-recheck-first: re-verify the last sweep before running the next

Before each sweep or audit pass, re-verify every prior finding
against live sources and strike or update anything filled or
partially filled — never carry stale findings forward into the
next round.

## When to use

- The user runs a recurring sweep or audit: gap hunts, stock
  sweeps, repo audits, delta scans — any scan that runs more than
  once over the same ground.
- A new sweep is about to start and a previous sweep's findings
  still stand on the record.
- Do NOT use this for a first-ever sweep — there is nothing to
  re-check yet. Do NOT skip the re-check because the last sweep
  was recent: a tool can launch, a version can jump, or a finding
  can turn out to have been a miss, in a single day.

## Re-verify every prior finding against live sources

- Before the new sweep starts, go back through every finding from
  the previous sweep and check it live: the web, GitHub, version
  numbers, release pages. A re-read of the old sweep file is not
  a re-check — the check has to touch the live source, because
  the world moved since the last sweep.
- Mark each finding STILL OPEN, PARTIALLY FILLED, or FILLED. A
  finding is FILLED only when something real now does the job;
  a partial match — the wrong scope, the wrong platform, an
  untested claim — is PARTIALLY FILLED, not filled, and the gap
  that remains is written down with it.
- Strike or update the record. A FILLED finding comes off the
  open list; a PARTIALLY FILLED finding keeps its place with the
  partial fill named next to it, so the next sweep does not
  re-discover the same half-answer. Correct version numbers and
  other facts that changed — a stale version on the record is a
  finding that is already wrong.
- Then run the new sweep on the corrected record. New findings
  join a list that is known fresh, not a list carrying last
  round's misses.

## A miss counts as a finding too

- When the re-check finds something the previous sweep missed
  entirely — a tool that already existed and was overlooked —
  record the miss openly. Hiding it leaves the gap on the books
  as open when it was never open, and the next sweep will miss
  it again.
- A miss changes the shape of the gap it touches: a tool that
  already ships most of the job turns an open gap into a
  partially filled one, and what is left to build is only the
  missing part. Say what is left, plainly, before anyone builds
  the whole thing again.

## Worked example

- A Linux tool-gap hunt ran Sweep 01 with 11 ranked gaps. Before
  Sweep 02, every Sweep 01 finding was re-checked live. The
  re-check caught a Sweep 01 miss: a scrolling-capture tool with
  on-device OCR already shipped on Linux, which partially filled
  the first gap — untested on Mint, so the remaining gap was
  narrowed to proving it there rather than building a new tool.
  Two more gaps came back partially filled (a native .env editor
  that only serves one framework, a trash tool whose Linux
  uninstall was desktop-only so far), and one version number was
  corrected (2.3.9 to 2.14.1). Sweep 02's verdict on the old list:
  13 still open, 3 partially filled, 0 filled — and the 12 new
  finds joined a list that was known fresh.

## Where this comes from

- Find Linux tool gaps to build thread (e0dc8d93, 2026-11-14
  ~21:21–22:26 EST): Joshua chartered the thread to search the web
  and GitHub for Linux tools that already exist and find the gaps,
  then ordered the re-check rule after Sweep 01 landed — "Before
  each sweep dobke check the previous sweep to ensure that the
  results rally dont exist at all." Sweep 02 applied it and caught
  the scrolling-capture miss, the two partial fills, and the
  version correction above.
- Found in the sixth BNB delta scan (2026-11-15). One in-window
  instance, user-ordered; the rule generalizes to any recurring
  sweep, since stale findings are the failure mode of every
  repeated scan.
