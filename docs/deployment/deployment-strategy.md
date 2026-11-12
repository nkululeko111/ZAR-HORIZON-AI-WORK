# Deployment strategy

## 1. Purpose

This document defines the deployment strategy for ZAR HORIZON AI @WORK at a governance level. It does not claim a production deployment is already configured or approved.

## 2. Environment model

The recommended environment model is:

- local development,
- automated test environment,
- staging environment,
- production environment.

This is a practical progression that matches a small but growing technology company without requiring premature infrastructure complexity.

## 3. Environment goals

### Local development

- rapid iteration,
- local database and service validation,
- minimal setup cost,
- alignment with the repo’s existing Docker and Compose setup.

### Automated test environment

- prove code quality and regression safety,
- validate infrastructure assumptions,
- run CI and branch-level checks.

### Staging environment

- realistic user workflow verification,
- release validation,
- security and approval checks,
- release readiness assessment.

### Production environment

- secure customer-facing deployment,
- strict controls,
- monitored and recoverable service delivery.

## 4. Deployment decision principles

- do not select a final hosting provider without founder approval,
- do not assume premium cloud infrastructure is required at this stage,
- keep deployment architecture simple and reviewable,
- separate development and production responsibilities,
- keep secrets out of code and deployment manifests,
- use change controls during promotion.

## 5. Recommended early-stage approach

A low-complexity early-stage deployment strategy is preferable:

- container-based deployment for application services,
- managed PostgreSQL or equivalent service in a controlled environment,
- clear promotion path from local/test to staging,
- explicit approval gate before production deployment,
- simple rollback procedure.

This is a practical starting point while allowing the team to grow without prematurely adopting a complex architecture.
