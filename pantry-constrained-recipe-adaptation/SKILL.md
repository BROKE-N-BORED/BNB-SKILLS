# S52 — Pantry-constrained recipe adaptation and target-app formatting

**Status: Tier 3, weak. The lowest-priority skill in this repo. The only distinctive bit is formatting to the target app by reading the app's existing content first. The rest is ordinary cooking help.**

## When to use

- Use this skill when the user has a recipe and wants it adapted to the ingredients they actually have, in the format of the app they keep recipes in.

## Scale to the real quantity

- Scale the recipe to the quantity the user actually has.

- Correct the scale when the user corrects the quantity, and re-issue the recipe at the new scale.

- Check the scaled amounts against what the user has on hand, including a mix of homemade and store-bought portions.

## Substitute with what the user has

- Substitute each missing ingredient with an on-hand equivalent the user confirms they have.

- Explain the method change each substitution needs, not just the swap.

- Drain ground beef when it replaces leaner sirloin, because the fattier meat leaves grease behind.

- Brown mushrooms first when they join a dish, because they dump water as they cook.

- Use broth plus vinegar when there is no red wine, to keep the acidity the wine would have given.

- Drop ingredients the user does not have and does not want, and fold in the ones they do have.

## Consolidate stacked corrections into one clean copy

- Take every correction the user has given across the conversation and fold them into one final clean copy.

- Re-issue the whole recipe clean each time, instead of leaving the user to stitch together a chain of corrections.

- Accept a correction to the dish's name and re-issue the clean copy with the new name and nothing else changed.

- Pin down amounts the user settles on, such as a final hot sauce quantity, and keep them pinned in later copies.

## Format to match the target app

- Read the app's existing recipes first, before writing the adapted one.

- Match the layout the app already uses: title, servings, ingredients, and instructions in the app's own order and style.

- Deliver the adapted recipe in that layout, ready to paste into the app.

## Where this comes from

- Distilled from two threads in the 2026-11-12 audit: "Old El Paso taco seasoning" (b98324c9) and "Adjust chili recipe for ingredients" (0bfee90a — Chili Mac). Both adapted a recipe to what was on hand and consolidated stacked corrections into one clean copy, formatted to match the target app.

## Alternatives for better results

- Offer to save the adapted recipe as a clean copy the user can paste straight into the app, instead of leaving it in chat history.
