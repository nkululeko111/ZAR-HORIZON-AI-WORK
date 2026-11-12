# Architecture decision record

## 1. Decision log

This record captures the main proposed architecture decisions for the platform and the two specialist products. These are not presented as founder-approved decisions unless clearly marked as such. Where the project still needs direction, the status is marked as proposed or pending.

| ID | Decision | Status | Reasoning |
| --- | --- | --- | --- |
| ADR-01 | Shared platform with independent specialist product domains | Proposed | Preserves business and security separation while reusing common infrastructure |
| ADR-02 | Modular monolith for initial release | Proposed | Realistic for a small team and safer than premature microservices |
| ADR-03 | Separate Business Partner and AI Hacker permission models | Proposed | Required by the product definitions and security boundaries |
| ADR-04 | Backend-enforced approval and policy checks | Proposed | Prevents UI-only bypass and matches execution safety requirements |
| ADR-05 | Deterministic financial calculation engine | Proposed | Prevents LLM arithmetic from becoming the source of truth |
| ADR-06 | Isolated security execution boundary for Hacker | Proposed | Required for scope control and safe tool execution |
| ADR-07 | Evidence-first execution model | Proposed | Required for auditability, trust, and verification |
| ADR-08 | Tenant-aware platform architecture | Proposed | Enforces organisation and workspace data separation |
| ADR-09 | Provider-independent AI and integration layer | Proposed | Prevents vendor coupling and supports future product evolution |
| ADR-10 | Shared audit and evidence services | Proposed | Supports operational traceability and security review |

## 2. Detailed decisions

### ADR-01: Shared platform with independent specialist product domains

Decision:
- create a shared platform for identity, workspace, policy, auditing, and integration foundations,
- keep Business Partner and AI Hacker as distinct product engines.

Reasoning:
- the repo already supports a common platform foundation,
- product separation is a core founder-approved product principle,
- infrastructure reuse is beneficial without equating product authority.

Alternatives considered:
- one monolithic product with mixed business/security capabilities,
- fully separate repositories for each product,
- fully separate services for every capability.

Advantages:
- shared costs and foundation,
- consistent governance,
- faster platform development.

Disadvantages:
- requires strong access boundaries,
- more complex policy control.

Security implications:
- product and tenant separation must be strict.

Cost implications:
- moderate platform investment, low duplication.

Dependencies:
- identity model,
- policy engine,
- tenant-aware data model.

Status:
- proposed.

### ADR-02: Modular monolith for initial release

Decision:
- use a modular monolith approach rather than a distributed microservice system in the first release.

Reasoning:
- small team,
- lower infrastructure and operational burden,
- easier product isolation and the same control plane.

Alternatives considered:
- microservices from day one,
- separate product repos,
- serverless-only design.

Advantages:
- simpler operations,
- easier governance,
- fewer deployment difficulties.

Disadvantages:
- later refactoring may be needed once scale increases.

Security implications:
- internal service separation still required.

Cost implications:
- lower than distributed systems early on.

Dependencies:
- disciplined module boundaries.

Status:
- proposed.

### ADR-03: Separate Business Partner and AI Hacker permission models

Decision:
- the Business Partner and AI Hacker must be independently permissioned and tool-scoped.

Reasoning:
- founder-approved product boundaries require separate execution authority,
- the products serve different operational contexts.

Advantages:
- reduces safety risk,
- prevents cross-product privilege leakage.

Disadvantages:
- requires careful permission matrix design.

Security implications:
- critical to enforcement across both product domains.

Cost implications:
- moderate increase in policy and identity complexity.

Dependencies:
- role definitions,
- capability registry,
- product tool maps.

Status:
- proposed.

### ADR-04: Backend-enforced approval and policy checks

Decision:
- all approvals and policy enforcement must occur in the backend service layer.

Reasoning:
- UI controls are not a security boundary,
- backend enforcement is required for auditability and trust.

Advantages:
- stronger security,
- better auditability,
- easier compliance review.

Disadvantages:
- requires more server-side logic.

Security implications:
- essential for all high-risk actions.

Cost implications:
- moderate implementation cost.

Dependencies:
- approval engine,
- policy engine,
- execution engine integration.

