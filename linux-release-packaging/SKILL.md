# S6 — Linux release packaging

Executable twin in BNB-TOOLS: [T6 linux-release-packager](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/linux-release-packager).

## When to use

- Use this skill to turn a project tree into a real Linux program the user can install by double-clicking, with an icon and a menu entry.
- Use it for every project that ships, and to retrofit the same packaging onto older projects that still install from a terminal.
- Build a native Linux desktop window for the app itself, never a web UI, unless the user has explicitly asked for a web UI.

## Make the icon

- Keep the icon SVG as the source of truth and render the PNG sizes from it at install time.
- Ship the prebuilt PNGs in the zip as well, so the install works even where the renderer is missing.
- Test the icon at the small sizes the desktop actually shows, and keep it readable at 16, 32, and 48 pixels.
- Render the PNGs in their own process, not inside the test or zip-build process: a render crash inside the test process fails the suite instead of the render. DATAPACKR v0.1.1 (2026-11-13 19:44): the fresh-clone suite failed 3 tests because the icon render crashed inside the test process; rendering in a subprocess fixed it (106/106 green both suites).
- The zip builder must be self-contained from a clean clone: render generated assets from source (SVG) at pack time instead of depending on gitignored files. (WINLINX: `build_zip.py` failed without the gitignored PNGs; render from the SVG before packing.)
- Icon PNGs cannot go through the snapshot push (SIMPLE APK v0.1, 2026-11-18 ~20:44-20:58). Installing from a fresh clone gets a generic menu icon (the Release zip carries icons fine). Ship an SVG fallback and/or generate icons at install time so a fresh-clone install still gets a proper icon. SIMPLE APK v0.1 shipped with the gap (SVG fix written but a machine glitch blocked test/repack); the fix follows as the next update.

## Build the GUI installer

