# API design standards

## 1. Purpose

This document defines the shared API design standards for the ZAR HORIZON AI @WORK platform, the Business Partner, and the AI Hacker product domains. It is a specification for future implementation, not an implemented API.

## 2. Core standards

### REST architecture

The platform should use RESTful resource-oriented endpoints with clear noun-based resource naming and standard HTTP semantics.

Use:
- `GET` for retrieval,
- `POST` for create or action execution,
- `PATCH` for partial update,
- `PUT` for full replacement when necessary,
- `DELETE` only when a delete workflow is explicitly supported.

### Base URL and versioning

The base URL should follow the pattern:

- `/api/v1/...`

This is appropriate for the existing stack and is consistent with the platform direction already reflected in the repo. It allows versioned evolution without breaking the stable API contract.

### Resource naming

Use lowercase resource names and nested resources that reflect hierarchy:

- `/api/v1/organisations/{organisationId}`
- `/api/v1/workspaces/{workspaceId}`
- `/api/v1/products/{productCode}`
- `/api/v1/agent/requests`
- `/api/v1/business/profile`
- `/api/v1/assessments/{assessmentId}`

Do not combine unrelated operations into a single endpoint.

### Request and response format

All API payloads should use JSON. Responses should be consistent and explicit:

- object payloads for resources,
- top-level metadata where needed,
- stable field names in snake_case or camelCase only if the entire platform intentionally chooses one pattern,
- explicit status on asynchronous tasks.

Recommended platform convention:
- JSON payloads use camelCase in the public API if frontend TypeScript is the main consumer,
- internal storage remains database-specific and not exposed directly.

## 3. JSON conventions

The API should include:

- an `id` field for resource identity,
- `createdAt` and `updatedAt` for lifecycle tracking,
- `tenantId` and `workspaceId` when relevant,
- `status` for multi-step or asynchronous flows,
- `meta` or `links` only when they are used consistently.

## 4. Pagination, filtering and sorting

Pagination should be explicit and consistent:

- `page` and `pageSize` or `limit`/`offset`
- `sortBy` and `sortOrder`
- filters via query parameters or structured filter payloads for POST endpoints.

Examples:
- `GET /api/v1/assessments?page=1&pageSize=25&status=running`
- `GET /api/v1/transactions?periodId=...&sortBy=date&sortOrder=desc`

## 5. Validation and errors

Validation errors should return a structured error body with:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "One or more fields are invalid.",
    "details": [
      {
        "field": "workspaceId",
        "message": "Workspace is required."
      }
    ],
    "requestId": "req_123",
    "status": 400
  }
}
```

Common error codes:
- `AUTH_REQUIRED`
- `FORBIDDEN`
- `TENANT_MISMATCH`
- `WORKSPACE_NOT_FOUND`
- `NOT_FOUND`
- `VALIDATION_ERROR`
- `RATE_LIMITED`
- `APPROVAL_REQUIRED`
- `EXECUTION_TIMEOUT`
- `TOOL_FORBIDDEN`
- `INTERNAL_ERROR`

Do not expose internal stack traces, secrets, or raw execution payloads.

## 6. Authentication and authorisation

### Authentication boundary

Authentication should be handled at the platform API boundary. It is not a product-level concern. The platform is responsible for establishing the authenticated principal and their active organisation and workspace context.

### Authorisation

The API must enforce:

- user authentication,
- organisation membership,
- workspace membership,
- product entitlement,
- product-specific permissions,
- tool permission checks,
- action approval checks,
- tenant and product separation.

## 7. Tenant context and workspace context

Every request must resolve:

- authenticated user,
- active organisation,
- active workspace,
- product context,
- effective permissions.

The API must reject requests when:

- the user is not in the organisation,
- the workspace does not belong to the organisation,
- the product entitlement is absent,
- the resource does not belong to the current tenant.

## 8. Product entitlements and rate limits

The API must check product entitlement before exposing product functionality. Rate limiting should be applied by:

- user,
- organisation,
- workspace,
- integration connection,
- tool or endpoint group.

## 9. Idempotency and request correlation

All state-changing operations should support idempotency keys or request IDs.

Required fields:
- `Idempotency-Key` header or request-level idempotency token,
- `X-Correlation-ID` or equivalent request ID,
- structured logs that allow tracing the request end-to-end.

## 10. API documentation

The API should eventually be represented using OpenAPI and linked to a public contract for frontend and backend teams. The contract should be versioned and kept in sync with implementation.

## 11. Security and sensitivity rules

The API must not expose:

- raw credentials,
- internal secrets,
- direct tool execution payloads for unapproved security tasks,
- evidence metadata unless the user has the required permissions,
- security findings or remediation data to unauthorised tenants.

## 12. Standard response envelope

For all responses, a standard envelope is useful for consistency:

```json
{
  "data": {},
  "meta": {
    "requestId": "req_123",
    "status": "success"
  }
}
```

Error responses should use the dedicated error structure shown above, not a raw exception payload.

## 13. MVP design principle

The initial API should prioritise an end-to-end workflow for each product over a broad list of experimental endpoints. That means the first release should support the MVP flows already documented in the product and use-case packages.

## 14. Summary

The recommended API standard is a versioned REST API under `/api/v1`, with strong tenant and product checks, structured error responses, idempotency, and explicit approval decisions for sensitive operations.
