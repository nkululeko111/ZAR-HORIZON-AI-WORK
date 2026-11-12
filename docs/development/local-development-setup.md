# Local development setup

## 1. Purpose

This document records the local development setup for the ZAR HORIZON AI @WORK monorepo based on the current repository configuration.

## 2. Required tools

### Required

- Git
- Node.js 22
- pnpm 9.15.9
- Python 3.12
- uv
- Docker and Docker Compose v2
- PostgreSQL client tools when needed

### Existing repository alignment

The repository already declares:

- Node.js 22 in the web Dockerfile and CI workflow
- pnpm 9.15.9 in the root package manifest
- Python 3.12 in `pyproject.toml` and `apps/api/pyproject.toml`
- Docker Compose with PostgreSQL and service containers

## 3. Installation steps

### Install Node.js and pnpm

```powershell
corepack enable
pnpm --version
```

If pnpm is not installed yet, Corepack will manage the version from the workspace configuration.

### Install Python and uv

On Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
```

## 4. Workspace setup

From the repo root:

```powershell
pnpm install
uv sync --all-packages --all-groups
```

This matches the current root workspace configuration and the Python workspace packages declared in `pyproject.toml`.

## 5. Environment configuration

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

For development-only defaults, also use:

```powershell
Copy-Item .env.development.example .env.development
```

Then replace placeholder credentials and local-only values before starting services.

## 6. Database startup

From the repo root:

```powershell
docker compose up -d db
```

The Compose configuration already defines a PostgreSQL 17 service with a named volume and health check.

## 7. Application startup

### Start the web app

```powershell
pnpm dev:web
```

### Start the API locally

```powershell
uv run --package zar-horizon-api alembic -c apps/api/alembic.ini upgrade head
uv run --package zar-horizon-api uvicorn --app-dir apps/api/src zar_horizon_api.main:app --reload
```

### Start both services together with Docker Compose

```powershell
docker compose up --build
```

## 8. Testing and validation commands

### Web checks

```powershell
pnpm format:check
pnpm lint:web
pnpm typecheck:web
pnpm test:web
pnpm build:web
```

### Python checks

```powershell
pnpm lint:python
pnpm format:python:check
pnpm test:python
```

### Database migrations

```powershell
uv run --package zar-horizon-api alembic -c apps/api/alembic.ini upgrade head
```

## 9. Common troubleshooting

### Node or pnpm issues

- reinstall dependencies with `pnpm install`
- confirm Node version 22 is active
- confirm Corepack is enabled

### Python or uv issues

- confirm Python 3.12 is active
- re-run `uv sync --all-packages --all-groups`
- check `.python-version` if a specific local interpreter is expected

### PostgreSQL connectivity

- confirm the Compose service is healthy
- verify `DATABASE_URL` and `.env` values
- check container logs using `docker compose logs db`

### Docker issues

- re-run `docker compose down` and `docker compose up --build`
- ensure the Docker daemon is running
- verify local ports 3000 and 8000 are not already in use

## 10. Summary

The repository already includes a credible local development setup: pnpm for web, uv for Python tooling, Docker Compose for PostgreSQL and app services. The main requirement is to keep config aligned with the existing repo and avoid introducing extra tooling beyond the current architecture.
