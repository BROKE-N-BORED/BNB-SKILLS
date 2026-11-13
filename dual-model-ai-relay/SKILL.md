# Dual-model AI-to-AI relay

## When to use

- Use this skill when building or running a chat interface where two
  AI models talk to each other under a human director: two windows
  side by side, each loaded with its own model, plus a director layer
  that starts the chat and steers it.
- Use it for the relay loop itself (one model's reply handed to the
  other as if from a person), for the director controls (reorder,
  edit-before-forward, compare mode), and for saved model pairs.
- Do not use it for a single-model chat window: the relay, the
  framing, and the stop conditions are the whole point here.

## Shape: two panes, one director, one turn at a time

- Two panes, one model per pane, each with its own model picker and
  its own conversation history. The director sends to A, to B, or
  to both ("Both" always orders A first, then B).
- Run generations strictly one at a time through a serial runner:
  B never starts until A finishes. Two models at once on an 8 GB
  PC thrashes; the one-at-a-time rule is a hardware fact, not a
  preference. Prove the ordering in tests, not just in the code.
- Pickers start blank with sends disabled until a model is picked.
  Nothing is selected by default, ever.
- Ollama local first so the whole thing is $0. A plain-language
  error when Ollama is down ("Ollama isn't running. Start Ollama
  and try again.") — no tracebacks in the UI.

## Blind and aware framing

- Blind mode (default): the other model receives the bare reply
  text as a plain user message — no framing, no mention of AI.
  Each model sees only a person talking to it.
- Aware mode: the reply is framed so the models know they are
  talking to another AI: "You are talking with another AI
  assistant (Model %s). It said: %s" with the sending side's name.
- Assert the exact payload in tests: in blind mode the receiving
  model's request body must be exactly `[{"role": "user",
  "content": "<bare text>"}]`; in aware mode it must carry the
  framed text with the correct side name per hop.

## Stop conditions

- Turn cap: default 10, range 1-50. A "turn" is one generation and
  the seed turn is turn 1, so a cap of N means exactly N
  generations before the relay halts. Halt at exactly N, not N+1.
- Stop phrases: a comma-separated field; a case-insensitive
  substring match stops the relay, and the status line and pane
  name the phrase that stopped it.
- Stop on agreement: a fixed phrase list ("i agree", "agreed",
  "sounds good", "that works"), plain case-insensitive substring
  matching — no LLM judge, the 2B models are slow enough already.
- A phrase or agreement stop is reported before the cap when they
  land on the same turn, because it says more about why the relay
  ended.
- A Stop button ends the relay at any time, and a live status line
  shows where it stands ("Relay on: turn 3/10, A to B" /
  "Relay stopped: turn cap reached.").
- Keep the relay's config, turn counting, framing, and stop checks
  in pure logic with no UI in it, so the loop is testable without
  opening a window.

## Director controls

- Reorder and delete: the director can move any message up or down
  or delete it from a side's history, and the model sees the
  edited order on the next turn. Test that the next turn sends
  exactly the new order.
- Review each hop: pause the relay before a reply is forwarded,
  show the text in an edit box, and offer forward-original,
  forward-edited, skip, and stop. The edited text — not the
  original — is what the other side receives.
- Per-side instructions: a system prompt per side, saved with the
  pair. An empty or whitespace-only instruction means no system
  message at all.
- Saved pairs: model A + model B + both instructions in one plain
  JSON file, loadable in one tap. A missing or malformed pairs
  file reads as no pairs — a bad file never stops the app.
- Compare mode: after Send to Both, each reply gets a "Use this"
  button; picking one sends "You picked this answer: %s" to the
  other side only, and marks the picked pane.

## Keep the display honest

- Relayed hops are tagged in the window's transcripts only ("You
  [relay from Model A]: ..."). The tag never reaches either
  model's history — assert that in tests.
- Disable Clear on both sides mid-relay so the relay cannot have
  its history pulled out from under it.
- Guard the shutdown path: closing the window mid-relay must not
  print tracebacks from queued signals landing on deleted objects.

## Verify against a fake Ollama, then his PC

- Verify the whole loop against a scripted fake Ollama over real
  HTTP (see fake-provider-verification): blind and aware drives,
  cap at exactly N, phrase and agreement stops, review-pause
  editing, compare pick going to one side only. Eyeball the
  screenshots yourself.
- Real Ollama models on his PC are still the closer: first-token
  latency, model load time, and RAM behavior with two real 2B
  models cannot be proven against a fake. Say so in the receipt.

## Approved but not yet built

- These were approved by Joshua on 2026-11-12 and are on the plan,
  but were NOT built or verified as of the v0.3 ship: auto-summarize
  for long loops (condense as the thread grows; a "History is long"
  nudge must NEVER auto-trigger a model call), per-turn speed and
  RAM readout (tok/s from eval_count/eval_duration, time to first
  token, model RAM from /api/ps — dashes before any turn, "n/a"
  when timing fields are absent, never invented numbers), files
  and documents upload, tasks and delegation, transcript
  save/export. Do not claim any of these as proven until they ship.

## Where this comes from

- Built as DUO in thread 284b2ad4 on 2026-11-12: Item 1 shell +
  picker + send (v0.1, 27/27 tests), Item 2 relay loop (v0.2,
  54/54 tests, blind 4-turn + aware 2-turn drives), Item 3
  director controls (v0.3, 81/81 tests, three GUI drives). The
  relay core is the `RelaySession` class in
  `dual-chat-v03-build/dual_chat.py` — pure logic, no Qt.

## Available connectors

- Use `muse.connector_search` to find other connectors and
  `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or
  MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer a scripted relay run through the dual-model-relay-harness
  tool when the user wants a relay without opening the GUI.
- Offer aware mode when the goal is collaboration between the two
  models rather than a blind conversation.
