# Developer onboarding

## 1. Purpose

This document defines the basic onboarding flow for new developers joining ZAR HORIZON AI @WORK.

## 2. Onboarding steps

### 1. Clone the repository

```powershell
git clone <repository-url>
cd ZAR-HORIZON-AI-WORK
```

### 2. Install required tools

Install:

- Git
- Node.js 22
- pnpm 9.15.9
- Python 3.12
- uv
- Docker Compose v2

### 3. Configure environment variables

```powershell
Copy-Item .env.example .env
Copy-Item .env.development.example .env.development
```

Update local values, especially database credentials and local URLs.

### 4. Install workspace dependencies

```powershell
pnpm install
uv sync --all-packages --all-groups
```

### 5. Start local infrastructure

```powershell
docker compose up -d db
```

### 6. Run database migrations if needed

```powershell
uv run --package zar-horizon-api alembic -c apps/api/alembic.ini upgrade head
```

### 7. Start the application services

Web:

```powershell
pnpm dev:web
```

API:

```powershell
uv run --package zar-horizon-api uvicorn --app-dir apps/api/src zar_horizon_api.main:app --reload
```

Or run the full local stack with Docker:

```powershell
docker compose up --build
```

### 8. Run tests and validation

```powershell
pnpm lint:web
pnpm typecheck:web
pnpm test:web
pnpm lint:python
pnpm test:python
```

### 9. Run formatting checks

```powershell
pnpm format:check
pnpm format:python:check
```

### 10. Create a feature branch and submit a pull request

```powershell
git checkout -b feature/<short-name>
```

Before merging, ensure the branch is reviewed and validated according to the repository workflow.

## 3. Recommended first-day checklist

- confirm tool versions,
- install dependencies,
- confirm env files are created and local-only,
- start Postgres,
- run the app or Docker stack,
- run the smallest relevant validation command,
- create a feature branch before making changes.

## 4. Summary

The onboarding flow is intentionally simple and aligned with the existing repo. It uses the current pnpm + uv + Docker pattern already present in the codebase.
