# Day 5 AI Hacker Decisions

## 1. Purpose

This document captures the key decisions and product directions emerging from the Day 5 AI Hacker use-case analysis. It distinguishes between decisions already grounded in the founder-approved product definition and decisions that still require customer validation or founder approval.

## 2. Decisions already established by the approved product definition

The following are already clear and approved:

- The AI Hacker is not a passive scanner.
- It must operate as an authorised offensive-security assessment capability.
- It must investigate, validate, and help remediate real security weaknesses.
- It must operate within explicit testing scope and safety rules.
- It must distinguish between potential findings, validated issues, and remediated fixes.
- It must preserve separation from Business Partner business execution authority.
- It must provide evidence-backed reporting and verification.

## 3. Product decisions informed by Day 5 analysis

These decisions are consistent with the approved vision and the use-case design:

1. The AI Hacker should be built around the security lifecycle, not around a simple scanning feature.
2. Asset discovery, web application assessment, API assessment, and validation are the strongest early technical capability set.
3. Findings must be validated against the actual target and cannot rely on scanner output alone.
4. Attack-path analysis is important because real risk is often a combination of issues rather than a single defect.
5. Remediation and retesting are essential to the product’s credibility and trust model.
6. Authorisation, scope control, and stop-testing rules are not optional; they are central to the product’s purpose.
7. The product should support human oversight in high-risk or privileged testing scenarios.

## 4. Highest-priority capabilities

The strongest early capability focus is:

- external attack surface discovery,
- web application security testing,
- API security assessment,
- identity and access review,
- vulnerability validation and evidence handling,
- remediation guidance,
- retesting and verification,
- reporting and risk communication.

This set aligns with real customer pain and with the product’s security-assessment purpose.

## 5. Use cases requiring further validation

These should not yet be assumed to be core to the first product release without customer validation:

- continuous monitoring at scale,
- broad cloud posture automation across diverse environments,
- invasive privilege escalation or exploit-like validation beyond clearly approved circumstances,
- high-risk attack-chain testing requiring significant human oversight,
- highly specialised MSP-delivered workflows that depend on strong professional review.

## 6. Decisions requiring founder approval

The following should be reviewed by the founder before being treated as final strategic commitments:

1. Whether the first release should focus on web/app assessment and API testing before broader infrastructure or cloud scope.
2. Whether the initial customer target should be software companies and SaaS businesses before broader MSP or enterprise security offerings.
3. What level of automation is acceptable for active validation versus reporting and remediation support.
4. The acceptable level of human involvement in high-risk testing and remediation sign-off.
5. Whether delivery should begin with project-based or recurring subscription models, or a hybrid model.
6. The level of allowed testing for cloud and infrastructure review in early product stages.

## 7. Key product implications

The AI Hacker should be designed as a disciplined security assessment agent with clear evidence rules, careful scope control, structured reporting, and mandatory retest before closure. The strongest product value is not the number of potential issues it can list, but the quality of the investigation, the credibility of the evidence, and the usefulness of the remediation guidance.

## 8. Final summary

The Day 5 analysis confirms the central design direction: the AI Hacker should be a controlled, evidence-backed security investigation system capable of authorised testing, validation, remediation support, and verification. It must remain within its approval model and should not drift toward a general-purpose exploitation platform or a passive scanning tool.
