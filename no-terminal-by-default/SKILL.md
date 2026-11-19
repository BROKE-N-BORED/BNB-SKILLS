# S91 - No-terminal-by-default: Joshua never uses the terminal unless the work absolutely requires it

The default for every project is NO terminal for Joshua. No terminal to
build, install, run, or check anything. Everything he has to do must be
doable by clicking or GUI. Any flow that hands him a terminal command is
a defect, not a workaround. The terminal stays dev/VM-only for the
assistant.

## When to use

- Use this skill for every project, every version, from the first
  build. This is a standing rule, not a per-project decision.
- Use it when a build, install, run, or check step would hand him a
  command to type or paste: that step is the thing this skill
  removes.
- Use it when writing release notes and docs too: the rule reaches
  what he reads, not just the program.
- Do NOT use it to forbid the assistant's own terminal use in the
  dev VM. The terminal stays the assistant's tool. The rule covers
  what Joshua has to do, not what the assistant does behind the
  scenes.

## The rule

- Default: no terminal for Joshua. Build, install, run, check: all
  by clicking or GUI.
- Exception (a): a specific project explicitly specifies otherwise.
- Exception (b): the work absolutely requires a terminal and there
  is no click/GUI alternative.
- Anything else is a defect. If something ever needs the terminal,
  that is a defect to fix in the program, not a command to hand
  him. (Reblend's framing, 2026-11-18 20:30.)
- This extends the INSTALLER RULE (see
  [linux-release-packaging](../linux-release-packaging/SKILL.md),
  S6, 2026-11-12, immutable) from install/run to BUILDING as well.
- It pairs with
  [pick-it-up-and-it-works](../pick-it-up-and-it-works/SKILL.md)
  (S85): the app sets itself up, so there is nothing for him to
  type in the first place.

## The textbook defect pattern

- Offering "the one-line terminal way" as a fallback. The "Run
  instructions from image" reply (2026-11-18 17:18 EST) did exactly
  this and is now the textbook defect pattern. A terminal fallback
  is still a terminal step. The click path is the only path; if
  there is no click path yet, building one is the work.

## What "no terminal" covers

- Building, installing, running, checking.
- Post-export steps: every step after an export, including model
  registration, must be a button, never a typed command. STELLA's
  post-export `ollama create` step gets a button.
- Missing dependencies, including system libraries: every missing
  dependency gets a GUI install path. The installer must never hand
  him a command to run. Android Photo Transfer's missing-libmtp
  command is the case in point.
- Model pulls: a model pull needs a click path or a settled
  exception. SHELFLIFE's Fara Phase 2A hand-typed `ollama pull`
  needs one before Phase 2A runs; Fyrn Chat's `ollama pull` has no
  GUI pull yet, and pull buttons that only copy the command are
  still a terminal step.
- Release notes and docs: ACR v0.12's release notes led with bash
  commands. The rule reaches release notes and docs, not just the
  program.

## The nuance: the model running commands is not Joshua running commands

- FYRN v0.8's run-command tool is the MODEL running commands, never
  Joshua. That does not violate the rule. The rule is about what
  Joshua has to do with his own hands. Code running commands under
  the hood is the point of the rule, not a breach of it.

## Forcing examples

- OST v22 (2026-11-18): installer.desktop shipped non-executable,
  so double-clicking opened a text editor instead of launching.
  Joshua: "No i shouldn't need the fucjing terminal". The fix was
  in the program (the zip builder now stores .desktop files
  executable, see S6), not a command handed to him.
- "Run instructions from image" reply (2026-11-18 17:18 EST):
  offered "the one-line terminal way" as a fallback. Now the
  textbook defect pattern.
- ACR v0.12 release notes: led with bash commands. The rule reaches
  docs.
- SHELFLIFE Fara Phase 2A: hand-typed `ollama pull` on his Mint PC.
  Needs a click path or a settled exception before Phase 2A runs.
- STELLA post-export: the `ollama create` step after an export
  gets a button.
- Fyrn Chat: `ollama pull` for new models has no GUI pull yet. The
  Best Models page's pull buttons copy the command, which is still
  a terminal step.
- Android Photo Transfer: missing libmtp produced a command to
  run. Needs a GUI install path.
- FYRN v0.8: run-command tool is the model running commands, never
  Joshua. Not a violation.
- Reblend (2026-11-18 20:30): if something ever needs the terminal,
  that is a defect to fix in the program, not a command to hand
  him.

## What to check

- Before shipping, walk every step he will take: build, install,
  run, check. If any step is a command to type or paste, it is a
  defect. Fix the program or the packaging, not the instructions.
- Check the release notes and docs the same way: no bash commands
  leading the notes.
- Check the installer handles missing dependencies with a GUI path,
  including system libraries.
- Check every post-export step is a button.
- If a step truly has no click alternative, settle it as an
  explicit exception with him before shipping. An unsettled
  exception is not an exception, it is a defect waiting to be
  found.
- Check the .desktop launcher and scripts in the release zip are
  stored executable (see S6): a non-executable launcher sends him
  to the terminal.

## Where this comes from

- Main chat / WinLinx thread, 2026-11-18 ~18:51 EST. Joshua
  ordered it: "the goal is to not have to use the terminal when
  building any project" and "I shouldn't have to use the terminal
  for anything unless I am working on something that absolutely
  requires it."
- Broadcast to all build/dev threads 2026-11-18 ~20:30-20:37 EST;
  acked in about 40 threads.
- Already recorded in the workspace AGENTS.md and the workspace
  MEMORY.md.
- Found in the eighth BNB delta scan (2026-11-18). The biggest
  finding of the delta: one order, broadcast to every build thread
  the same evening.
