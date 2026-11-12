# Execution and approval API contracts

## 1. Purpose

This document defines how the API and backend policy layer handle proposed actions, approvals, execution, verification, and cancellation for shared platform actions, Business Partner actions, and AI Hacker security workflows.

## 2. Proposed actions

A proposed action is a structured intent before execution. It must bind to:

- action type,
- tenant ID,
- workspace ID,
- product domain,
- user identity,
- resource identifiers,
- parameters,
- expected outcome,
- relevant scope or target boundary,
- approval requirements.

The system must store the exact action payload and compare subsequent execution against it.

If any material parameter changes after creation, the system must evaluate whether a new approval is required. Material changes include:

- target changes,
- financial amount changes,
- scope expansion,
- time-window change,
- technique or method change,
- customer or asset change,
- risk-level change,
- external recipient change.

## 3. Approval requests

Approval requests are generated server-side and must include:

- approvalId,
- subject or actionId,
- actor who proposed the action,
- approver or approval group,
- product context,
- tenant and workspace context,
- requested action payload hash,
- reason or policy basis,
- expiry timestamp,
- status.

Approvals are not based on the LLM conversation alone. They must be attached to an explicit action record and verified against the exact awaited execution payload.

## 4. Approval decisions

Approval decisions can be:

- approved,
- rejected,
- cancelled,
- expired,
- replaced by a new approval.

The approval decision must record:

- approver identity,
- timestamp,
- decision reason,
- source of validation,
- whether the system re-checked the action payload.

## 5. Approval expiry

Approvals must expire when the underlying action context becomes stale or when a time limit is exceeded. Expiry rules should be enforced in the API layer and job layer, not only in the UI.

Typical expiry conditions:

- a time-window expires,
- the resource or target changes,
- the authorisation expires,
- the scope is modified,
- the approval was never acted on within the defined validity period.

## 6. Approved execution

Execution is allowed only when all checks have succeeded:

- user authenticated,
- tenant and workspace valid,
- product entitlement valid,
- tool permission valid,
- policy check passes,
- approval record valid and current,
- execution request matches the approved action payload.

The backend must reject any execution if the action or parameters differ from approved values.

## 7. Cancellation

The system should support cancellation for in-flight actions when the action has not yet crossed a terminal state. Cancellation rules depend on product and execution context.

Examples:

- AI Hacker assessment cancellation before critical execution begins,
- Business Partner action cancellation before external side effects are committed,
- approval cancellation when the proposal is withdrawn.

Cancellation must record:

- cancellation reason,
- actor identity,
- affected action or approval ID,
- final state.

## 8. Failed execution

Failed execution means the action was attempted but did not complete successfully.

The API must return:

- execution status,
- failure code,
- error message for the caller,
- any relevant evidence reference,
- whether a retry is safe,
- whether the action remains approved.

A failed execution must not be treated as a successful action result.

## 9. Partial execution

Partial execution occurs when some work completed or some side effects persisted while the overall operation did not finish cleanly.

The API must expose the state explicitly:

- `partial_success`,
- `incomplete`,
- `needs_verification`,
- `recovery_required`.

Partial success is not the same as full completion. The system must require verification before closing the action as successful.

## 10. Verification

Verification is required for operational and security actions where the result matters.

Verification inputs include:

- success criteria,
- evidence references,
- expected outcome,
- resource or target state,
- source records.

Verification records should capture:

- status,
- evidence references,
- verification agent or actor,
- timestamp,
- confidence level.

## 11. Evidence capture

Evidence capture is mandatory for:

- Business Partner actions with external or financial impact,
- AI Hacker findings and validation,
- security report creation,
- approval outcomes,
- operational verification.

Evidence should include:

- provenance,
- timestamps,
- source reference,
- actor or system identity,
- classification or sensitivity level,
- retention metadata.

## 12. Security assessment approvals

AI Hacker approvals must account for:

- target asset,
- authorised scope,
- exclusions,
- test window,
- approved techniques,
- required evidence,
- customer-specific restrictions.

A scope change, technique change, time-window shift, or customer change requires re-approval before continued execution.

## 13. Reference examples

### Example approval payload

```json
{
  "approvalId": "apr_123",
  "actionId": "act_456",
  "product": "ai_hacker",
  "tenantId": "tenant_001",
  "workspaceId": "ws_099",
  "scopeHash": "sha256:abc123",
  "status": "pending",
  "expiresAt": "2026-02-01T12:00:00Z"
}
```

### Example execution guard

```text
if action.payloadHash != approved.action.payloadHash:
    reject execution
if action.approval.expiresAt < now():
    reject execution
if action.scope not within approved scope:
    reject execution
```

## 14. Summary

The backend must enforce approval and execution checks, not the UI. Approval must be exact, scoped, and revalidated when the underlying action or environment changes. Security-related approvals require additional controls for target, scope, timing, and approved technique boundaries.
