# Asynchronous execution and webhooks

## 1. Purpose

Some agent requests require longer than a normal synchronous HTTP request. This document defines how tasks such as research, financial analysis, assessment orchestration, or long-running approvals are handled asynchronously.

## 2. Asynchronous execution model

### Submission response

When a long-running request is submitted, the API should respond immediately with:

- `202 Accepted`,
- execution ID,
- status URL,
- optional polling interval,
- correlation ID,
- tenant and workspace context.

Example shell response:

```json
{
  "data": {
    "executionId": "exec_123",
    "status": "queued",
    "statusUrl": "/api/v1/agent/requests/exec_123",
    "correlationId": "req_abc_456"
  }
}
```

### Execution ID and status

Each job should have:

- execution ID,
- parent request ID,
- tenant ID,
- workspace ID,
- product code,
- status lifecycle,
- startedAt, updatedAt, completedAt,
- result URL or artifact references.

Status values may include:

- queued,
- running,
- waiting_for_approval,
- executing,
- partial_success,
- succeeded,
- failed,
- cancelled,
- expired.

### Status polling

The API should expose a status endpoint that allows the client to poll job state without blocking a web request. Polling should be safe and cheap, and it must respect rate limits.

### Completion notification

The API may notify users with:

- webhook event,
- email or message notification,
- in-app notification,
- status change resource update.

For long-running security or research jobs, completion notifications should contain minimal summary metadata and a reference to the execution details.

### Cancellation

A running execution may be cancelled only if:

- it is still cancellable,
- the backend policy allows cancellation,
- the job is within the user’s scope,
- the cancellation is logged and auditable.

Cancellation response should indicate whether the job was stopped, pending graceful halt, or already irreversible.

### Retry behaviour

Retries should be explicit and bounded. The system must differentiate between:

- transient infrastructure failure,
- policy validation failure,
- external dependency failure,
- approval timeout,
- client-level retry.

The job should not automatically retry unsafe or approval-blocked actions.

### Idempotency

Long-running job submission should support idempotency keys to prevent duplicate execution when the same submission is retried. The backend should return the same execution ID for the same idempotency key and request payload if the request is still considered the same operation.

### Failed jobs

Failed jobs must record:

- failure code,
- trace ID,
- failed stage,
- whether the job can be resumed,
- whether partial results are safe to view,
- whether a new approval is required.

### Partial results

A job may return partial results when some evidence or intermediate steps are available but not the full result. This must be visible as a partial state and not reported as full success.

## 3. Tenant and product context in background jobs

Asynchronous jobs must securely carry:

- tenant ID,
- workspace ID,
- organisation ID,
- product entitlement,
- user or service principal identity,
- policy context,
- approval status and approval tokens,
- execution scope and restrictions.

The background worker must not rely on ambient browser state or transient UI sessions. The job context must be immutable and stored with the request record.

## 4. Integration boundaries and webhooks

### Webhook authentication

Webhooks must authenticate using:

- a secret or shared secret stored in a secure secret manager,
- a signed payload using HMAC or equivalent,
- a per-connection credential or token bound to the connection.

The platform must never accept unsigned webhook requests.

### Signature validation

The webhook receiver must validate:

- expected signature header,
- timestamp freshness,
- payload hash or body hashing,
- secret identity for the source integration.

If validation fails, the request must be rejected and logged.

### Replay protection

Webhook replay protection should include:

- timestamp check,
- nonce or event ID check,
- deduplication cache for recent event IDs,
- event age guard.

### Event deduplication

A webhook event should be idempotent at the application boundary. The consumer should check event IDs and ignore duplicates.

### Retry policy

Webhook delivery should support retries with:

- exponential backoff,
- maximum retry count,
- dead-letter handling for unprocessable events,
- event queueing for asynchronous processing.

### Event logging

Every webhook event should be recorded with:

- integration ID,
- source system,
- event type,
- event ID,
- timestamp,
- status,
- delivery attempt count,
- verification result.

### Integration permissions

Each integration should use least-privilege permissions. Examples:

- accounting integration: read financial records and configuration only,
- CRM integration: read/contact update rights only,
- issue tracker: create or update issue metadata only,
- security tooling: evidence submission and policy-constrained result upload only.

No integration should receive more rights than the current tenant and product context require.

## 5. Security expectations

The platform must not accept unauthenticated webhook calls or deliver untrusted event payloads without verification. Webhooks must be treated as external input and validated against tenant, workspace, and product context.

## 6. Summary

Long-running operations should be asynchronous by design, with explicit status tracking, audit logging, and secure job context. Webhooks must be authenticated, signed, replay-resistant, and deduplicated. Tenant and product boundaries must travel with the job even after the user request returns.
