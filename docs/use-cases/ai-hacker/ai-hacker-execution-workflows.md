# AI Hacker Execution Workflows

## 1. Purpose

This document defines realistic execution workflows for the AI Hacker. It is intended to show how the product operates across the cybersecurity lifecycle while preserving strict authorisation and safety boundaries.

## 2. Workflow 1: External attack surface assessment

### Customer objective

A company wants to understand how much of its external digital footprint is exposed and whether obvious weaknesses or misconfigurations increase risk.

### Required authorisation

- customer identity and authority to test the target,
- explicit asset list,
- exclusions list,
- permitted discovery methods.

### Required information and access

- target domains or IP ranges,
- scope and exclusion list,
- contact for internal security review if needed.

### Agent reasoning and investigation stages

1. Confirm the target scope and exclusions.
2. Discover external hosts, domains, subdomains, and services.
3. Identify exposed endpoints and technologies.
4. Review configuration posture and obvious service weaknesses.
5. Prioritise the riskiest externally visible exposures.
6. Distinguish passive information gathering from active validation.

### Security tools or categories

- DNS and subdomain enumeration,
- service discovery,
- fingerprinting,
- web discovery,
- configuration review tools.

### Actions performed

- map external attack surface,
- identify weak public exposure,
- catalogue exposed endpoints,
- detect obvious misconfiguration and output risk.

### Approval checkpoints

- approval to run active probing against the target,
- approval to continue if high-risk findings are identified.

### Evidence collected

- discovered domains,
- services and ports,
- configuration evidence,
- risk notes and findings.

### Expected outputs

- external asset inventory,
- risk overview,
- list of potential security weaknesses requiring deeper review.

### Success verification

- all discovered assets correlate to the approved scope,
- evidence is attributable to the target assets,
- findings are classified as confirmed or unverified.

### Failure and escalation

- stop if scope is unclear,
- escalate if unapproved systems are discovered,
- halt if a high-risk condition is encountered without approval.

## 3. Workflow 2: Web application security assessment

### Customer objective

A product team wants to review the security of a customer-facing application before a release or when a suspected weakness has emerged.

### Required authorisation

- written or verifiable authorisation for target application,
- approved test accounts and access roles,
- authorised testing window,
- exclusions and rate-limit constraints.

### Required information and access

- app URLs,
- authentication flow details,
- test credentials and permitted roles,
- business-critical endpoints,
- environment information.

### Agent reasoning and investigation stages

1. Validate scope and environment.
2. Map the application surface and key user flows.
3. Assess authentication, session, and access controls.
4. Probe for input handling, misconfiguration, and injection patterns.
5. Review API surface and business logic weaknesses.
6. Correlate likely findings with impact and exploitability.

### Security tools or categories

- web application scanners,
- API testing tooling,
- authentication flow review,
- headers and transport validation,
- input validation testing.

### Actions performed

- review app attack surface,
- test common web weaknesses,
- inspect session and auth flows,
- assess access-control boundaries,
- validate candidate findings safely.

### Approval checkpoints

- approval before testing privileged roles,
- approval before brute-force or rate-limited abuse tests,
- approval before testing production-like functionality that could affect availability.

### Evidence collected

- request and response evidence,
- proof of auth or access control gap,
- reproduction conditions,
- impact analysis.

### Expected outputs

- vulnerable routes or controls summary,
- findings with evidence,
- risk and remediation recommendations.

### Success verification

- findings are proven against the authorised scope,
- the issue is not just a scanner hit,
- evidence supports severity and impact classification.

### Failure and escalation

- pause if the application behaves dangerously or unexpectedly,
- stop if access to sensitive data or production content appears outside scope.

## 4. Workflow 3: API security assessment

### Customer objective

A software company needs to review APIs before a release or after a suspected issue.

### Required authorisation

- authorisation for the API service and target endpoints,
- approved credentials and test accounts,
- defined access levels and roles,
- exclusions for production-sensitive or unrelated endpoints.

### Required information and access

- endpoint inventory,
- API docs or schema,
- authentication method,
- access roles.

### Agent reasoning and investigation stages

1. Enumerate endpoints and access flows.
2. Review auth, tokens, and session handling.
3. Check access-control logic for object-level exposure.
4. Review rate limits, input validation, and data exposure.
5. Test unsafe business logic and endpoint behaviour.
6. Correlate findings with business risk.

### Security tools or categories

