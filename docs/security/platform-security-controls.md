# Platform security controls

## 1. Purpose

This document defines the shared security control model for ZAR HORIZON AI @WORK. It is designed for a governance-first repository and should be used as a baseline for future implementation.

## 2. Core principles

- Backend enforcement is mandatory; frontend restrictions are not a security boundary.
- Product boundaries and tenant boundaries are enforced by the backend.
- Shared platform infrastructure does not confer shared authority across product domains.
- Security controls must be explicit, auditable, and reviewable.
- All sensitive actions require well-defined approval and evidence capture.

## 3. Control matrix

### Authentication

- user identity must be established before access is granted,
- service and worker identities must be distinct from end-user identities,
- session management must be explicit and enforceable,
- user sessions should be invalidated when access changes.

### Multi-factor authentication

- MFA should be considered for privileged accounts and administrative access,
- enforcement should remain policy-controlled and not hardcoded in the frontend.

### Role-based access control

- roles should be defined at the organisation, workspace, and product level,
- permissions must be checked at execution time,
- product-level separation must be enforced by backend policy.

### Tenant and workspace isolation

- the platform must prevent cross-tenant data access,
- workspace membership and object ownership must be checked for every sensitive operation,
- cross-product permission leakage must be prevented.

### API security

- every privileged API action must require authentication and authorisation,
- rate limiting and abuse controls should be applied,
- input validation must reject malformed or malicious payloads,
- outputs must be sanitised and handled as untrusted data.

### Secrets management

- secrets must not be checked into the repository,
- credentials must be provisioned through a managed secret system,
- backend services should keep secrets out of application logs,
- secret rotation and access review must be part of operational practice.

### Encryption and data protection

- traffic should use TLS,
- sensitive data at rest should be encrypted,
- keys and certificates should be managed by a secure platform capability,
- file and document storage must be access-restricted.

### Audit logging and accountability

- every material action must be logged,
- logs should include actor, action, context, and result,
- approval records must be retained,
- evidence should be linked to execution events.

## 4. High-risk areas

The controls must pay special attention to:

- cross-tenant access attempts,
- Business Partner vs Hacker permission leakage,
- secrets exposure,
- approval bypass attempts,
- malicious input or document content,
- background job privilege escalation,
- dependency and supply-chain risk.

## 5. Operational requirement

The platform should define a security review process for major changes before production approval. This remains a future operational requirement rather than an implemented system in the current repo state.
