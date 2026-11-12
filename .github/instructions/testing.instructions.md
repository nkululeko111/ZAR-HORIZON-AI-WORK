---
applyTo: "apps/**/*.ts,apps/**/*.tsx,apps/**/*.py,tests/**/*.py,tests/**/*.ts,**/*.{yaml,yml}"
---

# Testing and quality assurance instructions

- Validate the smallest relevant checks for the change. Do not claim a broader verification that was not run.
- Frontend validation may include formatting, linting, type checking, tests, and build checks if the relevant project commands are available.
- Backend validation may include Python linting, testing, and migration checks as the repo allows.
- For API or contract changes, compare against the approved `docs/api/` baseline and run the relevant validation only if available.
- For database or tenant-boundary work, validate assumptions with the most relevant migration or isolation checks available.
- For agent security and approval logic, verify the permission model instead of assuming the flow is safe.
- If a command cannot run because the environment or dependency is missing, say exactly that and describe the blocker.

Read `docs/development/`, `docs/api/`, and the relevant product or architecture docs before interpreting a test result as authoritative.
