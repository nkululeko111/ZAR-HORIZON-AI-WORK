# AI Hacker feature prioritisation

## Priority scale

- P0 = Essential foundation
- P1 = MVP differentiator
- P2 = Post-MVP
- P3 = Future research
- Excluded = outside agreed product scope or not justified in the first release

## Feature matrix

| Feature | Priority | Rationale |
|---|---|---|
| Organisation onboarding and asset registration | P0 | Required to ensure scope and ownership are explicit. |
| Authorisation and scope management | P0 | Core safety requirement; without it the product is unsafe and non-compliant with the product definition. |
| Controlled reconnaissance | P0 | Needed to create a safe, bounded baseline for the assessment. |
| Web application assessment | P0 | A high-value and highly relevant initial assessment capability. |
| API assessment | P0 | High-value, repeated and commercially meaningful. |
| Vulnerability investigation and validation | P0 | Necessary to distinguish real issues from suspected ones. |
| Finding classification and confidence | P0 | Required for trust, reporting and actionability. |
| Remediation guidance | P0 | Needed to convert findings into useful customer outcomes. |
| Retesting and fix verification | P0 | Required so the product does not claim remediation without proof. |
| Reporting and evidence pack | P0 | Essential for auditability, trust and customer communication. |
| Identity and access review | P1 | Valuable but should be introduced carefully due to permission and access complexity. |
| Attack path analysis | P1 | Strong differentiator but not required to deliver the first customer workflow. |
| Cloud configuration review | P1 | Valuable for cloud-centric customers but dependent on explicit cloud access and governance. |
| False-positive handling and deduplication | P1 | Important for usability but can be layered after the first release. |
| Continuous monitoring | P1 | Useful but should not be treated as automatic MVP due to operational complexity and risk. |
| Broad network infrastructure assessment | P2 | Valuable, but can be broader and more operationally intrusive than the first-release need. |
| Deep privilege escalation and exploit validation | P2 | Important in security practice but risky and requires specialist oversight and clear approval. |
| Advanced threat emulation and multi-stage exploitation | P3 | High complexity and matrix of risk; needs stronger customer validation and governance. |
| Unrestricted testing beyond approved scope | Excluded | Violates founder-approved boundaries and safety requirements. |
| Destructive exploitation or destructive DoS testing | Excluded | Explicitly prohibited under the product rules. |
| Credential theft or misuse | Excluded | Prohibited and outside the definition of authorised testing. |
| Unauthorised production impact testing | Excluded | Not acceptable and must remain out of scope. |

## Why P0 and P1 matter most

P0 features are the minimum safe and credible release for AI Hacker. Without them, the product would not be a responsible security testing product.

P1 features make the product more differentiated and commercially valuable, but they should be introduced only after the core workflow is stable and customer trust is established.
