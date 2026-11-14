# S68 — Paper-to-build translation

Translate a research paper into a shipping feature on a machine the paper
never considered: take the paper's mechanism, keep its evidence claims
honest, and implement it with the tools that already exist on the target
PC — no new infrastructure, no new dependencies, no pretending the paper's
setup is yours.

## When to use

- A paper (or a video about a paper) describes a mechanism the user wants
  in an app — here, Google's Sleep framework for continual learning.
- The paper's environment (scale, hardware, training regime) does not
  match the target machine, and the gap has to be bridged honestly.
- The paper has no code release, or the released code does not run on
  the target.

## What counts as a translation, and what does not

- Keep the paper's MECHANISM, re-derive the IMPLEMENTATION. The Sleep
  paper's mechanism is: an active phase that learns a task, an offline
  consolidation phase that distils it into a new low-rank expert while
  the base and older experts stay frozen, and a dreaming phase that
  replays synthetic samples to stop the new expert overwriting what came
  before. The implementation on a CPU-only 8 GB PC is: Consolidate trains
  one new LoRA adapter per cycle (base + older adapters frozen), Dream
  generates synthetic examples from the local model and filters and
  dedupes them, and a Replay check compares the new adapter against the
  old one on held-out data.
- Never claim the paper's numbers as your own. The paper's reported gains
  belong to its setup; your build's numbers come from your own runs. Say
  which numbers are the authors' and which are measured.
- Never claim the paper's machinery when you built a simpler thing. Sleep
  has no MoE routing, no RL, and trains one model at a time on the target
  PC — so the build's README says SFT only, no RL, no MoE routing, one
  model at a time. The honest-limits section is part of the feature, not
  an afterthought.
- Read the paper, not the summary of it. The Sleep translation was built
  from arXiv 2606.03979 itself (Behrouz et al.), checked against the
  Google Research blog post of 2026-10-27, and the build notes that the
  paper has no code release — so every implementation choice is the
  translator's, and is labelled as such.

## The translation steps

- Map each paper component to a target-PC component, and write the map
  down. Sleep → Stella: consolidation = a new LoRA adapter per cycle;
  dreaming = local Ollama synthetic examples; replay = a check that
  flags DEGRADED past a threshold, never silently passes. If a component
  has no target-PC equivalent, say so and drop it openly rather than
  faking it.
- Bound the synthetic data: generated examples are filtered and deduped,
  capped at the real row count (synthetic never outnumbers real), and the
  whole Dream step skips cleanly when the generator (Ollama) is down
  instead of failing the run.
- Design for interruption from the start: a half-written cycle folder
  (from a crash or a kill mid-write) must not crash a resume. The first
  Sleep build had exactly this defect — resume crashed on a half-written
  cycle folder — and it was found by verification, fixed, and re-verified
  before shipping.
- Ship it as a normal version: tests for the new phase, a fresh-unzip
  verification, a CLI smoke test, and a Release — the paper pedigree does
  not exempt it from the ship pipeline. Stella v0.3 shipped 142 train
  tests + 120 base tests green from a fresh unzip, plus the CLI smoke.
- Keep the real-PC proof open until it is real. The first real Sleep run
  on the user's PC is the proof the translation works on his hardware —
  it stays an open item until he runs it, not a claim in the release
  notes.

## Where this comes from

- STELLA ✨ Development thread (2d7b2739), 2026-11-13 ~09:39–09:40 EST:
  Joshua sent the Sleep-framework video ("We need to build something
  like this for Stella") and the build started the same hour,
  grounded in arXiv 2606.03979 itself (no code release, authors'
  numbers only), translated to PC specs — Consolidate = new low-rank
  adapter per cycle, Dream = local synthetic examples, Replay check
  flags DEGRADED.
- STELLA ✨ Development thread (2d7b2739), 2026-11-13 10:02–11:12 EST:
  the Sleep phase landed as Stella v0.3 — built, verified (142 train +
  120 base tests green from a fresh unzip, CLI smoke), one defect found
  and fixed in verification (resume crashed on a half-written cycle
  folder), shipped as Release v0.3 with the commit hash matched
  (2f775462). The README carries the honest-limits section (SFT only,
  no RL, no MoE routing, one model at a time). A real Sleep run on the
  user's PC is still the open proof.
- ACR DEV thread (f9230b1c), 2026-11-13 ~09:29 EST: the same Sleep
  framework video was shared there as relevant to ACR's theme-switch
  forgetting (resonance 0.52 → 0.125 on a theme change) — the paper's
  mechanism maps to more than one app, but no ACR build was ordered
  from it.

## Alternatives for better results

- When the paper HAS a code release that runs on the target, use it
  instead of translating — translation is for papers whose code does not
  exist or does not run here.
- When the paper's mechanism needs hardware the PC does not have (GPU
  training, multi-node), say so plainly and do not build a fake version
  of it.
