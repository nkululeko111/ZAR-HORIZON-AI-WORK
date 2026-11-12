# Day 08 architecture decisions

## 1. Decision summary

The recommended architecture for ZAR HORIZON AI @WORK is a shared platform with two independent specialist product domains:

- AI Business Partner
- AI Hacker

This architecture keeps the platform reusable while imposing strong boundaries around authority, execution, and evidence.

## 2. Architecture approach recommended

The recommended approach is a modular monolith with separate product execution domains and a shared platform control plane. This is the most realistic initial architecture for a small engineering team that needs both enterprise reusability and strong operational safety.

This approach avoids premature microservice decomposition while still preserving the two critical design principles:

1. shared infrastructure,
2. separate product authority.

## 3. Shared platform organisation

The shared platform provides:

- identity and access,
- tenant and workspace management,
- subscription and usage policies,
- AI provider abstraction,
- tool registry governance,
- approval and policy enforcement,
- evidence and audit services,
- document storage,
- notification and integration foundations,
- observability and operational monitoring.

The platform is the control plane. It governs what products and users can do, but it does not unify the execution authority of the two specialist systems.

## 4. Product isolation

The two product engines remain isolated by design:

- Business Partner: business context, commercial workflows, financial analysis, approved business actions, and reporting.
- Hacker: asset management, security assessment, authorised testing, evidence validation, remediation support, and retesting.

The Business Partner cannot access Hacker tools, and the Hacker cannot access Business Partner execution permissions.

This is enforced by product-specific capability registries, policy checks, approval boundaries, and separate execution environments.

## 5. Planning, execution, and verification

Each product follows the same common lifecycle:

- request intake,
- context retrieval,
- planning,
- policy evaluation,
- tool selection,
- approval,
- execution,
- evidence capture,
- verification,
- reporting,
- audit recording.

The LLM is not treated as a security boundary. It is an interpreter and planner, not the authority for approval or execution permission. Backend controls enforce the decision.

## 6. Tool execution and approvals

The tool registry is explicit and permission-based. Tools are only available when the product, tenant, workspace, and user context allow them.

Approval is required for sensitive actions. In all risky cases, the approval must be evaluated and enforced by the backend before the action executes. Frontend controls may assist the user experience, but they do not decide the final action result.

This is essential for both external business actions (Business Partner) and high-risk testing steps (AI Hacker).

## 7. Data and tenant separation

The platform uses tenant-aware storage and access control. Data is separated by:

- organisation,
- workspace,
- product domain,
- operational record type,
- evidence and audit record type.

Shared infrastructure is not unrestricted shared access. Product data is partitioned and access-controlled. Business and Hacker data should never be treated as a single shared dataset.

## 8. AI Hacker execution isolation

AI Hacker execution should be isolated from the main web application process using a dedicated worker or execution boundary. It must support:

- approved tool invocation,
- scoped execution,
- resource limits,
- timeouts,
- network restrictions,
- secure handling of credentials,
- evidence logging,
- cancellation,
- cleanup after execution.

The architecture should allow only tightly scoped, explicit security actions in this execution boundary.

## 9. Initial deployment recommendation

The initial deployment recommendation is:

- shared platform API and web app,
- PostgreSQL database,
- background workers,
- object/document storage,
- AI provider connectors,
- isolated Hacker execution worker when active security workflows are enabled,
- logging and monitoring services.

This is a practical first release and avoids unnecessary distributed infrastructure.

## 10. Major technical risks

The major risks are:

- incomplete policy and authorisation model,
- inadequate tenant-boundary enforcement,
- weak evidence retention design,
- insufficient control over security execution environments,
- over-reliance on model reasoning for critical business or security decisions,
- complexity in integrations and credential handling,
- uncertain final approval workflow for high-risk actions.

These are not reasons to reject the architecture, but they are areas that require deliberate design before implementation.

## 11. Decisions requiring founder approval

The following require founder review before implementation moves beyond the design stage:

- final product onboarding and tenant model,
- final approval workflow for high-risk actions,
- exact scope and retention policy for evidence and audit records,
- the initial deployment posture for the isolated Hacker worker,
- the precise final permission matrix across the shared platform and specialist products,
- final integration security model and credentials flow,
- final owner model for operational and security incident handling.

## 12. Architecture status

This is a design and documentation package only. It does not implement application code, create database schemas, create API endpoints, deploy infrastructure, or alter the existing project configuration.

The proposals are intended to be reviewed, refined, and approved before any implementation work begins.
