# Roster audit template

Re-check against a fresh `ollama list` before filling this in. Never trust a
stale roster.

## Seats

- Driver (incumbent, strengths, weaknesses):
- Reviewer (incumbent, strengths, weaknesses):
- Vision (incumbent, strengths, weaknesses):
- Tool (incumbent, strengths, weaknesses):
- Fast (incumbent, strengths, weaknesses):

## Cheapest wins

- Quant re-pulls that save RAM for free (for example Q8_0 to Q4_K_M):
- Dead weight to cut, with the reason for each cut:

## Graded candidates

For each candidate record: quant size, licence, runtime compatibility,
vendor benchmarks (flagged unreproduced), seat judged against, and verdict
(beats incumbent, ties, or loses).

## Ranked trials

Trials in order, each with its exact pull tag:

1. `ollama pull <tag>` (seat, why it earned the trial)
2. `ollama pull <tag>` (seat, why it earned the trial)

## Watchlist

Models to watch, with the trigger that would promote each one to a trial.

## Rejects with reasons (do-not-re-propose)

- Model: reason it was rejected, with the evidence.

## Cloud picks

Hard $0 and no card only, or this section stays empty.

## Unverified

Models that could not be graded, with what is missing for each one.
