# S58 — Fake-provider verification

## When to use

- Use this skill to verify a chat or benchmark app without real
  models, real API keys, or real spend: scripted fake provider
  servers stand in for Ollama and for OpenAI-compatible cloud
  providers over real HTTP.
- Use it when the app under test talks to a provider API —
  Ollama's `/api/*` or the OpenAI `/v1/*` shape — and the
  verification needs exact, repeatable answers.
- Do not use it to claim a live provider works. A fake proves the
  app's wiring, scoring, and failure handling; only a real call
  with a real key proves the provider.

## Serve scripted fakes over real HTTP

- Run real HTTP servers on localhost (see the
  [fake-provider-servers tool](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/fake-provider-servers) (T19, BNB TOOLS)): a fake Ollama (`/api/tags`,
  `/api/chat`, `/api/generate`, `/api/show`, `/api/ps`,
  `/api/pull`) and a fake OpenAI-compatible provider
  (`/v1/models`, `/v1/chat/completions` with SSE streaming and
  usage objects, plus media endpoints when the app has them).
- Keep the fakes stdlib-only, in-process, on ephemeral ports, so
  any test run can start them and tear them down.
- Match the real wire shapes: Ollama streams NDJSON lines ending
  in a `done: true` line with `eval_count` / `eval_duration`;
  the provider streams `data:` SSE chunks ending in
  `data: [DONE]`, with the usage object only when the request
  asked for it (`stream_options: {include_usage: true}`).

## Give the fakes canned brains and a memory

- Canned brains with fixed behaviour: smart (answers everything
  right), partial (answers some right), dumb (answers wrong or
  refuses). Deterministic scoring stays exact — smart 100,
  partial 60, dumb 0 — so a scoring bug shows up as a wrong
  number, not a flaky test.
- A broken model that answers 500 ("model exploded") and an
  unknown model that answers 404, so error paths get exercised
  without a real failure.
- Record every request the fake receives — full message histories,
  tool calls, images seen. Tests assert the exact payload the app
  sent: the bare text of a blind relay hop, a turn-2 request
  carrying the whole turn-1 history, a provider call with the
  right model id.

## Cover the failure modes, not just the happy path

- Dead server: close the connection without answering. The app
  must fail plainly and, for a provider, fail only that
  provider's models while local models keep running.
- Mid-stream reset: kill the stream partway through. A run must
  stop cleanly (Ollama dying stops the whole run) with no
  traceback and a responsive window afterwards.
- Slow mode: chunk delays with known timing, so a speed readout
  can be asserted exactly (e.g. slow-mode decode at exactly
  100.0 tok/s) instead of eyeballed.
- Bad key: 401 with the provider's message, never retried. A
  bad key is not a transient failure.
- Pull failure and pull success: streamed progress events ending
  in success (record the pull the moment success is visible, or
  the client's list refresh races the server) or in a plain
  error.
- Provider-only runs must work with Ollama down; mixed runs are
  still blocked when Ollama is down. Test both.

## Check for leaked keys

- Grep the whole results directory for the fake keys after a run:
  a key must appear in NO run file, profile, report, status
  line, or detail view.
- The provider config file holds keys and lives owner-only
  (0600) on the user's PC, is never shown on screen, and never
  ships inside the package directory. Assert its absence from
  the package in the suite.

## State the honest gaps

- The fake cannot truly see: vision answers come from the prompt,
  not from the image. Real vision quality is unproven until a
  real model looks at a real image.
- Real providers vary: usage timing, `reasoning_content`,
  429 rate limits. The app reports the provider's error and
  fails the model; there is no rate-limit backoff until one is
  built and proven against a real provider.
- The real-PC run with real models and real keys is always the
  closer. Say so in the receipt, every time.

## Where this comes from

- Proven across OLLAMA System Test v3 (233 checks), v4 (355
  checks, fake OpenAI provider with SSE + usage + 401/dead
  modes), and v5 (686 checks, `/api/show` capability screening)
  and DUO v0.1-v0.3 (blind/aware relay drives against a fake
  Ollama). The working fragments live in the OLLAMA System Test
  v5 verification files.

## Alternatives for better results

- Offer a live-provider check with a real key when the user
  explicitly asks for one, on the smallest possible call.
- Offer to add a new failure mode to the fake when a real failure
  shows up on his PC that no fake mode covers yet.
