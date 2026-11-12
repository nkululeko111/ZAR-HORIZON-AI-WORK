# AI Hacker testing

## 1. Purpose

The AI Hacker domain requires a separate, security-first test strategy. This domain must prove it cannot exceed its approved scope, cannot operate outside explicit authorisation, and cannot perform high-risk actions without controlled review and evidence capture.

## 2. Mandatory assurance principles

- The system must require explicit authorisation and defined scope.
- The system must enforce product permission boundaries.
- Tool access must be limited and auditable.
- High-risk actions require clear approval and evidence.
- Negative tests must prove the system refuses out-of-scope actions.
- Execution must be isolated and recorded.

## 3. Test domains

### Authorisation and scope

Tests should verify:

- missing or invalid authorisation is rejected,
- target scope is enforced,
- excluded systems are blocked,
- approval requirements are enforced before sensitive action,
- changed parameters require re-approval,
- revoked permissions are respected.

### Execution isolation and controls

Tests should verify:

- no unrestricted network execution,
- no unapproved shell access,
- no direct access to protected internal infrastructure,
- no permission leakage across product domains,
- no action execution without execution-environment isolation.

### Evidence and reporting

Tests should verify:

- evidence is captured for every material execution,
- findings cite the underlying evidence,
- confidence levels are explicit,
- false positives and uncertainty are documented,
- finding and remediation status are traceable.

## 4. Negative testing

The AI Hacker must include negative tests proving it refuses to:

- perform actions outside approved scope,
- access systems outside the target list,
- bypass approval or policy checks,
- execute destructive commands or unsafe actions,
- elevate privileges without approval,
- operate beyond the configured test window.

## 5. Controlled future fixtures

The project should plan for future controlled test fixtures such as:

- intentionally vulnerable applications,
- isolated internal targets,
- mock network services,
- evidence-capture validation environments,
- known-bad and known-good finding examples.

These fixtures must remain isolated and should never be run against external public systems.

## 6. Security-scope discipline

This repository does not authorise real scanning, exploitation, external-target probing, or intrusive security testing. The testing strategy is therefore design-oriented and evidence-driven, not adversarial against live production systems.
