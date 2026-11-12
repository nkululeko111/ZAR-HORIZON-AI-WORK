# Architecture overview

## Purpose

This document summarises the recommended architecture for ZAR HORIZON AI @WORK and points to the detailed design documents in this folder.

The architecture follows the approved product definition and MVP constraints already documented in the project: two specialist products share the same platform foundation but do not share authority, permissions, or tool registries.

## Recommended architecture approach

The recommended structure is a shared platform plus two independent specialist execution domains:

- AI Business Partner
- AI Hacker

This is a modular monolith at the platform level, with strict separation of product execution and permission boundaries. It is intentionally not a microservice-first pattern and does not rely on Kubernetes or distributed infrastructure in the first release.

## Existing repository alignment

The repository already contains the main preferred stack foundations:

- Next.js, React, TypeScript and Tailwind CSS in the web app,
- Python and FastAPI in the API application,
- PostgreSQL in the local Compose stack,
- pnpm workspaces and uv workspace configuration,
- Docker Compose for local services,
- GitHub Actions for CI.

The main gaps are not technology mismatch; they are missing product-control capabilities: tenant enforcement, approval engine, tool policy, isolated Hacker execution boundary, evidence services, and audit-backed execution history.

## Shared platform responsibilities

The shared platform handles:

- identity and access,
- organisation and workspace management,
- subscription and usage,
- AI provider abstraction,
- tool registry governance,
- approval and policy enforcement,
- evidence and audit capture,
- supporting storage and integration foundations.

These capabilities are shared, but they are not authority-sharing capabilities.

## Product separation

The Business Partner and AI Hacker remain independent domains with different permissions and tool sets.

- Business Partner focuses on commercial and operational business execution.
- AI Hacker focuses on authorised security assessment, vulnerability validation, evidence collection, and reporting.

Neither product inherits the other's authority. The platform must enforce separation by backend policy and execution environment.

## Execution pattern

Both products use the same conceptual operating model:

1. receive request,
2. determine product and tenant context,
3. retrieve relevant data,
4. create a plan,
5. validate permissions and policy,
6. identify tools,
7. request approval where required,
8. execute only permitted actions,
9. capture results and evidence,
10. verify the outcome,
11. report, and
12. record the execution history.

## Key design points

- LLM reasoning is not the security boundary.
- Business calculations must be deterministic and auditable.
- Approvals must be enforced in the backend.
- AI Hacker tool execution must be isolated from the main application process.
- Tenant isolation and evidence-backed execution are first-class requirements.
- The architecture remains realistic for a small initial team.

## Document set

- [architecture-overview.md](./architecture-overview.md)
- [shared-platform-architecture.md](./shared-platform-architecture.md)
- [business-partner-architecture.md](./business-partner-architecture.md)
- [ai-hacker-architecture.md](./ai-hacker-architecture.md)
- [agent-orchestration-and-execution.md](./agent-orchestration-and-execution.md)
- [data-flow-and-ownership.md](./data-flow-and-ownership.md)
- [integration-architecture.md](./integration-architecture.md)
- [security-architecture.md](./security-architecture.md)
- [reliability-and-observability.md](./reliability-and-observability.md)
- [deployment-architecture.md](./deployment-architecture.md)
- [architecture-diagrams.md](./architecture-diagrams.md)
- [architecture-decision-record.md](./architecture-decision-record.md)
- [day-08-architecture-decisions.md](./day-08-architecture-decisions.md)

## Architectural status

This is a documentation-only architecture proposal. It does not change application code, database schemas, API endpoints, package configuration, or deployment infrastructure.
