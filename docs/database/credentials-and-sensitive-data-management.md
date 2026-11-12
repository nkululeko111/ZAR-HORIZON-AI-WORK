# Credentials and sensitive data management

## 1. Purpose

This document defines the handling of credentials, secrets, and sensitive business or security data in the logical data model. The platform must not store ordinary secrets in regular application tables or allow LLMs or general application logs to see them.

## 2. Information requiring special protection

### Financial and commercial data
- revenue records,
- supplier pricing,
- customer and client information,
- business documents with commercial sensitivity,
- budgets and forecasts.

### Customer and employee data
- user identity fields,
- organisation contact information,
- internal assignee data,
- payroll or HR-like operational data where relevant.

### Integration credentials
- API keys,
- OAuth client secrets,
- signing keys,
- token refresh credentials,
- third-party connector credentials.

### Security test credentials
- test account details,
- authorised credentials for assessment environments,
- access tokens for lab or staging systems,
- credentials used in Hacker execution workers.

### Security findings and exploit evidence
- reproduction details,
- proof artifacts,
- vulnerability evidence files,
- exploit details that should be restricted.

### Audit and internal governance data
- platform permissions,
- approval records,
- change histories,
- security review material.

## 3. Storage model

The recommended pattern is:

- ordinary operational tables store only references to secrets,
- the actual secret values are stored in a dedicated secret store or environment-managed vault,
- the application retrieves secret values at execution time only when needed,
- the secret reference includes metadata such as version, expiry, and scope.

This means the database should not contain plaintext secrets in ordinary fields. It should store only:

- `secret_ref_id`,
- `secret_name`,
- `secret_version`,
- `expires_at`,
- `owner_organisation_id`,
- `access_scope`,
- `rotation_status`.

## 4. Encryption requirements

Sensitive data should be protected at rest and in transit:

- TLS for all network communication,
- encrypted storage for operational databases and ciphertext for secret material,
- encrypted backups for structured and evidence data,
- encrypted object storage for files and evidence.

## 5. Credential access restrictions

Access to credentials must be limited by:

- organisation and workspace scope,
- purpose-specific service identity,
- least privilege access principles,
- short-lived credentials where possible,
- explicit approval for privileged or security-specific access.

## 6. Rotation and expiry

The design should include:

- rotation schedules,
- expiry timestamps,
- revocation workflows,
- validation of active secret lifecycle,
- grace periods where operational continuity is required.

## 7. Temporary credentials

The system should support temporary, short-lived credentials for:

- external integrations,
- assessment-specific test accounts,
- isolated Hacker task execution,
- operations that should expire when a workflow ends.

Temporary credentials reduce the risk of long-lived secrets and stale access tokens.

## 8. Evidence and file access controls

Evidence and findings often contain sensitive details. These should be:

- access-controlled by organisation and workspace,
- linked to exact findings or tasks,
- protected with separate storage and retrieval policies,
- redacted when being shared outside the authorised team.

Evidence should not be treated as ordinary uploaded documents. It is a first-class control object with access restrictions and chain-of-custody expectations.

## 9. LLM and log protection

The system should ensure that:

- the LLM does not receive raw secrets,
- ordinary logs do not contain tokens or credentials,
- debug output is sanitised before storage,
- evidence payloads are redacted before broad sharing,
- secret values are masked in traces and monitoring.

## 10. Security-specific credentials

AI Hacker environments are especially sensitive because they may include:

- application credentials,
- staging credentials,
- API test tokens,
- scan or testing tool arguments,
- environment-specific secrets.

Those should be scoped to the isolated execution worker and not stored in shared operational tables or general-purpose application logs.

## 11. Recommended secret storage pattern

Recommended pattern:

- platform stores secret references, not actual values,
- a dedicated secret manager or vault stores the true secret,
- each integration or tool receives only the credentials it is allowed to use,
- secret retrieval occurs at the execution boundary only,
- secret use is recorded in audit events without exposing the secret value.

## 12. Risk summary

The biggest credential risks are:

- plaintext storage in application tables,
- shared credentials across organisations,
- long-lived secrets in logs or snapshots,
- insecure direct access from non-elevated services,
- poor rotation and revocation,
- accidental exposure of security test credentials.

These should be addressed as a core design requirement, not a post-implementation cleanup step.
