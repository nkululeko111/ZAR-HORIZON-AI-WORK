# AI Hacker tool catalogue

## 1. Purpose

This catalogue defines the initial tool set for the AI Hacker product. The tool catalogue is constrained to authorised security investigation, evidence handling, and workflow validation. It does not permit arbitrary execution of security tools, shell commands, or unrestricted network probing.

## 2. Core design constraints

All AI Hacker tools must enforce:

- approved asset and authorisation context,
- target scope inclusion and exclusion checks,
- authorised test windows,
- restriction policies,
- evidence capture before result acceptance,
- backend approval for sensitive actions.

The tool registry must deny by default. No tool may execute outside the assigned scope.

## 3. MVP prioritisation

### P0 tools

- `register_assessment_asset`
- `validate_authorisation`
- `validate_assessment_scope`
- `create_assessment_plan`
- `capture_security_evidence`
- `classify_security_finding`
- `generate_remediation_guidance`
- `request_retest`
- `generate_security_report`

### P1 tools

- `perform_controlled_reconnaissance`
- `assess_web_application`
- `assess_api`
- `investigate_vulnerability`
- `validate_security_finding`
- `verify_remediation`

## 4. Tool definitions

### `register_assessment_asset`

Purpose:
- register a customer asset for a security assessment.

Inputs:
- customerId, assetName, assetType, exposureInfo, ownerContact.

Outputs:
- asset record and asset identifier.

Required permissions:
- security asset management.

Authorisation requirements:
- organisation-level security permissions.

Scope requirements:
- asset must belong to the authorised customer context.

Approval requirements:
- no for onboarding; required for active assessment use.

Risk classification:
- medium.

Execution boundaries:
- validation only; no testing performed.

Evidence requirements:
- registration metadata, owner, asset metadata, date created.

Failure and cancellation behaviour:
- invalid customer or duplicate asset record returns structured validation error.

### `validate_authorisation`

Purpose:
- confirm that an asset and customer are authorised for the requested assessment.

Inputs:
- customerId, assetId, assessmentType, requestedScope.

Outputs:
- authorisation status record.

Required permissions:
- security authorisation review.

Authorisation requirements:
- asset and customer must already have active authorisation records.

Scope requirements:
- must validate against authorisation conditions and exclusions.

Approval requirements:
- required before ongoing assessment execution.

Risk classification:
- high.

Execution boundaries:
- read-only check, no target probing.

Evidence requirements:
- authorisation record reference and validation timestamp.

Failure and cancellation behaviour:
- if invalid or expired, execution is blocked.

### `validate_assessment_scope`

Purpose:
- confirm that the test target, methods, timing, and exclusions are allowed.

Inputs:
- assessmentId, assetId, targetDomains, testType, windows, exclusions.

Outputs:
- scope validation result.

Required permissions:
- security scope validation.

Authorisation requirements:
- active authorisation and approved scope plan.

Scope requirements:
- target must be in-scope and not excluded.

Approval requirements:
- required before any execution beyond read-only planning.

Risk classification:
- high.

Execution boundaries:
- no execution beyond policy checks.

Evidence requirements:
- scope snapshot, approved inclusions, exclusions, and restrictions.

Failure and cancellation behaviour:
- reject out-of-scope or restricted operations.

### `create_assessment_plan`

Purpose:
- create a structured plan for the authorised assessment.

Inputs:
- assessmentId, objectives, targets, phases, timings.

Outputs:
- assessment plan and execution stages.

Required permissions:
- security planning and asset access.

Authorisation requirements:
- valid assessment plus approved scope.

Scope requirements:
- must align to approved scope and test restrictions.

Approval requirements:
- required for plan execution.

Risk classification:
- medium.

Execution boundaries:
- planning only; no offensive execution.

Evidence requirements:
- plan version, authorisation references, approved windows.

Failure and cancellation behaviour:
- rejected if there is a mismatch between plan and authorised scope.

### `perform_controlled_reconnaissance`

Purpose:
- run constrained, approved reconnaissance within defined scope.

Inputs:
- assessmentId, targetList, allowedTechniques, timeWindow.

Outputs:
- reconnaissance results and evidence collection summary.