- Ship a double-click `.desktop` installer that asks for privilege with pkexec and installs to a fixed location, with no terminal step.
- The zip alone cannot be trusted to preserve exec bits through his extractor: the installer can be in the zip at root, stored executable, and still arrive without the bit set, so double-click does nothing. The settled ship format is the built zip with exec bits set (see [ship-pipeline](../ship-pipeline/SKILL.md)); a .deb was built and verified as an alternative for Forge Browser v0.10 and then dropped per his order ("just release it as a zip dude"). Do not re-litigate the format per release. (FORGE BROWSER, 2026-11-15 15:55 + 22:29.)
- The installer detects a failed install and reports it instead of dying silently: an install that dies before launcher creation leaves an empty-square icon and no program, and nothing tells him it failed. The failure shows a plain-language error dialog with the log path. (SKULLPT N55, 2026-11-15 14:59: "the icon didnt load on the executable whej i installed it neither it stayed an empty with square witha gear".)
- Cold-start timeouts are generous on a slow PC: a 10-second plugin timeout was a real failure on a cold start, and 30 seconds was the fix. (SOLDAR Phase 2, 2026-11-15.)
- Make the installer back up an existing install before it upgrades, and ship an uninstaller alongside it.
- Uninstall menu entry (Reblend Add-on Dev Suite, Joshua-ordered 2026-11-18 02:46: "Add a menu entry for uninstall"). Every app ships an Uninstall entry in the menu next to the app; it opens the uninstall window on its own, and it must work even after the release folder is deleted (the installer ships inside the install).
- Post-export steps must be buttons (STELLA, 2026-11-18 ~20:30). The one place Stella still hands him a typed command is after an export, the `ollama create` step; it gets a button. Every step after an export (including model registration) must be a button, never a typed command.
- Filename check (STELLA, 2026-11-18 ~16:00). Training install failed because torch was saved under a mangled name (`+` turned into `%2B`), so the installer looked for a name that did not exist. Downloaded filenames must be verified against the name the installer will look for; URL-encoding must be decoded before saving.
- Missing system libraries get a GUI install path (Android Photo Transfer, 2026-11-18 20:33). If his PC is missing libmtp, the installer still tells him to run a command. Every missing dependency, including system libraries, gets a GUI install path (the way PySide6 is already handled); the installer must never hand him a command to run.
- Run install scripts with bash explicitly, never with sh, because the scripts use bash arrays and `set -euo pipefail`, and sh dies on them under dash.
- Put every dependency the app needs in the core dependencies, never in optional extras, because an optional GUI toolkit once shipped a menu icon that died silently on a missing import while the terminal stayed hidden.
- A package with no PyPI wheels must never be left to plain pip: pip will compile it from source on his PC. llama-cpp-python has no wheels on PyPI at all — a plain install always builds llama.cpp from source (gcc + cmake, 15–30 minutes on 2 cores). Pin the project's own wheel index in requirements.txt (`--extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu`) plus `--only-binary=llama-cpp-python` so pip never falls back to a source build if that index lags PyPI by a version. FYRN v0.1 shipped 2026-11-13 with the model engine installing from the ready-made wheel — no compiler, no 20-minute build on his PC.
- Verify the install works before reporting success: run a fatal check that the packages are actually present, and a warning that names the missing library when the GUI cannot start on the machine's system libraries.
- The installer is a real WINDOW, not a terminal: a Terminal=false `.desktop` launcher starts the install behind a progress window (per-step percentages), shows a success dialog that asks "Open it now?", and shows a plain-language error dialog with the log path on failure. All install output goes to `install.log` in the install folder. Probe for a dialog tool in the order xenity, zenity, yad (Cinnamon's own probe order — xenity is Mint's maintained Zenity fork and may have replaced zenity on fully-updated Mint 22.x). If no dialog tool is installed, falling back to the terminal installer is the documented degraded path, not the plan.
- The installer HEALS its own missing system prerequisites instead of printing a command for the user: when `python3 -m venv` fails because python3-venv is missing, the installer installs that one package itself with ONE pkexec call (a GUI password prompt, no terminal) and retries venv creation automatically. If the user declines the prompt or apt fails, say so in plain language ("needs one system package to install — re-run the installer and allow it when asked"). The same one-pkexec-call heal applies to build tools and /opt installs. No terminal command appears in any user-facing message, and the installer never asks the user to type anything.
- The installer creates a private `.venv` in the install folder and installs the GUI toolkit into it itself — never `--user`, never `--break-system-packages` (both wrong on Mint 3.12) — and the launcher prefers `.venv/bin/python`. Never hand the user a `pip install` command: it fails on Mint's externally-managed Python (SKULLPT v1.1 printed `pip install PySide6` as the fix for its own missing dependency; the fix did not work and the app had never opened on the target PC).
- Cap parallel work in the installer to what the machine can hold: a compile or download step that spawns one job per core can fill 8 GB and swap the whole desktop to a freeze (Pixel Forge: 4 C++ compile jobs at once froze Joshua's PC mid-install; v0.51 caps the build to 2 jobs on an 8 GB machine so the desktop stays usable). Size job counts by RAM, not just by cores, and leave headroom for the desktop itself.
- Make long installer steps resumable: a partial download is detected and resumed instead of restarted, and an interrupted build resumes where it stopped (Pixel Forge v0.51: Joshua's install stuck at 92% and he stopped it to get his computer back — the fix resumes both the download and the engine build). Never make the user re-download or rebuild from zero because an install was interrupted.
- Installer checklist from Pixel Forge v0.53 (2026-11-14 ~09:38): disk-space check BEFORE the big writes; cheap steps first; progress bar moving INSIDE a long step, not just per-step; cancel mid-step that leaves everything resumable; show apt/pip output on failure.
- Seamless install: one install gets EVERYTHING, including third-party programs the app depends on (Blender, Ollama + model) — not just the app's own Python deps — and API keys are set up in-app (paste the key, the app checks it works, saves it), never in the terminal, never in code. (SKULLPT v1.8, 2026-11-14–15: "ALL DEPENDENCIES SHOULD BE INSTALLED WHEN INSTALLING SKULLPT I SHOULDN'T HAVE TO USE THE TERMINAL TO PULL OR DOWNLOAD ANYTHING ELSE".)
- Packaging downloads are pinned to a release and checksum-verified; never fetch unpinned 'latest'. (WINLINX: yabridge was unpinned 'latest' with no checksum — pin the release + SHA-256.)
- Installer keep/temp dirs must be a sibling of the install dir (same filesystem), never the system temp directory — tmpfs is small and a filled temp dir strands data mid-run. (Android Photo Transfer, 2026-11-14.)
- Audit every user-facing string in the installer, launcher, app, README, and desktop files for terminal commands — the install/run path must require none. A missing-dependency error points at the installer ("double-click Install SKULLPT"), never at a command. The README documents a terminal route only in a clearly labeled optional subsection for advanced users.
- Guard the first run in the app itself, not just in the installer: wrap the GUI import so a missing PySide6 shows a plain-language message naming the missing package and pointing at the installer, never a traceback. Put the same guard in `run.sh`. Test it by running the app with the dependency absent — DUO v0.14 proved the guard by running with no PySide6 installed at all.
- Accept any input format and normalize internally; never reject the user's input for its format. (SHELFLIFE, 2026-11-14: any photo, any size, any file type — HEIC, WebP, and AVIF all converted.)

## Write a .desktop file that survives GLib parsing

- Write the Exec line as `python3 -c "..."` with the `%k` field code as a separate argument token, and resolve the folder inside Python with dirname and a subprocess list call.
- Never put a nested escaped quote inside Exec, because the GLib desktop parser rejects the whole file with a missing Exec field error when it sees one.
- Keep an os.getcwd() fallback in the launcher for launchers that expand `%k` to empty.
- The `%k`-dirname pattern is for a `.desktop` file that sits NEXT TO what it launches (the installer `.desktop` in the unzip folder, next to `install.sh`). For the APP launcher the installer places on the Desktop or in the app menu, write the ABSOLUTE install path into the Exec line at install time — `%k` resolves to the Desktop folder, where the program is not, so a launcher that looks next to itself runs, finds nothing, and quits silently with no window at all (ACR v0.8: the desktop icon did exactly this; v0.8.1 fixed it by pointing straight at the program).
- Verify the installed launcher with a launch simulation before shipping: place the `.desktop` file in a different folder from the program, launch it from an unrelated working directory, and confirm the app actually starts (see the T11 launch-simulation check and the T25 desktop-launch-sim tool).
- See the [desktop entry template](references/desktop-entry-template.desktop) for the working pattern.

## Mark the desktop icon trusted, and keep user data out of update zips

- The installer must mark the installed `.desktop` launcher trusted, or Mint can refuse to launch it: a v1.5 launcher shipped with the icon never marked trusted, and the fix (v1.5.1) was the trusted marking plus a launcher that opens the program directly instead of a terminal window the user had to leave running.
- Update zips exclude the user-data file (no `data.json`): the user unzips the update over their install folder, and their notes and progress must survive the overwrite. Test the overwrite with seeded data (a seeded note and a completion) before shipping the update.

## Harden the launcher and installer against three real failures

- Resolve symlinks in CLI wrappers: if the app installs a command as a symlink (e.g. `~/.local/bin/stella` → the app folder), the wrapper must resolve the symlink before locating its own directory. Resolving from `$0` through the symlink points at `~/.local/bin` instead of the app folder and the command dies with `ModuleNotFoundError`. Resolve in the wrapper, in `run.sh`, and in `install.sh`, and add a regression test that invokes the command through its installed symlink.
- Quote absolute paths in generated `.desktop` files ONLY on the Exec= line, never on the Icon= line: GLib strips quotes from Exec but takes an Icon value literally, quotes included, so a quoted Icon= points at a path with literal quote characters in it and the icon never shows (STELLA audit #6 W1: the v0.1 quoting fix backfired — the quoted Icon broke the menu icon on every install; a libgio probe showed the resolved path carrying the quotes; fixed by unquoting in v0.3.1). An unquoted Icon= resolves fine, including on a spaced path.
- Name the fix for a missing system prerequisite — and heal it when you can: when the installer needs something like `python3-venv`, install that one package itself with one pkexec call (a GUI password prompt, no terminal) and retry automatically, instead of printing a command for the user. Only if the user declines the prompt or apt fails, say so in plain language. Never fail cryptically downstream, and never put a terminal command in a user-facing message.
- Snapshot pushes cannot carry binary files: keep the icon SVG as the source of truth in the repo with a render script to regenerate the PNGs, and ship the prebuilt PNGs in the Release zip only — do not expect them to survive a push.
- Binary assets (icon PNGs) go in via browser commit, not the code push. (Android Photo Transfer, 2026-11-14: the icon PNGs were committed via browser because they can't travel with the code push.)

## Verify the package before it ships

- Audit the zip contents before it ships: list every file and confirm each one belongs to the program. No user projects, no user data, and no stray demo or leftover folders — the distribution is the program only. A stray gets removed from the tree (and from main via the web UI when it is already there) before the Release is updated.
- The executable install launcher is in EVERY release, and its presence is verified before shipping. A release without it is a failed ship. (DUO, 2026-11-15 15:04: "Whybdoesnt the updated releae have the eccutabkenintall launcher man why the fuck do you keep doing this every ducking project has the same shit".)
- A web game ships a standalone HTML file in the release that opens in any browser, alongside the zip. (YAHTZEE, 2026-11-17 16:46: "Push and uodate the release make sure there is an active html file as well that opens it in any browser".)
- Each version ships under a new filename: the same filename across versions serves the cached old one. (COLOR PALLETS, 2026-11-15 - proven twice, the video incident and the palette cards; see [ship-pipeline](../ship-pipeline/SKILL.md).)
- Test the installer in a fake-HOME scratch copy, in two phases: dependencies present, then dependencies hidden. Each phase runs end to end on its own. (SOLDAR Phase 2, 2026-11-15: installer Phase A and Phase B each passed end to end in a scratch copy.)
- Verify the zip exec bits after repacking (see [ship-pipeline](../ship-pipeline/SKILL.md)) and test-extract the zip before sending it.
- `.desktop` launchers must ship executable in the zip (OST v22, 2026-11-18 ~12:25-12:27). Joshua: "No i shouldn't need the fucjing terminal". The zip builder must set stored mode 0o100755 on BOTH `.sh` files AND `.desktop` files (external_attr must include regular-file type bits); a non-executable .desktop double-clicked in Nemo/Thunar opens in a text editor instead of launching. Add a pre-upload check: verify stored modes in the built zip before attaching it to the Release (T39 release-zip-mode-checker enforces it). Worked example: OST v22 fixed-asset re-upload, new zip SHA-256 `3bc65955dd3840eec1d9bd5cd0c3299d8db0f7bb58c3d523b217455987f3fbb1`.
- Test the installer in a clean environment that does not already have the dependencies, because a venv that already has them hides a missing-deps failure.
- Select nothing by default in the installer or the app, and let the user choose.
- Run the suite once in a fresh copy with the exec bits stripped, as well as in the tree: a clone stores every file 100644, so this proves nothing in the build or the tests depends on stored modes. The Release zip still carries the correct 0o100755 modes (see [ship-pipeline](../ship-pipeline/SKILL.md)).

## Where this comes from

- This packaging shape was built for Code Forge and retrofitted onto MIMIK (after the silent PySide6 launch failure), Pixel Forge, WinLinx, Forge Browser, and getcompute, with the installer rules set in the main chat and the GITHUB thread. The GUI installer window, python3-venv self-heal, private-venv dependency install, and no-terminal audit come from SKULLPT v1.2/v1.3 (2026-11-12); desktop-icon trust and data-safe update zips from Study Shell v1.5.1 (2026-11-12). It is recorded in the BNB audit as S6.
- ACR v0.8.1 desktop-icon fix and the DATAPACKR icon-render subprocess fix, both 2026-11-13; Pixel Forge v0.51 installer caps + resumable install, same day; STELLA v0.3.1 Icon-quoting correction, same day.

## Available connectors

- [GitHub](../CONNECTORS.md) for pushing the packaged project and updating the Release that carries it.

## Alternatives for better results

- Offer to retrofit the same installer onto an older project when the user reports installing it from a terminal.
- Do NOT offer a terminal install path: the standing rule is no terminal at all to run or install anything, period. If the GUI installer cannot run on the user's machine, that is a defect to fix in the installer (including its degraded path), not a reason to hand the user commands.
