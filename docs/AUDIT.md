# BNB SKILLS / BNB TOOLS — Full Chat Audit

**Date:** 2026-11-12
**Auditor:** coordinator + 5 worker subagents (worker files: `worker-A.md` … `worker-E.md` in this directory)
**Scope:** 67 chat threads read (main chat + 66 side chats). The audit-request chat itself (`089d9759`) was skipped as a source. Every thread below is accounted for — including threads checked with nothing reusable.
**Method:** each worker actually read its assigned chats with `chat.read_messages` (20 turns/page, multiple pages for big threads, newest first), plus `~/MEMORY.md` and `~/workspace/custom-skills/` to avoid proposing duplicates. Workflows are grounded in things actually done in the threads — nothing invented.

## Headline counts

| | Count |
|---|---|
| **Net-new SKILLS proposed (BNB SKILLS)** | **52** |
| **Net-new TOOLS proposed (BNB TOOLS)** | **17** (14 pair with a skill, 3 standalone) |
| Already-built custom skills (do NOT re-propose) | 6 |
| Threads read | 67 / 67 |
| Threads with at least one workflow | 57 |
| Threads checked with nothing reusable | 10 |
| Threads unreadable | 0 |

---

# PART 1 — BNB SKILLS (master list, priority order)

Priority = most-reused / most-valuable first. "Pair" means the skill has a TOOL half listed in Part 2. Source threads are given by short chat ID; full IDs are in Part 4.

## Tier 1 — the house operating system (used across nearly every build thread)

### S1. Ship pipeline — verify → email → push → Release → hash-match — SKILL + TOOL (pair)
- **Sources:** all build threads — MIMIK (d22a66c0), Pixel Forge (b2e2291b), OLLAMA (662fb3aa), CODE FORGE DEV (94792a18), Reblend (2a82689c), Forge Browser (611e974d), WinLinx (0b4e32ae), Design Shell (d238e3ce), main chat.
- **What:** The one shipping sequence used for every single shipment: build zip with correct modes (0o100755 scripts / 0o100644 files) → verify from a fresh unzip (suite green + own checks + screenshots eyeballed) → email zip (Sent read-back: attachment name + exact byte size) → push to GitHub (read-back verify) → cut Release with zip attached → download the asset back and SHA-256-match against the local zip. Standing rules: every push gets a Release; every Release zip carries an icon + double-click installer.
- **Inputs:** verified build tree, version, changelog. **Outputs:** emailed zip, pushed commit, live Release URL, hash-match confirmation.
- **Reusability:** HIGHEST — every shipment in every project.

