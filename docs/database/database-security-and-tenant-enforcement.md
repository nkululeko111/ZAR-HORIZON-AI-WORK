# Database security and tenant enforcement

## 1. Purpose

This document defines how tenant isolation and product data separation are enforced in the logical PostgreSQL design. The database architecture must enforce separation beyond the application UI and beyond LLM logic.

## 2. Core tenant enforcement principles

1. Every tenant-owned record must carry `organisation_id`.
2. Workspace-scoped records must carry `workspace_id`.
3. Product data must carry `product_code` or equivalent domain markers.
4. Every background job must carry tenant, organisation, workspace, and user context.
5. Access checks must happen in the service layer and, where appropriate, in PostgreSQL policy enforcement.
6. The frontend and LLM are never trusted as the security boundary.

## 3. Recommended enforcement model

### Service-layer authorisation

This is the primary enforcement layer.

Rules:
- API handlers validate the user and organisation context,
- the service resolves the authorised workspace and product scope,
- the query runtime checks tenant ownership before reading or writing,
- the policy engine validates the tool or operation against product permissions.

Advantages:
- easier to reason about,
- simpler to implement in a small team,
- works well with a modular monolith.

Limitations:
- depends on correct application logic,
- must be consistently applied in all code paths,
- does not protect against every accidental misuse at the database layer.

### PostgreSQL Row-Level Security (RLS)

RLS is a valuable second layer for tenant-scoped rows.

How it helps:
- restrict rows returned by a query to the current tenant,
- reduce accidental cross-tenant data leakage,
- provide a consistent database-layer safety mechanism.

Advantages:
- enforces tenant boundaries even when application code is imperfect,
- strong for multi-tenant designs.

Limitations:
- adds operational complexity,
- may be more difficult to manage with highly dynamic role and workspace logic,
- still requires service-layer checks for product-level restrictions.

### Database roles and privileges

The database should not grant broad privileges to application users.

Recommended practice:
- app service account with restricted access to only required tables,
- separate account category for admin and migration tasks,
- distinct service roles for platform and product workloads,
- no direct access to secrets or unrestricted query privileges.

### Composite relationships

The design should use composite ownership keys:

- `organisation_id + workspace_id` for workspace-scoped records,
- `organisation_id + product_code` for domain-level records,
- `organisation_id + user_id` for user-owned records when needed.

This makes it harder to accidentally pair a record with the wrong tenant.

## 4. Product domain enforcement

The platform must enforce product restrictions in addition to tenant restrictions:

- Business Partner workflows should never query AI Hacker asset tables without explicit cross-domain policy.
- AI Hacker workflows should never query Business Partner financial tables without specific business justification and authorisation.
- Tool registry metadata must restrict which product and environment can invoke which tool.

## 5. Background job tenant context

Background jobs must include and validate:

- organisation_id,
- workspace_id,
- product_code,
- user_id or service principal,
- request id or execution id,
- approved tool or workflow target.

The job must fail closed if tenant context is missing or inconsistent.

## 6. Document access and evidence retrieval

Document and evidence access should validate:

- the document owner organisation,
- the associated workspace,
- the product domain,
- the user or service's permission to that domain,
- whether the document or evidence is in scope for the task.

This is necessary to prevent insecure direct object references and accidental access to another tenant's evidence.

## 7. Direct object reference prevention

The database and application design should avoid passing raw resource identifiers without verification.

Example pattern:
- fetch evidence by `evidence_id` only after validating organisation and product scope,
- reject resource IDs that do not match the current tenant or workspace,
- treat missing or mismatched IDs as access failures.

## 8. Validation for API requests

For every API request, the platform must validate:

- the authenticated user,
- their active organisation membership,
- workspace membership,
- product or feature entitlements,
- resource owner organisation,
- whether the requested resource is accessible under the current role.

## 9. Validation for database queries

The database should assume the application is not always perfect. This is why RLS or a disciplined query abstraction layer matters.

At minimum, the query layer should:

- always filter on `organisation_id`,
- include `workspace_id` when relevant,
- reject cross-tenant joins or implicit broad reads,
- require explicit product awareness on product-specific domain records.

## 10. Validation for tool execution

Almost every tool execution should validate:

- tool id and registry membership,
- product domain origin,
- user permission to execute the tool,
- current tenant/workspace,
- approval status for sensitive actions,
- execution environment policy,
- scope or exclusion rules for hacker actions.

## 11. Advantages and limitations summary

| Mechanism | Advantages | Limitations |
| --- | --- | --- |
| Service-layer checks | Clear and easy to maintain; good policy control | Relies on developer discipline |
| PostgreSQL RLS | Strong tenant enforcement at database layer | More operational complexity |
| Database roles | Simplifies least privilege | Still requires service-level checks |
| Composite identifiers | Prevents accidental cross-tenant mismatches | More query complexity |
| Background job validation | Prevents orphaned or mismatched jobs | Needs disciplined telemetry |

## 12. Final recommendation

Use a layered approach:

- service-layer authorisation as the primary control,
- PostgreSQL RLS or equivalent row constraints where beneficial,
- product-specific permission checks for cross-domain access,
- strong validation for background jobs and document access,
- explicit query templating for tenant and workspace scope.

This is the most practical secure model for the current team and product stage.
