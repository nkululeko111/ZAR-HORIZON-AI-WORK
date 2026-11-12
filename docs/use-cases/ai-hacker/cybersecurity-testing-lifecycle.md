# Cybersecurity Testing Lifecycle

## 1. Purpose

This document defines the security assessment lifecycle for the AI Hacker. It is designed to govern how the product moves from initial customer onboarding to final validation and reporting, while staying within the authorised testing boundaries established for the product.

## 2. Lifecycle stages

### Stage 1: Customer onboarding and security assessment

#### Objective

Establish who the customer is, what they want tested, and whether the target is eligible for assessment under the product’s authorisation model.

#### What the agent does

- confirms customer identity and organisation,
- confirms jurisdiction, ownership, and permitted testing boundary,
- identifies the target environment and objective,
- records the person or team authorised to approve testing,
- identifies the likely security context and expected deliverables.

#### Required information

- business or technical owner,
- asset inventory or target summary,
- project scope,
- any legal or contractual constraints,
- the requested assessment type.

#### Outputs

- onboarding record,
- assessment brief,
- estimated scope and risk category,
- request for authorisation and approval checks.

### Stage 2: Authorisation and scope definition

#### Objective

Establish the precise legal and technical permissions for the engagement.

#### What the agent does

- defines the target list,
- records excluded systems,
- identifies approved techniques,
- sets test windows and required controls,
- records emergency stop procedures,
- captures evidence of authority and approval.

#### Outputs

- scope statement,
- allowed techniques list,
- exclusions list,
- authorised testing window,
- approval record.

### Stage 3: Asset discovery and reconnaissance

#### Objective

Identify the visible system footprint and map the target attack surface.

#### What the agent does

- discovers domains, subdomains, services, and infrastructure,
- identifies public-facing endpoints,
- records technologies and exposed assets,
- separates passive reconnaissance from active testing,
- maps likely attack surface and dependencies.

#### Tools or categories

- DNS enumeration,
- subdomain discovery,
- service discovery,
- fingerprinting,
- web discovery,
- API discovery.

#### Outputs

- asset inventory,
- service map,
- exposure summary,
- discovery findings with classification status.

### Stage 4: Attack surface mapping

#### Objective

Understand which exposed systems and components are within scope and relevant to testing.

#### What the agent does

- maps relationships between assets,
- links services to owners and routes,
- notes exposed admin interfaces and public surfaces,
- identifies likely entry points and security boundaries.

#### Outputs

- attack surface map,
- likely ingress points,
- asset relationship diagram,
- target prioritisation list.

### Stage 5: Security assessment and vulnerability discovery

#### Objective

Identify potential weaknesses systematically and in a manner aligned to the approved scope.

#### What the agent does

- checks security controls,
- reviews web applications, APIs, networks, and cloud configuration,
- identifies likely weaknesses,
- assesses whether controls are missing or weak,
- records evidence of each issue.

#### Outputs

- preliminary findings,
- security issue inventory,
- confidence level and evidence notes,
- test coverage summary.

### Stage 6: Vulnerability validation

#### Objective

Determine whether a suspected issue is real and exploitable under the approved conditions.

#### What the agent does

- reproduces the issue under controlled conditions,
- confirms whether the issue affects the intended system,
- distinguishes confirmed vulnerabilities from false positives,
- evaluates exploitability and business impact.

#### Outputs

- validated findings,
- suspected findings list,
- suppressed false positives,
- reproduction evidence.

### Stage 7: Attack path analysis

#### Objective

Understand whether findings combine into a meaningful security compromise path.

#### What the agent does

- correlates weak findings across systems,
- evaluates chains of exposure,
- identifies conditions that increase business risk,
- assesses whether findings matter in combination.

#### Outputs

- attack path summary,
- risk narrative,
- impact assessment,
- prioritised security concerns.

### Stage 8: Risk and business impact assessment

#### Objective

Assess the practical risk of each finding and how it affects business operations.

#### What the agent does

- considers data sensitivity,
- assesses technical impact,
- evaluates exposure and exploitability,
- ties risk to business function and operational consequences.

#### Outputs

- risk matrix,
- business-impact summary,
- prioritised remediation guidance.

### Stage 9: Evidence collection

#### Objective

Create a defensible record of findings and their verification state.

#### What the agent does

- captures evidence and reproduction details,
- records affected assets and conditions,
- classifies confidence level,
- preserves proof without exposing unnecessary sensitive data.

#### Outputs

- evidence pack,
- technical record of each finding,
- link to retest results when available.

### Stage 10: Security reporting

#### Objective

Communicate findings, impact, and remediation priorities to the customer in a useful format.

#### What the agent does

- prepares executive summary,
- prepares technical report,
- tags issues by finding status,
- describes whether findings are confirmed or suspected,
- identifies critical next steps.

#### Outputs

- executive report,
- technical security report,
- actionable remediation summary.

### Stage 11: Remediation guidance

#### Objective

Help the customer fix the issues in a practical and prioritised way.

#### What the agent does

- identifies affected components and risky configurations,
- explains the issue in clear language,
- recommends technical remediation,
- produces remediation priorities,
- supports developer-facing fix notes and tickets.

#### Outputs

- remediation guidance,
- fix priorities,
- developer tickets or remediation notes,
- change-tracking comments.

### Stage 12: Retesting and verification

#### Objective

Confirm that the issue was actually resolved, not simply claimed to be fixed.

#### What the agent does

- retests the affected asset,
- checks whether the original condition still exists,
- documents whether the fix was successful,
- updates the status and risk record.

#### Outputs

- retest results,
- updated finding status,
- closure or re-open status.

### Stage 13: Continuous security monitoring where explicitly configured

#### Objective

Monitor for repeated or newly introduced exposure where the customer has explicitly requested ongoing assessment.

#### What the agent does

- monitors configured assets and alerts,
- compares current posture to expected secure baseline,
- flags new exposure or changed risk conditions.

#### Outputs

- monitoring summary,
- risk drift report,
- recurring issue notes.

## 3. Key lifecycle requirement

The lifecycle is not a “scan and report” loop. It is an evidence-driven security investigation process. Every stage requires proper scope control, evidence handling, and explicit verification before a finding is treated as valid or resolved.

## 4. Safety principle

The product must stop, escalate, and pause testing when:

- scope is unclear,
- the target is outside the approved environment,
- unusual sensitive data is encountered,
- safety controls are triggered,
- the test would be destructive or disruptive,
- a high-risk condition emerges without explicit approval.

## 5. Summary

The lifecycle reflects an authorised red-team assessment model. It balances technical investigation, evidence collection, and risk assessment with the requirement for professional control, accountability, and human approval in high-risk or sensitive scenarios.
