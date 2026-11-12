# AI Hacker architecture

## 1. Objective

The AI Hacker is a separate specialist security system designed for authorised security investigation and validation. It must act as a disciplined professional security workflow engine, not a generic or unbounded automation layer.

The architecture explicitly separates security domain logic from business operations and does not permit the Hacker to inherit Business Partner permissions.

## 2. Logical components

1. Customer and organisation onboarding
2. Asset registry
3. Authorisation management
4. Scope and exclusions manager
5. Assessment planning
6. Reconnaissance engine
7. Web application testing engine
8. API testing engine
9. Vulnerability investigation and validation
10. Evidence collection
11. Finding classification and confidence
12. Attack-path analysis
13. Remediation guidance
14. Retesting and verification
15. Security reporting

## 3. Component responsibilities

### Customer and organisation onboarding

Purpose:
- create the organisation security context,
- register authorised contacts and assessment owners,
- bind assets and scope to a valid customer organisation.

### Asset registry

Purpose:
- maintain the list of in-scope assets,
- map domains, services, APIs, and assets to authorised assessments,
- track owner, environment, and status.

### Authorisation management

Purpose:
- store the authorised engagement and customer permissions,
- ensure tests are aligned with the engagement contract and authorised testing windows.

### Scope and exclusions manager

Purpose:
- define in-scope targets,
- record exclusions,
- enforce blocked subdomains or test areas,
- prevent scope drift.

### Assessment planning

Purpose:
- convert approved scope into a structured testing plan,
- assign tasks to reconnaissance and testing engines,
- incorporate stop conditions and escalation points.

### Reconnaissance engine

Purpose:
- discover assets and exposed services,
- gather threat-relevant metadata,
- map behaviour and exposure as permitted by scope.

### Web application testing engine

Purpose:
- assess web application authentication, authorisation, input handling, misconfiguration, and business logic issues,
- operate only within approved URLs, accounts, and test windows.

### API testing engine

Purpose:
- test authorised APIs,
- validate authentication and authorisation boundaries,
- assess input validation and leakage patterns,
- focus on confirmed security behaviour.

### Vulnerability investigation and validation

Purpose:
- distinguish suspected findings from confirmed vulnerabilities,
- verify actual exploitation conditions,
- attach evidence and confidence ratings.

### Evidence collection

Purpose:
- retain proof of observation and validation,
- capture requests, responses, timestamps, asset context, and result status,
- bind evidence to a specific finding.

### Finding classification and confidence

Purpose:
- classify by severity, impact, exploitability, and confidence,
- prevent the system from treating a scanner signal as a proof of vulnerability.

### Attack-path analysis

Purpose:
- correlate multiple weaknesses into a meaningful exploit path,
- identify combined impact based on attack feasibility.

### Remediation guidance

Purpose:
- recommend fixes and mitigations,
- help teams understand risk and corrective action,
- specify validation methods for retesting.

### Retesting and verification

Purpose:
- confirm that remedial action removed or reduced risk,
- verify the fix against the original finding conditions.

### Security reporting

Purpose:
- communicate findings to stakeholders,
- report risk, evidence, and recommended priority.

## 4. MVP workflow mapping

The AI Hacker workflow is:

Customer onboarding → Verify authorisation → Register assets → Define scope → Plan assessment → Execute permitted reconnaissance and tests → Investigate findings → Validate vulnerabilities → Collect evidence → Produce report → Recommend remediation → Retest.

This maps to the internal architecture as:

- Customer onboarding: onboarding module
- Verify authorisation: authorisation management + policy engine
- Register assets: asset registry
- Define scope: scope and exclusions manager
- Plan assessment: assessment planning
- Execute permitted reconnaissance and tests: reconnaissance + test engines
- Investigate findings: validation and attack-path analysis
- Validate vulnerabilities: vulnerability investigation and validation
- Collect evidence: evidence service
- Produce report: security reporting
- Recommend remediation: remediation guidance
- Retest: retesting and verification

## 5. Enforcement model

The architecture must enforce:

- explicit authorisation before testing starts,
- approved target scope before any action is run,
- exclusions as hard blocking rules,
- test windows and time-bound execution,
- tool restrictions by product and environment,
- limits on privileged actions,
- approval requirements for high-risk operations,
- stop-testing conditions when policy or scope is violated,
- evidence protection and secure storage,
- secure handling of credentials and secrets,
- full audit trail for all operations.

## 6. Execution isolation

The Hacker must not execute arbitrary security tools directly from the main web application process. The recommended boundary is an isolated execution worker or security sandbox that receives approved tasks from the platform and runs under tightly restricted conditions.

Required controls:

- only approved tools may be invoked,
- each tool call includes explicit scope constraints,
- execution environment is resource-limited,
- timeouts and cancellation are enforced,
- network egress is constrained to approved destinations,
- credentials are injected only within the isolated boundary,
- execution logs and evidence are captured centrally,
- results are stored with task ID, tenant ID, and execution record ID,
- cleanup executes after each run.

## 7. Automatic vs approved operations

Operations that can run automatically under strict policy:

- passive asset discovery in approved scope,
- safe reconnaissance within configured constraints,
- non-destructive metadata collection,
- report generation from validated evidence,
- status tracking and audit logging.

Operations that require explicit approval:

- active web application exploitation tests,
- authenticated testing beyond the approved test account set,
- privileged or administrative access testing,
- credential-bearing or sensitive network actions,
- destructive or high-risk verification steps,
- any execution outside the defined scope.

## 8. Security boundaries

The Hacker must never inherit Business Partner operational or financial permissions. Its execution authority remains limited to the security assessment domain. This separation must be enforced by the platform authorisation system and by a distinct tool registry and execution environment.

## 9. Evidence and protection requirements

The evidence path must preserve the chain of custody for findings:

- source of the asset,
- exact test performed,
- request and response data,
- validation result,
- classification and confidence,
- remediation recommendation,
- retest confirmation.

Evidence must be stored at a level that is protected from unauthorised access and subject to audit review. Production credentials and secrets must not be embedded in logs or evidence artifacts.

## 10. Operational safety

The architecture must define clear stop-testing conditions:

- scope violation,
- unexpected target detected,
- unapproved or unsafe tool invocation,
- credential or secret exposure,
- evidence integrity issue,
- timeout or resource exhaustion,
- policy conflict,
- escalation required by the customer or security lead.

Once a stop condition triggers, the system must terminate the activity, preserve evidence, and notify the appropriate human review path.
