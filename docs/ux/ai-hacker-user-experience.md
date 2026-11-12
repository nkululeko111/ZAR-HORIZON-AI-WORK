# AI Hacker user experience

## 1. Product experience goal

The AI Hacker should feel like a professional, controlled security assessment workspace. The UX must be built around authorisation, scope, evidence, findings, and remediation. It should help security teams understand what is permitted, what is in progress, what has been validated, and what still requires human review.

The product should never imply unrestricted testing capability or generic command execution.

## 2. Main navigation

Recommended MVP navigation:

- Security Overview
- Assets
- Authorisations and Scope
- Assessments
- Findings
- Evidence
- Remediation
- Reports
- Activity
- Settings

Deferred items should be clearly labelled as future features.

## 3. Security overview dashboard

The dashboard should show:

- registered assets,
- authorisation status,
- active assessments,
- completed assessments,
- findings by severity,
- findings awaiting validation,
- remediation progress,
- retesting status,
- recent security activity,
- scope or authorisation warnings.

Important UX rule:

- a registered asset is not evidence that a system is authorised or tested,
- a finding is not a validated vulnerability until it has been reviewed.

## 4. Asset management experience

### Asset registration screens

The UI should support:

- registering domains,
- registering web applications,
- registering APIs,
- associating assets with customers or organisations,
- viewing asset metadata and owners,
- checking status against active authorisations.

### Asset detail panel

Asset details should include:

- asset name and type,
- owner and customer,
- authorisation status,
- scope coverage,
- test windows,
- restrictions,
- related assessments,
- evidence records.

## 5. Authorisation and scope experience

This is a critical part of the product. The interface must make it visually obvious when a target is not authorised or cannot proceed.

### Required information

- customer authorisation record,
- scope inclusions,
- exclusions,
- permitted techniques,
- testing windows,
- test accounts and restrictions,
- assessment readiness status.

The UX should show states such as:

- authorised,
- pending approval,
- expired,
- blocked by scope,
- blocked by authorisation,
- ready for assessment.

## 6. Assessment workspace

The assessment workspace should show:

- assessment details,
- target asset,
- approved scope,
- plan and phases,
- current progress,
- execution status,
- tool activity,
- findings discovered,
- evidence collected,
- blocked actions or warnings,
- completion state.

Required run states:

- planned,
- running,
- blocked,
- cancelled,
- failed,
- completed.

It should be clear whether an assessment is:

- simply created,
- authorised and ready,
- actively running,
- completed with evidence,
- failed or cancelled mid-way.

## 7. Findings workspace

Finding screens should include:

- title,
- affected asset,
- severity,
- confidence,
- validation status,
- technical description,
- business impact,
- evidence references,
- reproduction notes where appropriate,
- remediation guidance,
- retest status.

The interface should clearly distinguish:

- potential findings,
- validated vulnerabilities,
- rejected findings,
- findings requiring review.

## 8. Remediation and reporting

The remediation workflow should support:

- review of guidance,
- status tracking,
- note progress,
- request retesting,
- verification of fix status,
- report generation.

### Report experience

Reports should include:

- summary of findings,
- evidence references,
- remediation status,
- retest verification,
- final risk evaluation,
- CTA to share or archive the report.

## 9. AI Hacker AI interaction model

The AI assistant should help with investigation and understanding, but it should not offer an unrestricted command prompt. It should stay within structured assessment workflows.

The assistant should help by:

- summarising assessment status,
- explaining scope and exclusions,
- guiding validation steps,
- linking evidence to findings,
- preparing remediation guidance,
- supporting report narrative.

It should not imply that it can run arbitrary security commands or test anything not in scope.

## 10. Design principles for this product

- Permission before execution.
- Scope before technique.
- Evidence before conclusion.
- Authorisation visible at all times.
- Findings must be validated before they are treated as confirmed vulnerabilities.
- Security status must be explicit and auditable.

## 11. Summary

The AI Hacker UX should feel disciplined, evidence-driven, and operationally safe. It prioritises legal and technical boundaries, supported assessment execution, and high-quality report and remediation workflows over a flashy or open-ended AI experience.
