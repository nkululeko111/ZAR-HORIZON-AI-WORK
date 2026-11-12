# UX strategy and design principles

## 1. Goal

This document defines the user experience direction for the shared platform, the AI Business Partner, and the AI Hacker products. It translates the approved product and architecture decisions into a practical product experience without inventing features beyond the documented MVP.

This is a design specification only and not a runtime implementation.

## 2. Overall UX direction

### Shared product positioning

The platform should feel like a trusted operating layer for business and security work. The experience should communicate that the system is:

- professional,
- auditable,
- permission-aware,
- operationally useful,
- clear about risk and approval states,
- safe around sensitive actions.

### Product positioning in the interface

The shared platform should provide a neutral shell with shared account, workspace, and notification infrastructure. Product-specific experiences should feel distinct:

- Business Partner: practical business command centre,
- AI Hacker: professional security assessment workspace.

The product switcher should make this difference visible without creating confusion.

## 3. Shared navigation principles

The shared platform should have consistent top-level patterns:

- account and workspace switcher,
- product switcher,
- global search or quick actions,
- notifications,
- approval centre,
- settings.

Navigation should be:

- predictable,
- permission-aware,
- compact on desktop,
- readable on tablet and mobile,
- explicit about state.

## 4. Information hierarchy

The platform should rank information by actionability:

1. urgent actions and approvals,
2. business or security health indicators,
3. current tasks and execution status,
4. supporting details and evidence,
5. secondary configuration and settings.

This hierarchy matters more than decorative layout in both products.

## 5. Visual design direction

The design should aim for a professional, enterprise-grade aesthetic rather than a consumer chatbot style.

Recommended direction:

- low-noise background,
- clear information cards,
- strong hierarchy between primary metrics and supporting facts,
- readable tables and lists,
- explicit status badges and caution states,
- system and product terminology that matches the domain.

The design should not rely on arbitrary colour alone to communicate severity or state.

## 6. Product-specific experience goals

### AI Business Partner

The Business Partner should feel like a practical operating companion for a founder or small team. It should help the user understand the business, act on evidence, and execute approved actions without needing to become a data analyst.

Key experience goals:

- clarity over complexity,
- fact-based recommendations,
- visible approval and execution state,
- action tracking and outcome proof,
- support for small business operations.

### AI Hacker

The AI Hacker experience should feel like a disciplined security operations workspace. It should prioritise containment, trust, and evidence quality.

Key experience goals:

- clear authorisation status,
- explicit scope boundaries,
- visible findings and evidence,
- strong separation between planned and validated work,
- controlled remediation and retesting workflow.

## 7. Navigation structure

### Shared platform

- Home or workspace overview
- Organisations and workspaces
- Products and entitlements
- Approvals
- Notifications
- Account settings

### Business Partner (MVP)

- Overview
- My Business
- Financials
- Business Intelligence
- Tasks and Actions
- Documents
- Research
- Activity
- Settings

Future capabilities should be explicitly marked as future or not in MVP, rather than hidden inside the main nav.

### AI Hacker (MVP)

- Security Overview
- Assets
- Authorisations and Scope
- Assessments
- Findings
- Evidence
- Remediation
- Reports
- Activity
- Settings

## 8. Loading, empty and error states

Every core screen should have clear empty and loading states:

- loading: skeleton or progress placeholders for data-heavy screens,
- empty: guidance that explains what is missing and next steps,
- partial data: note what is missing and whether the user can continue,
- error: explain what failed and whether retry or follow-up is required,
- success: confirm completion and show next action.

Examples:

- no financial data imported → show guidance to import records
- no active assessment → show readiness checklist
- approval expired → show status with clear next action
- finding not yet validated → show pending validation status

## 9. Accessibility requirements

The UX should support:

- keyboard navigation across all core workflows,
- visible focus states,
- labelled form fields,
- logical heading order,
- screen-reader-friendly status updates,
- readable contrast ratios,
- accessible tables and filters,
- non-colour indicators for state, severity, and approval status.

Accessibility is not optional; it is required for compliance and operational usability.

## 10. Responsive behaviour

The interface should be designed desktop-first but remain functional on tablet and mobile.

- desktop: dense tables, multi-panel layouts, rich summaries
- tablet: stacked panels and simplified navigation
- mobile: condensed cards, detail-first layouts, reduced chart density

Important rule: tables and dense status layouts must remain readable without relying on tiny columns.

## 11. Behavioural design recommendations

- explicit action boundaries: proposed vs approved vs executed vs verified
- obvious risk indicators with text labels
- direct path from evidence to recommendation
- clear statement of missing data before analysis is shown
- explicit approval panel with exact proposed action and parameters
- no interface should imply an action has been executed without verification

## 12. Design principles summary

1. Be clear about what is known, unknown, pending, approved, or failed.
2. Keep system behaviour honest and evidence-based.
3. Separate the shared platform from product-specific authority.
4. Respect the MVP and do not over-design future features.
5. Make approvals and execution state visible before, during, and after actions.
6. Keep the interface professional and practical, not chat-first.

## 13. Future design work

This document intentionally limits the design to MVP-relevant screens and flows. Large design-system expansion and experimental UI patterns should be deferred until the product experience is validated with real customer workflows.
