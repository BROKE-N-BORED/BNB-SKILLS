# S40 — Token burn-rate baseline and scheduled recheck

> Twin tool: [token-burn-rate-tracker (T16)](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/token-burn-rate-tracker) — baseline snapshot, scheduled recheck, tokens per day and pool-lifetime estimate.

## When to use

- Use it when the user asks how long a metered pool — tokens, credits, or any capped resource — will last.

- Use it when a single snapshot cannot answer the question and a measured rate over days is needed.

- Do not use it to check subscription status alone; the system `subscription-status` skill already covers that. This skill is the baseline-to-recheck-to-rate workflow around it.

## Record the baseline

- Record a baseline snapshot: subscription status plus the locally logged token totals on that date.

- Write the baseline down with its date; the baseline is a file entry, not a memory.

- Record the baseline in the [baseline record](templates/baseline-record.md): date, subscription status, logged total, pool size, and remaining.

- Note the pool size the lifetime will be measured against.
- Use pool numbers only for the rate: a locally logged totals counter may not map to the pool. The November 3 recheck's "local totals" counter (~340M) did not map to the pool at all (the pool was still 0% used then), so the token plan used pool numbers only (main chat, 2026-11-13 17:07).

## Schedule a one-time recheck

- Schedule a one-time recheck days later; a few days of real usage is enough to measure a rate.

- The recheck is one-shot, not recurring; it fires once and the math is done then.

- Do not schedule the recheck for the same day; a same-day recheck measures nothing.

## Compute the rate at recheck

- At the recheck, record the same totals again and compute tokens per day since the baseline.

- Break the usage down per day where the logs allow it, so a single heavy day does not hide as an average.

- Compute the remaining-pool lifetime at the measured pace: remaining pool divided by tokens per day.

## Turn the rate into a rationing plan

- When the pool is finite and the pace would burn it fast, turn the measured rate into a written rationing plan (see the token plan, main chat 2026-11-13 17:03–17:07): a weekly budget from the measured burn, a tier split across the work, slowdown tripwires, and waste rules.
- Set the weekly budget from the measured pace, not from hope: the first billion went in ~10 days at ~100M/day once the free limit ran out, so the plan set 150M/week (~21M/day), stretching the second billion to ~6.5 weeks.
- Split the budget by tier: money work 50M, Code Forge 50M, active builds 30M, everything else + scheduled jobs 20M (per week, from the same plan).
- Set tripwires that tighten as the pool drains: 500M left → one build at a time + sweeps paused; 250M left → money + Forge only; 100M left → chat only.
- Name the waste rules that do most of the saving: one build at a time (parallel builds were the peak burn, 25–37M/hour); verify once — never re-verify what is already verified, reuse evidence; no unsolicited or giant sweeps.
- State what is unknown in the plan itself: expiry on additional tokens (none shown — do not assume one), the free weekly allowance size (not shown — do not count on it), exact per-build costs (use measured daily/hourly rates, not per-item costs).

## Report with the caveat

- Report the burn rate, the per-day breakdown, and the pool-lifetime estimate together.

- Carry the caveat: the pool may still be untouched if the weekly limit has not been exhausted, in which case the lifetime estimate is about the weekly allowance, not the pool.

- Never present the lifetime as certain; it is an estimate at the measured pace, and pace changes.

## Standing rules

- Never claim more than was checked; a rate measured over three days is a three-day rate.

- Measure, do not eyeball; the rate comes from logged totals, not from a feeling about usage.

- One recheck, one report; do not keep re-running the math without new data.

## Where this comes from

- Proven in the How long 1 billion tokens last thread: October 31 baseline to November 3 recheck measured about 13.1M tokens per day, about 77 days of pool at that pace — recorded in the BNB audit as S40.
- The token rationing plan (2026-11-13) extended the skill from measurement to budgeting: weekly budget, tier split, tripwires, waste rules.

## Alternatives for better results

- To check subscription status alone, the system `subscription-status` skill covers that; this skill is the baseline-to-recheck-to-rate workflow around it.
