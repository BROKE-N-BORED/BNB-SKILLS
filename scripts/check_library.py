#!/usr/bin/env python3
"""Check the BNB-SKILLS library against the audit-fix standard.

Run from the repo root (or anywhere; the script finds the root from its
own location):

    python3 scripts/check_library.py

Exit 0 when every check passes, 1 otherwise, with a per-check failure
list. Standard library only, no dependencies. Also run in CI on every
push and pull request (see the validate workflow).

Checks:
  (a) README tier tables match the tree: one row per skill folder,
      numbers contiguous S1-S<N> for N skill folders, slugs match
      folder names exactly, each row's tier column matches the tier
      table it sits in, tier counts sum to N, and the number/tier in
      each skill.yaml agree with the README row.
  (b) Every skill.yaml parses with exactly the 7 keys, in order: name,
      title, description, category, include_in_prompt, number, tier.
      Also: name matches the folder slug, include_in_prompt is a
      boolean, number is an "S<n>" string (a bare integer is also
      accepted), tier is 1, 2, or 3.
  (c) Every SKILL.md H1 title matches its yaml title after stripping
      the "S<n> - " number prefix from the H1.
  (d) Every supporting file (references/, templates/, examples/) is
      referenced by filename from its own skill's SKILL.md.
  (e) No absolute install or sandbox paths in any .md/.yaml/.yml/.py/
      .json file, except docs/AUDIT.md (see below).
  (f) No TODO/FIXME placeholders (a TODO/FIXME marker followed by a
      colon, or in square brackets). The words "todo" and "TODOs" in
      ordinary prose are not placeholders and do not fail this check.

Exclusion: docs/AUDIT.md is a verbatim historical copy of the audit
that sourced this repo, kept byte-identical as provenance. It is
excluded from checks (e) and (f) because editing it would destroy that
provenance; it is never edited in place.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPECTED_KEYS = [
    "name",
    "title",
    "description",
    "category",
    "include_in_prompt",
    "number",
    "tier",
]

ROW_RE = re.compile(
    r"^\|\s*S(\d+)\s*\|\s*\[`([^`]+)`\]\(([^)]*)\)\s*\|.*\|\s*([123])\s*\|$"
)
TIER_HEADING_RE = re.compile(r"^#{1,6}\s+Tier\s+([123])\b")
HEADING_RE = re.compile(r"^#{1,6}\s+")
H1_PREFIX_RE = re.compile(r"^S\d+\s+[-\u2013\u2014]\s+")
PLACEHOLDER_RE = re.compile(r"(?:\b(?:TODO|FIXME)\b\s*:|\[(?:TODO|FIXME)\])",
                            re.IGNORECASE)

# Absolute-path patterns, built from pieces so this file's own source
# contains none of the literal strings it scans for.
ABS_PATH_PATTERNS = [
    "/o" + "pt/",
    "/ho" + "me/",
    "~/" + "workspace",
    "/tm" + "p/",
]

EXCLUDED = {Path("docs/AUDIT.md")}
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".json"}
SUPPORT_DIRS = {"references", "templates", "examples"}


def parse_scalar(raw):
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == '"' and raw[-1] == '"':
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return raw[1:-1]
    if len(raw) >= 2 and raw[0] == "'" and raw[-1] == "'":
        return raw[1:-1].replace("''", "'")
    if raw == "true":
        return True
    if raw == "false":
        return False
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


def parse_number(value):
    """Accept a skill number as a bare int or an "S<n>" string.

    Returns the integer, or None when the value is neither.
    """
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, str):
        m = re.fullmatch(r"S(\d+)", value.strip())
        if m:
            return int(m.group(1))
    return None


def parse_yaml(path):
    """Parse the flat key: value skill.yaml. Returns (keys, values)."""
    keys = []
    values = {}
    for lineno, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"{path}:{lineno}: cannot parse line: {line!r}")
        key, raw = line.split(":", 1)
        key = key.strip()
        keys.append(key)
        values[key] = parse_scalar(raw)
    return keys, values


def skill_folders():
    return sorted(
        child for child in ROOT.iterdir()
        if child.is_dir() and (child / "skill.yaml").exists()
    )


def read_text(path):
    return path.read_text(encoding="utf-8")


def check_readme(folders):
    """(a) README tier tables match the tree."""
    failures = []
    readme = read_text(ROOT / "README.md")
    rows = {}  # slug -> (number, tier, link_target)
    tier_counts = {1: 0, 2: 0, 3: 0}
    current_tier = None
    for line in readme.splitlines():
        stripped = line.strip()
        m = TIER_HEADING_RE.match(stripped)
        if m:
            current_tier = int(m.group(1))
            continue
        if HEADING_RE.match(stripped):
            current_tier = None
            continue
        m = ROW_RE.match(stripped)
        if not m:
            continue
        if current_tier is None:
            failures.append(f"README: skill row outside a tier table: {stripped}")
            continue
        number, slug, target, tier_col = (
            int(m.group(1)), m.group(2), m.group(3), int(m.group(4)))
        if slug in rows:
            failures.append(f"README: duplicate row for slug {slug!r}")
        rows[slug] = (number, tier_col, target)
        tier_counts[current_tier] += 1
        if tier_col != current_tier:
            failures.append(
                f"README: S{number} {slug} sits in the Tier {current_tier} "
                f"table but its tier column says {tier_col}")
        if target != slug + "/":
            failures.append(
                f"README: S{number} {slug} link target is {target!r}, "
                f"expected {slug + '/'}")
    total = sum(tier_counts.values())
    expected = len(folders)
    if total != expected:
        failures.append(
            f"README: {total} skill rows, expected {expected} "
            f"(Tier 1: {tier_counts[1]}, Tier 2: {tier_counts[2]}, "
            f"Tier 3: {tier_counts[3]})")
    numbers = sorted(n for n, _, _ in rows.values())
    if numbers != list(range(1, expected + 1)):
        failures.append(
            f"README: numbers are not contiguous S1-S{expected}: {numbers}")
    folder_slugs = {f.name for f in folders}
    missing = folder_slugs - set(rows)
    extra = set(rows) - folder_slugs
    if missing:
        failures.append(
            f"README: no row for skill folders: {sorted(missing)}")
    if extra:
        failures.append(f"README: rows with no skill folder: {sorted(extra)}")
    # yaml number/tier agree with the README row
    for folder in folders:
        slug = folder.name
        if slug not in rows:
            continue
        try:
            _, values = parse_yaml(folder / "skill.yaml")
        except ValueError:
            continue  # reported under (b)
        number, tier_col, _ = rows[slug]
        if "number" in values:
            yaml_number = parse_number(values["number"])
            if yaml_number is None:
                failures.append(
                    f"{slug}: yaml number {values['number']!r} is not "
                    'an "S<n>" string or integer')
            elif yaml_number != number:
                failures.append(
                    f"{slug}: yaml number {values['number']!r} != README S{number}")
        if "tier" in values and values["tier"] != tier_col:
            failures.append(
                f"{slug}: yaml tier {values['tier']!r} != README tier {tier_col}")
    return failures


def check_yamls(folders):
    """(b) skill.yaml parses with exactly the 7 keys, in order."""
    failures = []
    for folder in folders:
        slug = folder.name
        path = folder / "skill.yaml"
        try:
            keys, values = parse_yaml(path)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if keys != EXPECTED_KEYS:
            failures.append(
                f"{slug}/skill.yaml: keys {keys}, "
                f"expected {EXPECTED_KEYS}")
            continue
        if values["name"] != slug:
            failures.append(
                f"{slug}/skill.yaml: name {values['name']!r} != folder slug")
        if not isinstance(values["include_in_prompt"], bool):
            failures.append(
                f"{slug}/skill.yaml: include_in_prompt "
                f"{values['include_in_prompt']!r} is not true/false")
        if parse_number(values["number"]) is None:
            failures.append(
                f"{slug}/skill.yaml: number {values['number']!r} "
                'is not an "S<n>" string or integer')
        if values["tier"] not in (1, 2, 3):
            failures.append(
                f"{slug}/skill.yaml: tier {values['tier']!r} is not 1, 2, or 3")
        for key in ("title", "description", "category"):
            if not isinstance(values[key], str) or not values[key].strip():
                failures.append(
                    f"{slug}/skill.yaml: {key} is empty or not a string")
    return failures


def check_titles(folders):
    """(c) H1 title matches yaml title after stripping the S<n> prefix."""
    failures = []
    for folder in folders:
        slug = folder.name
        try:
            _, values = parse_yaml(folder / "skill.yaml")
        except ValueError:
            continue  # reported under (b)
        if "title" not in values:
            continue
        text = read_text(folder / "SKILL.md")
        h1 = None
        for line in text.splitlines():
            if line.startswith("# "):
                h1 = line[2:].strip()
                break
        if h1 is None:
            failures.append(f"{slug}/SKILL.md: no H1 title line")
            continue
        stripped = H1_PREFIX_RE.sub("", h1, count=1)
        if stripped != values["title"]:
            failures.append(
                f"{slug}/SKILL.md: H1 {stripped!r} != "
                f"yaml title {values['title']!r}")
    return failures


def check_supporting_files(folders):
    """(d) Every supporting file is referenced by its own SKILL.md."""
    failures = []
    for folder in folders:
        slug = folder.name
        text = read_text(folder / "SKILL.md")
        for sub in SUPPORT_DIRS:
            support = folder / sub
            if not support.is_dir():
                continue
            for path in sorted(p for p in support.rglob("*") if p.is_file()):
                if path.name not in text:
                    failures.append(
                        f"{slug}: {path.relative_to(folder)} not referenced "
                        f"by filename in {slug}/SKILL.md")
    return failures


def text_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel in EXCLUDED:
            continue
        if path.suffix in TEXT_SUFFIXES:
            yield rel, path


def check_abs_paths():
    """(e) No absolute install/sandbox paths (except docs/AUDIT.md)."""
    failures = []
    for rel, path in text_files():
        for lineno, line in enumerate(
                read_text(path).splitlines(), 1):
            for pattern in ABS_PATH_PATTERNS:
                if pattern in line:
                    failures.append(
                        f"{rel}:{lineno}: absolute path {pattern!r}")
                    break
    return failures


def check_placeholders():
    """(f) No TODO/FIXME placeholders (except docs/AUDIT.md)."""
    failures = []
    for rel, path in text_files():
        for lineno, line in enumerate(
                read_text(path).splitlines(), 1):
            if PLACEHOLDER_RE.search(line):
                failures.append(f"{rel}:{lineno}: {line.strip()[:120]}")
    return failures


CHECKS = [
    ("(a) README tier tables match the tree", check_readme),
    ("(b) skill.yaml: 7 keys in order", check_yamls),
    ("(c) H1 titles match yaml titles", check_titles),
    ("(d) supporting files referenced", check_supporting_files),
    ("(e) no absolute paths", check_abs_paths),
    ("(f) no TODO/FIXME placeholders", check_placeholders),
]


def main():
    folders = skill_folders()
    print(f"found {len(folders)} skill folders")
    all_pass = True
    for label, func in CHECKS:
        try:
            if func in (check_readme, check_yamls, check_titles,
                        check_supporting_files):
                failures = func(folders)
            else:
                failures = func()
        except Exception as exc:  # noqa: BLE001 - report, don't crash
            failures = [f"checker error: {exc}"]
        status = "PASS" if not failures else "FAIL"
        if failures:
            all_pass = False
        print(f"\n{status} {label} ({len(failures)} failures)")
        for failure in failures:
            print(f"  - {failure}")
    print("\nALL CHECKS PASSED" if all_pass else "\nCHECKS FAILED")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