- API discovery tools,
- authentication and token analysis,
- request manipulation testing,
- rate-limit and abuse testing,
- schema review tools.

### Actions performed

- enumerate API surface,
- validate auth and authorisation,
- test endpoint abuse conditions,
- check for sensitive data leak patterns.

### Approval checkpoints

- approval before testing privileged or production-like endpoints,
- approval before testing unauthorised roles or object access.

### Evidence collected

- request and response logs,
- auth flow evidence,
- data exposure examples,
- business impact notes.

### Expected outputs

- endpoint-by-endpoint vulnerability review,
- validated vulnerabilities,
- remediation guidance for developers.

### Success verification

- issue reproduction is consistent and traceable,
- the result is not a generic API warning,
- findings match the authorisation scope.

### Failure and escalation

- stop if credentials expose unauthorised or unrelated data,
- halt if a test could affect service availability without explicit approval.

## 5. Workflow 4: Network infrastructure assessment

### Customer objective

A business wants to assess whether its externally exposed or internal network services are unnecessarily exposed or misconfigured.

### Required authorisation

- explicit infrastructure scope,
- approved IP ranges and assets,
- exclusions,
- review of permitted network methods.

### Required information and access

- asset list,
- network diagram or service inventory,
- permitted test windows,
- contact for infrastructure owner.

### Agent reasoning and investigation stages

1. Confirm target network range and host inventory.
2. Identify exposed services.
3. Check service versions and configuration posture.
4. Review segmentation, administrative exposure, and protocol weakness.
5. Validate whether findings matter operationally and technically.

### Security tools or categories

- host and service discovery,
- port scanning,
- protocol and version assessment,
- infrastructure configuration review.

### Actions performed

- host and port inventory,
- service fingerprinting,
- network exposure review,
- segmentation and admin-interface assessment.

### Approval checkpoints

- approval before active probing,
- approval before any testing that may affect availability or service continuity.

### Evidence collected

- service inventory,
- version evidence,
- network path and exposure notes,
- identified risks and conditions.

### Expected outputs

- infrastructure risk summary,
- service exposure list,
- remediation guidance for operations teams.

### Success verification

- evidence matches the authorised network scope,
- vulnerabilities are confirmed and not merely inferred from open ports.

### Failure and escalation

- stop once the scope extends beyond authorised ranges,
- halt if the testing approach could affect production availability without approval.

## 6. Workflow 5: Cloud configuration assessment

### Customer objective

A cloud-hosted business wants to detect risky permissions, public exposure, configuration drift, and secret leakage.

### Required authorisation

- explicit cloud account scope,
- permission to read security configuration,
- agreed secrets and object access boundaries,
- list of excluded workloads and data.

### Required information and access

- cloud environment inventory,
- IAM and resource access policy details,
- public-facing services list,
- secret-handling policy if relevant.

### Agent reasoning and investigation stages

1. Confirm cloud scope and access.
2. Inventory resources and identities.
3. Review permissions, storage, networking, and exposure.
4. Identify configuration risks and data leakage paths.
5. Correlate risky settings with business impact.

### Security tools or categories

- cloud audit and inventory tooling,
- policy review,
- configuration scanning,
- secret exposure review.

### Actions performed

- review permissions,
- detect public exposure,
- inspect storage and configuration posture,
- identify risky cloud patterns.

### Approval checkpoints

- approval before reading or testing sensitive cloud objects or secrets,
- approval before any action affecting production workloads.

### Evidence collected

- config evidence,
- IAM misconfiguration notes,
- exposure and resource evidence,
- business impact assessment.

### Expected outputs

- cloud security findings,
- exposure summary,
- remediation recommendations.

### Success verification

- every risk is tied to the authorised asset set,
- evidence supports the classification and severity,
- no unrelated cloud objects are reviewed.

### Failure and escalation

- stop if the account contains broad or unrelated data outside the agreed scope,
- escalate if access or credentials are not explicitly approved.

## 7. Workflow 6: Vulnerability investigation and validation

### Customer objective

A team wants to confirm whether a reported issue is real and whether it poses actual risk.

### Required authorisation

- target and test method approval,
- authorised validation method,
- clear boundary for safe exploitation or demonstration, if any.

### Required information and access

- findings list,
- asset details,
- likely business context,
- environment information.

### Agent reasoning and investigation stages

1. Validate the issue against the target system.
2. Confirm whether the target is in scope.
3. Determine if the weak condition actually behaves as expected.
4. Assess exploitability and business impact.
5. Decide if the issue should be labelled confirmed, suspected, or false positive.

