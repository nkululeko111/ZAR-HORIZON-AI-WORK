# Product data isolation and access matrix

## 1. Purpose

This document defines who may access each core data domain and whether the other product may access it. The platform must treat the Business Partner and AI Hacker as separate product data domains with different permissions and access authority.

## 2. Data access matrix

| Data domain | Owning product or platform | Tenant-owned | Workspace-owned | Permitted access | Other product may access? | Sensitivity | Retention guidance |
| --- | --- | --- | --- | --- | --- | --- | --- |
| User identity | Platform | Yes | Optional | Platform users, org admin, authorised service accounts | No | High | Standard account lifecycle |
| Organisation | Platform | Yes | No | Org admins, platform operators | No | High | Tenant lifecycle |
| Workspace | Platform | Yes | Yes | Org members with workspace access | No | Medium | Tenant lifecycle |
| Memberships | Platform | Yes | Optional | Org admins, platform auth service | No | Medium | While membership active |
| Roles and permissions | Platform | Yes | Optional | Org admins, product policy engine | No | Medium | Until role removal |
| Product entitlement | Platform | Yes | No | Platform billing and policy engine | No | Medium | Subscription lifecycle |
| Subscription records | Platform | Yes | No | Platform billing and admin | No | Medium | Subscription lifecycle |
| Usage records | Platform | Yes | Optional | Product policy engine, platform ops | No | Medium | Policy-driven retention |
| Business profile | Business Partner | Yes | Yes | Business Partner users with workspace access | No | High | Tenant-defined retention |
| Financial records | Business Partner | Yes | Yes | Business Partner users with explicit entitlement | No | High | Tenant-defined retention |
| Customer and supplier records | Business Partner | Yes | Yes | Business Partner users with access | No | High | Tenant-defined retention |
| Tasks and follow-up records | Business Partner | Yes | Yes | Business Partner users | No | Medium | Tenant-defined retention |
| Quotations and documents | Business Partner | Yes | Yes | Business Partner users, approved service jobs | No | Medium | Tenant-defined retention |
| Recommendations and actions | Business Partner | Yes | Yes | Business Partner orchestrator and authorised users | No | Medium | Task lifecycle |
| Security customer | AI Hacker | Yes | Yes | AI Hacker admins and authorised users | No | High | Engagement lifecycle |
| Assets and applications | AI Hacker | Yes | Yes | Approved security users and service jobs | No | High | Assessment lifecycle |
| Authorisations and scope | AI Hacker | Yes | Yes | Security admins and policy engine | No | High | Engagement lifecycle |
| Assessment plans and runs | AI Hacker | Yes | Yes | Assessment operators and worker services | No | High | Assessment retention |
| Findings and severity | AI Hacker | Yes | Yes | Approved security reviewers and stakeholders | No | High | Security evidence retention |
| Evidence records | AI Hacker | Yes | Yes | Approved security users and evidence service | No | High | Security evidence retention |
| Remediation and retest | AI Hacker | Yes | Yes | Security team and customer user roles | No | High | Assessment lifecycle |
| Audit events | Platform | Yes | Optional | Platform ops and compliance review | No | High | Compliance retention |
| Notification records | Platform | Yes | Optional | Organisation users, system service | No | Medium | Platform policy |
| Integration configs | Platform | Yes | Optional | Platform ops, product integration services | No | High | Integration lifecycle |
| Secret refs only | Platform | Yes | Optional | Secret manager and service credentials | No | Critical | Rotation and expiry |
| Temporary execution data | Platform / execution boundary | Yes | Yes | Job or execution service | No | High | Short retention and cleanup |

## 3. Explicit prohibitions

The following must be prohibited:

- Business Partner accessing AI Hacker credentials
- AI Hacker accessing Business Partner financial information
- access to other organisations' records by user or job context
- tool invocation escaping product permission sets
- any background job reading tenant data without the correct tenant context

## 4. Access model rules

1. Product permission is evaluated by product code and workspace scope.
2. User access is always validated against organisation membership and role assignment.
3. Shared identity does not imply shared availability of all product data.
4. Secrets are never read as ordinary application data.
5. Background jobs must include tenant, organisation, workspace, and product metadata.
6. Execution records must retain both the actor and the execution boundary used.

## 5. Sensitivity classification

- Critical: secrets, security credentials, exploit evidence, sensitive audit material
- High: financial records, customer identity data, security findings, evidence files
- Medium: workspaces, tasks, notifications, operational data
- Low: non-sensitive configuration and reporting metadata

## 6. Retention requirements summary

- Platform user and tenant records: standard platform lifecycle
- Business Partner financial and customer data: tenant-defined business retention
- AI Hacker findings and evidence: security evidence retention and review policy
- Temporary execution data: short retention with automated cleanup
- Integration credentials: rotation, expiry, and strict access control
- Audit events: longer-term compliance retention

## 7. Security note

No product may be given implicit access to the other product's data domain. Even when both products are served by the same database instance, the database must remain a shared platform utility, not a shared authority store.
