# Changelog

All notable changes to BNB-SKILLS. Dates are in EST.

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
