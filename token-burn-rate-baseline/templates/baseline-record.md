# Burn-rate baseline record — <resource / pool>

## Baseline

- Date: <date>
- Subscription status: <as reported by the subscription-status skill>
- Locally logged total used: <number>
- Pool size: <number>
- Remaining at baseline: <number>

## Recheck

- Scheduled recheck date: <date, days after baseline>
- Recheck date (actual): <date>
- Locally logged total used at recheck: <number>
- Days elapsed: <number>

## Computed

- Tokens/day since baseline: <(recheck total − baseline total) / days elapsed>
- Per-day breakdown: <per-day figures where logs allow>
- Remaining-pool lifetime at measured pace: <remaining / tokens per day, in days>

## Caveat

- The pool may still be untouched if the weekly limit has not been exhausted;
  in that case this lifetime estimates the weekly allowance, not the pool.
