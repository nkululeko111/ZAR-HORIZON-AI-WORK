# Repository strategy

## 1. Purpose

This document records the repository strategy for ZAR HORIZON AI @WORK as a development foundation for the shared platform and independent specialist products.

## 2. Current repository assessment

The repository already has the structure expected for a cross-product monorepo:

- `apps/web` for the Next.js web application
- `apps/api` for the FastAPI application
- `agents/business-partner` for the Business Partner service boundary
- `agents/hacker` for the AI Hacker service boundary
- `docs/` for product, architecture, database, API and UX design
- `tests/` for validation coverage
- `.github/workflows` for CI foundation

This is a good fit for a monorepo at this stage because the project is still defining shared platform services and product separation without large independent deployment needs. The repository is already structurally aligned to a shared platform + product boundary model.

## 3. Why the monorepo remains the preferred approach

The monorepo remains the preferred approach because:

- the platform is shared by both products,
- the repository already contains cross-cutting configuration,
- the teams are still small and the project is not yet at a scale requiring independent repo splits,
- shared infrastructure such as CI, workspace tooling, and env configuration are easier to standardise in one place,
- product separation can still be preserved through directory boundaries, service boundaries, and runtime policy boundaries.

## 4. Separation model

The products remain logically separate even though they share a single repository.

### Shared platform layer

The shared platform owns:

- identity and tenant context,
- organisation and workspace metadata,
- common app shell and platform services,
- shared tooling, dependency management, and CI,
- centralised documentation and architecture records.

### Product layer

The two specialist products remain separate by directory and service boundary:

- `apps/web` for the common web shell and product entry point
- `apps/api` for the shared platform API
- `agents/business-partner` for the Business Partner execution boundary
- `agents/hacker` for the AI Hacker execution boundary

The architecture documentation already distinguishes product authority and service separation. The repo structure should continue to reflect that, without implying cross-product ownership or shared execution rights.

## 5. Review and change governance

As the codebase grows, shared changes should be reviewed by:

- the platform owner for config and shared tooling changes,
- the product owner for product-specific changes,
- the repo maintainers for cross-cutting changes affecting multiple products.

Pull requests should remain small and should clearly identify which layer is affected.

## 6. Future deployment support without premature split

The monorepo can support future independent deployment by keeping each product boundary isolated while preserving a common codebase today. The project should avoid premature split if the services are still tightly coupled at the platform layer.

Recommended approach:

- retain monorepo for the initial platform and MVP stages,
- isolate product service boundaries in subdirectories and package boundaries,
- document deployment boundaries early,
- split into independent repositories only if product teams, deployment pipelines, or compliance needs genuinely justify it.

## 7. Conclusion

The repository strategy is to keep the monorepo for now, while making the shared platform and product boundaries explicit in structure, tooling, and review expectations. This is the simplest and safest way to support the current phase without imposing unnecessary complexity.
