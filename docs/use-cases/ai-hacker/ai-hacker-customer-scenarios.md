# AI Hacker Customer Scenarios

## 1. Purpose

This document provides illustrative scenarios for the AI Hacker. These are not real customer case studies or interviews. They are realistic examples of how the product could operate within its approved scope and according to the founder-approved security vision.

## 2. Scenario 1: South African SaaS startup

### Customer situation

A South African SaaS startup has a customer-facing web application and a public API. It is growing quickly and does not yet have a dedicated internal security team.

### Security problem

The company needs to review the application and APIs before scaling further, but cannot support a full-time red-team process.

### What the AI Hacker investigates

- app attack surface,
- authentication and session handling,
- access control weaknesses,
- API security posture,
- exposed configuration and dependency risk.

### What it actually tests

- login flow and access paths,
- role-based access boundaries,
- sensitive API endpoints,
- configuration and misconfiguration issues,
- obvious high-risk issues in a controlled environment.

### Evidence it collects

- request and response evidence,
- role access testing results,
- version and misconfiguration findings,
- technical reproduction notes.

### What it reports

- a summary of confirmed issues,
- risk prioritisation,
- remediation steps,
- retest plan.

### How it helps resolve the issue

- identifies the security defects that matter most,
- helps engineering teams prioritise fixes,
- supports retesting after remediation.

### How the result is verified

- findings are confirmed against the authorised environment,
- fixes are retested before closure.

## 3. Scenario 2: Software development company

### Customer situation

A software company builds customer-facing systems and is preparing a new production release.

### Security problem

The team wants a faster pre-release assessment to catch common web and API vulnerabilities before launch.

### What the AI Hacker investigates

- application-layer weaknesses,
- authentication boundaries,
- API access and input validation,
- configuration posture,
- business logic risk in release features.

### What it actually tests

- app and API routes,
- privileged versus non-privileged flows,
- security headers and transport configuration,
- common input-validation weaknesses.

### Evidence it collects

- technical reproduction proof,
- issue classification,
- developer-facing description of each issue.

### What it reports

- high-priority weaknesses,
- vulnerability validation status,
- risk and remediation list.

### How it helps resolve the issue

- reduces release risk,
- identifies issues before launch,
- supports retest after fix.

### How the result is verified

- through retest after remediation and evidence-backed final status.

## 4. Scenario 3: MSP or IT services provider

### Customer situation

An MSP wants to offer recurring security validation to its clients without needing a large internal red-team team.

### Security problem

The provider needs a repeatable security-assessment workflow that can be delivered consistently across client environments.

### What the AI Hacker investigates

- client asset exposure,
- externally visible services,
- configuration weaknesses,
- client security reporting requirements.

### What it actually tests

- authorised client assets,
- infrastructure and app exposure,
- configuration review and security posture,
- approved remediation support.

### Evidence it collects

- asset inventory,
- client-specific vulnerability evidence,
- business impact notes,
- a repeatable reporting format.

### What it reports

- client-facing executive summary,
- technical findings,
- remediation priority matrix,
- retest status.

### How it helps resolve the issue

- provides standardised assessment and reporting,
- supports recurring client services,
- helps MSP teams allocate remediation priorities.

### How the result is verified

- retesting after remediation confirms issue closure.

## 5. Scenario 4: E-commerce platform

### Customer situation

A growing e-commerce business handles transactions and customer records and needs to understand exposure around web and API surfaces.

### Security problem

The business is concerned about payment-related exposure, customer data, and the security of customer-facing endpoints.

### What the AI Hacker investigates

- public-facing platform exposure,
- web app security weaknesses,
- API authentication and access control,
- customer-facing data handling.

### What it actually tests

- authentication flow,
- session handling,
- access boundaries,
- sensitive data exposure,
- web and API misconfiguration.

### Evidence it collects

- request/response traces,
- access-control validation evidence,
- configuration and exposure notes.

### What it reports

- risk summary,
- high-priority issues,
- remediation recommendations,
- retest plan.

### How it helps resolve the issue

- reduces uncertainty around customer-facing exposure,
- gives the business a defensible security review.

### How the result is verified

- by retesting after remediation and documenting final status.

## 6. Scenario 5: Small business with customer portal

### Customer situation

A small business runs a customer portal and allows account access for customers to manage services or ordering.

### Security problem

The business is concerned that the portal may have weak authorisation or session controls but does not have a security team to assess it.

### What the AI Hacker investigates

- login flow,
- identity boundaries,
- authorisation and role checks,
- portal configuration,
- account security posture.

### What it actually tests

- authentication strength,
- session security,
- access control patterns,
- account privilege separation.

### Evidence it collects

- role and privilege evidence,
- repeated access-control findings,
- reproduction details where relevant.

### What it reports

- portal security status,
- key weaknesses,
- customer-impact summary,
- remediation guidance.

### How it helps resolve the issue

