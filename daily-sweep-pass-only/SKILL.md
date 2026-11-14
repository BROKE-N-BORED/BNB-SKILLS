# S10 — Daily sweep with pass-only reporting

## When to use

- Use this skill for a scheduled scan that runs against fixed criteria, such as a daily stocks sweep, a free-services sweep, or a course sweep.
- Run the scan on its schedule and report only the items that pass, whether the scan is a cron job or a manual run.
- Update the cron job instructions in place when a rule changes, so the next run follows the new rule.

## Scan against fixed criteria

- Write the criteria down before the first run and keep them fixed between runs, so a pass means the same thing every day.
- Check every candidate against every criterion, and record the evidence for each pass.
- Dedupe new finds against the catalogue before reporting, so an item already listed is not reported twice.
- See the [criteria template](references/criteria-template.md) for the criteria of the three established variants.

## Report only what passes

- Report only the items that pass, with the evidence that cleared them.
- When nothing passes, send one short line saying nothing cleared the bar, with no rejects list and no watchlist.
- Report losses first when a previously passing item stops passing, such as a free tier that is gone or a service that is now phone-gated.
- Never pad a thin day with near-misses. A pass-only report stays trustworthy only when a pass is rare and real.

## Keep the catalogue honest

- Add each newly verified find to the catalogue and remove each loss, so the catalogue stays the true list of what passes.
- Record the date and the source of every verification, because free tiers and prices change.
- Flag anything you could not verify instead of listing it as passing.

## A tracker stamp never verifies a credit grant

- A third-party tracker's "verified" date — or any aggregator stamp — never
  counts as verification for a free-credit grant. It may just be re-reading
  the provider's old announcement, not testing an account.
- A credit grant counts as verified ONLY from the provider's CURRENT pricing
  page or a live account check (a real balance read on a real key). An old
  launch blog post never overrides current pricing.
- Re-verify a grant claim on the morning of the sweep, from one of those two
  sources — never publish it from a stored tracker stamp. A sweep built from
  a stale stamp is stale the minute it goes out.
- When a grant turns out to be dead: correct the sweep record AND the tracker
  record the same day, and post the correction where the bad info went out.
  Report a tracker-only grant as UNVERIFIED, with the gap named, until a
  live check or current pricing page confirms it.

## Where this comes from

- This shape runs daily as the stocks and crypto sweep (17:20 cron) and the $0-services sweep (about 10:20 AM cron), and the same discipline was applied to the $0 course catalogue and reused for inbox triage and the Raon Ollama-support watch. It is recorded in the BNB audit as S10.
- The credit-grant rule comes from the Tripo miss on 2026-11-13: the morning sweep listed 2,000 free Tripo API credits as a verified pass off a tracker "verified Oct 31" stamp; the live balance check (0.0, four times) landed after the sweep was already posted, and the grant turned out to be dead since Tripo's April 2024 launch post. Second repeat of the Replicas lesson.

## Alternatives for better results

- Offer to tighten the criteria when too many items pass to act on, or loosen one criterion when nothing has passed for a long run.
- Offer to re-verify a passing item later the same day when its price or stock is known to move fast.
