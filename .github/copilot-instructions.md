# GitHub Copilot repository instructions

## Repository context

This monorepo contains a shared platform and two product domains:

- `apps/web` — Next.js / React / TypeScript frontend
- `apps/api` — Python / FastAPI backend and migrations
- `agents/business-partner` — Business Partner service scaffold
- `agents/hacker` — AI Hacker service scaffold
- `docs/` — approved product, architecture, API, UX, database, and development foundation documentation

This repo is intentionally design-first and governance-driven. The application is not a free-form product build; it is a controlled repository foundation.

## Required workflow

1. Read the relevant docs before changing a subsystem.
2. Check whether the request conflicts with the founder-approved architecture or product boundaries.
3. Keep the change narrow, understandable, and testable.
4. Inspect `git status` before substantial work.
5. Ensure secrets, credentials, and customer data stay out of prompts, logs, and repo files.
6. Validate only the checks that are actually available and runnable.
7. Report the files changed, assumptions, and any unresolved risks.

## Priorities

- Follow the approved architecture in `docs/architecture/`.
- Keep tenant, workspace, and product boundaries enforced by backend logic.
- Treat the frontend as a presentation layer, not a security boundary.
- Keep AI Hacker execution isolated and approval-driven.
- Keep Business Partner calculations deterministic and auditable.
- Prefer documentation updates when implementation changes affect the design baseline.

## Prohibited actions

- Do not implement product features or create unapproved UI pages or API routes.
- Do not add AI provider integrations or external services without approval.
- Do not create database migrations or data models without an explicit design change request.
- Do not expand into Kubernetes, microservices, or infrastructure changes outside the approved scope.
- Do not weaken approval, tenant-isolation, or security controls to make checks pass.
- Do not claim a CI, migration, or build passed unless it was actually run.

## Project commands

Use the repository’s known toolchain:

- `pnpm install`
- `pnpm format:check`
- `pnpm lint:web`
- `pnpm typecheck:web`
- `pnpm test:web`
- `pnpm build:web`
- `uv sync --all-packages --all-groups`
- `uv run --package zar-horizon-api alembic -c apps/api/alembic.ini upgrade head`
- `uv run --package zar-horizon-api ...` for backend checks when available
- `docker compose up --build` for local infrastructure in the approved stack

If a command is unavailable or a dependency is missing, say exactly why and do not assume success.

## Documentation sources of truth

Use these documents as the canonical guidance when making repo-level decisions:

- `docs/products/`
- `docs/architecture/`
- `docs/database/`
- `docs/api/`
- `docs/ux/`
- `docs/development/`
- `README.md`