### S2. Isolated-copy build + delta-port merge with batteries — SKILL + TOOL (pair)
- **Sources:** CODE FORGE DEV (94792a18), GUIFX (dfc78d3f), SECURITY (f59bdf32), CodeRabbit (febd57ac), Manus/Improvement (fc98cfd5), Forge Browser (611e974d), MIMIK (d22a66c0), Pixel Forge (b2e2291b), Reblend (2a82689c), Design Shell (d238e3ce), Model Research (4b2f5ba5), Groq/Gemini (be74cb87), Prompts (b026eda9).
- **What:** Build the feature in an isolated copy of the tree (shared tree untouched while other lines run); run the lead battery there; back up the live tree; port only the delta (anchor port of named paths); verify the tree against the source copy before calling the merge clean; run the merged-tree battery; only then ship. Solo-suite rule: never run two suites at once.
- **Inputs:** live tree, feature spec. **Outputs:** merged tree + battery receipts + backup.
- **Reusability:** HIGHEST — the dominant build pattern in every dev thread, dozens of items (CR1–CR10, M1–M13, F1–F7, T2-1–T2-3, browser #1–#22, S2–S7).

### S3. Cross-thread dispatch + report-back — SKILL
- **Sources:** everywhere — main chat ↔ all DEV threads (MIMIK bridge, Blender MCP, Raon trial, die → Reblend, Victor sheets → Reblend, merge notes DEV→GITHUB, GUIFX→DEV merge notes).
- **What:** Send work to the owning thread with a self-contained brief (what, why, constraints, what to report back: file paths, sizes, counts, orientation), and report completions back with verified facts only. Merge notes carry the held build path + battery receipt so the receiving thread can delta-port.
- **Inputs:** task + context. **Outputs:** brief sent; completion report returned.
- **Reusability:** HIGHEST — the constant coordination pattern.

### S4. Task receipt format (per-task proof block) — SKILL
- **Sources:** GUIFX (dfc78d3f, every T-task), CODE FORGE DEV (94792a18), Pixel Forge (b2e2291b), MIMIK (d22a66c0).
- **What:** Close every build task with a fixed receipt: files changed (with line deltas), tests (new suite count + full-suite count + failure-set vs baseline), how it was verified (diff read, greps, renders eyeballed, fresh unzip), and honest gaps / what still needs his PC. Never claim more than was checked.
- **Inputs:** completed task. **Outputs:** receipt block in chat + (often) report file.
- **Reusability:** HIGH — used on essentially every completed task.

### S5. Full product review (strengths / weaknesses / gaps / UI / code / perf) — SKILL
- **Sources:** OLLAMA (662fb3aa), MIMIK (d22a66c0), Pixel Forge (b2e2291b), Yahtzee (b345e8db), WinLinx (0b4e32ae), Forge Browser (611e974d), repo-audit thread (b074e650), main chat. Same verbatim ask in 4 threads on 2026-11-12.
- **What:** Read the whole codebase end to end, open every tab/screen and screenshot it, time slow paths instead of guessing, probe suspected defects live rather than guessing, then deliver strengths, weaknesses, gaps, what's missing, and ranked improvements (Pixel Forge: 24 improvements in 3 tiers + avoid list; Yahtzee: P0–P4 phased plan + 25-item task list). Audit is a list for Joshua to direct from — no code changed.
- **Inputs:** project tree + built app. **Outputs:** review report (chat + file) + ranked fix list / task list.
- **Reusability:** HIGH — 5+ full reviews, same shape each time.

### S6. Linux release packaging (icon + double-click installer + menu entry) — SKILL + TOOL (pair)
- **Sources:** main chat (rule set), CODE FORGE GITHUB (7d1ee11c, retrofit + convergence), CODE FORGE DEV (94792a18), MIMIK (d22a66c0, installer fix), Pixel Forge (b2e2291b), WinLinx / Forge Browser / getcompute retrofits.
- **What:** Turn a project tree into a real Linux program: app icon (SVG source of truth, PNGs rendered at install), GUI installer (double-click `.desktop`, pkexec, fixed install location, backup/upgrade, uninstaller), `.desktop` Exec quoting that survives GLib parsing (python3 -c with %k as separate argv token), installer self-verification (deps actually installed before reporting success; fatal check + named warning if GUI can't start). Deps are core, never optional.
- **Inputs:** project tree + icon SVG. **Outputs:** installable zip / release package.
- **Reusability:** HIGH — every project ships this way; retrofit applied to 4+ older projects.

### S7. Name-availability check (GitHub exact-name + web) — SKILL + TOOL (pair)
- **Sources:** main chat (portal: 24 candidates, 7 clean), WinLinx (0b4e32ae: 29 + 28 + 20 names), EVERY MOUSE (5bb9ed96, EveryMouse), Stella (2d7b2739 / 8fc2998a), Universal Study Portal (4955a021).
- **What:** Before presenting ANY name, check GitHub for an exact-name repo and the web for a live product/site with that name; present only verified-clean names, with the dead ones listed separately and why (e.g. WinLink dead: ham-radio email system + 13 repos; StudyQuay dead: live agency). Born from a failure: Joshua created a repo for an unchecked name that was already taken. Durable rule: check before presenting.
- **Inputs:** candidate name(s). **Outputs:** clean/dead verdict per name with evidence.
- **Reusability:** HIGH — every new project needs a name.

### S8. Post-merge battery + baseline failure-set comparison — SKILL + TOOL (pair)
- **Sources:** GUIFX (dfc78d3f, every receipt: "failure set byte-identical to baseline"), CODE FORGE DEV (94792a18), SECURITY (f59bdf32, battery run twice incl. deck served-page rule).
- **What:** Run the full suite before and after a change; compare the failure lists (not just pass counts); a change is clean only if the failure set is byte-identical to baseline (or differs only by intended fixes). New failures get diagnosed against the pre-merge backup before any claim. Post-merge battery runs read-only against the merged tree, holds while the tree is changing mid-merge (discards partial results, re-runs from scratch on stability), includes the deck served-page rule (extract the served page's `<script>`, node --check it) and a phone smoke. Merge verification against the source copy (marker counts, byte-identical files) — this caught the patch tool silently reverting ~1,260 lines across 19 files while reporting "already applied".
- **Inputs:** test suite + baseline failure list + merged tree. **Outputs:** pass/fail verdict + failure diff + relayed defect notes (exact file + line).
- **Reusability:** HIGH — used on every GUIFX task and every Forge merge.

### S9. Screenshot-driven diagnosis + fix spec — SKILL
- **Sources:** CODE FORGE ERROR HANDLING (907dc170 — Gemini thought_signature 400, EXAONE 429, misleading "LOADED MODEL" label), GUIFX (dfc78d3f — header clip: true min-width 1094 vs reported 982, checked at 5 widths), Yahtzee (b345e8db — grey dice = lighting not model; cup = backface culling), OLLAMA (662fb3aa), MIMIK (d22a66c0, Hosts_Learn mnemonic bug).
- **What:** Read the user's phone screenshot, name the visible symptom in his words, find the real cause by reading the actual code (never assume a sandbox artifact — his photo proves it's real), separate real bug vs misleading label vs user error vs provider limit, give an immediate workaround, name exactly what evidence is still needed (e.g. the raw session-log line), then send an ordered fix spec to the DEV thread. Fix verified with measurements (pixel widths, geometry at multiple window sizes) rather than assertions. Ask what specifically is wrong when he rejects something before reworking.
- **Inputs:** user screenshot + description + code tree. **Outputs:** diagnosis + workaround + ordered fix spec.
- **Reusability:** HIGH — screenshots are his main bug-report channel.

### S10. Daily sweep with pass-only reporting — SKILL
- **Sources:** Stocks and Crypto Sweep (d0d4144c, daily 17:20 cron), Free AI trials (3720590d, daily ~10:20 AM $0-services sweep cron), main chat (inbox-triage 30-min scan; Raon Ollama-support watch cron), Study Dashboard (dc0566e7, verified-$0 course catalogue).
- **What:** Run a scheduled scan against fixed criteria and report ONLY items that pass — if none pass, one short line, no rejects list, no watchlist. Variants: stocks (analyst target ≥20% above price + mostly Buy; earnings beat/revenue growth/guidance raised; trend check; hard $100 cap, focus $20–$100); $0 free services (hard $0, no card, no phone/SMS verification; dedupe vs catalogue; report only new verified finds or losses, losses first); $0 courses (same verification discipline applied to education providers — 24 universities + 3 platforms checked, 18–19 pass, Coursera killed full free audit 2025-08-08, edX audit is the usable door). When a rule changes, update the cron job instructions in place so the next run follows it.
- **Inputs:** scan criteria + sources. **Outputs:** pass-only report (or one-line "nothing cleared the bar") + catalogue updates.
- **Reusability:** HIGH — daily recurring by design; same shape reused for inbox triage + Raon watch.

### S11. Deep research → report + interactive artifact — SKILL
- **Sources:** Compare CodeForge (7a4222f3 — 20 competitors + valuation), Groq/Gemini (be74cb87 — 34 free-tier models scored), Model Research (4b2f5ba5), Pixel Forge competitive research (b2e2291b — 24 ranked improvements), Reblend vs Blender (2a82689c — 163 capabilities), Meridian ground resources (da24d372 — 106-record catalog), Code Forge logo research (983a94e7 — 10-section report, 45 sources).
- **What:** Run deep research into a `report.md` (index-sourced figures with dates, vendor claims labelled separately from independent checks, conflicts and could-not-verify items flagged), give headlines in chat, then build an interactive artifact page (searchable/filterable table, expandable profiles, ranked scores) and probe-verify it (filters, no console errors, no mobile overflow). Two variants: **comparison** (ranked scores, best-for picks) and **catalog** (sourced values, plausibility gates for items needing a special deposit, copyable JSON data schema, explicit caveats for unverifiable values — never invented).
- **Inputs:** a comparison or research question. **Outputs:** research_notes/&lt;topic&gt;/report.md + interactive artifact page + chat headlines.
- **Reusability:** HIGH — done 6+ times across threads with the same shape.

### S12. External-tool adaptation study → tiered build queue — SKILL
- **Sources:** CodeRabbit research (febd57ac), Manus/Improvement (fc98cfd5), Forge Browser AI research (611e974d — 22-item improvements doc), sellable-ads research (d2fbad7e).
- **What:** Deep-research an external product/tool, write a full report to `~/workspace/research_notes/<slug>/report.md`, then map its features onto the user's own project as a tiered list (Tier 1 integrate now / Tier 2 adapt at Forge scale / skip list), each item naming the system it integrates INTO (not bolted on), with a suggested sequence. User picks items; each builds one at a time (via S2).
- **Inputs:** product name + the user's own project context (hardware limits, existing systems). **Outputs:** research report.md + tiered implementation list + (later) per-item builds.
- **Reusability:** HIGH — used 4+ times (CodeRabbit, Manus, Forge Browser AI, sellable ads).

### S13. Model sweep + roster audit (hardware-graded) — SKILL + TOOL (pair)
- **Sources:** OLLAMA SYSTEM TEST (662fb3aa — ~40-model HF 2B sweep), Model Research (4b2f5ba5 — Sweep #1/#2), STELLA Dev (2d7b2739 — Forge roster audit), Stella crash course (8fc2998a).
- **What:** Grade candidate models against the machine (RAM ceiling, CPU-only, quant size, licence, runtime compat) using vendor benchmarks flagged as unreproduced; judge against incumbent roster seats (driver/reviewer/vision/tool/fast) and produce incumbent verdicts, ranked trials with exact pull tags, a watchlist, a rejects-with-reasons list (saved as do-not-re-propose), cloud picks, and an unverified list. Audit an installed roster per seat and name the cheapest wins (e.g. Q8_0→Q4_K_M re-pull) and dead weight. Follow-up: hand-typeable `ollama pull` commands in trial order, a same-task trial test, and a pass/fail verdict from the user's screenshot. Always re-check against a fresh `ollama list` — never trust a stale roster.
- **Inputs:** model candidates / installed roster + hardware spec. **Outputs:** graded pull list / audit report with verdicts per model.
- **Reusability:** HIGH — recurs whenever a new model (Raon) or seat opens.

### S14. Guided in-tool build walkthrough (one step, pass/fail gate, next step) — SKILL
- **Sources:** EMBER BREAK (01a04f3a — full planned form), Design Shell (d238e3ce — Unreal/Blender install walkthrough, reactive variant), Groq/Gemini (be74cb87 — Whisper error screenshot → diagnosis).
- **What:** Give the user a full map (step NAMES only) up front, then deliver ONE step at a time with exact mode/settings/prompt, state the pass criteria, and wait for the user's pass/fail report before giving the next step. Includes a model map (fixed seats set once + driver swapped per step) and a re-check step when the build underfoot changes. Reactive variant: read the user's screenshot, diagnose the exact error, give ONE short single-line hand-typeable command, repeat. (He hand-types commands from his phone screen; multi-line pastes collapse.)
- **Inputs:** a multi-step build or install the user performs on their own PC. **Outputs:** step-by-step walkthrough with pass/fail gates.
- **Reusability:** HIGH — Ember Break is the full form; the reactive form runs through the whole Design Shell thread.

### S15. Debug sweep with repair authorized ("Debug it") — SKILL
- **Sources:** Yahtzee (b345e8db — full inspection found bot soft-lock + 4 more faults, all fixed), MIMIK (d22a66c0 — review → ranked defects), CODE FORGE DEV (94792a18 — "Fix the failures" → 6 diagnosed, 4 fixes, suite 2,435/2,435 green).
- **What:** Given a bare "debug it" with no symptom, run a full inspection of the app/code, find real faults, fix them in place (per existing `fix_defects_in_place`), and report what was found + fixed + what was checked. Diagnose-only variant exists too (review inspections, see S5).
- **Inputs:** app/codebase. **Outputs:** fault list + fixes + verification.
- **Reusability:** MEDIUM-HIGH — 3 uses; distinct from S5 in that repair is authorized and expected.

### S16. Read-only security audit — SKILL
- **Sources:** CODE FORGE SECURITY DEV (f59bdf32 — S1 audit; also the code-forge-audit-2026-11-07 method: four independent review passes, decisive claims re-verified by hand).
- **What:** Freeze a read-only scope (tree + named copies, nothing touched), scan for findings, rank them Critical/High/Medium/Low, name verified-strong areas too, and re-verify every decisive claim in the code before reporting (S1: 1 Critical, 9 High, 14 Medium, 9 Low, 12 areas genuinely strong).
- **Inputs:** a codebase tree. **Outputs:** severity-ranked audit report with code-grounded findings.
- **Reusability:** MEDIUM-HIGH — done once fully (S1) plus the earlier full-codebase audit; same shape ordered for other projects.

## Tier 2 — repeated, solid, project-spanning

### S17. Reference-sheet character pipeline (per-piece build → assemble → preset) — SKILL
- **Sources:** EVERY MOUSE (5bb9ed96) + REBLEND DEV (2a82689c): Victor v2.
- **What:** Take a multi-view character reference sheet, itemize it into separate pieces (hoodie, shorts, belt, phone, shoes, tools, backpack), model each piece separately from its own sheet, assemble the character, verify view-by-view against the sheet, and save the whole thing as a reusable preset/template (part list + materials + assembly). Approval gates at itemize / per-piece / assembly. Belt-only rule example: a sheet showing tools in the belt still means model the belt empty — tools are their own piece.
- **Inputs:** reference sheets (multi-view images). **Outputs:** assembled model + preset file.
- **Reusability:** MEDIUM — one character so far, but designed as the standard way characters get made; preset workflow being built into Reblend on his order.

### S18. Trace-and-overlay verification (3D model vs reference image) — SKILL + TOOL (pair)
- **Sources:** REBLEND DEV (2a82689c — belt trace rework; 3/4-view backdrop support), EVERY MOUSE (5bb9ed96 — v2 view-by-view checks).
- **What:** Verify a 3D model against its reference sheet by measurement, not eyeballing: use the reference image as a viewport backdrop (orthographic front/side; 3/4 views via matched camera angle), measure dimensions off the image, lay the render over the sheet at the same scale, and match silhouettes/overlays. Report residual offsets honestly (e.g. ~1–2 cm vertical offset remains). Standing rule: no eyeballing.
- **Inputs:** reference sheet + model + renders. **Outputs:** overlay-match verdict + measured deltas.
- **Reusability:** MEDIUM — proven on the belt; applies to every future sheet-built piece.

### S19. GitHub repo creation walkthrough + publish gate checklist — SKILL
- **Sources:** Implement prompts in Code Forge (b026eda9 — CODE-FORGE repo creation); per MEMORY the same dance for PIXEL-FORGE, MIMIK, WinLinx, STELLA, OLLAMA-SYSTEM-TEST.
- **What:** (a) Creation walkthrough: exact phone steps to create an EMPTY repo (name, Public, ALL checkboxes off — no README/.gitignore/license, or the push collides), the app-access check (Meta Muse AI app repo access: add the repo or switch to All repositories), then live verification from the agent side (repo exists + readable; note discrepancies: private vs public, uppercase name, placeholder README from a left-on checkbox). (b) Publish gate checklist split owner-only vs agent: owner flips Private→Public at launch (10-second toggle, only the owner can); agent replaces placeholder README, adds LICENSE, creates the Release with the zip, fills About description/topics. License pick kept as a separate owner decision.
- **Inputs:** a project ready for a repo / ready to publish. **Outputs:** created + verified repo; publish checklist.
- **Reusability:** HIGH — the repo-create-then-verify dance repeats for every project.

### S20. Repo-identity check (existence + description match) — SKILL + TOOL (pair)
- **Sources:** Stella crash course (8fc2998a — no repo named Stella/Stellar; private StemLab matches the description almost exactly), STELLA Dev (2d7b2739 — STELLA repo verified exists + empty), OLLAMA (662fb3aa), main chat (WinLinx repo verified).
- **What:** Before building/pushing, verify the repo exists (or doesn't) live on GitHub, is empty or has expected content, and — for identity questions — read its description/README to judge whether it matches the user's description of a project. Never assume; put the match to him as a question. Note: GitHub get_file_contents returns ok:true with isError:true for missing files — check isError.
- **Inputs:** repo name / user description. **Outputs:** exists/empty/match verdict with evidence.
- **Reusability:** MEDIUM — used at the start of most new projects.

### S21. Brand-matched logo / glyph design (anti-slop) — SKILL + TOOL (pair)
- **Sources:** Code Forge logo research (983a94e7 — Brand DNA brief + 12-test battery), RICH$XPRNC8 sigil (527e8c07 — letter-reduction method), Reblend logo (2a82689c — code-built SVG variant rounds), LA logo merch (7580cc0c — rejection data point).
- **What:** Three methods, one discipline. (a) Brand-matched: audit the product UI first, extract palette/type/material as closed tokens, write a 1-page Brand DNA brief, generate concepts from product-specific ideas only, run every mark through a 12-test pass/fail battery (actual 16/32/48px renders, solid-black silhouette, grayscale, invert, circle/squircle crop, pasted into a real product screenshot, competitor wall, letterform audit, grid audit), iterate one variable at a time. (b) Sigil/glyph: reduce a name (vowels + repeats removed → R C H X P N), merge letters plus key symbols ($, 8) into ONE glyph with a documented mapping, deliver a variant set (black-on-cream, gold-on-black, transparent). (c) Code-built rounds: hand-written SVG geometry, 3 genuinely different concepts per round, no image generation for marks, user picks/rejects, rebuild from code. Anti-slop rules: brief-first gate, banned nouns copied verbatim, never ship generated lettering, human vector redraw on grid. On rejection: stop guessing, ask direction via options widget, rebuild to his pick.
- **Inputs:** brand/product + constraints. **Outputs:** Brand DNA brief, logo/glyph variants, test-battery results.
- **Reusability:** MEDIUM-HIGH — logo work recurs per new project/brand.

### S22. Role prompt engineering (12-section master pack + 8,000-char discipline) — SKILL
- **Sources:** AI Role Engineer (f4854c69 — GUIFX role v1.0→v3.1, 7,846 chars verified), Three.js environmental systems (c0765ec4), white-tailed deer sim (e364b6a6), animal/insect sim (215a932b).
- **What:** (a) The 12-section master role pack template: identity, core objectives, systems covered, architecture rules (resource-first, authoritative state separate from render mesh), interaction/transformation rules, realism levels (visual / interactive / resource sim / physical sim — stated, never faked), engineering standards, persistence rules, validation invariants, response contract — same skeleton, domain swapped. (b) The hard-limit discipline: drafts under an 8,000-character HARD limit with pre-output length audit, mandatory EXACT character-count verification (never estimate), compress during drafting if near the limit, plain instructions only (v1/v2 rejected for redundant metadata vs actual instructions), fundamental rules as an engineer not a guide, source files attached as governing references, saved to `~/workspace/role-engineering/`.
- **Inputs:** role purpose + domain knowledge + constraints. **Outputs:** role instructions file, verified under limit.
- **Reusability:** MEDIUM-HIGH — the Role Engineer thread exists to do this repeatedly for every Forge role; two full packs already in use as thread constitutions.

### S23. Species dossier → simulation build pipeline — SKILL
- **Sources:** Three.js animal and insect simulation (215a932b).
- **What:** Turn a real species into a buildable sim entity: deep research per species (or a user-supplied research report) → fixed-template dossier (form/3D spec, phenology, habitat rules, life cycle, food web, manipulation responses, simulation parameter table) → gap audit ("what's missing to recreate this animal?") → gap register sorted into already-filled / derivable (labelled *derived*, never dressed as measured) / needs research / unknowable (blanks left blank) → targeted research rounds folded back into the dossier → pilot build in a standalone sandbox on the dossier's numbers → numeric + screenshot verification. Conflicts kept as conflicts; assumptions labelled; literature gaps never invented (e.g. hide thickness left blank).
- **Inputs:** species name + research reports / user files. **Outputs:** dossier page, parameter table, gap register, pilot sim file, test results.
- **Reusability:** HIGH within its thread — repeated across three subjects (deer dossier with 3 research rounds, 27-species berry catalog, freshwater valley ecosystem with 14 fish profiles); also produced the 102-model complete animal list and a depth-stack wound model.

### S24. Sandbox-first sim build + headless verification harness — SKILL + TOOL (pair)
- **Sources:** Three.js environmental systems (c0765ec4 — dirt engine v1–v8), white-tailed deer sim (e364b6a6), animal/insect sim (215a932b — leg ground-penetration fix), Remaster Q (42200820 — Puppeteer playtests).
- **What:** Build a simulation as a standalone sandbox test file first (game file untouched), core simulation kept separate from rendering so parts can be lifted in later; verify with a screenshot rig that renders the actual file and eyeballs it before delivery ("no more blind builds"); test interactions the way a person aims on a phone (human-style raycast aims, not machine sweeps — a broken test once measured one stale ray 49 times); run automated suites (75/75, 82/82 incl. save/load round-trips, 300 simulated births); measure numerically instead of eyeballing (Q+: ball rest position, launch height, win detection; deer: leg ground penetration per pose — found 0.23–0.36 m underground in bedded/freeze poses). Sub-step: verified reference-image list (expand list, check every URL live, exclude dead/hotlink-blocked, note honest gaps — 12 → 58 images in the deer thread).
- **Inputs:** a sim feature + reference dossier/photos; HTML file path + scripted interactions/assertions. **Outputs:** verified standalone file + test results + screenshots + measurements.
- **Reusability:** HIGH — the harness genus was built twice independently in two threads; packaging it once serves every future HTML/Three.js build. Pairs with (does not duplicate) existing `verify_like_the_user` — that skill says *what* to verify; this is the executable code that does it.

### S25. Video watch → extract workflow/lesson → honest critique — SKILL
- **Sources:** Implement prompts in Code Forge (b026eda9 — Sumiro video → 6-step pipeline), Design Shell (d238e3ce — 4-video batch: cottage/Seedance trick, Underhollow sprite overhaul, Kimi K3.1 hype reel, fireball game-feel lesson).
- **What:** Watch the video(s) all the way through, extract the actual workflow or lesson (cross-checking the creator's thread when the video doesn't show the real prompt text), and give an honest critique: what's real vs hype (e.g. "the gorgeous footage is Seedance dreaming on top of a crude blockout — there is no cottage file"), what's usable vs what breaks the $0/hardware rules. Correct misses by pulling stills from ALL files instead of trusting captions. Optional follow-on: map the pipeline onto Forge's existing machinery (copy the pipeline, not the tools), rewrite prompts short/sectioned/fill-in-the-blanks for small local models, generalize scope when the user corrects it, then implement as a skill + module under S2.
- **Inputs:** user-supplied video(s). **Outputs:** workflow/lesson summary + critique + (optional) implementation spec/skill.
- **Reusability:** MEDIUM-HIGH — completed twice with different shapes; Joshua sends videos often.

### S26. Real-capture promo video production + sellable-ads playbook — SKILL + TOOL (pair)
- **Sources:** CODE FORGE VIDEO GENERATION (d2fbad7e).
- **What:** Produce promo videos from the REAL product only: drive the actual app in a capture rig (typing, windows opening, checkpoints creating — no still screenshots, no generated video, no fake UI), cut to the sellable-ads structure (15s: hook 0–2s with the result in frame 1, proof 2–10s with 2–3 real UI beats, trust 10–12s only if verifiable, CTA 12–15s "Free download — link in bio"), 3 hook variants before a 30s cut, sound from real licensed recordings with CC BY credit lines (never synthesized audio — rejected 3x; never his music unless he names the track for that use), loudness-normalized (LUFS), fresh filenames per cut so he never watches a cached old version, caption with his words + plain facts. Standing rules accumulated in-thread: real product only, no people/hands, no invented copy, ship volume and judge by installs not views.
- **Inputs:** the real app + a concept/hook + licensed sound. **Outputs:** video file(s) + post caption with credits.
- **Reusability:** MEDIUM-HIGH — many cuts made in one thread; the playbook transfers to every future product launch (Pixel Forge, MIMIK, etc.).

### S27. Social account setup kit (paste-ready, one platform at a time) — SKILL
- **Sources:** CODE FORGE SOCIAL MEDIA MGMT (1fd34d86).
- **What:** Verify the download link is live FIRST, then build a paste-ready kit for every platform (names, bios, first posts, pinned comments, which video files to post — the good cuts, not the rejected ones), and walk the user through ONE platform at a time with exact in-app steps. Check platform gating rules before promising anything (TikTok hides the Links field under 1,000 followers or without a Verified Business Account) and supply the workaround when gated (bio line + pinned download comment on every video).
- **Inputs:** a project with a download link + video assets. **Outputs:** setup kit doc + per-platform walkthrough.
- **Reusability:** MEDIUM — used once (Code Forge), but every new project launch will need the same kit.

### S28. Donate/support wiring (payment link → README → Linktree → in-app screen) — SKILL
- **Sources:** Add donate button with Cash App (20dcff58).
- **What:** Explain the link format (cash.app/$cashtag — Cash App has no official embeddable button), tell the user how to find their cashtag, VERIFY the live payment page shows their name + QR, then wire it into the GitHub README (badge button + Support section), Linktree (titled link), and an in-app startup welcome screen (non-blocking, close-to-run, button opens the payment page, big QR rendered by the app's own built-in QR encoder with a printed-link fallback if QR fails). Verified with targeted tests (11/11) + full suite (1713/1713) + offscreen screenshot.
- **Inputs:** a project + the user's payment handle. **Outputs:** README + Linktree + in-app donate screen, verified.
- **Reusability:** MEDIUM — reusable for every project launch; the welcome-screen pattern itself (startup screen, non-blocking, close-to-run) is reusable for other startup content too.

### S29. Hotfix zip (one-file patch of a shipped build) — SKILL
- **Sources:** Groq/Gemini (be74cb87 — CODE-FORGE-v2.5-FILTERFIX.zip); related fix-and-refresh for MIMIK v0.1.1 per MEMORY.
- **What:** Take the EXACT shipped build the user is running, change ONE file (the provider code, swapped for the filtered version), diff first to prove only that file moved, run the targeted tests on the patched tree, then email it with Sent-verification (name + size exact). Used when the user has a stale pre-fix build and the full re-ship pipeline is still gated on a slow full-suite run.
- **Inputs:** shipped build + one-file fix. **Outputs:** hotfix zip, emailed + verified.
- **Reusability:** LOW-MEDIUM — used once in-thread; a recurring need whenever a stale build is in his hands.

### S30. Brand scrub + rename-with-migration — SKILL + TOOL (pair)
- **Sources:** CODE FORGE DEV (94792a18) + CODE FORGE GITHUB (7d1ee11c) — no-brands scrub (235 substitutions, 28 files, whole-tree grep catch of a missed file, battery re-run); Goldfish→GoFish rename (351 substitutions, 14 files, migrations so user state carries over — plan key, toggle key, known_skills).
- **What:** Remove/replace a name across a whole tree (docs + code + docstrings + module/skill names) via grep-driven substitution, catch stragglers with a case-insensitive whole-tree grep, add state migrations so existing user data (plans, toggles, skill on/off) survives the rename, and re-run the battery to prove nothing broke.
- **Inputs:** old name, new name (or removal), tree. **Outputs:** scrubbed/renamed tree + migration + battery receipt.
- **Reusability:** LOW-MEDIUM — one big use; recurs whenever a rebrand or policy scrub lands.

### S31. Phone-first crash-course lesson format — SKILL
- **Sources:** Stella crash course (8fc2998a — lesson 1), STELLA Dev (2d7b2739).
- **What:** Teach one concept per lesson, grounded in his hardware and his own project (StemLab analogy), honest about what his PC can and cannot do (small models, LoRA/PEFT, CPU training of tiny models; bigger needs a free cloud GPU), step by step, no dumping the whole course at once. Short single-line commands only (he hand-types from his phone).
- **Inputs:** topic + his hardware/project context. **Outputs:** one lesson per turn.
- **Reusability:** LOW-MEDIUM — one course so far; same shape would fit CS50 study.

### S32. OpenAI-compatible provider wiring (Forge) — SKILL
- **Sources:** Free AI trials (3720590d — EXAONE); MEMORY (Gemini Decisions lane, same shape).
- **What:** Add a new cloud provider to Forge: verify base URL + exact model ID from the vendor's own docs first, wire the client on the existing provider pattern, add the Providers-tab block (enable checkbox, vaulted key field), verify with fake transports, note "no live call made yet" honestly.
- **Inputs:** provider name + vendor docs. **Outputs:** provider wired in an isolated copy, verified, held for merge.
- **Reusability:** MEDIUM — used for EXAONE + Decisions; recurs each time a new provider is approved (7 models on the allowlist now).

### S33. Living-document build with multi-pass audits — SKILL
- **Sources:** Winterize a sealed room in Meridian (e4953ec7 — 34 sections, 481 lines; 43 gap findings; 7 research tracks integrated).
- **What:** Build one master document as the single source of truth, updated in place (never re-written in chat); fold user ground-truth corrections into the right sections instead of pasting them verbatim; then run three distinct audits — a consistency audit (contradictions across sections), a gap audit (missing content), and a "live the guide" scenario-simulation audit (arrival day, a January week, a nor'easter, hour by hour, tracing every procedure for gear it silently assumes).
- **Inputs:** user's dictated facts/corrections + research tracks. **Outputs:** one numbered-section master document + audit findings folded back in.
- **Reusability:** MEDIUM — used heavily in one thread; pattern generalises to any long-lived guide/manual. The multi-pass audit trio is the new part (the constraint-checking overlaps existing `check_constraints_before_acting`).

### S34. Covert questionnaire → character profile — SKILL
- **Sources:** Arlo character questionnaire (369cab4f — 45 questions, closed 2026-11-06), Muse tips (2648fd53).
- **What:** Build a character/persona profile through a long covert questionnaire: one question at a time, labelled `q. N-`, questions COVERT (steering purpose not obvious), scenario-based with "pinned down" constraints that close loopholes (when the user finds a loophole, the question is re-asked with it closed); passes allowed ("I don't want to answer that" → logged as pass, no reason needed); every answer logged to a profile file as it comes; no decoding shown as you go; no batches of finished options; at the end, build the character from the whole pattern at once (profile doc + visual build + activation with a preview→confirm→activate→revert-on-rejection loop). Rules file: `~/workspace/goals/arlo-character-profile/files/QUESTIONNAIRE.md`.
- **Inputs:** subject + question territory. **Outputs:** questionnaire log, profile doc, visual build, activated avatar/outfit.
- **Reusability:** MEDIUM-HIGH — used once end-to-end, but the method is generic: any persona, character, brand voice, or user profile.

### S35. UI direction-finding via mockup rounds — SKILL
- **Sources:** Pixar inspired Code Forge UI (3b29448b — locked: Future 3 Dark Glass Minimal, no ring gauges).
- **What:** Find a UI direction by rounds of generated mockups instead of guessing once: generate 4 directions in a named aesthetic → take one-line verdicts ("colors stay, game goes", "too generic, like a PowerPoint slide") → re-dose a single variable across a range (pixel amount, lightest→heaviest, A–D) → mix directions at explicit ratios (bench-dominant / glass-dominant / max-workspace) → lock the winner as a standing reference with scope rules attached (reference to upgrade what exists, not a layout to copy over it; nothing existing replaced) → hand spec-writing to the dev thread only, never run a second spec in parallel (avoids drift). Iteration rule throughout: fix the one named thing, don't redo everything.
- **Inputs:** product + aesthetic prompt. **Outputs:** mockup rounds, locked direction spec, standing reference.
- **Reusability:** MEDIUM — one thread end-to-end; the one-variable iteration rule also appears in S21's logo workflow.

### S36. Research → rebuild-better single-file game clone — SKILL
- **Sources:** Remaster Q in HTML (42200820 — Q+ at `~/workspace/q-plus/Q-PLUS.html`, 15 missions + sandbox + IQ TEST).
- **What:** Research an existing game (core loop, level structure, flaws from reviews — Q's were luck-based physics, frustrating controls, an ad after every level) → build an improved single-file offline HTML version (physics engine embedded, no CDN, no ads) with named improvements over the original (undo + tap-to-erase, pin tool, materials, hold-to-win meter, ghost preview, ink stars, hints, slow-mo, saved progress, sandbox) → verify by actually playing it headlessly at phone size → cut levels that fail playtesting twice and replace them → v2 rebuild driven by the user's real-phone verdict (all-buttons-visible at 360×800, rules book, IQ measurement with graded stages + strengths graph, stats + downloadable report).
- **Inputs:** original game name. **Outputs:** single-file HTML game, research summary, verification notes.
- **Reusability:** MEDIUM — used once, but the research→clone→playtest→iterate shape is directly reusable for any "make me a better version of X" game request.

### S37. Play-based game design study (itinerary sheet) — SKILL
- **Sources:** Study Miniplay game design reference (96341033 — 32 categories / 310 games).
- **What:** Build a reusable game-design reference library by actually playing games: compile a queue (top 10 most-played per category from the portal's own category pages, ads excluded, honest gaps where a top 10 can't be verified) → one game at a time, actually played in the browser → Step 0: read the game's own How to Play menu first (objective, controls, what you can do) → fill a fixed itinerary sheet (entry & menus, character design, pixel art/graphics, animation, gameplay, camera, specs box, hub-vs-game-inside-it distinction) → file per-game notes → report PARTIAL / walled / not-played honestly (login gates, 1 FPS, listing-name mismatches such as RIVALS→Veck.io, UNO→4 Colors). The sheet itself was iteratively refined in batches from holes early games exposed.
- **Inputs:** portal URL + category list. **Outputs:** ranked game queue file, per-game filled itinerary sheets, reference doc.
- **Reusability:** MEDIUM — **caveat: execution failed in-thread** — the browser player kept failing to play properly (not focusing the game, tapping where a hold was needed), Joshua said "Just stop dude" and the study was stopped 2026-11-08. The sheet + protocol are the salvageable reusable parts, not the play-execution.

### S38. Pace-adaptive study itinerary — SKILL
- **Sources:** STUDY DASHBOARD DEV (dc0566e7 — CS50 11-course journey), Universal Study Portal (4955a021 — reuses the same pace engine concept).
- **What:** Build a schedule from a seed pace, then measure real pace from logged completions (2+ units) and recalculate all projected dates from the real pace; weekly check-ins feed the math; seed-vs-live dates shown side by side.
- **Inputs:** course list + seed pace. **Outputs:** itinerary with dates that move as pace is measured.
- **Reusability:** MEDIUM — one thread + the portal concept; generalizes to any multi-course plan.

### S39. Sprite-sheet prompt pack (character lock + full action map) — SKILL
- **Sources:** Free AI trials (3720590d — Titan-13-style robot; also 10 Civitai/fal.ai prompts built around his actual projects).
- **What:** Build a reusable prompt pack for consistent game art: one character-lock block (design details fixed) pasted before every prompt + one prompt per action/pose, same lock + same model + same seed = same character across every sheet; master one-shot prompt flagged hit-or-miss, per-action strips the reliable route.
- **Inputs:** character description + action list. **Outputs:** copy-paste prompt blocks.
- **Reusability:** MEDIUM — used once; sprite/game-asset work recurs (Pixel Forge, Yahtzee, Meridian Origins).

### S40. Token burn-rate baseline + scheduled recheck — SKILL + TOOL (pair)
- **Sources:** How long 1 billion tokens last (fea170f0 — Oct 31 baseline → Nov 3 recheck: ~13.1M/day → ~77 days).
- **What:** Record a usage baseline (subscription status + locally logged token totals), schedule a one-time recheck days later, then compute tokens/day since baseline, per-day breakdown, and remaining-pool lifetime at the measured pace — with the caveat that the pool may still be untouched if the weekly limit hasn't been exhausted.
- **Inputs:** baseline snapshot + recheck date. **Outputs:** burn rate (tokens/day) + pool-lifetime estimate.
- **Reusability:** MEDIUM — used once; repeatable for any metered resource. Note: the system `subscription-status` skill already covers the status check itself; the baseline→recheck→rate workflow is the new part.

### S41. Song key/BPM lookup + mashup compatibility — SKILL (+ TOOL if a data source is scriptable)
- **Sources:** Key and bpm for songs (0b4e32ae — Tomorrow / Alive / Plush).
- **What:** Look up key + BPM for a list of songs, then work out mashup compatibility: which songs share a key family (relative major/minor), a BPM anchor with minimal stretches, and the semitone shift needed to bring an outlier into key (or flag it as its own section/key change). Example: 146 BPM anchor, Plush +4 semitones to B minor.
- **Inputs:** song list (title + artist). **Outputs:** key/BPM table + compatibility verdict + shift math.
- **Reusability:** MEDIUM — used once, but music work recurs (Stella/StemLab threads, his mashup interest).

### S42. Live local stock verification (verified vs lead) — SKILL
- **Sources:** Find Rug Doctor antifoam in Lewes (e83c3975 — two live verifications, 3:20 PM and 6:50 PM Nov 8).
- **What:** Find a product for same-day pickup without sending the user on a wasted trip: set the exact pickup store on each retailer's site, check the product page (not just search results — search said "Pickup Today" while the product page said "Pickup Tomorrow"), report **verified** items (price, stock count, aisle/bay, pickup window, check time) separately from **phone leads** (unverified, "don't go on my word"), re-verify later the same day because stock changes, and broaden by chemical equivalence when the brand fails (Rug Doctor Anti-Foam → any silicone-based defoamer). Born from a real failure: unverified store suggestions sent Joshua to four stores that had nothing.
- **Inputs:** product + town/area + store list. **Outputs:** verified pickup options + phone leads, each labelled, with prices/aisles/times.
- **Reusability:** MEDIUM — single thread, but the pattern fits any local "find it tonight" request. Overlap: system skill `live_page_checks` covers one-time checks; the multi-store pickup-tonight protocol + labelling is the additional part.

### S43. Authority incident-report drafting — SKILL
- **Sources:** Report caregiver neglect in Delaware (8b121215).
- **What:** Turn a user's account of neglect/abuse into formal reports for authorities: collect facts with explicit `[NEED]` blanks that are never guessed; draft separate reports per agency (police / APS / DFS-CPS) from one fact base; separate **fact** from **belief** in the wording; build a timeline from the user's screenshots/messages; anonymize on request and verify the name appears nowhere; keep a private incident record separate from filed reports and produce a SEND version with the private record stripped; research the actual statutes before advising (Delaware recording law, APS confidentiality 31 Del. C. § 3912); evidence-preservation guidance (unedited original, two backups outside the house, context note with timestamps); route to the right intake (APS phone, DFS line, Medicaid fraud unit, free legal aid CLASI).
- **Inputs:** user's account + screenshots + agency targets. **Outputs:** per-agency report drafts, SEND version, private record, call scripts, intake contacts.
- **Reusability:** MEDIUM — single thread, sensitive/personal subject; keep the skill generic (report-drafting), not tied to this case. The drafting pattern (never-guess blanks, fact/belief separation, anonymization check, send-vs-private versions) is reusable for any formal report, complaint, or statement.

### S44. Photo-guided vehicle electrical diagnosis — SKILL
- **Sources:** Fix 2004 Chevy Astro headlights (f0b35e4c — fixed the van via fuse #15 TBC).
- **What:** Diagnose a vehicle electrical fault from user photos of fuse boxes: read the fuse map off the photo, name components by photo landmarks ("big orange 40A LIGHTING, top row far left"), run ordered elimination tests (fuses → relay swap → switch), use split-branch symptom questions (tail lights? high-beam flash? DRL?) to narrow to one part, and record the actual fix for next time.
- **Inputs:** vehicle year/make/model + symptom + fuse-box photos. **Outputs:** step-by-step test sequence + identified failed part.
- **Reusability:** MEDIUM — used once, fully successful. Generalises to any vehicle electrical / appliance troubleshooting with photos.

### S45. Idea → newspaper comic strip — SKILL
- **Sources:** Create newspaper comic from ideas (426af22b).
- **What:** Turn any idea/concept into a classic 3–4 panel newspaper comic (setup, visual gag, punchline). Hard rules learned in-thread: the user's words are notes to draw FROM, never text to put in the art (no labels/speech in the drawing); when asked for a new image, generate from scratch, don't edit the old one; abstract concepts (glass house, stones, DARVO, discard) must be portrayed visually, not labelled.
- **Inputs:** an idea/feeling/headline + corrections. **Outputs:** comic script + drawn strip.
- **Reusability:** MEDIUM — used once (one strip, several revision rounds). Repeatable for any idea-to-comic request.

### S46. Verified reference-image list (live URL check) — SKILL (small)
- **Sources:** White-tailed deer simulation (e364b6a6 — 12 → 58 images).
- **What:** Expand a reference-image list for a build, check every URL live, exclude dead/hotlink-blocked candidates (7 excluded), and record honest gaps where no usable photo exists (e.g. the exact moment an antler casts). Could fold into S24 or S23 as a step; listed separately because the live-check + gap-noting discipline is its own reusable step.
- **Inputs:** a topic + needed coverage areas. **Outputs:** REFERENCE_IMAGES.md with verified-live URLs + noted gaps.
- **Reusability:** LOW-MEDIUM — used once; small.

## Tier 3 — niche / weak / single-use (include for completeness; build last)

### S47. Live symptom triage with timed vitals recheck + escalation thresholds — SKILL (safety-sensitive)
- **Sources:** Seek medical help now (0f35b782 — live yohimbe reaction).
- **What:** Real-time triage for a suspected supplement/drug reaction: identify the substance from a label photo, check interactions (coffee + dabs + empty stomach), teach a 30-second pulse count, set a timed recheck cadence (~15 min), state hard escalation lines up front (HR >120 sitting, sharp pain, vomiting blood → 911 / Poison Control 1-800-222-1222), offer a private text route (webPOISONCONTROL) when the user can't call, accept one-word answers, and write a one-paragraph summary the user can show a third party.
- **Inputs:** symptoms + substance label photo + timing. **Outputs:** monitoring plan, escalation lines, ready-to-show summary.
- **Reusability:** LOW — used once (a live crisis). Repeatable as a playbook only — must stay a SKILL with explicit "escalate, don't diagnose" guardrails, never a diagnostic tool.

### S48. VLC / IPTV setup from a streaming site — SKILL
- **Sources:** Android VLC and Termux help (7d85fa44).
- **What:** Given a TV-streaming site that won't play in the browser, find the real links (full playlist, guide, direct per-channel stream), then give copy-paste VLC Android steps (More → New stream), starting with the single-channel link as the fast test and warning the full playlist is heavy; note VLC's guide limitation and the alternatives (TiviMate/Kodi/Jellyfin).
- **Inputs:** a streaming-site URL. **Outputs:** exact links + setup steps.
- **Reusability:** LOW-MEDIUM — used once; repeatable whenever he finds another such site, but narrow.

### S49. Free-track enrollment via browser (guardrailed) — SKILL
- **Sources:** STUDY DASHBOARD DEV (dc0566e7 — edX CS50x enrollment as SpaceWok).
- **What:** Enroll him in a free course via a browser task with hard guardrails: free/audit track only, never choose a paid option, never enter payment info; credentials via Secure Vault only; handle rejection (bad password / compromised password) by asking him for a fresh one on a secure card.
- **Inputs:** course URL + account email. **Outputs:** enrollment confirmation on the free track.
- **Reusability:** LOW-MEDIUM — used once (CS50x); recurs for each new course enrollment (Saylor, Helsinki, OpenLearn queued).

### S50. Email-a-zip code intake + dead-button diagnosis — SKILL (weak, unexecuted)
- **Sources:** Fix System Forge Care code (51ec77e5).
- **What:** Intake for fixing a user's codebase: user emails a source zip to the connected Gmail (zip hygiene: exclude `.venv`/`__pycache__`), agent pulls the attachment, unpacks, runs a file check so the user can see the whole thing arrived, diagnoses before changing anything, one fix at a time. For a dead UI button: find where the button is created → check what its click is supposed to call (missing/misnamed/wrong target) → trace that function through the steps to the break point; triage by symptom (nothing at all / starts then stops / error popup).
- **Inputs:** emailed source zip + symptom description. **Outputs:** file check, diagnosis, fix.
- **Reusability:** LOW — **caveat: stated but never executed in-thread** (the zip never arrived; no fix was done). The thread cites the Code Forge zip intake as precedent, so the intake pattern is claimed repeated but unverified from these threads.

### S51. PC spec review → bottleneck + compatible upgrade shortlist — SKILL (weak)
- **Sources:** Linux Mint PC specifications (d81cbb00 — HP All-in-One 22-df0xxx, Ryzen 3 3250U, 8 GB single-stick, 1 TB HDD).
- **What:** Read a PC spec file, record the machine, name the real bottlenecks (HDD, single-channel RAM), check the exact model's upgrade path (empty M.2 2280 socket, Gen4 drives run at Gen3 speed), then find the cheapest compatible parts across stores with a compatibility verdict per item.
- **Inputs:** spec file + upgrade question. **Outputs:** bottleneck analysis + priced shortlist.
- **Reusability:** LOW — used once. Partially covered by the existing system `shopping` skill; the spec-to-bottleneck analysis is the only new bit. Lowest priority.

### S52. Pantry-constrained recipe adaptation + target-app formatting — SKILL (weak)
- **Sources:** Old El Paso taco seasoning (b98324c9) + Adjust chili recipe (0bfee90a — Chili Mac).
- **What:** Adapt a recipe to what the user actually has: scale to the real quantity (and correct it when the user corrects the quantity — 2 lb → 3 lb), substitute missing ingredients with on-hand equivalents and explain the method change each substitution needs (ground beef fattier than sirloin → drain; mushrooms dump water → brown first; no red wine → broth + vinegar), consolidate stacked corrections into one final clean copy, and format it to match the target app by reading the app's existing content first (checked his Recipe Bro recipes to match title/servings/ingredients/instructions layout).
- **Inputs:** original recipe + on-hand/missing ingredients + target app. **Outputs:** adapted recipe in target-app format.
- **Reusability:** LOW — repeated across 2 threads, but generic cooking help with no distinctive machinery beyond "format to the target app by reading it". Lowest priority; included for completeness, not recommended as a build.

---

# PART 2 — BNB TOOLS (master list, priority order)

14 of the 17 tools are the executable half of a skill in Part 1; 3 are standalone. "Existing fragment" notes where a script already exists in the workspace that the tool would generalize — verified by directory listing on 2026-11-12 (not by reading the scripts in full).

| # | Tool | Pairs with | What it does | Existing fragment |
|---|---|---|---|---|
| T1 | Ship pipeline scripts | S1 | Zip builder with correct stored modes (0o100755 scripts / 0o100644 files, file-type bits included — GUI extractors drop the bit otherwise), SHA-256 of local zip vs downloaded Release asset, read-back checks of pushed files. | `~/workspace/build_release_zip.py`, `~/workspace/build_graphqueue_zip.py` (per-build packers, not yet one reusable tool) |
| T2 | Delta-port / diff-verify script | S2 | Ports only the marked delta from an isolated copy into the live tree; verifies the merged tree against the source copy (diff must equal exactly the intended changes; marker counts, byte-identical files). | `~/workspace/forge-queue-verify/port_queue.py`, `probe_queue.py`, `port-spec.md` |
| T3 | Post-merge battery runner | S8 | Waits for a stable window (no tree changes mid-merge), runs targeted classes + full suite, diffs the failure list against the baseline, reports only the delta. Must live in a script file — a bash -c watchdog pgreps itself forever (AGENTS.md lesson). | `~/workspace/forge-queue-verify/wait_and_fullsuite.sh`, `run_battery.sh`, `run_fullsuite_chunked.py` |
| T4 | Name-check script | S7 | Batch GitHub exact-name search + web check per candidate name; outputs clean/dead with evidence. | None — done by hand each time |
| T5 | Model sweep harness | S13 | Scripted benchmark/compat table builder (size, quant, licence, runtime compat, vendor-benchmark flags) feeding the sweep report. | None — tables built by hand |
| T6 | Linux release packager | S6 | From a tree + icon SVG: render PNGs, generate GUI installer + `.desktop` (GLib-safe Exec quoting), uninstaller, installer self-verification step. | Per-project installers exist (Forge, MIMIK, Pixel Forge, WinLinx, Forge Browser) — converge into one template |
| T7 | Overlay-match script | S18 | Lays a render over a reference sheet at the same scale, measures silhouette/dimension deltas, reports residual offsets. | None |
| T8 | Logo test battery | S21 | Renders a mark at 16/32/48px, silhouette, grayscale, invert, circle/squircle crop, pasted into a real product screenshot; pass/fail per test. | None |
| T9 | Brand scrub / rename script | S30 | Grep-driven whole-tree substitution with straggler catch (case-insensitive whole-tree grep), migration scaffolding for user state keys. | None — done by hand (235 + 351 substitutions) |
| T10 | Repo-identity check script | S20 | GitHub existence/empty/description check for a repo name; handles the get_file_contents ok:true + isError:true trap. | None |
| T11 | Fresh-unzip verification harness | — (standalone; discipline is existing skill `verify_like_the_user`) | Unzip the shipped zip into a clean directory, run the full suite there, run smoke checks, screenshot GUI tabs, report. | None — done by hand every time |
| T12 | Qt offscreen/Xvfb verification harness | — (standalone) | One command that sets the known-good Qt test env (LD_LIBRARY_PATH to ~/workspace/qt-libs/root, __EGL_VENDOR_LIBRARY_DIRS, test venv python, HOME, TMPDIR=/tmp, QT_QPA_PLATFORM=offscreen or xvfb-run for OpenGL) and runs a launch/screenshot/render-grab check. Env recipe is in AGENTS.md; the reusable part is turning it into one command. | None — incantation re-derived each time |
| T13 | Headless play/render verification harness | S24 | Puppeteer/screenshot harness at phone viewport (360×800 / 430×950): simulated input, live state reads, screenshots, numeric measurement (ball physics; leg ground-penetration per pose). | One-off scripts in /tmp (Q+ thread) + a screenshot harness (deer thread) — built twice independently, never packaged |
| T14 | Video capture rig + ffmpeg cut/loudness pipeline | S26 | Drive the real app and capture it; cut to the 15s structure; LUFS loudness-normalize; fresh filenames per cut. | Capture rig + ffmpeg commands exist inside the video thread's working files (not packaged) |
| T15 | Target-size video compression CLI | — (standalone) | `compress-to-size <file> <target-MB>`: bitrate math from duration + target size with safety margin (aim ~88 MB for a 100 MB cap), emits the ffmpeg command; audio-only extraction alternative. | None — math done by hand once |
| T16 | Token burn-rate tracker | S40 | Baseline snapshot → scheduled recheck → tokens/day + pool-lifetime estimate. | None |
| T17 | Song key/BPM lookup | S41 | Key/BPM data lookup + mashup-compatibility math (key families, BPM anchor, semitone shifts). Tentative — depends on a scriptable key/BPM data source. | None |

---

# PART 3 — ALREADY BUILT (do NOT re-propose)

## Custom skills on disk (verified present in `~/workspace/custom-skills/`, all 6 seen actively used in the audited threads)

| Skill | Where it was seen in use |
|---|---|
| `answer_the_question_as_asked` | Stocks thread corrections; flea-bomb thread shows the exact failure mode it guards ("You didn't answer me") |
| `check_constraints_before_acting` | Price cap, no-web-UI, $0/hardware rules checked before recommending anything; Meridian guide ground-truth facts |
| `fix_defects_in_place` | Pixel Forge v0.5/v0.6 defects, MIMIK v0.2, Forge "Fix the failures", T2-2's three fixes, deer bedded-leg fix, Q+ seesaw level cut |
| `one_item_at_a_time` | Every plan/queue thread (CR/M/T/F items, browser #1–#22, portal decisions, Miniplay "one game at a time", deer "1 thing at a time") |
| `verify_attachment_before_claiming_sent` | Email zips Sent-verified byte-exact (Design Shell v0.2/v0.3/v0.6/v0.9, Forge Browser v0.2/v0.4/v0.6, Study Shell v1/v1.2, FILTERFIX 986,605 bytes) |
| `verify_like_the_user` | "His real-PC verdict closes it" everywhere; fresh-unzip verifications; screenshot eyeballing; phone-size playtests |

## System skills that already cover part of a candidate (noted in the entries above)

- `live_page_checks` — one-time price/stock page checks (overlaps S42's single-check part; S42's multi-store pickup-tonight protocol is the new part).
- `email_management` — draft-reply-for-approval pattern (covers the Tavus thread's only pattern).
- `shopping` — product search/comparison (covers most of S51; only the spec-to-bottleneck analysis is new).
- `subscription-status` — usage/status check (covers the status half of S40; the baseline→recheck→rate workflow is new).

## Existing code in repos / workspace (starting points, not finished tools)

- **CODE-FORGE tree** (`~/workspace/code-forge-*/Linux Forge Agent/skills/`) — Forge's own in-product skills (provider patterns, C6/C7/C10 skills, reference-driven-build module). These are product features, not the agent-side playbooks proposed here; S32 (provider wiring) and S2 build on them.
- **Forge queue-verify scripts** (`~/workspace/forge-queue-verify/`) — `port_queue.py`, `wait_and_fullsuite.sh`, `run_battery.sh`, `run_fullsuite_chunked.py` — working fragments of T2/T3, built for one queue; generalizing them is the T2/T3 build.
- **Per-build zip packers** — `~/workspace/build_release_zip.py`, `build_graphqueue_zip.py` — fragments of T1.
- **Role-engineering sources** (`~/workspace/role-engineering/`) — governing references for S22.
- **Questionnaire rules** (`~/workspace/goals/arlo-character-profile/files/QUESTIONNAIRE.md`) — source material for S34.
- **Research dossiers** (`~/workspace/research_notes/`) — source reports behind S11/S12 (CodeRabbit, Manus, sellable ads, logo research, etc.).
- **aura-skills:** no `aura-skills` directory or repo was found in the workspace during this audit (searched 2026-11-12) — if it exists elsewhere (e.g. a GitHub repo not cloned here), its contents were NOT checked against this list. Flag for the parent: check it before building, to avoid duplicates.

---

# PART 4 — PER-THREAD NOTES (all 67 threads)

Short IDs are the first 8 hex chars of the full chat ID. "→" lists the master-list entries the thread grounds. Threads are grouped by audit worker batch.

## Batch A (main chat + flagship dev threads)

| Thread | Notes | → |
|---|---|---|
| c6ee49a6 — Main chat (Meridian Origins + general) | Hub thread: receives completion reports, dispatches work out (Blender MCP → DEV, Raon trial → HF thread, MIMIK+Reblend bridge → MIMIK). Standing rules set here and propagated: GitHub push ⇒ also a Release; Release zip must carry icon + double-click installer; no third-party brand names in docs; "push everything to GitHub". Name checks (portal: 24 candidates), inbox-triage cron (pass-only), security-alert triage, Raon-1 Nano research + trial dispatch, Adobe/Blender MCP research, scheduled reminders. 2 pages / 40 turns read; deep history (e.g. Meridian Origins patch flow) not read — see caveats. | S1, S3, S6, S7, S10, S13 |
| 662fb3aa — OLLAMA SYSTEM TEST | HF 2B sweep (~40 models, hardware-graded, pull list emailed), Bonsai-2 runner, OLLAMA SYSTEM TEST v1→v5 (GUI benchmark tool, JSON test templates, deterministic scoring, provider support, multimedia templates + capability screening). Full review ordered verbatim. Ship pattern every version: build → verify vs fake Ollama → email zip → push → Release → SHA-256 match. 2 pages / 40 turns. | S1, S5, S13 |
| d22a66c0 — MIMIK Dev | Linux port of littledivy/mimic: traffic capture → deterministic $0 Python client gen. v0.1 → v0.1.1 (Qt `&` mnemonic bug) → v0.2 (Reblend bridge; pattern presets via traffic fingerprinting, 15 fingerprints, ≥2-signal matching). Launch defect on real PC (PySide6 in optional extras → silent menu-icon death) → root-caused in clean venv, fixed (core deps + installer self-verification) + same-family fixes (mitmweb venv discovery, PYTHONUNBUFFERED). Full review ordered. Ship: push + Release only ("stop sending me zips"). | S1, S5, S6 |
| b345e8db — Build multiplayer Yahtzee web app | Three.js Yahtzee (static artifact): full rules, bots, pass-and-play; Reblend die (.glb, 3,846 tris, pip counts verified, opposite faces sum to 7); lighting fix (grey dice = RoomEnvironment + ACES, not the model); drag-reorder of held dice; "Debug it" → bot soft-lock + 4 faults fixed; full review → P0–P4 plan + 25-item task list; cup bug from user screenshot (backface culling) → rebuilt as a real cup. Photos rule: reference photos must not appear in the game. | S5, S9, S15 |
| b2e2291b — PIXEL FORGE DEVELOPMENT | Standalone Linux sprite engine, items 1–6 built and verified in one day (image→pixel core, video→frames, prompt→sprite via pinned LCM model, spritesheets+animation, library+presets, code+game-asset input incl. Minecraft skins). Every item: isolated copy → independent fresh-unzip verification → defects fixed in place + regression tests + CHANGELOG → zip with SHA-256 → (from v0.5) GitHub push + Release only. Live proof: real sd.cpp built from source + real generation run. Competitive research → 24 ranked improvements in 3 tiers + avoid list + pricing, as a comparison page. | S1, S2, S6, S11 |
| 94792a18 — CODE FORGE DEV | Core Forge development. Isolated copy → lead battery → delta-port merge → merged-tree battery (queue 321/321, Decisions lane 83/83→84/84, T2-3 111+19); backup before merge; diff checked ("diff is exactly the four fixes"); failure-set comparison vs baseline; solo-suite rule (wait-for-window watchdog in a script file); no-brands scrub (235 substitutions, 28 files); Goldfish→GoFish rename (351 substitutions, 14 files, migrations so user state carries over); test-order flakiness diagnosed. Ship: zip → email → push (8 paths read-back) → notify releases thread. 2 pages / 40 turns. | S1, S2, S8, S30 |
| 7d1ee11c — CODE FORGE GITHUB | Releases + repo management only. Staging rsync (excludes install.sh/README/CHANGELOG — staging owns install.sh), zip-vs-previous-zip audit, installer retrofit convergence (two installers compared, fuller one picked), browser-based Release creation (saved login, password-reject recovery via Secure Vault card), release-notes scrub + live-page verification, CHANGELOG scrub + push, read-back verification. Standing rule origin: no third-party brand names in docs. Read to completion. | S1, S6 |
| d0d4144c — Stocks and Crypto Sweep | Daily 17:20 cron sweep. Per pick: price + as-of time + source, consensus target + upside %, analyst split, why (earnings beat / revenue growth / guidance raised), risk, next step; "most-likely-profitable check" (3 criteria). Hard constraints from corrections: $100 max per share/coin, focus $20–$100; report ONLY passing picks — if none pass, one short line, no rejects list, no watchlist. Cron instructions updated in place when a rule changes. | S10 |
| 5bb9ed96 — EVERY MOUSE — Victor | Desktop-pet coordination. Victor v1 (23 parts, 4,420 tris, .glb + walk-cycle proof) → rejected ("looks absolutely terrible") → direction asked before rework → character reference sheet (6 views) + rule: everything made separately and pieced together properly. Sheets per piece (hoodie 7 views, shorts 8 views, belt 7 views + belt-only rule) → forwarded to REBLEND DEV per sheet. Preset direction: Victor as reusable character preset — BOTH GitHub + built into Reblend. Name check: EveryMouse verified clear. Plan: 6 items, Item 2 on hold until v2 lands. | S7, S17, S18 |
| 2a82689c — REBLEND DEV | 3D engine development (T7–T11 mesh block: .obj/.glb import+export shipped, each emailed + Sent-verified). Victor v2 + belt trace rework: rebuild by TRACING the reference sheet (dimensions measured off the image, overlays matched — not eyeballed); 3/4-view backdrop support. Blender gap research: 163 capabilities, 41 must / 71 should / 47 later, 5 "needs inventing" (never "impossible" — "there is always a way"). Character pipeline design: upload sheet → itemize → build each piece with 3 approval gates → assemble → save as preset. Logo variants hand-built in code (SVG geometry), rounds of 3. Chatbot-shell design (T43–T50, designed not built). 2 pages / 40 turns. | S11, S17, S18, S21 |
| 2d7b2739 — STELLA ✨ Development | Stella = standalone Linux fine-tuning program (profiles → projects → export). Item 1: Forge roster audit — per model: seat, strengths, weaknesses, wasted performance, tune-up candidate vs dead weight; grounded in sweep evidence + Forge tree + fresh `ollama list` screenshot (stale-list mistake caught: vision seat was filled, not empty). Verdicts: driver holds but Q8_0→Q4_K_M is the biggest free win; reviewer contested (A/B trial before training); phi4-mini cut; first fine-tune LFM3 1.7B. Repo BROKE-N-BORED/STELLA verified exists + empty before any push. Read to completion. | S13, S20 |
| 8fc2998a — Stella — fine-tuning crash course | Two jobs: (1) GitHub check for Stella — no repo named Stella/Stellar, no "stella" in code; private StemLab matches the description almost exactly → put to him as a question, not assumed. (2) Crash course: one concept per lesson, grounded in his hardware, honest about CPU limits. Standing rule set here: push everything (standalone or combined tools/skills/projects/programs) to GitHub so there's always a repo to pull from. Read to completion. | S20, S31 |
| dfc78d3f — CODE FORGE GUIFX | GUI effects, one task at a time (T3–T8 + fixes). Every task ends with a RECEIPT: files changed (+/- lines), tests (own re-run + full suite with failure set byte-identical to baseline), verified-how (diff read, greps, render eyeballed, geometry checks at 5 widths). Screenshot-driven fixes: header letters clipping (true min width 1094 vs reported 982 — verified at 1024/1280/1366/1500/1600), subtitle cut off. Token discipline: drifted hardcoded colors swept onto state tokens + guard against literals creeping back. Merge notes to DEV with held build paths. | S4, S8, S9 |

## Batch B (Forge-dev + services threads)

| Thread | Notes | → |
|---|---|---|
| b074e650 — Audit GitHub repo for Broke-N-Bored | Joshua designated Arlo his GitHub repo audit + update manager for BROKE-N-BORED (17 live repos, 14 public + 3 private). He corrected Arlo for auditing a repo from conversation history that doesn't exist live (WinTux) — durable rule: audit ONLY repos that exist live on GitHub. Format agreed: one repo at a time in a queue file, each report covering features/functions, strengths, weaknesses, gaps, UI flaws, innovation + design suggestions, updates/upgrades; stop after each for his go-ahead. No audit report delivered yet in the turns read. Read fully (6 turns). | S5 |
| febd57ac — Research CodeRabbit for Code Forge | Deep research on CodeRabbit (report at ~/workspace/research_notes/…) → tiered Forge plan (Tier 1: CR1–CR10 build-now; Tier 2: 6 adapt items; skip list). Built one at a time in isolated stacked copies, verified solo (targeted tests + neighbors + diff-exact), port spec handed to DEV, held for merge order. CR1–CR10 + T2-1 (linter), T2-2 (code graph), T2-3 (finishing touches) all done this way. CR4 refused 3x by a safety check, then built directly after Joshua said "No solve the problem". T2-2's verification caught and fixed 3 real defects in place. Read fully (~60 turns). | S2, S12 |
| cdcadb23 — Flea bomb prep checklist | One-off personal/household thread: full prep checklist (gas/flame + electric/spark shutoffs, pilot lights, fridge unplug, smoke alarms), bomb-count math (cu ft → sq ft at 8 ft ceilings; Raid 5,000 vs green 2,000 cu ft cans), placement + start order, photo-guided water-heater/furnace pilot identification, air-out timing, re-light sequence, mouse-trap placement, Borax carpet powder, round-2 timing. Joshua repeatedly corrected the agent for re-serving the Raid number when he asked about the 2,000 number. **CHECKED — NOTHING REUSABLE** as a tool/skill. Micro-pattern only: "photo as before-picture for restore" (gas handles photographed before shutoff). Read fully (~60 turns). | — |
| 0b4e32ae — Key and bpm for songs | Key/BPM lookup for 3 songs → mashup compatibility (relative major/minor pair, 146 BPM anchor, Plush +4 semitones to B minor) → stem-separation software hunt (his forgotten Windows app identified as Acon Digital Remix or RipX DeepRemix; Demucs on Linux with short single-line commands) → the WinLinx project: "build my own driver" reframed as a Wine/yabridge wrapper, Windows program manager + bloatware/spyware scanner, native Qt → name clearance saga (WinTux taken; 29 unchecked names all taken; 28 coined checked, 13 clean; WinLinx picked; WinLink dead — ham radio email system + 13 repos) → v0.1 rebrand + push + Release (password rejected, re-entered, Release live, SHA-256 verified) → full code review (~3,000 lines read). Read fully (~40 turns). | S1, S5, S7, S41 |
| 611e974d — FORGE BROWSER DEV | Forge Browser standalone-first: v0.1 search+fetch skeleton (keyless chain DuckDuckGo Lite→HTML→Bing, SearXNG optional), v0.2 engine room (CDP client from scratch, vault, research, multimodal), v0.3 standalone test script, v0.4 install.sh/run.sh, v0.5 real Chromium window, v0.6 Qt window (after "it IS a browser" correction — no browser-in-browser, no web UI), AI-browser upgrade (chat dock driven by local Ollama), deep research → 22-item improvements doc → all 22 built one at a time → cap removal on "no unnecessary limitations" → Release v0.1 with icon + double-click installer. Also a full codebase analysis (E1–E4, P1, U1/U2, security) with recommended fix order, delivered as a list. Read fully (~60 turns). | S1, S2, S5, S12 |
| 3720590d — Free AI trials with no card | Deep research → ~60 passing / 22 rejected catalogue page (38 no-card services, filterable, rejected list separate; Cash App route proven dead); hard rules ($0, no card, no phone); daily-free-services-sweep cron (~10:20 AM, dedupe vs catalogue, report only new finds/changes, losses first — Mistral API free tier gone, NVIDIA NIM phone-gated, Lightning AI phone-blocked); signup tracker; single-service $0 checks (K-EXAONE verified from LG's own announcement, then integrated into Forge as a provider on the Groq pattern); Gemini Decisions API find → SKRIBE lane; fal.ai full-chain check; Replicas $100 credit + bring-your-own Groq brain; sprite-sheet prompt pack (Titan-13 robot character lock + full action map); 10 Civitai/fal.ai prompts. Read fully (~60 turns). | S10, S32, S39 |
| 4955a021 — Universal Study Portal | Study Shell for everybody — download or website, account/login, pick free classes from the verified catalog, build schedule, same dashboard/pace engine/notebook/tracking. Open question put to him first (downloadable vs hosted vs both) — still unanswered. Name check: 24 candidates checked on GitHub + web, 7 clean (ScholarQuay, CampusQuay, LearnQuay, ClassQuay, CourseQuay, Syllaport, ScholarHarbor); StudyQuay dead (live agency). Windows + Linux builds required, each a GitHub Release with icon + double-click installer. No build started yet. Read fully (6 turns). | S7 |
| dc0566e7 — STUDY DASHBOARD DEV | Free-college research (24 universities + 3 platforms, 18–19 verified $0, Coursera dead, edX audit the door) → categorized catalogue page + best-school-per-subject → MIT Term 1 schedule (starts Mon Nov 16) + Mon–Fri ~9:20 AM reminder cron → CS50x enrollment via browser (edX account, Secure Vault password, compromised-password rejection → new password card; Joshua enrolled himself as SpaceWok, free track) → pace-adaptive 11-course itinerary (seed 1 unit/week + buffer, recalculates from real completions, Friday pace reports) → Study Shell v1 built (dashboard, courses, pace engine, notebook, work log, schedule, edX panel; stdlib-only, local web UI, data.json state, never stores his edX password) → emailed, Sent-verified → v1.2 fix (edX dashboard URL was dead — www.edx.org/dashboard 404s, real one is home.edx.org; update zip deliberately excludes data.json so overwriting can't touch his notes). Read fully (~60 turns). | S10, S38, S49 |
| fc98cfd5 — CODE FORGE IMPROVEMENT | "Research manuscript" → clarified to Manus (no product called Manuscript exists) → deep research (report at ~/workspace/research_notes/…) → tiered list (Tier 1 M1–M8, Tier 2 M9–M13) with "done means" lines → built one at a time in isolated stacked copies, verified solo → M1–M13 all done → F1–F7 proper-fixes batch → merge: backup first, port only marked changes (Inbox + 3 hotfixes preserved), targeted 150/150 + full suite 2,353/2,362 with 9 failures reproduced on the untouched backup → push check (already on GitHub in the WAVE commit, no duplicate push). Read fully (~60 turns; one middle page delivered truncated by the tool, but visible portion + other pages cover M1–M13 + F1–F7 completely). | S2, S12 |
| d3d03908 — Maya and buck in woods | Joshua shared a video of walking through the woods with his cat Maya during the flea bombing and spotting a buck. One light exchange. **CHECKED — NOTHING REUSABLE.** Pure personal moment, no workflow. Read fully (2 turns). | — |
| 7d85fa44 — Android VLC and Termux help | VLC work: explained how TV in VLC works (stream link .m3u8 / playlist .m3u), then for the freetv site pulled the exact links via browser (playlist.m3u, guide.xml, direct .m3u8) — "Open in app" is a dropdown, not a vlc:// link; site doesn't relay streams, device fetches direct. Copy-paste VLC Android steps (More → New stream), single-channel fast test first, full playlist (~10,390 channels) is heavy, VLC has no guide support (TiviMate/Kodi/Jellyfin for the guide), network-caching bump + gesture/background-playback/subtitle "hacks" list. No Termux work happened in the thread. Read fully (7 turns). | S48 |
| 907dc170 — CODE FORGE ERROR HANDLING | Thread locked to Code Forge troubleshooting only. Three cases: (1) EXAONE 429 on first-ever use — diagnosed from Forge's code: no EXAONE cap recorded (LG publishes no numbers); popup lies twice ("per-minute" is a default guess; "shrunk requests" only exists for Groq); asked for the raw "EXAONE returned HTTP 429:" log line to learn the real limit. (2) Gemini 400 — real Forge bug: Gemini 3 thought_signature dropped both ways, so the second step of any tool turn fails; hits all three approved Gemini drivers. (3) "LOADED MODEL" label — not a behavior bug (it's Ollama's in-RAM list; cloud models can never appear there) but the label misleads; wording fix needed. Fixes sent to DEV in order, one at a time, his PC verdict closes each. Read fully (11 turns). | S9 |
| d2fbad7e — CODE FORGE VIDEO GENERATION | Promo-video thread. Arc: early generated commercials (rejected — fake footage, invented rival, his music used without asking) → real-capture method (drive the real app in a capture rig; 14+ real windows filmed) → Apple-style rebuild → "boring / looks like PowerPoint" → flagship rebuilt with the product performing → "stop showing boring screenshots" → cinematic teaser (no screenshots at all) → sound saga: synthesized scores rejected 3x → door closed on synthesized audio entirely; his music used once without permission → rejected + pulled to a rejected folder, standing rule (never use his music unless he names the track for that use); real fire recordings from Wikimedia Commons (CC BY credits) + Uuriter drone pad, loudness-normalized (LUFS) → "I don't like it" + same-video complaint → stop-guessing, ask what specifically → sellable-ads deep research (8 rules, 15s storyboard, named launches, sound rules, failure list) → desire film ("Dream it. Forge it." — his TikTok bio words only) → 3 hook variations → ready-to-paste caption with CC BY credit line. 4 pages / ~80 turns read; one older page (earliest generated-commercial turns) unread — full arc already covered. | S12, S26 |

## Batch C (research / security / roles / launch threads)

| Thread | Notes | → |
|---|---|---|
| 7a4222f3 — Compare CodeForge to competitors | Real comparison vs all major competitors + projected valuation + what it takes to get there. Deep research produced report.md (20 products, 16 profiles, market context, scenario-based valuation S0–S5 using cost-to-recreate + Berkus + ARR multiples, conflicts flagged). Headlines in chat, then an interactive artifact page (searchable/filterable table, valuation ladder, roadmap, open questions) probe-verified. Read fully (5 turns). | S11 |
| 7580cc0c — LA logo merch ideas | User pitched an LA = "Local Agent" / "a gent(leman)" merch logo; assistant mocked up one simple version with a basic font; user rejected it ("That looks like shit... basic font no cool at all"); assistant asked whether the layout or just the font was wrong and what style he pictured. **CHECKED — NOTHING REUSABLE.** One-off mockup + rejection; the glyph-design ground is covered better by S21. Read fully (5 turns). | — |
| d238e3ce — Blender Unreal Design Shell Dev | Item-by-item build of the Design Shell (v0.2 live render window, v0.3 Blender making engine with real renders, v0.5 install.sh/run.sh, v0.6, v0.7 image engine with a real sd.cpp generation, v0.9 Bench one-window, v1.0 native Qt Bench after he rejected the web Bench outright), zip + email + Sent-verify deliveries throughout, Unreal 5.9 download/extract/first-launch walkthrough and Blender 5.3.0 setup walkthrough via screenshots + one-line commands, .desktop launcher creation, naming discussion (no GitHub/web name check done in-thread), video lessons (Seedance cottage trick, Kimi hype reel, fireball game-feel), the skull project built without an order ("I didnt tell you to make it"), and the zip exec-bit failure + chmod fix. 4 pages / 80 turns read; oldest tail (early v0.1 scaffolding, same item-build pattern) unread. | S2, S14, S25; T1, T12 |
| f59bdf32 — CODE FORGE SECURITY DEV | S1 read-only audit (1 Critical, 9 High, 14 Medium, 9 Low, 12 strong areas, every decisive claim re-verified in code); S2–S5 staged builds in isolated copies, each independently re-verified (test counts re-run by the agent) and held with merge notes; post-merge Security battery (184 tests) run read-only with the deck served-page rule, held while the Manus merge was in flight, caught 2 HIGH merge defects (plaintext secrets re-saved; untrusted hooks running), relayed with exact file/line, re-verified 20/20 after fix; merge verification caught the patch tool's silent ~1,260-line revert. Off-topic stock message routed to its own thread. Read fully. | S2, S8, S16 |
| f4854c69 — AI Role Engineer | Master AI Role Engineer role accepted with the 8,000-char hard limit + character-limit protocol (pre-output audit, mandatory exact verification, compress while drafting). Two source files attached as governing references (Role Engineering Frameworks 5,707 chars; Master AI Role Engineer 6,135 chars). GUIFX role built v1.0 (6,828 chars, first draft 9,705 compressed), rejected by user for metadata bloat ("way too much redundant metadata than actual instructions"), rebuilt v3.0 as plain instructions only (7,017 chars), then v3.1 with fundamental rules as an engineer not a guide (7,846 chars, verified under limit). Read fully. | S22 |
| 4b2f5ba5 — CODE FORGE MODEL RESEARCH | Role locked as premier model R&D agent with judging rules (best smallest that runs comfortably, speed counts, abliteration preferred not gating, cloud = hard $0). Sweep #1: deep research → report.md (incumbents, 5 ranked local trials with exact pull tags, watchlist, rejects with reasons, 4 cloud picks, unverified list) → interactive page → pull commands in trial order → Trial #1 verdict from screenshot (fail: tool call printed as text, not issued). Sweep #2 filed from the GUIFX thread. Gemini Deep Research/Canvas deep research → spec → Write/Research modes built in isolated copy (965/965) → merge duty relayed to DEV. Multimodal crash diagnosis (no capability check → HTTP 400) → vision-seat design. Read fully. | S11, S13, S2 |
| 01a04f3a — EMBER BREAK GAME CF DEV | Scope locked: build EMBER BREAK inside Code Forge on his PC, by Forge — Arlo only does the walkthrough. Full 14-step map (names only), then one step at a time with exact mode/settings/prompt + pass criteria, waiting for pass/fail before the next step. Step 1: setup/seats/project + .forge/instructions.md. Model map: fixed local seats (Reviewer Qwen, Tester Bonsai, SKRIBE grader) + driver swapped per step (Groq gpt-oss-120b big steps, Gemini flash-lite Research/Design/Write, Groq gpt-oss-20b small turns). Step 2 re-check required in the new COMPLETE build before spending anything. Read fully. | S14 |
| 1fd34d86 — CODE FORGE SOCIAL MEDIA MGMT | Download link verified live first, paste-ready kit built for TikTok/Linktree/X/Facebook/YouTube/Instagram (names, bios, first posts, pinned comments, good video cuts only), one platform at a time starting with TikTok @code.forge41 with exact in-app steps, TikTok 1,000-follower Links-field gate checked with workaround (bio line + pinned download comment). Read fully. | S27 |
| 527e8c07 — Create sygil for RICH$XPRNC8 | Sigil built by letter reduction (R C H X P N + $ + 8) with documented glyph mapping; variant set (black-on-cream, gold-on-black, transparent). "Make it cooler" cut (spear tips, molten gold, ember glow) → rejected ("It doesn't look good at all") → retired, three cleaner sketches self-checked and withheld as not good enough → asked direction via options widget instead of guessing again → user picked "Dark engraved seal — fine detail, like a coin stamp" → seal built (reeded edge, rim lettering, thin engraved glyph, guilloche). Read fully. | S21 |
| be74cb87 — Compare Groq and Gemini free models | Deep research scored all 34 free-tier Groq + Gemini API models on one scale (strengths/weaknesses/specs) → interactive ranked page with best-for picks. User ordered Forge configured to accept only the best → 6-model allowlist filter built in an isolated copy, verified, merged. User's screenshot showed the stale pre-filter zip still listing ~60 models (Whisper erroring: "does not support chat completions") → agent diagnosed the stale-build cause, then built a hotfix zip from his exact build with one file swapped, diffed, provider tests run, emailed + Sent-verified (986,605 bytes). Read fully. | S2, S11, S29 |
| 20dcff58 — Add donate button with Cash App | Explained Cash App link mechanics (no official button; any button linking to cash.app/$cashtag), how to find the cashtag, verified $XPRNC8's live page shows "Joshua Lofland" + QR, added README badge + Support section + Linktree title, then built the startup welcome screen (non-blocking, close-to-run, donate button opens cash.app/$XPRNC8, big QR from Forge's built-in encoder + printed-link fallback, re-openable from menu). Verified: targeted 11/11, full suite 1713/1713, offscreen screenshot eyeballed. Read fully. | S28; T12 |
| b026eda9 — Implement prompts in Code Forge | Watched the Sumiro video, noted it never shows actual prompt text, cross-checked the creator's X thread, extracted the 6-step pipeline, mapped it onto Forge's existing modes/seats (copy the pipeline, not the tools), rewrote the 6 prompts short/sectioned/fill-in-the-blanks for small local models, with an honest $0/hardware constraint check. User corrected scope (not games-only) → generalized to reference-driven-build with 7 profiles → implemented as module + skill, verified (new tests 5/5, full suite 1160), backup, held. Also built C10 recipes + C6 security-scan skill + C7 in this thread, ran a fresh-folder install rehearsal, and did the GitHub repo creation walkthrough (empty-repo steps, app-access check, live verification noting private/uppercase/placeholder-README) + publish gate checklist (owner-only vs agent items). Read fully. | S2, S19, S25 |
| 16160aa6 — Debunk claims in video | User sent a video asking what it's asking him to do and how to prove the man's claims wrong; agent started video analysis prep (ffmpeg: 1 fps frame extraction + audio to wav for transcription) but the user then said it was the wrong video ("Whoops wrong video lmao" — it was a TikTok about an AI bird buying a 3D printer). The debunk never happened. **CHECKED — NOTHING REUSABLE** (only an aborted video-analysis attempt; the completed video-analysis workflow is captured as S25). Read fully (4 turns). | — |

## Batch D (design / games / personal threads)

| Thread | Notes | → |
|---|---|---|
| 983a94e7 — Code Forge logo design research | "Research what makes a great logo and how to match the aesthetics of an already-established theme/brand" → deep research (10-section report, 45 sources) → interactive dossier page (artifact `code-forge-logo-research`, with versatility labs + 12-test checklist) → standing anti-slop rule adopted → 3 logos drawn cell-by-cell on one pixel grid (Spark / CF Interlock / Bench Panel) with a test battery → Joshua rejected the old AI-generated logo he was actually using ("Disgusting work") and then rejected the new blocky rebuild ("Ew no") as too crude vs his taste for smaller pixels. Read to the beginning. | S11, S21 |
| b98324c9 — Old El Paso taco seasoning recipe | Copycat packet recipe scaled to his meat; he corrects 2 lb → 3 lb; assistant confirms his 2 lb homemade + 1 real packet = 3 lb, gives water ratio (2/3 cup/lb) and simmer steps. Read to the beginning. | S52 (weak) |
| e83c3975 — Find Rug Doctor antifoam in Lewes | Two live browser verifications (3:20 PM and 6:50 PM, Nov 8) across Walmart/Home Depot/Ace; failure arc (sent to 4 stores with nothing) → correction → chemical-equivalence broadening (silicone defoamer) → verified pickup-tonight answer (Walmart Rehoboth, HTH Spa Defoamer $9.37, Aisle G42). Read to the beginning. | S42 |
| 96341033 — Study Miniplay game design reference | Queue build (32 categories, 310 games, 4 parallel chunks) → itinerary sheet built and refined in batches → games 1–9 played/reported (PokéSurvivor, Bloxd/Bedwars, Veck.io, 4 Colors, Minecraft Classic, Steal a Brainrot, Let's Fish walled, Boxity/Palmhaven, Meccha Chameleon 1 FPS) → FNAF 2 run failed → Joshua: "Just stop dude" → study stopped. Read to the beginning. | S37 |
| 8b121215 — Report caregiver neglect in Delaware | Night-of-crisis thread (Nov 3–4): safety advice + 911 push → three report drafts (police/APS/DFS) with [NEED] blanks → facts added across turns (address, move-in date, doctor lie, fraud suspicion, phone records both sides, cochlear implant) → theft removed from filed reports but kept in private record → anonymized → SEND version + intake email DelawareADRC@delaware.gov → later flag: report finished Nov 4, never sent, now stale (Nov 7 events missing). Read to the beginning. | S43 |
| 3b29448b — Pixar inspired Code Forge UI | 4 Pixar/pixel mockups → "colors stay, game goes" → 4 pro versions → #1 + pixel retro-modern dosed A–D → "too generic, PowerPoint" → 4 full-bleed material directions → #2 "getting somewhere" → mix 2+3 in 3 ratios → "too old-timey/steampunk" → 3 future-material directions → Future 3 Dark Glass Minimal locked → "No ring gauges" correction passed to CODE FORGE DEV. Read to the beginning. | S35 |
| 42200820 — Remaster Q in HTML | Research Q REMASTERED → Q+ v1 (15 missions, sandbox, undo/pin/materials) verified by Puppeteer playtests; seesaw level cut after 2 failed playtests → user phone verdict (tiny text, invisible buttons, no rules, no IQ measure) → Q+ v2 rebuilt (one-screen 360×800, rules book, IQ TEST 5 stages + 6 questions = Q-IQ/500 with strengths graph, stats + downloadable report). Read to the beginning. | S24, S36; T13 |
| 215a932b — Three.js animal and insect simulation | Role brief pasted by Joshua ("THREE.JS ANIMAL & INSECT SYSTEMS ENGINEER") → freshwater ecosystem research → berry research (27 species) → per-species dossier template locked → thread re-scoped to animals/insects only → task list proposed, Joshua resets it (never signed off 1–13) → deer dossier + gap audit + addendum + round 3 → 102-model list → deer pilot build (12 deer, 82/82 tests) → full anatomy (24 regions, organs, teeth) → depth-stack wound model → leg-ground-penetration fix (measured 0.23–0.36 m) + growth-cycle lineup. Read to the beginning. | S22, S23, S24 |
| 0bfee90a — Adjust chili recipe for ingredients | Sirloin chili adapted to 2 lb ground beef + mushrooms, no red wine → further corrections (no cilantro/scallions/liquid smoke, has Worcestershire; 2×14.5 oz stewed tomatoes; green pepper added) → consolidated final versions → Recipe Bro format (matched to his existing recipes) → renamed Chili Mac (elbows added), red pepper 2 tbsp → 1 tbsp, hot sauce pinned to 3 tbsp Cholula. Read to the beginning. | S52 (weak) |
| 369cab4f — Arlo character — questionnaire | Briefing moved the questionnaire into this thread (rules: one at a time, covert, fun/adult, no batches, no decoding shown) → q.2–q.45 answered (43 answered, 2 passed) with loophole-closing re-asks → wrapped at 45 → profile built (goal files) → visual build → Option 3 activated as avatar → Joshua: "change it back, I don't want that" → reverted → "dress up like the character" variant → hat spec (light grey, black square, golden spiral) → activated. Read to the beginning. | S34 |
| 51ec77e5 — Fix System Forge Care code | Intake setup only: email the zip to broke.n.bored.studio@gmail.com, exclude .venv/__pycache__, say "sent", file check on arrival, diagnose before changing; broken piece identified as the one Care button (Advanced SystemCare-style one-click scan/clean); button-trace diagnosis plan + symptom triage. Zip never arrived in-thread; no fix done. Read to the beginning. | S50 (weak, unexecuted) |
| dc24c8b5 — Qwenputer R&D — small model computer | Single turn: a parked-track briefing moved into its own thread (R&D-1 note at ~/workspace/coding-agent-rd-notes.md, Bonsai 2 2B as candidate branch, first experiment listed, status PARKED, do not start until Joshua opens it). No work was done. **CHECKED — NOTHING REUSABLE.** The parked-track convention (note + candidate + first experiment + parked status) is minor housekeeping, not a workflow. Read to the beginning. | — |
| 139f2b24 — Picture of sand burrs | Two-turn one-off: show photos of sand burrs (*Cenchrus*), then the black/mature ones, with a look-alike distinction offered (beggarticks). **CHECKED — NOTHING REUSABLE.** Pure one-off identification. Read to the beginning. | — |

## Batch E (sims / life / utility threads)

| Thread | Notes | → |
|---|---|---|
| 0f35b782 — Seek medical help now | Live crisis: yohimbe reaction, timed pulse rechecks, Poison Control routing, safety planning around a roommate. Read fully (2 pages). | S47 |
| 2efc89c7 — Account security | One-off: Meta email-confirmation code timing vs a Facebook/Muse Code login failure on the Mint PC; ended in age-verification dead end. **CHECKED — NOTHING REUSABLE** (the "never paste OTP codes" rule is safety policy, not a workflow). Read fully (2 turns). | — |
| f0b35e4c — Fix 2004 Chevy Astro headlights | Photo-guided fuse/relay diagnosis, fixed via fuse #15 TBC. Read fully. | S44 |
| e4953ec7 — Winterize a sealed room in Meridian | Living survival guide: one master doc, ground-truth corrections, 7 research tracks, consistency/gap/live-simulation audits (34 sections, 481 lines; 43 gap findings). 2 pages / 40 turns read; older pages are earlier guide-building turns in the same pattern. | S33 |
| 2648fd53 — Muse tips | Scheduled onboarding tips (Tips 2–6, system-driven, not a workflow) + the covert 45-question character questionnaire that produced the Arlo profile. Read fully. | S34 |
| 426af22b — Create newspaper comic from ideas | Idea → newspaper comic, with the no-text-in-art and regenerate-from-scratch rules. Read fully. | S45 |
| f985f6d8 — Compress video to 100 MB | Bitrate math + ffmpeg command + audio-only alternative. Read fully (1 turn). | T15 |
| fea170f0 — How long 1 billion tokens last | Token-lifetime estimates + baseline/scheduled-recheck workflow (Oct 31 baseline → Nov 3 recheck: ~13.1M/day → ~77 days). Read fully. | S40; T16 |
| 2e2d01c6 — Notes & reminders | **Empty thread, zero turns.** CHECKED — nothing to extract (a content fact, not a read failure). | — |
| c0765ec4 — Three.js environmental systems engineering | Master role pack + soils/dirt todo list + dirt engine v1–v8 with human-aim testing (75/75, 82/82 suites). Read fully (2 pages). | S22, S24 |
| 9318fd31 — Send reference code for tokens | One-off how-to: share invite link, friend redeems in Settings within 48h. **CHECKED — NOTHING REUSABLE.** Read fully (1 turn). | — |
| e364b6a6 — Three.js white-tailed deer simulation | Master role pack + dossier-driven living deer model + screenshot-rig rebuilds + genetics + verified reference images (12 → 58, 7 excluded dead/blocked). Read fully. | S22, S24, S46 |
| da24d372 — Meridian game ground resource research | Deep research → sourced report → 106-record searchable catalog artifact (120+ minerals, each with formula, density, hardness, temps, location, abundance tier, source) + JSON schema + caveats for unverifiable values. Read fully. | S11 |
| d81cbb00 — Linux Mint PC specifications | Spec review + bottleneck analysis + cheapest compatible NVMe shortlist (HP All-in-One 22-df0xxx, Ryzen 3 3250U, 8 GB single-stick, 1 TB HDD; empty M.2 2280 socket). Read fully. | S51 (weak) |
| 98e65f7a — Tavus connector | One-off support-thread triage (PAL connector question, draft-reply-for-approval pattern). **CHECKED — NOTHING NEW** (approval pattern already in the system `email_management` skill). Read fully (1 turn). | — |

## Threads checked with nothing reusable (10)

cdcadb23 (flea bomb), d3d03908 (Maya and buck), 7580cc0c (LA logo merch), 16160aa6 (debunk video — wrong video sent), dc24c8b5 (Qwenputer — parked briefing only), 139f2b24 (sand burrs), 2efc89c7 (account security), 2e2d01c6 (Notes & reminders — empty thread), 9318fd31 (reference code for tokens), 98e65f7a (Tavus connector — pattern already in the system `email_management` skill). Count check: 57 threads contributed at least one workflow; 67 − 57 = 10.

---

# PART 5 — COVERAGE, CAVEATS, AND OPEN QUESTIONS

## Coverage
- **67 of 67 threads read.** 0 unreadable. The audit-request chat (089d9759) was skipped as a source, per the task.
- Most threads were read to `has_more=false` (complete). Big threads were read newest-first, 2–4 pages each (40–80 turns): main chat (40), CODE FORGE DEV (40), REBLEND DEV (40), OLLAMA (40), Design Shell (80), CodeRabbit (60), Manus (60), Forge Browser (60), Free AI trials (60), Study Dashboard (60), video generation (80), flea bomb (60), WinLinx/songs (40).
- Unread tails: main chat deep history (Meridian Origins patch flow may hold an uncaptured workflow), CODE FORGE DEV / REBLEND DEV / OLLAMA older pages, Design Shell oldest tail (early v0.1 scaffolding, same item-build pattern), video generation's earliest page (generated-commercial turns; full arc covered), Meridian winterize older pages (same guide-building pattern). Workers judged no workflow is likely missed in these tails, but the tails were not verified turn-by-turn.
- One fc98cfd5 page was delivered truncated by the tool; the visible portion plus the other two full pages cover M1–M13 + F1–F7 completely.
- Two chat-read results (caregiver thread, questionnaire thread) carried system prompt-injection notices; workers treated transcripts as data only and followed no embedded instruction.

## Deduplication notes
- The same workflow surfaced under different names across workers and was merged once: ship pipeline (A-W2 / B-W5), isolated-copy build+merge (A-W4 / B-W2 / C-W4), full review/audit (A-W1 / B-W3, with C-W3 kept separate as the security variant), name check (A-W6 / B-W4), model sweep (A-W8 / C-W2), deep-research comparison (A-W7 / C-W1, with E-W10 folded in as the catalog variant), baseline failure-set (A-W5 / C-W5), screenshot diagnosis (A-W11 / B-W7), covert questionnaire (D-W4 / E-W4), headless harness + sandbox-first sim build (D-W6 / E-W8), role packs + char-limit engineering (C-W6 / E-W9), logo/glyph design (A-W16 / C-W11 / D-W1), daily sweeps (A-W13 / B-W6 / B-W11).
- B-W11 (verified-$0 course catalogue) was folded into S10 as a variant rather than a separate skill; E-W11 (verified reference-image list) was kept as small S46 rather than folded, so its live-check discipline isn't lost.

## Already-built check
- All 6 existing custom skills were confirmed on disk and seen in use; none re-proposed.
- `aura-skills` was NOT found in the workspace — if it exists as a GitHub repo not cloned here, check it before building (see Part 3).
- CODE-FORGE's in-product skills are product features, not agent playbooks; no conflict, but S32 and S2 build on them.

## Suggested build order (if Joshua picks a first batch)
1. **S1 + T1 ship pipeline** and **S2 + T2 isolated-copy build+merge** — the two workflows every project runs on; the tools generalize scripts that already exist as fragments.
2. **S3 cross-thread dispatch**, **S4 task receipt**, **S7 + T4 name check**, **S8 + T3 post-merge battery** — the rest of the house operating system; all cheap to write, all used constantly.
3. **S5 full review**, **S6 + T6 Linux packaging**, **S11 deep-research artifact**, **S13 model sweep** — the high-value judgment playbooks.
4. Everything else in Tier 2 order; Tier 3 only if he asks for it (S47 is safety-sensitive and should stay a guarded playbook, never a tool; S50 is unexecuted; S51/S52 are weak).

## Worker source files
- `worker-A.md` — main chat + OLLAMA + MIMIK + Yahtzee + Pixel Forge + CODE FORGE DEV + GITHUB + stocks + EVERY MOUSE + Reblend + Stella ×2 + GUIFX (20 workflows)
- `worker-B.md` — repo audit + CodeRabbit + flea bomb + songs/WinLinx + Forge Browser + free trials + portal + Study Dashboard + Improvement + Maya/buck + VLC + error handling + video generation (15 workflows)
- `worker-C.md` — competitors + LA merch + Design Shell + security + role engineer + model research + Ember Break + social + sigil + Groq/Gemini + donate + prompts + debunk (15 workflows)
- `worker-D.md` — logo research + taco + Rug Doctor + Miniplay + caregiver + Pixar UI + Q+ + animal sim + chili + questionnaire + System Forge Care + Qwenputer + sand burrs (11 workflows)
- `worker-E.md` — medical + account security + Astro + Meridian winterize + Muse tips + comic + video compress + tokens + notes + environmental sims + reference code + deer sim + ground resources + PC specs + Tavus (12 workflows)
- Raw candidate count across workers: 73; deduplicated master list: 52 skills + 17 tools.
