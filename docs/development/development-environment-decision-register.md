# Development environment decision register

## 1. Purpose

This document records the environment, tooling, and workflow decisions for the Day 12 development-foundation stage.

## 2. Decision log

### DEV-001: monorepo retained

Decision:
- Keep the existing monorepo structure for the current stage.

Reason:
- the repository already reflects the shared platform + specialist product structure and there is no strong reason to split early.

Status:
- retained.

### DEV-002: pnpm + uv + Docker remain the standard stack

Decision:
- Use pnpm for the web workspace, uv for Python tooling, and Docker Compose for local database and app services.

Reason:
- this matches the current repository and the existing CI setup.

Status:
- retained.

### DEV-003: PostgreSQL remains the local data store

Decision:
- Keep PostgreSQL as the default local data store.

Reason:
- it is already configured in the repository and matches the architecture direction.

Status:
- retained.

### DEV-004: local env files remain local-only

Decision:
- Track example env files and ignore local `.env` files.

Reason:
- prevents accidental credential leakage while keeping setup reproducible.

Status:
- retained and documented.

### DEV-005: CI remains minimal and toolchain-aligned

Decision:
- Keep the existing CI workflow as the baseline until additional project complexity justifies expansion.

Reason:
- it already validates the current stack without unnecessary automation.

Status:
- retained.

### DEV-006: no additional infrastructure added yet

Decision:
- Do not add Redis, message brokers, vector stores, or Kubernetes for the current phase.

Reason:
- the repository does not yet show a clear requirement for them.

Status:
- no new infra added.

## 3. Outstanding environment decisions

- final branch protection policy for GitHub
- exact approval path for shared tooling changes across products
- any future separate deployment requirements if product teams decouple

## 4. Summary

The repository is already in a sensible shape for structured development. The development-foundation work is primarily about documenting and reinforcing existing conventions rather than replacing them with a larger process or infrastructure layer.
