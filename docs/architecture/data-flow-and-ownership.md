# Data flow and ownership

## 1. Purpose

This document defines the conceptual movement of data across the platform and makes ownership boundaries explicit. It separates shared platform data, Business Partner data, AI Hacker data, execution data, credentials, audit records, and evidence records.

The guiding principle is: shared infrastructure does not imply unrestricted shared data access.

## 2. Data entry points

### Shared platform data entry

User data enters through:

- sign-up and login,
- organisation setup,
- workspace creation,
- subscription management,
- user profile configuration,
- admin and settings flows.

### Business Partner data entry

Business Partner data enters through:

- user-uploaded files,
- CRM and accounting integrations,
- sales pipeline information,
- business documents,
- operational metrics and workflows,
- external research results.

### AI Hacker data entry

AI Hacker data enters through:

- customer onboarding data,
- asset inventory,
- authorised scope and test definitions,
- findings and evidence,
- vulnerability workflow records,
- retest and remediation evidence.

## 3. Validation and normalisation

All data entering the platform should pass through validation and context-binding:

- file type and size validation,
- tenant and organisation binding,
- workspace and user context validation,
- schema validation for structured data,
- quality and completeness scoring,
- source provenance capture,
- classification between fact, assumption, estimate, and recommendation.

Data validation is a shared platform responsibility because it prevents incorrect downstream reasoning.

## 4. Storage and ownership

### Shared platform data

Examples:
- users,
- organisations,
- workspaces,
- roles,
- subscriptions,
- settings,
- platform policies,
- notification records.

Ownership:
- shared platform control plane.

### Business Partner data

Examples:
- business context,
- customer records,
- documents,
- pricing assumptions,
- supplier records,
- operational workflows,
- performance reports.

Ownership:
- tenant-owned Business Partner domain.

### AI Hacker data

Examples:
- authorised assets,
- scope exclusions,
- security assessments,
- findings,
- evidence,
- retest status,
- remediation records.

Ownership:
- tenant-owned AI Hacker domain.

### Temporary execution data

Examples:
- job payloads,
- temporary files,
- working directories,
- cached event data,
- transient validation output.

Ownership:
- execution boundary only; subject to short retention and cleanup.

### Sensitive credentials

Examples:
- integration API keys,
- secrets,
- test credentials,
- service tokens.

Ownership:
- platform secret management boundary; never stored in application logs or general documents.

### Audit records

Examples:
- who invoked a tool,
- who approved the action,
- what was executed,
- timestamps,
- result status.

Ownership:
- shared platform audit domain.

### Evidence records

Examples:
- request/response artifacts,
- screenshots or files,
- validation notes,
- source references,
- remediation verification outputs.

Ownership:
- product-owned evidence domain with platform-level retention and security controls.

## 5. Execution record creation

Every execution creates a record containing:

- task identifier,
- product identifier,
- tenant and workspace identifiers,
- user identity,
- tool identifier,
- input summary,
- execution state,
- output summary,
- approval status,
- evidence links,
- error or timeout status,
- verification state.

This record becomes the foundation for both status reporting and audit review.

## 6. Linking evidence to results

Evidence is linked to results using immutable relationships:

- task record -> tool execution record -> evidence record
- finding -> evidence collection -> validation -> final result
- approval -> action -> execution -> verification -> report

This chain ensures conclusions are grounded in traceable data instead of unstructured LLM narrative alone.

## 7. Tenant and organisation separation

The platform must enforce:

- tenant-bound storage,
- workspace-level context validation,
- role and membership boundaries,
- product-specific object access restrictions,
- no cross-tenant reading or execution,
- no shared secrets or tokens across organisations.

The platform cannot allow a user from one organisation to view another organisation's Business Partner or Hacker data even when both products use the same infrastructure.

## 8. Retention and deletion

The architecture should define a retention policy for each data class:

- platform identity data: standard account lifecycle retention
- product operational data: tenant-defined retention
- audit records: longer retention for compliance and incidents
- evidence records: retain as long as needed to support findings and customer review
- temporary execution data: short retention and cleanup after success or failure
- secrets: strict rotation and short-lived storage where possible

Deletion must consider legal, contractual, and security obligations. For security evidence, deletion should occur only under explicit policy and case review.

## 9. Data separation between products

The Business Partner and AI Hacker must use separate product data namespaces even when both share the same platform. They may share common infrastructure but cannot share permissions or unrestricted access.

Examples:

- Business Partner data cannot be used to execute Hacker workflows.
- Hacker asset and scope data cannot be used as operational business records.
- A user with Business Partner access does not imply access to Hacker scope or evidence.

## 10. Architectural implication

The platform requires a robust data governance layer for:

- tenant-aware storage and query access,
- execution record integrity,
- evidence retention and linkage,
- secret isolation,
- product-level data separation,
- safe and auditable deletion.

Without these controls, the shared platform would become a single shared-authority environment, which violates the product and security requirements.
