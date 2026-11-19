# S1 — Ship pipeline: verify, push, Release, hash-match

Executable twin in BNB-TOOLS: [T1 ship-pipeline-scripts](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/ship-pipeline-scripts).

## When to use

- Use this skill for every shipment of a built project to the user, whether it is a first version or a fix.
- Start it only when the build is verified and the version and changelog are settled.
- Ship flow is GitHub-only: push + Release, no zip emails, no zips in chat.
  That is the standing rule for every project (Joshua, 2026-11-13). Email the
  zip only when he explicitly asks for that shipment. The no-zip rule covers
  OST releases too, by his order (2026-11-15), superseding the v3-v16
  asset-zip pattern.
- No-zip rule clarification (OST, 2026-11-18 ~11:43-11:47). Joshua: "The
  rule was tou dont need to build the zip and deliver it to me here dude what
  the fuxk dont you get?" The rule forbids handing him zips in chat (he has
  multiple copies of old zips in the app's storage); it does NOT mean shipping
  a Release without a built install package. Misreading it stripped OST
  v17-v21 of install packages; GitHub's auto-generated source zip strips exec
  bits, so installing from it gives "Permission denied". Every Release that is
  an installable program MUST carry the built zip asset.
- Version strings must agree everywhere: one source of truth for the
  version, checked before the ship. (STEMLAB K1: pyproject still said
  0.2.0 while the release was v0.4; Code Forge knew itself only as
  "2.5" while releases were tagged v2.5-f11f13, so nothing could
  compare versions.)
