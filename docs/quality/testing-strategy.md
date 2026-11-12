# Testing strategy

## 1. Purpose

This document defines the quality-assurance strategy for ZAR HORIZON AI @WORK. It is intentionally process-oriented and policy-led because the repository is still in a documented design and governance phase rather than a feature-implementation phase.

## 2. Testing principles

- Tests must protect the approved architecture, product boundaries, and security policies.
- The shared platform must enforce tenant, workspace, product, and approval boundaries.
- Business calculations must be deterministic and testable.
- AI Hacker tests must prove the system cannot exceed the approved scope.
- A passing result must be backed by an actual run using the repository’s available tooling.
- If a check cannot run, the result must be reported as unverified rather than assumed.

## 3. Layered testing model

### Unit testing

Unit tests should cover:

- financial and business calculations,
- permission and policy evaluation,
- API validation,
- schema and contract validation,
- tool contract generation and checking,
- data validation and sanitisation,
- basic business logic and edge cases.

### Integration testing

Integration tests should cover:

- API to database interaction,
- tenant and workspace enforcement,
- approval workflow execution,
- background job processing,
- document and evidence handling,
- external adapter interactions under mock or controlled conditions,
- AI provider adapter error handling.

### End-to-end testing

End-to-end test planning should cover:

- onboarding,
- organisation and workspace setup,
- Business Partner operational workflows,
- Hacker authorised assessment flows,
- approval and execution journeys,
- reporting and verification flows.

### Regression testing

Regression checks should protect:

- tenant separation,
- product boundary enforcement,
- financial arithmetic integrity,
- approval flow enforcement,
- security restrictions,
- API compatibility within the approved contract set.

A change should not be considered complete unless the relevant regression tests are either updated or deliberately scoped as not applicable.

## 4. Performance and reliability testing

The project should define performance and reliability measures for:

- API latency and throughput,
- long-running task execution,
- queue and background worker behaviour,
- database query latency,
- concurrency under multiple users and jobs,
- retries, timeouts, and fault handling,
- resource consumption during background security and business workflows.

The repository does not currently define approved performance targets, so the strategy focuses on measurement, evidence, and operational readiness rather than arbitrary thresholds.

## 5. Governance for test evidence

All tests should record:

- name and purpose,
- environment used,
- data or fixtures used,
- pass/fail result,
- failures and their cause,
- whether the scenario was automated or manual.

No test result should be reported as valid unless it was actually executed and observed.
