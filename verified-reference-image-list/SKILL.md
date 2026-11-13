# S46 — Verified reference-image list

## When to use

- Use it when a build needs reference images and every link in the list must actually open.

- Use it to expand a short reference list into a fuller one with honest coverage.

- This is a small skill: it is one disciplined step — expand, check live, record gaps — and it can also run as a step inside a larger build skill.

## Expand the list for the coverage the build needs

- Start from the topic and the coverage areas the build needs: angles, details, stages, variants.

- Expand the list until each coverage area has candidates, not just the easy ones.

- Keep the list organized by coverage area so gaps are visible at a glance.

## Check every URL live

- Check every candidate URL live before it goes on the list.

- A URL that returns an error, a redirect to nowhere, or a page without the image does not go on the list.

- Record the check date with the list so staleness is visible later.

## Exclude dead and hotlink-blocked candidates

- Exclude dead links and hotlink-blocked images; a candidate the build cannot load is not a reference.

- Count the exclusions and note why each was excluded, so the next pass does not re-add them.

- Never keep a broken candidate "just in case"; the list is only as trustworthy as its worst link.

## Record honest gaps

- When no usable photo exists for a coverage area, record the gap plainly instead of stretching a near-miss into place.

- Name what is missing and why it matters, so the build can work around it knowingly.

- A noted gap is a finished outcome, not a failure to hide.

## Deliver REFERENCE_IMAGES.md

- Deliver the list as `REFERENCE_IMAGES.md`: verified-live URLs grouped by coverage area, plus the noted gaps.

- Start from the [reference-images template](templates/reference-images-template.md): verified URLs grouped by coverage area, exclusions noted, gaps recorded.

- Keep the exclusions in the file as a short note, so the list's history is visible.

- Re-check the list live before a later build reuses it; links rot.

## Standing rules

- Never claim more than was checked; a URL on the list was opened and loaded, or it is not on the list.

- Hard $0: use only freely accessible images.

- Verify, do not eyeball; a search result snippet is not a live check.

## Where this comes from

- Proven in the White-tailed deer simulation thread: a reference list expanded from 12 to 58 images, 7 candidates excluded as dead or hotlink-blocked, honest gaps recorded where no usable photo existed — recorded in the BNB audit as S46.

## Alternatives for better results

- Run as a step inside a larger build skill instead of a standalone pass; the audit notes it could fold into [sandbox-first-sim-build](../sandbox-first-sim-build/SKILL.md) or [species-dossier-simulation-pipeline](../species-dossier-simulation-pipeline/SKILL.md).
