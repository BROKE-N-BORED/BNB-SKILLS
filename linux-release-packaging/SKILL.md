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

## Build the GUI installer

- Ship a double-click `.desktop` installer that asks for privilege with pkexec and installs to a fixed location, with no terminal step.
- Make the installer back up an existing install before it upgrades, and ship an uninstaller alongside it.
- Run install scripts with bash explicitly, never with sh, because the scripts use bash arrays and `set -euo pipefail`, and sh dies on them under dash.
- Put every dependency the app needs in the core dependencies, never in optional extras, because an optional GUI toolkit once shipped a menu icon that died silently on a missing import while the terminal stayed hidden.
- A package with no PyPI wheels must never be left to plain pip: pip will compile it from source on his PC. llama-cpp-python has no wheels on PyPI at all — a plain install always builds llama.cpp from source (gcc + cmake, 15–30 minutes on 2 cores). Pin the project's own wheel index in requirements.txt (`--extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu`) plus `--only-binary=llama-cpp-python` so pip never falls back to a source build if that index lags PyPI by a version. FYRN v0.1 shipped 2026-11-13 with the model engine installing from the ready-made wheel — no compiler, no 20-minute build on his PC.
- Verify the install works before reporting success: run a fatal check that the packages are actually present, and a warning that names the missing library when the GUI cannot start on the machine's system libraries.
- The installer is a real WINDOW, not a terminal: a Terminal=false `.desktop` launcher starts the install behind a progress window (per-step percentages), shows a success dialog that asks "Open it now?", and shows a plain-language error dialog with the log path on failure. All install output goes to `install.log` in the install folder. Probe for a dialog tool in the order xenity, zenity, yad (Cinnamon's own probe order — xenity is Mint's maintained Zenity fork and may have replaced zenity on fully-updated Mint 22.x). If no dialog tool is installed, falling back to the terminal installer is the documented degraded path, not the plan.
- The installer HEALS its own missing system prerequisites instead of printing a command for the user: when `python3 -m venv` fails because python3-venv is missing, the installer installs that one package itself with ONE pkexec call (a GUI password prompt, no terminal) and retries venv creation automatically. If the user declines the prompt or apt fails, say so in plain language ("needs one system package to install — re-run the installer and allow it when asked"). The same one-pkexec-call heal applies to build tools and /opt installs. No terminal command appears in any user-facing message, and the installer never asks the user to type anything.
- The installer creates a private `.venv` in the install folder and installs the GUI toolkit into it itself — never `--user`, never `--break-system-packages` (both wrong on Mint 3.12) — and the launcher prefers `.venv/bin/python`. Never hand the user a `pip install` command: it fails on Mint's externally-managed Python (SKULLPT v1.1 printed `pip install PySide6` as the fix for its own missing dependency; the fix did not work and the app had never opened on the target PC).
- Cap parallel work in the installer to what the machine can hold: a compile or download step that spawns one job per core can fill 8 GB and swap the whole desktop to a freeze (Pixel Forge: 4 C++ compile jobs at once froze Joshua's PC mid-install; v0.51 caps the build to 2 jobs on an 8 GB machine so the desktop stays usable). Size job counts by RAM, not just by cores, and leave headroom for the desktop itself.
- Make long installer steps resumable: a partial download is detected and resumed instead of restarted, and an interrupted build resumes where it stopped (Pixel Forge v0.51: Joshua's install stuck at 92% and he stopped it to get his computer back — the fix resumes both the download and the engine build). Never make the user re-download or rebuild from zero because an install was interrupted.
- Audit every user-facing string in the installer, launcher, app, README, and desktop files for terminal commands — the install/run path must require none. A missing-dependency error points at the installer ("double-click Install SKULLPT"), never at a command. The README documents a terminal route only in a clearly labeled optional subsection for advanced users.
- Guard the first run in the app itself, not just in the installer: wrap the GUI import so a missing PySide6 shows a plain-language message naming the missing package and pointing at the installer, never a traceback. Put the same guard in `run.sh`. Test it by running the app with the dependency absent — DUO v0.14 proved the guard by running with no PySide6 installed at all.

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

## Verify the package before it ships

- Audit the zip contents before it ships: list every file and confirm each one belongs to the program. No user projects, no user data, and no stray demo or leftover folders — the distribution is the program only. A stray gets removed from the tree (and from main via the web UI when it is already there) before the Release is cut.
- Verify the zip exec bits after repacking (see [ship-pipeline](../ship-pipeline/SKILL.md)) and test-extract the zip before sending it.
- Test the installer in a clean environment that does not already have the dependencies, because a venv that already has them hides a missing-deps failure.
- Select nothing by default in the installer or the app, and let the user choose.
- Run the suite once in a fresh copy with the exec bits stripped, as well as in the tree: a clone stores every file 100644, so this proves nothing in the build or the tests depends on stored modes. The Release zip still carries the correct 0o100755 modes (see [ship-pipeline](../ship-pipeline/SKILL.md)).

## Where this comes from

- This packaging shape was built for Code Forge and retrofitted onto MIMIK (after the silent PySide6 launch failure), Pixel Forge, WinLinx, Forge Browser, and getcompute, with the installer rules set in the main chat and the GITHUB thread. The GUI installer window, python3-venv self-heal, private-venv dependency install, and no-terminal audit come from SKULLPT v1.2/v1.3 (2026-11-12); desktop-icon trust and data-safe update zips from Study Shell v1.5.1 (2026-11-12). It is recorded in the BNB audit as S6.
- ACR v0.8.1 desktop-icon fix and the DATAPACKR icon-render subprocess fix, both 2026-11-13; Pixel Forge v0.51 installer caps + resumable install, same day; STELLA v0.3.1 Icon-quoting correction, same day.

## Available connectors

- [GitHub](../CONNECTORS.md) for pushing the packaged project and cutting the Release that carries it.

## Alternatives for better results

- Offer to retrofit the same installer onto an older project when the user reports installing it from a terminal.
- Do NOT offer a terminal install path: the standing rule is no terminal at all to run or install anything, period. If the GUI installer cannot run on the user's machine, that is a defect to fix in the installer (including its degraded path), not a reason to hand the user commands.
