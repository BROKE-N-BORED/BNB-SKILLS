# BNB SKILLS

Reusable agent playbooks distilled from real work in Joshua's chats. Each skill is a folder containing a `SKILL.md` playbook (plus a `skill.yaml` and supporting files where the skill needs them). A skill teaches an agent how to do one kind of task well: when to use it, the procedure, and what to check before calling it done.

Built from `~/workspace/bnb-skills-tools/AUDIT.md` (2026-11-12, all 67 chats read: main chat plus 66 side chats, 73 raw workflow candidates deduped to 52 net-new skills). First delta scan the same evening (scan window ~17:54–19:00 EST) added 7 more skills (S53–S59) and updates to 11 existing skills.

## How to use a skill

- One folder is one skill. The folder name is the skill slug.
- `SKILL.md` is the playbook. Read it before doing the task it covers.
- `skill.yaml` beside it carries the name, title, and description.
- Supporting files (references, scripts, templates) live in the same folder where the skill needs them.
- Skills are playbooks, not code. The executable halves of some skills live in the companion repo, BNB TOOLS.

## Tiers

- **Tier 1 — the house operating system.** Used across nearly every build thread. Learn these first.
- **Tier 2 — repeated, solid, project-spanning.** Used more than once, or built to be reused across projects.
- **Tier 3 — niche / weak / single-use.** Included for completeness, built last. Some carry caveats in the skill itself: S47 is a guarded safety playbook, S50 was stated but never executed in-thread, S51 and S52 are weak.

## All 59 skills

