# AI-assisted testing and review

## Purpose

This repository requires tools to validate only what is actually available and understandable. The instruction set does not permit guessing or silent assumptions about tests, builds, or security controls.

## Frontend checks

For changes in `apps/web`, the expected checks are:

- formatting,
- linting,
- TypeScript type checking,
- relevant tests,
- build verification when the repo supports it.

These are defined in the project’s local workflow and CI baseline, which are recorded in `README.md` and `.github/workflows/ci.yml`.

## Backend checks

For changes in `apps/api` and the Python workspace, the expected checks are:

- Python formatting,
- linting,
- type checking when configured,
- API-related and unit test runs where available,
- migration validation when database changes are relevant.

## Database and tenant-isolation checks

For any change that affects data models, migration assumptions, tenant logic, or workspace mapping, verify the relevant isolation logic and migration flow instead of assuming data boundaries are safe.

## Security and approval checks

For changes touching permissions, tool use, approvals, or security workflows, validate the enforcement controls and evidence flow. The assistant must not treat an approval model as safe because it looks complete on paper.

## Review standard

When a task is complete, the assistant should report:

- files changed,
- checks actually run,
- failures or blockers,
- assumptions,
- outstanding risk or follow-up requirements.

If a validation step cannot run, that limitation must be stated clearly.
