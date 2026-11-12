# AI-assisted development decision register

## Purpose

This register records the decisions made to configure AI assistants for the repository. It documents the baseline build and governance decisions for the current phase.

## Decision log

### AI-001: repository-level governance file created

Decision:
- Create a root `AGENTS.md` to define the repository-wide rules.

Reason:
- the project requires a shared source of truth for design alignment, scope restriction, and security expectations.

### AI-002: GitHub Copilot repository instructions created

Decision:
- Add `.github/copilot-instructions.md` and focused `.github/instructions/*.instructions.md` files.

Reason:
- the repo needs both global and path-specific guardrails.

### AI-003: Cursor rules created

Decision:
- Add `.cursor/rules/*.mdc` files with global, frontend, backend, database, product, and testing-specific guidance.

Reason:
- the repo requires tool-specific instruction coverage for both GitHub Copilot and Cursor.

### AI-004: no runtime feature implementation introduced

Decision:
- Keep the work in engineering-governance and documentation scope only.

Reason:
- the task explicitly forbids feature implementation and infrastructure changes beyond instruction configuration.

## Outstanding decisions

- whether branch protection or more formal repo governance needs founder approval later,
- whether additional instruction layers are required as the repo evolves,
- whether to expand path-specific instructions once product implementation begins.
