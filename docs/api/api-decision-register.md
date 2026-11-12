# API decision register

## 1. Purpose

This register captures the key architecture and API decisions for the Day 10 documentation set. It is intended as a working record of design choices and open decisions that still need founder review.

## 2. Decision log

### ADR-API-001: REST with `/api/v1`

Decision:
- Use versioned REST endpoints under `/api/v1`.

Why:
- Clear separation of contract version from future evolution.
- Matches the platform direction and the repo’s architecture documentation.

Status:
- accepted.

### ADR-API-002: Tenant-aware API boundary

Decision:
- All requests must resolve tenant, workspace, and product context at the backend.

Why:
- Required to preserve strict isolation between organisations and products.

Status:
- accepted.

### ADR-API-003: Shared platform plus domain ownership

Decision:
- The platform owns shared identity, tenancy, execution, approval, integration, and audit foundation.
- Business Partner and AI Hacker own their domain-specific endpoints and tools.

Why:
- Maintains product separation and enables consistent cross-product controls.

Status:
- accepted.

### ADR-API-004: Approval is backend-enforced

Decision:
- Approval is tied to the exact action payload and validated by the backend.

Why:
- Prevents UI-only or prompt-only bypass.

Status:
- accepted.

### ADR-API-005: Financial logic must be deterministic

Decision:
- Financial calculations should use explicit calculation logic with audit references.

Why:
- Prevents opaque or unverifiable LLM arithmetic.

Status:
- accepted.

### ADR-API-006: AI Hacker is scope-limited

Decision:
- AI Hacker tools must be bound to approved assets, authorisations, and test windows.

Why:
- Required to preserve safety and legal boundaries.

Status:
- accepted.

### ADR-API-007: Long-running tasks are asynchronous

Decision:
- Long-running operations use asynchronous execution with status polling and notifications.

Why:
- Keeps web requests responsive and preserves execution traceability.

Status:
- accepted.

### ADR-API-008: Evidence is required for high-impact action

Decision:
- Approved actions, security investigations, and action verification require evidence and audit metadata.

Why:
- Supports trust, compliance, and accountability.

Status:
- accepted.

### ADR-API-009: Tool registry is deny-by-default

Decision:
- The registry denies access unless explicitly allowed and policy-checked.

Why:
- Prevents unsafe, accidental, or prompt-driven tool execution.

Status:
- accepted.

### ADR-API-010: OpenAPI and shared schemas are the long-term contract layer

Decision:
- The platform should eventually maintain OpenAPI and shared schema definitions for backend and frontend contract discipline.

Why:
- Keeps implementation aligned and reduces drift.

Status:
- accepted with implementation pending.

## 3. Open decisions or follow-up items

### Decision review required: security testing execution boundaries

The documentation defines the control boundary for intended security assessment tasks, but the final operational boundaries for specific techniques and testing classes still require founder or legal sign-off.

### Decision review required: external integrations and vendor choices

The API design allows integration points, but specific vendor onboarding and external credentials remain to be approved later.

### Decision review required: approval delegation model

The design assumes a structured approval model with exact action matching, but final approver roles, escalation paths, and approval delegation rules require a product policy decision.

### Decision review required: document and evidence retention policy

The repository documents retention principles at a high level, but a concrete retention schedule for business and security evidence still requires formal policy review.

## 4. Summary

The API and tool design is deliberately conservative, permissioned, and enforceable. It is consistent with the product separation and architecture decisions already captured in earlier days of the project documentation.
