# S42 — Live local stock verification

## When to use

- Use it when the user needs a product for same-day pickup and a wasted trip costs them real time and effort.

- Use it for any local "find it tonight" request, not just the product that first needed it.

- Do not use it for a delivery order; this skill is about walking into a store and finding the item there.

## Set the exact pickup store first

- On each retailer's site, set the exact pickup store before checking anything.

- A stock result for the wrong store is worse than no result; it sends the user to the wrong place.

- Record which store each check was for, by name and town.

## Check the product page, not just search results

- Check the product page itself for stock and pickup timing; never trust the search-results line alone.

- Search results have lied: one run showed "Pickup Today" in search while the product page said "Pickup Tomorrow".

- Record what the product page said, including the pickup window it offered.

## Report verified items separately from phone leads

- Report VERIFIED items with price, stock count, aisle or bay, pickup window, and check time.

- Report PHONE LEADS separately: stores that might have it but are unverified, labelled "don't go on my word" with the phone number to call first.

- Never mix the two lists; a lead presented as verified is how a wasted trip happens.

- Report in the [verification report](templates/verification-report.md) shape: a VERIFIED table and a PHONE LEADS table, each with its check time.

## Re-verify later the same day

- Stock changes during the day; re-verify a VERIFIED item later the same day before the user leaves.

- If the re-check disagrees with the earlier check, report the newer result and say the earlier one changed.

- Record the check time on every verification so staleness is visible.

## Broaden by equivalence when the brand fails

- When the exact brand is not in stock anywhere, broaden by equivalence: what the product does, not what it is called.

- Name the equivalence plainly, such as a chemical class, so the user can judge the substitute.

- Verify the substitute with the same product-page discipline; a substitute is not verified just because the brand was not found.

## Why this skill exists

- It was born from a real failure: unverified store suggestions sent the user to four stores that had nothing.

- Every rule above exists so that failure does not repeat: product page over search results, verified over leads, re-check over stale check.

## Standing rules

- Never claim more than was checked; an unchecked store is a lead, not a find.

- Check the time on every claim; a morning verification is not an evening guarantee.

- Hard $0: no paid stock-check service, no delivery fee smuggled into a pickup plan.

## Where this comes from

- Proven in the Find Rug Doctor antifoam in Lewes thread: two live verifications the same day (3:20 PM and 6:50 PM), brand broadened to any silicone-based defoamer — recorded in the BNB audit as S42.

## Alternatives for better results

- For a one-time price or stock check, the system `live_page_checks` skill covers it; this skill adds the multi-store pickup-tonight protocol and the verified-vs-lead labelling.