### Security tools or categories

- targeted validation commands,
- application or API testing tools,
- reproduction environment tooling,
- evidence collection tools.

### Actions performed

- confirm reproduction,
- gather deterministic evidence,
- assess severity and exploitability,
- deduplicate overlapping issues.

### Approval checkpoints

- approval before attempting any exploit-like validation beyond safe demonstration,
- approval before testing high-impact controls or privilege boundaries.

### Evidence collected

- reproduction logs,
- request and response traces,
- validation notes,
- business and technical impact notes.

### Expected outputs

- confirmed or unconfirmed finding status,
- technical evidence summary,
- impact and priority classification.

### Success verification

- the issue is verified against the actual target and environment,
- no unsupported severity is assigned.

### Failure and escalation

- halt if the issue cannot be proven without entering unauthorised or unsafe testing.

## 8. Workflow 7: Attack path investigation

### Customer objective

A customer wants to understand whether multiple findings combine into a realistic compromise path.

### Required authorisation

- explicit permission for all assets involved,
- authorisation to test combined path conditions,
- approval for relevant privilege or lateral movement testing if needed.

### Required information and access

- validated findings,
- architecture or asset map,
- access model and environment context.

### Agent reasoning and investigation stages

1. Correlate related findings.
2. Determine whether the conditions create a meaningful path.
3. Assess exposure and business impact.
4. Rank the path by practicality and severity.

### Actions performed

- combine findings into a narrative,
- assess attack chain viability,
- describe the likely business consequence.

### Expected outputs

- attack path summary,
- impact narrative,
- remediation prioritisation.

### Success verification

- each attack step has evidence and is relevant to the target environment,
- the narrative does not overstate risk.

### Failure and escalation

- stop before testing lateral movement or privilege escalation that is not explicitly approved.

## 9. Workflow 8: Security report generation

### Customer objective

A customer wants a security review to understand the overall state of risk and the next actions to take.

### Required authorisation

- scope and report audience approval,
- approval for what information may be included.

### Required information and access

- findings list,
- evidence pack,
- technical and business context.

### Agent reasoning and investigation stages

1. Group findings by severity and business impact.
2. Distinguish confirmed vs suspected findings.
3. Summarise technical and executive implications.
4. Prioritise remediations and retest needs.

### Expected outputs

- executive summary,
- technical report,
- remediation priorities,
- risk status by asset or function.

### Success verification

- report reflects verified findings and does not claim certainty where evidence is incomplete.

## 10. Workflow 9: Remediation planning

### Customer objective

A team wants to know how to fix the issues and what to prioritise first.

### Required authorisation

- approved scope and test environment,
- customer permission to propose fixes.

### Required information and access

- findings,
- affected components,
- ownership and remediation context.

### Agent reasoning and investigation stages

1. Identify root cause and affected components.
2. Recommend remediation steps.
3. Prioritise by impact and ease of fix.
4. Create developer-facing guidance or tickets.

### Expected outputs

- remediation plan,
- fix guidance,
- priority matrix,
- retest plan.

### Success verification

- each recommendation is tied to the underlying issue and supported by evidence.

## 11. Workflow 10: Retesting after remediation

### Customer objective

A team wants to confirm that security fixes solved the issue without introducing a new problem.

### Required authorisation

- customer approval for retest,
- confirmation of the fix window and test conditions.

### Required information and access

- original finding details,
- remediation status,
- target asset state.

### Agent reasoning and investigation stages

1. Re-run the relevant validation steps.
2. Check whether the prior vulnerability still exists.
3. Look for side effects or new findings introduced by the fix.
4. Update the finding and evidence records.

### Expected outputs

- retest findings,
- updated issue status,
- remediation verification report.

### Success verification

- the original condition is absent or reduced and evidence is collected to substantiate that conclusion.

## 12. Key protocol for all workflows

Every security workflow must include:

- clear scope and authorisation,
- target asset list,
- evidence collection,
- safe and controlled validation,
- explicit finding status labels,
- approval points for risky actions,
- human oversight where needed,
- closure or escalation path.

## 13. Summary

These workflows define the practical operating model of the AI Hacker. They are grounded in authorised inspection, careful validation, and evidence-based reporting. Their value is in helping customers assess and remediate real security risk under strict control, rather than simply producing a large list of potential issues without proof.
