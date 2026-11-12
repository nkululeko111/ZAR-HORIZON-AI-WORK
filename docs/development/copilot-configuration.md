# GitHub Copilot configuration

## Overview

GitHub Copilot is configured at multiple layers in this repository so that the assistant behaves consistently with the approved architecture and product boundaries.

## Instruction layers

### 1. Root repository instructions

The repository-level file `AGENTS.md` is the primary source of governance. It describes:

- the approved documentation set,
- the architectural and security boundary rules,
- product separation rules,
- Git safety expectations,
- testing and verification requirements,
- scope restrictions.

### 2. Repository-level Copilot instructions

The file `.github/copilot-instructions.md` gives Copilot the repo-specific context and expected workflow. It explains the monorepo structure, required review cycle, prohibited actions, and validation expectations.

### 3. Path-specific Copilot instructions

The `.github/instructions/` directory contains targeted guidance for:

- frontend work,
- backend work,
- database and tenant separation,
- agent boundaries and approval logic,
- testing and QA,
- infrastructure and environment configuration.

These files are intentionally concise and should not duplicate the root instructions in full.

## Conflict resolution

The precedence is:

1. explicit user instructions,
2. `AGENTS.md`,
3. `.github/copilot-instructions.md`,
4. path-specific `.github/instructions/*`,
5. the repository’s design documents.

When multiple sources conflict, the assistant should reconcile toward the approved design baseline and ask for clarification if the conflict is material.

## Maintenance

Update these files when the repo architecture, supported stack, standards, or product boundaries change. Keep the guidance aligned with the documentation in `docs/` and the actual repo structure.
