# CI/CD and release management

## 1. Purpose

This document aligns the repository’s delivery process with its existing CI foundation while keeping the process minimal and reviewable.

## 2. Recommended release process

1. Developer creates a feature branch.
2. Code is reviewed before merge.
3. Automated checks run on the branch or pull request.
4. Formatting, linting, and tests are executed.
5. Relevant security validation is performed.
6. Pull request is approved.
7. Merge into the main branch occurs only after required checks pass.
8. Staging deployment is performed when approved.
9. Smoke and acceptance tests are completed.
10. Production release requires explicit approval and verification.

## 3. Required checks

The repository already has a sensible base set of checks in the CI workflow. Those should continue to include:

- formatting,
- linting,
- type checking,
- web and Python tests,
- database migration validation where relevant,
- dependency health checks,
- secrets scanning where the repo or deployment process is configured for it.

## 4. Release controls

- keep deployments small and reviewable,
- separate local, test, staging, and production roles,
- require explicit approval before production update,
- preserve rollback capability,
- verify production health after deployment.

## 5. Important limitation

This repository does not currently claim to have an operational production deployment pipeline. The enforcement model is therefore a documented recommendation, not a confirmed real deployment implementation.
