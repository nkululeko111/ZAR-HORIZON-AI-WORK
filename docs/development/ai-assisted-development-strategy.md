# AI-assisted development strategy

## Purpose

This repository is governed by a documentation-first, architecture-first model. AI-assisted development is allowed only within the rules established by the approved product and architecture documents. The goal is to improve implementation quality while preventing accidental drift from the project’s security, product, and policy boundaries.

## Source of truth

The repository’s approved design set remains authoritative:

- `docs/products/`
- `docs/market-research/`
- `docs/customer-validation/`
- `docs/use-cases/`
- `docs/competitive-research/`
- `docs/mvp/`
- `docs/architecture/`
- `docs/database/`
- `docs/api/`
- `docs/ux/`
- `docs/development/`
- `README.md`

When a request touches implementation, the assistant must read the relevant documentation before proposing or making a change.

## Working model for assistants

The assistant should follow this process:

1. Understand the request.
2. Identify the affected subsystem and the relevant documentation.
3. Check for conflicts with the product or architecture baseline.
4. Confirm whether the work is inside scope.
5. Propose a narrow plan only when the change is meaningful or security-sensitive.
6. Implement only within the authorised scope.
7. Run the smallest relevant validation that is available.
8. Review the resulting diff.
9. Report files changed, checks performed, assumptions, and remaining risks.

## Guardrails

- No product features without design approval.
- No new database models or API contracts without a matching design update.
- No broad refactoring, dependency sprawl, or infrastructure expansion without explicit approval.
- No secret exposure, credential tracking, or unsafe operational shortcuts.
- No claim of success without verification.

## Conflict handling

If the repository instructions, architecture docs, or implementation request conflict, the assistant must stop and ask for clarification rather than choosing an arbitrary approach. This prevents accidental policy drift or security weakening.

## Maintenance

The instruction files in this repository should be reviewed whenever the architecture, security boundaries, stack, or working conventions materially change. Documentation and configuration must remain aligned.
