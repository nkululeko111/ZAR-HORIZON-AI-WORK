# CI and continuous integration foundation

## 1. Purpose

This document records the existing CI foundation and the minimal approach to continuous integration for the repository.

## 2. Existing repository baseline

The repository already includes:

- `.github/workflows/ci.yml`
- Node.js 22 setup
- pnpm 9.15.9 setup
- Python 3.12 and 3.14 matrix checks
- PostgreSQL service for tests
- uv sync and validation steps

This is already a practical CI starting point for a monorepo of this size.

## 3. Existing workflow behaviour

The current CI workflow runs checks on pushes to `main` and on pull requests. It includes:

- `pnpm install --frozen-lockfile`
- `uv sync --all-packages --all-groups --locked`
- migration check for the API
- formatting checks
- web linting and type checking
- web tests and build
- Python linting and tests

This is appropriate for the current repository and should remain the baseline rather than being replaced by a more complicated pipeline.

## 4. What is appropriate to add

A minimal CI foundation is reasonable for the current repo. It should include:

- formatting validation,
- linting,
- type checking,
- Python tests,
- web tests,
- build validation,
- database migration check where relevant.

## 5. What should not be added yet

Do not add:

- deployment automation,
- production environment promotion pipelines,
- cloud infrastructure provisioning,
- external secret-dependent workflows without explicit approval,
- unnecessary multi-stage build complexity.

## 6. Recommendation

Keep the current CI workflow as the baseline and expand only when the repo genuinely needs additional validation. The existing file is already aligned with the project’s stack and architecture and should not be replaced by a larger system before the team has matured its delivery patterns.

## 7. Summary

The repository already has a reasonable minimal CI foundation. The safe path is to retain and refine it rather than over-engineer deployment automation before implementation begins.
