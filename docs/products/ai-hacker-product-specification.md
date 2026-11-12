# AI Hacker Product Specification

## 1. Product overview

The AI Hacker is an AI-powered red-team digital employee designed to investigate, test, and validate the security of authorised systems before malicious actors can exploit weaknesses.

It is not a simple vulnerability scanner. It is intended to behave like an ethical offensive security specialist that can:

- investigate target environments,
- perform authorised reconnaissance,
- identify attack surfaces,
- validate vulnerabilities,
- understand probable attack paths,
- assess the impact and exploitability of weaknesses,
- guide remediation,
- retest after remediation,
- report evidence clearly and responsibly.

The product must operate only within explicit customer-authorised scope and governed execution boundaries.

## 2. Vision and positioning

Official positioning: "An AI red team that tests your systems before criminals do."

The product is designed for organisations that need proactive, authorised testing of digital infrastructure, applications, and cloud/security posture. Initial focus is on South African organisations, with expansion to broader enterprise and SME markets later.

The AI Hacker must support technical security teams and business stakeholders with a disciplined security validation workflow, not passive reporting.

## 3. Target customers

Primary customers:

- small businesses,
- startups,
- software development companies,
- IT departments,
- technology companies,
- enterprises.

Initial priority:

- South African organisations.

## 4. Customer problems

Security teams and organisations face ongoing challenges:

- incomplete asset visibility,
- outdated or misconfigured systems,
- difficult-to-prioritise vulnerabilities,
- weak validation of potential weaknesses,
- limited internal red-team capacity,
- uncertainty about real exploitability and business impact,
- need for evidence-backed remediation guidance.

The AI Hacker addresses these problems by supporting authorised, structured, and evidence-driven security testing.

## 5. Core capability domains

### A. Reconnaissance and asset discovery

The agent must support authorised reconnaissance by:

- discovering in-scope domains,
- enumerating subdomains,
- identifying network assets,
- discovering services,
- fingerprinting technology stacks,
- mapping the attack surface.

This should be performed only within explicitly defined assessment scope.

### B. Vulnerability discovery

The agent must support vulnerability detection in:

- outdated software and versions,
- system misconfiguration,
- exposed credentials or secrets,
- authentication weaknesses,
- access control problems,
- web application weaknesses,
- API security issues,
- cloud configuration concerns.

This includes both direct detection and supporting evidence gathering.

### C. Offensive security testing

The agent must eventually be capable of:

- validating vulnerabilities,
- performing controlled exploitation,
- testing privilege boundaries,
- investigating attack paths,
- assessing security controls,
- validating proof-of-concept impact under authorised conditions.

These activities must remain tightly scoped and controlled.

### D. Security intelligence

The agent must correlate findings into usable intelligence by:

- linking related weaknesses,
- identifying possible attack chains,
- separating false positives from validated findings,
- evaluating exploitability,
- assessing technical and business impact,
- prioritising remediation.

### E. Remediation and verification

The agent must support:

- generation of security reports,
- technical remediation guidance,
- proposed code and configuration fixes,
- tracking vulnerability status,
- retesting after remediation,
- verifying whether the issue has been resolved.

## 6. Execution philosophy

The AI Hacker must not simply run scanners and produce a list of CVEs.

It must investigate, validate, and determine whether a finding is a genuine risk. It must behave like an ethical security operator that can understand targets, use specialised tooling, and provide evidence for conclusions.

The product must differentiate between:

- detected potential issues,
- validated vulnerabilities,
- confirmed exploitability,
- false positives,
- remediated findings.

## 7. Representative assessment workflow

### Example: authorised review of a web application

1. Scope confirmation
   - confirm the target domain, application, and in-scope systems,
   - confirm test boundaries and approval for any intrusive testing.

2. Reconnaissance
   - enumerate subdomains and services,
   - identify technologies and exposed assets,
   - map the application attack surface.