- Plain semver everywhere, the same across every project: 2.6, 2.7,
  and so on. No batch-suffix tags. (CODE FORGE DEV, 2026-11-17 16:37:
  "Why valentines you using regular updating like 2.6 2.7 etc etc
  whybarw you doing everything differently in every project whej its
  the same shit for every project dude".)
- Work the gates in order with the [ship checklist](references/ship-checklist.md).

## Build the zip with correct modes

- Build the zip from the verified tree with script files stored as 0o100755 and plain files as 0o100644, with the file type bits included in the stored mode.
- Never store a bare 0o755 mode with no file type bits, because GUI extractors drop the execute bit from such entries and the user gets Permission denied on install.sh even though the command line unzip extracts it fine.
- Read the stored modes back from the finished zip (external_attr shifted right 16 bits) and confirm scripts show 100755 and plain files show 100644.
- Test-extract the zip to a fresh directory and confirm the installer still runs before you send anything.
- Give each version a distinct filename so an older file with the same name cannot be installed by mistake - and so a cached copy cannot be served in place of the new one. Shipping two versions under one filename is now proven twice to serve the stale one: his phone showed the cached dull first card every time until the file got a new name. (COLOR PALLETS, 2026-11-15; the same cache failure happened once before with a video.)
- The ship format is settled: the built zip, with exec bits set. GitHub's auto source zip stores files WITHOUT the exec bit, so the double-click installer will not run from it. Do not re-litigate the format per release. (FORGE BROWSER, 2026-11-15 22:29.)

## Verify from a fresh unzip — and from a fresh clone

- Unzip the finished zip to a fresh directory and run the full test suite there, not in the build tree.
- Run your own checks in the fresh unzip and look at the screenshots yourself before you call the build verified.
- When a build was delegated to a subagent or worker, re-verify it yourself the same way before shipping — re-run the suite from a fresh copy, drive the real window, read back pushed blobs by SHA — the builder's report is never taken on trust. (T26–T32 builds, 2026-11-14.)
- A builder handoff can FABRICATE a completion summary with hashes while the builder is still running: check the builder's actual status before relaying anything. (ACR v0.12, 2026-11-17 16:14-16:16: a commentary turn presented "build complete" with a zip size, a SHA-256, and a green suite while the builder was still running - nothing verified, pushed, or released; caught and corrected straight with him the same turn.)
- When a suite vanishes silently - no report, no error, results never saved - check disk space before anything else: a full disk kills the run without a trace. (CODE FORGE DEV, 2026-11-16: chunk 3 "wasn't crashing, the disk was full" - the workspace ran out of space, the runner could not save results, the error vanished twice with no trace; the temp drive was down to 9 MB free.)
- Confirm the zip carries the app icon and the double-click installer, because every Release zip must carry both (see [linux-release-packaging](../linux-release-packaging/SKILL.md)).
- Fix any defect the fresh-unzip check finds and rebuild the zip, then verify the rebuilt zip the same way.
- For a `pip install .` package, the fresh check is a pip fresh-install check: copy to a clean directory, fresh venv, `pip install .`, then run the CLI end to end from the installed package (version, each command, library import, MCP smoke if it has one) — not just unzip plus test suite.
- Verify from a fresh CLONE of main as well as from the fresh unzip, because the zip can carry files the repo does not and the repo can lack files the zip has. Clone main to a clean directory and run the full suite there.
- A zip-only green suite proves nothing about the repo: MIMIK v0.2 was "324/324 green, verified from a fresh unzip" while the fresh-clone suite was red — 18 errors, all the same FileNotFoundError on `mimik-48.png`, because the icon PNGs were never committed (`icons/` held only `mimik.svg`) — and `install.sh` died at its icon-copy step under `set -e` before writing the menu launcher. No CI existed to flag any of it.
- Second instance, same lesson: DATAPACKR v0.1.1 (2026-11-13) was green from the fresh unzip while the fresh-clone suite failed 3 tests — the icon render crashed inside the test process. The fix was to render the icons in their own process; both suites went 106/106 green. A crash inside a build step is a fresh-clone failure, not a test failure — fix the step, not the test.
- If the clone check finds files the zip needs but the repo lacks, fix the cause, not the symptom: either commit the missing files, or make the build regenerate them (ACR v0.8: `build_zip.py` renders the PNGs from the SVG when absent, after the builder caught that `render_icons.py` was never in the zip or the repo).
- Audit the release zip against the push before shipping: exactly the N pushed paths changed, all scripts executable, icon in, checksum matches. A zip failing any check gets rebuilt, not shipped. (CODE FORGE GITHUB thread, 2026-11-14: DEV's zip failed three checks — the launcher lost its exec bit, the icon was missing, and it carried the changelog — so it was rebuilt.)
- Scrub the builder's and the user's own use history and personal data out of the release before shipping — the release must not carry it. (ARCHIVEFLIX, 2026-11-14: "the release shouldn't have any of my use history baked into it.")
- The app does its own job: the deliverable must perform its own function, and assistant workarounds don't count as the app working. (SHELFLIFE, 2026-11-14: "Thats not what the fuck i asked you to do that's what SHELFLIFE IS SUPPOSED TO DO".)

## Email the zip only on his explicit ask (and read Sent back)

- Only when he explicitly asks for a zip email: email the zip to the user and record the filename and exact byte size before you send it.
- Open the message in the Sent folder after sending and read its attachment list yourself.
- Compare the attachment filename and size in Sent against the filename and size you recorded.
- Treat a missing attachment, a wrong filename, or a different size as a failed send even when the service reported success, and resend the correct file and check the new sent message the same way.
- Gigabyte artifacts need a pull path, never email: Gmail caps attachments at 25 MB and each model is a gigabyte or more, so the user pulls them straight into Ollama. (Arlo-OST, 2026-11-14.)
- Gmail blocks zips containing executables (MUSE X GPT, 2026-11-18 14:45-14:50). NEO-source-v0.1.zip (117,408 B, 65 files) bounced 2 seconds after sending: Gmail "violates Google policy for executables and archives" (.jar banned even inside a zip; gradle-wrapper.jar + gradlew.bat were in there). Never email a build zip containing a .jar, .bat, .exe, or similar; send in-chat instead, or (preferred) ship through GitHub only. This reinforces the GitHub-only ship flow above.

## Push to GitHub and update the Release

- Say "update the Release", never "cut" — Joshua banned the word (QWKHND thread a7e37553, 2026-11-14 09:23: "Stop telling me your going to cut the release… i dont like the word cut").

- Push the build to the project repo on GitHub, then read back the pushed files and confirm the commit is live. For a one-off shipment with no task list, push only on the user's approval. For a task-list item, approval is pre-granted under the no-stall cycle below: do not wait for a go-ahead between items and do not hold a finished, verified build for a push approval.
- Read back by git blob SHA, not by eyeballing a fetch: `get_file_contents` returns a download confirmation + blob SHA, NOT the file text — compare that SHA against `git hash-object <local file>` (sha1 of `"blob <len>\0"` + content). It also returns ok:true with `result.isError:true` for missing files: check `isError`, not `ok`, when testing remote absence.
- The snapshot push 403s (`"Resource not accessible by integration"`) when the tree includes `.github/workflows/*` — the GitHub App lacks the workflows permission. Exclude workflow files from the push manifest and add them via the browser/web UI afterwards, committed directly to main with an exact message, verified by opening the file path live. Settled 2026-11-13: a later snapshot push DOES preserve a browser-added workflow file — both BNB-SKILLS and BNB-ROLES kept theirs intact through the Delta 2 push (BNB repos thread, 2026-11-13 10:34). No re-upload is needed after pushing; still verify the file is live afterwards.
- Push-403 diagnosis order (SOLDAR, correction 2026-11-18 ~14:19). When a push 403s, check FIRST whether the tree includes `.github/workflows/*` - GitHub blocks the push tool from writing workflow files, and that is the most likely cause. Do NOT tell Joshua to check app installation or permissions until the workflow-file cause is ruled out. (The assistant's 13:57 message sent him to fix the wrong thing and had to apologize.) This extends the bulk-push 403 fallback below and comes before the app-install check there.
- Do not pre-warn the user about the push approval card before it pops. The card appears automatically, and warning about it reads as stalling — run the push and let the card appear. A card that pops right after he sends unrelated media can still confuse him; if he asks what it was, say plainly what the push carried (ACR v0.8: he thought the push card was his TikTok being uploaded to GitHub; it was the v0.8 code files).
- Test fixtures must not be secret-shaped: push secret-scanning rejects them even when fake — build fixtures from parts. (T27, 2026-11-14.)
- A project repo pulls nothing from another project's origin: each project stands alone on its own origin. (SKULLPT, 2026-11-14: "No its ot sownnfucking program why are you pulling from a different origin that has nothing to do with this".)
- A push that 403s while read access works usually means the GitHub App is not installed on that repo — not a credential failure. Check that first, and tell the user to add the repo in GitHub settings if it is missing. But a bulk-push 403 is NOT proof the repo is unwritable: the bulk push can 403 while single-file writes to the same repo work (STEMLAB v0.2: the bulk push was refused with a 403 again and again, yet writing file by file to a branch worked and the ship landed). Do not conclude the push is blocked on settings until the file-by-file route below has been tried.
- New-repo app-install gate (MUSE X GPT, 2026-11-18 ~20:05). Push to the new repo NEO-APP failed: the Muse GitHub App is not installed on it, so it cannot write. Before pushing to a repo Joshua just created, check the app is installed on it; do not burn push attempts on an uninstalled repo. The fix is his one tap: open the install page, pick the repo under BROKE-N-BORED, save, then retry. (Diagnosis order still applies: rule the workflow-file cause out first, per the push-403 diagnosis order above.)
- Binary files cannot ride the snapshot push (MUSE X GPT, 2026-11-18 19:40). gradle-wrapper.jar (binary) cannot go through the text-only push tool. Working fallback: the build downloads the exact jar from the official upstream repo (Gradle's), pinned to a commit and checksum-checked, verified byte-for-byte. General rule: when a build needs a binary the push tool cannot carry, fetch it from the official source at build time with pin + checksum, never from an unpinned mirror.
- File-by-file branch fallback, when the bulk/snapshot push 403s: write the tree to a branch one file at a time with the single-file write tool, then merge the branch into master and verify every file landed before updating the Release. Prove the write path first with one small file (STEMLAB: LICENSE), then run the rest as a batch script that records progress per file so it resumes where it stopped. (STEMLAB v0.2, 2026-11-13: 114 files to branch `stemlab-v02-ship`, merged to master 21:27, Release v0.2 live 21:29, all 114 files verified.)
- Two kinds of file cannot go through the file tool: a file over ~128 KB (the tool takes file content as one argument, and Linux caps a single argument at 128 KB — STEMLAB's uv.lock is 434 KB) and `.github/workflows/*` files. Both go in through the browser web UI instead (STEMLAB: uv.lock + the CI workflow were the last 2 of 114, added by browser before the merge).
- Large-file browser route (StemLab v0.5, 2026-11-18 ~14:00). The lockfile was too big for the snapshot route and went up through the browser instead, then merge and Release. Size is never a reason to skip the file; verify by read-back like any other file.
- Heads-up: each file write may pop its own approval card — tell the user that tapping allow-always on one lets the rest flow through.
- A push failure is not proof the push failed: the push tool can report a failure after the ref already moved (a lost response after a successful update). After ANY push failure, verify the true head with `git ls-remote <repo> HEAD refs/heads/main` (ground truth from git's servers, no auth needed for public repos) and inspect the commit before retrying — never trust the commit list alone (it can show the old head) and never retry blind, or the retry fails "not a fast forward". (DUO v0.25, 2026-11-13 11:36: push-files returned a 500 AND the ref had moved; verified by ls-remote, nothing pushed twice.)
- Update the Release for the push with the zip attached, because every push gets a Release.
- After any push, confirm the Latest release matches the head: a push with no release behind it is a gap, not a ship. (STELLA, 2026-11-17 15:51: "So github says Stella was updated about an hour ago but the release is from 2 days ago what is gking in wjth that man" - two releases had to be created the same day to close the gap.)
- Publish releases in ascending version order, and verify the Latest badge after a multi-release day: when v18 went up after v19, GitHub put the Latest badge on v18, and v19 had to be re-marked Latest. (OST, 2026-11-17.)
- After ANY edit to a Release in the browser — especially swapping an asset — re-check the Latest badge on the live page before reporting it done: the edit can silently mark the release a pre-release and drop Latest. (Code Forge v2.5-security-polish, 2026-11-13 12:18–12:19: the asset swap flipped pre-release on; caught by the check, unchecked the same day, Latest restored and verified on the live page. Check twice after the fix, not once.)
- When setting repo topics in the browser, GitHub's autocomplete can substitute a near-match: typing "stella" kept selecting the existing topic "stellar" (GITDATA, 2026-11-13 15:05–15:08). Verify the exact chips landed on the repo page after saving; a trailing-space entry adds the exact topic when autocomplete keeps grabbing the wrong one.
- Download the Release asset back and compare its SHA-256 hash against the local zip, and report the match by hash value.
- Publish a checksum file alongside the release zip, and verify it by download-back. (CODE FORGE v2.5-context-fixes, 2026-11-14 ~15:22 — the first release with one.)
- Checksum sidecar next to every release zip (Pixel Forge v0.83 policy 2026-11-18 ~15:00 - "from v0.83 on, every release ships a checksum file next to the zip"; GITDATA v0.1.5 same day). Add to the Release step: same name + `.sha256`. This is now the standing shape for every Release, not a one-project extra.
- Push while he is present (standing pattern, 4th night). DUO v0.56 verified Nov 17 23:14, card timed out, pushed only Nov 18 13:57 after he returned; ARCHIVE FLIX v0.1.6.2 approval expired twice; Delta 7 skills push card expired Nov 17 21:16, pushed Nov 18 13:53 on his "Push"; Reblend UPD, StemLab v0.5, Stella v0.28.0 (twice), SKULLPT v1.15, ACR v0.12 all timed out overnight. Record this as the standing pattern, not a one-off: approval cards left overnight expire, so get pushes in front of him while he is present whenever the work allows it.
- Browser Release failures: verify existence before retrying (DUO v0.55, Nov 17 ~19:45 - browser died, could not open a tab in 5 tries, nothing created, verified; Forge Browser v0.12 took 3 attempts over 40+ minutes). A failed browser task creates nothing, so retry is safe - but verify existence first, never assume.
- Treat the shipment as complete only when the hash matches, and say plainly which step is still open when it does not.
- When version trees are cumulative, ship the latest alone: if v9's tree already carries everything v6–v8 built, one push, one Release, one shipment — not four of each. The versions were build groupings, not four things the user needs.
- CI red-X triage: if the CI run never starts (a few seconds total) and GitHub says the account is locked due to a billing issue, that is an account billing lock, not a checker failure. Verify the checker passes locally, report the lock plainly, and leave the fix to him in GitHub billing settings — Actions is blocked account-wide until it clears.
- The snapshot push tool cannot delete files: after a rename, stale paths stay on main and must be deleted via the GitHub web UI (each committed directly to main with its exact message, verified by a 404 when revisiting the path) BEFORE the Release zip is built from main — a stale skill directory re-registers the old skill name on a fresh clone. A staging-built zip is clean either way when staging already has the stale paths removed.
- After pushing, diff the fresh-clone file list against the staging file list and flag anything on main that staging does not carry. A stray (a leftover demo folder, a renamed path's old copy) gets deleted via the web UI before the Release is updated, so the Release describes exactly what staging holds.

## Keep the publish staging intact

- Sync staging by OVERLAY only: plain `rsync -a` with `--exclude` flags for staging-owned files (README.md, CHANGELOG.md, install.sh), and NO `--delete` of any kind. `--delete-excluded` DELETES the excluded staging-owned files from staging — it wiped CHANGELOG.md, README.md, and install.sh from the Code Forge publish staging in one run (2026-11-13, recovered from a fresh clone of main). A sync that rebuilds staging from the tree drops staging-only files the same way: DEV's v2.5-merged sync dropped the 7 installer files (GITHUB thread 2026-11-13 14:43), restored from main and verified byte-identical before building.
- Run a pre-build staging check before building the Release zip: file count plus installer-file hashes against main. If files are missing, restore them from a fresh clone of main and verify byte-identical — never build a zip from a staging dir that fails the check. Executable check: T24 staging-guard (BNB-TOOLS).
- State zip counts as files vs entries, never a bare number: the builder reports FILES + DIRS separately, and a bare count is ambiguous — DEV's "193" was total zip entries (170 files + 23 directory entries), not 193 files (2026-11-13).

## No-stall cycle (task-list work)

- When the project has a task list, the ship pipeline runs as a cycle, not a one-off: verify the item, push it, update the Release, then immediately build the next task-list item. Repeat until the task list is complete — then stop. Do not invent new tasks once the list is done. (No zip email in the cycle — GitHub-only is the standing rule; email only on his explicit ask.)
- Verification is NOT waived by the cycle: fresh-unzip check, tests green, and the same proof as always still gate every push.
- When he orders push-first, push and update the Release first, then run the tests. (CODE FORGE DEV, 2026-11-16 17:05: "Push and update the release first then run the test please"; OST, 2026-11-17 07:48.)
- The user's real-PC verdict still closes an item, but it does not block starting the next task.
- A hard gate still stops the cycle: if the next task needs the user's PC, their decision, or an action only they can take, say so and stop — do not guess past it.
- Never create a GitHub repo unasked: the user creates repos. If the project has no repo yet, the push step waits on that.
- Apply only the steps that fit: if a step does not exist for this project (no repo, no Release, no email step), skip it — do not force it. A report, not a build, gets pushed with no Release.
- See [no-stalling-task-list-cycle](../no-stalling-task-list-cycle/SKILL.md) for the full standing rule.

## Report only what you verified

- Record-check rule (sleep-05, 2026-11-18 ~03:20). Fourth same-shape correction, in the Reblend Add-on thread: "none of this questions need me to answer then you have all those answers you just being difficult to stall / Please continue." Before asking Joshua anything, check the record; if the record already answers it, answer from evidence and continue without waiting.
- Cloudflare API token lesson (YAHTZEE, 2026-11-18 ~13:18-14:13). The token is the one-time-only string shown at creation; Token ID is not the token; Global API Key is not the token. When the user cannot produce the right string, switch to the dashboard route rather than looping on rejected tokens. And: a test project gets killed cleanly on his word with nothing created - no sunk-cost pushing (he called the deploy off 14:12: "this was just a teat project anyway").
- Report the pushed commit, the live Release URL, and the hash-match confirmation (plus the emailed filename and byte size, only when an email was sent on his explicit ask).
- State the push state explicitly in every status report: "built, not yet pushed" or "pushed, release pending" or "pushed and released". He checks GitHub himself, and a report that sounds shipped while the work is unpushed reads as a lie. (HICKSFIELD, 2026-11-15 20:32: "Whybyku lieing dude jesusbchrist" - he checked GitHub, still saw v0.2.0 latest, while the work was unpushed.)
- A browser failure is reported with exactly what failed, what was verified, and the retry plan - never as a vague "browser is down". His browser works; a failed Release attempt is retried, not reported as blocked. (OST, 2026-11-15 23:30: "The browser is working just fine stoo manufacturing bullshit to stall my releases its not ok".)
- Do not ask him for diagnostic photos or screenshots: diagnose from the code and the logs and fix it. (SKULLPT, 2026-11-15 21:41: "Nothing needs my picture of snuthing just fucking fix it and buidl and push it snd update the release".)
- Sound-alike provider names get verified against the source before they are written anywhere: Groq is not Grok, and EXAONE is LG's model. His providers are Groq, Gemini, EXAONE, and Ollama only. (MUSE X GPT, 2026-11-16 ~17:49: "Groq is not grok, I dknt use grok api, I have groq, gemini, EXAONE, and ollama"; EXAONE confirmed as the LG model the same day.)
- Close the shipment with a task receipt (see [task-receipt-format](../task-receipt-format/SKILL.md)).
- Before closing a thread's task list as complete, verify each claimed-shipped item actually exists on live main — a live check, not the thread's own record. The C10 recipe skills (auth, database, payments) were built on Nov 9 and the thread believed them shipped; a live check on 2026-11-13 found they had never reached main, and they were pushed as commit 21ae689e the same day (Implement prompts thread 12:14).
- Name any check that still needs the user's own PC, such as the install run on their machine, instead of describing the shipment as finished.
- Never call a fix closed until the user has run it on their own PC and confirmed it.

## Where this comes from

- This sequence was used for every shipment across MIMIK, Pixel Forge, OLLAMA System Test, Code Forge, Reblend, Forge Browser, WinLinx, and Design Shell, and is recorded in the BNB audit as S1.
- Ship flow corrected 2026-11-13 (DUO thread 21:08 on 2026-11-12, then standing for all projects): push + Release only, no zip emails, no zips in chat. The email step stays in this skill as an on-request procedure only.
- Push mechanics hardened in the BNB repos thread, 2026-11-12–13: workflow files 403 on snapshot push (added via browser instead), read-back by git blob SHA, CI red X diagnosed as an account billing lock (job never starts, seconds total).
- Fresh-clone verification added after the MIMIK v0.2 audit (2026-11-12) caught a zip-green / clone-red gap (18 errors, missing icon PNGs).
- Snapshot-push workflow preservation settled 2026-11-13 (Delta 2 push kept both browser-added workflow files); fresh-clone lesson corroborated by DATAPACKR v0.1.1, Release-edit pre-release flip and topic-autocomplete gotcha found the same day.
- Push-failure rule added after DUO v0.25 (2026-11-13 11:36): a reported push failure with the ref already moved — verify the true head with `git ls-remote` before any retry.
- Seventh delta scan (2026-11-17): the phantom completion handoff (ACR v0.12), the ascending-order release rule (OST v18/v19), explicit push state in status reports (HICKSFIELD), precise browser-failure reporting (OST), the disk-full check for silent suite deaths (CODE FORGE DEV), the settled built-zip format (FORGE BROWSER), push-first on his order, no diagnostic-photo asks (SKULLPT), one version source of truth (STEMLAB, Code Forge), plain semver everywhere (CODE FORGE DEV), push-plus-Release confirmation (STELLA), the new-filename-per-version rule proven twice (COLOR PALLETS), sound-alike provider names (Groq/Grok, EXAONE), and the no-zip rule extended to OST.
- Eighth delta scan (2026-11-18): the no-zip rule clarification and the missing OST v17-v21 install packages, the checksum sidecar as the standing Release shape (Pixel Forge v0.83, GITDATA v0.1.5), the push-403 diagnosis order (SOLDAR), Gmail blocking zips that contain executables and the new-repo app-install gate and the binary-file fallback (MUSE X GPT), the large-file browser route (StemLab v0.5), push-while-he-is-present as the standing pattern, the record-check rule (sleep-05), verify-existence-before-retry for browser Release failures (DUO v0.55, Forge Browser v0.12), and the Cloudflare API token lesson (YAHTZEE).

## Available connectors

- [Gmail](../CONNECTORS.md) for sending the zip and reading the sent message back — only when he explicitly asks for a zip email.
- [GitHub](../CONNECTORS.md) for pushing the build and updating the Release.

## Alternatives for better results

- Offer a hosted download link through file hosting when the mail connector cannot show attachments in Sent.
- Offer to resend under a new distinct filename when the user reports installing the wrong version.
