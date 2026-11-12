# Security Reporting and Remediation

## 1. Purpose

This document defines how the AI Hacker communicates security risk and helps the customer remediate issues. The product must not simply produce a list of flaws. It must support understandable reporting, clear remediation guidance, prioritisation, and verification after the fix.

## 2. Reporting principles

The product must distinguish:

- confirmed vulnerabilities,
- suspected issues,
- informational findings,
- false positives,
- remediated findings,
- findings that require retesting,
- findings that remain unvalidated.

The reports must explain the difference between visible evidence and assumptions.

## 3. Report formats

### Executive report

Designed for business owners, decision-makers, and leadership teams.

It should include:

- summary of overall exposure,
- high-priority findings,
- business impact,
- recommended next actions,
- risk trend and urgency,
- overall confidence level of the assessment.

### Technical report

Designed for developers, engineers, and security teams.

It should include:

- affected assets,
- issue details,
- technical evidence,
- reproduction conditions,
- remediations,
- severity and confidence,
- retest status.

## 4. Remediation workflow

### Step 1: Understand the issue

The system explains:

- what the finding is,
- which asset is affected,
- why it matters,
- how it was observed.

### Step 2: Recommend a fix

The system should suggest:

- code-level remediation,
- configuration changes,
- permission or access control adjustments,
- architecture or deployment changes,
- patching or version upgrades where relevant,
- operational controls such as monitoring or logging improvements.

### Step 3: Prioritise

Remediation should be ranked based on:

- severity,
- exploitability,
- exposure,
- business impact,
- urgency of the fix,
- whether the risk enables broader compromise.

### Step 4: Prepare remediation guidance

The product should provide developer-facing guidance that is actionable and specific to the finding.

### Step 5: Verify the fix

The system must retest and confirm whether the issue remains or has been resolved.

## 5. Remediation guidance model

Each remediation recommendation should include:

- the vulnerability or issue description,
- affected component or asset,
- why it matters,
- the recommended fix or control,
- validation method for proof of fix,
- estimated urgency,
- whether additional monitoring or review is needed.

## 6. Example reporting structure

### Finding record summary

- Title
- Asset
- Category
- Severity
- Confidence
- Status
- Business impact
- Evidence
- Remediation
- Retest result

## 7. Risk communication rules

The product must:

- present the evidence clearly,
- avoid claiming certainty when a finding is only suspected,
- separate confirmed security issues from potential warnings,
- show whether the issue is directly exploitable,
- explain the business consequence in clear terms.

## 8. Retest and closure

The product must not classify a finding as remediated without:

- re-checking the original condition,
- confirming that the fix changed the vulnerable condition,
- updating the record and status,
- documenting any remaining uncertainty.

## 9. Customer-facing conclusions

The final security report should help the customer answer:

- what is the real risk,
- what evidence supports it,
- what can be fixed first,
- what remains unverified,
- what the next steps are.

## 10. Summary

Reporting and remediation are essential to the AI Hacker’s value proposition. The product must communicate risk clearly, recommend practical fixes, and verify remediation before closing the issue. This keeps the product disciplined, useful, and aligned with the founder-approved responsibility to operate as a serious, evidence-based security assessment capability.
