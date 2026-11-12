# Shared Platform Principles

## 1. Purpose

The shared platform is the common foundation used by both the AI Business Partner and the AI Hacker. It provides the core operational, security, and governance infrastructure required for enterprise use.

The platform provides shared capabilities, but it does not grant shared authority. Both specialist systems remain independently governed, permissioned, and operationally distinct.

## 2. Shared platform responsibilities

The shared platform must support:

- user authentication,
- organisation and workspace management,
- multi-tenant architecture,
- subscription and usage management,
- audit logging,
- notifications,
- agent execution history,
- user permissions,
- document storage,
- integration management,
- AI provider configuration.

These are shared platform responsibilities that enable both product lines to operate in a consistent enterprise environment.

## 3. Separation of agent systems

The Business Partner and Hacker are separate specialist systems with independent capabilities, permission models, and operational boundaries.

The Business Partner focuses on business research, planning, operational execution, and commercial workflows.

The Hacker focuses on authorised offensive security investigation and testing.

Shared infrastructure does not mean shared authority. The platform must keep agent capability boundaries explicit and enforceable.

## 4. Multi-tenancy principles

The platform must support multi-tenant organisation-level separation. Each organisation must be able to maintain distinct:

- users,
- workspaces,
- data sets,
- permissions,
- integrations,
- agent execution histories.

The platform must enforce boundary protections so that data and workflows remain segregated by organisation and workspace.

## 5. Identity and permissions

A robust identity and access model is required:

- user identities and roles,
- workspace-level context,
- organisation-level access control,
- agent-specific permission scopes,
- approval requirements for sensitive operations,
- role-based restrictions on tool and workflow access.

The Business Partner must not inherit offensive security permissions. The Hacker must not inherit financial or business-operational permissions. Permission boundaries must be explicit and auditable.

## 6. Agent execution lifecycle

The platform should manage a consistent lifecycle for agent execution:

1. task or objective intake,
2. permission and scope validation,
3. execution context creation,
4. tool or workflow access checks,
5. execution logging,
6. evidence capture,
7. outcome validation,
8. report or action delivery.

This lifecycle ensures that both agents operate with clear accountability, traceability, and reviewability.

## 7. Integration architecture principles

The platform must support integrations in a disciplined manner:

- integration credentials are managed centrally,
- access is scoped to a defined business or security purpose,
- integrations must be auditable,
- sensitive operations require approval or verification,
- integration configuration must be tenant-aware.

The platform must not enable automatic, unsupervised access across unrelated domains.

## 8. Auditability

Auditability is a core requirement. The platform must record:

- who initiated an action,
- what was requested,
- which agent executed it,
- what tools or systems were used,
- what permissions were granted,
- what evidence was captured,
- whether the task succeeded or failed,
- whether approval was required and obtained.

This is required for both business operations and security assessments.

## 9. Security and data isolation

The platform must protect sensitive business and security data through:

- tenant separation,
- workspace constraints,
- permission enforcement,
- restricted tool access,
- secure storage of credentials and integration secrets,
- execution logging,
- isolation of security execution environments.

Business operational data and security assessment data must never be treated as equivalent from a control perspective.

## 10. Governance principles

The shared platform must maintain strong governance around:

- customer authorisation,
- human review for high-risk actions,
- deletion or suppression of evidence where applicable,
- lifecycle management of integrations and permissions,
- operational and compliance traceability.

The shared platform is the control layer that allows both product lines to operate safely in a regulated environment.

## 11. Design implication

The platform is shared in infrastructure, but not shared in authority. The organisation’s environment is shared, but each specialist system is independently responsible for the quality, evidence, and controls of its domain-specific actions.

This design preserves the foundational founder-approved separation between business execution and security testing while enabling a common enterprise foundation.
