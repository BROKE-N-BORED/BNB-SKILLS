# Changelog

All notable changes to BNB-SKILLS. Dates are in EST.

## Third delta scan — 2026-11-13

SHA: TBD

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
