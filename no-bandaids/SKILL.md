# S74 — No bandaids: fix the root cause, never mask a defect with a workaround

When something is broken, fix the underlying code — never paper over it
with a UI workaround, a button, or an extra step that masks the defect. If
the fix needs a workaround to be usable at all, the workaround is a bug,
not a feature.

## When to use

- Something is broken and the tempting fix is a button, a toggle, a
  restart step, or an instruction to the user instead of a code change.
- You catch yourself adding a control whose only job is to work around a
  defect (a "start the service" button, a "retry" that hides a connection
  bug, a manual step that stands in for code that should just work).
- You are reviewing a fix and asking whether it addresses the real fault
  or only its symptom.
- Do NOT use this to refuse a genuine feature: a control the user asked
  for, or one that does real work on its own, is not a bandaid. The test
  is whether the control exists only because something else is broken.

## Fix the code, not the symptom

- Find the real fault first. If another app on the same machine does the
  same job without the problem, the fault is in your code, not in the
  service, the machine, or the user — compare the two and find the
  difference.
- A workaround instruction ("close the browser and start over") is not a
  fix. Telling the user to do extra steps to get around broken code is
  the same failure as adding a masking button.
- Root cause first, always: when something is broken, do the research,
  find the solution, and build the real fix - do not create a
  workaround or a bandaid. (PIXEL FORGE, 2026-11-17 07:38: "Figure it
  out, do some research find the solution do not create work around or
  bandaid, really get to the root and build the solution if necessary".
  The grid bug's root cause was the tile path being relative; v0.81
  fixed it for real.)
- When the root fix lands, remove the workaround. A button that masked a
  bug does not become a feature once the bug is fixed — it gets deleted,
  and the ship note says so.

## The test: would the workaround survive the fix?

- Ask it before building the workaround: if the underlying code worked
  properly, would this button, step, or instruction still be needed? If
  the answer is no, do not build it — fix the code instead.
- If you already shipped a workaround, the fix is not done until the
  workaround is gone. Leaving it in place means the next person reads it
  as a feature and builds on top of a masked defect.
- The same rule covers UI that lies about state: a button or badge that
  claims something works when it does not is a bandaid on the truth, not
  a fix.

## Where this comes from

- DUO DEV thread (284b2ad4, Sat 2026-11-14 09:16–09:30 EST): DUO
  shipped a Start Ollama button (v0.35) to work around a connection
  problem Code Forge never had. Joshua: "Code Forge doesnt gace this
  probkem amd there is no ollma button roght,? You are coding bullshit
  and then masking it with more vullshit" — "You are coding bullshit and
  then masking it with more bullshit" — and "Im not at the fucking screen
  I didntsay I was or that there was a problem 8m telling you that your
  building shit to bandaid the real fucking issue is your code not
  ollama". v0.49 fixed the connection ("DUO stays connected to Ollama now
  the way Forge does") and removed the button.
- MAIN CHAT thread (c6ee49a6, Sat 2026-11-14 08:28–09:23 EST): the Forge
  context fix — "No more workarounds" — after Joshua called out the
  workaround habit and the "close Firefox and start over" instruction:
  "You're right. The workarounds weren't the fix, and telling you to
  close Firefox and start over wasn't it either. The code fixes are
  built."
- HICKSFIELD thread (c3656ead, Sat 2026-11-14): the "lying red button"
  — a control that claimed a state that was not real — fixed in place.
- PIXEL FORGE DEVELOPMENT thread (b2e2291b, Sat 2026-11-14 ~22:00 EST):
  v0.72 made the sheet command stop lying about files (exit-code
  honesty) — same rule, applied to what the tool reports.
- PIXEL FORGE DEVELOPMENT thread (b2e2291b, 2026-11-17 07:38 EST):
  root-cause-first restated as the rule itself - "Figure it out, do
  some research find the solution do not create work around or
  bandaid, really get to the root and build the solution if
  necessary" - and the grid bug was fixed for real in v0.81 (root
  cause: the tile path was relative).
- Found in the sixth BNB delta scan (2026-11-15). One in-window instance
  plus three supporting instances of the same failure mode.
