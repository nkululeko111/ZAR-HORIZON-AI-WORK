# AI Business Partner architecture

## 1. Objective

The AI Business Partner is the operational business intelligence and action engine. It supports business research, planning, operating coordination, financial assessment, workflow execution, and reporting for entrepreneurs and small businesses.

The architecture must keep the agent grounded in verified business facts and maintain strict separation from security execution logic.

## 2. Logical component model

The Business Partner architecture contains these logical components:

1. Business context and profile manager
2. Business data ingestion
3. Data normalisation and quality handling
4. Financial analysis engine
5. Business intelligence and reasoning
6. Research capabilities
7. Document generation
8. Task and workflow coordination
9. Tool registry and execution
10. Approval and permission checks
11. Execution verification
12. Evidence and reporting

## 3. Component responsibilities

### Business context and profile manager

Purpose:
- maintain the current business profile,
- store organisation, goals, workflows, financial context, and target segments,
- track customer, supplier, and operational configuration.

Ownership:
- product domain for Business Partner.

Security considerations:
- business context must remain tenant-scoped,
- no cross-tenant access to customer or financial records.

### Business data ingestion

Purpose:
- accept inputs from user uploads, CRM records, documents, spreadsheets, invoices, and external integrations,
- intake structured and unstructured business data.

Supported input types:
- accounting exports,
- sales records,
- customer files,
- supplier documentation,
- email or messaging summaries,
- uploaded documents.

Security considerations:
- validate file types and ingestion limits,
- treat sensitive business data as confidential,
- maintain source provenance for all imported records.

### Data normalisation and quality handling

Purpose:
- standardise schema and field names,
- reconcile duplicates,
- flag missing values,
- separate known facts from estimates and assumptions.

This is a critical safeguard because the product must not conflate source truth with reasoning.

### Financial analysis engine

Purpose:
- calculate margins, cash flow, revenue, expenses, break-even points, forecasts, and variance trends,
- keep calculations deterministic and auditable,
- separate arithmetic from narrative interpretation.

Architecture rule:
- the financial engine must use deterministic calculations and explicit formulas;
- the LLM may explain patterns but should not be treated as the source of truth for arithmetic.

### Business intelligence and reasoning

Purpose:
- interpret trends,
- generate recommendations,
- identify bottlenecks and opportunities,
- reason about operational actions.

This logic should consume the normalised data model and the financial analysis outputs rather than raw files directly.

### Research capabilities

Purpose:
- gather external market context,
- validate assumptions,
- support competitor analysis,
- identify likely suppliers or customers,
- ground recommendations in evidence.

Boundaries:
- research data must be labelled as external or secondary evidence,
- the agent should not claim commercial certainty without a source or a user-owned data source.

### Document generation

Purpose:
- produce proposals, reports, summaries, quotations, and action plans,
- maintain source citations and assumptions when generating documents.

### Task and workflow coordination

Purpose:
- convert a business objective into a structured execution plan,
- coordinate research, document creation, workflow actions, and review steps,
- manage work-state transitions.

### Tool registry and execution

Purpose:
- support approved tools for CRM updates, document updates, task creation, email drafts, data exports, or business workflow actions.

Tool constraints:
- tools are only available if the user and tenant are permitted,
- send/execute actions require approval when they affect a customer, invoice, financial record, or external communication.

### Approval and permission checks

Purpose:
- gate sensitive business actions such as sending quotations, committing to a purchase, updating finance records, or triggering external communications.

Architecture requirement:
- approvals are enforced by the backend; frontend controls are not the security boundary.

### Execution verification

Purpose:
- confirm the action actually happened,
- compare expected and observed results,
- detect partial success or failure,
- record the result as evidence.

### Evidence and reporting

Purpose:
- record the reasoning chain,
- store source references,
- capture execution records,
- deliver final reports and status summaries with evidence labels.

## 4. Mapping to the Business Partner MVP workflow

The Business Partner MVP workflow is:

Business information → Data ingestion → Analysis → Identify business problem → Generate recommended action → Request approval where required → Execute approved action → Verify result → Report outcome.

The mapping is:

- Business information: entered by the user or imported from connected data sources.
- Data ingestion: normalisation and validation pipeline.
- Analysis: financial engine, trend analysis, and market-context reasoning.
- Identify business problem: reasoning over exposure, performance, and opportunity signals.
- Recommended action: generated by business intelligence logic with citations and assumptions.
- Approval: policy engine checks action type and exposure.
- Execute approved action: tool registry invokes the permitted workflow.
- Verify result: execution verification compares expected results to actual system state.
- Report outcome: evidence-backed summary with known/estimated/assumed labels.

## 5. How business context is maintained

Business context is stored in a tenant-scoped business profile with:

- organisation and workspace references,
- customer and supplier records,
- operational goals and constraints,
- cost and pricing assumptions,
- workflow state and tasks,
- related documents and decisions.

This profile is updated incrementally and is treated as business memory, not a secret source of truth. New facts are versioned and source-linked.

## 6. How uploaded or connected data is processed

Data enters through:

- user uploads,
- connected business systems,
- document ingestion,
- finance or CRM integrations.

Then it passes through:

1. ingestion validation,
2. format and schema normalisation,
3. source metadata capture,
4. duplicate detection,
5. quality scoring,
6. business-context linking,
7. analysis and reasoning.

## 7. How calculations are separated from LLM-generated reasoning

The Business Partner should treat financial calculations as deterministic and auditable. The financial engine is the source of truth for arithmetic. The LLM can interpret the results, explain them, and propose actions, but it should not generate final financial figures without explicit deterministic computation or approved policy-backed calculation templates.

## 8. How source data and assumptions are recorded

Every decision should retain:

- source reference,
- source type,
- date captured,
- confidence or quality score,
- assumption list,
- formula or calculation basis,
- affected business object or workflow.

This ensures the system can distinguish observed data from assumptions or estimates.

## 9. How tools are chosen and invoked

The Business Partner tool selection process is:

1. define task and required capability,
2. match the action to an approved tool in the registry,
3. check tenant and user permission,
4. validate inputs,
5. create an execution plan,
6. request approval if required,
7. execute,
8. verify the outcome,
9. store execution record.

## 10. Approval and execution rules

Sensitive actions include:

- external communication,
- sending quotes or offers,
- changing financial records,
- purchasing or supplier commitments,
- customer-impacting workflow changes.

These actions require explicit approval before execution. The approval engine checks backend policy before the tool is invoked.

## 11. Failed or incomplete actions

The system should support three states:

- success with evidence,
- partial completion with warnings,
- failure with root cause and remediation guidance.

A failed or incomplete action does not count as completed. It is reported with evidence, risk status, and the next likely recovery step.

## 12. Security and operational boundaries

The Business Partner must not be granted:

- Hacker security tooling,
- arbitrary shell execution,
- privileged network scanning,
- broad credential access,
- destructive operational control beyond approved business workflows.

Its domain remains commercially and operationally focused, not security-investigation focused.
