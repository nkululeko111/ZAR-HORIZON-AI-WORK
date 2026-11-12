# Architecture and security readiness

## Summary

The documented direction is a shared platform with product-separated execution domains and a modular-monolith starting point. The direction is coherent, but core trust controls and much of the supporting data/API surface remain design-level only. The present runtime scaffold must not be mistaken for an implementation of those controls.

## Cross-layer consistency

- **Product to architecture:** the separation between Business Partner and AI Hacker is consistent in principle. Shared infrastructure is explicitly not shared authority.
- **Architecture to database:** the documents describe tenant/workspace/product ownership and audit/evidence needs. The actual schema and migration are a small platform foundation; membership, role, entitlement, approval, evidence, and product-specific records are not fully represented.
- **Architecture to API:** the API specifications describe authenticated, tenant-scoped interactions and approval-oriented workflows. The runtime exposes health/version routes only; the product API contracts are not implemented.
- **API to UX:** screen and journey documents assume onboarding, workspaces, approvals, execution status, and reporting. Those journeys have no matching runtime endpoints or pages yet.
- **Security to execution:** the design calls for policy-gated tools, isolated Hacker execution, evidence, and audit. Agent entry points are unimplemented and tool sets are empty.
- **Decision status:** the architecture and product materials contain both approved principles and recommendations awaiting decisions. The implementation team must distinguish them rather than treating all prose as final authority.

## Required negative scenarios

| Scenario | Intended enforcement layer | Documentation specificity | Actual implementation evidence |
|---|---|---|---|
| Business Partner user attempts to access Hacker tools | Backend product entitlement/permission check plus separate capability registry and execution boundary | Product separation and backend enforcement are stated; concrete permission schema, registry policy, and denial contract still require design | No registered agent tools or policy engine; no cross-product runtime authorization verified |
| Hacker user attempts to access Business Partner financial records | API authorization on every object/query, product-level access policy, tenant/workspace scoping | Data ownership and product separation are documented; exact role-to-resource matrix and enforcement queries remain incomplete | No request authentication/authorization; current relational constraints do not prove access checks |
| Organisation A attempts to access Organisation B data | Authenticated API tenant context, scoped data access, database constraints; decide whether to add PostgreSQL RLS | Tenant principles and some composite-constraint patterns are documented; RLS is an option, not a settled decision | A composite organisation/workspace constraint is tested; no cross-tenant request denial is established |
| Background job runs without valid tenant context | Job creation must capture validated tenant, workspace, product, actor/service identity and authorization; worker must fail closed if context is missing or stale | Documents expect contextual execution and audit; the exact job envelope, service identity, revocation behavior, and revalidation point need specification | No production job framework or validated tenant-bound worker context exists |
| Approved action is changed before execution | Server stores canonical action + parameter digest, binds approval to that exact payload, rechecks at execution, and requires reapproval on material change | Exact-action approval principle is documented; canonicalization, hashing, expiry, replay/idempotency behavior need detail | No approval model or execution-time revalidation exists |
| Direct API request bypasses approval | Every sensitive API/tool execution path calls backend policy and approval enforcement; deny by default | Backend-enforced approval is stated; endpoint coverage and policy integration contract need completion | Product endpoints and approval engine are absent; bypass resistance has not been tested |

**Conclusion:** the documents provide a useful security intent and several implementable principles, but not enough detailed behavior to implement and test all six controls without further choices. None of the scenarios has been demonstrated as enforced by the current runtime.

## Database and API readiness

### Database

The model has initial organisation, user, workspace, agent session/execution, and audit concepts, and a relational constraint can prevent an execution session from pairing a workspace with the wrong organisation. That is a useful foundation but is not a complete authorization system.

Before sensitive product-data work, resolve:

- organisation membership and workspace roles,
- product entitlements and permission ownership,
- tenant enforcement strategy, including whether RLS is required,
- approval records and exact-action binding,
- audit/evidence lifecycle, retention, deletion, and access,
- product-specific data schema boundaries,
- execution context required by background jobs.

### API

The API documents are detailed design contracts, not actual runtime routes. Before implementation, align the first workflow against its endpoints and decide authentication/authorization, error behavior, idempotency, async status transitions, cancellation, audit fields, and webhook boundaries. Do not build to endpoint catalogs as if they were already implemented or fully approved.

## UX readiness

The UX documentation covers distinct products, journeys, approval concepts, and wireframes. It is design-only. The first implementation needs approved scope for onboarding/workspace selection, uncertain or incomplete data, approvals, execution pending/running/failed/cancelled states, post-action verification, and responsive/accessibility expectations. Current API/runtime cannot support the complete documented journeys.

## AI-specific security readiness

- Treat prompts, uploaded documents, external research, and tool outputs as untrusted input.
- LLM output cannot grant permission or override backend authorization, approval, scope, or execution policy.
- Bind each action to actor, tenant/workspace, product, exact parameters, approval, execution, result, and evidence.
- Hacker execution needs a controlled worker, bounded network access, credential isolation, resource limits, and emergency stop before any actual assessment capability.
- Keep Business Partner financial calculations deterministic, sourced, and reviewable.

These are policy/design requirements, not verified defenses. No real penetration test, external scan, or production-like agent execution was performed.

The shared security documentation also addresses authentication/MFA, RBAC, session handling, API rate limiting and input/output handling, secrets, encryption, audit, retention, file access, background jobs, and dependency supply-chain risk. The inspected application and CI configuration do not demonstrate these as complete operational controls; they remain implementation and verification work.

## Readiness actions

1. Approve a first workflow and its acceptance criteria.
2. Decide identity/membership, tenant enforcement, product permissions, and exact-action approval semantics.
3. Model and test the complete authorization context for API requests and background jobs.
4. Complete product-specific execution and evidence contracts before enabling external actions.
5. Keep AI Hacker assessment capability disabled until scope, isolation, emergency-stop, and evidence controls are implemented and tested.
