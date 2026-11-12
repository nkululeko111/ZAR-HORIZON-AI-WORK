# Shared platform architecture

## 1. Purpose

The shared platform provides the enterprise and operational foundation for both specialist products. It delivers identity, tenancy, storage, policy, logging, integration management, and execution abstraction without granting cross-product authority.

The platform is foundational infrastructure; the specialist products remain independent execution domains with their own permission sets and tool registries.

## 2. Core platform responsibilities

### Identity and access

Purpose:
- authenticate users,
- manage organisations and workspaces,
- structure memberships and invitations,
- assign roles and permission scopes,
- maintain user sessions and refresh flows,
- control access to platform features.

Ownership:
- shared platform team/service.

Dependencies:
- PostgreSQL persistence,
- session and token service,
- policy evaluation service.

Security considerations:
- enforce MFA and secure session handling for privileged roles,
- keep workspace membership and tenant binding explicit,
- never allow a session to cross tenant boundaries,
- deny privilege escalation through product configuration alone.

### Multi-tenancy

Purpose:
- isolate organisation-level data and configuration,
- enforce workspace boundaries,
- prevent org-to-org leakage,
- allow tenant-aware access control and configuration.

Ownership:
- shared platform control plane.

Dependencies:
- tenant table and workspace table,
- row-level or service-level tenant enforcement,
- audit records keyed to organisation and workspace.

Security considerations:
- all major data read/write paths must carry tenant context,
- cross-tenant queries must be blocked by policy and by database constraints,
- product-specific data is not visible outside the tenant even if the user is authenticated.

### Subscription and usage

Purpose:
- manage subscriptions,
- define product entitlements,
- track usage and quotas,
- gate premium features based on plan,
- define billing boundary interfaces.

Ownership:
- shared platform domain with product-specific entitlement checks.

Dependencies:
- plan registry,
- usage event records,
- integration boundary for billing provider when approved.

Security considerations:
- entitlement decisions must be enforced server-side,
- usage metering should be immutable per event,
- product permissions should not depend on client-side plan flags.

### AI provider abstraction

Purpose:
- decouple business logic from a single model or vendor,
- manage provider configuration,
- track token and usage data,
- support retries and fallback behaviour,
- allow structured outputs and cost control.

Ownership:
- shared platform plus product adaptation layer.

Dependencies:
- LLM provider adapters,
- model registry,
- usage telemetry,
- retry and timeout policies.

Security considerations:
- never treat the model as a security boundary,
- separate model access configuration from business logic,
- redact secrets, track provider failures, and capture prompts and responses only when policy permits.

### Tool registry and execution

Purpose:
- register available tools,
- restrict tools to explicit product permissions,
- validate tool inputs,
- manage execution state,
- capture execution logs and results.

Ownership:
- shared control plane plus product-specific tool registrations.

Dependencies:
- product permission policies,
- execution engine,
- evidence service,
- approval engine.

Security considerations:
- tool availability is authorisation-based and not inferred from the frontend,
- each tool carries product and tenant restrictions,
- dangerous operations must be gated through policy and approval.

### Approval engine

Purpose:
- represent preconditions for sensitive actions,
- capture who approved what and when,
- track expiration and cancellation,
- enforce approvals before execution.

Ownership:
- shared platform policy and approval service.

Dependencies:
- policy definitions,
- execution engine,
- user identity and role model,
- evidence store.

Security considerations:
- approvals must be checked by the backend before execution;
- can be implemented as decision records, not just UI toggles;
- high-risk operations require human approval and explicit policy checks.

### Evidence and audit

Purpose:
- record user actions,
- store execution records,
- record approvals,
- store evidence supporting conclusions,
- support traceability and compliance review.

Ownership:
- shared platform evidence and audit domain.

Dependencies:
- execution engine,
- product services,
- document storage,
- event logging.

Security considerations:
- separate audit logs from execution records from evidence material,
- ensure evidence is tied to a specific agent action and tenant,
- protect sensitive evidence with role-based access and encryption at rest.

### Supporting services

Purpose:
- document storage,
- notifications,
- integration foundations,
- background job processing,
- observability and error reporting.

Ownership:
- shared platform service layer.

Dependencies:
- queue or worker runtime,
- object storage,
- telemetry and monitoring stack,
- notification providers.

Security considerations:
- implement least-privilege service accounts,
- isolate job execution contexts,
- log operational failures without exposing secrets.

## 3. Control model

The platform control model is organised into three layers:

1. Identity and access layer
2. Policy and approval layer
3. Execution and evidence layer

The frontend does not decide whether an action is allowed. The backend enforces all decisions. Product logic expresses intent, but platform policy decides whether it is permitted.

## 4. Product separation model

The platform supports both products but does not unify their authority:

- Business Partner permissions are business-oriented and commercial.
- Hacker permissions are security-oriented, scope-limited, and audit-heavy.
- Cross-product permissions are denied by default.

This model is enforced by explicit capability registries and role-to-tool mappings.

## 5. Platform data domains

The shared platform must keep data classes distinct:

- shared platform data: users, orgs, workspaces, subscriptions, settings
- product data: business context and operational records for Business Partner; asset, scope, evidence, and findings for AI Hacker
- execution data: task states, command invocations, logs, results
- temporary execution data: scratch files, ephemeral work folders, queued jobs
- sensitive credentials: integration secrets and test credentials
- audit records: who did what and when
- evidence records: source-backed facts and validation data

## 6. Security and governance

The platform must maintain:

- strict tenant boundary checks,
- workspace-scoped access,
- policy-enforced tool access,
- API authentication and rate limiting,
- audit history for every execution,
- environment isolation for sensitive workload types,
- secure storage of all secrets and credentials.

## 7. Recommended implementation stance

For the initial release, the platform should be implemented as a modular monolith with explicit application modules rather than as independent microservices. This keeps the system realistic for a small team while still preserving the critical boundaries required by product safety and security.

The temporary security execution environment for AI Hacker should be treated as an isolated worker boundary rather than a general-purpose distributed system.
