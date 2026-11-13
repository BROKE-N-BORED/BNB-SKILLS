# S61 — Debug log layer: every project ships with error handling, logging, and an emailable debug report

## When to use

- Every project build ships with a debug log layer. It is part of the build, not an optional extra — add it when the project is built, not after the first bug report.
- Use it when adding logging and error handling to a new or existing project, and when diagnosing a failure from a debug report he emails.
- Use the [module](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/debug-log-layer) (T21, BNB TOOLS) to implement it; this skill is the standard the module follows.

## The standard

Every project has, from its first shipped version:

- A logger writing timestamped lines to a rotating log file, capped in size so it can never eat the disk.
- A ring buffer of the last N actions/steps before an error — the "what was it doing just before it broke" record.
- Error capture with full tracebacks, not just error messages.
- A context snapshot: app name + version/build, OS + version, Python version, RAM/disk, relevant dependency versions, settings that affect behaviour, and the status of every service the app depends on.
- A report generator, reachable two ways: on demand (a "Generate debug report" button or a `debug-report` command) and automatically on a crash.
- A crash hook that writes the report on any unhandled exception, then lets the crash show as normal. The report must never hide the crash.

## What it must capture

- Errors with full tracebacks. A message without a traceback is a guess; the report carries the whole stack.
- Warnings, not just errors — the warning before the crash is often the cause.
- The last N actions/steps before the error (default 200). What the user pressed, what the app started, what finished.
- Timestamps on every line, so the order of events is provable.

## Context

- App name + version/build, OS + version, Python version, RAM total/available, disk total/free.
- Dependency versions that matter to the failure (Qt, Ollama client, image libraries — whatever the app stands on).
- Settings that affect behaviour: which model/provider, which mode, which options. Never the keys themselves — see the no-secrets rule.
- Service status for everything the app depends on. The case that created this standard: Ollama died silently on his PC and DUO had nothing to say about it. The report must answer "is Ollama running, and which models are loaded" without him checking. Every service gets a short status check with a short timeout, so a dead service cannot stall the report.

## The report

- One file, plain text: `debug-report-<app>-<YYYYMMDD-HHMMSS>.txt`. If the logs are large, zip the report + the log files; the report itself stays one file.
- Same sections in every project, in the same order: Context, Settings, Services, Recent actions, Errors, Log tail. One report always reads the same way, whichever project it came from.
- Written somewhere he can find it: the project folder and the standard log path. The button/command tells him the exact path it wrote to.
- Generated on demand AND automatically on a crash. A crash the user did not see still leaves a report behind.
- Two reports in the same second must not overwrite each other — suffix, never clobber.

## The email flow

- The report is a single attachment he sends to broke.n.bored.studio@gmail.com when something breaks.
- It must be complete enough to diagnose from the report alone — no screenshots needed, no follow-up questions about versions or settings. If a diagnosis needs something the report does not carry, that is a gap in the layer, fixed in the layer.
- The report tells him what to do with it: the filename and path are shown when it is generated, and the project tells him where to send it.

## No secrets, ever

- Hard rule: the report scrubs API keys, tokens, passwords, and auth headers. Values are redacted; only which key/setting was present or absent survives.
- Scrubbing happens at write time, in the logger and in the report builder — not as an afterthought. A secret that reaches the log file is already a failure.
- Test the scrub: the smoke test logs fake keys and tokens, generates a report, and asserts no secret value appears anywhere in it. Any new secret shape gets a new scrub pattern and a new test.

## Lightweight

- Logging must not slow the app or eat disk: capped log size with rotation, a bounded ring buffer, cheap checks with short timeouts. His PC has 8 GB of RAM; the layer's footprint stays trivial next to the app.
- Service checks run at report time, not on a polling loop. Nothing in the layer runs in the background while the app works.

## Standard across projects

- Same report format, same file naming, same trigger in every project. A DUO report and a Pixel Forge report read the same way.
- Adoption rolls out from the main chat once the standard and the module exist: each project build adds the layer, it is not retrofitted by this skill's repo. The skill defines the standard; the projects adopt it.

## How to add it to a project

- Drop in the [module](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/debug-log-layer) (T21): one file, standard library only.
- Create the logger at startup, register the project's services and settings, install the crash handler.
- Wire the report to a button or a command, and show the path it wrote.
- Test it by forcing an error: log a fake exception, generate the report, and check the report carries the traceback, the context, and no secrets.

## Where this comes from

- Joshua's order, main chat 2026-11-12 ~20:22 EST: a debug and logging layer in every project build — error handling and debugging that generates a report of everything, so he can email it instead of diagnosing from screenshots.
- Triggered the same evening in the DUO thread (~20:20): Ollama stopped running on his PC and DUO had no report to say so. The Ollama service check exists because of that case.

## Available connectors

- [Gmail](../CONNECTORS.md) for the email flow — the report arrives as an attachment to broke.n.bored.studio@gmail.com.

## Alternatives for better results

- Offer to add the layer to a specific project build, wired to its real services and settings.
- Offer to read a debug report he emails and diagnose from the report alone, and to name anything the report was missing so the layer improves.
