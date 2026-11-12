# Quality and operational decision register

## Purpose

This register captures the quality, security, and deployment decisions defined during Day 14.

## Decision log

### Q-001: layered testing model adopted

Decision:
- Use unit, integration, end-to-end, regression, performance, and reliability tests.

Reason:
- the project needs process-level assurance across business logic, product security boundaries, and operational reliability.

### Q-002: Business Partner arithmetic must remain deterministic

Decision:
- LLM output must not be treated as the source of truth for financial arithmetic.

Reason:
- financial logic must be auditable and safe for business use.

### Q-003: AI Hacker requires negative and scope-enforcement testing

Decision:
- The AI Hacker must include negative tests proving out-of-scope actions are rejected.

Reason:
- security execution domains require explicit authorisation, evidence, and control validation.

### Q-004: shared platform must enforce back-end security

Decision:
- The backend is the security boundary; frontend restrictions are not sufficient.

Reason:
- tenant and product boundaries must be enforced consistently.

### Q-005: phased environments are preferred

Decision:
- Maintain local, automated test, staging, and production environment categories.

Reason:
- this supports a practical early-stage deployment model without premature infrastructure commitment.

### Q-006: backup, monitoring, and incident response are required as policy

Decision:
- define monitoring, backup, disaster recovery, and incident handling before production rollout.

Reason:
- this reduces operational risk and provides a clear path for future production governance.

## Outstanding decisions

- cloud provider and region,
- production hosting strategy,
- backup retention and RPO/RTO values,
- production monitoring budget,
- incident escalation authority and responsibilities.
