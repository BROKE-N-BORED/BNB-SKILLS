# S73 — No invented limits: never create a cap or rule on your own without asking

Never bake a cap, limit, or rule into a plan or build unless Joshua set it
or you asked first. A convention from a library entry, a reference app, or a
standard is not his rule. Default is no limit.

## When to use

- You are writing a plan, a task list, or a design doc and a number, a cap,
  or a rule would go in it.
- You are about to hard-code a limit into a build (a maximum count, a size
  ceiling, a restricted set of options).
- You catch yourself writing "the limit is X" or "the rule is Y" and you
  cannot point to Joshua saying it.
- Do NOT use this to second-guess limits Joshua already set — his stated
  constraints are real rules, and checking them first is the opposite
  direction of this skill.

## A convention is not his rule

- A number that came from a library entry, a reference app, a standard, or
  a common convention is a suggestion, not a rule. It does not become
  Joshua's rule by being written into a plan.
- If the plan needs a number, ask him first — or leave it unlimited and say
  so. "No cap unless you set one" is a valid plan line.
- The failure mode is silent: the cap gets baked into the plan as if it
  were a requirement, the build follows the plan, and Joshua finds a limit
  he never agreed to. Catch it at the plan stage, not after the build.

## Ask, or leave it unlimited

- Before writing any cap or rule into a plan or build, ask one question:
  did Joshua set this, or did I? If you set it, either ask him or drop it.
- When you ask, name the source honestly: "Blender's convention is 8, the
  library entry says 8 — do you want a cap, and if so what number?" That
  gives him a real choice instead of a baked-in decision.
- The same rule covers non-numeric rules. An agent's own note ("no
  decoration") elevated into a rule is the same failure as a number cap:
  a rule nobody set, enforced as if it were immutable.

## Where this comes from

- REBLEND DEV thread (2a82689c, Sun 2026-11-15 ~11:40 EST): an 8-slice
  cap and an 8-light cap came from a library entry and Blender's
  convention and were baked into the camera/lighting plan as if they were
  rules. Joshua: "Bmstoo cresring caps for shitnwithoutbasking imfirst
  nobody tildbyku to create caps or rules on your own without asking me
  please" — "nobody told you to create caps or rules on your own without
  asking me". The assistant owned it: "You're right, and I'm sorry — that
  was mine."
- ACR DEV thread (f9230b1c, Fri 2026-11-13 ~19:48 EST, pre-window
  supporting instance): "I dont knownwhere you got these stupid rules
  from like not decorative and shit nobody ever said that as an immutable
  rule" — the "no decoration" line came from the assistant's own notes,
  confirmed by grep: "There is no rule against decoration in your
  immutable rules… The 'no decoration' line came from my own notes."
- CODE FORGE DEV thread (94792a18, Fri 2026-11-13 ~22:50 EST,
  pre-window supporting instance): a 6 MiB ceiling the assistant had
  imposed was removed — same pattern, a cap nobody set.
- Found in the sixth BNB delta scan (2026-11-15). One in-window instance
  plus two pre-window instances of the same failure mode.
