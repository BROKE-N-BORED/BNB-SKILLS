# BNB SKILLS

Reusable agent playbooks distilled from real work in Joshua's chats. Each skill is a folder containing a `SKILL.md` playbook (plus a `skill.yaml` and supporting files where the skill needs them). A skill teaches an agent how to do one kind of task well: when to use it, the procedure, and what to check before calling it done.

Built from the audit in [docs/AUDIT.md](docs/AUDIT.md) (2026-11-12, all 67 chats read: main chat plus 66 side chats, 73 raw workflow candidates deduped to 52 net-new skills). First delta scan the same evening (scan window ~17:54–19:00 EST) added 7 more skills (S53–S59) and updates to 11 existing skills. S60 (side-quest) was added later the same evening from Joshua's main-chat concept. S61 (debug-log-layer) was added the same evening from his main-chat order for a debug layer in every project build. Second delta scan (2026-11-13, window ~19:13 EST 2026-11-12 → ~10:00 EST) added 5 more skills (S62–S66) and updates to 13 existing skills; its tools (T22–T23) and tool updates live in BNB-TOOLS. Third delta scan the same evening (2026-11-13, window ~10:00–19:53 EST) added 6 more skills (S67–S72) and updates to 19 existing skills; its tools (T24–T25) and tool updates live in BNB-TOOLS.

## Start here

Read these six first, in this order — they are the house operating system everything else runs on:

1. S53 — [`no-stalling-task-list-cycle`](no-stalling-task-list-cycle/) — verify, ship, next item, repeat until the list is done.
2. S54 — [`pre-delivery-enhancement-gate`](pre-delivery-enhancement-gate/) — the mandatory enhancement gate before every delivery.
3. S1 — [`ship-pipeline`](ship-pipeline/) — verify, push, Release, SHA-256 hash-match.
4. S2 — [`isolated-copy-build-merge`](isolated-copy-build-merge/) — build in an isolated copy, delta-port, verify, run the merged-tree battery.
5. S60 — [`side-quest`](side-quest/) — when the main build hits a wall, build the smallest standalone thing that fills the gap.
6. S61 — [`debug-log-layer`](debug-log-layer/) — every project ships with logging, error handling, and an emailable debug report.

Then work by tier: Tier 1 next, Tier 2 as needed, Tier 3 only when its niche comes up.

## How to use a skill

- One folder is one skill. The folder name is the skill slug.
- `SKILL.md` is the playbook. Read it before doing the task it covers.
- `skill.yaml` beside it carries exactly 7 keys, in this order: `name`, `title`, `description`, `category`, `include_in_prompt`, `number`, `tier`.
- Supporting files live in the same folder where the skill needs them, in two kinds of subfolder:
  - `references/` — background reading: checklists, brief templates, and notes the playbook points at. Read, don't copy.
  - `templates/` — copy-and-fill: files meant to be copied and filled in for a specific task.
  - A few skills also carry an `examples/` folder of worked examples.
  - Every supporting file is referenced by filename from its own skill's `SKILL.md`.
- No skill ships scripts. Skills are playbooks, not code. The executable halves of some skills live in the companion repo, BNB TOOLS. The repo-level `scripts/` folder holds library tooling instead: `generate_catalog.py` (builds `skills.json`) and `check_library.py` (validates the whole library).
- `skills.json` at the repo root is a machine-readable catalog of all 72 skills, generated from the tree. It is GENERATED — do not hand-edit it. Regenerate with `python3 scripts/generate_catalog.py`.
- Connectors: most skills need none. The skills that touch a live service use the GitHub connector, the Gmail connector, or the custom-connector-setup skill — see [CONNECTORS.md](CONNECTORS.md).
- Run `python3 scripts/check_library.py` to validate the library (README tables, yamls, titles, supporting-file references, absolute paths, placeholders). It also runs in CI on every push and pull request.

### `include_in_prompt`

`include_in_prompt` marks whether a skill belongs in the agent's prompt by default. The rule is by tier:

- Tier 1 skills: `include_in_prompt: true`
- Tier 2 and Tier 3 skills: `include_in_prompt: false`

No loader in the workspace reads this key today (checked 2026-11-12 across the custom skills and the Code Forge trees) — the value is a convention for future loaders. Tier 1 is the house operating system and belongs in the prompt; everything else is loaded on demand.

## Tiers

- **Tier 1 — the house operating system.** Used across nearly every build thread. Learn these first.
- **Tier 2 — repeated, solid, project-spanning.** Used more than once, or built to be reused across projects.
- **Tier 3 — niche / weak / single-use.** Included for completeness, built last. Some carry caveats in the skill itself: S47 is a guarded safety playbook, S50 was stated but never executed in-thread, S51 and S52 are weak.

