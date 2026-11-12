# Test environment strategy

## 1. Purpose

This document defines how ZAR HORIZON AI @WORK should organise test environments without prematurely committing to expensive production-grade infrastructure.

## 2. Environment categories

### Local development

Purpose:
- developer iteration,
- local validation,
- rapid feedback,
- local database and service checks.

Configuration:
- local PostgreSQL via Docker Compose,
- local web and API services,
- example environment files,
- repo-based validation commands.

### Automated test environment

Purpose:
- CI and PR validation,
- regression protection,
- automated quality checks.

Configuration:
- isolated test runners,
- service-backed PostgreSQL,
- project-level validation commands,
- branch-based enforcement.

### Staging environment

Purpose:
- release validation,
- end-to-end scenario testing,
- release readiness checks,
- security and permission validation against a realistic but non-production environment.

Configuration:
- protected environment,
- non-production data only,
- limited access,
- controlled promotion workflow.

### Production environment

Purpose:
- live customer or customer-facing operations.

Configuration:
- production-grade controls,
- strict access restrictions,
- secret management,
- backup and monitoring,
- change approval controls.

This stage does not decide the final production hosting provider or residency model.

## 3. Environment principles

- Local and test environments must remain isolated from production.
- Production data must never be used in development or staging without explicit approval.
- Secrets must remain outside the repository and outside logs.
- Test fixtures should be representative but controlled.
- Promotion should require successful validation and explicit approval.

## 4. Verification before promotion

Before release to a more advanced environment, the project should verify:

- code builds successfully,
- lint and type checks pass,
- unit and integration tests pass,
- migration safety is accepted,
- security checks have been performed,
- permission and approval controls are still correct.

## 5. Founder decisions still required

The repository should not commit to a final production deployment model yet. The founder or technical owner must still choose the provider, residency, backup policy, and operational approval model.
