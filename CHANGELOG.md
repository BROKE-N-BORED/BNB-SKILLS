# Changelog

All notable changes to BNB-SKILLS. Dates are in EST.

## Eighth delta scan - 2026-11-18

Eighth delta scan of all chat threads (window ~18:47 EST 2026-11-17
to ~21:02 EST 2026-11-18, 106 chats read). Two new skills: S91
no-terminal-by-default (Tier 1) and S92 how-to-manual. S91 carries
the standing order from 2026-11-18 ~18:51: the default for every
project is no terminal for Joshua, no terminal to build, install,
run, or check anything; everything he has to do is doable by
clicking or GUI, and any flow that hands him a terminal command is
a defect. S92 is the manual playbook from the SOLDAR how-to manual
he ordered the same day (write MANUAL.md in plain words, verify
every claim against the real tree, render an A4 PDF via headless
Chromium, deliver PDF plus source, name anything unverified).

Fourteen existing skills updated. S1 gains 11 patches: the no-zip
rule means no zips in chat, not no built zip on the Release (the
OST v17-v21 incident); a checksum sidecar next to every release
zip; the push-403 diagnosis order (check .github/workflows/*
first); Gmail blocks zips containing executables; the new-repo
app-install gate; binary files cannot ride the snapshot push;
the large-file browser route; push while he is present; the
record-check rule; verify a Release exists before retrying a
browser failure; and the Cloudflare API token lesson. S5 gains 6
patches, including the failure-was-in-the-test rule, the sandbox
write-burst glitch, long jobs must checkpoint, and the
capability-claim rule. S6 gains 6 patches, including .desktop
launchers shipping executable in the zip, the Uninstall menu
entry, icon PNGs not riding the snapshot push, post-export steps
as buttons, the filename check, and GUI install paths for missing
system libraries. S69 gains 5 patches (stalled-driver case,
Android SDK setup traps, sandbox Gradle daemon failure mode,
shared-failure awareness, long-run watchdog pattern). S70 gains 5
patches (preserve aspect ratio, validate poster matches, clear
the poster cache when the matcher gets stricter, dialogs sized to
content, declutter by subtraction). S71 records RIZA through
chapter 25, Part 6. S74 gains the Pixel Forge v0.81 root-cause
worked example. S77 gains 4 patches (results step separates
grader bugs from model failures, bench of specialists plus
autoswitch framing, result-file rule, thin-evidence rule). S79
gains 3 patches (quiet-box precondition, P01 status, hold do not
re-run). S84 gains 7 patches: the MIMIK live-update lessons (bash
never sh, scrub inherited env, launcher lives in .local/bin, the
live end-to-end update run in the verification protocol), rollback
restores every build folder, the download-back proof step, the
first live-GitHub end-to-end proof with the two-stage proof
pattern and the sidecar rule, the ACR v0.12 implementation notes,
five more worked implementations, and the script exemption (a
script read fresh from disk every run is always current), a Delta
7 miss now fixed. S85 gains the look-it-up-yourself rule. S86
gains 5 patches, headlined by the mandatory comparison step (the
SOLDAR n8n gap audit: a review must compare against the reference
product and the full promised scope, listing what is missing, not
only what is broken). S87 extends its plain-language rule to
status updates. S90 gains one message, one "one".

The delta's tools (T39-T41) and tool updates live in BNB-TOOLS;
its new role pack (ost-report-card-analyzer) lives in BNB-ROLES.

## Seventh delta scan — 2026-11-17

SHA: 3a18f4fe

Seventh delta scan of all chat threads (window ~11:42 EST 2026-11-15
→ ~18:47 EST 2026-11-17). Seven new skills: S84 silent-update-check
(Tier 1), S85 pick-it-up-and-it-works (Tier 1), S86 dogfood-review
(Tier 1), S87 plain-text-task-lists, S88 lean-core-addons, S89
thread-scope, S90 info-only-answers. S84 carries the standing order
from the main chat (2026-11-17 ~15:53-15:56): every app silently
checks its GitHub repo for a newer Release on launch, stays quiet
when current, asks before pulling, verifies the download before
installing, and asks before restarting to complete the update.

Thirteen existing skills updated, headlined by S1 (14 patches):
the phantom completion handoff (a builder handoff can fabricate a
completion summary with hashes while the builder is still running),
releases published in ascending version order with the Latest badge
verified after multi-release days, explicit push state in status
reports, precise browser-failure reporting with a retry plan, the
disk-full check when a suite vanishes silently, the settled built-zip
ship format, push-first on his order, no diagnostic-photo asks,
one version source of truth, plain semver everywhere with no
batch-suffix tags, push-plus-Release confirmation, a new filename
per version (proven twice), sound-alike provider names (Groq is not
Grok; EXAONE is LG), and the no-zip rule extended to OST. S5 gains
7 new "Verify before you claim" examples, including the second
verify-the-claimed-CORRECTION instance and the fake-verification-UI
pattern; S6 gains the exec-bit extractor lesson, installer failure
detection, the standalone-HTML rule for web games, the
every-release launcher check, the new-filename rule, the two-phase
installer test pattern, and generous cold-start timeouts; S53 gains
browser-down is not a stall excuse; S63 gains the both-themes proof
rule; S65 gains no questions whose answers are in the record; S69
gains the Delta 7 restart-recovery shapes (parent-picks-up-and-
finishes, resumable-from-saved-state, writes-blocked, resume-not-
restart); S70 gains five field-proven design rules (dark theme,
empty states, plain-words labels, the radial wheel/dial pattern, no
arbitrary caps); S71 tracks RIZA through chapter 22, Part 6 underway;
S72 gains the full-chain rule for free-service verification; S74
gains the root-cause-first reinforcement; S77 gains the fresh-content
rationale, the OST v21 score break, the analyzer role (pending),
and the Fara-cycle note (Delta 6 near-miss, pre-window); S79 gains
the joint testing protocol, real scores for every test, the resume
rule with its source, and the v1.1.0 / 152-test stale fix. Library
now 90 skills (Tier 1: 25, Tier 2: 55, Tier 3: 10).

## Sixth delta scan — 2026-11-15

Sixth delta scan of all chat threads (window ~23:17 EST 2026-11-13
→ ~11:42 EST 2026-11-15). Eleven new skills: S73 no-invented-limits
(Tier 1), S74 no-bandaids (Tier 1), S75 self-test-command, S76
ai-code-review-loop, S77 trim-test-train-cycle, S78
rubric-score-fix-rescore-loop (ships the DQI rubric as its worked
example), S79 living-user-test-suite, S80 sweep-recheck-first, S81
destructive-action-defaults, S82 sleep-cycle-consolidation (Tier 3),
S83 plain-numbers-answer (Tier 3). S77 follows Joshua's exact
sequence — OST test > results > STELLA trim > OST test > results >
STELLA train > OST test > results — and is marked as the gist, with
further detail to land when he gives it.

Twenty-four existing skills updated, headlined by the "cut" wording
fix: say "update the Release", never "cut" (S1, S6 — Joshua banned
the word 2026-11-14). S1 also gains parent-verification of delegated
builds, the zip audit checklist, the checksum file beside the zip,
user-data scrubbing, and the app-does-its-own-job rule; S5 gains 9
new "Verify before you claim" examples; S6 gains the v0.53 installer
checklist and seamless install; S69 gains 10 new recovery shapes;
S70 and S71 get their stale counts fixed (library at 72 entries,
Drops 5–6; RIZA manual through chapter 13, Part 3 underway). Library
now 83 skills (Tier 1: 22, Tier 2: 51, Tier 3: 10). Pushed as commit
394470b2.

## S6 template fix — 2026-11-14

SHA: 41742fee

One-line fix in the S6 desktop-entry template
(`linux-release-packaging/references/desktop-entry-template.desktop`):
the empty-`%k` fallback did `dirname(os.getcwd())`, which looks for
install.sh in the parent folder — one level too high. The fallback
now uses the working directory directly, the form already proven in
BNB-TOOLS T26's installer. Found during the T26 build (2026-11-14);
the same bug was reported in MIMIK's installer `.desktop` and is
flagged to its thread.

## Fifth delta scan — 2026-11-13

SHA: 19be266d

Fifth delta scan of all chat threads (window ~20:24–23:17 EST
2026-11-13, 83 threads read). No new skills, no new tools, no new
presets/roles/plugins. Fifteen patches across 8 existing skills,
headlined by the STEMLAB file-by-file branch fallback + the corrected
bulk-push 403 diagnosis (S1), the round-2 "measure what round 1 only
read" section + the verify-the-correction rule + GITDATA provenance
(S5), the no-PyPI-wheels install rule (S6), "finish the task means
finish" (S53), audit #9 provenance (S65), the errored-builder
recovery trigger (S69), the rule repos + apply-the-library sections
and Drops 3–4 provenance (S70), and the five-chapter confirmation
(S71). Library still 72 skills (Tier 1: 20, Tier 2: 44, Tier 3: 8).

## Fourth delta scan — 2026-11-13

SHA: 42645b98

Fourth delta scan of all chat threads (window ~19:53–20:24 EST
2026-11-13, 82 threads read). A 30-minute window: no new skills, no
new tools, no new presets/roles/plugins. Two skill updates: the
encyclopedia rebuild of the UI design library + the gap-audit-before-
every-sweep standing rule (S70), and the three-chapter confirmation of
the roadmap-first manual shape + one chapter per "Go" (S71). Library
still 72 skills (Tier 1: 20, Tier 2: 44, Tier 3: 8).

## Third delta scan — 2026-11-13

SHA: 3c512e5b

Third delta scan of all chat threads (window ~10:00–19:53 EST
2026-11-13, 82 threads read). Six new skills: S67
low-usage-state-capture, S68 paper-to-build-translation, S69
restart-recovery, S70 ui-design-source-library, S71
roadmap-first-manual, S72 paid-service-viability-filter. Updates to
19 existing skills, headlined by the settled snapshot-push workflow
preservation + push-failure ls-remote rule + pre-release flip +
staging-intact subsection (S1), the Icon-quoting correction +
absolute-path launchers + installer caps and resume (S6), the
never-present-unchecked-names rule + 429 hold-the-list + taste rules
(S7), the disk-space gate + per-module suite split (S8), the
tracker-stamp credit-grant rule (S10), the real-function-only
immutable rule (S53), the dead-controls gate check (S54), and the DUO
v0.23–v0.31 record (S55). Library now 72 skills (Tier 1: 20, Tier 2:
44, Tier 3: 8).

## Second delta scan — 2026-11-13

SHA: 364ca685

Second delta scan of all chat threads (window ~19:13 EST 2026-11-12 →
~10:00 EST 2026-11-13, 71 threads read). Five new skills: S62
un-stall-sweep, S63 qt-gui-proof-harness, S64 audit-each-one-combine,
S65 audit-findings-task-list-merge, S66 atomic-file-saves. Updates to
13 existing skills, headlined by the GitHub-only ship flow (S1 retitled,
email off by default everywhere; S53, S2), the no-card-pre-prompts rule
(S53, S1), workflow-file 403 + git blob-SHA read-back + CI billing-lock
triage (S1), fresh-clone verification (S1), the S55 stop-condition
corrections, the S56 audit-to-task-list conversion, the S6 GUI installer
window + python3-venv pkexec self-heal + no-terminal rule, the S12
licence gate, the S16 coverage-rot check + review-gate variant, the S17
measurement-vs-look lesson, the S36 low-end hardening section, and the
S44 trivial-physical-cause check. Secrets-rule fix: a "no secrets in
code" verification step in the S1 ship checklist, the immutable rule
referenced in S61, and a secrets section in the repo .gitignore.
Library now 66 skills (Tier 1: 20, Tier 2: 39, Tier 3: 7).

## Audit-fix release — 2026-11-12

SHA: 47e9f3e3

Fixes from the repo audit (received 2026-11-12, verified mechanically from a
fresh clone): all 61 skills unified to the house format with numbered
playbook titles, `number` and `tier` added to every `skill.yaml`,
`include_in_prompt` set by tier (Tier 1 true, Tier 2/3 false), dead
absolute-path links replaced with a repo-level [CONNECTORS.md](CONNECTORS.md),
the S22 character-counting correction, all 15 orphaned supporting files
wired into their playbooks, and a new front door: tier-grouped README
index, Start here path, generated `skills.json` catalog, library checker
(`scripts/check_library.py`), and CI validation on push and pull request.
The audit itself is preserved verbatim in `docs/AUDIT.md`.

Licensed under the MIT License (see LICENSE).

## S53 no-rule-stalls update — 2026-11-12

SHA: 55c61ca7

S53 (no-stalling-task-list-cycle) updated with the standing no-rule-stalls
rule: no rule, process, question, or approval step is ever an excuse to
stall — verify, ship, next item, repeat until the list is done.

## S61 + T21 debug log layer — 2026-11-12

SHA: 011082c9

Added S61 (debug-log-layer): every project build ships with logging, error
handling, and an emailable debug report. Companion tool T21 in BNB-TOOLS is
the drop-in module for the standard.

## S60 side quest — 2026-11-12

SHA: 1aa56960

Added S60 (side-quest): when the main build hits a wall, build the
smallest standalone thing that fills the gap — verify it alone, plug it
in, log it as a BNB asset, return to the main build.

## Delta 1 — 2026-11-12

SHA: 52a40e85

First delta scan (scan window ~17:54–19:00 EST): 7 new skills S53–S59
(no-stalling task-list cycle, pre-delivery enhancement gate, dual-model
AI relay, org repo audit queue, BNB repo-manager delta scan, fake-provider
verification, Qt UI-thread offload), companion tools T18–T20 in BNB-TOOLS,
and 12 updates to existing skills (including the S18 per-cell
scale-matching correction).

## v1 — 2026-11-12

SHA: 9139f320

First release: 52 skills (S1–S52) distilled from all 67 chat threads —
73 raw workflow candidates deduped to 52 net-new skills. Full audit with
per-thread notes in `docs/AUDIT.md`.
