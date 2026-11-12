# Deployment architecture

## 1. Recommended initial topology

The recommended initial topology is a small, pragmatic platform that matches the actual repository state and the product maturity level. It is a shared platform foundation with isolated product execution boundaries.

Core components:

- Next.js frontend application
- FastAPI API application
- PostgreSQL database
- background workers for async tasks and job processing
- object or document storage for files and evidence
- AI provider connectors and model adapters
- isolated execution worker for AI Hacker operations
- logging and monitoring services

## 2. Environment model

### Local development

The existing Docker Compose stack already reflects a reasonable local development setup:

- PostgreSQL,
- API service,
- web application.

This is enough for local development of the platform and product scaffolds. The Hacker execution worker should not be mixed into the main web process and should remain separately managed until the execution boundary is designed and approved.

### Testing and staging

Testing and staging should separate:

- the shared platform,
- the Business Partner application configuration,
- the AI Hacker execution environment,
- the test dataset and evidence store,
- the monitoring and log collection stack.

This environment should support review of workflow behaviour and policy enforcement without exposing production data.

### Production

Production should contain:

- web frontend,
- API application,
- database,
- background job workers,
- object/document storage,
- secret management and key handling,
- telemetry,
- isolated Hacker worker environment,
- evidence storage and audit retention infrastructure.

## 3. Components that can initially be deployed together

The following can be deployed together in a single initial platform footprint:

- web application,
- API service,
- PostgreSQL,
- basic queue or background worker runtime,
- shared platform authentication and tenant services,
- shared audit and evidence storage,
- common model provider adapter layer.

This follows the existing monorepo structure and keeps the initial release lean.

## 4. Components that should remain isolated

The following should remain isolated from the main application process:

- AI Hacker execution worker,
- approved security tools and sandboxed command execution,
- credential-bearing or privileged security tasks,
- any high-risk validation process,
- any operation that touches production security workflows without explicit approval.

This is both a security and operational requirement.

## 5. Initial release deployment posture

The first release should avoid heavy distributed infrastructure. A modular monolith with separate execution boundaries is enough for the MVP and for the founder-approved risk posture.

The right deployment posture is:

- shared platform service as the main runtime unit,
- distinct product execution domains in the same codebase or clearly partitioned modules,
- separate isolated Hacker worker boundary when security tasks become active,
- no Kubernetes requirement in the first release.

## 6. Infrastructure choices to avoid in the first release

The architecture intentionally does not introduce:

- microservices-first decomposition,
- Kubernetes orchestration,
- unnecessary distributed infrastructure,
- paid vendor-specific infrastructure without approval,
- broad multi-region complexity,
- general-purpose shared execution model for all products.

This keeps the architecture realistic, safe, and aligned with a small initial team.
