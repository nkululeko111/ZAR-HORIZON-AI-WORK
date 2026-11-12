# Agent orchestration and execution lifecycle

## 1. Common execution lifecycle

Both specialist products use the same conceptual lifecycle:

1. Receive user request.
2. Identify product and user context.
3. Interpret the task.
4. Retrieve relevant context.
5. Create an execution plan.
6. Check permissions and policy.
7. Identify required tools.
8. Request approval where required.
9. Execute permitted actions.
10. Capture results and evidence.
11. Verify execution.
12. Handle errors or incomplete results.
13. Report the outcome.
14. Record execution history.

This lifecycle is not a vague workflow document; it is the operational contract for the platform and the product engines.

## 2. Core responsibilities

### Agent orchestrator

Purpose:
- begin the task,
- select the active product domain,
- create a plan based on task type and status,
- coordinate state transitions.

Responsibilities:
- map user intent to product workflow,
- resolve tenant and workspace context,
- gate execution by policy,
- manage retries and cancellations.

### Planning component

Purpose:
- break tasks into subprocesses,
- identify necessary data, tools, approvals, and verification steps,
- keep steps ordered and auditable.

Responsibilities:
- estimate dependencies,
- determine whether the task is a research-only task or an execution task,
- identify when the system requires human approval.

### Context retrieval

Purpose:
- load relevant organisational, product, and task context,
- fetch prior records, documents, policy, and evidence.

Responsibilities:
- retrieve tenant-scoped records only,
- filter by product authority,
- surface only authorised context.

### Tool registry

Purpose:
- provide explicit tool definitions,
- store permissions and product restrictions,
- validate tool inputs and outputs,
- manage execution metadata and logs.

Responsibilities:
- attach policy metadata to each tool,
- prohibit a tool from being available outside its allowed domain,
- bind tool execution to tenant and product identity.

### Policy engine

Purpose:
- evaluate the request against security and operational policy,
- determine if the action is permitted,
- decide whether approval is required.

Responsibilities:
- enforce product separation,
- enforce tenant constraints,
- validate scope and exclusions,
- detect unauthorised tool or environment usage.

### Approval engine

Purpose:
- manage approval requests,
- assign decision owners,
- capture time, status, and reasons,
- enforce expiration and cancellation handling.

Responsibilities:
- allow or deny before execution,
- record an approval decision as an audit event,
- block execution when the decision is missing or expired.

### Execution engine

Purpose:
- run the permitted action,
- assign task metadata and execution state,
- integrate with the tool registry and verification service.

Responsibilities:
- invoke the tool in the correct environment,
- capture results and partial failure state,
- surface structured execution output back to the orchestrator.

### Evidence service

Purpose:
- persist the records required to prove what happened,
- keep source references, outputs, and validation evidence,
- link evidence to task records and final reports.

### Verification component

Purpose:
- validate whether the expected outcome actually occurred,
- compare preconditions and postconditions,
- detect partial success and runtime anomalies,
- emit the final execution status.

## 3. Preventing bypass of permissions or approval

The platform prevents privilege bypass by taking the following approach:

- frontend UI is not trusted for security or approval decisions,
- all permission checks occur in the backend policy engine,
- tool registry entries declare exact product scope and restriction metadata,
- the execution engine requires a valid approval record before high-risk actions,
- tool invocation is validated against current tenant, workspace, user, and product roles,
- evidence is recorded for every tool execution and approval decision,
- sensitive operations require policy evaluation and an explicit execution record,
- the model is not treated as a security boundary.

## 4. Execution safety patterns

The platform should enforce several operational patterns:

- deny-by-default for tool access,
- require explicit capability mapping for each product,
- keep approvals server-side and separate from frontend state,
- fail closed when policy cannot be evaluated,
- log every execution and approval event,
- quarantine insecure or temporary execution results,
- prevent direct arbitrary execution from user-controlled application processes.

## 5. Product-specific orchestration differences

Business Partner orchestration focuses on reasoning, context, and business action plans. AI Hacker orchestration focuses on authorised scope, asset context, evidence validation, and stop-testing conditions. The platform lifecycle remains common, but policy requirements differ by product.

## 6. Outcome reporting

All task completion paths should end with a structured final report containing:

- objective,
- context used,
- decision or action taken,
- verification outcome,
- evidence references,
- approval status,
- remaining risk or unknowns,
- final state of the task.

This makes execution history usable for both customer-facing reporting and internal audit review.
