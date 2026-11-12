---
applyTo: "docker-compose.yml,.github/workflows/**/*.yml,.env*,pyproject.toml,pnpm-workspace.yaml,package.json,**/*.toml"
---

# Infrastructure and configuration instructions

- Keep infrastructure changes aligned with the approved repository strategy and development standards.
- Do not modify production configuration, deployments, or cloud environment settings without explicit approval.
- Local infrastructure should remain minimal and reproducible; do not add Redis, message brokers, vector stores, or Kubernetes prematurely.
- Keep env files example-based and do not commit real credentials or secrets.
- Distinguish local development configuration from production configuration and document any assumptions.
- Respect the current monorepo setup with pnpm, uv, Docker Compose, PostgreSQL, and CI checks already present in the repo.
- If a change affects CI, env variables, or local services, update the documentation that reflects the environment baseline.

Read `docs/development/`, `README.md`, and `.github/workflows/ci.yml` before changing infrastructure or configuration files.
