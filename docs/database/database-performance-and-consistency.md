# Database performance and consistency

## 1. Purpose

This document defines the expected query shapes, indexing strategy, consistency model, and transaction boundaries for the logical data model. The goal is not premature optimisation but a practical, maintainable design that supports the initial shaped workloads of both products.

## 2. Core workloads

### Business Partner workloads

- financial period reporting,
- revenue and expense aggregation,
- budget vs actual comparison,
- customer and supplier lookups,
- task and follow-up retrieval,
- recommendation history and outcome review.

### AI Hacker workloads

- assessment history retrieval,
- asset and domain lookup,
- finding search and filtering,
- evidence retrieval,
- retest history and validation review.

## 3. Primary identifiers

The logical design should use:

- UUIDs or stable surrogate identifiers for most entities,
- natural keys only where they are stable and low-risk,
- tenant-aware composite uniqueness rules where needed,
- explicit versioning for changing records where required.

## 4. Foreign key and relationship design

The model should use explicit foreign keys for:

- organisation to workspace,
- workspace to task or assessment,
- customer or business profile to financial records,
- assessment to findings,
- findings to evidence and remediation records,
- approval requests to approval decisions,
- execution runs to tool invocations and verification results.

## 5. Unique constraints and tenant-aware uniqueness

Common examples:

- unique `email` for active user identity records,
- unique `workspace_slug` per organisation,
- unique `subscription` state per active organisation and product,
- unique `tool_id` and `tool_name` within a product domain,
- unique active authorisation set per customer and scope,
- unique findings per assessment and asset where appropriate.

## 6. Indexing strategy

Indexing should focus on the most common query patterns:

- `organisation_id` on all tenant-owned records,
- `workspace_id` on workspace-scoped tables,
- `product_code` on product-specific tables,
- `status` and `created_at` on execution, approval, and workflow records,
- `tenant_id + status + created_at` for audit and event history queries,
- `assessment_id + finding_id` for evidence and remediation lookup,
- `business_profile_id + period_id` for financial summaries,
- `asset_id + assessment_id` for security findings,
- `customer_id` and `supplier_id` for operational and financial review queries.

## 7. Query patterns and pagination

The design should support:

- time-bounded queries for execution history,
- page-by-page retrieval of tasks, assessments, evidence, and findings,
- filtered queries by organisation, workspace, product, and status,
- dashboards for financial variance and security metrics,
- large evidence list retrieval via cursor or explicit pagination.

## 8. Reporting requirements

Business Partner reporting requires aggregated views such as:

- revenue by period,
- expense by category,
- cash flow by period,
- actual vs budget,
- profitability and margin summaries,
- tasks and follow-up aging.

AI Hacker reporting requires:

- assessment history by customer and assessment status,
- finding counts by severity and status,
- evidence retrieval linked to finding and assessment,
- retest effectiveness and closure state.

## 9. Large evidence and document handling

Evidence and uploaded documents are not ordinary small-row tables. They should be designed to support:

- blob or document storage for large artifacts,
- metadata rows in the database,
- references from findings or reports to stored evidence,
- access control metadata and hash checks,
- separate cleanup policy for temporary working files.

This avoids overloading the relational database with large files while retaining traceability.

## 10. Consistency and transaction boundaries

### Require transactions for

- creating a user and membership records together,
- creating an organisation + initial owner + workspace,
- financial import events that must be atomic,
- approval creation plus approval decision linking,
- assessment and authorisation activation,
- status transitions that must be recorded atomically,
- evidence creation tied to a finding.

### Prefer asynchronous processing for

- large or slow file ingestion,
- external integration synchronization,
- background execution jobs,
- provider retries or queue-based processing,
- evidence processing and report generation after the main action completes.

## 11. Failure handling and inconsistent states

The design must avoid inconsistent states when a worker fails mid-workflow. To do that:

- record execution state before and after each step,
- persist transition events and timestamps,
- allow recovery or resume from a known last-successful step,
- do not assume task completion until verification and evidence are present,
- mark actions as failed or partial rather than silently losing status.

## 12. Duplicate data and deduplication

The design must handle:

- duplicate transaction imports,
- repeated webhooks,
- re-triggered tool invocations,
- repeated security findings or data sources.

This can be managed with:

- unique constraints on logical operations,
- idempotency keys,
- hashing for source or payload deduplication,
- status and verification history rather than overwriting prior records.

## 13. Avoiding unnecessary duplication

The design should avoid duplicating:

- user identity across all product tables,
- tenant metadata in every record where a foreign key suffices,
- evidence payloads in both operational and evidence tables,
- financial source values in both source and summary tables without a clear provenance model.

## 14. Readiness and scalability guidance

The architecture should not prematurely optimise for scale beyond the first release. It should be strong enough for the initial workload and flexible enough to extend when evidence, financial, and security data sets become larger.

The recommended posture is:

- keep logical separation clear,
- ensure indexes support the common query patterns,
- manage large artifacts outside the main relational tables,
- avoid building an overcomplicated distributed database pattern before the product is validated.
