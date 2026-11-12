# Data lifecycle and retention

## 1. Purpose

This document defines the lifecycle management of records across the platform, Business Partner, and AI Hacker data domains. It covers creation, update, archive, retention, deletion, legal holds, and operational handling of sensitive records.

This document does not claim POPIA compliance. It documents how the conceptual design should support future legal and compliance review.

## 2. Lifecycle categories

The lifecycle design groups records into categories:

- user and tenant records,
- product operational records,
- financial and customer records,
- execution and tool records,
- evidence and findings,
- temporary working files,
- integration credentials,
- audit and compliance records.

## 3. User accounts and tenants

### User accounts

Lifecycle:
- creation on onboarding or invitation,
- validation of identity and ownership,
- membership updates,
- permission changes,
- deactivation on account closure or role removal,
- deletion or anonymisation under policy.

Retention:
- standard platform lifecycle retention for active accounts,
- longer retention for audit events and security-related records.

### Organisations

Lifecycle:
- onboarding,
- workspace and subscription setup,
- active use,
- suspension or closure,
- deletion after final approval.

Retention:
- tenant records should remain available for the required legal and operational period,
- final deletion requires explicit policy and ownership review.

## 4. Workspaces and product records

### Workspaces

Lifecycle:
- creation,
- access assignment,
- product enablement,
- archival or deletion.

Retention:
- workspace records are retained while the organisation remains active or until a delete action is approved.

### Product operational records

Lifecycle:
- document creation,
- task or workflow update,
- completion or closure,
- historical retention for trend and audit analysis.

Retention:
- tenant-defined policy for Business Partner records,
- security policy for AI Hacker records.

## 5. Financial records

Financial and operational records should remain traceable from the original source to the report or recommendation.

Lifecycle:
- import or user entry,
- validation and normalisation,
- classification,
- analysis and reporting,
- archival or removal under policy.

Retention:
- keep at least as long as needed for audit and business review,
- final retention period requires business and legal review.

## 6. Uploaded documents and generated outputs

Lifecycle:
- upload or creation,
- validation,
- association to business or security context,
- use in analyses or reports,
- archive or deletion.

Retention:
- separate from evidence and audit retention rules,
- generated documents remain tied to task or report history.

## 7. AI execution histories and approvals

Lifecycle:
- request intake,
- plan creation,
- execution,
- approval event,
- verification,
- completion or failure record.

Retention:
- operational execution records should be preserved long enough to support troubleshooting, audit, and customer review.

Approval records should remain linked to the exact action and decision for traceability.

## 8. Audit events

Lifecycle:
- event generation,
- system storage,
- period retention,
- archive or deletion according to policy.

Retention:
- audit records should retain a longer period than operational task data because they support governance, compliance, and incident investigation.

## 9. Security assessments and findings

Lifecycle:
- assessment initiation,
- authorisation and scope review,
- execution,
- validation,
- reporting,
- remediation and retest,
- closure or revision.

Retention:
- evidence and findings should be kept according to the project's security evidence policy, which likely exceeds ordinary operational record retention.

Important note:
- a finding should remain traceable to evidence and validation status even after closure.

## 10. Temporary execution data

Temporary execution data includes:

- intermediate files,
- worker scratch areas,
- retry payloads,
- staged outputs,
- temporary logs.

Lifecycle:
- creation at task execution start,
- use during operation,
- cleanup after successful completion or failure,
- purge based on retention threshold.

Retention:
- short-lived and policy-driven; not a long-term storage class.

## 11. Integration credentials

Lifecycle:
- creation,
- validation,
- periodic rotation,
- expiry,
- revocation,
- deletion after connection removal.

Retention:
- secret material should not persist beyond required use and must be replaced through rotation or revocation.

## 12. Organisation closure and deletion requests

When an organisation closes or requests deletion:

- record deletion should follow explicit policy,
- affected product records and evidence should be reviewed,
- legal or contractual holds may override deletion,
- audit and security evidence may require longer retention.

## 13. Backup retention

Backup retention should cover:

- database backups,
- object-storage evidence backups,
- configuration snapshots,
- historical operational state.

Retention should be aligned with disaster recovery and compliance needs, but not used as a substitute for a well-defined product retention policy.

## 14. POPIA and compliance implications

The design should account for South Africa's POPIA obligations where data is personal or sensitive, but this document does not claim compliance. The conceptual database design alone does not guarantee lawful processing or retention.

The design should still support:

- data minimisation,
- purpose limitation,
- accountability,
- deletion and correction workflows,
- access security and retention controls.

## 15. Open decisions requiring approval

The following are not yet final decisions:

- evidence retention periods,
- audit record retention periods,
- maximum age for security findings and historical assessments,
- deletion workflow for inactive organisations,
- whether some business records are archived instead of deleted.

These require legal, founder, and security review before final operational enforcement.
