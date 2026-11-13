# S50 — Email-a-zip code intake and dead-button diagnosis

**Caveat: stated but NEVER EXECUTED in-thread (the zip never arrived; no fix was done).**

## When to use

- Use this skill when the user wants help fixing their codebase and will send the source as a zip by email.

- Treat the intake steps as stated practice, not proven practice. The zip never arrived in the source thread, so no fix was ever done this way. Run the steps, and say plainly what worked and what did not.

## Take in the zip

- Ask the user to email the source zip to the connected Gmail account.

- Tell the user to exclude `.venv` and `__pycache__` from the zip before sending.

- Ask the user to say "sent" once the email is gone, so you know to look for it.

- Pull the attachment from Gmail, unpack it, and run a file check so the user can see the whole thing arrived.

- Report the file check back to the user before doing anything else.

## Diagnose before changing anything

- Read the code and diagnose the fault before changing a single line.

- Fix one thing at a time, in the order the user signed off on.

- Report each fix and its verification before moving to the next one.

## Diagnose a dead button

- Find where the button is created in the code.

- Check what its click is supposed to call, and look for a missing, misnamed, or wrong target.

- Trace that function through its steps to the break point.

- Triage by symptom first: nothing at all when clicked, starts then stops, or an error popup. Each symptom points at a different break point.

## Where this comes from

- Distilled from the "Fix System Forge Care code" thread (51ec77e5) in the 2026-11-12 audit: the intake was set up (email the zip, exclude `.venv`/`__pycache__`, file check on arrival) and the dead Care button diagnosed by tracing its click target — but the zip never arrived, so no fix was ever done this way. The thread cites the Code Forge zip intake as precedent, unverified from these threads.

## Available connectors

- [Gmail](../CONNECTORS.md) for pulling the emailed source zip attachment.

## Alternatives for better results

- Offer a hosted download link through file hosting when the zip is too large to email.

- Offer to run the file check as a plain file list the user can eyeball, so they can confirm nothing is missing before any fix starts.
