# Agent tool contract standard

## 1. Purpose

This document defines the standard contract for agent tools used by the Business Partner and AI Hacker product domains. The goal is to ensure that every tool is explicit, permissioned, tenant-aware, approved when required, and auditable.

This is a specification for future implementation and must not be confused with actual tool execution code.

## 2. Required tool metadata

Every tool should define:

- tool name
- product owner
- purpose
- description
- input schema
- output schema
- required permissions
- tenant requirements
- workspace requirements
- approval requirements
- risk classification
- execution timeout
- idempotency behaviour
- failure behaviour
- evidence requirements
- audit requirements

## 3. Tool contract schema

A tool contract should include:

```json
{
  "toolName": "example_tool",
  "productOwner": "business_partner",
  "purpose": "Summary of purpose",
  "description": "Human readable description",
  "inputSchema": "reference_or_definition",
  "outputSchema": "reference_or_definition",
  "requiredPermissions": ["business.read", "business.actions.execute"],
  "tenantRequired": true,
  "workspaceRequired": true,
  "approvalRequired": false,
  "riskClassification": "low",
  "executionTimeoutMs": 30000,
  "idempotency": "perExecutionRequest",
  "failureBehavior": "return structured error and write audit record",
  "evidenceRequirements": ["source_ref", "verification_record"],
  "auditRequirements": ["tool_invocation", "result_status", "actor", "tenant"]
}
```

## 4. Tool invocation lifecycle

The standard lifecycle is:

Request → Validate input → Verify identity → Verify tenant → Verify product permissions → Check policy → Check approval → Execute → Capture result → Verify → Record audit event.

This sequence must be enforced for every tool invocation.

## 5. Product and permission enforcement

Tools must be registered according to product and tenant scope. The registry is deny-by-default.

A tool may be invoked only when all of the following are true:

- the current user is authenticated,
- the user belongs to the active organisation,
- the workspace is valid and tenant-bound,
- the product entitles the user to the tool,
- the tool is registered for that product,
- the tool is allowed in the current environment,
- approval checks have passed where required,
- the execution request remains within its authorised scope.

## 6. Tool policy expectations

The platform must enforce:

- no tool permission mutation by the LLM,
- no policy bypass through prompt manipulation,
- no unapproved side effects,
- no direct access to secrets, raw DB connections, or unrestricted shell commands,
- no direct invocation of tools outside the permitted product domain.

## 7. Risk classification

The tool registry should classify tools into tiers such as:

- low risk: read-only informational tools
- medium risk: read-write but bounded operational tools
- high risk: financial commitments, external communication, or privileged workflows
- critical risk: security testing and sensitive execution tasks

Critical-risk tools must be isolated and require explicit review and approval.

## 8. Approval requirements

A tool may require approval based on:

- the action type,
- the affected tenant or workspace,
- whether the tool delivers an external side effect,
- whether it makes a financial commitment,
- whether it impacts security scope or high-risk environment state.

Approval is not just a UI flag. It is a server-side requirement attached to exact action parameters.

## 9. Evidence requirements

Any tool invocation that creates or modifies state should create or link to:

- request metadata,
- result metadata,
- associated payload or output,
- verification record,
- audit event.

For security tools, evidence capture is mandatory.

## 10. Failure behaviour

Each tool must define:

- expected failures,
- timeout behaviour,
- retries or no-retry rules,
- partial-success handling,
- structured error response,
- audit event on failure.

The system must not silently treat a failed tool call as success.

## 11. Idempotency behaviour

The tool contract should define:

- whether the tool supports idempotency keys,
- whether duplicate invocation is safe,
- whether a second invocation with the same idempotency token should return the prior result.

This matters for both Business Partner actions and security assessment tasks.

## 12. Audit and observability requirements

Every tool invocation should be recorded with:

- actor identity,
- product and tenant context,
- workspace context,
- tool name and version,
- approval status,
- execution status,
- execution duration,
- result summary,
- evidence references.

## 13. Summary

The tool contract standard is designed to ensure that the LLM cannot fabricate execution results or bypass permission checks. The tool registry is a backend enforcement layer, not a prompt-level convenience feature.
