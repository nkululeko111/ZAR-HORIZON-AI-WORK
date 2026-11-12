# Integration architecture

## 1. Purpose

The platform requires a provider-independent integration layer for both specialist products. The goal is to support multiple external systems without hard-coding a single vendor or service into the core product logic.

The architecture is intentionally generic. It does not select vendors or approve specific external providers.

## 2. Integration principles

- integrations must be adapter-based,
- integration permissions must be tenant-aware,
- credentials must remain in secure secret storage,
- external actions must be auditable,
- retries and rate limits must be implemented by policy,
- failures must be retriable without duplicating side effects,
- monitoring must track both operational and security-related integration health.

## 3. Business Partner integrations

### Accounting and financial systems

Purpose:
- read balances,
- import transactions,
- reconcile revenue and expenses,
- track invoices and payables.

Adapter responsibilities:
- map external financial objects into the internal business model,
- handle sync policies and rate constraints,
- flag data quality and reconciliation gaps.

Security considerations:
- read-only access by default for monitoring use-cases,
- write or update actions only under explicit approval.

### CRM platforms

Purpose:
- access customer and lead data,
- update sales opportunities,
- create activity records.

Security considerations:
- contact or customer records should be scoped to the tenant and workspace,
- outbound communications require approval before sending.

### Email and calendars

Purpose:
- draft and queue messages,
- sync scheduling and meeting notes,
- track follow-up tasks.

Security considerations:
- message sending must require approval for external communication or financial commitments.

### Documents and spreadsheets

Purpose:
- ingest files,
- extract structured business data,
- generate reports and proposals.

Security considerations:
- files should be scanned for dangerous content and stored with source metadata,
- external document access must remain scoped to the organisation.

### Sales and task management systems

Purpose:
- create follow-up tasks,
- update pipeline status,
- coordinate workflows.

Security considerations:
- task writes must be user- and tenant-scoped,
- actions that affect customer commitments require review.

### Inventory and POS systems

Purpose:
- read stock data,
- monitor inventory pressure,
- support operational decisions.

Security considerations:
- inventory writes require approval and evidence.

## 4. AI Hacker integrations

### Asset and domain discovery

Purpose:
- maintain discovery and inventory data,
- provide live security context for assessments.

Security considerations:
- discovery must remain within authorised scope and test windows.

### Web application testing tools

Purpose:
- test authentication, authorisation, input handling, and configuration posture.

Security considerations:
- must run only in isolated execution environments,
- strict network and scope constraints apply,
- active exploitation steps require higher approval.

### API testing tools

Purpose:
- test API behaviour, authentication patterns, and data exposure.

Security considerations:
- API credentials must be short-lived or tightly scoped,
- output should be recorded with evidence and findability metadata.

### Vulnerability intelligence

Purpose:
- connect findings to known issues, public advisories, or internal knowledge.

Security considerations:
- treat intelligence as supporting evidence, not proof by itself.

### Security reporting

Purpose:
- deliver peer-reviewable reports,
- produce structured findings and remediation summaries.

### Remediation and issue tracking

Purpose:
- create remediation tasks,
- track fix status,
- coordinate retesting.

Security considerations:
- issue tracking write actions should be limited to authorised project contexts.

## 5. Adapter model

Each external system should follow an adapter model with:

- adapter definition,
- credential provider,
- auth handler,
- schema mapper,
- rate-limit policy,
- retry and failure policy,
- monitoring hooks,
- evidence capture for requests and responses.

This keeps core product logic independent from vendor-specific implementation details.

## 6. Authentication and credential storage

The integration layer should support:

- OAuth or equivalent service credentials,
- scoped credentials per organisation or workspace,
- short-lived tokens where feasible,
- secret rotation support,
- encrypted storage at rest,
- restricted access to specific workflow types.

Credentials must never be embedded in logs or application code.

## 7. Permission scopes

Every integration adapter must declare:

- access scope,
- target product domain,
- tenant restrictions,
- read/write capability,
- required approval states,
- execution environment restrictions,
- data retention expectations.

## 8. Data synchronisation and webhooks

The platform should support:

- scheduled synchronisation for low-risk data,
- event-driven webhooks for fast updates,
- idempotent processing for duplicate events,
- robust handling of out-of-order or repeated updates,
- explicit retry policy for failed syncs.

Webhook and sync processing must be designed with idempotency to avoid duplicate actions when a provider retries.

## 9. Rate limits, retry policies, and failure handling

The integration layer should implement:

- per-provider rate-limit tracking,
- quota management,
- exponential backoff or jittered retry,
- partial failure handling,
- explicit dead-letter or retry queues,
- timeout and cancellation rules,
- alerting for persistent failures.

## 10. Integration monitoring

Monitoring must cover:

- authentication failures,
- sync lag,
- provider outages,
- repeated 5xx or timeout issues,
- rate-limit throttling,
- permission drift,
- side-effect failures.

Operational health should be visible to both product teams and platform operators.
