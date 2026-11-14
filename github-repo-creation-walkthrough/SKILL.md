# S19 — GitHub repo creation walkthrough

Walk the user through creating an empty GitHub repo from their phone, verify it live from the agent side, and run the publish gate when the project is ready to go public.

## When to use

- A project needs its first repo.
- An existing private repo is ready to publish.

## Walk the user through creating an empty repo

- Give the exact phone steps in order, naming each tap, starting from the new repository screen.

- Tell the user to set the repo name exactly as agreed, and to pick Public visibility.

- Tell the user to leave ALL checkboxes off, with no README, no .gitignore, and no license, because any file the creation step adds will collide with the first push.

- Tell the user what the app-access check is, that the Meta Muse AI app needs access to the new repo, either by adding the repo to the app's access list or by switching the app to All repositories, and wait for the user to confirm that step is done.

- Keep each instruction short and single-action, because the user is following the steps on a phone.

## Verify the repo live from the agent side

- Check the repo exists on GitHub and is readable from the agent side as soon as the user says it is created, and do not proceed on the user's word alone.

- Check whether the repo is empty, and note any discrepancy plainly, such as a repo that is private instead of public, a name with different capitalization than agreed, or a placeholder README that means a checkbox was left on. A repo name that differs from the agreed name by even one letter is a discrepancy too — ask which spelling is the name before pushing: the repo said qwkhnd-4-linux while the picked name was Qkhnd (QWKHND, 2026-11-13 14:51); he picked Qwkhnd and the build was re-renamed before the push.

- Report the verification result with the evidence, including the repo URL, its visibility, and whether it is empty.

- Fix a placeholder README or other stray file only as part of the publish gate or the first push, and say which one it will be, instead of silently tidying it.

## Run the publish gate checklist

- Split the publish gate into owner-only items and agent items, and never present an owner-only item as something the agent can do.

- Name the owner-only item first, that only the owner can flip the repo from Private to Public, and that it is a quick toggle the owner does at launch time.

- Do the agent items in order, replacing a placeholder README with the real one, adding the LICENSE file, creating the Release with the zip attached, and filling in the About description and topics.

- Keep the license pick as a separate owner decision, and ask the user which license they want before adding the LICENSE file, instead of choosing one for them.

- Use the [publish gate checklist](references/publish-gate-checklist.md) so no item is skipped, and report each item as done or still open.

## Where this comes from

- From the CODE-FORGE repo creation in the Implement prompts in Code Forge thread (b026eda9); the same create-then-verify dance repeated for PIXEL-FORGE, MIMIK, WinLinx, STELLA, and OLLAMA-SYSTEM-TEST. Recorded in the BNB audit as S19.

## Available connectors

- Use the [GitHub connector](../CONNECTORS.md) for repo checks, pushes, and releases, and read its current doc before running its commands.

## Alternatives for better results

- Offer to draft the README and About text while the user creates the repo, so the publish gate has nothing left to write.

- Ask the user to send a screenshot of the repo page when a discrepancy is unclear, instead of guessing what the creation step did.
