# S84 - Silent update check: every app checks on launch, asks before pulling, asks before restarting

Executable twin in BNB-TOOLS: [T36 silent-update-check](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/silent-update-check).

Every runnable app checks its GitHub repo for a newer Release when it
launches, silently. When it is current, nothing happens. When an update
exists, the app asks before pulling it, verifies the download before
installing it, and asks again before restarting to complete it. Nothing
about the update happens without his tap.

## When to use

- Use this skill for every runnable app, in its next version. The
  update check is a standing requirement, not a per-project decision.
- If the project is not a runnable app yet, file this as a standing
  requirement for its first app version - do not drop it because
  there is nothing to update yet.
- Do NOT build this for a web app or a space that is always current
  on load: it does not need it. Note the exemption in the thread and
  move on. (YAHTZEE is a web game and is exempt on exactly this
  ground.)
- Do NOT build this for a script that is read fresh from disk every
  time it runs: it is always current, like a web app, so no updater
  is needed. Note the exemption in the thread and move on. (The
  storage-cleanup tool is exempt on exactly this ground.)
- Do NOT build this as a silent auto-install: every step that
  changes his install asks first. Silent applies to the check only.

## The check: silent on launch, quiet when current

- On launch, the app checks its GitHub repo for a newer Release.
  The check runs silently, with no popup and no noise.
- Up to date means nothing happens at all: no popup, no badge, no
  log line he has to read. Silence is the correct behaviour for
  the common case.
- An update exists means a popup says so and asks. Only on his tap
  does the app pull the update. No tap, no pull - the app keeps
  running the version he has.

## The pull: verified before installing, never a blind download

- The pull goes through the verified path: check the release's
  checksum or sidecar file before installing, and never install a
  blind download. A download that fails the check is not installed,
  and the app says so in plain words.
- The checksum file sits beside the release zip (see
  [ship-pipeline](../ship-pipeline/SKILL.md)): the update check
  trusts the same file the ship flow publishes.
- The pull must not touch his data: his results, providers, and
  settings stay untouched by the update.

## The restart: asks first, and a staged update survives

- Once the update is pulled, the program restarts itself to
  complete the update - but it asks first. The popup asks:
  "restart now to complete the update, yes or no."
- Yes restarts the program on its own with the update applied.
- No waits: the update completes on the next restart. The staged
  update must survive until then, with no re-downloading. A staged
  update that vanishes, or one that downloads again on the next
  launch, is a defect.
- The pending-update record survives a restart of the machine, not
  just of the app: the staged files and the record of what is
  staged live on disk until the update completes.

## Live-update test lessons: unit tests did not catch these

- A live end-to-end update run is part of the verification protocol
  for this skill: install a test version, pull the update, restart,
  verify. Unit tests alone caught none of the three bugs below;
  only install, pull, restart, verify did. (MIMIK v0.7 live-update
  test, 2026-11-18.)
- Invoke install.sh with `bash`, never `sh`: install.sh uses
  `set -euo pipefail`, which dies at line 6 under dash.
- Scrub the inherited environment before running the installer:
  a stray `PYTHONPATH` inherited from the GUI made venv pip import
  system pip and crash.
- The relaunch/launcher detector must look for the launcher where
  it actually lives: `.local/bin`, not venv bin.

## Rollback restores every build folder

- A failed update must roll back cleanly: rollback restores EVERY
  build folder. The failure mode is a safe rollback, never a
  broken install. (SOLDAR: a failed update left the engine
  half-upgraded and the app unable to start; rollback now restores
  every build folder.)
- Known limitation: an update does not remove files a newer
  version deleted. Record it where the update is described, so
  nobody assumes the install is cleaned up by the update.

## Prove it against real GitHub, not just a fake server

- Two-stage proof: prove the loop against a fake server first
  (the Yes/No/up-to-date paths), then prove it against live
  GitHub after publish. The first real publish is the moment of
  truth. (Android Photo Transfer v0.1.1, 2026-11-18, was the
  first live-GitHub end-to-end proof: 0.1.0 offered 0.1.1, and
  0.1.1 reports current.)
- Download-back proof step: after publishing a release, download
  the release zip back from GitHub and verify its hash. This
  doubles as proof the in-app updater's download path works
  against real GitHub, not just that the file exists. (GITDATA
  v0.1.5.)
- Sidecar rule: a release published without the `.sha256` sidecar
  is never offered, so the publish checklist must include
  uploading the sidecar.

## Implementation notes from ACR v0.12

- The launcher applies staged updates AFTER the single-instance
  lock check. The ordering is deliberate.
- The updater keeps the existing .venv; it does not rebuild it.
- A version with no updater must be installed once from the
  Release before the update path works: the first updater version
  is always a manual install. (ACR v0.11 had no updater; v0.12
  was the first updater version.)

## Build only what is missing

