# Day 1 Product Definition

## 1. Company and product context

ZAR HORIZON (Pty) Ltd is the parent company. Its technology division, ZAR HORIZON AI @WORK, is building specialist AI digital employees designed to operate in real business and security contexts.

This Day 1 product definition establishes the approved foundation for the platform and for the two independent product lines.

## 2. Product definitions

### AI Business Partner

The AI Business Partner is an AI-powered digital business employee intended to help entrepreneurs and businesses across the lifecycle of business creation, operation, and growth.

It supports:

- research and validation,
- market and commercial intelligence,
- business operations management,
- execution of approved workflows,
- evidence-backed decision support.

It must behave as a practical business operating partner, not a generic chatbot.

### AI Hacker

The AI Hacker is an AI-powered red-team digital employee designed to investigate and validate the security of authorised systems before malicious actors can exploit weaknesses.

It supports:

- reconnaissance and asset discovery,
- vulnerability discovery,
- offensive security testing within authorised scope,
- security intelligence and human review,
- remediation verification and retesting.

It must behave as a disciplined ethical security specialist, not a passive scanner.

## 3. Product comparison

| Area | AI Business Partner | AI Hacker |
| --- | --- | --- |
| Primary purpose | Business support and execution | Authorised security testing |
| Core context | Business operations, strategy, commercial workflows | Security testing, validation, attack-path review |
| Typical outputs | proposals, reports, lead lists, quotes, monitoring summaries | findings, validation notes, impact assessment, remediation guidance |
| Primary risk | commercial or operational mistakes | security overreach or uncontrolled testing |
| Control model | permissioned business actions | explicit authorisation and scope boundaries |
| Evidence requirement | validated business facts and recommendations | validated vulnerabilities and evidence-backed conclusions |

## 4. Shared capabilities

Both products require a common enterprise foundation for:

- user authentication,
- organisation and workspace management,
- multi-tenant separation,
- subscription and usage management,
- audit logging,
- notifications,
- execution history,
- user permissions,
- document storage,
- integrations,
- AI provider configuration.

This common platform delivers operational consistency while preserving independent specialist execution boundaries.

## 5. Independent responsibilities

The two specialist systems are deliberately independent.

The Business Partner must not have access to offensive security tools or security testing execution capabilities.

The Hacker must not inherit business financial execution permissions or commercial workflow privileges.

Shared infrastructure does not mean shared authority.

## 6. Execution philosophy

Both products must follow the same high-level operating model:

RESEARCH → REASON → USE TOOLS → EXECUTE → VERIFY → REPORT.

This means each product must:

- gather relevant information,
- interpret context and constraints,
- use approved tools and workflows,
- perform authorised actions where allowed,
- verify completion or risk status,
- report clearly with evidence.

The products are not passive advisors; they are operational digital employees operating within defined permissions.

## 7. Boundaries

The Business Partner is bounded to business, commercial, and operational tasks.

The Hacker is bounded to authorised security testing, investigation, validation, and remediation support.

The shared platform enforces separation by role, workspace, tenant, and permission model. It does not allow the product lines to share authority simply because they are built on the same foundation.

## 8. Key architectural implications

These decisions establish the architectural direction:

- two independent product systems sharing a platform foundation,
- independent configuration, permissioning, and tool boundaries,
- no cross-product capability inheritance,
- enterprise-grade auditability for execution,
- strong control of sensitive action types,
- evidence-backed reporting as a product requirement.

This design supports both business automation and ethical security testing without collapsing one domain into the other.

## 9. Decisions established on Day 1

The following decisions were already approved by the founder and are now established as product foundation decisions:

- Two separate AI products.
- Both agents must execute actual work.
- Shared platform with independent agent engines.
- South Africa as the initial target market.
- Evidence-backed results.
- Human approval for sensitive operations.
- Advanced offensive security capabilities within authorised scope.
- Existing AI models initially rather than training our own foundation model.

These decisions are considered FOUNDER APPROVED.

## 10. Product quality expectations

Both products must be documented in a way that is actionable for engineers and product teams. The specification must describe what the agent does, what information it uses, what permissions it needs, what outputs it generates, and how success is verified.

The documentation must clearly distinguish:

- current product vision,
- expected capabilities,
- future capabilities,
- areas still requiring research,
- decisions not yet approved.

No capability should be described as implemented if it is only a future vision or aspiration.

## 11. Conclusion

This Day 1 product definition defines the approved foundation for ZAR HORIZON AI @WORK. It preserves the founder-approved intent: two independent digital employees, each acting as a capable specialist within defined permissions, supported by a shared enterprise platform that enforces separation and accountability.
