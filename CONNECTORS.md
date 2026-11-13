# Connectors used by these skills

Most skills in this repo need no connector at all — they are playbooks for
judgment, procedure, and verification. The skills that touch a live service
use the connectors below. Read the connector's current doc before running
its commands; the doc is the authority on setup, operations, and flags.

## GitHub

What it is for: checking whether a repo exists live (and whether it is
empty or holds the expected content), checking exact-name availability
before presenting a name, pushing a verified build, and cutting or updating
the Release that carries it.

Skills that use it include ship-pipeline, isolated-copy-build-merge,
name-availability-check, repo-identity-check, org-repo-audit-queue,
github-repo-creation-walkthrough, linux-release-packaging,
no-stalling-task-list-cycle, full-product-review, and
donate-support-wiring.

Docs: the GitHub connector's CONNECTOR.md in your Muse install.

## Gmail

What it is for: sending a build zip by email, reading the Sent folder back
to verify the attachment that actually went out, and pulling a source zip
attachment out of an emailed codebase intake.

Skills that use it include ship-pipeline, hotfix-zip,
email-zip-code-intake, no-stalling-task-list-cycle, debug-log-layer, and
authority-incident-report-drafting.

Docs: the Gmail connector's CONNECTOR.md in your Muse install.

## Custom connectors (custom-connector-setup skill)

What it is for: when no bundled connector fits the service a task needs,
find a maintained API or MCP server for it and set it up as a custom
connector — credential kept in Muse's secure connection flow, with a
connector doc and reusable skill saved alongside.

Docs: the custom-connector-setup skill in your Muse install.

## Finding other connectors

Use `muse.connector_search` to find other connectors and
`muse.skill_search` to find related skills. If nothing bundled fits, look
on the web for a maintained API or MCP server and set it up with the
custom-connector-setup skill, or build a custom connector.
