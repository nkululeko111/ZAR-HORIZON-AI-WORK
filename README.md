# ZAR HORIZON AI @WORK

ZAR HORIZON AI @WORK is the technology division of ZAR HORIZON (Pty) Ltd, building purpose-specific
AI digital employees. This repository establishes the shared platform and independent product boundaries. The first
Business Partner workflow supports local business profiles, classified CSV imports, deterministic
financial summaries, evidence-linked insights and internal action tracking. It does not execute
external business actions or implement Hacker testing capabilities, payments, or billing.

## Products

- **AI Business Partner** — intended to help entrepreneurs research, plan, run, and grow a business.
- **AI Hacker** — intended to support security teams with authorised security assessments. No
  security tools, targets, or test execution are enabled in this scaffold.

The two products have independent service and configuration boundaries. Read the
[architecture overview](docs/architecture/overview.md) for the separation and tenancy design.

## Technology

- Web: Next.js, React, TypeScript, Tailwind CSS.
- API: Python, FastAPI, Pydantic Settings, SQLAlchemy, Alembic.
- Database: PostgreSQL.
- Workspace tools: pnpm and uv.
- Local services: Docker Compose.

## Repository structure

```text
apps/
  api/                    FastAPI application and Alembic migrations
  web/                    Next.js landing page and Business Partner workspace
agents/
  business-partner/       Isolated Business Partner service scaffold
  hacker/                 Isolated Hacker service scaffold
docs/architecture/        Architecture decisions and boundaries
tests/                    API and agent-boundary tests
packages/                 Reserved for shared JavaScript packages
.github/workflows/        CI checks
```

## Prerequisites

- Node.js 22 and pnpm 9.15.9 (Corepack is included with Node.js).
- Python 3.12 and uv.
- Docker with Docker Compose v2 (for the full local stack).

Python 3.12 remains the default development baseline. The workspace metadata now permits Python
3.14 for compatibility testing, but that target is still provisional until the upstream runtime and
framework dependency set is fully validated. Create the local Python environment with uv; the
`.python-version` file selects the intended default version for local development.

## Development documentation

The repository includes a development foundation package in [docs/development](docs/development/), covering repository strategy, Git workflow, environment configuration, Docker usage, onboarding, CI, and security hygiene.

## Local setup

1. Install the JavaScript workspace:

   ```powershell
   corepack enable
   pnpm install
   ```

2. Install Python 3.12 if it is not already available, then install uv and project packages:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   uv sync --all-packages --all-groups
   ```

3. Configure local environment:

   ```powershell
   Copy-Item .env.example .env
   ```

   Replace the example PostgreSQL password in `.env` with a local-only value before starting
   Compose. `.env` is ignored by Git.

## Run the applications

Start the web application:

```powershell
pnpm dev:web
```

Start PostgreSQL and the API using Compose (the API applies database migrations on startup):

```powershell
docker compose up --build db api
```

Alternatively, run the API locally after PostgreSQL is available and `.env` is configured:

```powershell
uv run --package zar-horizon-api alembic -c apps/api/alembic.ini upgrade head
uv run --package zar-horizon-api uvicorn --app-dir apps/api/src zar_horizon_api.main:app --reload
```

The web app is at <http://localhost:3000>. The API health check is at
<http://localhost:8000/health>, version information is at
<http://localhost:8000/api/v1/version>, and interactive API documentation is at
<http://localhost:8000/docs>.

The Business Partner workspace is at <http://localhost:3000/business-partner>. It is a
development-only, single local workspace without authentication. Use synthetic or non-sensitive
data only. Its AI layer uses a configurable OpenAI-compatible endpoint; configure
`BUSINESS_PARTNER_AI_CHAT_COMPLETIONS_URL` and `BUSINESS_PARTNER_AI_MODEL`. A key is required for
remote endpoints, but not for local HTTP inference endpoints. Model name, version, source, licence
and licence category are configurable and recorded with analysis when supplied. Licence categories
distinguish `open_source`, `open_weights`, `restricted` and `unknown`; confirm model-specific
commercial terms independently. The model strategy is open-source/open-weight-first and
provider-independent: evaluate each model's actual capabilities, licence and privacy requirements
instead of selecting by developer size or benchmark claims. AI Hacker will retain its own model
selection and controlled security-task evaluation configuration; this sprint does not select or
evaluate a Hacker model.

Run the complete local stack with `docker compose up --build`. Stop it with
`docker compose down`; add `-v` only when intentionally deleting the local PostgreSQL data volume.

## Quality checks

```powershell
pnpm format:check
pnpm lint:web
pnpm typecheck:web
pnpm test:web
pnpm lint:python
pnpm format:python:check
pnpm test:python
pnpm build:web
```

Python tests expect the uv workspace environment. PostgreSQL migrations can be checked against the
Compose database using:

```powershell
uv run --package zar-horizon-api alembic -c apps/api/alembic.ini upgrade head
```

## Configuration and security

Settings are environment-based; see [.env.example](.env.example). Never place real secrets in
tracked files. Tenant-owned workspace and agent-session records include organisation identifiers,
with a composite database constraint preventing a session from pairing a workspace with the wrong
organisation. Authentication and request-level tenant authorization are not implemented yet and
must be in place before exposing tenant data to users.

Agent tools are not registered and both orchestration entry points explicitly remain unimplemented.
The Hacker scaffold has no target configuration or security-testing capability.
