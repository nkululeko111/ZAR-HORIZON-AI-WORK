# AI Hacker API specification

## 1. Purpose

This specification defines the API contract for the AI Hacker product. It supports the authorised security assessment workflow: onboarding → authorisation → scope → planning → permitted testing → investigation → validation → evidence → report → remediation → retest.

The API must not expose unrestricted command execution or arbitrary security tool execution.

## 2. Customer and asset management endpoints

### POST /api/v1/security/customers

Purpose:
- register a security customer.

Product:
- AI Hacker.

Auth:
- required.

Permissions:
- organisation admin or security admin role.

Approval:
- no for onboarding; required for active assessment work.

MVP priority:
- P0.

### GET /api/v1/security/customers/{customerId}

Purpose:
- retrieve a customer record.

### POST /api/v1/security/assets

Purpose:
- register an asset.

### GET /api/v1/security/assets

Purpose:
- list assets under the organisation and authorised scope.

### GET /api/v1/security/assets/{assetId}

Purpose:
- retrieve a specific asset.

### PATCH /api/v1/security/assets/{assetId}

Purpose:
- update asset metadata.

## 3. Authorisation and scope endpoints

### POST /api/v1/security/authorisations

Purpose:
- create an authorisation record.

### GET /api/v1/security/authorisations/{authorisationId}

Purpose:
- retrieve authorisation details.

### POST /api/v1/security/scopes

Purpose:
- define an assessment scope.

### POST /api/v1/security/scopes/{scopeId}/inclusions

Purpose:
- add approved targets.

### POST /api/v1/security/scopes/{scopeId}/exclusions

Purpose:
- define excluded targets or domains.

### POST /api/v1/security/scopes/{scopeId}/restrictions

Purpose:
- add test restrictions and stop conditions.

### POST /api/v1/security/scopes/{scopeId}/windows

Purpose:
- define authorised test windows.

### GET /api/v1/security/assets/{assetId}/authorisation

Purpose:
- validate whether an asset is authorised for assessment.

## 4. Assessment management endpoints

### POST /api/v1/security/assessments

Purpose:
- create a new assessment.

### GET /api/v1/security/assessments/{assessmentId}

Purpose:
- retrieve assessment details.

### POST /api/v1/security/assessments/{assessmentId}/submit

Purpose:
- submit an assessment for execution.

### GET /api/v1/security/assessments/{assessmentId}/status

Purpose:
- retrieve the current assessment status.

### POST /api/v1/security/assessments/{assessmentId}/cancel

Purpose:
- cancel an active assessment when permitted.

### GET /api/v1/security/assessments/{assessmentId}/history

Purpose:
- retrieve assessment history.

## 5. Findings and evidence endpoints

### GET /api/v1/security/findings

Purpose:
- list findings for a customer or assessment.

### GET /api/v1/security/findings/{findingId}

Purpose:
- retrieve detailed finding metadata.

### GET /api/v1/security/findings/{findingId}/evidence

Purpose:
- retrieve all evidence attached to a finding.

### GET /api/v1/security/findings/{findingId}/validation

Purpose:
- retrieve validation status and rationale.

### PATCH /api/v1/security/findings/{findingId}/status

Purpose:
- update status through an authorised workflow.

Approval note:
- status changes that affect severity, rejection, or validation state require explicit human approval and risk review.

## 6. Remediation and retesting endpoints

### POST /api/v1/security/remediation

Purpose:
- create a remediation record.

### GET /api/v1/security/remediation/{remediationId}

Purpose:
- retrieve remediation guidance and status.

### POST /api/v1/security/remediation/{remediationId}/retest

Purpose:
- request retest or verification.

### GET /api/v1/security/retests/{retestId}

Purpose:
- retrieve retest results.

### GET /api/v1/security/assessments/{assessmentId}/report

Purpose:
- retrieve final assessment report.

## 7. Approval requirements

The following require explicit approval beyond merely selecting a UI option:

- any active assessment execution outside the authorised scope,
- any change to scope or exclusions,
- any test involving privileged or administrative credentials,
- any web or API testing beyond the approved test window,
- any high-risk security technique,
- any status change that affects the confidence or severity classification of a finding.

## 8. Endpoint reference table

| Endpoint | Method | Purpose | Auth | Permission | Approval | MVP |
| --- | --- | --- | --- | --- | --- | --- |
| /api/v1/security/customers | POST/GET | Customer management | Required | Security admin access | No | P0 |
| /api/v1/security/assets | POST/GET | Asset inventory | Required | Security access | No | P0 |
| /api/v1/security/authorisations | POST/GET | Authorisation records | Required | Security admin access | No | P0 |
| /api/v1/security/scopes | POST | Scope management | Required | Security admin access | Conditional | P0 |
| /api/v1/security/assessments | POST/GET | Assessment lifecycle | Required | Security access + authorisation | Conditional | P0 |
| /api/v1/security/assessments/{assessmentId}/submit | POST | Start execution | Required | Security access | Yes | P0 |
| /api/v1/security/findings | GET | Finding list | Required | Security access | No | P0 |
| /api/v1/security/findings/{findingId}/evidence | GET | Evidence retrieval | Required | Security access + evidence permission | No | P0 |
| /api/v1/security/remediation | POST/GET | Remediation lifecycle | Required | Security access | Conditional | P0 |
| /api/v1/security/retests/{retestId} | GET/POST | Retest execution and status | Required | Security access | Conditional | P0 |
| /api/v1/security/assessments/{assessmentId}/report | GET | Final report | Required | Security access | No | P0 |

## 9. Important constraints

- There is no unrestricted endpoint for arbitrary security tools or shell execution.
- Active security testing must remain within approved scope and environment.
- Evidence, findings, and remediation records must preserve validation status and provenance.
- This specification is an API design contract, not an implementation or live service.
