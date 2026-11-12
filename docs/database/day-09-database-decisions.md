# Day 09 database decisions

## 1. Overall recommendation

The recommended database design for the initial platform is:

- one PostgreSQL database instance,
- multiple logical schemas or domains for platform, business, and security,
- vital shared tenant and identity tables in the platform schema,
- product-specific data models for Business Partner and AI Hacker,
- strict tenant and product-bound access controls,
- a clear distinction between operational records, evidence, audit events, and secret references.

This is not a fully approved implementation decision. It is the recommended design for the next design and implementation planning phase.

## 2. Tenant and organisation model summary

The tenant model should be built around:

- `User`
- `Organisation`
- `Workspace`
- `OrganisationMembership`
- `Role`
- `Permission`
- `ProductEntitlement`
- `Subscription`
- `UsageRecord`

A user may belong to multiple organisations, and an organisation may contain multiple workspaces. Product access should be defined by entitlement and role, not by default access or UI state.

The model must support both formal businesses and individuals working without a registered company.

## 3. Shared platform entities summary

The shared platform owns the identity, policy, execution, approval, and integration domains, including:

- auth/session records,
- organisation and workspace records,
- plans and entitlements,
- subscriptions,
- usage events and summaries,
- execution runs and tool invocations,
- approval requests and decisions,
- evidence references,
- audit records,
- notification and integration metadata,
- secret references rather than raw secrets.

## 4. Business Partner entities summary

The Business Partner domain should include:

- business profile and operating context,
- financial accounts and transactions,
- reporting periods and budgets,
- tasks, follow-ups, customer and supplier records,
- quotes and documents,
- analysis runs and recommendations,
- proposed actions and outcome records.

The model must distinguish imported financial facts from calculated metrics and AI-generated interpretation.

## 5. AI Hacker entities summary

The AI Hacker domain should include:

- customer records,
- assets, domains, applications and APIs,
- authorisation records and scope definitions,
- assessment plans and runs,
- tool execution history,
- vulnerability findings,
- evidence records,
- remediation records,
- retest and verification results.

The model must preserve validation status and evidence provenance for every security finding.

## 6. Data isolation strategy

The platform uses a shared database for convenience and lower cost, but the architecture still requires product and tenant isolation. This means:

- every tenant-owned record carries `organisation_id`,
- workspace-scoped records carry `workspace_id`,
- domain tables remain product-specific,
- service-layer authorisation is mandatory,
- RLS or equivalent database enforcement is recommended as a second layer,
- background jobs must carry explicit tenant context,
- product access must never be implicit.

## 7. Credential protection approach

The recommended approach is:

- store secret references in normal tables,
- store actual secrets in a dedicated secret manager or vault,
- restrict secrets by organisation and environment,
- rotate and expire credentials,
- prevent raw secret values from entering applications logs or generic LLM prompts.

## 8. Evidence and audit data model

The platform should distinguish:

- audit events for who did what and when,
- execution records for tool and workflow state,
- evidence records for proof tied to analysis or a finding,
- document references for generated or uploaded files.

This prevents casual confusion between documents, evidence, and audit history.

## 9. Data lifecycle recommendations

The recommended lifecycle model includes:

- user and organisation lifecycle tracking,
- workspace lifecycle management,
- business and security record retention,
- evidence retention and security review,
- short-term retention for temporary execution data,
- secret rotation and revocation,
- explicit deletion and archive steps for organisation closure.

No final retention periods are fixed in this document because those require founder, legal, and security review.

## 10. Major technical risks

The major risks are:

- poor tenant enforcement if service logic is not consistent,
- accidental cross-product access due to shared infrastructure,
- overbroad DB privileges,
- weak validation of background job tenant identity,
- secret leakage through logs or application payloads,
- insufficient evidence retention policy,
- oversimplified financial and security provenance models.

## 11. Decisions requiring founder approval

The following are still unresolved and require founder or governance signoff before implementation becomes operationally final:

- single PostgreSQL database versus future-separated product databases,
- whether PostgreSQL RLS is adopted immediately or deferred,
- secret management platform or vault selection,
- evidence retention periods,
- organisation and workspace governance model,
- how customer and internal user roles are formally mapped,
- final legal and operational retention policy for business and security data.

## 12. Documentation status

This day contains the database and multi-tenant architecture documentation package for the project. It remains within the documentation-only scope and does not create actual database objects, code, migrations, or runtime infrastructure.