## All 72 skills

### Tier 1 — the house operating system

| # | Skill | Description | Tier |
|---|---|---|---|
| S1 | [`ship-pipeline`](ship-pipeline/) | Verify, push, Release, SHA-256 hash-match: the one shipping sequence | 1 |
| S2 | [`isolated-copy-build-merge`](isolated-copy-build-merge/) | Build in an isolated copy, delta-port the change, verify, run the merged-tree battery | 1 |
| S3 | [`cross-thread-dispatch`](cross-thread-dispatch/) | Send self-contained briefs to the owning thread and report completions back with verified facts | 1 |
| S4 | [`task-receipt-format`](task-receipt-format/) | Close every build task with a fixed proof block: files, tests, verification, honest gaps | 1 |
| S5 | [`full-product-review`](full-product-review/) | Read the whole codebase end to end and deliver strengths, weaknesses, gaps, ranked improvements | 1 |
| S6 | [`linux-release-packaging`](linux-release-packaging/) | Icon, double-click GUI installer, menu entry, installer self-verification | 1 |
| S7 | [`name-availability-check`](name-availability-check/) | Check GitHub exact-name plus the web before presenting any name | 1 |
| S8 | [`post-merge-battery`](post-merge-battery/) | Full suite before and after a change; clean only if the failure set matches baseline | 1 |
| S9 | [`screenshot-driven-diagnosis`](screenshot-driven-diagnosis/) | Read the user's screenshot, find the real cause in the code, send an ordered fix spec | 1 |
| S10 | [`daily-sweep-pass-only`](daily-sweep-pass-only/) | Scheduled scan against fixed criteria; report only items that pass | 1 |
| S11 | [`deep-research-artifact`](deep-research-artifact/) | Deep research into a sourced report plus an interactive artifact page | 1 |
| S12 | [`external-tool-adaptation-study`](external-tool-adaptation-study/) | Research an external product, map its features onto your own project as a tiered list | 1 |
| S13 | [`model-sweep-roster-audit`](model-sweep-roster-audit/) | Grade candidate models against the machine and judge them against incumbent roster seats | 1 |
| S14 | [`guided-build-walkthrough`](guided-build-walkthrough/) | One step at a time with exact settings and a pass/fail gate before the next step | 1 |
| S15 | [`debug-sweep-repair`](debug-sweep-repair/) | Bare "debug it": full inspection, find real faults, fix them in place | 1 |
| S16 | [`read-only-security-audit`](read-only-security-audit/) | Frozen read-only scope, severity-ranked findings, every decisive claim re-verified in code | 1 |
| S53 | [`no-stalling-task-list-cycle`](no-stalling-task-list-cycle/) | Verify, push, Release, email, then immediately the next task-list item; repeat until the list is done | 1 |
| S54 | [`pre-delivery-enhancement-gate`](pre-delivery-enhancement-gate/) | Run the mandatory enhancement gate silently before every reply, delivery, or task completion | 1 |
| S60 | [`side-quest`](side-quest/) | When the main build hits a wall, build the smallest standalone thing that fills the gap | 1 |
| S61 | [`debug-log-layer`](debug-log-layer/) | Every project ships with logging, error handling, and an emailable debug report | 1 |

### Tier 2 — repeated, solid, project-spanning

