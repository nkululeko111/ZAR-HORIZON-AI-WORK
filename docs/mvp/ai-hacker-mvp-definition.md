# AI Hacker MVP definition

## Objective

Define the first commercially useful version of the AI Hacker product. The MVP must remain within the founder-approved vision: an authorised, execution-oriented red-team AI that investigates, validates, reports, and verifies remediation within explicit boundaries.

## MVP recommendation

### Primary MVP workflow: authorised web application and API security assessment

The recommended first workflow is an authorised web application and API security assessment that takes a customer from authorisation and scope definition through assessment, validation, reporting and remediation verification.

The workflow includes:

1. organisation and asset registration;
2. proof of authorisation and scope definition;
3. test plan approval;
4. authorised discovery of the application and API surface;
5. assessment of relevant application and API risk areas;
6. investigation of identified issues;
7. controlled validation of eligible findings;
8. evidence capture and business-impact assessment;
9. remediation guidance and report generation;
10. retesting of approved fixes;
11. final verification status to the customer.

This is the strongest MVP candidate because it combines real customer value, clear authorisation boundaries, manageable testing scope, and strong evidence requirements.

## Why this workflow fits the MVP

- It reflects a major customer pain point: organisations need a faster and more structured way to assess web and API risk.
- It is within realistic product scope and can be delivered with explicit control points.
- It supports the security product requirement that findings must be evidenced, not merely scanned.
- It creates a credible, audit-friendly flow that can be repeated for specific products or organisations.
- It preserves the product’s trauma-free focus on explicit permission and responsible testing.

## MVP feature set

### P0 foundation features

These are essential to a safe, credible first release.

| Feature | Customer problem | Target user | Security value | Required permissions | Inputs | Outputs | Execution behaviour | Tool dependencies | Human approval | Safety controls | Verification method | Complexity | MVP recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Organisation onboarding and asset registration | Customers need a structured way to define what is in scope | Security lead, service provider, app owner | Establishes test boundaries | Organisation identity, verified authority | Customer profile, asset inventory, target list | Registered scope record | Captures authorised targets and context | Asset registry and workspace tools | Required for customer identity and asset registration | Tenant isolation and permission model | Registration checklist review | Low | P0 |
| Authorisation and scope management | Security testing must be limited to approved systems | Security team, organisation owner | Prevents uncontrolled testing | Written or approved test authority | Scope, exclusions, target asset list, test window | Authorisation record | Restricts execution to approved assets, flows and time windows | Workflow and approval engine | Required | Stop-testing triggers, scope enforcement | Audit trail and approval status | Medium | P0 |
| Controlled reconnaissance | Customers need early visibility into the external surface without over-testing | Security analyst | Establishes safe baseline understanding | Authorised asset list | Allowed domain names, targets, exclusions | Asset inventory and discovery summary | Executes only approved discovery activities | DNS, discovery, and web enumeration tools | Required for active tests | Passive-first and bounded active probes | Output reviewed against scope | Medium | P0 |
| Web application assessment | Applications are common attack surfaces | AppSec team, engineering lead | Identifies exposed control weaknesses | Approved app URLs, access permissions, test accounts | App URLs, app metadata, test environment access | Security assessment output | Discovers routes, tests auth and input handling | Web app scanners and test tools | Required for risky or high-impact flows | Strict scope limits and test account separation | Findings supported by evidence | High | P0 |
| API assessment | APIs are a major operational risk surface | AppSec team, engineering lead | Identifies auth, validation and exposure issues | Authorised API endpoints and test accounts | API docs, auth methods, test credentials | API finding set | Checks auth, rate limits, input validation and exposure | API test tools and payload tooling | Required for privileged flows | Separate test credentials and environment isolation | Evidence record with reproduction conditions | High | P0 |
| Vulnerability investigation and validation | Scanner signals must not be treated as proof | Security analyst, engineer | Reduces false positives and supports trust | Authorised scope and access | Finding candidates, target behaviour, logs | Confirmed or suspected finding record | Investigates and validates behaviour within scope | Security tooling and manual review | Required for high-risk validation | Bounded validation only | Reproduction evidence and status | High | P0 |
| Finding classification and confidence | Customers need to know what is real, likely or uncertain | Security lead, developer | Supports prioritisation and action | Finding set and evidence | Status-labelled findings | Confirmed/suspected/informational classification | Compares evidence to actual behaviour | Evidence analysis and documentation | Moderate | No unsupported confidence claims | Evidence record review | Medium | P0 |
| Remediation guidance | Customers need actionable next steps | Developer, security engineer | Reduces time to fix | Vulnerability details, affected components | Remediation plan | Explains root cause and fix direction | Uses code, config and service analysis | Code review and config context | Low to moderate | No fix is claimed without verification | Evidence-based fix recommendation | Medium | P0 |
| Retesting and fix verification | Customers need to know whether the issue is actually resolved | Security lead, developer | Validates fix quality | Remediation actions and prior finding context | Retest result | Re-runs relevant checks under same scope | Security test tools and verification actions | Required for re-test approval | Strict verification requirement | Must not claim resolution without evidence | Retest evidence and closure status | Medium | P0 |
| Reporting and evidence pack | Stakeholders need a clear summary and record | Security lead, business owner | Makes risk understandable and auditable | Findings, test scope, evidence record | Executive and technical report | Produces structured reports | Reporting engine with evidence attachments | Documentation and report templates | Moderate | Must separate assumptions from verified results | Report checks and evidence review | Medium | P0 |

