# S75 — Self-test command: every shipped app gets a --self-test that proves its live path in one step

Every shipped app gets a `--self-test` entry point that exercises its live
path end-to-end in one step — not just the unit suite. It is the thing a
user or a verifier runs to prove the app actually works after install.

## When to use

- You are shipping an app (any app: desktop, CLI, or GUI) and it has no
  one-step way to prove it works after install.
- A verifier or the user needs to check the app on a real machine without
  reading the code or running the full test suite.
- Do NOT use this as a replacement for the unit suite — the suite checks
  the parts, the self-test proves the live path. Both exist.

## What the self-test must do

- Run the app's real live path end to end: the actual flow a user runs,
  with real inputs and real outputs, in one command.
- Print a clear pass or fail for the whole run, in plain words, and exit
  non-zero on failure — a verifier must be able to tell from the exit
  code alone whether the app works.
- Be runnable from the installed app with no setup beyond the install
  itself. If it needs test fixtures, the app ships them or generates
  them; the user never has to fetch anything first.
- Keep it to one step. `--self-test` with no arguments is the whole
  interface — anything that needs a second command or a manual check is
  not a self-test.

## Worked example: Pixel Forge v0.70

- Pixel Forge v0.70 added `--self-test`, which "proves the Prompt tab's
  live path in one step": it runs the prompt-to-output flow the way a
  user runs it, instead of only exercising the unit tests.
- The pattern to copy: pick the app's main live path (the one tab, flow,
  or command the app exists for), drive it for real, and report pass or
  fail in one step. A self-test that checks a side feature instead of
  the main path proves the wrong thing.

## Where this comes from

- PIXEL FORGE DEVELOPMENT thread (b2e2291b, Sat 2026-11-14 ~22:00 EST):
  v0.70 shipped `--self-test`, described as proving "the Prompt tab's
  live path in one step". Pixel Forge v0.53–v0.73 shipped the same day,
  and v0.70's self-test is the one-step proof the app works after
  install — distinct from the unit suite and from package verification,
  which check the parts and the zip, not the live path from inside the
  app.
- Found in the sixth BNB delta scan (2026-11-15). One in-window
  instance; the workflow is stated as written and should be re-checked
  against a second app before it is treated as proven.
