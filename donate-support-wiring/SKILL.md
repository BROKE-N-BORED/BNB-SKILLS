# S28 — Donate support wiring

Wire a donation link into a project, from the payment page through the README and Linktree to an in-app startup welcome screen.

## When to use

- A project needs a way for people to support it.

## Explain the link and verify the payment page

- Explain the link format plainly, that a Cash App link is cash.app/$cashtag, and that Cash App has no official embeddable button, so any button is just a link to that page.

- Tell the user how to find their cashtag, and ask them for it, instead of guessing it.

- Verify the live payment page shows the user's name and QR code before you wire the link anywhere, and report what the page showed.

- Do not wire a link you have not verified, because a wrong cashtag sends money to the wrong person.

## Wire the link into README and Linktree

- Add a badge button and a Support section to the GitHub README, linking to the verified payment page.

- Add a titled link on Linktree, pointing to the same verified page.

- Keep the link identical in every place it appears, and check each one after wiring.

## Build the in-app startup welcome screen

- Build a startup welcome screen that is non-blocking and close-to-run, so the user can dismiss it and get straight into the app.

- Put a donate button on the screen that opens the payment page, and render a big QR code with the app's own built-in QR encoder.

- Add a printed-link fallback on the screen, so the link is still usable when the QR code fails.

- Make the screen re-openable from the menu, so it is not lost after the first run.

- Verify the screen with targeted tests, the full test suite, and an offscreen screenshot you look at yourself, and report the results.

## Where this comes from

- From the Add donate button with Cash App thread (20dcff58) — the $XPRNC8 page verified live showing Joshua Lofland and a QR code, then wired into the README, Linktree, and a startup welcome screen, verified 11/11 targeted tests and 1713/1713 full suite plus an offscreen screenshot. Recorded in the BNB audit as S28.

## Alternatives for better results

- Offer to reuse the welcome-screen pattern for other startup content, since the non-blocking close-to-run shape works for more than donations.

- Ask the user whether they want the welcome screen on every launch or only on first launch, instead of choosing for them.
