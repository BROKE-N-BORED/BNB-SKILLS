# S20 — Repo-identity check

Verify a GitHub repo live before you build against it or push to it, and judge whether an existing repo matches the user's description of a project.

Companion tool: [T10 repo-identity-check](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/repo-identity-check) — checks GitHub existence, empty state, and description for a repo name, and handles the get_file_contents ok plus isError trap.

## When to use

- At the start of any new project.
- Before any push.
- Whenever the user asks whether a project already exists on GitHub.

## Check existence and contents live

- Check the repo live on GitHub, and report whether it exists or not, with the URL as evidence.

- Check whether the repo is empty or has content, and name what is in it when it is not empty, so a push never lands blind on unexpected files.

- Check the repo's visibility, and note when it is private, because a private repo changes what the user can see and what the agent can do with it.

- Run this check before building or pushing, never after, and never assume a repo exists or is empty because the user thinks it is.

## Judge a match against the user's description

- Read the repo's description and README when the question is whether an existing repo is the project the user means.

- Re-check the description and topics live at report time — do not trust a listing from earlier in the day. Repo metadata changes within hours (OpenRealism's and FRIDAY's descriptions both changed on 2026-11-12 between the morning listing and the evening audits). If the live description disagrees with what you planned to write, the live one wins.

- Compare what the repo says it is against what the user described, and name the points that match and the points that do not.

- Put the match to the user as a question, such as whether the repo you found is the project they meant, instead of assuming it is and building on it.

- Say plainly when no repo matches, including when a search turns up similarly named repos that are different projects, and name what the search did find.

## Watch for the missing-file trap

- Check the `isError` field on a `get_file_contents` result, not just the `ok` field, because the call returns `ok: true` with `isError: true` for a missing file.

- Treat a result with `isError: true` as the file being absent, and say so, instead of treating the call as a success.

- Apply the same care to every GitHub read, and report what the call actually returned when a result looks contradictory.

## Where this comes from

- From the Stella repo checks — the Stella crash course thread (8fc2998a), where no repo named Stella/Stellar existed and private StemLab matched the description almost exactly, and STELLA Dev (2d7b2739), where the STELLA repo was verified to exist and be empty — plus the OLLAMA thread (662fb3aa) and the WinLinx repo verification in the main chat. Recorded in the BNB audit as S20.

## Available connectors

- Use the [GitHub connector](../CONNECTORS.md) for repo checks, and read its current doc before running its commands.

## Alternatives for better results

- Offer to create the repo with the [github-repo-creation-walkthrough](../github-repo-creation-walkthrough/SKILL.md) skill when the check shows it does not exist yet.

- Ask the user for the exact repo name or a link when a name search returns several close matches.