Status:
- proposed.

### ADR-05: Deterministic financial calculations

Decision:
- financial calculations and deterministic arithmetic are implemented in a controlled analysis engine rather than by the LLM.

Reasoning:
- business financial outputs must be reliable and auditable,
- arithmetic cannot be delegated blindly to model reasoning.

Advantages:
- improves trust and repeatability,
- easier explanation and review.

Disadvantages:
- requires explicit formula and data lineage design.

Security implications:
- reduced risk of fabricated financial values.

Cost implications:
- moderate, but manageable.

Dependencies:
- financial data model,
- calculation rules,
- evidence linkage.

Status:
- proposed.

### ADR-06: Isolated security execution boundary for Hacker

Decision:
- Hacker tools must not execute directly from the main application process.

Reasoning:
- security tools are high risk and commanded within approved scope,
- the architecture requires a separate execution boundary with network restrictions, timeouts, and logging.

Advantages:
- higher safety and reduced blast radius,
- clearer auditability.

Disadvantages:
- more infrastructure and process complexity.

Security implications:
- foundational to the Hacker safety model.

Cost implications:
- moderate but justified.

Dependencies:
- worker isolation design,
- tool registry,
- network controls,
- evidence capture.

Status:
- proposed.

### ADR-07: Evidence-first execution model

Decision:
- every execution must capture evidence, verification state, and result metadata.

Reasoning:
- both products require evidence-backed reporting and auditability.

Advantages:
- improves trust and transparency,
- better remediation and review.

Disadvantages:
- more storage and ingest complexity.

Security implications:
- evidence must be protected and linked to user, task, and tenant.

Cost implications:
- moderate storage and processing cost.

Dependencies:
- evidence service,
- execution state model,
- verification component.

Status:
- proposed.

### ADR-08: Tenant-aware platform architecture

Decision:
- the platform is shared by infrastructure, but all product, user, and workspace data remains tenant-aware and isolated.

Reasoning:
- required for multi-tenant operation and security boundaries.

Advantages:
- safer platform operations,
- better support for customer organisations.

Disadvantages:
- requires careful policy and query-level enforcement.

Security implications:
- essential for customer data separation.

Cost implications:
- moderate.

Dependencies:
- tenant, workspace and relationship model.

Status:
- proposed.

### ADR-09: Provider-independent AI and integration layer

Decision:
- both AI provider access and external integrations are abstracted behind adapter and policy layers.

Reasoning:
- the architecture must remain model-independent and not be tightly coupled to one provider.

Advantages:
- more flexibility,
- easier future expansion,
- cleaner product logic.

Disadvantages:
- more adapter and abstraction work.

Security implications:
- provider configuration remains strictly controlled.

Cost implications:
- moderate implementation overhead.

Dependencies:
- model registry,
- adapter interfaces,
- provider security configuration.

Status:
- proposed.

### ADR-10: Shared audit and evidence services

Decision:
- execution logs, audit trails, and evidence records are centralised in shared platform services.

Reasoning:
- both products require traceability and review.

Advantages:
- consistent visibility,
- easier investigation and operational support.

Disadvantages:
- higher data retention and access management burden.

Security implications:
- must be carefully protected and scoped.

Cost implications:
- moderate storage cost.

Dependencies:
- audit event model,
- evidence store,
- retention policy.

Status:
- proposed.

## 3. Unresolved design choices requiring founder approval

The following items are not architecture decisions in the sense of being fully approved; they require owner or founder review before implementation planning is finalised:

- which tenant segmentation model is preferred for customer onboarding and workspace management,
- final deployment topology for the Hacker execution boundary,
- whether to keep a single shared platform or split the platform into clearly separate product-controlled service domains,
- final retention and deletion policy for sensitive security evidence,
- final security review and escalation workflow for high-risk AI Hacker actions,
- whether the platform should support only one orchestration runtime or both product-specific execution engines with a common control layer,
- the final decision on whether all integrations are centrally managed or product-owned with standard adapters.

## 4. Decision status summary

All architecture decisions in this record are currently proposed because the document is a design exercise rather than an implementation handoff. They are ready for technical review and founder approval before system development begins.
