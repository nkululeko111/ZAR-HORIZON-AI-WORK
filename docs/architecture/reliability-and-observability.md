# Reliability and observability

## 1. Reliability goals

The architecture must support resilient operation in the face of provider variability, partial execution, retries, and background job failure. Reliability requirements differ between the two products, but the platform should use common patterns wherever possible.

## 2. Expected failure modes

### LLM provider outages

If a model provider is unavailable, the system must:

- detect the outage,
- retry according to policy,
- fail to a degraded mode where possible,
- preserve task state and user context,
- avoid executing high-risk actions without a completed decision step.

### Tool failures

Tool failures must be represented as structured execution outcomes, not as generic errors. The system should capture:

- timeout or connection errors,
- validation errors,
- permission denials,
- API error codes,
- partial data results,
- final exception state.

### Timeouts and partial execution

The execution engine must support:

- task-level timeouts,
- cancellation paths,
- partial result capture,
- recovery or resubmission logic,
- explicit reporting of incomplete work.

### Duplicate requests

The platform should support idempotency keys to prevent duplicated action execution when the user retries or a provider retries a request.

### Interrupted workflows

Workflows should be resilient to interruption by:

- persisting task state,
- keeping execution checkpoints,
- resuming safely from the last confirmed state,
- preventing repeated external actions after a retry.

### Background job failures

Background jobs must:

- emit structured failure records,
- retry under controlled policies,
- record queue position and attempt count,
- allow human review if a task is blocked or ambiguous.

## 3. Reliability controls

### Retry safety and idempotency

The system should guarantee that repeated attempts do not accidentally trigger duplicate external actions. For Business Partner actions, this is particularly important where sending a quote, updating a record, or creating a task could otherwise happen twice.

Recommended model:

- task-level idempotency token,
- tool-level deduplication checks,
- ensure external side effects are not repeated without verification,
- compare expected state before and after retry.

### Cancellation

The platform must support cancellation of:

- user-requested operations,
- provider-side timeouts,
- stuck or long-running tool calls,
- security execution tasks that violate scope or policy.

### Usage and cost tracking

The platform should track:

- tokens and model usage,
- tool execution time,
- provider cost,
- per-tenant consumption,
- quota exceedance and warnings,
- operational and security-related usage patterns.

## 4. Observability requirements

### Logging

The platform should log:

- request metadata,
- tenant and workspace context,
- user and service identity,
- product and task identifiers,
- tool execution details,
- approval events,
- verification results,
- error context.

Logs must be structured and sanitised.

### Metrics

Recommended metrics include:

- task throughput,
- tool execution counts,
- approval rate and denial rate,
- failure rate by product and tool,
- provider latency and error rate,
- queue depth,
- evidence storage volume,
- security execution timeouts and cancellations.

### Tracing

The platform should support request tracing across:

- API layer,
- orchestration layer,
- tool execution layer,
- provider calls,
- background job processing,
- verification loop.

This enables operational root cause analysis and audit investigation.

## 5. Security-specific reliability concerns

For AI Hacker operations, execution failures and scope violations must be detected and recorded with high specificity. The system should record:

- scope drift,
- timeouts or aborted assessments,
- unexpected network or credential use,
- blocked tools,
- policy denials,
- partial validation states,
- any action that violates the set execution boundary.

These records should be accessible to both operational teams and audit reviewers.

## 6. Business Partner-specific reliability concerns

For Business Partner workflows, the system must avoid duplicate external actions during retries or repeated sync events. The design should use:

- exact action idempotency keys,
- operation versioning,
- deterministic sync reconciliation,
- record verification before repeating a side effect,
- safe retry after result validation only.

This is essential for order creation, customer communication, and financial workflow actions.

## 7. Operational posture

The initial implementation should favour structured observability over elaborate distributed operations patterns. That means:

- logs and task state in a durable store,
- explicit failure classification,
- simple background worker patterns,
- clear operational dashboards,
- evidence and audit records retained per task.

This is sufficient for the early release without overbuilding infrastructure.
