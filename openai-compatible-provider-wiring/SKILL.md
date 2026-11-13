# Wire an OpenAI-compatible provider into Forge

## When to use this skill

- Use it when a new cloud model provider is approved for Forge and needs to be added as a selectable provider.

- Use it for any provider that exposes an OpenAI-compatible chat API, whether or not it is on the current allowlist.

- Do not use it to pick which provider or model to add; that decision comes from the user first.

## Verify before you wire

- Read the vendor's own documentation first and confirm the exact base URL and the exact model ID from that source.

- Do not guess a model ID, a base URL, or an endpoint path from a third-party roundup or from memory.

- Record the vendor doc URL you verified against, so a later check can re-verify it.

## Wire the provider on the existing pattern

- Build in an isolated copy of the tree, never in the live tree, and hold the result for merge.

- Follow the existing provider client's shape: same request/response handling, same error paths, same settings plumbing.

- Keep the provider behind its own enable flag so it is off until the user turns it on.

## Add the Providers-tab block

- Add a block for the new provider in the Providers tab with an enable checkbox.

- Add a key field for the provider that stores its value in the vault, never in plain text in settings or in the repo.

- Keep the block consistent with the existing provider blocks so the tab stays uniform.

## Verify with fake transports

- Verify against fake providers, not live ones: the standard method is the fake-provider-verification skill (S58, BNB SKILLS) and the fake-provider-servers tool (T19, BNB TOOLS) — a fake Ollama and a fake OpenAI-compatible server with failure modes (dead, slow, mid-stream RST, bad-key 401 never retried, server-death), request recording, and a key-leak grep over the run files. Proven across OLLAMA-SYSTEM-TEST v3/v4/v5 and DUO v0.1–v0.3.

- Run the existing provider test suite and keep it green; add tests for the new provider on the same pattern.

- Do not make a live API call as part of verification unless the user explicitly asks for one.

## Report honestly

- Say plainly in your report that no live call has been made yet, when that is true.

- Name what was verified (wiring, UI block, fake-transport tests) and what still needs a live call with a real key.

- Never claim the provider works end to end until a live call has actually succeeded.

## Standing rules

- Keep everything hard $0: no paid tier, no trial that converts, no key that costs money to obtain.

- Build in an isolated copy and hold for merge; never ship straight from the build copy.

- Never claim more than was checked.

## Source

- Audit S32. Proven in the Free AI trials thread (EXAONE provider) and the Gemini Decisions lane, same shape both times.
