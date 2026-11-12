# Read-only security audit

## When to use

- Use this skill when the user orders a security audit of a codebase.
- Use it before fixes are planned, so the user directs from a ranked list instead of from a guess.
- Change nothing during the audit. The scope is frozen and read-only, and the fixes come later as their own items.

## Freeze a read-only scope

- Freeze the scope before you start: the tree and the named copies you will read, and nothing else.
- Touch nothing in the tree. Read the code, run no writes, and make no fixes, even small ones.
- Record the exact tree state you audited, so a later reader can tell what the findings apply to.

## Scan in independent passes and rank the findings

- Scan the frozen scope in independent review passes, each looking for a different class of problem, so one pass does not inherit another pass's blind spots.
- Rank every finding Critical, High, Medium, or Low, and ground each one in the code with the file and line.
- Name the areas that are genuinely strong too, with the evidence that shows it, because a report that only lists faults hides what is already safe.
- Re-verify every decisive claim in the code by hand before you report it, and drop any claim the code does not support.

## Report the ranked findings and stop

- Deliver the report in chat with the severity counts and the top findings, and write the full report to a file for the record.
- Keep every finding tied to the code that proves it, and flag anything you could not verify instead of dressing it up as a finding.
- Change no code, file no fixes, and start no build item. The user directs the next step from the list.
- Offer to build the picked fixes one at a time (see isolated-copy-build-merge) once the user has chosen.

## Where this comes from

- This shape ran as the Code Forge S1 audit (1 Critical, 9 High, 14 Medium, 9 Low, 12 areas genuinely strong) and the earlier full-codebase audit with four independent review passes and hand re-verification of decisive claims. It is recorded in the BNB audit as S16.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.
- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Offer a narrow follow-up audit of one subsystem when the full audit surfaces a deep problem in one place.
- Offer to re-audit after the picked fixes land, instead of letting the old report describe a changed tree.
