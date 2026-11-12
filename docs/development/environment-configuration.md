# Environment configuration

## 1. Purpose

This document establishes the repository’s environment-variable conventions and explains how local and deployment configuration should be handled without exposing secrets.

## 2. Existing baseline

The repository already contains:

- `.env.example` at the repository root
- existing Compose configuration using environment variables
- root `pyproject.toml` and app-level Python config expecting environment-based settings

The current repository already uses the correct general pattern: keep development environment values in local `.env` files and ignore them from Git.

## 3. Safe configuration principles

The project should follow these rules:

- keep all secrets out of version control,
- use placeholders only in tracked files,
- never commit a real password, API key, or token,
- keep local development settings separate from production values,
- do not expose backend-only secrets to the frontend,
- document which service owns each variable.

## 4. Tracked example files

### `.env.example`

This file is already present and is the default repo-safe template. It should remain the canonical tracked example for local setup.

### `.env.development.example`

This file is used as an explicit development-only template and is safe to track. It should contain local development defaults for the current workspace.

## 5. Environment variable categories

### Shared platform and app settings

- `APP_ENV`
- `APP_VERSION`
- `LOG_LEVEL`

### Database settings

- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `DATABASE_URL`

These values belong to the API and database layer. They should not be placed into frontend code.

### Frontend settings

- `NEXT_PUBLIC_API_URL`

This variable is safe for frontend use only when it points to a public or local development API endpoint. It must not be used for privileged data or secret values.

## 6. Local developer usage

Developers should copy tracked example files into local untracked files:

```powershell
Copy-Item .env.example .env
Copy-Item .env.development.example .env.development
```

Then update values as required for the local machine.

## 7. Production and deployment expectations

Production and deployment environments should use secure secret injection rather than repository files. The repository should never be the source of truth for live credentials.

Recommended model:

- local: `.env` or docker env variables
- CI: GitHub Actions secrets or environment variables
- deployment: provider secret store or secret manager

## 8. Security notes

- do not put raw credentials in `README.md`, docs, or tracked example files,
- do not use placeholders that look like real secret values too closely,
- do not expose backend connection strings to browser code,
- do not add secrets to log output or error messages.

## 9. Summary

The repo already follows the correct basic pattern: `.env` files remain local-only, and example files are tracked for guidance. The main improvement is to provide an explicit development template and to document ownership and safe usage clearly.