| # | Skill | Description | Tier |
|---|---|---|---|
| S17 | [`reference-sheet-character-pipeline`](reference-sheet-character-pipeline/) | Multi-view sheet, per-piece build, assemble, verify view by view, save as preset | 2 |
| S18 | [`trace-and-overlay-verification`](trace-and-overlay-verification/) | Verify a 3D model against its reference sheet by measurement, not eyeballing | 2 |
| S19 | [`github-repo-creation-walkthrough`](github-repo-creation-walkthrough/) | Exact phone steps to create an empty repo, plus the publish gate checklist | 2 |
| S20 | [`repo-identity-check`](repo-identity-check/) | Verify a repo exists live, is empty or has expected content, and matches the description | 2 |
| S21 | [`brand-matched-logo-design`](brand-matched-logo-design/) | Brand DNA brief, concept rounds, 12-test battery; anti-slop rules throughout | 2 |
| S22 | [`role-prompt-engineering`](role-prompt-engineering/) | 12-section master role pack under a hard 8,000-character limit, verified exactly | 2 |
| S23 | [`species-dossier-simulation-pipeline`](species-dossier-simulation-pipeline/) | Real species to buildable sim entity: dossier, gap register, pilot build, verification | 2 |
| S24 | [`sandbox-first-sim-build`](sandbox-first-sim-build/) | Standalone sandbox file first, human-style testing, numeric measurement, screenshot rig | 2 |
| S25 | [`video-workflow-extraction`](video-workflow-extraction/) | Watch the video all the way through, extract the real workflow, give an honest critique | 2 |
| S26 | [`promo-video-production`](promo-video-production/) | Promo videos from the real product only, cut to the sellable-ads structure | 2 |
| S27 | [`social-account-setup-kit`](social-account-setup-kit/) | Paste-ready kit per platform, one platform at a time, gating rules checked first | 2 |
| S28 | [`donate-support-wiring`](donate-support-wiring/) | Payment link verified live, then wired into README, Linktree, and an in-app screen | 2 |
| S29 | [`hotfix-zip`](hotfix-zip/) | One-file patch of the exact shipped build, diffed, tested, emailed and Sent-verified | 2 |
| S30 | [`brand-scrub-rename`](brand-scrub-rename/) | Grep-driven whole-tree rename with straggler catch and state migrations | 2 |
| S31 | [`phone-first-crash-course`](phone-first-crash-course/) | One concept per lesson, grounded in the user's hardware, short single-line commands | 2 |
| S32 | [`openai-compatible-provider-wiring`](openai-compatible-provider-wiring/) | Add a new cloud provider to Forge on the existing provider pattern | 2 |
| S33 | [`living-document-build`](living-document-build/) | One master document as the single source of truth, plus consistency, gap, and live-simulation audits | 2 |
| S34 | [`covert-questionnaire-character-profile`](covert-questionnaire-character-profile/) | Long covert questionnaire, one question at a time, decoded into one character at the end | 2 |
| S35 | [`ui-direction-mockup-rounds`](ui-direction-mockup-rounds/) | Find a UI direction by rounds of mockups, one variable at a time, then lock the winner | 2 |
| S36 | [`rebuild-better-game-clone`](rebuild-better-game-clone/) | Research a game, build an improved single-file offline version, playtest it headlessly | 2 |
| S37 | [`play-based-game-design-study`](play-based-game-design-study/) | Build a game-design reference library by actually playing games against a fixed itinerary sheet | 2 |
| S38 | [`pace-adaptive-study-itinerary`](pace-adaptive-study-itinerary/) | Schedule from a seed pace, then recalculate all dates from measured real pace | 2 |
| S39 | [`sprite-sheet-prompt-pack`](sprite-sheet-prompt-pack/) | Character-lock block plus one prompt per action for consistent game art | 2 |
| S40 | [`token-burn-rate-baseline`](token-burn-rate-baseline/) | Usage baseline, scheduled recheck, tokens per day and pool-lifetime estimate | 2 |
| S41 | [`song-key-bpm-mashup`](song-key-bpm-mashup/) | Key and BPM lookup plus mashup compatibility: key families, BPM anchor, semitone shifts | 2 |
| S42 | [`live-local-stock-verification`](live-local-stock-verification/) | Same-day pickup without a wasted trip: verified items separate from phone leads | 2 |
| S43 | [`authority-incident-report-drafting`](authority-incident-report-drafting/) | Formal reports for authorities: never-guess blanks, fact/belief separation, SEND vs private versions | 2 |
| S44 | [`photo-guided-vehicle-diagnosis`](photo-guided-vehicle-diagnosis/) | Diagnose a vehicle electrical fault from fuse-box photos with ordered elimination tests | 2 |
| S45 | [`idea-to-newspaper-comic`](idea-to-newspaper-comic/) | Any idea into a classic 3 to 4 panel newspaper comic, drawn visually, never labelled | 2 |
| S46 | [`verified-reference-image-list`](verified-reference-image-list/) | Expand a reference-image list, check every URL live, record honest gaps | 2 |
| S55 | [`dual-model-ai-relay`](dual-model-ai-relay/) | Two models side by side with a director layer; blind/aware AI-to-AI relay with turn cap and stop conditions | 2 |
| S56 | [`org-repo-audit-queue`](org-repo-audit-queue/) | Audit every repo in a GitHub account one at a time from a live queue file | 2 |
| S57 | [`bnb-repo-manager-delta-scan`](bnb-repo-manager-delta-scan/) | Watermark-based delta scan of all chat threads against the BNB repo baselines | 2 |
| S58 | [`fake-provider-verification`](fake-provider-verification/) | Verify against scripted fake Ollama and OpenAI-compatible servers with failure modes and request recording | 2 |
| S59 | [`qt-ui-thread-offload`](qt-ui-thread-offload/) | Move blocking work off the Qt UI thread into a QThread worker; debounce rapid controls | 2 |
| S62 | [`un-stall-sweep`](un-stall-sweep/) | When the user returns, sweep all build threads for verified-but-unshipped builds behind expired approval cards; verify live state first, retry only the genuinely stuck pushes | 2 |
| S63 | [`qt-gui-proof-harness`](qt-gui-proof-harness/) | Qt GUI proof scripts that cannot hang: safety watcher, real-button dialog drives, harness-applied theme, timeouts, stderr checks | 2 |
| S64 | [`audit-each-one-combine`](audit-each-one-combine/) | Audit a list one item at a time with the same report shape, combine into one prioritized list, verify the combine by script | 2 |
| S65 | [`audit-findings-task-list-merge`](audit-findings-task-list-merge/) | Fold a later audit's findings into an existing task list: overlaps fold in, new findings get continued IDs, coverage verified by script | 2 |
| S67 | [`low-usage-state-capture`](low-usage-state-capture/) | When usage is nearly out, order every work thread to write its task list in its own thread — list only, no new work — so the next session starts from written state | 2 |
| S68 | [`paper-to-build-translation`](paper-to-build-translation/) | Translate a research paper's mechanism into a shipping feature on a machine the paper never considered, keeping the evidence claims honest | 2 |
| S69 | [`restart-recovery`](restart-recovery/) | Recover a builder killed by a runtime restart: judge liveness by output, never resume twice, dispatch a fresh finisher, tell the user plainly | 2 |
| S70 | [`ui-design-source-library`](ui-design-source-library/) | Seed and maintain a design source library repo: charter with the bar, techniques from live software with exact numbers, uploads diffed before adding | 2 |
| S71 | [`roadmap-first-manual`](roadmap-first-manual/) | Write a long manual from a table-of-contents roadmap: chapters one at a time, every number verified against sources or by measurement before pushing | 2 |