Required permissions:
- security assessment execution with reconnaissance permission.

Authorisation requirements:
- approved authorisation record and valid scope plan.

Scope requirements:
- target list must be in-scope, exclusions preserved, rate limits respected.

Approval requirements:
- required before execution.

Risk classification:
- high.

Execution boundaries:
- read-only discovery and authorised enumeration only; no arbitrary exploitation.

Evidence requirements:
- raw result set, timestamps, target references, request traces.

Failure and cancellation behaviour:
- cancels automatically if scope or window violations occur.

### `assess_web_application`

Purpose:
- evaluate the authorised web application using approved techniques only.

Inputs:
- assessmentId, assetId, testTargets, allowedChecks, config.

Outputs:
- web assessment results, findings summary, evidence references.

Required permissions:
- security assessment access and web application assessment permission.

Authorisation requirements:
- active customer authorisation, approved scope, and approved technique list.

Scope requirements:
- target must be in-scope and within test window.

Approval requirements:
- required before execution.

Risk classification:
- critical.

Execution boundaries:
- must not include unrestricted scanning or exploit execution.

Evidence requirements:
- request/response capture, targeted proof, validation results, timestamps.

Failure and cancellation behaviour:
- stop immediately if scope, policy, or approval violations are detected.

### `assess_api`

Purpose:
- assess authorised API endpoints with approved checks only.

Inputs:
- assessmentId, apiTarget, allowedMethods, endpoints, constraints.

Outputs:
- API assessment result, issues found, evidence references.

Required permissions:
- security assessment access and API assessment permission.

Authorisation requirements:
- valid authorisation and approved endpoint list.

Scope requirements:
- target endpoints and methods must be included in assessment scope.

Approval requirements:
- required before execution.

Risk classification:
- critical.

Execution boundaries:
- no unrestricted scanning, fuzzing beyond approved limits, or exploitation.

Evidence requirements:
- endpoint hit logs, request/response metadata, finding references.

Failure and cancellation behaviour:
- cancel and require reapproval if modified scope or method list is detected.

### `investigate_vulnerability`

Purpose:
- investigate a suspected vulnerability within the approved assessment boundary.

Inputs:
- assessmentId, findingId, targetRef, evidenceRef, investigationPlan.

Outputs:
- investigation result, validation results, potential exploitability assessment.

Required permissions:
- vulnerability investigation permission.

Authorisation requirements:
- active approved scope and explicit target permission.

Scope requirements:
- must remain inside the approved target and technique scope.

Approval requirements:
- required for additional or high-risk techniques.

Risk classification:
- critical.

Execution boundaries:
- no uncontrolled exploitation or unrestricted execution.

Evidence requirements:
- investigation log, proof artifacts, validation details.

Failure and cancellation behaviour:
- halt if evidence is incomplete or scope is exceeded.

### `validate_security_finding`

Purpose:
- validate or reject a candidate security finding.

Inputs:
- findingId, evidenceRef, validationRules, context.

Outputs:
- validation status, confidence, reason, required remediation steps.

Required permissions:
- security finding validation.

Authorisation requirements:
- authorised assessment and evidence access.

Scope requirements:
- validation must only use the evidence and conditions of the approved assessment.

Approval requirements:
- required for severity changes or material finding classification changes.

Risk classification:
- high.

Execution boundaries:
- no new testing beyond the approved validation plan.

Evidence requirements:
- evidence chain, validation rules, reviewer identity, timestamps.

Failure and cancellation behaviour:
- missing evidence results in a rejected or pending status, not presumed valid.

### `capture_security_evidence`

Purpose:
- store security evidence with provenance and retention controls.

Inputs:
- findingId, evidenceType, contentRef, metadata, hash.

Outputs:
- evidence record and evidence ID.

Required permissions:
- evidence capture and protected document storage.

Authorisation requirements:
- must respect evidence access policy and classification.

Scope requirements:
- evidence must belong to the relevant assessment or finding.

Approval requirements:
- none for storage; required for sensitive evidence exposure.

Risk classification:
- high.

Execution boundaries:
- storage and sealing only.

Evidence requirements:
- full provenance, hash, and access metadata.

