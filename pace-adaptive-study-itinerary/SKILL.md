# Pace-adaptive study itinerary

## When to use this skill

- Use it for any multi-course or multi-unit study plan where the schedule must stay honest as real pace becomes known.

- Use it when the user has a list of courses or units and a rough idea of pace, but no measured pace yet.

- Do not use it for a one-off study session; the method needs repeated completions to measure pace.

## Build the schedule from a seed pace

- Start with a seed pace: the user's best guess at how fast they will complete units, stated as units per week or days per unit.

- Build the full itinerary from the seed pace, with a projected date for every unit.

- Label every date as a seed date so nobody mistakes a guess for a measured projection.

## Measure real pace from logged completions

- Log every unit completion with its date as it happens.

- Once 2 or more units are logged, compute the real pace from the completions: units completed divided by time taken.

- Do not recalculate from a single completion; one data point is not a pace.

## Recalculate all projected dates from real pace

- Recalculate every remaining projected date from the measured real pace, not from the seed.

- Keep the seed dates visible next to the live dates so the drift is honest and visible.

- Recalculate again each time new completions change the measured pace.

## Weekly check-ins feed the math

- Check in weekly: log what was completed, recompute the pace, and update the live dates.

- A check-in with no completions is still data; it lowers the measured pace and moves the dates, and that is correct.

- Never hide a slip by leaving old dates in place; the itinerary moves with the math.

## Standing rules

- Never claim more than was checked; seed dates are guesses until real pace replaces them.

- One item at a time: log completions as they happen, do not backfill a whole history from memory.

- Show seed-vs-live dates side by side; the comparison is the honest part.

## Source

- Audit S38. Proven in the STUDY DASHBOARD DEV thread (CS50 11-course journey) and reused as the pace-engine concept in the Universal Study Portal.
