# Security architecture

## 1. Policy goals

The platform must protect both business and security workflows while preserving independent product authority. Security design is not a bolt-on feature; it is a core architectural requirement.

## 2. Platform-wide security requirements

### Secure authentication

- strong identity verification,
- tenant-aware user sessions,
- secure token handling,
- separate roles for platform admin, Business Partner users, and Hacker users,
- multi-factor enforcement for privileged roles where required.

### Authorisation checks

- permission checks at every major API boundary,
- product-specific capability enforcement,
- workspace and tenant scoping,
- policy checks for all external actions,
- no client-side enforcement as the only control.

### Tenant isolation

- organisation-level separation,
- workspace restriction,
- distinct data boundaries per tenant,
- no shared data access across organisations,
- tenant-aware execution context and policy evaluation.

### Secrets management

- no hard-coded credentials,
- centrally stored and encrypted secrets,
- separate credential sets per integration and environment,
- rotation and revocation support,
- restricted access for operational and security staff.

### Encryption in transit and at rest

- TLS for all network traffic,
- encrypted storage for sensitive content,
- encrypted backups,
- explicit handling for logs and evidence with sensitive contents.

### Input validation

- schema validation for all structured inputs,
- uploaded file validation and screening,
- strict format and size controls,
- validation before execution or persistence.

### API protection

- authenticated API access,
- rate limiting by client and tenant,
- request validation,
- anomaly detection and abuse protection,
- secure error handling without leaking internal details.

### Rate limiting

- limit per user, tenant and integration,
- apply to both platform APIs and external calls,
- monitor for abuse and policy violation.

### Secure file handling

- local or object storage with access controls,
- restricted file lifecycle and cleanup,
- validation before export or external transmission,
- separation of temporary execution files and persisted evidence.

### Audit logging

- who did what,
- when it happened,
- what tool was called,
- what permission was checked,
- what the result was,
- approval status and who approved it.

### Data retention

- retention lifecycle per data class,
- deletion rules for temporary execution data,
- compliance-aware retention for evidence and audit records.

### Backup and recovery

- encrypted backups,
- tested restore process,
- operational recovery for service, data, and evidence store issues.

### Dependency security

- dependency scanning,
- pinned or approved versions,
- vulnerability tracking for Python and JavaScript packages,
- periodic review of upstream issues.

### Secure deployment practices

- environment separation,
- least-privilege deployment identities,
- no secrets in repository files,
- isolated deployment boundaries for the Hacker execution environment.

## 3. Business Partner-specific security requirements

The Business Partner must protect:

- customer and supplier data,
- financial and operational information,
- commercial documentation,
- pricing assumptions and forecasts,
- customer communication records.

Additional rules:

- external action approvals are mandatory for sensitive business flows,
- integration permissions must be narrow and explicit,
- customer information must remain separated by organisation,
- financial calculations must be evidence-backed and auditable.

## 4. AI Hacker-specific requirements

The AI Hacker requires stronger controls due to the exposure of security testing activities:

- explicit authorisation before any assessment begins,
- isolated tool execution boundaries,
- strict scope enforcement and exclusions,
- credential protection and minimisation,
- evidence protection and preservation,
- controlled network access,
- high-risk operation approvals,
- secure handling of sensitive findings and notes.

## 5. Architecture risks requiring further design

The following areas should be designed before implementation begins:

- exact role model and permission matrix for all products,
- exact tenant and workspace enforcement strategy at the database and service layers,
- secret rotation and long-term key management approach,
- final evidence retention policy,
- final alerting and incident response model,
- final security worker runtime boundary for Hacker executions,
- how customer-supplied credentials are provisioned and revoked securely,
- product-specific decision rights for who can approve high-risk actions.

These are not implementation blockers for the architecture document, but they are prerequisites for production-grade execution.
