# Incident response plan

## 1. Purpose

This document defines a practical incident response pattern for ZAR HORIZON AI @WORK. It covers security, service, and operational incidents without assuming a production environment has already been approved.

## 2. Incident types

The plan covers:

- security incidents,
- suspected data exposure,
- credentials compromise,
- unauthorised AI action,
- Hacker scope violations,
- service outage,
- database corruption,
- AI provider failure,
- approval or policy enforcement failure.

## 3. Response phases

### Detection

- monitor for service degradation, policy violations, and suspicious access,
- capture logs and execution history,
- identify the affected tenant, workspace, or product domain.

### Containment

- block affected accounts or workflows where necessary,
- revoke or limit tokens and credentials,
- isolate impacted execution environments,
- suspend non-essential automated activity.

### Investigation

- establish what happened,
- identify affected data and systems,
- preserve evidence,
- determine whether the incident crosses tenant or product boundaries.

### Recovery

- restore only the necessary service or data set,
- verify permissions and evidence trails after recovery,
- re-run validation checks relevant to the incident.

### Communication

- notify the appropriate internal stakeholders,
- maintain a factual record of the event,
- define escalation paths for customer or regulator concerns where required.

### Review

- document root cause,
- identify corrective actions,
- update the policy, tooling, or controls that allowed the incident.

## 4. Critical principle

Any unauthorised AI or agent action must be treated as a serious security event. It must be isolated, investigated, and recorded with preservation of evidence.