| # | Skill | Description | Tier |
|---|---|---|---|
| S1 | `ship-pipeline` | Verify, email, push, Release, SHA-256 hash-match: the one shipping sequence | 1 |
| S2 | `isolated-copy-build-merge` | Build in an isolated copy, delta-port the change, verify, run the merged-tree battery | 1 |
| S3 | `cross-thread-dispatch` | Send self-contained briefs to the owning thread and report completions back with verified facts | 1 |
| S4 | `task-receipt-format` | Close every build task with a fixed proof block: files, tests, verification, honest gaps | 1 |
| S5 | `full-product-review` | Read the whole codebase end to end and deliver strengths, weaknesses, gaps, ranked improvements | 1 |
| S6 | `linux-release-packaging` | Icon, double-click GUI installer, menu entry, installer self-verification | 1 |
| S7 | `name-availability-check` | Check GitHub exact-name plus the web before presenting any name | 1 |
| S8 | `post-merge-battery` | Full suite before and after a change; clean only if the failure set matches baseline | 1 |
| S9 | `screenshot-driven-diagnosis` | Read the user's screenshot, find the real cause in the code, send an ordered fix spec | 1 |
| S10 | `daily-sweep-pass-only` | Scheduled scan against fixed criteria; report only items that pass | 1 |
| S11 | `deep-research-artifact` | Deep research into a sourced report plus an interactive artifact page | 1 |
| S12 | `external-tool-adaptation-study` | Research an external product, map its features onto your own project as a tiered list | 1 |
| S13 | `model-sweep-roster-audit` | Grade candidate models against the machine and judge them against incumbent roster seats | 1 |
| S14 | `guided-build-walkthrough` | One step at a time with exact settings and a pass/fail gate before the next step | 1 |
| S15 | `debug-sweep-repair` | Bare "debug it": full inspection, find real faults, fix them in place | 1 |
| S16 | `read-only-security-audit` | Frozen read-only scope, severity-ranked findings, every decisive claim re-verified in code | 1 |
| S17 | `reference-sheet-character-pipeline` | Multi-view sheet, per-piece build, assemble, verify view by view, save as preset | 2 |
| S18 | `trace-and-overlay-verification` | Verify a 3D model against its reference sheet by measurement, not eyeballing | 2 |
| S19 | `github-repo-creation-walkthrough` | Exact phone steps to create an empty repo, plus the publish gate checklist | 2 |
| S20 | `repo-identity-check` | Verify a repo exists live, is empty or has expected content, and matches the description | 2 |
| S21 | `brand-matched-logo-design` | Brand DNA brief, concept rounds, 12-test battery; anti-slop rules throughout | 2 |
| S22 | `role-prompt-engineering` | 12-section master role pack under a hard 8,000-character limit, verified exactly | 2 |
| S23 | `species-dossier-simulation-pipeline` | Real species to buildable sim entity: dossier, gap register, pilot build, verification | 2 |
| S24 | `sandbox-first-sim-build` | Standalone sandbox file first, human-style testing, numeric measurement, screenshot rig | 2 |
| S25 | `video-workflow-extraction` | Watch the video all the way through, extract the real workflow, give an honest critique | 2 |
| S26 | `promo-video-production` | Promo videos from the real product only, cut to the sellable-ads structure | 2 |
| S27 | `social-account-setup-kit` | Paste-ready kit per platform, one platform at a time, gating rules checked first | 2 |
| S28 | `donate-support-wiring` | Payment link verified live, then wired into README, Linktree, and an in-app screen | 2 |
| S29 | `hotfix-zip` | One-file patch of the exact shipped build, diffed, tested, emailed and Sent-verified | 2 |
| S30 | `brand-scrub-rename` | Grep-driven whole-tree rename with straggler catch and state migrations | 2 |
| S31 | `phone-first-crash-course` | One concept per lesson, grounded in the user's hardware, short single-line commands | 2 |
| S32 | `openai-compatible-provider-wiring` | Add a new cloud provider to Forge on the existing provider pattern | 2 |
| S33 | `living-document-build` | One master document as the single source of truth, plus consistency, gap, and live-simulation audits | 2 |
| S34 | `covert-questionnaire-character-profile` | Long covert questionnaire, one question at a time, decoded into one character at the end | 2 |
| S35 | `ui-direction-mockup-rounds` | Find a UI direction by rounds of mockups, one variable at a time, then lock the winner | 2 |
| S36 | `rebuild-better-game-clone` | Research a game, build an improved single-file offline version, playtest it headlessly | 2 |
| S37 | `play-based-game-design-study` | Build a game-design reference library by actually playing games against a fixed itinerary sheet | 2 |
| S38 | `pace-adaptive-study-itinerary` | Schedule from a seed pace, then recalculate all dates from measured real pace | 2 |
| S39 | `sprite-sheet-prompt-pack` | Character-lock block plus one prompt per action for consistent game art | 2 |
| S40 | `token-burn-rate-baseline` | Usage baseline, scheduled recheck, tokens per day and pool-lifetime estimate | 2 |
| S41 | `song-key-bpm-mashup` | Key and BPM lookup plus mashup compatibility: key families, BPM anchor, semitone shifts | 2 |
| S42 | `live-local-stock-verification` | Same-day pickup without a wasted trip: verified items separate from phone leads | 2 |
| S43 | `authority-incident-report-drafting` | Formal reports for authorities: never-guess blanks, fact/belief separation, SEND vs private versions | 2 |
| S44 | `photo-guided-vehicle-diagnosis` | Diagnose a vehicle electrical fault from fuse-box photos with ordered elimination tests | 2 |
| S45 | `idea-to-newspaper-comic` | Any idea into a classic 3 to 4 panel newspaper comic, drawn visually, never labelled | 2 |
| S46 | `verified-reference-image-list` | Expand a reference-image list, check every URL live, record honest gaps | 2 |
| S47 | `live-symptom-triage` | Real-time triage for a suspected supplement/drug reaction; guarded playbook only, escalate, don't diagnose | 3 |
| S48 | `vlc-iptv-setup` | Find the real stream links behind a TV site and set them up in VLC on Android | 3 |
| S49 | `free-track-enrollment` | Enroll in a free course via a browser task: free/audit track only, never paid, never payment info | 3 |
| S50 | `email-zip-code-intake` | Codebase intake from an emailed source zip, plus dead-button diagnosis; stated but never executed in-thread | 3 |
| S51 | `pc-spec-review-upgrade` | Spec file to bottlenecks to cheapest compatible parts; weak, shopping overlap | 3 |
| S52 | `pantry-constrained-recipe-adaptation` | Adapt a recipe to what the user has and format it to match the target app; weak | 3 |
| S53 | `no-stalling-task-list-cycle` | Verify, push, Release, email, then immediately the next task-list item; repeat until the list is done | 1 |
| S54 | `pre-delivery-enhancement-gate` | Run the mandatory enhancement gate silently before every reply, delivery, or task completion | 1 |
| S55 | `dual-model-ai-relay` | Two models side by side with a director layer; blind/aware AI-to-AI relay with turn cap and stop conditions | 2 |
| S56 | `org-repo-audit-queue` | Audit every repo in a GitHub account one at a time from a live queue file | 2 |
| S57 | `bnb-repo-manager-delta-scan` | Watermark-based delta scan of all chat threads against the BNB repo baselines | 2 |
| S58 | `fake-provider-verification` | Verify against scripted fake Ollama and OpenAI-compatible servers with failure modes and request recording | 2 |
| S59 | `qt-ui-thread-offload` | Move blocking work off the Qt UI thread into a QThread worker; debounce rapid controls | 2 |

## Skills that live outside this repo

Six custom skills already existed before this audit and are NOT duplicated here. They live in `~/workspace/custom-skills/`:

- `answer_the_question_as_asked`
- `check_constraints_before_acting`
- `fix_defects_in_place`
- `one_item_at_a_time`
- `verify_attachment_before_claiming_sent`
- `verify_like_the_user`

## How to add a new skill

- Make a folder named with the skill slug (lowercase, hyphenated).
- Write `SKILL.md` in the house format: title, when to use, procedure sections, checks, available connectors, alternatives for better results. Match the existing skills: plain second person, one idea per bullet, no filler.
- Add a `skill.yaml` beside it with name, title, description, category, and `include_in_prompt: false`.
- Add supporting files in the same folder only where the skill needs them.
- Add a row to the table above, in number order, with the right tier.
- Ground the skill in work actually done. Do not invent a workflow. If a skill was stated but never executed, say so in the skill itself, as S50 does.

License: TBD — Joshua's call, not set yet.
