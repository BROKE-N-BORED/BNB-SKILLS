# S60 — Side quest: when the main build hits a wall, build the smallest standalone thing that fills the gap

## When to use

- The main build needs a capability, tool, program, or algorithm that is missing, does not run on his PC, costs money, or needs hardware or software he does not have.
- Use it instead of stalling, instead of dropping the feature, and instead of declaring it impossible. His line: there is always a way — inside his PC's specs, build around the limitation rather than declaring it impossible.
- Do not use it when the gap is a decision only he can make, or needs his PC or his action. That is a hard gate, not a side quest (see [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md)).

## The trigger

Name the wall plainly: what the main build needs, and why it cannot have it — it does not exist, it does not run on Linux Mint, it needs a GPU, it is paywalled, it is hardware-gated. The trigger is a missing capability, not a missing decision.

## Step 1 — Name the gap

State exactly what capability is missing and what the main build needs it to DO. The precise function, not a vague "we need X". Not "we need meshing" — "we need a text prompt turned into a watertight mesh on a machine with no GPU". The gap statement is the spec the side quest builds against.

## Step 2 — Check first

Look for an existing $0 answer before building anything: the BNB repos (skills, tools, presets, roles, plugins), the workspace, open source. Use the [org repo inventory tool](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/org-repo-inventory) (T20, BNB TOOLS) and the [org repo audit queue](../org-repo-audit-queue/SKILL.md) (S56) to see what already exists under BROKE-N-BORED. If one exists, use it — no new build. The side quest only starts when the check comes back empty.

## Step 3 — Build the smallest standalone thing

- A tool, a skill, a program, or an algorithm — whichever fits the gap.
- Standalone first: usable on its own, not tangled into the main build. The main build plugs into it; it does not live inside the main build's code.
- Built for his PC's limits: Linux Mint, Ryzen 3, 8 GB RAM, no GPU. $0. No hardware he does not have, no paid service, no account with a paywall.
- The smallest thing that fills the gap — the gap's function only, nothing extra. The mandatory gate's "stay relevant" applies here: the side quest serves the gap, not adjacent ideas.

## Step 4 — Verify standalone, then plug it in

- Verify the side quest's output works on its own first: run it, drive it the way the main build will use it, prove the capability exists.
- Then plug it into the main build and verify the unblock: the main build does the thing it could not do before. The side quest is not done until the main build moves again.

## Step 5 — Log it

The side quest's output becomes a reusable BNB asset — a skill, a tool, or a preset, as fits — documented so the next build hitting the same wall does not start from zero. It goes into the matching BNB repo under the repo-manager's no-stall cycle (see [bnb-repo-manager-delta-scan](../bnb-repo-manager-delta-scan/SKILL.md)).

## Step 6 — Return to the main quest

The side quest is done when the main build is unblocked, not when the side tool is perfect. Return to the main build the same turn the unblock verifies. Polish on the side tool is a later item, never a reason to stay on the detour.

## Rules

- A side quest never replaces the main build. It is a detour, not a new project. If the detour starts looking like a project of its own, stop and tell him — that is his call.
- It stays small: the smallest thing that fills the gap. Scope creep here stalls the main build twice over.
- It never costs money and never needs hardware he does not have. A side quest that needs a GPU to fix a missing GPU is not a side quest.
- If the side quest itself hits a wall, one level deeper is allowed — a side quest inside a side quest — but flag it when it happens. Do not nest forever: two levels is the limit without his word.
- The mandatory enhancement gate still applies (see [pre-delivery-enhancement-gate](../pre-delivery-enhancement-gate/SKILL.md)): run it on the side quest's output before it plugs in, and keep it relevant to the gap.
- One side quest at a time per build. If the main build has several gaps, queue them; do not run parallel detours.

## Already done without the name

- Reblend: Blender too heavy for his PC → build a lightweight 3D engine from scratch.
- WinLinx: Windows programs do not run on Linux → build the compatibility layer.
- MIMIK: mimic has no Linux port → port it to Linux.
- SKULLPT's ZeroGPU mesh step: the mesh step needs an NVIDIA GPU → run it in the cloud instead.
- Qt test-env library extraction: VM restarts wipe system packages and apt is unreliable → extract the EGL/xcb libraries into the workspace and run tests against them.

## Where this comes from

- Joshua's concept, main chat 2026-11-12 ~19:56 EST: a skill for building standalone tools, skills, programs, and algorithms that fill a gap so a build limited by missing software or hardware can go ahead anyway.
- The pattern predates the name: every example above was done the same way before the skill existed.

## Available connectors

- [GitHub](../CONNECTORS.md) for checking what already exists under BROKE-N-BORED before building (with the [org-repo-inventory tool](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/org-repo-inventory), T20).

## Alternatives for better results

- Offer to check the BNB repos and the workspace first and show him what the check found before building anything.
- Offer to log the side quest's output into the matching BNB repo as part of the return step, so the next build finds it instead of rebuilding it.
