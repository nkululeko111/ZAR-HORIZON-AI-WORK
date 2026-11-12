# Authorisation and Testing Scope

## 1. Purpose

This document defines the critical safety and authorisation model for the AI Hacker. The product is designed to perform high-value security assessment within authorised boundaries. It must not operate as a general-purpose offensive security system in unapproved or uncontrolled conditions.

## 2. Core authorisation requirements

Before any assessment begins, the product must verify the following:

- the customer is a legitimate organisation or authorised representative,
- the target assets are clearly identified,
- the customer has authority to test those assets,
- the scope is documented and approved,
- the testing window and conditions are known,
- any restrictions or exclusions are recorded,
- the authorised testing techniques are explicitly defined,
- there is a stop-testing procedure and escalation path.

## 3. Authorisation record

A valid assessment should include:

- customer identity,
- contact information for the authorised representative,
- the target system or asset list,
- target owner or responsible party,
- the approved testing window,
- the test purpose,
- permitting organisation or legal reference if applicable,
- exclusions,
- evidence of customer approval,
- assigned security owner and review chain,
- audit log of the engagement state.

## 4. Testing scope model

### In-scope assets

- authorised domains,
- approved subdomains,
- permitted service endpoints,
- named applications,
- approved network ranges,
- authorised cloud assets,
- approved test environments.

### Out-of-scope assets

- unrelated domains or services,
- third-party systems not explicitly authorised,
- production systems without approval,
- unrelated cloud resources,
- systems or data outside the test environment.

### Scope controls

The AI Hacker must stop if it encounters:

- an asset outside the approved scope,
- an unknown or unapproved owner,
- a test target lacking clear permission,
- a host or endpoint that was not named in the approval,
- a data boundary it is not authorised to access.

## 5. Risk categories and approval requirements

### Category 1 — Low-risk assessment

Examples:

- passive reconnaissance,
- public documentation review,
- non-invasive asset discovery,
- configuration review,
- service exposure review,
- public information gathering within scope.

Approval requirements:

- well-defined scope,
- approval to inspect the assets,
- no destructive or disruptive behaviour,
- explicit stop conditions.

Human oversight:

- minimal for passive review,
- still requires review of findings and scope integrity.

### Category 2 — Controlled active testing

Examples:

- authorised web application testing,
- API testing in a controlled environment,
- targeted vulnerability validation,
- bounded configuration review,
- role-limited access testing under an approved test user.

Approval requirements:

- written or auditable approval,
- specific techniques approved,
- active validation limited to the defined target set,
- safety guardrails and escalation path.

Human oversight:

- required before any privileged or authentication role testing,
- required if a finding affects customer data or production behavior.

### Category 3 — High-risk testing

Examples:

- intrusive exploitation,
- privilege escalation validation,
- denial-of-service testing,
- broad or aggressive network probing,
- tests affecting availability or data integrity,
- any test that could materialise business risk beyond the approved scope.

Approval requirements:

- explicit written approval with clear boundaries,
- senior stakeholder review,
- defined safeguards and rollback plan,
- stop conditions documented before testing starts.

Human oversight:

- mandatory,
- direct responsible-owner approval,
- escalation before executing the test if impact risk is high.

## 6. Prohibited and restricted actions

The AI Hacker must never perform any of the following without explicit approval and control:

- testing systems outside the authorised scope,
- exploiting a system in a way that could disrupt business operations,
- destructive exploitation,
- denial-of-service or availability attacks,
- unauthorised data extraction,
- persistence or unauthorised backdoors,
- credential theft or misuse,
- lateral movement outside the approved scope,
- unauthorised privilege escalation,
- any activity that exceeds the test plan without an emergency stop or approval.

## 7. Safety and execution controls

### Isolation

- tests must run in controlled environments where possible,
- production-like systems must be isolated from unrelated data and workloads,
- data handling must be restricted to the authorised environment.

### Execution logging

- every security action must be logged,
- evidence should be preserved in a traceable chain,
- the user should be able to review the test scope and actions taken.

### Credential handling

- credentials must be managed securely,
- test accounts must be restricted to approved roles,
- secrets and tokens must be handled with care and not exposed in reports or logs.

### Evidence protection

- technical evidence should be stored with controlled access,
- sensitive data should be minimised,
- findings should avoid unnecessary exposure of secrets or customer data.

## 8. Stop-testing conditions

The system must stop when any of the following occurs:

- authorisation or scope is unclear,
- a test crosses boundary into an unapproved asset,
- a result contains sensitive data outside the approved set,
- the testing method is no longer within the approved technique set,
- a condition is encountered that could cause significant disruption,
- a safety condition is triggered,
- a customer requests a halt.

## 9. Human oversight and review

The AI Hacker should require human review for:

- high-risk active testing,
- privilege-boundary assessment,
- exploitation or validation that could affect production,
- any action that could impact availability, confidentiality, or data integrity,
- any finding that may be sensitive to legal or contractual risk.

## 10. Summary

Authorisation and safety are not optional product features. They are the foundation of the AI Hacker’s trust model. The product must be effective, evidence-driven, and capable of real security investigation, but it must also be disciplined enough to remain inside the approval model and stop when conditions are unsafe or not authorised.
