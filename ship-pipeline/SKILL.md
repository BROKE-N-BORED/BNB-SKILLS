# Ship pipeline: verify, email, push, Release, hash-match

## When to use

- Use this skill for every shipment of a built project to the user, whether it is a first version or a fix.
- Start it only when the build is verified and the version and changelog are settled.
- Skip the email step only when the user has said that a project ships by push and Release only.

## Build the zip with correct modes

- Build the zip from the verified tree with script files stored as 0o100755 and plain files as 0o100644, with the file type bits included in the stored mode.
- Never store a bare 0o755 mode with no file type bits, because GUI extractors drop the execute bit from such entries and the user gets Permission denied on install.sh even though the command line unzip extracts it fine.
- Read the stored modes back from the finished zip (external_attr shifted right 16 bits) and confirm scripts show 100755 and plain files show 100644.
- Test-extract the zip to a fresh directory and confirm the installer still runs before you send anything.
- Give each version a distinct filename so an older file with the same name cannot be installed by mistake.

## Verify from a fresh unzip

- Unzip the finished zip to a fresh directory and run the full test suite there, not in the build tree.
- Run your own checks in the fresh unzip and look at the screenshots yourself before you call the build verified.
- Confirm the zip carries the app icon and the double-click installer, because every Release zip must carry both (see linux-release-packaging).
- Fix any defect the fresh-unzip check finds and rebuild the zip, then verify the rebuilt zip the same way.

## Email the zip and read Sent back

- Email the zip to the user and record the filename and exact byte size before you send it.
- Open the message in the Sent folder after sending and read its attachment list yourself.
- Compare the attachment filename and size in Sent against the filename and size you recorded.
- Treat a missing attachment, a wrong filename, or a different size as a failed send even when the service reported success, and resend the correct file and check the new sent message the same way.

## Push to GitHub and cut the Release

- Push the build to the project repo on GitHub only on the user's approval, then read back the pushed files and confirm the commit is live.
- Cut a Release for the push with the zip attached, because every push gets a Release.
- Download the Release asset back and compare its SHA-256 hash against the local zip, and report the match by hash value.
- Treat the shipment as complete only when the hash matches, and say plainly which step is still open when it does not.

## Report only what you verified

- Report the emailed filename and byte size, the pushed commit, the live Release URL, and the hash-match confirmation.
- Close the shipment with a task receipt (see task-receipt-format).
- Name any check that still needs the user's own PC, such as the install run on their machine, instead of describing the shipment as finished.
- Never call a fix closed until the user has run it on their own PC and confirmed it.

## Where this comes from

- This sequence was used for every shipment across MIMIK, Pixel Forge, OLLAMA System Test, Code Forge, Reblend, Forge Browser, WinLinx, and Design Shell, and is recorded in the BNB audit as S1.

## Available connectors

- [Gmail](/opt/hatch/connectors/gmail/CONNECTOR.md) for sending the zip and reading the sent message back.
- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for pushing the build and cutting the Release.
- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer a hosted download link through file hosting when the mail connector cannot show attachments in Sent.
- Offer to resend under a new distinct filename when the user reports installing the wrong version.
