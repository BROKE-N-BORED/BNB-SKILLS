# S63 — Qt GUI proof harness: drive the real window without hanging

## When to use

- Use this skill whenever a Qt (PySide6) build needs a live GUI
  proof: a script that opens the real window from a fresh unzip,
  drives it through the new feature, and checks real behaviour —
  not the unit suite, the proof on top of it.
- Use it for every proof script you write, and for every proof
  script a builder hands you to re-run. A proof that hangs teaches
  nothing and burns the run.
- This skill is about the harness — the script that drives the app.
  The Qt test environment (libs, platform, TMPDIR) lives in the
  [qt-verification-harness](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/qt-verification-harness)
  tool (T12, BNB TOOLS); run the proof through it. Product-side
  threading (worker + debounce) is
  [qt-ui-thread-offload](../qt-ui-thread-offload/SKILL.md), not this
  skill.

## Run a persistent safety watcher from the start

- Start a persistent QTimer watcher before any other step. It
  polls for unexpected modal dialogs, records each one (title +
  text), and dismisses it. A `processEvents()` settle pump can be
  trapped FOREVER by an unexpected modal dialog's nested event
  loop — the deadline never gets checked and the script sits at
  ~0 CPU until killed.
- Stop the watcher only around a dialog the harness expects and
  handles itself, then restart it immediately after.
- Run the script with `python -u` and log to a file: piped stdout
  buffers, and a timeout kill loses all output otherwise.

## Drive expected dialogs for real, by role

- For a dialog the test expects, use a QTimer modal watcher that
  finds the real dialog and clicks the real button — never
  `dlg.accept()`: `QMessageBox.accept()` does not click a button,
  `question()` returns NoButton, and the answer reads as a decline.
- Click by role, not by text: `dlg.button(QMessageBox.StandardButton.Yes)`.
  Standard-button text carries a mnemonic (`"&Yes"`, not `"Yes"`),
  so a text match on `"Yes"` never fires and the harness hangs in
  `exec()` forever.
- A widget's signal is not its behaviour: emitting
  `QListWidget.itemClicked` does NOT move the current row — a real
  click does both. Set the row with `setCurrentRow(...)` AND emit
  `itemClicked`, or the dialog loads the wrong row. Some lists
  update on `itemClicked`, not on selection — call the handler
  explicitly when the harness drives the list.
- A debounced control fires AFTER the setter returns (Pixel Forge
  video settings: 300 ms). Keep the modal watcher running while
  the harness pumps until the dialog is seen, or the safety
  watcher swallows the expected dialog.

## Apply the app's real theme yourself

- A verify harness that constructs the main window directly runs
  WITHOUT the app's stylesheet when only `main()` applies it — and
  verifies the wrong theme. Call
  `app.setStyleSheet(DARK_STYLESHEET)` (or the app's equivalent)
  in the harness itself before driving anything.
- Sample colours on enabled buttons, away from the text: disabled
  buttons render greyed.
- `setCurrentIndex` only emits `currentChanged` when the index
  actually changes — start a tab-switch probe from a different tab.

## Use absolute paths, persistent assets, and wall-clock waits

- Use ABSOLUTE paths everywhere in the harness. `~` and
  `os.path.expanduser("~")` resolve under an overridden HOME in
  the Qt test env, so a clip path can silently point at a file
  that does not exist.
- Keep shared test assets in the persistent workspace, never
  `/tmp`: a missing clip file raises a modal error dialog, which
  traps the settle pump (above) instead of failing the checks.
- A bare pump loop exits in milliseconds. Video and async waits
  need a wall-clock deadline with sleeps, not a bare
  `processEvents()` loop.
- Create the `QApplication` BEFORE any library work that loads
  images: some loaders lazily bootstrap a `QCoreApplication`,
  and constructing `QApplication` afterwards raises RuntimeError.
- Keep `QMimeData` alive in the caller's scope until after a
  synthetic drag event is handled: `QDragEnterEvent` holds a raw
  pointer to it, and freeing the mime object first segfaults Qt.

## Know what offscreen cannot do, and drive around it

- Offscreen Qt never synthesizes a double-click from synthetic
  presses: neither `QTest.mouseDClick` nor two rapid `mouseClick`s
  open an editor whose triggers are DoubleClicked — double-click
  detection happens in the platform plugin. Open the editor with
  `editItem()` directly; it is the same editor the double-click
  would open.
- `QTest.mouseMove` has no buttons argument in this PySide6 build,
  so a synthetic drag never starts. Drive a reorder through the
  strip model's `moveRows` (the same operation a drag performs —
  it fires `rowsMoved`, which is what updates the order) and verify
  the strip's drag configuration attributes instead.

## Bound every run, and check stderr even when green

- Run long suites under `timeout` (e.g. `timeout 280 ...`) in
  builder briefs and in your own verification, so a hang becomes
  a diagnosable failure instead of a silent stall. A suite can sit
  hung for 45+ minutes with seconds of CPU and no report.
- Check stderr, not just the suite result: a `setIcon` call inside
  an `itemChanged` handler recurses until the stack blows
  (RecursionError + a knock-on SystemError), while the suite stays
  green because the first icon swap landed before the blow-up.
  Only stderr shows it. (The product fix is to block the widget's
  signals around the icon swap.)
- After a recursion fix lands, keep a stderr check in the proof:
  zero RecursionError / SystemError / traceback matches in the
  suite log and the proof log.

## Where this comes from

- PIXEL FORGE DEVELOPMENT thread (b2e2291b), overnight
  2026-11-12–13, proofs v31–v46 (00:33–07:52 EST): the QTimer
  modal watcher driving real dialogs (v31, 17/17 checks); the
  harness-lessons report — `QMessageBox.accept()` reads as a
  decline, bare pump loops exit in milliseconds, lists update on
  `itemClicked` (01:46); the first proof run hung at ~0 CPU when
  a video-import failure dialog trapped the `processEvents()`
  pump, fixed by a persistent safety watcher that records +
  dismisses unexpected modals, plus absolute paths after `~`
  resolved under the overridden HOME (03:20); the persistent
  QTimer safety watcher + dark stylesheet as the standard proof
  setup from v35 on (03:43, 04:03, 04:30, 04:42, 05:01, 05:16,
  05:34, 06:36, 07:10, 07:34, 07:52); the `setIcon` inside
  `itemChanged` RecursionError with a green suite, fixed by
  blocking signals around the icon swap, and the stderr check
  that stayed in later proofs (04:03, 04:30, 04:42); `&&`
  escaping so Qt renders a literal `&` instead of eating it as a
  mnemonic (05:16); the builder suite run hung 45 minutes and
  killed by hand (21:40, 2026-11-12).
- Four items rest on AGENTS.md entries dated 2026-11-13 from the
  same verify runs, with the in-thread proof runs as
  corroboration but the failure detail not in the visible
  transcript: the `&Yes` mnemonic button text (v0.35 proof,
  03:43), `setCurrentRow` + `itemClicked` (v0.35 proof, 03:43),
  the `moveRows` drag drive-around (v0.36 proof, 04:03), and
  offscreen double-click via `editItem()` (v0.45 proof, 07:34).
  Cut them if the library requires transcript-only evidence.
- Found in the second BNB delta scan (2026-11-13).

## Alternatives for better results

- Offer a bare-runnable subset of the suite (module-guarded GUI
  tests that skip cleanly without PySide6) when the proof must
  also run where Qt is absent — Pixel Forge v0.18 shipped its
  suite that way.
