# S30 — Brand scrub rename

Remove or replace a name across a whole tree, catch every straggler, migrate existing user data so it survives the rename, and prove nothing broke.

Companion tool: [T9 brand-scrub-rename](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/brand-scrub-rename) — grep-driven whole-tree substitution with straggler catch and migration scaffolding for user state keys.

## When to use

- A rebrand lands, a name has to go, or a policy scrub removes brand names from a project.

## Substitute grep-driven across the whole tree

- Find every occurrence of the old name with a grep across the whole tree before you change anything, and count what you find.

- Substitute the old name for the new name, or remove it, in docs, code, docstrings, and module and skill names, working through the grep results file by file.

- Keep a substitution count as you go, so the report can say how many substitutions landed and in how many files.

- Change only the name and the lines the rename needs, and leave working code around it alone.

## Catch stragglers with a whole-tree grep

- Run a case-insensitive whole-tree grep for the old name after the substitution pass, and check every hit it returns.

- Fix each straggler the grep finds, including a missed file the first pass never touched, and re-run the grep until it comes back clean.

- Check the name in every form it can appear, such as different capitalizations, hyphenated and unhyphenated forms, and names embedded in longer identifiers.

- Report the final grep as clean, with the command you ran, so the scrub is proven rather than claimed.

## Scrub the published surface too

- Scrub the published surface too, not just the code tree: live Release notes, CHANGELOG, and README on main. Verify 0 hits on the live pages, not just in the tree. (2026-11-12: the v2.5-gofish-decisions release notes said "(was Goldfish)" — caught by Joshua, not by the scrub.)

- Never mention the old name even parenthetically — no "(was Goldfish)" anywhere: no notes, no changelogs, no asides. The rule is zero mentions, full stop. Check every public word against the rule before publishing.

- Migration code reading old keys is a deliberate exception, not a miss: 12 lowercase "goldfish" literals were kept in main.py / planning.py because they read the user's old settings and plan keys so his data carries over. Flag them in the report as functional code, and drop them in a later build after his data is confirmed migrated — never in the scrub build itself. When grepping a published zip, expect those hits and treat them as code. If hits are migration code, report the count + locations and wait for his call — do not rebuild unilaterally.

- Before the next push, re-sync publish staging's CHANGELOG from main so a stale staging copy does not clobber the scrub.

## Migrate user state so data survives

- Find every place the old name lives in user state, such as plan keys, toggle keys, and known-skill lists, before the rename ships.

- Add state migrations that carry the old keys to the new keys, so existing user data survives the rename instead of being orphaned.

- Test the migration on a copy of real-shaped state, and say what the test showed.

- Never ship a rename that silently drops user data.

## Re-run the battery and report the receipt

- Re-run the full test battery on the renamed tree, and report the pass counts.

- Fix any failure the battery finds, and re-run until it is green.

- Report the rename as a receipt, with the substitution count, the file count, the clean final grep, the migration, and the battery result.

## Where this comes from

- From the CODE FORGE DEV (94792a18) and CODE FORGE GITHUB (7d1ee11c) threads — the no-brands scrub (235 substitutions, 28 files) and the Goldfish→GoFish rename (351 substitutions, 14 files, with state migrations so user data carried over). Recorded in the BNB audit as S30.

## Alternatives for better results

- Offer to run the scrub on the docs first and the code second when the tree is large, so each pass can be checked on its own.

- Ask the user to confirm the new name and its exact spelling and capitalization before the substitution starts.
