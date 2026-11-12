# AI Hacker Capability Catalogue

## 1. Purpose

This catalogue defines the execution-oriented capabilities of the AI Hacker product. It reflects the founder-approved vision: this is not a passive scanner or generic chatbot. It is an authorised offensive-security assistant designed to investigate, test, validate, report, and support remediation within defined boundaries.

The product must support the lifecycle of security investigation and assessment, from onboarding and authorisation through testing, evidence collection, remediation guidance, retesting, and reporting.

## 2. Product positioning and execution model

The AI Hacker operates under the high-level model:

RESEARCH → REASON → USE TOOLS → EXECUTE → VERIFY → REPORT.

The product must do more than identify possible issues. It must:

- discover assets and system exposure,
- assess attacker-relevant behaviours,
- validate whether a vulnerability is real,
- explain business and technical impact,
- support remediation and retesting,
- provide evidence-backed reporting with clear status labels.

It must never treat a scanner alert or a CVE match as proof of an exploitable issue.

## 3. Capability domains

### A. Asset discovery and reconnaissance

1. Domain and subdomain discovery
2. DNS and infrastructure information gathering
3. Public-facing asset identification
4. Network service discovery
5. Technology fingerprinting
6. Web application discovery
7. API endpoint discovery
8. Cloud asset inventory in authorised environments
9. Attack surface mapping
10. Asset relationship mapping

### B. Web application security testing

11. Authentication weakness review
12. Session management assessment
13. Access control and authorisation review
14. Input validation testing
15. Injection vulnerability review
16. Security misconfiguration assessment
17. Sensitive data exposure review
18. File upload security review
19. Business logic testing
20. API security testing within web applications
21. HTTP security header and transport checks
22. Third-party component and dependency risk review

### C. API security testing

23. API discovery and inventory
24. Authentication testing
25. Authorisation testing
26. Object-level access control review
27. Rate limiting and abuse protection review
28. Input validation testing
29. Data exposure assessment
30. API configuration weakness review
31. Token and session handling review
32. Business logic testing for APIs

### D. Network and infrastructure security

33. Host discovery
34. Port and service discovery
35. Service version identification
36. Network exposure assessment
37. Configuration weakness review
38. Insecure protocol review
39. Firewall and segmentation review
40. Infrastructure vulnerability assessment
41. Administrative exposure review

### E. Cloud and configuration security

42. Cloud asset inventory
43. Identity and access configuration review
44. Excessive permissions assessment
45. Publicly exposed resource review
46. Storage configuration weakness review
47. Secret exposure review
48. Logging and monitoring gaps review
49. Security configuration assessment
50. Cloud workload exposure review

### F. Identity and access security

51. Authentication mechanism review
52. Multi-factor configuration review
53. Privilege boundary testing
54. Role-based access control review
55. Excessive permission review
56. Account lifecycle weakness review
57. Session security review
58. Privilege escalation risk assessment

### G. Vulnerability intelligence and validation

59. Potential vulnerability identification
60. Correlation against known vulnerability intelligence
61. Validation of target relevance
62. Safe controlled validation procedures
63. Suspected vs confirmed finding classification
64. Exploitability and practical impact assessment
65. Duplicate detection and deduplication
66. Severity assignment with evidence

### H. Attack path and risk analysis

67. Single-finding correlation
68. Multi-step attack path analysis
69. Business impact assessment
70. Combined weakness evaluation
71. Exploitation feasibility assessment
72. Stakeholder risk prioritisation

### I. Remediation and verification

73. Vulnerability communication and explanation
74. Remediation recommendation generation
75. Affected component and dependency identification
76. Code and configuration fix guidance
77. Developer-facing remediation ticket creation
78. Prioritised remediation plan
79. Retest and verification workflow
80. Fix validation and closure tracking

## 4. Detailed capability definitions

### 4.1 Asset discovery and reconnaissance

#### Capability: Domain and subdomain discovery

