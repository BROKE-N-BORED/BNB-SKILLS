# S78 — Rubric-score-fix-rescore loop: improve scored work until the gains stop

Improve a piece of work against a weighted rubric with hard-fail
gates: score it, fix the lowest dimension first, re-score with an
independent scorer, and keep going while each round gains more
than a point.

## When to use

- The user wants a build, a scene, a model, a document, or any
  scored artifact graded and then improved round by round.
- A rubric already exists for the kind of work (a design rubric,
  a writing rubric, a review checklist with weights) — or the user
  asks for one to be built first.
- Do NOT use this for a one-off review with no follow-up round —
  a single score with ranked improvements is a review, not the
  loop. Do NOT re-score your own fix with the same scorer that
  scored it the first time: the re-score must be independent.

## Score against the rubric, gates included

- Score every dimension of the rubric, 0–10, in plain words: each
  level says what the work looks like, not what a textbook calls
  it. The composite is the weighted sum, but the bands and the
  hard-fail gates decide the verdict, not the number alone — a
  gated dimension failing means Rejected whatever the composite
  says.
- The rubric is a YAML file with weights, bands, and gates spelled
  out, so the same work scores the same way whoever runs it. The
  worked example shipped with this skill is rubric.yaml, the DQI
  (Design Quality Index) rubric for 3D design and results: eight
  dimensions (Modeling 20%, Fidelity to the brief 20%, Materials
  15%, Lighting 10%, Composition 10%, Animation 10%, Performance
  on the user's PC 10%, Render quality 5%), five bands from 95
  Zenith down to under 70 Rejected, with hard-fail gates. Its
  source is quality-rubric-3d/rubric.yaml (2026-11-14).
- The same shape works in any domain: the writing rubric this one
  was modeled on scores writing the same way — weighted
  dimensions, bands, gates, and the same improve-until-it-stops-
  gaining loop. Build the rubric for the domain first, then run
  the loop on it.

## Fix the lowest dimension first, then re-score

- After scoring, fix the lowest dimension first — that is where
  the biggest composite gain lives. Name the fix and its expected
  gain before building it, so the re-score can check whether the
  gain actually landed.
- The re-score is done by an independent scorer, not the builder
  of the fix. The builder's job is the fix; the scorer's job is
  the honest number. A fix that scores itself will always look
  better than it is.
- Continue while each round gains more than a point on the
  composite. When a round gains a point or less, the loop has
  stopped paying: stop, report the final score and band, and let
  the user decide whether more rounds are worth it. A loop that
  runs past its gains burns time for nothing.

## Worked example

- A 3D dice scene for a game was scored against the DQI rubric
  and came out at 65.00 — Rejected band, with Materials 4.5,
  Composition 4.5, and Lighting 5.0 as the weak dimensions. The
  loop said fix the lowest dimension first, and that was
  materials: procedural PBR maps plus fixing the scene UVs, worth
  about +5 on the composite.
- The materials fix was built and verified — all checkers passing,
  files under budget, renders eyeballed: the felt had a real weave,
  the wood rim read as boards with joints, the cup read as
  leather. An independent re-score came back at 69.45, up from
  65.00 — still Rejected, by 0.55, but up more than a point, so
  the loop continues: the next round fixes the next-lowest
  dimension, and the loop stops only when a round gains a point
  or less.

## Where this comes from

- MAIN CHAT thread (c6ee49a6, 2026-11-14 ~16:59 EST): Joshua
  ordered the rubric — "Find some really good blender builds and
  models and scenes and animations and what nit and take extensive
  notes to create a yaml rubric like FZI does for writing only we
  need a rubric for quality design and results whke it uses
  reblend" — and added SKULLPT. The result was DQI, built
  FZI-style: eight dimensions, five bands, hard-fail gates, and
  "the same improve-until-it-stops-gaining loop."
- Reblend work for Uahztee game thread (1c1928e9, 2026-11-14
  ~20:58 – 2026-11-15 ~11:01 EST): the loop run in full — v4
  scored 65.00 Rejected, the materials fix built, v5 independently
  re-scored at 69.45, and the continuation rule stated plainly:
  "The loop continues since we gained more than a point."
- Found in the sixth BNB delta scan (2026-11-15). Two in-window
  instances: the rubric's creation and its first full loop.
