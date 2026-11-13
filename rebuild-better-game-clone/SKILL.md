# S36 — Research to rebuild-better single-file game clone

## When to use

- Use it when the user asks for a better version of an existing game.

- Use it when the result must run offline as one file, with no server and no ads.

- Do not use it to copy a game wholesale; the point is a rebuild that fixes what the original gets wrong.

## Research the original first

- Research the original game's core loop and level structure before writing anything.

- Read reviews and player complaints to find the original's flaws; name them explicitly, because they are the rebuild's brief.

- Record the research in a short summary: core loop, level structure, named flaws.

## Build a single-file offline version

- Build one self-contained HTML file that runs offline: the engine embedded, no CDN, no ads.

- Implement named improvements over the original, one per flaw found in research, and list them in the research summary.

- Keep the file runnable by opening it directly; no build step and no install step.

## Harden the single file for low-end hardware

- Lazy-load a heavy 3D library behind a capability probe, with a 2D fallback: at boot, probe for WebGL first, and only on success load the 3D code (show a "Loading the 3D dice…" line meanwhile). When 3D cannot load, the game still plays with its 2D representation — never a blank screen or a dead page because a library failed.

- Self-host every font and make zero external requests: download the exact font files the page uses (a variable font needs one file per subset to cover its weight range) and serve them locally, so the game plays fully offline with no CDN dependency.

- Update the DOM incrementally instead of rebuilding it: build a scorecard or board once per roster/lineup and update it cell by cell afterwards, so unchanged cells keep their place, focus, and scroll position. A full rebuild happens only when the roster itself changes.

- Verify the SETTLE, not just the animation: a dice roll can tumble correctly and still land wrong — Yahtzee's dice re-rolled each die's orientation with a fresh random spin at settle and snapped it into its slot, up to a 270° jump, in about 3 out of 4 rolls. The fix lands the die with the right face up; never swap the skin/texture to match the rolled number at the end — the user will see the swap and call it a glitch.

## Verify by actually playing it

- Verify by actually playing the game headlessly at phone size, not by reading the code.

- Play through the levels the way a player would: start, play, win, lose, use every control.

- Record what was played, at what size, and what passed or failed.

- Record the playtest in the [playtest checklist](templates/playtest-checklist.md): one row per level, played, result, and fail count.

## Cut levels that fail playtesting twice

- When a level fails playtesting, fix it once and retest.

- When a level fails playtesting a second time, cut it and replace it with a new level.

- Do not keep patching a level that has failed twice; the replacement is the fix.

## v2 is driven by the user's real-phone verdict

- Ship v1 for the user's verdict on their real phone; their verdict drives the v2 rebuild.

- Fix what they name: layout at their screen size, missing rules or help, measurement or scoring they ask for.

- Keep v2 a rebuild of the same single file, not a second file or a new project.

## Standing rules

- Hard $0: no paid assets, no licensed engine, no service that costs money.

- Verify by playing, not by eyeballing the code; a level that was never played is unverified.

- The user's real-phone verdict closes a fix, not the headless playtest.

- Never claim more than was checked; name the levels played and the ones not yet played.

## Where this comes from

- Proven in the Remaster Q thread: Q+ as a single-file offline HTML game, 15 missions plus sandbox plus IQ TEST, with v2 driven by the user's real-phone verdict (all buttons visible at 360×800, rules book, IQ measurement with graded stages and a strengths graph, stats plus downloadable report) — recorded in the BNB audit as S36.
- The low-end hardening section comes from Yahtzee v0.2–v0.6 (2026-11-12–13): lazy-loaded Three.js behind a WebGL probe with a chips-only fallback, self-hosted fonts, incremental scorecard updates, and the dice-settle fix.
