# S55 — Dual-model AI-to-AI relay

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
  WHOLE-WORD match stops the relay, and the status line and pane
  name the phrase that stopped it. Substring matching was the v0.2
  behaviour and it was wrong: "cap" stopped a relay on "capital".
  Whole words only.
- Stop on agreement: a fixed phrase list ("i agree", "agreed",
  "sounds good", "that works"), negation-aware matching — no LLM
  judge, the 2B models are slow enough already. A negated phrase
  must NOT stop the relay: "I disagreed" ended relays until v0.12
  fixed it, while a real "I agree" still stops one.
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
  HTTP (see [fake-provider-verification](../fake-provider-verification/SKILL.md)): blind and aware drives,
  cap at exactly N, phrase and agreement stops, review-pause
  editing, compare pick going to one side only. Eyeball the
  screenshots yourself.
- Real Ollama models on his PC are still the closer: first-token
  latency, model load time, and RAM behavior with two real 2B
  models cannot be proven against a fake. Say so in the receipt.

## Built after v0.3 (shipped by v0.10, 2026-11-12)

- Everything this section once listed as approved-but-unbuilt has
  shipped: auto-summarize for long loops (Summarize keeps the last
  4 turns verbatim, 12,000-char budget nudge — the nudge must
  NEVER auto-trigger a model call); per-turn speed and RAM readout
  (tok/s, time to first token, model RAM — dashes before any turn,
  "n/a" when timing fields are absent, never invented numbers);
  file attachments (5 x 100 KB, text only, one-shot); tasks and
  delegation (one-round worker + review/continue/nothing
  follow-up); transcript save/export (one side, both, or the full
  interleaved transcript; attachments never pasted in).
- Per-pane token counts (v0.20): each pane's stats line shows the
  last turn's token counts, in and out, straight from Ollama's own
  numbers, plus a session total per side. Clearing a pane resets
  its stats.
- Relay presets (v0.21): a preset holds the whole relay setup —
  which side starts, blind or aware, turn cap, stop phrases,
  stop-on-agreement, review-each-hop — saved and restored like a
  model pair. Loading a preset never starts a relay on its own.
- Multi-round tasks (v0.22): the Rounds control (1–10) next to
  the follow-up picker. "Continue it" keeps building on the last
  result each round; "Review it" alternates review and revise.
  Rounds 1 with a follow-up is exactly the old one-round task
  flow — the floor matters, because the first cut made Rounds 1 a
  single generation and would have broken it.
- Per-pane search (v0.23): each pane has a search row under its
  transcript — type to find text, every match highlighted, Previous
  and Next stepping between them with wrap — plus conversation
  import.
- Markdown rendering (v0.24): model replies render as formatted text
  (bold, italic, inline code, code blocks, headers, lists,
  blockquotes, links). While a reply streams it still shows as plain
  text, and the formatting lands the moment the turn finishes, so
  partial markup never flickers mid-stream. Links are clickable and
  open in the browser. The user's own messages stay plain text
  exactly as typed, and nothing stored changes — history, transcript
  exports, and saved conversations keep the raw text.
- Monolith split (v0.25): the one big code file is now ten focused
  modules. Nothing visible changed — same window, same features,
  same files — just easier to work on and safer to change.
- One message structure + MIT (v0.26): one message structure holds
  each message's role, text, label, and display together instead of
  three parallel lists; conversations saved by older versions still
  open. MIT LICENSE in the repo.
- Bounded transcript log (v0.27): the full-transcript log keeps the
  most recent 2,000 entries and trims the oldest first, so a long
  session cannot grow it forever. If anything was trimmed, the
  exported transcript says so right under the header. Per-pane
  histories are untouched.
- Update check (v0.28): DUO checks for a newer Release when it
  starts, in the background, and stays silent if there is no
  network. A "Check for updates" button sits in the bottom row. No
  auto-download or install — it just tells you.
- Activity lights + machine meter (v0.29): each side has a light and
  a line of small text under the stats — green "Thinking…" while it
  generates, amber "Waiting for Ollama…" / "Queued…" / "Waiting for
  you to review…", red if a turn fails, grey "Idle" when done — plus
  a live CPU/RAM meter in the bottom-right corner, refreshed every
  second.
- Menu bar + How to Use (v0.30): File, Relay, and Help across the
  top, with shortcuts (Ctrl+S save, Ctrl+O open, Ctrl+Shift+S save
  full transcript, Ctrl+Q quit); every menu item does exactly what
  its button does. Help carries a built-in How to Use index covering
  the whole app. Visible text is em-dash-free throughout.
- Director toggle + exit-crash fix (v0.31): the Director toggle
  collapses the controls below the panes so they take the full
  window, remembers the choice between runs, and never stops
  anything running. Also fixes a real crash: closing DUO while a
  background check was running could kill it on exit.

## Where this comes from

- Built as DUO in thread 284b2ad4 on 2026-11-12: Item 1 shell +
  picker + send (v0.1, 27/27 tests), Item 2 relay loop (v0.2,
  54/54 tests, blind 4-turn + aware 2-turn drives), Item 3
  director controls (v0.3, 81/81 tests, three GUI drives). The
  relay core is the `RelaySession` class in
  `dual-chat-v03-build/dual_chat.py` — pure logic, no Qt.
- Stop conditions corrected in v0.12 (2026-11-12): whole-word stop
  phrases, negation-aware agreement stop. The five approved items
  all shipped by v0.10 the same evening; relay presets (v0.21) and
  multi-round tasks (v0.22) shipped 2026-11-13, and v0.23–v0.31
  (search, Markdown, monolith split, one message structure + MIT,
  bounded transcript, update check, activity lights + meter, menu
  bar, Director toggle) shipped the same day.

## Alternatives for better results

- Offer a scripted relay run through the [dual-model-relay-harness](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/dual-model-relay-harness) tool (T18, BNB TOOLS) when the user wants a relay without opening the GUI.
- Offer aware mode when the goal is collaboration between the two
  models rather than a blind conversation.
