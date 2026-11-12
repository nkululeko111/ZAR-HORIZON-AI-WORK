# Product readiness assessment

## Overall product finding

Both products have a documented vision, but neither has a founder-approved, customer-validated, implementation-ready MVP contract. The product definitions are useful as design inputs; scope, customer evidence, and implementation dependencies still need decisions.

## Product and market alignment

| Dimension | AI Business Partner | AI Hacker |
|---|---|---|
| Intended customer | Entrepreneurs/SMEs and business operators; exact initial buyer/segment remains to be confirmed | Security teams and organisations needing authorised assessments; exact initial buyer/segment remains to be confirmed |
| Core problem | Fragmented business information and difficulty turning it into informed, practical action | Cost and complexity of producing controlled, evidence-backed security assessments |
| Value proposition | A business execution partner combining business context, analysis, recommendations, approved actions, and verification—not just a chat interface | A controlled assessment workflow supporting scope, investigation, evidence, reporting, and retesting—not unrestricted automated hacking |
| Product lifecycle | Business context and data → analysis → recommendation → approval where needed → action → verification | Customer/assets → authorisation and scope → controlled assessment → evidence/findings → remediation → retest/report |
| MVP state | Recommended business-performance/action workflow exists; final scope and founder approval are unresolved | Recommended authorised web/API assessment workflow exists; final scope and founder approval are unresolved |
| Commercial model | Subscription/pricing assumptions exist but require buyer and willingness-to-pay validation | Commercial delivery/pricing assumptions exist but require buyer validation and a credible safe execution model |
| Customer evidence | No completed interviews recorded in the tracker | No completed interviews recorded in the tracker |

The market-research and competitive-research documents provide hypotheses and reference material, not proof of demand or product-market fit. Do not claim that customer segments or pricing have been validated until interviews and outcomes are recorded.

## AI Business Partner

### Strengths in the specification

- Positions the product as an execution-oriented business partner rather than a generic chatbot.
- Defines business context, operational workflows, business intelligence, and action boundaries across product, use-case, MVP, API, and UX documentation.
- Recognises that financial calculations must be deterministic and auditable, with recommendations grounded in sources and clear assumptions.
- Includes approval and execution concepts rather than treating generated advice as permission to act.

### Readiness gaps before a first usable version

- Confirm the first buyer, target SME profile, exact first workflow, and what measurable outcome constitutes MVP success.
- Specify supported financial data sources and initial import formats, period/currency handling, duplicate detection, and the behavior for incomplete or conflicting records.
- Approve calculation definitions and assumptions for revenue, expenses, margins, cash flow, and VAT treatment; distinguish bookkeeping/tax advice from operational analysis.
- Define the first source-attribution and evidence model, including how a user can correct or reject imported data.
- Bound market and supplier research by approved sources, recency, comparison criteria, and source attribution; specify which generated documents are in scope, what evidence they cite, and how they are reviewed or approved.
- Select which recommendations can be informational only and which can lead to external actions; define approval, idempotency, failure, and post-action verification semantics.
- Specify operational task/action ownership, lifecycle states, execution verification, and a bounded first integration set. These are dependencies, not permission to add integrations without approval.
- Preserve the boundary that the product is not a replacement for an accountant, tax professional, or other regulated adviser.

### Assessment

**Ready with conditions for discovery and a bounded design-to-implementation plan; not ready for broad product implementation.** A narrow deterministic analysis slice is plausible after the founder selects the workflow and data source and the shared authorization/approval baseline is resolved. The lower relative execution risk compared with AI Hacker does not establish customer demand.

## AI Hacker

### Strengths in the specification

- Clearly requires customer authorisation, explicit scope, evidence, and controlled assessment.
- Separates security assessment permissions from Business Partner commercial permissions.
- Documents assessment, finding, reporting, and remediation concepts, with safety-oriented negative tests.
- Explicitly excludes unrestricted testing and external-target activity from this planning stage.

### Safety and commercial trust gaps before implementation

- Define how customer identity and authority to approve assets are verified and recorded.
- Decide the canonical scope representation, exclusions, test window, permitted methods, and how scope changes invalidate prior approval.
- Specify the isolated worker boundary, network egress allowlist/deny model, credential injection and redaction, resource limits, and emergency-stop behavior.
- Define which tools and actions are permitted at each risk level and how backend enforcement prevents a model/tool from exceeding those grants.
- Define finding severity/confidence evidence requirements, false-positive review, evidence integrity/provenance, and remediation/retest verification.
- Define cancellation and containment behavior for active jobs, including partial results and audit records.
- Approve the first assessment methods and the boundary between asset discovery, web testing, API testing, vulnerability validation, reporting, and retesting; the current web/API MVP is a recommendation, not an approved scope.
- Build only against intentionally vulnerable local fixtures or explicitly controlled environments after the required design and isolation are approved. No live security testing was performed for this audit.

### Assessment

**Not ready for automated security-execution implementation.** Safe product discovery and non-executing workflow design may proceed. Any capability that sends traffic, uses credentials, or validates vulnerabilities must remain blocked until authorisation, scope, isolation, network controls, approval, emergency stop, and evidence handling are implementable and tested.

## First-product recommendation

The recommended first implementation focus is **AI Business Partner**, narrowly scoped to a deterministic, evidence-backed business-performance workflow, conditional on customer discovery and founder approval. It has a lower execution-risk profile than autonomous security assessment and is more compatible with starting from local data analysis before external actions.

This is a recommendation, not founder approval. Risks include poor or incomplete SME records, data-access friction, financial error and trust, and unvalidated willingness to pay. If customer evidence favors AI Hacker, do not relax its controls; start with a human-led, controlled assessment workflow after safety decisions are resolved.

## Evidence references

- Product vision: `../products/day-01-product-definition.md`
- Product specifications: `../products/business-partner-product-specification.md`, `../products/ai-hacker-product-specification.md`
- Market assumptions: `../market-research/`
- Interview plan and tracker: `../customer-validation/day-03-validation-strategy.md`, `../customer-validation/customer-validation-tracker.csv`
- Recommended MVP and pending choices: `../mvp/day-07-mvp-decisions.md`, `../mvp/founder-mvp-decision-register.md`
- Business Partner and AI Hacker workflows: `../use-cases/business-partner/`, `../use-cases/ai-hacker/`
