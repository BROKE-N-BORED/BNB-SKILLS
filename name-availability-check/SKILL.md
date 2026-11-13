# S7 — Name-availability check

Executable twin in BNB-TOOLS: [T4 name-check](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/name-check).

## When to use

- Use this skill before presenting any name for a new project, product, app, or repo.
- Check every candidate name, not just the favourite, so the user picks from a list that is already clean.
- Never present a name you have not checked. This rule was born from a real failure: the user created a repo for an unchecked name that was already taken.

## Check GitHub and the web for each name

- Search GitHub for a repo with the exact name, and count the exact-name matches.
- Search the web for a live product, site, or service with that name, and open the top results to see whether the name is actually in use.
- Treat a same-name product in a different field as a collision worth reporting, and let the user decide whether it matters.
- When testing whether a remote file or repo is absent, check the error flag on the result rather than the success flag, because the GitHub file read returns success with an error flag set for missing files.

## Present only verified-clean names

- Present only the names that came back clean on both checks, with the evidence for each one.
- List the dead names separately, each with the reason it died, so the user can see what was ruled out and why.
- Keep a dead name dead. Do not re-present it in a later round without new evidence that the collision is gone.

## Where this comes from

- This check ran for the study portal (24 candidates, 7 clean), WinLinx (three rounds totalling 77 names, with WinLink dead as a ham-radio email system plus 13 repos), EveryMouse, Stella, and the Universal Study Portal. It is recorded in the BNB audit as S7.

## Available connectors

- [GitHub](../CONNECTORS.md) for checking exact-name repos.

## Alternatives for better results

- Offer to check spelling variants of a favourite name when the exact name is dead.
- Offer to re-check a shortlist right before the repo is created, in case a name was taken since the first check.
