#!/usr/bin/env python3
"""Generate skills.json from the skill tree.

Reads every skill folder (skill.yaml + SKILL.md) under the repo root and
writes skills.json at the root: one entry per skill with number, slug,
title, description, tier, category, include_in_prompt, and files (the
files in the skill folder, as paths relative to the skill folder).

skills.json is GENERATED. Do not hand-edit it. Regenerate with:

    python3 scripts/generate_catalog.py

Run from the repo root (or anywhere; the script finds the root from its
own location). Standard library only, no dependencies.

Number and tier come from skill.yaml when present. During the audit-fix
migration some yamls may not carry them yet; in that case they fall back
to the README tier tables, which are the verified index.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
OUT = ROOT / "skills.json"

# One row of a README tier table:
# | S1 | [`ship-pipeline`](ship-pipeline/) | description | 1 |
ROW_RE = re.compile(
    r"^\|\s*S(\d+)\s*\|\s*\[`([^`]+)`\]\(([^)]*)\)\s*\|.*\|\s*([123])\s*\|$"
)


def parse_scalar(raw):
    """Parse one simple YAML scalar: double-quoted, single-quoted, or plain."""
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


def parse_yaml(path):
    """Parse the flat key: value skill.yaml into an ordered dict."""
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"{path}: cannot parse line: {line!r}")
        key, raw = line.split(":", 1)
        data[key.strip()] = parse_scalar(raw)
    return data


def read_readme_index():
    """Return {slug: (number, tier)} from the README tier tables."""
    index = {}
    if not README.exists():
        return index
    for line in README.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line.strip())
        if m:
            index[m.group(2)] = (int(m.group(1)), int(m.group(4)))
    return index


def skill_folders():
    folders = []
    for child in sorted(ROOT.iterdir()):
        if child.is_dir() and (child / "skill.yaml").exists():
            folders.append(child)
    return folders


def parse_number(value):
    """Accept a skill number as a bare int or an "S<n>" string."""
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    if isinstance(value, str):
        m = re.fullmatch(r"S(\d+)", value.strip())
        if m:
            return int(m.group(1))
    raise ValueError(f"bad skill number: {value!r}")


def build_entry(folder, readme_index):
    slug = folder.name
    yaml_data = parse_yaml(folder / "skill.yaml")
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        raise ValueError(f"{slug}: SKILL.md missing")
    number = yaml_data.get("number")
    tier = yaml_data.get("tier")
    if number is None or tier is None:
        fallback = readme_index.get(slug)
        if fallback is None:
            raise ValueError(
                f"{slug}: skill.yaml has no number/tier and README has no row"
            )
        if number is None:
            number = fallback[0]
        if tier is None:
            tier = fallback[1]
    number = parse_number(number)
    files = sorted(
        str(p.relative_to(folder))
        for p in folder.rglob("*")
        if p.is_file()
    )
    return {
        "number": number,
        "slug": slug,
        "title": str(yaml_data["title"]),
        "description": str(yaml_data["description"]),
        "tier": int(tier),
        "category": str(yaml_data["category"]),
        "include_in_prompt": bool(yaml_data["include_in_prompt"]),
        "files": files,
    }


def main():
    readme_index = read_readme_index()
    entries = []
    for folder in skill_folders():
        entries.append(build_entry(folder, readme_index))
    entries.sort(key=lambda e: e["number"])
    numbers = [e["number"] for e in entries]
    if numbers != list(range(1, len(entries) + 1)):
        print(
            f"error: skill numbers are not contiguous 1..{len(entries)}: {numbers}",
            file=sys.stderr,
        )
        return 1
    OUT.write_text(
        json.dumps(entries, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT} with {len(entries)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
