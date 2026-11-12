# Database decision register

## 1. Overview

This register captures the logical database decisions for the platform architecture. These are proposed design decisions and not founder-approved implementation decisions unless explicitly recorded as such.

## 2. Decision log

| ID | Decision | Recommendation | Reasoning | Status |
| --- | --- | --- | --- | --- |
| DB-01 | Database model | One PostgreSQL instance with separate logical schemas | Balances isolation, simplicity, and cost | Proposed |
| DB-02 | Product data separation | Separate product data domains under shared platform | Required by product and security boundaries | Proposed |
| DB-03 | Tenant model | Organisation and workspace as first-class tenant dimensions | Required by multi-tenant architecture | Proposed |
| DB-04 | Authorisation model | Service-layer checks plus database-layer protections | Better enforcement than UI-only controls | Proposed |
| DB-05 | Approval data model | Approval records must bind to exact action payloads | Required for auditability and security | Proposed |
| DB-06 | Evidence model | Separate evidence, audit, and document records | Essential for traceability and clarity | Proposed |
| DB-07 | Credential handling | Secret references, not plaintext storage | Required for security | Proposed |
| DB-08 | Financial model | Distinguish facts, derived metrics, and AI interpretation | Required for reliability and trust | Proposed |
| DB-09 | Security findings model | Store validation status and evidence on every finding | Required for defensible assessments | Proposed |
| DB-10 | Retention strategy | Define lifecycle policies by record class | Required for legal and operational clarity | Proposed |

## 3. Detailed decisions

### DB-01: One PostgreSQL instance with separate logical schemas

Recommendation:
- single PostgreSQL database instance,
- logical separation by schema or domain,
- tenant-aware and product-aware table design.

Alternatives:
- one shared schema,
- one product database per product,
- separate databases for every domain.

Advantages:
- practical for small team,
- easier reporting and shared platform operations,
- simpler backup model.

Disadvantages:
- requires strong access enforcement,
- accidental cross-product access is a risk if policy is weak.

Security implications:
- product and tenant isolation must be enforced at service and database layers.

Cost implications:
- lower than multiple databases.

Implementation implications:
- requires disciplined schema boundaries and access control.

Status:
- proposed.

### DB-02: Separate product data domains

Recommendation:
- separate Business Partner and AI Hacker data spaces under a common platform and shared identity layer.

Advantages:
- product independence,
- stronger governance,
- easier permission enforcement.

Disadvantages:
- requires careful data access rules.

Security implications:
- essential for the product safety model.

Implementation implications:
- requires product-specific domain tables and cross-checking.

Status:
- proposed.

### DB-03: Organisation and workspace tenancy

Recommendation:
- organisation is the tenant boundary,
- workspace is the operational scope within the tenant,
- records carry organisation and workspace identifiers where appropriate.

Advantages:
- clear operational ownership,
- easier permission model,
- supports customer and team separation.

Disadvantages:
- added query complexity.

Security implications:
- required for multi-tenant operation.

Status:
- proposed.

### DB-04: Service-layer plus database-layer enforcement

Recommendation:
- primary enforcement in service layer,
- supplemental enforcement via RLS or equivalent row filters where appropriate.

Advantages:
- stronger safety net,
- reduced accidental leakage.

Disadvantages:
- more complexity.

Implementation implications:
- requires careful design and disciplined code review.

Status:
- proposed.

### DB-05: Exact approval binding

Recommendation:
- approval records hold the exact action and parameters approved.

Advantages:
- auditability,
- prevents approval drift,
- supports later dispute review.

Disadvantages:
- requires careful payload handling.

Status:
- proposed.

### DB-06: Evidence and audit separation

Recommendation:
- keep evidence, audit events, and uploaded documents as distinct record classes.

Advantages:
- clearer traceability,
- easier governance,
- clearer security handling.

Disadvantages:
- additional modeling effort.

Status:
- proposed.

### DB-07: Secret references instead of plaintext credentials

Recommendation:
- store only secret references in standard data tables.

Advantages:
- safer operational design,
- easier rotation and access control.

Disadvantages:
- more infrastructure coordination.

Status:
- proposed.

### DB-08: Separate financial facts from derived values and AI interpretations

Recommendation:
- financial imports remain raw facts,
- calculations are distinct outputs,
- AI-generated narrative is clearly separated.

Advantages:
- increases trust and auditability.

Disadvantages:
- requires explicit provenance design.

Status:
- proposed.

### DB-09: Findings carry validation and evidence

Recommendation:
- every vulnerability finding carries classification, severity, confidence, validation status, and evidence references.

Advantages:
- stronger evidence traceability,
- prevents overconfidence from scanner noise.

Disadvantages:
- more metadata and validation work.

Status:
- proposed.

### DB-10: Explicit retention policy by record class

Recommendation:
- different retention lifecycles for user, financial, evidence, audit, and temporary execution data.

Advantages:
- better governance and compliance readiness.

Disadvantages:
- needs legal and founder alignment.

Status:
- proposed.

## 4. Unresolved decisions

The following require further review:

- whether the final platform uses a single database or separate product databases later,
- whether to implement PostgreSQL RLS immediately or defer it to a later phase,
- final retention periods for security evidence and financial data,
- final credential management tool or vault solution,
- specific workspace and subscription policy for founder or trial accounts,
- how organisation closure and deletion are handled operationally.
