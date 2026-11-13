# S9 — Screenshot-driven diagnosis and fix spec

## When to use

- Use this skill when the user reports a bug with a phone screenshot, which is their main bug-report channel.
- Use it to turn a screenshot and a short description into a diagnosis, a workaround, and an ordered fix spec for the DEV thread.
- Ask the user what specifically is wrong when they reject a render or a build, before you rework anything.

## Read the screenshot and name the symptom

- Look at the screenshot yourself and name the visible symptom in the user's own words.
- Never dismiss what the screenshot shows as a sandbox artifact, because the user's photo proves it is real.
- Read the actual code behind the symptom to find the real cause, instead of guessing from the picture alone.

## Separate the kinds of cause

- Decide which kind of cause the evidence supports: a real bug, a misleading label, a user error, or a provider limit.
- Name the evidence for the kind you picked, and name the evidence that would change your mind.
- Give an immediate workaround the user can use right now, even when the fix itself goes to the DEV thread.
- Name exactly what evidence is still needed, such as the raw session-log line, instead of guessing at the missing piece.

## Send an ordered fix spec to the DEV thread

- Send the fix spec to the owning thread as a self-contained brief (see [cross-thread-dispatch](../cross-thread-dispatch/SKILL.md)), ordered by what to fix first.
- Include the symptom in the user's words, the real cause with file and line, and the kind of cause, so the DEV thread does not re-diagnose from scratch.
- Verify the fix with measurements rather than assertions: pixel widths, geometry at multiple window sizes, and renders checked at several sizes.

## Where this comes from

- This diagnosis shape was used for the Gemini thought-signature error and the EXAONE rate limit, the misleading LOADED MODEL label, the header clip (true minimum width 1094 against a reported 982, checked at five widths), the grey dice (lighting, not the model), the cup (backface culling), and the Hosts and Learn mnemonic bug. It is recorded in the BNB audit as S9.

## Alternatives for better results

- Offer to ask for the raw log line or a second screenshot from a different angle when the first screenshot leaves two causes open.
- Offer to reproduce the fault in the sandbox first when the code alone does not settle the cause.
