# OpenAPI and type contract strategy

## 1. Purpose

This document recommends how API specifications and tool contracts should be represented as the platform matures. The goal is to keep frontend, backend, and tool contracts consistent while preserving version compatibility.

## 2. Recommended representation

### OpenAPI

The long-term API contract should be represented in OpenAPI 3.x. This provides:

- machine-readable API definitions,
- generated clients,
- generated docs,
- contract validation,
- backend and frontend alignment.

### Pydantic models

Pydantic models may be used on the Python API server side for request and response validation, but the design work in this repository is intentionally documentation-only and does not define actual models.

### Shared TypeScript types

The frontend should rely on a shared TypeScript contract layer derived from the API schema. This keeps the UI aligned with the backend contract and reduces drift.

## 3. Contract principles

- API contracts should be authored once and reused by backend and frontend teams.
- Request and response payloads should be versioned explicitly.
- Tool schemas should be validated against policy metadata and approval rules.
- Security-sensitive objects should be represented with explicit access semantics.
- Idempotency and correlation IDs should be part of the contract where applicable.

## 4. Tool schema strategy

Agent tools should have a schema or contract definition separate from the API resource schema. The tool registry should validate:

- required fields,
- permissions,
- tenant context,
- product scope,
- approval requirements,
- evidence requirements,
- output shape,
- rate-limit context.

## 5. Contract validation

The system should validate contracts at multiple layers:

- runtime validation in API handlers,
- schema validation in upstream service layers,
- tool validation before execution,
- approval validation before sensitive side effects,
- compatibility checks when versioning changes.

## 6. API version compatibility

Versioning should be explicit:

- `/api/v1/...` for the initial public API,
- new breaking changes only in a new version,
- deprecations communicated in advance,
- compatibility windows for old clients.

The platform should avoid silent field removal or schema drift.

## 7. Frontend and backend consistency

The frontend and backend should agree on:

- naming conventions,
- auth patterns,
- error shapes,
- pagination contract,
- correlation IDs,
- status enums,
- tool invocation metadata.

This reduces accidental divergence and keeps the platform design coherent.

## 8. Summary

The recommended approach is a shared OpenAPI contract, with TypeScript and backend validation layers aligned to the same canonical API definitions. This approach supports versioning, contract validation, and safe evolution without inventing a runtime implementation.
