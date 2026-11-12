# Approval and execution experience

## 1. Purpose

This document defines the approval and execution experience for the shared platform, the AI Business Partner, and the AI Hacker products. The UX must make approval states visible and distinguish clearly between proposed, approved, executed, failed, and verified outcomes.

## 2. Shared approval experience

Every approval flow should include:

- approval list,
- approval detail page,
- exact action summary,
- exact parameters and scope,
- product context,
- tenant and workspace context,
- risk classification,
- supporting evidence,
- approve / reject / cancel controls,
- expiry and status information.

The user must not see a generic confirmation without the details of the exact action being approved.

## 3. Business Partner approval examples

### Example 1: external communication

Scenario:
- proposed action sends an external email or customer-facing message.

UX requirements:
- show the message content or a summary,
- show impacted customer or market context,
- show approval expiry and risk level,
- show who requested the action.

### Example 2: financial commitment

Scenario:
- proposed action creates a supplier quote or purchase-related action.

UX requirements:
- show monetary value,
- show business objective,
- show source assumptions,
- show whether a supplier or pricing decision changed materially,
- request explicit approval before execution.

### Example 3: customer system update

Scenario:
- proposed action updates an internal or customer-facing system with a business action.

UX requirements:
- show exact target and payload,
- show whether a new approval is required if parameters changed,
- show execution history and result verification.

## 4. AI Hacker approval examples

### Example 1: assessment start

Scenario:
- proposed assessment starts after authorisation and scope review.

UX requirements:
- show target asset,
- show authorised scope and exclusions,
- show time window and approved techniques,
- show approval expiry.

### Example 2: intrusive technique

Scenario:
- proposed testing technique exceeds prior approval conditions.

UX requirements:
- block execution until approval is reissued,
- show exactly what changed,
- show relevant risk classification and reason for re-approval.

### Example 3: expand scope

Scenario:
- the system proposes additional assets or methods after the initial scope was approved.

UX requirements:
- show delta between approved and proposed scope,
- require explicit re-approval,
- present reason for expansion and risk review.

## 5. Approval detail view structure

The approval detail layout should include:

- action summary,
- requestor and approver,
- product and workspace,
- status and expiry,
- exact parameters,
- evidence summary,
- risk label,
- approve and reject buttons,
- cancel option if available,
- link to execution history.

## 6. Execution state model

The product should clearly visualize:

- proposed,
- pending approval,
- approved,
- queued,
- executing,
- partial success,
- completed,
- failed,
- cancelled,
- verified,
- rejected.

This must be visible in both the action list and the action detail panel.

## 7. Verification experience

After execution, users should see whether the action achieved its goal. The UX should show:

- expected outcome,
- result summary,
- evidence references,
- confidence or status,
- whether verification is pending.

A completed action is not automatically “successful” without verification evidence.

## 8. Notifications and inbox pattern

The shared platform should have an approvals inbox and a general activity feed. Business Partner and AI Hacker each may also have a product-level queue.

Notification examples:

- pending approval,
- approval expired,
- execution failed,
- verification required,
- evidence uploaded,
- assessment ready for review.

## 9. Design quality requirements

- approvals must be exact and not generic,
- execution state must always be visible,
- risk classification must be clear,
- approval expiry must be visible,
- failed or partial states must not look successful,
- evidence should be directly linked to the action outcome,
- the boundary between proposed and executed actions must stay obvious.

## 10. Summary

The approval and execution UX is a core product requirement. Both products depend on a visibly trustworthy and auditable action model, especially where external actions, sensitive business decisions, or security testing are involved.
