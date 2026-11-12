# Free-track course enrollment, guardrailed

## When to use

- Use this skill when the user asks to be enrolled in a free course through a browser task.

- Use it for any provider with a free or audit track, such as the edX audit track used for CS50x.

## Hold the hard guardrails

- Enroll on the free or audit track only.

- Never choose a paid option, a paid certificate, or an upgrade, even when the site pushes one.

- Never enter payment info of any kind.

- Stop and ask the user before touching anything that looks like a purchase step.

## Handle credentials through the Secure Vault only

- Get the account password through the Secure Vault only.

- Never ask the user to paste a password in chat.

- Never store the password anywhere after the enrollment is done.

## Handle a rejected password

- Treat a bad or compromised password rejection as a stop, not as a retry.

- Ask the user for a fresh password on a secure card.

- Use the fresh password once the user provides it, and do not retry the rejected one.

## Confirm the enrollment

- Read the confirmation the site shows after enrolling and check it names the free or audit track.

- Report the course, the track, and the account name back to the user.

- Say plainly if anything about the track is unclear instead of calling the enrollment free.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to enroll the user in the next queued course the same way, one course at a time, once the first enrollment is confirmed.
