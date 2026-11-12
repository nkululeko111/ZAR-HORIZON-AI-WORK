# Day 12 development environment decisions

## 1. Summary

This document captures the development-environment decisions made during the Day 12 repository foundation review. The focus is to keep the repository practical, reproducible, and aligned with the architecture and product boundaries already documented in the earlier days.

## 2. Retained repository structure

- monorepo retained for now,
- shared platform and product boundaries remain visible in directory structure,
- development tooling remains centralised,
- Docker and local tooling remain minimal and practical.

## 3. Retained tooling and configuration

- Node.js 22 and pnpm 9.15.9
- Python 3.12 with uv
- PostgreSQL 17 via Docker Compose
- existing CI workflow for linting, tests, and migration checks
- existing `.env.example` and local `.env` conventions

## 4. New documentation and config created

- repository strategy
- Git workflow standards
- local development setup
- environment configuration guidance
- Docker and local services guidance
- developer onboarding steps
- development standards
- CI foundation guidance
- repo security and hygiene guidance
- development environment decision register

## 5. New config file created

- `.env.development.example`

## 6. Existing files modified

- `.gitignore` updated to track `.env.development.example` while continuing to ignore local env files

## 7. Recommendations documented but not implemented

- final branch protection configuration on GitHub
- any future repository split if product deployment needs require it
- expanded deployment or infrastructure automation beyond the current stage

## 8. Final confirmation

This Day 12 work is a documentation and repository-setup foundation task only. No runtime application code, product features, auth flows, API endpoints, database models, or product functionality were added or modified.
