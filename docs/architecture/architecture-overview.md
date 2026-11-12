# Architecture overview

## Purpose

This document defines the proposed shared technical architecture for ZAR HORIZON AI @WORK. It follows the approved product definition, MVP boundaries, and execution-safety requirements documented in the product, market, use-case, and MVP packages.

This architecture is intentionally documentation-only. It does not implement code, database schemas, API endpoints, or infrastructure. It defines the target control model and the design direction for the platform and the two specialist product systems.

## Existing repository alignment

The repository already reflects several parts of the preferred technology direction:

- Frontend: Next.js, React, TypeScript, and Tailwind CSS are already used in the web application scaffold.
- Backend: Python and FastAPI are already used in the API application scaffold.
- Database: PostgreSQL is already selected and configured through Docker Compose and Alembic.
- Package management: pnpm workspaces and uv workspace configuration are present.
- Development environment: Docker Compose is already used for local infrastructure.
- CI/CD: GitHub Actions is already configured.

The main gaps relative to the desired operating architecture are not technology stack mismatches; they are missing control-plane capabilities and product isolation controls:

- no multi-tenant enforcement beyond scaffold-level design notes,
- no identity and access model with real role enforcement,
- no product-specific tool registry with permission checks,
- no approval engine enforcing backend checks,
- no isolated execution boundary for AI Hacker tooling,
- no evidence and audit service with immutable execution records,
- no provider abstraction layer for AI models and tools,
- no implemented orchestration engine or background execution workers.

In other words, the repository is an architectural foundation, not yet a production platform. The design below respects that status and keeps scope aligned with the existing monorepo structure.

## Recommended architecture approach

The recommended architecture is a shared platform with two independent specialist execution systems under a common control plane.

This is a modular monolith architecture at the platform level, with explicit service boundaries for:

1. shared platform services,
2. AI Business Partner execution domain,
3. AI Hacker execution domain,
4. shared approval, evidence, and audit services,
5. isolated execution workers for security operations.

It is not a microservice-first architecture and does not call for Kubernetes or distributed infrastructure in the first release. The small initial engineering team, mixed product complexity, and need for strong security boundaries favour a modular monolith pattern with independent deployment boundaries for the specialist products.

## Architectural principles

1. Shared infrastructure, separate authority.
2. Product separation by permission, not by folder structure alone.
3. Backend enforcement for all approvals and tool access.
4. Deterministic calculations for financial logic, with LLM reasoning as interpretation only.
5. Evidence-backed execution and audit as first-class capabilities.
6. Explicit authorisation and scope control for AI Hacker operations.
7. Tenant-aware data isolation at all layers.
8. Realistic implementation readiness for a small team.

## Functional decomposition

The platform contains five key areas:

- Shared identity, tenancy, and workspace management
- Shared approvals, policies, and audit record services
- AI provider abstraction and orchestration layer
- Product-specific execution domains
- Isolated security execution environment

The Business Partner and Hacker each have operational logic for task interpretation, context gathering, tool selection, execution, verification, evidence capture, and reporting, but they do not share the same permission model or tool registry.

## Separation of product authority

The two products are intentionally independent:

- Business Partner: business context, commercial workflows, operational execution, business data processing, and approved external actions within a business permission profile.
- AI Hacker: authorised security investigations, asset assessment, vulnerability validation, evidence gathering, remediation guidance, and retesting within approved scope.

Neither product inherits the other product's execution permissions. The platform enforces this at the authorisation layer, not by UI hiding alone.

## Architectural decision framing

The proposal uses a common execution lifecycle across both products:

1. Receive request
2. Identify product and tenant context
3. Interpret task and constraints
4. Retrieve relevant context
5. Create execution plan
6. Check permission, policy, and scope
7. Identify required tools
8. Request approval when required
9. Execute permitted actions
10. Capture results and evidence
11. Verify outcome
12. Handle partial failure or error
13. Report result
14. Record execution history

## Required documentation set

This architecture package includes:

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

## Architectural summary

The recommended architecture keeps the platform reusable and secure while leaving the AI Business Partner and AI Hacker as distinct specialist systems with separate execution authorities. It supports the MVP flows already defined for both products and keeps the platform realistic for a small team without premature distributed infrastructure.