Failure and cancellation behaviour:
- evidence record is rejected if provenance is incomplete.

### `classify_security_finding`

Purpose:
- classify a finding according to the approved taxonomy.

Inputs:
- findingContent, assetContext, evidence, language, severityInputs.

Outputs:
- severity, category, impact, confidence, classification rationale.

Required permissions:
- classification access within the relevant assessment.

Authorisation requirements:
- assessment must be active and authorised.

Scope requirements:
- classification must not exceed the in-scope asset and assessment context.

Approval requirements:
- required for final severity or risk acceptance decisions.

Risk classification:
- high.

Execution boundaries:
- analysis and classification only.

Evidence requirements:
- evidence references and classification logic metadata.

Failure and cancellation behaviour:
- unresolved evidence leads to pending classification rather than an assumed severity.

### `generate_remediation_guidance`

Purpose:
- provide remediation recommendations for an accepted finding.

Inputs:
- findingId, assetContext, affectedComponent, riskProfile.

Outputs:
- remediation guidance record and suggested mitigations.

Required permissions:
- security remediation access.

Authorisation requirements:
- valid asset and finding context.

Scope requirements:
- guidance must map to the actual target and approved environment.

Approval requirements:
- required for any recommendation that alters production-facing controls or deployment decisions.

Risk classification:
- high.

Execution boundaries:
- recommendations only; no direct system change.

Evidence requirements:
- supporting evidence, root cause, and mitigation references.

Failure and cancellation behaviour:
- return guidance as draft until evidence and scope are confirmed.

### `request_retest`

Purpose:
- request a verification retest after remediation or scope adjustment.

Inputs:
- findingId, remediationId, retestWindow, objective.

Outputs:
- retest request, pending status, retest workflow reference.

Required permissions:
- remediation and retest participation.

Authorisation requirements:
- must be tied to an authorised assessment and the same target scope.

Scope requirements:
- retest must remain within the approved target and permitted techniques.

Approval requirements:
- required for any changes to accepted scope or retest strategy.

Risk classification:
- high.

Execution boundaries:
- workflow orchestration only.

Evidence requirements:
- remediation proof and retest plan.

Failure and cancellation behaviour:
- reject if remediation evidence is missing or scope is no longer valid.

### `verify_remediation`

Purpose:
- verify whether a remediation outcome mitigates the identified risk.

Inputs:
- remediationId, evidenceRefs, verificationPlan.

Outputs:
- remediation verification status and confidence.

Required permissions:
- security verification and evidence review.

Authorisation requirements:
- same authorised asset and assessment scope.

Scope requirements:
- verification cannot expand beyond approved testing boundaries.

Approval requirements:
- required when finalised status impacts the assessment closure or client report.

Risk classification:
- high.

Execution boundaries:
- validation only.

Evidence requirements:
- before/after evidence, proof of mitigation, reviewer log.

Failure and cancellation behaviour:
- if evidence is insufficient, verification remains pending or failed.

### `generate_security_report`

Purpose:
- create the final assessment report for an authorised assessment.

Inputs:
- assessmentId, findings, evidence, remediationSummary, finalStatus.

Outputs:
- final security report and summary metadata.

Required permissions:
- report generation and security data access.

Authorisation requirements:
- only for authorised customers and active assessments.

Scope requirements:
- only include findings and evidence within the approved scope.

Approval requirements:
- required before delivery to a customer or external party.

Risk classification:
- high.

Execution boundaries:
- reporting only; no testing or exploitation.

Evidence requirements:
- final evidence chain and report metadata.

Failure and cancellation behaviour:
- report generation is blocked when evidence is incomplete or scope is invalid.

## 5. Prohibited tool behaviour

The following are explicitly forbidden:

- arbitrary shell execution,
- unrestricted network scanning,
- exploitation or payload delivery outside approved scope,
- direct execution of security tooling without policy controls,
- direct LLM access to raw server or database credentials,
- tool self-approval or permission mutation.

## 6. Design principle

AI Hacker tools are built around a controlled, evidence-first, scope-locked workflow. The product is designed to support authorised security assessment, not unrestricted penetration testing or real-world exploitation.
