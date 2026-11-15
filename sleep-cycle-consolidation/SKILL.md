# S82 — Sleep-cycle consolidation: consolidate, dream, replay-check, report

The nightly sleep cycle for a long-running agent with durable memory:
consolidate only what is new since the last sleep, dream synthetic
recombinations seeded from real material, replay-check old decisions and
rules for degradation, and report what consolidated, what emerged, and
what the check caught.

## When to use

- A scheduled nightly cycle for an agent that keeps durable memory across
  days — the cycle runs while the user sleeps and reports in the morning.
- Do NOT use this as a brainstorm sweep or an idea generator. The first
  attempt at this cycle did exactly that and was corrected: dreaming is
  recombination seeded from real material, not manufacturing new product
  pitches.
- Do NOT use this to rewrite or reorganize old memory entries. The cycle
  only adds what is new; old entries are left untouched.

## Consolidate only what is new

- Gather what happened since the last sleep — new decisions, new rules,
  new facts, new friction — and write it into dated memory as new
  entries.
- Do not touch old entries: no rewriting, no rewording, no reorganizing
  what is already there. The cycle appends; it never edits history.
- If nothing new happened, say so and consolidate nothing. An empty
  consolidation is a valid result, not a failure.

## Dream from replay, ungraded

- Dream synthetic recombinations seeded from real material: combine
  things the agent actually saw or did into new patterns, connections,
  or questions worth raising in the morning.
- Dreams are ungraded — no scoring, no ranking, no picking winners.
  They are offered as material, not as decisions.
- No product pitches. A dream never becomes a proposal for something to
  build or sell unless the user asks for that separately.

## Replay-check old decisions and rules

- Re-check a sample of old decisions and rules against what has happened
  since: do they still hold, have they degraded, do two rules now
  collide?
- Report what the check caught, including collisions between rules that
  each made sense alone — for example, "push after every verified task"
  colliding with "push only on my tap" while the user sleeps.
- A clean check is reported as clean. Do not invent problems to make the
  check look productive.

## Report what consolidated, what emerged, and what the check caught

- The morning report has three parts: what consolidated (the new items
  added), what emerged (patterns or questions from the dreams), and what
  the replay check caught (degradation or collisions, or clean).
- Keep the report short and plain. The user reads it over coffee; it is
  a summary, not a log dump.

## Where this comes from

- DREAM STATE thread (4ee01464, 2026-11-14–2026-11-15 EST): dream-01
  (2026-11-14 ~00:30 EST) was the wrong method — an intentional
  brainstorm sweep of 82 chats that drafted 20 product candidates.
  Joshua corrected it 2026-11-14 ~08:31 EST: it "just repackaged what
  already exists" and deliberately manufactured ideas, the opposite of
  dreaming. The corrected charter (dreams/CHARTER.md) was confirmed by
  Joshua with "Yes" 2026-11-14 ~08:35 EST: consolidate only what is new
  since the last sleep, dream from replay (ungraded, no product
  pitches), replay-check old decisions and rules, report what
  consolidated, what emerged, and what the check caught. Sleep-02 ran
  2026-11-15 ~03:24 EST as the first real cycle under the corrected
  charter: 5 items consolidated, dreams ungraded, replay check clean.
  It also surfaced that approval cards are the overnight bottleneck (5
  verified builds stalled on expired push cards in one night) and that
  subagents are 54% of token burn.
- Found in the sixth BNB delta scan (2026-11-15). One corrected charter
  plus one clean first cycle; the workflow is stated as written and
  should be re-checked against further cycles before it is treated as
  proven. This skill is Arlo-internal in origin and generalizes to any
  long-running agent with durable memory.