- helps the business prioritise security improvement,
- reduces risk before customer or data exposure grows.

### How the result is verified

- the issue is retested after remediation and marked as fixed or unresolved.

## 7. Scenario 6: Fintech startup

### Customer situation

A fintech startup builds a customer-facing platform and manages transaction workflows and identity processes.

### Security problem

The company needs a structured assessment of authentication, permissions, and API security because the business is highly sensitive to risk and trust.

### What the AI Hacker investigates

- auth and session security,
- role boundaries,
- permission design,
- API access controls,
- transaction workflow assumptions.

### What it actually tests

- auth and role boundaries,
- data exposure,
- API access control weaknesses,
- sensitive business logic conditions.

### Evidence it collects

- request traces,
- privilege boundary evidence,
- impact notes,
- technical reproduction evidence.

### What it reports

- executive summary,
- technical findings,
- remediation priorities,
- retest and closure status.

### How it helps resolve the issue

- supports technical risk reduction,
- helps leadership understand which gaps matter most.

### How the result is verified

- through trusted retests and clear issue-status changes.

## 8. Scenario 7: Cloud-hosted application

### Customer situation

A company runs a cloud-hosted application with storage, identity, and internet-facing services.

### Security problem

The team wants to determine whether identity permissions, cloud exposure, and configuration are creating unnecessary risk.

### What the AI Hacker investigates

- cloud asset inventory,
- IAM and permission posture,
- storage and public exposure,
- configuration weaknesses,
- secret exposure risk.

### What it actually tests

- cloud permission structure,
- public exposure and resource configuration,
- secret handling and visibility,
- service exposure and misconfiguration.

### Evidence it collects

- cloud configuration evidence,
- role and permission findings,
- security posture assessment notes.

### What it reports

- key cloud risks,
- recommended configuration changes,
- exposure summary.

### How it helps resolve the issue

- gives the team a prioritised view of cloud risks,
- supports remediation and retest.

### How the result is verified

- by confirming the configuration changed and the risky condition no longer exists.

## 9. Scenario 8: Company preparing for a major product release

### Customer situation

A digital company is preparing a significant product release and needs a final security check before launch.

### Security problem

The company needs assurance that high-risk issues have been validated and addressed before the release goes live.

### What the AI Hacker investigates

- app and API surface,
- key workflows,
- access controls,
- high-risk configuration weaknesses,
- critical dependencies.

### What it actually tests

- security-critical routes and flows,
- auth and authorisation boundaries,
- exposure and configuration weaknesses,
- product launch risk points.

### Evidence it collects

- issue evidence,
- high-risk findings list,
- retest results,
- business risk priority.

### What it reports

- pre-release security status,
- critical issues requiring action,
- list of issues cleared or requiring deeper follow-up.

### How it helps resolve the issue

- reduces launch risk,
- creates a defensible pre-release security position,
- supports final fix verification before release.

### How the result is verified

- through the final retest and evidence record.

## 10. Scenario 9: Organisation responding to a suspected weakness

### Customer situation

A business suspects a security weakness but is not sure whether it is a real issue or a false alarm.

### Security problem

The team needs a controlled investigation to determine whether a vulnerability is valid and whether it matters operationally.

### What the AI Hacker investigates

- the suspected route, system, or configuration,
- relevant exposure and risk conditions,
- evidence required to confirm or disprove the issue.

### What it actually tests

- the suspected weak condition under controlled validation,
- whether the issue is real and relevant,
- the scope and impact of the risk.

### Evidence it collects

- reproduction logs,
- technical evidence,
- business impact assessment,
- classification status.

### What it reports

- whether the issue is confirmed, suspected, or false positive,
- next actions required.

### How it helps resolve the issue

- reduces uncertainty,
- allows effective triage and remediation decisions.

### How the result is verified

- by confirming or disproving the issue based on evidence and retest if necessary.

## 11. Scenario 10: Organisation requiring remediation verification

### Customer situation

A business has already received an assessment and needs to confirm that fixes were successful.

### Security problem

The organisation does not want to rely on a developer claim that an issue is fixed without evidence.

### What the AI Hacker investigates

- the original issues,
- the implemented fix path,
- the environment after remediation.

### What it actually tests

- the previously vulnerable controls,
- the changed configuration,
- the resolution of the original issue and side effects.

### Evidence it collects

- retest results,
- confirmation that the vulnerability no longer reproduces,
- updated risk status.

### What it reports

- final finding status,
- the remediation verification result,
- any remaining issues or follow-up work.

### How it helps resolve the issue

- creates a trusted validation loop,
- provides evidence that the issue has been addressed.

### How the result is verified

- through direct retest results and final status classification.

## 12. Summary

These scenarios show how the AI Hacker is expected to work in practice: investigate within scope, validate findings with evidence, prioritise risk, support remediation, and verify the fix before the issue is considered closed.
