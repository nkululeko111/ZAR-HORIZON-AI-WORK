# Business Partner API specification

## 1. Purpose

This specification defines the API contract for the AI Business Partner product. It supports the approved MVP workflow: business context → financial data → analysis → issue identification → recommended action → approval → execution → verification → reporting.

## 2. Business context endpoints

### GET /api/v1/business/profile

Purpose:
- retrieve the current business profile for the active workspace.

Product:
- Business Partner.

Auth:
- required.

Permissions:
- Business Partner access and workspace membership.

Approval:
- no.

MVP priority:
- P0.

### POST /api/v1/business/profile

Purpose:
- create or update the business profile.

### GET /api/v1/business/objectives

Purpose:
- retrieve business objectives and operating context.

### PATCH /api/v1/business/profile/context

Purpose:
- update organisational operating context.

## 3. Financial data endpoints

### POST /api/v1/business/financial/import

Purpose:
- import financial records from a source file or integration.

MVP priority:
- P0.

Required controls:
- validate source format,
- store import source metadata,
- distinguish imported facts from derived values.

### GET /api/v1/business/financial/transactions

Purpose:
- list transactions.

### GET /api/v1/business/financial/summary

Purpose:
- retrieve revenue and expense summaries.

### GET /api/v1/business/financial/cashflow

Purpose:
- retrieve cash-flow summary.

### GET /api/v1/business/financial/profitability

Purpose:
- retrieve profitability and margin analysis.

### GET /api/v1/business/financial/budgets

Purpose:
- retrieve budgets and actual versus budget status.

### GET /api/v1/business/financial/periods

Purpose:
- retrieve reporting periods.

Important rule:
- source data and derived analysis must be separately represented so that calculated outputs are not mistaken for user-entered facts.

## 4. Business intelligence endpoints

### POST /api/v1/business/analysis

Purpose:
- submit a new business analysis request.

MVP priority:
- P0.

### GET /api/v1/business/analysis/{analysisId}

Purpose:
- retrieve analysis result.

### GET /api/v1/business/analysis/{analysisId}/issues

Purpose:
- retrieve issues found during analysis.

### GET /api/v1/business/analysis/{analysisId}/opportunities

Purpose:
- retrieve opportunities.

### GET /api/v1/business/analysis/{analysisId}/recommendations

Purpose:
- retrieve recommendations.

### GET /api/v1/business/analysis/{analysisId}/evidence

Purpose:
- retrieve evidence supporting analysis conclusions.

## 5. Business action endpoints

### POST /api/v1/business/actions/proposed

Purpose:
- create a proposed business action.

### GET /api/v1/business/actions/proposed

Purpose:
- list proposed actions.

### POST /api/v1/business/actions/{actionId}/approve

Purpose:
- request approval for the proposed action.

### POST /api/v1/business/actions/{actionId}/execute

Purpose:
- execute an approved action.

### GET /api/v1/business/actions/{actionId}/verification

Purpose:
- retrieve action verification status.

### GET /api/v1/business/actions/{actionId}/outcomes

Purpose:
- retrieve outcomes and result evidence.

### POST /api/v1/business/actions/{actionId}/cancel

Purpose:
- cancel an action if supported by the workflow.

Approval notes:
- external communications, purchases, financial commitments, and high-risk operational changes require explicit approval.

## 6. Task and document endpoints

### POST /api/v1/business/tasks

Purpose:
- create a task.

### GET /api/v1/business/tasks

Purpose:
- list tasks.

### PATCH /api/v1/business/tasks/{taskId}

Purpose:
- update task status or metadata.

### POST /api/v1/business/quotations

Purpose:
- create a quotation.

### GET /api/v1/business/quotations/{quotationId}

Purpose:
- retrieve a quotation.

### POST /api/v1/business/documents

Purpose:
- generate a business document.

### GET /api/v1/business/documents

Purpose:
- list generated business documents.

## 7. Research endpoints

### POST /api/v1/business/research/market

Purpose:
- request market research.

### POST /api/v1/business/research/suppliers

Purpose:
- request supplier discovery or comparison.

### GET /api/v1/business/research/{researchId}

Purpose:
- retrieve the result of a research request.

### GET /api/v1/business/research/{researchId}/sources

Purpose:
- retrieve source references and evidence for the research.

## 8. Endpoint reference table

| Endpoint | Method | Purpose | Auth | Permission | Approval | MVP |
| --- | --- | --- | --- | --- | --- | --- |
| /api/v1/business/profile | GET/POST/PATCH | Business profile lifecycle | Required | Business Partner access | No | P0 |
| /api/v1/business/objectives | GET | Objectives and operating context | Required | Business Partner access | No | P0 |
| /api/v1/business/financial/import | POST | Import financial records | Required | Business Partner access | Conditional | P0 |
| /api/v1/business/financial/summary | GET | Revenue and expense overview | Required | Business Partner access | No | P0 |
| /api/v1/business/financial/cashflow | GET | Cash-flow summary | Required | Business Partner access | No | P0 |
| /api/v1/business/financial/profitability | GET | Margin and profitability analysis | Required | Business Partner access | No | P0 |
| /api/v1/business/financial/budgets | GET | Budget vs actual | Required | Business Partner access | No | P0 |
| /api/v1/business/analysis | POST | Business analysis request | Required | Business Partner access | No | P0 |
| /api/v1/business/actions/proposed | POST/GET | Proposed actions | Required | Business Partner access | No | P0 |
| /api/v1/business/actions/{actionId}/approve | POST | Approve action | Required | Approval authority | N/A | P0 |
| /api/v1/business/actions/{actionId}/execute | POST | Execute approved action | Required | Business Partner access + approval | Yes | P0 |
| /api/v1/business/tasks | POST/GET | Task management | Required | Business Partner access | No | P0 |
| /api/v1/business/quotations | POST/GET | Quote management | Required | Business Partner access | Conditional | P0 |
| /api/v1/business/documents | POST/GET | Generated document retrieval | Required | Business Partner access | Conditional | P1 |
| /api/v1/business/research/market | POST | Market research request | Required | Business Partner access | No | P1 |
| /api/v1/business/research/suppliers | POST | Supplier discovery request | Required | Business Partner access | No | P1 |

## 9. Notes

- This API is intentionally scoped to the approved MVP and should not claim support for a wide business automation platform prematurely.
- All calculations should be backed by deterministic financial engine outputs, not free-form LLM arithmetic.
- Recommendations and action outcomes must track evidence and verification status.
