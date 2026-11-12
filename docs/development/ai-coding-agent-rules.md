# AI coding agent rules

## Core rules

The repository expects AI coding assistants to work as disciplined engineering partners rather than autonomous feature generators. The approved documents are the source of truth, not ad hoc assumptions.

## Required behaviour

- Understand the request and the affected subsystem.
- Inspect the relevant code and design documents before editing.
- Check whether the work is inside the authorisation and product scope.
- If a design conflict exists, ask for clarification instead of choosing arbitrarily.
- Prefer narrow, readable changes over broad refactoring.
- Keep existing architecture, security, and tenant boundaries intact.
- Do not invent new business logic, agent capabilities, database entities, integrations, or security authorities.

## Security and policy rules

- Keep credentials, secrets, and customer data out of prompts, logs, and repo files.
- Do not weaken approval or security controls to make a test or workflow pass.
- Respect the distinct Business Partner and Hacker domains.
- Treat the backend as the enforcement boundary and the frontend as a presentation layer.
- Keep evidence, auditability, and approval policy aligned with the repository design.

## Git and operational rules

- Inspect `git status` before substantial changes.
- Never overwrite unrelated user work or delete files without explicit approval.
- Avoid destructive Git commands.
- Never commit, push, merge, or deploy without explicit authorisation.
- Do not modify production configuration without approval.

## Validation rules

- Run the smallest relevant check for the affected subsystem.
- If the check cannot run, say why and do not infer success.
- Report files changed, assumptions, and remaining risks when the work is complete.
