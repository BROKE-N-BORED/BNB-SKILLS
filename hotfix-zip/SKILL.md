# S29 — Hotfix zip

Patch the exact shipped build the user is running with a one-file fix, prove only that file moved, and email it with Sent verification.

## When to use

- The user has a stale pre-fix build in their hands and the full re-ship pipeline is still gated.

## Start from the exact shipped build

- Take the EXACT shipped build the user is running, not a newer tree and not a rebuild, because the hotfix has to match what is on their machine.

- Confirm which build the user is running first, from the version they report or a screenshot, and say which build the hotfix is based on.

- Change ONE file only, swapping in the fixed version, and touch nothing else in the tree.

## Prove only that file moved

- Diff the patched tree against the shipped build before you package anything, and check that the diff shows only the one file moved.

- Stop and say so when the diff shows anything else, instead of shipping a hotfix with unexplained changes.

- Run the targeted tests for the changed area on the patched tree, and report the results.

- Name the fix plainly in the report, such as which provider code was swapped and why, so the user knows what the hotfix changes.

## Package, email, and verify the send

- Package the patched tree as a zip with a fresh, distinct filename that names the fix, so it cannot be confused with the original build or an earlier hotfix.

- Record the exact filename and byte size of the zip before you send it.

- Email the zip to the user, then open the message in the Sent folder and read its attachment list yourself.

- Compare the attachment filename and size in Sent against the filename and size you recorded, and treat a missing attachment, a wrong filename, or a different size as a failed send, even when the service reported success.

- Resend the correct file when the check fails, and check the new sent message the same way before you report anything.

- Tell the user the hotfix is sent only after the Sent check passes, with the filename and size in the report.

## Where this comes from

- From the Groq/Gemini thread (be74cb87 — the CODE-FORGE-v2.5-FILTERFIX.zip hotfix, one file swapped, diffed, emailed and Sent-verified), with a related fix-and-refresh for MIMIK v0.1.1. Recorded in the BNB audit as S29.

## Available connectors

- Use the [Gmail connector](../CONNECTORS.md) to send the zip and read the Sent folder back, and read its current doc before running its commands.

## Alternatives for better results

- Offer the full [re-ship pipeline](../ship-pipeline/SKILL.md) instead when the fix needs more than one file, because a hotfix is only for a one-file patch.

- Ask the user to confirm the fix works on their machine, because their real-PC verdict closes a fix.