### P1 differentiating features

These strengthen the product but are not essential to the first release.

| Feature | Customer problem | Target user | Security value | Required permissions | Inputs | Outputs | Execution behaviour | Tool dependencies | Human approval | Safety controls | Verification method | Complexity | MVP recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Identity and access review | Organisations need to understand access risk | IAM or security lead | Identifies privilege and auth problems | Authorised systems and credentials | Auth model, role definitions | Access review findings | Tests role boundaries within scope | IAM and auth tooling | Required for risky privilege checks | Does not include credential misuse | Correlation with actual access behaviour | High | P1 |
| Attack path analysis | Finding lists are not enough; customers want realistic paths | Security lead, IT team | Helps explain business risk | Authorised asset and finding context | Vulnerability set and environment data | Attack path summary | Correlates findings into likely exposure paths | Asset and network context | Moderate | Must remain within approved scope | Path evidence and business impact review | High | P1 |
| Cloud configuration review | Customers need to understand public exposure and permission drift | Cloud security lead | Reduces cloud risk | Authorised cloud access and permissions | Cloud metadata, identities, configs | Cloud security finding set | Reviews authorised cloud assets and settings | Cloud integrations or authorised access | Required | Must not exceed cloud role scope | Evidence from config review and asset state | High | P1 |
| False-positive handling and deduplication | Large volumes of issues can overwhelm teams | Security analyst | Improves trust and triage quality | Findings and evidence context | Finding corpus | Deduplicated and triaged results | Compares evidence and duplicates | Evidence records and correlation engine | Low | No automatic closure without evidence | Re-test and review status | Medium | P1 |
| Continuous monitoring | Customer wants repeat risk visibility | Security lead | Helps reduce blind spots | Continued scope and authorisation | Asset inventory and change triggers | Change-based findings and monitoring reports | Re-assesses authorised scope | Monitoring and alerting | Required for ongoing access | Controlled and explicitly contracted | Reassess and confirm changes | High | P1 |

## Primary workflow candidate selection

### Candidate A: authorised web application and API assessment

Strong points:

- immediate and visible value to a broad set of customers;
- strong relevance to digital businesses and SaaS customers;
- clear fit for security testing and evidence-driven reporting;
- realistic authorisation and workflow model.

Weak points:

- can become a broad product scope if not disciplined;
- requires careful management of test accounts, auth flows and business logic testing.

### Candidate B: continuous attack surface and vulnerability validation

Strong points:

- appealing for ongoing security assurance;
- good for customers that want regular change validation.

Weak points:

- often more complex operationally;
- can drift into “always-on scanner” territory if not tightly scoped;
- should not automatically be treated as a first release requirement.

## Recommended primary workflow

The recommended primary workflow is Candidate A: authorised web application and API security assessment.

The reason is simple: this workflow demonstrates the product’s core value clearly while staying controllable and evidence-driven. It also aligns with the founder-approved AI Hacker definition and the product’s emphasis on clear boundaries, validation, and business-impact assessment.

## MVP exclusions

The following are intentionally excluded from the first release:

- broad autonomous exploitation across the entire enterprise estate;
- unrestricted network scanning beyond the authorised scope;
- destructive or high-risk exploitation testing;
- privilege-escalation testing beyond explicit, tightly controlled approval;
- continuous client-side monitoring without a clear customer contract and operational model;
- broad cloud security assessment without explicit cloud access and governance;
- highly invasive data extraction testing unrelated to the approved test objective;
- assumptions that a scanner hit is equivalent to a confirmed vulnerability.

## Risks and unresolved assumptions

- Customers may expect more autonomous testing than is safe or commercially appropriate.
- Security buyers often want broader coverage than the MVP can support.
- Some customers will confuse AI security tooling with full human-led consulting or red-team service levels.
- Retesting and evidence handling must remain disciplined to prevent false closure.

## MVP decision status

These are preliminary product recommendations only and are not founder-approved scope decisions.
