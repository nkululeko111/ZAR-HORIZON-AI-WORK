# AI Business Partner MVP definition

## Objective

Define the first commercially useful version of the AI Business Partner. The focus is on a complete business workflow that a small business owner or operator can use repeatedly, with clear approval points and evidence-backed output.

## MVP recommendation

### Primary MVP workflow: business performance and action agent

The recommended first workflow is a business performance and action agent that helps an owner or manager:

1. understand the state of the business;
2. analyse available revenue, expense and operational information;
3. identify trends, gaps or opportunities;
4. explain the evidence behind the conclusion;
5. propose a practical action;
6. create approved business documents or tasks;
7. execute approved actions through authorised tools;
8. track progress and report the outcome.

This is the strongest first-release candidate because it combines recurring value, realistic data availability, manageable complexity and clear execution boundaries.

## Why this workflow fits the MVP

- It addresses a frequent and high-friction customer pain point: business owners need more clarity and action, not more reporting.
- It can operate with a realistic data set: revenue, expenses, sales records, tasks, documents, supplier information and approved workflow actions.
- It produces outputs that are immediately actionable: summaries, tasks, budget comparisons, quotations, performance notes and business documents.
- It supports execution without requiring the product to become an unmanaged autopilot.
- It retains the founder-approved operating philosophy: research → reason → use tools → execute → verify → report.

## MVP feature set

### P0 foundation features

These are essential to a first-release product that can operate sensibly and safely.

| Feature | Customer problem | User | Business value | Inputs required | Expected output | Execution behaviour | Required integrations | Approval requirements | Verification method | Complexity | Dependencies | MVP recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Business profile and context setup | User must define what the business does, where it operates, and how it makes money | Founder, SME owner, manager | Provides the foundation for all business analysis | Business description, products/services, geography, target customers | Structured business profile | Agent captures and organises info | Minimal | Low | Structured profile review | Low | None | P0 |
| Business information ingestion | Product must understand user-supplied business data | SME owner | Enables relevant analysis | Revenue, expenses, sales info, supplier info, task records | Organised business data model | Reads and structures data | Spreadsheet, CRM, accounting or document imports if available | Low | User confirms imported information | Medium | Data import standards | P0 |
| Revenue and expense analysis | Owners need a clear view of current performance | SME owner, operator | Helps identify cost and revenue issues | Financial data, monthly breakdowns, categories | Revenue/expense summary | Calculates and interprets trends | Accounting integrations or manually uploaded files | Low | Review of calculations and source data | Medium | Data quality and categorisation | P0 |
| Cash-flow visibility and summary | Cash-flow problems are critical in SMEs | Founder, finance lead | Enables operational decision-making | Inflows, outflows, invoices, expenses, payroll if provided | Cash-flow summary and risk notes | Summarises known movement and highlights anomalies | Accounting or bank feeds if connected | Low to moderate | Compare reported numbers to source records | Medium | Data completeness | P0 |
| Profitability and margin analysis | Business owners need to know which activities make money | Owner, manager | Supports pricing and operational decisions | Sales and cost data, margin assumptions | Profitability overview and margin analysis | Performs calculations and explains drivers | Finance or accounting systems | Low | Recalculate against source data | Medium | Financial data accuracy | P0 |
| Business performance reporting | Owners need a concise operational picture | Founder, operator | Improves decision quality and reduces reporting effort | Data from finance, sales, operations | Management-style performance report | Generates evidence-backed summary | Optional integrations | Low | User reviews numbers and assumptions | Medium | Data quality | P0 |
| Business document generation | Business owners need proposals, plans and reports | Owner, manager | Saves time and standardises output | Business information and templates | Doc drafts | Generates draft files or proposals | Document storage, templates | Moderate for external sending | User validation before sharing or sending | Medium | Human review for external use | P0 |
| Task creation and coordination | Business owners need outcomes, not just advice | Owner, team lead | Supports follow-up actions | Tasks, deadlines, owners, workflows | Action list and tasks | Creates tasks and tracks status | Task tools or internal workflow system | Moderate | Task completion status and evidence | Medium | Workflow permissions | P0 |
| Approval-gated external actions | Sensitive actions require review before communication or submission | Owner or authorised user | Prevents unwanted outbound actions | Action context, customer or supplier info, communication content | Approved action or draft | Requests approval before execution | Email, CRM, messaging tools if authorised | Required | User approval log and execution record | Medium | Tool permissions and policy | P0 |
| Execution verification | Business actions must be validated after execution | Owner, operator | Builds trust and operational reliability | Action target and expected result | Verification summary | Checks workflow status or output | CRM, messaging, task systems | Low to moderate | Result proves completion | Medium | Tool-level status visibility | P0 |

