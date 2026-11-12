# Cursor configuration

## Overview

Cursor is configured through rules stored in `.cursor/rules/`. These are short, scoped instruction files that guide implementation within the repository’s product and security model.

## Rule structure

The repository uses Cursor rule files in the standard `.mdc` format with YAML frontmatter, for example:

- `global.mdc` — repository-wide rules
- `frontend.mdc` — web implementation rules
- `backend.mdc` — API implementation rules
- `database.mdc` — data and tenant boundary rules
- `business-partner.mdc` — Business Partner-specific boundaries
- `ai-hacker.mdc` — AI Hacker-specific boundaries
- `testing-security.mdc` — validation and security rules

Each rule is scoped either globally or by file pattern. This keeps the instructions specific without duplicating the entire repository policy in every file.

## What the rules enforce

- architecture and product alignment,
- no feature drift from the approved design set,
- no unsafe or unrestricted execution in the Hacker domain,
- no Business Partner access to Hacker privileges,
- frontend/backend separation,
- secrets handling,
- testing/verification and Git safety expectations.

## Maintenance

The rules should be updated whenever the repo structure, product boundaries, or security assumptions materially change. The rule set should remain consistent with `AGENTS.md`, `.github/copilot-instructions.md`, and the approved docs in `docs/`.
