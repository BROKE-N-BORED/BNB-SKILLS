# Linux release packaging

## When to use

- Use this skill to turn a project tree into a real Linux program the user can install by double-clicking, with an icon and a menu entry.
- Use it for every project that ships, and to retrofit the same packaging onto older projects that still install from a terminal.
- Build a native Linux desktop window for the app itself, never a web UI, unless the user has explicitly asked for a web UI.

## Make the icon

- Keep the icon SVG as the source of truth and render the PNG sizes from it at install time.
- Ship the prebuilt PNGs in the zip as well, so the install works even where the renderer is missing.
- Test the icon at the small sizes the desktop actually shows, and keep it readable at 16, 32, and 48 pixels.

## Build the GUI installer

- Ship a double-click `.desktop` installer that asks for privilege with pkexec and installs to a fixed location, with no terminal step.
- Make the installer back up an existing install before it upgrades, and ship an uninstaller alongside it.
- Run install scripts with bash explicitly, never with sh, because the scripts use bash arrays and `set -euo pipefail`, and sh dies on them under dash.
- Put every dependency the app needs in the core dependencies, never in optional extras, because an optional GUI toolkit once shipped a menu icon that died silently on a missing import while the terminal stayed hidden.
- Verify the install works before reporting success: run a fatal check that the packages are actually present, and a warning that names the missing library when the GUI cannot start on the machine's system libraries.

## Write a .desktop file that survives GLib parsing

- Write the Exec line as `python3 -c "..."` with the `%k` field code as a separate argument token, and resolve the folder inside Python with dirname and a subprocess list call.
- Never put a nested escaped quote inside Exec, because the GLib desktop parser rejects the whole file with a missing Exec field error when it sees one.
- Keep an os.getcwd() fallback in the launcher for launchers that expand `%k` to empty.
- See references/desktop-entry-template.desktop for the working pattern.

## Harden the launcher and installer against three real failures

- Resolve symlinks in CLI wrappers: if the app installs a command as a symlink (e.g. `~/.local/bin/stella` → the app folder), the wrapper must resolve the symlink before locating its own directory. Resolving from `$0` through the symlink points at `~/.local/bin` instead of the app folder and the command dies with `ModuleNotFoundError`. Resolve in the wrapper, in `run.sh`, and in `install.sh`, and add a regression test that invokes the command through its installed symlink.
- Quote absolute paths in generated `.desktop` files: Exec= and Icon= lines built from the install path must be quoted, so an install path containing spaces still launches.
- Name the fix for a missing system prerequisite: when the installer needs something like `python3-venv`, check for it and fail with the exact install command (`sudo apt install python3-venv`) instead of failing cryptically downstream.
- Snapshot pushes cannot carry binary files: keep the icon SVG as the source of truth in the repo with a render script to regenerate the PNGs, and ship the prebuilt PNGs in the Release zip only — do not expect them to survive a push.

## Verify the package before it ships

- Verify the zip exec bits after repacking (see ship-pipeline) and test-extract the zip before sending it.
- Test the installer in a clean environment that does not already have the dependencies, because a venv that already has them hides a missing-deps failure.
- Select nothing by default in the installer or the app, and let the user choose.

## Where this comes from

- This packaging shape was built for Code Forge and retrofitted onto MIMIK (after the silent PySide6 launch failure), Pixel Forge, WinLinx, Forge Browser, and getcompute, with the installer rules set in the main chat and the GITHUB thread. It is recorded in the BNB audit as S6.

## Available connectors

- [GitHub](/opt/hatch/connectors/github/CONNECTOR.md) for pushing the packaged project and cutting the Release that carries it.
- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer to retrofit the same installer onto an older project when the user reports installing it from a terminal.
- Offer a terminal install path with short single-line commands only when the GUI installer cannot run on the user's machine.
