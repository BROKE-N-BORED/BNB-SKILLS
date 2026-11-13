# S39 — Sprite-sheet prompt pack

## When to use

- Use it when a game needs consistent art of the same character across many actions, poses, or sheets.

- Use it when the same character must survive repeated image generations without drifting into a different design.

- Do not use it for one-off art; the lock block pays off only across many prompts.

## Write one character-lock block

- Write a single character-lock block that fixes the character's design details: body, colors, clothing, gear, proportions, and style.

- Make the details specific enough that a different artist following them would draw the same character.

- Paste the lock block before every prompt in the pack, unchanged, every time.

## Write one prompt per action or pose

- Write one prompt per action or pose, each starting with the full lock block followed by the action.

- Keep the action description to the pose and the motion; the lock block already carries the design.

- Cover the full action map the game needs before generating anything, so no action is invented mid-run.

- See the [prompt pack example](examples/prompt-pack-example.md) for the lock-block-plus-action shape.

## Hold lock, model, and seed constant

- Use the same lock block, the same model, and the same seed across every sheet.

- Same lock plus same model plus same seed is what keeps the character the same across every sheet.

- When any one of the three changes, say so plainly and expect the character to drift.

## Prefer per-action strips over the master one-shot

- The master one-shot prompt — all actions in a single generation — is flagged hit-or-miss; it sometimes works and often does not.

- Per-action strips are the reliable route: one generation per action, each with the lock block.

- Offer the one-shot as an option, but build the pack around per-action strips.

## Standing rules

- Hard $0: use only free models and free generation routes.

- Never claim more than was checked; a prompt pack is a plan for consistent art, not proof the art will match until it is generated and compared.

- Fix the one named thing when a generation drifts; do not rewrite the whole lock block for one bad strip.

## Where this comes from

- Proven in the Free AI trials thread: a Titan-13-style robot prompt pack, plus 10 Civitai/fal.ai prompts built around the user's actual projects — recorded in the BNB audit as S39.
