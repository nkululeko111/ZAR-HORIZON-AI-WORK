---
applyTo: "apps/api/**/*.py,apps/api/**/*.toml,docs/database/**/*.md,**/*.sql"
---

# Database and tenant isolation instructions

- Respect the data model in `docs/database/` as the baseline for tenant, workspace, and product boundaries.
- Do not create or modify database models or migrations outside an explicitly approved design change.
- Treat tenant isolation and workspace mapping as enforcement requirements, not UI preferences.
- The backend must enforce product and workspace separation; the frontend must not be trusted as the security boundary.
- If a change affects data lifecycle, permissions, or credential handling, review the architecture and database security documents before proceeding.
- Avoid adding infrastructure or data stores that are not justified by the approved architecture.
- Keep evidence, approval, and audit concerns aligned with the design requirements.

Read `docs/database/`, `docs/architecture/`, and `docs/api/` before any database-related change.
