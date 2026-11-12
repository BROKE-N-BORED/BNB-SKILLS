# Email-a-zip code intake and dead-button diagnosis

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

## Available connectors

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for pulling the emailed source zip attachment.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer a hosted download link through file hosting when the zip is too large to email.

- Offer to run the file check as a plain file list the user can eyeball, so they can confirm nothing is missing before any fix starts.
