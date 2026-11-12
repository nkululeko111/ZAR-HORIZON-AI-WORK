# Shared platform API specification

## 1. Purpose

This specification defines the shared platform API contract for identity, organisation management, workspaces, permissions, subscriptions, execution, approvals, documents, and integration management.

## 2. Authentication and identity endpoints

### GET /api/v1/auth/profile

Purpose:
- retrieve the authenticated user profile.

Product:
- shared platform.

Auth:
- required.

Permissions:
- any authenticated user.

Approval:
- none.

MVP priority:
- P0.

### GET /api/v1/organisations

Purpose:
- list organisations the user belongs to.

Auth:
- required.

### GET /api/v1/organisations/{organisationId}

Purpose:
- retrieve organisation details.

Auth:
- required.

Permissions:
- membership in organisation.

### POST /api/v1/organisations

Purpose:
- create an organisation.

Auth:
- required.

Permissions:
- platform or org-admin-level creation capability.

### PATCH /api/v1/organisations/{organisationId}

Purpose:
- update organisation information.

### GET /api/v1/organisations/{organisationId}/members

Purpose:
- list organisation members.

### POST /api/v1/organisations/{organisationId}/members/invitations

Purpose:
- invite a user to the organisation.

### PATCH /api/v1/organisations/{organisationId}/members/{membershipId}

Purpose:
- update membership status or role assignment.

### GET /api/v1/workspaces

Purpose:
- list workspaces available to the current user.

### POST /api/v1/workspaces

Purpose:
- create a workspace in an organisation.

### GET /api/v1/workspaces/{workspaceId}

Purpose:
- retrieve workspace details.

### PATCH /api/v1/workspaces/{workspaceId}

Purpose:
- update workspace metadata.

## 3. Roles and permissions endpoints

### GET /api/v1/roles

Purpose:
- list available roles for the active organisation.

### POST /api/v1/roles

Purpose:
- create a custom or organisation-specific role.

### GET /api/v1/permissions/effective

Purpose:
- retrieve effective permissions for the current user and workspace.

### PATCH /api/v1/memberships/{membershipId}/roles

Purpose:
- assign or update a role.

### GET /api/v1/products

Purpose:
- list available products.

### GET /api/v1/products/{productCode}/entitlements

Purpose:
- retrieve entitlement information for an organisation.

### GET /api/v1/products/{productCode}/subscription

Purpose:
- retrieve subscription status.

### GET /api/v1/products/{productCode}/usage

Purpose:
- retrieve product usage information.

## 4. Agent execution endpoints

### POST /api/v1/agent/requests

Purpose:
- submit a new agent request.

Product:
- shared platform with product-specific routing.

Auth:
- required.

Permissions:
- product entitlement and product role.

Approval:
- required for sensitive or high-risk actions.

MVP priority:
- P0.

### GET /api/v1/agent/requests/{requestId}

Purpose:
- retrieve execution request status.

### GET /api/v1/agent/requests/{requestId}/history

Purpose:
- retrieve execution history.

### GET /api/v1/agent/requests/{requestId}/details

Purpose:
- retrieve request details and current state.

### GET /api/v1/agent/requests/{requestId}/steps

Purpose:
- retrieve execution steps.

### POST /api/v1/agent/requests/{requestId}/cancel

Purpose:
- cancel a supported in-flight execution.

### GET /api/v1/agent/requests/{requestId}/results

Purpose:
- retrieve execution result data.

## 5. Approval endpoints

### GET /api/v1/approvals/pending

Purpose:
- retrieve current pending approvals for the user.

### GET /api/v1/approvals/{approvalId}

Purpose:
- retrieve approval details.

### POST /api/v1/approvals/{approvalId}/approve

Purpose:
- approve a proposed action.

### POST /api/v1/approvals/{approvalId}/reject

Purpose:
- reject an action.

### POST /api/v1/approvals/{approvalId}/cancel

Purpose:
- cancel a pending approval if permitted.

### GET /api/v1/approvals/{approvalId}/history

Purpose:
- retrieve approval history.

Key rule:
- every approval record must bind to the exact action payload, tenant, workspace, product, and relevant scope.

## 6. Documents and evidence endpoints

### POST /api/v1/documents

Purpose:
- upload a document.

### GET /api/v1/documents/{documentId}

Purpose:
- retrieve a document.

### GET /api/v1/documents

Purpose:
- list documents.

### GET /api/v1/evidence/{evidenceId}

Purpose:
- retrieve evidence metadata.

### GET /api/v1/evidence/references

Purpose:
- list evidence references for a resource.

### GET /api/v1/evidence/{evidenceId}/download

Purpose:
- retrieve evidence payload or artifact, subject to access control.

Security note:
- security evidence endpoints must be restricted to authorised users and services.

## 7. Notifications and integrations endpoints

### GET /api/v1/notifications

Purpose:
- list notifications.

### PATCH /api/v1/notifications/{notificationId}/read

Purpose:
- mark notification as read.

### GET /api/v1/integrations

Purpose:
- list connected integrations.

### POST /api/v1/integrations/connect

Purpose:
- begin a secure integration connection flow.

### GET /api/v1/integrations/{integrationId}

Purpose:
- retrieve integration status and metadata.

### DELETE /api/v1/integrations/{integrationId}

Purpose:
- disconnect an integration.

### POST /api/v1/webhooks/{provider}/events

Purpose:
- receive provider webhooks.

Security note:
- webhook endpoints must be authenticated or signed and should verify replay protection and event deduplication.

## 8. Endpoint reference table

| Endpoint | Method | Product | Purpose | Auth | Permission | Approval | MVP |
| --- | --- | --- | --- | --- | --- | --- | --- |
| /api/v1/auth/profile | GET | Shared | User profile | Required | Authenticated user | No | P0 |
| /api/v1/organisations | GET/POST | Shared | Org management | Required | Org access | No | P0 |
| /api/v1/workspaces | GET/POST | Shared | Workspace management | Required | Workspace access | No | P0 |
| /api/v1/roles | GET | Shared | Roles | Required | Org admin / policy | No | P1 |
| /api/v1/products/{productCode}/entitlements | GET | Shared | Entitlements | Required | Product access | No | P0 |
| /api/v1/agent/requests | POST | Shared | Agent task submission | Required | Product entitlement | Conditional | P0 |
| /api/v1/agent/requests/{requestId} | GET | Shared | Status | Required | Task access | No | P0 |
| /api/v1/approvals/pending | GET | Shared | Pending approvals | Required | Approval access | No | P0 |
| /api/v1/approvals/{approvalId}/approve | POST | Shared | Approval decision | Required | Approval authority | N/A | P0 |
| /api/v1/documents | POST/GET | Shared | Document lifecycle | Required | Document access | Conditional | P0 |
| /api/v1/evidence/{evidenceId} | GET | Shared | Evidence metadata | Required | Evidence permissions | No | P0 |
| /api/v1/notifications | GET | Shared | Notification list | Required | User access | No | P1 |
| /api/v1/integrations | GET/POST | Shared | Connection management | Required | Integration permissions | Conditional | P1 |

## 9. Notes

- This is a platform-facing API contract and not a product-specific implementation.
- Product-specific APIs are defined separately.
- The platform API must be designed to allow both Business Partner and AI Hacker to coexist while preserving separate tool and permission scopes.
