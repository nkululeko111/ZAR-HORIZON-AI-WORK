# Development standards

## 1. Purpose

This document defines the baseline development expectations for the repository. These standards are intentionally pragmatic and aligned with the current technology stack and architecture.

## 2. Technology standards

### TypeScript and web standards

- use TypeScript across the frontend application,
- keep the frontend intentionally simple and stable,
- prefer small, maintainable components and clear imports,
- use linting and type checks before merging,
- avoid ad hoc client-side logic for business-critical or security-sensitive flows.

### Python standards

- use Python 3.12 as the development baseline,
- keep Python services explicit and boundary-aware,
- prefer clear module boundaries between shared platform and product-specific services,
- use structured validation and typed configuration where available.

## 3. Formatting and linting

The repository already defines:

- Prettier for JavaScript and TypeScript formatting
- Ruff for Python linting and formatting
- ESLint for the web app

Developers should run project checks before opening or merging a pull request.

## 4. Naming conventions

- use descriptive filenames and component names,
- use lowercase or kebab-case for file names where appropriate,
- maintain consistent naming across shared platform and domain services,
- avoid ambiguous names across product boundaries.

## 5. Error handling and logging

- surface clear validation errors,
- avoid leaking credentials, secrets, or stack traces to user-facing output,
- use structured logs and correlation IDs where applicable,
- distinguish operational errors from validation or permission errors.

## 6. Testing expectations

- write tests for validation and regression coverage in the relevant layer,
- prefer the smallest relevant validation command,
- run project checks before merging changes,
- avoid making product-feature claims that are not covered by tests or documentation.

## 7. Environment configuration expectations

- use local `.env` files only for local development,
- keep tracked example env files with placeholders,
- never commit real credentials,
- keep back-end configuration separate from frontend-exposed variables.

## 8. Dependency management

- use pnpm and uv as the repository’s package managers,
- do not add dependencies without a clear need,
- keep lockfiles up to date when dependency inputs change,
- prefer existing tooling and configuration over introducing new infrastructure.

## 9. Documentation expectations

- update documentation when architecture, tooling, or workflow changes,
- keep docs accurate and aligned with the repository structure,
- document product and platform boundaries where relevant.

## 10. Secure coding practices

- do not commit secrets or tokens,
- do not place privileged configuration in browser-visible files,
- follow least privilege and product boundary rules,
- validate permissions and approval logic in the backend, not only in the UI.

## 11. Summary

These standards are intentionally straightforward. The project should favor clarity, maintainability, and safety rather than unnecessary tooling complexity.
