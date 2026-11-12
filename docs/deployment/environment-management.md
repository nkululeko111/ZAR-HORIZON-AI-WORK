# Environment management

## 1. Purpose

This document defines how environments should be managed for the repository. It does not assume a final deployment platform or hosting provider has been selected.

## 2. Environment responsibilities

### Local development

- used by engineers and reviewers,
- should reflect the repo’s documented stack,
- should use example env files and local secrets only,
- should be reproducible and lightweight.

### Automated test environment

- used for CI and validation,
- should be controlled and isolated,
- should reject secrets, production data, or customer content,
- should be repeatable and versioned.

### Staging

- used for smoke testing and release validation,
- should use test or synthetic data only,
- should be subject to review before release.

### Production

- mission-critical environment,
- must be tightly controlled,
- must use managed secrets and monitored access,
- must have explicit approval and rollback capability.

## 3. Configuration principles

- separate local, test, staging, and production values,
- do not reuse production keys in development,
- keep config externalised,
- treat environment files as templates, not credential stores,
- document ownership of each configuration variable.

## 4. Founder decisions required

- cloud provider and region,
- database hosting model,
- secret-management provider,
- production access model,
- production-level monitoring and alerting budget.

Until those are decided, the repository should maintain documented recommendations instead of claiming a production environment definition is final.