### P1 differentiating features

These add valuable business-partner differentiation but are not required for the first release unless they support the primary workflow clearly.

| Feature | Customer problem | User | Business value | Inputs | Expected output | Execution behaviour | Required integrations | Approval requirements | Verification method | Complexity | Dependencies | MVP recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Market and competitor research | Founders need to validate opportunity and positioning | Founder, business development lead | Improves market awareness | Sector, geography, customer segment | Research summary with evidence notes | Researches and synthesises findings | Web search and approved research tools | Low to moderate for external use | Source quality and traceability | High | Research permissions and data quality | P1 |
| Supplier discovery and comparison | Businesses need better procurement decisions | Owner, operations lead | Reduces procurement friction | Product requirements, supplier list, pricing | Supplier shortlist and comparison sheet | Finds suppliers and compares price/terms | Search and procurement tools if available | Moderate for external quotations | Quote and terms comparison | High | Supplier data quality | P1 |
| Sales lead organisation and follow-up | Businesses struggle to manage leads and follow-ups | Sales lead, owner | Improves conversion and operational discipline | Leads, notes, outreach data | Prospect tracking list and next actions | Creates tasks and outreach drafts | CRM or contact tools | Moderate | Outcome and follow-up status | Medium | CRM data quality | P1 |
| Quotation preparation | Businesses need to draft commercial offers quickly | Sales lead, operations | Speeds commercial response | Product/service data, pricing assumptions | Customer quotation draft | Builds quote with assumptions and summary | Pricing and document tools | Moderate | User validation before sending | Medium | Pricing assumptions and approvals | P1 |
| Budget vs actual analysis | Owners need to compare plan and reality | Finance lead, owner | Helps identify underperformance | Budgets and actuals | Variance analysis | Compares expected and actual performance | Accounting or spreadsheet inputs | Low | Data source review | Medium | Budget data quality | P1 |
| Improvement recommendations | Owners need practical next steps | Founder, manager | Converts analysis into action | Business context and performance data | Recommended actions with rationale | Explains issue and proposes steps | Optional | Low to moderate | Outcome review over time | Medium | Business context | P1 |

## Primary workflow candidate selection

### Candidate A: business performance and action agent

Strong points:

- highly repeatable and practical;
- easy to relate to real-value use cases;
- strong data availability from financial records and tasks;
- good fit for a first commercial release.

Weak points:

- depends on the customer’s data being organised enough to be analysed;
- needs careful handling of assumptions and estimates.

### Candidate B: sales and supplier operations agent

Strong points:

- strong operational value for certain segments;
- useful for service businesses and businesses with lead generation challenges.

Weak points:

- more dependent on external integrations and customer data quality;
- more likely to require separate CRM and sales stack readiness.

## Recommended primary workflow

The recommended primary workflow is Candidate A: the business performance and action agent.

This is more robust for the initial MVP because it can be anchored in data the customer already has or can reasonably upload. It is less dependent on large third-party ecosystems and more likely to produce immediate action and measurable value.

## MVP exclusions

The following are intentionally outside the first-release MVP:

- full autonomous cross-system orchestration across every business tool;
- broad supplier or market intelligence at scale;
- deep partner or distributor ecosystem management;
- complex multi-entity multi-branch financial operations;
- highly autonomous external communications across multiple channels;
- full legal or compliance advisory capability;
- advanced AI-driven forecasting as a stand-alone feature without clear data quality and review.

## Risks and unresolved assumptions

- Data quality is often weaker than expected in small businesses.
- Financial information may require human review for correctness.
- The customer may demand a broader role than a core workflow offers.
- Some customer segments will expect more system integration than the MVP can support.

## MVP decision status

These are product design recommendations, not founder-approved decisions.
