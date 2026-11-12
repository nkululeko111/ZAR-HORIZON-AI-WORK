# Repository security and hygiene

## 1. Purpose

This document defines the baseline security and hygiene expectations for the repository. The goal is to reduce accidental credential leaks and keep the development environment reproducible and safe.

## 2. Current hygiene baseline

The repository already contains sensible defaults:

- `.gitignore` ignores `.env` and local database files
- `.gitignore` ignores build output and Python caches
- `.env.example` is tracked for safe local setup
- Docker Compose uses environment-based secrets rather than hard-coded production values

This is a strong starting point and should be retained.

## 3. Security rules

- never commit real credentials or secrets,
- store local secrets only in untracked `.env` files,
- keep frontend variables free of backend-only secrets,
- avoid logging credentials, tokens, or connection strings,
- separate local development variables from deployment values,
- do not place production secrets in example files.

## 4. Git hygiene

- keep commits focused and reviewable,
- avoid rewriting history without approval,
- review sensitive files before merging,
- ensure no generated files or caches are committed.

## 5. Dependency hygiene

- keep lockfiles current and tracked,
- do not add packages without review,
- prefer the repository’s current package managers and setups,
- validate dependency changes before merge.

## 6. GitHub Actions security

The repository already has a workflow file but does not define production deployment or privileged permissions. That is appropriate for a project at this stage. Avoid adding external secret dependencies unless they are needed and approved.

## 7. Local generated files to protect

The repo should ignore or actively exclude:

- `.env` and local env files
- `.venv` directories
- database data volumes
- build outputs
- pytest cache
- local logs
- editor metadata

## 8. Summary

The repository already follows a sensible baseline for security hygiene. The key practice is to keep secrets local, maintain small reviewable change sets, and avoid introducing new infrastructure or secrets before real product needs justify them.
