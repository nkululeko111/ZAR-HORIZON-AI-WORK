# API security and authorisation

## 1. Purpose

This document defines the security and authorisation expectations for the shared platform, Business Partner, and AI Hacker APIs. It is designed to align with the repository’s architecture and data model decisions: strong tenant isolation, explicit product boundaries, approval enforcement, and bounded tool execution.

## 2. Authentication

Authentication must occur at the platform API boundary. The platform authenticates the user and resolves:

- user identity,
- organisation membership,
- workspace context,
- product entitlements,
- active permissions.

The API must not trust client-side flags or UI state as proof of identity or entitlement.

## 3. Authorisation

Authorisation must be enforced server-side. The API should validate:

- the user is authenticated,
- the user belongs to the organisation,
- the workspace belongs to the organisation,
- the requested product is allowed for the organisation,
- the user has the required role or permission,
- the action is within the tenant and workspace scope,
- the requested tool or endpoint is allowed for the product,
- any required approval has been obtained.

## 4. Tenant isolation

Every resource should be tied to a tenant and, where relevant, a workspace. Requests must be rejected when:

- a tenant mismatch is detected,
- a workspace does not belong to the active organisation,
- a user tries to access product data outside their organisation,
- a product catalogue reference is missing or invalid.

This is essential for Business Partner and AI Hacker separation.

## 5. Product permissions and entitlements

Product access must be explicit. The platform should maintain an entitlement model that checks:

- product subscription or access record,
- organisation-level entitlement,
- workspace-level activation,
- role-based permissions,
- approval capability.

Business Partner and AI Hacker must not share execution permissions by default. The same user must not access AI Hacker tooling through Business Partner entitlement or vice versa.

## 6. Input validation

All request payloads must be validated before processing. Validation should include:

- type checks,
- field presence rules,
- tenant and workspace ownership checks,
- data-range checks,
- reference integrity checks,
- content safety checks where relevant.

Malformed input must return a structured validation error, not an internal service exception.

## 7. Output filtering

API responses must filter sensitive data according to the caller’s access level. For example:

- evidence may be hidden from unauthorised users,
- security findings may be restricted to approved roles,
- financial records may be restricted to authorised workspaces.

Do not echo raw backend internals or internal stack traces.

## 8. Rate limits and abuse prevention

The platform should apply rate limits by:

- user,
- organisation,
- workspace,
- integration connection,
- endpoint group,
- tool or policy class.

Additional abuse mitigations include:

- bot protection for public endpoints,
- escalation controls for repeated invalid requests,
- job throttling for expensive or sensitive tasks,
- request correlation and anomaly detection.

## 9. Sensitive information handling

The API must protect:

- customer records,
- assessment evidence,
- raw secrets or credentials,
- financial records,
- supplier data,
- security findings and remediation details.

The system should avoid returning sensitive metadata to callers without the relevant permission. Secret storage must use references to secure secret stores rather than plaintext values in application data.

## 10. Credential protection

Credentials and tokens must never be:

- stored in plain text in regular application tables,
- exposed in API responses,
- echoed in logs or debug output,
- reused across unrelated tenants or products.

The system should store secret references and rotate credentials through a managed secret and integration layer.

## 11. Audit logging

Every significant API and tool event should be recorded with:

- actor identity,
- tenant and workspace context,
- product and entitlement state,
- tool or endpoint action,
- approval state,
- request correlation ID,
- timestamp,
- result status,
- evidence reference.

Audit logs must be immutable and retain enough detail for later review.

## 12. Idempotency and approval enforcement

The API must support idempotency for state-changing actions and require backend approval checks for sensitive workflows. A repeated request with the same idempotency key should not create duplicate effects.

Approval enforcement must be a backend policy, not a frontend-only feature.

## 13. Security worker boundaries

Security workers and analysis jobs must be isolated. The AI Hacker product must never be allowed to directly access:

- unrestricted database connections,
- unrestricted shell commands,
- arbitrary execution environments,
- secrets outside the approved environment,
- raw platform administrative functions,
- unrelated product domains.

The LLM must not directly bypass the tool registry or backend approval checks.

## 14. Explicit statement

The LLM cannot directly access unrestricted database connections, arbitrary shell commands, secrets, or unrestricted execution environments. Tool execution must be mediated by policy-checked tool contracts with explicit permissions and validation.

## 15. Summary

The security model for the platform is layered and enforceable: authenticate the user, validate tenant and product context, enforce permission and approval checks, validate all input, protect sensitive outputs, and isolate high-risk execution behind controlled tools and workers.