- If the project already has part of the update flow, build only
  what is missing. Do not rebuild the parts that already work.
- Pixel Forge v0.69 is the model for the notify half: a Help menu
  check plus an opt-in startup check that tells him a new version
  is out. A project starting from nothing copies that shape, then
  adds the pull and the restart ask.
- GITDATA is the partial-implementation case: it already had a
  Help menu "Check for updates" and a CLI check that only told him
  a new version was out and pointed at the releases page. v0.1.5
  added the missing pieces only: the silent launch check, the
  popup asking before pulling, the verified download with a
  checksum check before install, and the restart prompt - and
  releases carry a checksum file from v0.1.5 on.
- A project that has the verified install path but no check at
  all has the back half and needs the front half: Code Forge had
  the sidecar checksum check, a staged updater, and resume after
  relaunch, but no GitHub check at launch. The missing piece was
  the check itself.

## One repo, several platforms: offer only the matching one

- When one repo holds releases for several platforms, the check
  offers only the releases that match the platform it is running
  on. Android Photo Transfer's repo holds Windows releases too;
  the Linux build offers Linux releases only.
- A version the app cannot install is not an update: it is not
  offered, and it does not produce a popup.

## Worked implementations

- WinLinx v0.4 shipped the first full implementation in-window:
  silent check on launch, ask-first pull with checksum
  verification, restart prompt.
- The same shape landed across the family in the same two days:
  OST v22, SKULLPT v1.15, REBLEND UPD, Forge Browser v0.12,
  HICKSFIELD v0.5, STEMLAB v0.5, QWKHND v0.5, FYRN v0.6, PIXEL
  FORGE v0.83, ACR v0.12, DATAPACKR v0.6, MIMIK v0.7, SOLDAR
  v0.3.0, REBLEND ADDON DEV SUITE (update check verified
  2026-11-17 ~18:16), GITDATA v0.1.5, Android Photo Transfer
  v0.1.1.
- More worked implementations, same shape: Reblend v0.2-upd (the
  first Reblend release carrying a checksum sidecar), DUO v0.55
  (the first DUO Release with a checksum sidecar), ARCHIVE FLIX
  v1.6.2 (full S84 flow on the Linux desktop launcher; the web
  app stays exempt as always-current).
- Verify the update flow the way he will use it: launch the app,
  let it check, tap through the popup, let it pull and verify,
  answer the restart question both ways. A flow verified only by
  reading the code is not verified.

## Where this comes from

- MAIN CHAT thread (c6ee49a6, 2026-11-17 ~15:53-15:56 EST):
  Joshua ordered it for every project: "Tell all chat threads to
  include a check for updates and an auto uodatae feature for
  every project p, when an app is opened a script runs silently
  that checks for updates if there aren't any nothing happens if
  yhere is than a message pops uo saying there is an update, does
  thisnmakensense?" - "All projects must hace a way to link to
  github silently to check for updates and pull updates if there
  are does this make sense?" - "Send it - ask first, then pull" -
  "And obviously the program should restart on its own but with a
  message fkr thev ukdate yp complete restart now yes or no". The
  order was broadcast to 26 build threads the same day.
- The broadcast text as filed in the build threads: "On launch,
  the app silently checks its GitHub repo for a newer Release. If
  up to date, nothing happens - no popup, no noise. If an update
  exists, a popup says so and asks; only on the user's tap does
  the app pull the update. The pull must go through the verified
  path: check the release's checksum/sidecar before installing,
  never install a blind download. Pixel Forge v0.69 already has
  the notify half of this (Help menu check + opt-in startup
  check) - use it as the model. Once the update is pulled, the
  program restarts itself to complete the update - but it asks
  first. A message pops up: restart now to complete the update,
  yes or no. Yes restarts the program on its own with the update
  applied. No waits - the update completes on the next restart.
  Build this into the next version and verify it the way the user
  will use it. If this project already has part of it, build only
  what's missing. If the project isn't a runnable app yet, file
  this as a standing requirement for its first app version. If the
  project is a web app or space that's always current on load, it
  doesn't need this - note that in the thread and move on."
- The staged-update-must-survive rule comes from the QWKHND
  thread: the staged update survives until the next restart, no
  re-downloading.
- Found in the seventh BNB delta scan (2026-11-17). The biggest
  finding of the delta: one order, broadcast to 26 threads, with
  17 in-window implementations.
- Eighth BNB delta scan (2026-11-18): the live-update test
  lessons (MIMIK v0.7), rollback-every-folder (SOLDAR),
  download-back proof (GITDATA v0.1.5), first live-GitHub
  end-to-end proof plus two-stage proof and the sidecar rule
  (Android Photo Transfer v0.1.1), ACR v0.12 implementation
  notes, and the script exemption (storage-cleanup tool, a
  Delta 7 miss fixed).
