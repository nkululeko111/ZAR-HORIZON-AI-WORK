---
applyTo: "apps/api/**/*.py,agents/**/*.py,apps/api/**/*.toml,agents/**/*.toml"
---

# Backend instructions

- Keep the FastAPI backend aligned with the approved API and architecture documents.
- Do not invent endpoints, schemas, or integrations that are not documented in the approved contract set.
- Respect the repository’s tenant and workspace boundary expectations; the backend is the enforcement point.
- Keep Python code readable, typed where practical, and consistent with the existing repository standards.
- Avoid broad refactors or new framework layers when a focused fix is enough.
- For any change affecting auth, permissions, approval logic, or tool execution, inspect the architecture and API documents first.
- When debugging Python code, prefer the smallest relevant validation command and report if tests or checks cannot run.
- Do not allow AI Hacker execution logic to leak into Business Partner workflows or vice versa.

For product and architecture alignment, read `docs/api/`, `docs/database/`, and `docs/architecture/` before implementing backend changes.
