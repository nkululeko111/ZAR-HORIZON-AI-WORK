# Business Partner tool catalogue

## 1. Purpose

This catalogue defines the initial tool set for the AI Business Partner product. The list is intentionally narrow and MVP-focused. Not all candidate tools are included in the first release. Tools are selected for deterministic financial logic, auditable actioning, and approval-gated external effects.

## 2. MVP prioritisation

### P0 tools

- `get_business_profile`
- `get_financial_summary`
- `get_revenue_expense_breakdown`
- `calculate_cash_flow`
- `calculate_profitability`
- `compare_budget_actuals`
- `propose_business_action`
- `create_task`
- `update_task_status`
- `generate_business_document`
- `execute_approved_action`
- `verify_business_action`

### P1 tools

- `analyse_business_performance`
- `research_market`
- `discover_suppliers`
- `compare_suppliers`
- `prepare_quotation`

## 3. Tool definitions

### `get_business_profile`

Purpose:
- retrieve the active business profile and current operating context.

Inputs:
- businessId, workspaceId, profileScope.

Outputs:
- business profile JSON, market context, organisation summary, relevant KPIs.

Required access:
- Business Partner product access and workspace membership.

Approval:
- none for read-only access.

Evidence:
- retrieval metadata, timestamp, actor context.

Failure cases:
- missing business record, stale workspace, insufficient permissions.

### `get_financial_summary`

Purpose:
- return aggregate financial snapshots for a period.

Inputs:
- reportingPeriodId, sourceScope, currency.

Outputs:
- revenue, expenses, gross margin, net margin, cash position.

Required access:
- Business Partner product access and financial data permissions.

Approval:
- no for read-only summary.

Evidence:
- source period ID, source record counts, calculation version.

Failure cases:
- missing period, incomplete financial import, currency mismatch.

### `get_revenue_expense_breakdown`

Purpose:
- provide detailed revenue and expense categories.

Inputs:
- periodId, categoryGroup, filters.

Outputs:
- category-level totals and trend data.

Required access:
- active product access.

Approval:
- no for read-only category analysis.

Evidence:
- source ledger references, category mapping version.

Failure cases:
- incomplete import, broken mapping, unsupported granularity.

### `calculate_cash_flow`

Purpose:
- calculate deterministic cash-flow movement for a window.

Inputs:
- periodId, startDate, endDate, sourceRecords, assumptions.

Outputs:
- inflow, outflow, net cash movement, cash-flow narrative.

Required access:
- Business Partner product access and financial permissions.

Approval:
- no for non-commitment calculation.

Evidence:
- source financial records, formula version, audit trail.

Failure cases:
- incomplete records, missing payment dates, ambiguous transactions.

### `calculate_profitability`

Purpose:
- compute profitability and margin metrics.

Inputs:
- periodId, businessUnit, currency, calculationMode.

Outputs:
- revenue, COGS, gross profit, operating margin, bottom-line margin.

Required access:
- Business Partner access and read permission to the relevant financial ledger.

Approval:
- no for analysis-only calculation.

Evidence:
- transaction references, accounting rule version.

Failure cases:
- missing source data, inconsistent accounting categories.

### `compare_budget_actuals`

Purpose:
- compare actuals against budget and highlight variance.

Inputs:
- budgetId, comparisonPeriodId, varianceThreshold.

Outputs:
- variance by category, trend indicators, flagged issues.

Required access:
- Business Partner access and budget permissions.

Approval:
- no for read-only comparison.

Evidence:
- budget version, source actual records, variance logic version.

Failure cases:
- missing budget, mismatched periods, time-window conflict.

### `analyse_business_performance`

Purpose:
- synthesize operational performance insights from financial and business metrics.

Inputs:
- periodId, objectiveSet, optional trend window.

Outputs:
- high-level findings, issue statements, key opportunities, risk flags.

Required access:
- Business Partner access plus business intelligence access.

Approval:
- no for informational analysis.

Evidence:
- supporting metrics, assumption list, source references.

Failure cases:
- poor data quality, insufficient data coverage, unsupported KPI set.

### `research_market`

Purpose:
- gather market research and contextual intelligence for a company or industry segment.

Inputs:
- marketScope, geography, targetSegment, researchQuestion.

Outputs:
- findings, competitor notes, market opportunities, references.

Required access:
- Business Partner access and research capability permission.

Approval:
- required if research is used to support external messaging, pricing, or commitments.

Evidence:
- citations, source links, date of research, confidence scoring.

Failure cases:
- stale source data, insufficient source coverage, unsupported region.

