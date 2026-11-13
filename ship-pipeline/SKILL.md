# S1 — Ship pipeline: verify, email, push, Release, hash-match

Executable twin in BNB-TOOLS: [T1 ship-pipeline-scripts](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/ship-pipeline-scripts).

## When to use

- Use this skill for every shipment of a built project to the user, whether it is a first version or a fix.
- Start it only when the build is verified and the version and changelog are settled.
- Skip the email step only when the user has said that a project ships by push and Release only.
- Work the gates in order with the [ship checklist](references/ship-checklist.md).

## Build the zip with correct modes

- Build the zip from the verified tree with script files stored as 0o100755 and plain files as 0o100644, with the file type bits included in the stored mode.
- Never store a bare 0o755 mode with no file type bits, because GUI extractors drop the execute bit from such entries and the user gets Permission denied on install.sh even though the command line unzip extracts it fine.
- Read the stored modes back from the finished zip (external_attr shifted right 16 bits) and confirm scripts show 100755 and plain files show 100644.
- Test-extract the zip to a fresh directory and confirm the installer still runs before you send anything.
- Give each version a distinct filename so an older file with the same name cannot be installed by mistake.

## Verify from a fresh unzip

- Unzip the finished zip to a fresh directory and run the full test suite there, not in the build tree.
- Run your own checks in the fresh unzip and look at the screenshots yourself before you call the build verified.
- Confirm the zip carries the app icon and the double-click installer, because every Release zip must carry both (see [linux-release-packaging](../linux-release-packaging/SKILL.md)).
- Fix any defect the fresh-unzip check finds and rebuild the zip, then verify the rebuilt zip the same way.
- For a `pip install .` package, the fresh check is a pip fresh-install check: copy to a clean directory, fresh venv, `pip install .`, then run the CLI end to end from the installed package (version, each command, library import, MCP smoke if it has one) — not just unzip plus test suite.

## Email the zip and read Sent back

- Email the zip to the user and record the filename and exact byte size before you send it.
- Open the message in the Sent folder after sending and read its attachment list yourself.
- Compare the attachment filename and size in Sent against the filename and size you recorded.
- Treat a missing attachment, a wrong filename, or a different size as a failed send even when the service reported success, and resend the correct file and check the new sent message the same way.

## Push to GitHub and cut the Release

- Push the build to the project repo on GitHub, then read back the pushed files and confirm the commit is live. For a one-off shipment with no task list, push only on the user's approval. For a task-list item, approval is pre-granted under the no-stall cycle below: do not wait for a go-ahead between items and do not hold a finished, verified build for a push approval.
- Cut a Release for the push with the zip attached, because every push gets a Release.
- Download the Release asset back and compare its SHA-256 hash against the local zip, and report the match by hash value.
- Treat the shipment as complete only when the hash matches, and say plainly which step is still open when it does not.
- The snapshot push tool cannot delete files: after a rename, stale paths stay on main and must be deleted via the GitHub web UI (each committed directly to main with its exact message, verified by a 404 when revisiting the path) BEFORE the Release zip is built from main — a stale skill directory re-registers the old skill name on a fresh clone. A staging-built zip is clean either way when staging already has the stale paths removed.

## No-stall cycle (task-list work)

- When the project has a task list, the ship pipeline runs as a cycle, not a one-off: verify the item, push it, update the Release, email the zip, then immediately build the next task-list item. Repeat until the task list is complete — then stop. Do not invent new tasks once the list is done.
- Verification is NOT waived by the cycle: fresh-unzip check, tests green, and the same proof as always still gate every push.
- The user's real-PC verdict still closes an item, but it does not block starting the next task.
- A hard gate still stops the cycle: if the next task needs the user's PC, their decision, or an action only they can take, say so and stop — do not guess past it.
- Never create a GitHub repo unasked: the user creates repos. If the project has no repo yet, the push step waits on that.
- Apply only the steps that fit: if a step does not exist for this project (no repo, no Release, no email step), skip it — do not force it. A report, not a build, gets pushed with no Release.
- See [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md) for the full standing rule.

## Report only what you verified

- Report the emailed filename and byte size, the pushed commit, the live Release URL, and the hash-match confirmation.
- Close the shipment with a task receipt (see [task-receipt-format](../task-receipt-format/SKILL.md)).
- Name any check that still needs the user's own PC, such as the install run on their machine, instead of describing the shipment as finished.
- Never call a fix closed until the user has run it on their own PC and confirmed it.

## Where this comes from

- This sequence was used for every shipment across MIMIK, Pixel Forge, OLLAMA System Test, Code Forge, Reblend, Forge Browser, WinLinx, and Design Shell, and is recorded in the BNB audit as S1.

## Available connectors

- [Gmail](../CONNECTORS.md) for sending the zip and reading the sent message back.
- [GitHub](../CONNECTORS.md) for pushing the build and cutting the Release.

## Alternatives for better results

- Offer a hosted download link through file hosting when the mail connector cannot show attachments in Sent.
- Offer to resend under a new distinct filename when the user reports installing the wrong version.
