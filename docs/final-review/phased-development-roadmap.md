# Phased development roadmap

## Roadmap principles

- Do not build both products simultaneously until evidence justifies the added complexity.
- Complete customer discovery and founder decisions before committing to a product backlog.
- Build shared authorization and audit foundations before product features that process tenant data or execute actions.
- Keep AI Hacker execution disabled until its authorization, isolation, scope, and emergency-stop controls are implemented and tested.
- Treat the phases below as a recommendation, not an approved delivery commitment.

## Phase 0 — Discovery and scope decisions

**Purpose:** close decisions that prevent product code from becoming speculative.

1. Interview target customers for each product and record evidence in the validation tracker.
2. Select the initial buyer, product, and one complete workflow.
3. Approve the MVP boundary, exclusions, and measurable outcome.
4. Reconcile which design decisions are approved versus recommendations.
5. Confirm the financial and security review responsibilities relevant to the selected workflow.

**Exit gate:** founder decision recorded for product/workflow; customer evidence and remaining assumptions are explicit.

## Phase 1 — Engineering foundation

**Purpose:** verify the existing scaffold rather than rebuild it.

1. Clone or use a clean worktree and follow the documented local setup.
2. Verify dependency installation, local PostgreSQL/Compose startup, API health, and migration behavior.
3. Run formatting, lint, type-check, tests, and build commands from the documented workflow.
4. Verify CI runs on a pull request and document its actual results.
5. Resolve Python 3.14’s status in the CI matrix: required, provisional/allowed failure, or removed from the tested matrix until validated.
6. Establish clean baseline test evidence and define how new checks are added.

**Exit gate:** repeatable setup and passing baseline are evidenced; failures and worktree changes are not concealed.

## Phase 2 — Shared platform controls

**Dependencies:** Phase 0 decisions; Phase 1 baseline.

1. Decide identity provider, organisation membership, workspace roles, and service identities.
2. Choose tenant enforcement strategy, including whether PostgreSQL RLS is required.
3. Define product entitlements and explicit permission separation.
4. Define audit, execution context, approval records, and exact-action binding.
5. Implement shared controls only for the chosen MVP, with negative tests for cross-tenant, cross-workspace, cross-product, missing-context, modified-action, and direct-API approval bypass cases.

**Exit gate:** authorization decisions are backend-enforced and negative tests demonstrate denial; tests cover job context and approval revalidation.

## Phase 3 — AI Business Partner MVP (conditional first focus)

**Dependencies:** selected product/workflow; Phase 2 controls appropriate to data access; financial data and calculation decisions.

1. Business profile and context for the selected customer.
2. One approved financial data input path with validation for incomplete, duplicated, and inconsistent records.
3. Deterministic calculations with known-answer tests for revenue, expenses, margin, cash flow, currency, and VAT assumptions as applicable.
4. Evidence-backed business-performance analysis that distinguishes verified values, estimates, and assumptions.
5. Recommendation and task/action lifecycle for the approved workflow.
6. Add an external action only if its approval, idempotency, failure handling, and verification behavior are designed and tested.

**Exit gate:** the chosen user outcome is demonstrated with representative test cases, traceable evidence, and clear professional limits. No unapproved integrations or financial advice claims.

## Phase 4 — AI Hacker MVP (separate safety gate)

**Dependencies:** founder choice to prioritize Hacker; legal/authorization model; isolated execution and operational readiness.

1. Customer, asset, and authorization record model.
2. Scope, exclusions, test window, change/revocation, and approval policy.
3. Isolated worker, bounded network access, credentials, resource controls, and emergency stop.
4. Controlled target discovery and web/API assessment only within the approved fixture or customer scope.
5. Finding validation, confidence, evidence integrity, remediation guidance, and retest state.
6. Audit trail and customer-readable reporting.
7. Validate with isolated, deliberately vulnerable fixtures and negative out-of-scope tests.

**Exit gate:** independent security review and demonstrated denial of out-of-scope actions before any pilot with real assets. No unrestricted execution.

## Phase 5 — Integration and commercial readiness

**Dependencies:** evidence that the selected product delivers value and owner-approved production decisions.

1. Customer onboarding and support workflow.
2. Billing/usage limits after pricing and value validation.
3. Monitoring, alerting, cost controls, backup, restore drills, and incident ownership.
4. Provider/region, production database, secrets manager, data-retention, and residency decisions.
5. Staging and production deployment, release approval, smoke/acceptance tests, and rollback.
6. Independent security review appropriate to data sensitivity and product risk.
7. Pilot readiness review before customer production data or autonomous actions are enabled.

## Recommended sequencing

The recommended sequence is discovery → foundation verification → shared platform controls → a narrow Business Partner workflow → reassessment → AI Hacker only after its dedicated safety gate. If interviews show stronger demand for AI Hacker, change the product order by founder decision, not by weakening its controls.

The highest risks in this sequence are unvalidated demand, low-quality SME data and financial trust for Business Partner, and authorization/isolation failure for AI Hacker. Each should be a release gate rather than a post-launch cleanup item.