### `discover_suppliers`

Purpose:
- identify supplier candidates from approved discovery criteria.

Inputs:
- category, geography, requirements, constraints.

Outputs:
- candidate supplier list, contact facts, scoring summary.

Required access:
- Business Partner product access and supplier research permission.

Approval:
- no for discovery-only research; required before formal procurement action or commitment.

Evidence:
- source references, search criteria, scoring methodology.

Failure cases:
- invalid supplier criteria, missing region data, low-quality source results.

### `compare_suppliers`

Purpose:
- compare suppliers on cost, capability, delivery, and risk.

Inputs:
- supplierIds or candidate list, comparison criteria.

Outputs:
- comparison table with weighted ranking and risk flags.

Required access:
- Business Partner access and supplier evaluation permission.

Approval:
- required before acting on supplier selection for commitment or external communication.

Evidence:
- source references, scoring weights, decision summary.

Failure cases:
- missing candidate data, unverifiable supplier submissions.

### `generate_business_document`

Purpose:
- generate an approved business document from structured business data.

Inputs:
- documentType, context, templateId, data inputs.

Outputs:
- generated document record, content, metadata, version reference.

Required access:
- Business Partner access and document generation permission.

Approval:
- required for externally sent or legally sensitive documents.

Evidence:
- template version, generation payload, review status.

Failure cases:
- invalid template, missing required fields, unsupported document type.

### `create_task`

Purpose:
- create a task for a business workflow.

Inputs:
- title, description, assignee, dueDate, contextId.

Outputs:
- task record.

Required access:
- Business Partner access and task-authoring permission.

Approval:
- no for internal task creation.

Evidence:
- task metadata and owning context.

Failure cases:
- invalid assignee, missing context, duplicate task conflict.

### `update_task_status`

Purpose:
- update task progress or completion status.

Inputs:
- taskId, newStatus, reason, evidenceRef.

Outputs:
- updated task and status history.

Required access:
- Business Partner access and task ownership or task-management permission.

Approval:
- no for ordinary internal status updates; required when status changes affect legal, financial, or customer commitments.

Evidence:
- before/after status record, actor, optional comment.

Failure cases:
- task not found, invalid status transition, missing actor context.

### `prepare_quotation`

Purpose:
- prepare a quotation document for a proposal.

Inputs:
- customer context, items, pricing assumptions, validity period.

Outputs:
- quotation record and price summary.

Required access:
- Business Partner access and quotation creation permission.

Approval:
- required before submission to external parties when pricing, terms, or commitments are involved.

Evidence:
- assumptions, pricing calculation inputs, approval status.

Failure cases:
- incomplete pricing data, invalid customer scope, unsupported quote components.

### `propose_business_action`

Purpose:
- create a proposed action bound to an objective, context, and funding or operational implications.

Inputs:
- businessObjective, actionType, parameters, expectedOutcome, riskLevel.

Outputs:
- proposed action record, approval request reference.

Required access:
- Business Partner product access and action proposal permission.

Approval:
- required before execution.

Evidence:
- objective mapping, action parameters, expected impact, proposer identity.

Failure cases:
- invalid action type, missing objective context, unsupported parameter set.

### `execute_approved_action`

Purpose:
- execute a previously approved action.

Inputs:
- actionId, executionParams, approvalToken, idempotencyKey.

Outputs:
- execution record, result summary, verification status.

Required access:
- Business Partner access and approval-gated execution permission.

Approval:
- required; no execution without a valid backend approval.

Evidence:
- approval reference, execution trace, output, verification result.

Failure cases:
- approval mismatch, invalid execution payload, external dependency failure, timeout.

### `verify_business_action`

Purpose:
- verify whether a previously executed action achieved the expected outcome.

Inputs:
- actionId, evidenceSources, successCriteria.

Outputs:
- verification result: successful, partial, failed, or requires human review.

Required access:
- Business Partner access and verification permission.

Approval:
- required when the verification changes a commitment record or escalates a risk state.

Evidence:
- objective check, source records, result summary, status attestation.

Failure cases:
- missing post-action evidence, unverifiable results, stale status.

## 4. Security and approval boundary

The Business Partner product must not use unrestricted agent actions to make unreviewed external commitments. External communications, purchases, supplier commitments, or financial effects require explicit backend approval, not just conversational confirmation.

## 5. Design principle

All financial and operational tools should be deterministic, auditable, and linked to source records. LLM reasoning may explain or summarise a calculation but may not be treated as the authoritative implementation of financial logic.