3. Vulnerability discovery
   - inspect weak configurations,
   - identify outdated dependencies,
   - assess authentication and access-control risks,
   - review common web application weaknesses.

4. Validation
   - confirm which findings are reproducible,
   - validate whether they are exploitable,
   - distinguish real vulnerabilities from noise.

5. Impact assessment
   - determine business and technical risk,
   - identify possible lateral movement or privilege escalation paths,
   - assess remediation urgency.

6. Remediation guidance
   - document technical fixes,
   - provide operator guidance,
   - propose validation steps after remediation.

7. Retesting
   - verify that the issue has been addressed,
   - confirm whether the weakness remains exploitable.

8. Reporting
   - provide evidence-backed results,
   - include risk ratings,
   - document validation and retest status.

This workflow must be controlled, evidence-rich, and scoped to approved targets.

## 8. Security tool requirements

The product must eventually be able to use a set of specialised tools for authorised security work, including:

- network and service discovery tools,
- reconnaissance tooling,
- web application test tools,
- API testing tools,
- cloud posture and configuration analysis tools,
- credential and secret scanning tools,
- vulnerability validation utilities,
- reporting and evidence collection tools.

Tools must be deployed in secure, constrained environments and used only under explicit customer and organisational authorisation.

## 9. Execution environment requirements

The AI Hacker must run in an isolated, controlled environment designed for security testing, including:

- environment isolation,
- explicit target boundaries,
- audit logging,
- evidence retention,
- restricted outbound behaviour,
- sandboxing or controlled execution contexts where required,
- separation from business operations and normal production workloads.

This is essential to prevent accidental collateral impact and to preserve a clear chain of evidence.

## 10. Authorisation and scope controls

The AI Hacker must require:

- explicit target authorisation,
- defined assessment scope,
- permission levels for the test environment,
- approval for intrusive or high-risk activity,
- clear boundaries for destructive or out-of-scope actions,
- human review for high-risk assessments.

The following are mandatory controls:

- authorised target list,
- scope definitions,
- execution approval records,
- audit logs,
- evidence management,
- data handling rules,
- restrictions on destructive actions,
- prohibition of testing outside approved systems.

## 11. Evidence and reporting requirements

The product must distinguish among:

- detected potential vulnerabilities,
- validated vulnerabilities,
- successfully demonstrated security impact,
- unverified findings,
- remediated findings.

For every finding, the product must document:

- the target,
- the method used,
- the evidence collected,
- whether it was validated,
- the likely impact,
- the recommended remediation,
- the retest status.

The product must maintain execution records so that it can explain what it did and why it concluded a finding was valid or not.

## 12. Remediation and retesting

The AI Hacker must support a full remediation cycle:

- identify issues,
- produce technical remediation guidance,
- propose code, configuration, or policy fixes,
- track vulnerability resolution status,
- retest after remediation,
- verify whether weakness remains unresolved.

This closes the loop between discovery and resolution and ensures findings are not treated as static alerts without follow-through.

## 13. Product boundaries

The AI Hacker is a security testing specialist. It does not become a general business execution engine and must not inherit financial or commercial execution permissions from the Business Partner.

It must not:

- operate outside authorised targets,
- perform destructive or indiscriminate activity,
- test unsupported systems,
- conduct out-of-scope intrusion,
- operate without evidence tracking and approval controls.

This product is intentionally independent from the Business Partner’s capabilities.

## 14. Future expansion opportunities

Future capabilities may include:

- more advanced cloud security assessments,
- deeper API and application testing workflows,
- automated validation of remediation,
- richer attack-path intelligence,
- cross-environment security correlation,
- wider integration with security tooling and triage systems.

These are future growth opportunities and must not be confused with current implementation commitments.

## 15. Summary

The AI Hacker is an authorised offensive security assistant designed to validate weaknesses before criminals can exploit them. It must be capable of structured investigation, evidence-backed evaluation, controlled testing, and remediation guidance within strong approval and scope controls. It must remain operationally disciplined, audit-friendly, and separated from business execution authority.