- Objective: identify the scope of externally visible assets.
- Inputs: authorised target domains, scope details, exclusions.
- Outputs: discovered hostnames, service inventory, exposure summary.
- Safety status: passive reconnaissance and approved active probing only.

#### Capability: Technology fingerprinting

- Objective: identify technologies, frameworks, versions, and exposed components.
- Outputs: technology inventory and likely platform characteristics.
- Verification: match against observed service behaviour and authorised framework details.

### 4.2 Web application security testing

#### Capability: Authentication and session review

- Objective: assess whether login flows and session controls are strong enough.
- Inputs: authorised application URLs, test accounts, admin role access if specifically approved.
- Outputs: session and authentication risk notes, recommended fixes.
- Human oversight: required for any account or privilege-level testing beyond the approved test set.

#### Capability: Input validation and injection review

- Objective: determine whether dangerous input handling patterns exist.
- Outputs: vulnerability notes, reproduction conditions, and evidence chain.
- Safety: only validated, controlled testing within approved application scope.

### 4.3 API security testing

#### Capability: API discovery and auth review

- Objective: identify API endpoints and assess their authentication and authorisation posture.
- Inputs: API routes, documentation, access to a test environment, authorised credentials.
- Outputs: inventory, security findings, control gaps, and remediation steps.

### 4.4 Network and infrastructure security

#### Capability: Service discovery and infrastructure review

- Objective: identify exposed hosts, ports, protocols, and services.
- Output: asset inventory with version summary and exposure risk.
- Safety: must remain within authorised scope and assess only intended targets.

### 4.5 Cloud and configuration security

#### Capability: Cloud configuration review

- Objective: detect public exposure, permission drift, storage risk, secret leakage, and insecure service configuration.
- Inputs: authorised cloud access, scope details, asset inventory.
- Outputs: cloud security finding set with business impact and evidence.
- Critical condition: access and credentials must be explicitly authorised and restriction-aware.

### 4.6 Identity and access security

#### Capability: Privilege boundary assessment

- Objective: determine whether roles and permissions are excessive or inconsistent.
- Outputs: risk notes, privilege analysis, and remediation guidance.
- Safety: any privilege escalation validation must be controlled and specifically authorised.

### 4.7 Vulnerability intelligence and validation

#### Capability: Confirmed vs suspected findings

- Objective: avoid false confidence by separating a scanner signal from a validated issue.
- Outputs: finding status and confidence rating.
- Rule: a CVE match or scanner alert is not proof unless confirmed against the tested asset and the actual behaviour.

### 4.8 Attack path and risk analysis

#### Capability: Correlate findings into attack paths

- Objective: identify how multiple weaknesses combine into a meaningful security risk.
- Inputs: validated findings, asset inventory, architecture context, business impact.
- Outputs: attack path narrative, impact assessment, and remediation priority.

### 4.9 Remediation and verification

#### Capability: Retesting after remediation

- Objective: confirm the fix actually removed or reduced the issue.
- Outputs: retest evidence, updated status, and closure notes.
- Rule: do not claim a finding is remediated unless verification has been performed.

## 5. Required evidence for every finding

Every reported issue must state:

- affected asset or system,
- attack category or weakness,
- how it was identified,
- whether it is validated or only suspected,
- technical evidence,
- reproduction conditions if applicable,
- impact assessment,
- remediation recommendation,
- validation status.

## 6. Product boundaries

The AI Hacker must not autonomously:

- test systems without explicit authorisation,
- exceed scope or target boundaries,
- run high-risk destructive actions,
- attempt credential theft or exploit activities beyond approved boundaries,
- persist malicious access or backdoor functionality,
- act without audit logging and approval.

## 7. Summary

The AI Hacker capability catalogue defines a security agent that is operational, evidence-driven, tightly controlled, and specific to authorised testing. Its value is not in scanning for a broad list of potential issues; it is in investigating, validating, reporting, and helping teams remediate real security problems under proper controls.
