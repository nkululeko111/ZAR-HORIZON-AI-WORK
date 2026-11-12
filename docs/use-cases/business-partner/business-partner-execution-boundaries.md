# Business Partner Execution Boundaries

## 1. Purpose

This document defines the operational boundaries of the AI Business Partner. These boundaries are essential because the product is designed to execute tasks, not simply generate advice. The product must be powerful within its approved domain, but it must not cross into unauthorised financial, legal, or communications risk.

## 2. Action categories

### Category 1: Read-only operations

These are activities that gather information, review internal or external data, and summarise findings without altering business records.

Examples:

- market research,
- competitor scanning,
- supplier listing and comparison,
- financial summary generation,
- lead research,
- operational reporting,
- trend review,
- document drafting for review.

Approval requirements:

- usually user-initiated,
- no external action unless the user explicitly approves.

Evidence requirements:

- source and date of data,
- clearly marked assumptions,
- distinction between verified facts and estimates.

### Category 2: Research operations

These are tasks that require investigation and synthesis rather than data creation.

Examples:

- customer segmentation research,
- supplier discovery,
- market opportunity research,
- competitor analysis,
- pricing comparison research,
- operational performance review.

Approval requirements:

- usually user approval for scope and target,
- no external outreach without explicit permission.

Evidence requirements:

- source quality notes,
- transparency around any limitations,
- clear separation of facts from estimates.

### Category 3: Reversible actions

These are actions that can be corrected or undone without material external harm.

Examples:

- draft document generation,
- internal task creation,
- internal reminders,
- draft email for review,
- proposed internal report,
- working spreadsheet preparation,
- internal notes and pipeline draft updates.

Approval requirements:

- user review before sending or finalising,
- explicit permission for any external impact.

Evidence requirements:

- clear record of draft or proposed changes,
- visible audit trail for changes to working documents.

### Category 4: External communications

These actions involve customer or stakeholder communication.

Examples:

- sending a quotation,
- sending follow-up messages,
- contacting a lead,
- supplier emails,
- external customer notices.

Approval requirements:

- explicit human approval before sending,
- review of content, business terms, and intended recipient,
- audit logging of the communication record.

Evidence requirements:

- final message text,
- recipient, date, and approval record,
- reason for communication.

### Category 5: Financial or commercially sensitive actions

These actions involve money, contracts, offers, pricing commitments, or other commercially significant decisions.

Examples:

- issuing an invoice,
- changing pricing,
- creating a sales commitment,
- approving a payment or supplier commitment,
- preparing a contract or commercial offer,
- creating a financial forecast intended for decision-making.

Approval requirements:

- explicit user approval,
- human review for sensitive, pricing-critical, or high-risk financial decisions,
- clear visibility into assumptions and calculations.

Evidence requirements:

- calculations shown and traceable,
- source data identified,
- assumptions listed,
- approval record and audit trail.

### Category 6: High-risk or restricted actions

These actions may create material legal, commercial, or operational risk.

Examples:

- making a binding commitment to a customer,
- issuing contractual language without review,
- processing external payments or transactions,
- acting on behalf of a business without explicit permission,
- sharing sensitive business information with external parties without approval,
- taking regulated actions outside appropriate professional review.

Approval requirements:

- explicit human authorisation,
- supervisory review if the action is material,
- clear restrictions if the business or customer rules require it.

Evidence requirements:

- exact content, approval chain, and final confirmation,
- reason for risk classification,
- record of whether the action was executed or blocked.

## 3. Actions allowed without additional approval

These may be allowed with ordinary user context and workspace permission:

- summarising internal operational information,
- preparing a business report for review,
- helping classify leads or tasks,
- creating a draft quotation for user review,
- preparing internal comparison spreadsheets,
- organising recurring business tasks,
- generating management summaries based on user-provided data.

These actions may be performed as part of normal workflow if the user requested the task, but they must still be visible and auditable.

## 4. Actions requiring explicit user approval

Examples:

- sending emails to leads or customers,
- updating supplier or customer records in live systems,
- creating or sending quotations,
- issuing invoices,
- proposing cost changes,
- initiating external communications,
- making a purchase recommendation that is intended to trigger action,
- acting on private or sensitive business information.

## 5. Actions requiring external integration access

These actions require an authorised data connection or tool integration.

Examples:

- CRM updates,
- inventory record updates,
- email sending,
- invoice generation,
- financial data sync,
- supplier data retrieval,
- document storage updates,
- task management updates,
- calendar scheduling and reminder creation.

The agent must not assume that an integration is authorised simply because it exists. Access must be controlled by permission, tenant boundaries, and user approval.

## 6. Actions requiring professional or human review

The AI Business Partner must not replace professional guidance where the subject requires specialist judgment.

Examples:

- tax, legal, accounting, and compliance advice,
- financial record validation,
- contract review,
- formal tax filings,
- accounting treatment of business transactions,
- legal interpretation of obligations or liabilities.

The product may prepare material, but it must not present that material as professional, audited, or regulated advice.

## 7. Actions that must not be performed autonomously

The AI Business Partner must not autonomously:

- issue invoices or payment instructions,
- commit the business to a contract,
- approve suppliers or negotiate binding terms without human review,
- send external communications that contain material commercial commitments,
- make financial decisions with real consequences without evidence and approval,
- process sensitive personal or customer data beyond the user’s authorised scope,
- act as though it is an accountant, auditor, or regulated financial adviser.

## 8. Evidence and reporting requirements

For all actions, the Business Partner must provide:

- the task performed,
- information used,
- any calculations or assumptions,
- approval status,
- final result,
- any unresolved issues,
- any remaining risk or uncertainty.

No business action should be reported as completed unless the agent can verify the outcome or clearly state that it is pending or unverified.

## 9. Boundary summary

The AI Business Partner should be powerful and operational, but not uncontrolled. It should help a business owner act with greater speed and clarity, without becoming a substitute for human judgement in legally, financially, or commercially sensitive decisions.

This boundary is essential to the founder-approved product vision and to the need to build trust in real business operations.
