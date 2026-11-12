# AI Business Partner user experience

## 1. Product experience goal

The AI Business Partner should feel like a practical business command centre for a founder, manager, or operations user. It should help the user understand business health, identify issues, review opportunities, decide on actions, and track execution outcomes.

This experience should be operational and evidence-based. It should not feel like a generic AI chatbot with a dashboard attached.

## 2. Main navigation

Recommended MVP navigation structure:

- Overview
- My Business
- Financials
- Business Intelligence
- Tasks and Actions
- Documents
- Research
- Activity
- Settings

### Future or deferred items

Items that should be marked as future or not in MVP include:

- supply-chain orchestration,
- advanced predictive planning,
- broader sales automation,
- large external workflow orchestration,
- open-ended autonomous actions.

## 3. Default dashboard

The default dashboard should present the business owner with a concise operational picture. It should be readable at a glance and should clearly indicate missing information.

### Dashboard modules

- Business health overview
- Revenue and expense snapshot
- Cash-flow summary
- Profitability and margin
- Performance trends
- Tasks and approvals
- Important business issues
- Opportunities
- Recommended next actions
- Recent agent activity

### Dashboard behaviour with incomplete information

When the business has insufficient data, the dashboard should:

- show a partial state rather than misleading numbers,
- say exactly what data is missing,
- provide next-step guidance,
- keep imported and derived data visibly separated,
- show no fabricated metrics.

Example empty state:

- “No financial records imported yet. Import invoices, revenue or expense data to unlock dashboard analytics.”

## 4. Financial workspace

### Financial data import

The import screen should support:

- source selection,
- import type,
- file or integration selection,
- data quality checks,
- mapping review.

The user should see:

- uploaded records,
- validation issues,
- unresolved mapping items,
- last imported timestamp.

### Data quality and distinction

The UI must clearly distinguish:

- imported source data,
- calculated financial metrics,
- AI-generated interpretation,
- assumptions and estimates.

This can be done via labelled panels and visual metadata such as badges.

### Financial summary views

- Revenue and expenses
- Cash-flow summary
- Profitability and margins
- Budget vs actuals
- Reporting periods

Each view should include:

- time period selector,
- data source badge,
- assumptions panel,
- validation status,
- export or document action.

## 5. Business intelligence workspace

The business intelligence experience should let the user ask natural questions while also showing structured analytical output.

Examples:

- “Why is profitability down this month?”
- “Which area is most affecting cash flow?”
- “What opportunity should we pursue next?”

### Analysis detail layout

Each analysis result should include:

- question or business objective,
- summary of findings,
- evidence list,
- issues identified,
- opportunities,
- recommendations,
- recommended actions,
- confidence or confidence status,
- action approval state.

Critical requirement: the user must be able to inspect why the agent reached a conclusion, not just see a summary.

## 6. Action and task workspace

This workspace must distinguish workflow states clearly.

Required statuses:

- proposed,
- pending approval,
- approved,
- executing,
- completed,
- failed,
- verified.

### Proposed action detail

The detail view should show:

- action title,
- affected business objective,
- parameters,
- risk and approval requirements,
- evidence behind recommendation,
- reason for the action,
- approval decision controls.

### Execution tracking

The user should be able to:

- view the action progress,
- review related tasks,
- see errors or blocked steps,
- check verification status,
- review outcomes.

## 7. Business Partner AI interaction model

The interaction experience should not be a generic chat-only screen. It should combine a natural-language assistant with structured workflow panels.

The user can ask questions naturally, but the system should present them through guided steps:

1. understand business context,
2. review business data,
3. identify issue or opportunity,
4. present evidence,
5. propose practical actions,
6. request approvals,
7. execute approved work,
8. report outcomes.

Example prompt:

“I want to increase monthly revenue by R30,000.”

The response should show:

- current revenue baseline,
- relevant opportunity areas,
- supporting business evidence,
- recommended action plan,
- approval options,
- execution and verification tracking.

## 8. Design principles for this product

- Practical over decorative.
- Evidence over speculation.
- Clear action status over vague “AI summary”.
- Small-business usability over enterprise complexity.
- Approvals are visible and explicit.
- Financial logic must be distinguishable from AI interpretation.

## 9. Summary

The Business Partner UX should feel useful to a founder or manager on day one. It should help the user understand the business, review evidence, act on approved recommendations, and confidently track what happened after a proposed action was executed.