### Tier 3 — niche / weak / single-use

| # | Skill | Description | Tier |
|---|---|---|---|
| S47 | [`live-symptom-triage`](live-symptom-triage/) | Real-time triage for a suspected supplement/drug reaction; guarded playbook only, escalate, don't diagnose | 3 |
| S48 | [`vlc-iptv-setup`](vlc-iptv-setup/) | Find the real stream links behind a TV site and set them up in VLC on Android | 3 |
| S49 | [`free-track-enrollment`](free-track-enrollment/) | Enroll in a free course via a browser task: free/audit track only, never paid, never payment info | 3 |
| S50 | [`email-zip-code-intake`](email-zip-code-intake/) | Codebase intake from an emailed source zip, plus dead-button diagnosis; stated but never executed in-thread | 3 |
| S51 | [`pc-spec-review-upgrade`](pc-spec-review-upgrade/) | Spec file to bottlenecks to cheapest compatible parts; weak, shopping overlap | 3 |
| S52 | [`pantry-constrained-recipe-adaptation`](pantry-constrained-recipe-adaptation/) | Adapt a recipe to what the user has and format it to match the target app; weak | 3 |
| S66 | [`atomic-file-saves`](atomic-file-saves/) | Save by writing to a temp file and atomically renaming over the target, so a failed save leaves the previous file intact | 3 |
| S72 | [`paid-service-viability-filter`](paid-service-viability-filter/) | Decide which projects survive as paid online services: map the credit fit, cut everything an existing free product beats, keep the survivors ranked | 3 |

## Skills that live outside this repo

Six custom skills already existed before this audit and are NOT duplicated here. They live in the custom-skills folder in your Muse install:

- `answer_the_question_as_asked`
- `check_constraints_before_acting`
- `fix_defects_in_place`
- `one_item_at_a_time`
- `verify_attachment_before_claiming_sent`
- `verify_like_the_user`

## How to add a new skill

- Make a folder named with the skill slug (lowercase, hyphenated).
- Write `SKILL.md` in the house format: title, when to use, procedure sections, checks, available connectors, alternatives for better results. Match the existing skills: plain second person, one idea per bullet, no filler. Number the playbook title with its `S<n> — ` prefix.
- Add a `skill.yaml` beside it with exactly the 7 keys, in order: `name`, `title`, `description`, `category`, `include_in_prompt`, `number`, `tier`. The `number` value is the skill's S-number as a string (e.g. `number: "S62"`).
- Set `include_in_prompt` by tier: `true` for Tier 1, `false` for Tier 2 and Tier 3 (see above).
- Add supporting files in the same folder only where the skill needs them: background reading goes in `references/`, copy-and-fill files go in `templates/`. Reference every supporting file by filename from the `SKILL.md`.
- Add a row to the right tier table above, in number order, with the right tier — and a relative link to the skill folder.
- Run `python3 scripts/check_library.py` and `python3 scripts/generate_catalog.py` to validate the library and regenerate `skills.json`.
- Ground the skill in work actually done. Do not invent a workflow. If a skill was stated but never executed, say so in the skill itself, as S50 does.

## License

This repo is MIT-licensed — see [LICENSE](LICENSE).
