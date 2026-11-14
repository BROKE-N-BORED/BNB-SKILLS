# S7 — Name-availability check

Executable twin in BNB-TOOLS: [T4 name-check](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/name-check).

## When to use

- Use this skill before presenting any name for a new project, product, app, or repo.
- Check every candidate name, not just the favourite, so the user picks from a list that is already clean.
- Never present a name you have not checked — and never present a name AS checked when it was not. This rule was born from a real failure: the user created a repo for an unchecked name that was already taken. It was broken again in the Shorthand thread (2026-11-13 14:01–14:16): "Shrthnd" was presented as "all GitHub-safe" without ever being checked, and it was taken — four exact-name repos, a live AI product at shrthnd.ai, and an npm package. The user had already decided on it. A name on a "checked" list must have both checks run; anything else is a lie by presentation.

## Check GitHub and the web for each name

- Search GitHub for a repo with the exact name, and count the exact-name matches.
- Search the web for a live product, site, or service with that name, and open the top results to see whether the name is actually in use.
- Treat a same-name product in a different field as a collision worth reporting, and let the user decide whether it matters.
- When testing whether a remote file or repo is absent, check the error flag on the result rather than the success flag, because the GitHub file read returns success with an error flag set for missing files.

## When a check is blocked, hold the list — or show it with the caveat

- When GitHub rate-limits (429) mid-sweep, stop instead of hammering it, and hold the list until the blocked half clears. The FYRN sweep (2026-11-13 18:43) stopped at the web half: 48 checked, 13 clean on the web, GitHub half pending.
- Never present an unverified name as clean. The RIZA sweeps left 27 (round 2) and 61 (round 3) names web-clear but GitHub-unverified — none of them was presented as clean.
- If he demands the list anyway, show the web-clean names WITH the pending-check caveat stated plainly, and run the full check on his pick first: "All 13 are clean on the web. GitHub half still pending, so a couple could still die there. Pick one you like and I'll run the GitHub check on it first." (FYRN, 2026-11-13 18:46).
- Re-verify the pick before the repo is created when the sweep was rate-limited: the RIZA round-3 shortlist was presented with GitHub counts not re-run (GitHub 429-hot), so the pick needed a fresh check first.

## Present only verified-clean names

- Present only the names that came back clean on both checks, with the evidence for each one.
- List the dead names separately, each with the reason it died, so the user can see what was ruled out and why.
- Keep a dead name dead. Do not re-present it in a later round without new evidence that the collision is gone.
- His taste rules, stated 2026-11-13: no Q names (FYRN 18:47, RIZA 18:50 — he rejected Q-names twice in one evening) and no letter-prefix coined names — no V/X/Z/K prefixes (RIZA 19:02: "Stop naming shit with letters like that, it's fucking goofy as fuck"). Plain descriptive names only. Qwkhnd predates the rule (picked 15:03) and stands.
- When a name is taken globally but free inside his org, report the collision plainly with its scale and let him decide — do not decide for him. He kept Fyrn (6 tiny zero-star repos, FYRN 18:53), Rhiza→RIZA (14 exact-name repos + a live PyPI package, RIZA 19:14), and Gitdata (a dozen repos + an active org + live PyPI packages, GITDATA 15:01). In each case the org name was free to create and he chose to keep it.
- Once he picks a name and the repo exists, naming is closed. Do not re-offer names on a stale tap: FYRN 19:42, "We alrwdy have a fucjing name" — the assistant re-offered names after Fyrn was settled and the repo created, misreading an old tap as a change of mind.
- Flag a live-brand near-collision once, then drop it after he decides: HicksField sits close to Higgsfield, a live company's brand (HICKSFIELD, 2026-11-13 19:38). He kept it ("Im keeping thats none if your concern", 19:41) — the flag is not re-raised.

## Where this comes from

- This check ran for the study portal (24 candidates, 7 clean), WinLinx (three rounds totalling 77 names, with WinLink dead as a ham-radio email system plus 13 repos), EveryMouse, Stella, and the Universal Study Portal. It is recorded in the BNB audit as S7.
- The 2026-11-13 evening naming rounds (RIZA: 4 rounds, 491 names checked; FYRN; QWKHND; GITDATA; HICKSFIELD) added the rate-limit, taste-rule, taken-globally, and settled-name rules above.

## Available connectors

- [GitHub](../CONNECTORS.md) for checking exact-name repos.

## Alternatives for better results

- Offer to check spelling variants of a favourite name when the exact name is dead.
- Offer to re-check a shortlist right before the repo is created, in case a name was taken since the first check.
