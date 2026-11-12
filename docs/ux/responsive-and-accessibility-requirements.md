# Responsive and accessibility requirements

## 1. Responsive layout requirements

### Desktop

The primary experience should be desktop-first.

Key features:

- multi-panel workspaces,
- dense but readable data tables,
- side navigation,
- summary cards and trend panels,
- approval sidebars and evidence panes.

### Tablet

Tablet layouts should collapse side-by-side panels into stacked sections while keeping action flows visible.

Key features:

- simplified navigation,
- responsive cards,
- reduction of dense visual clutter,
- preserve action-first layout.

### Mobile

Mobile layouts should emphasise task completion and detail review.

Key features:

- single-column flow,
- action buttons placed near context,
- condensed metrics,
- progressive disclosure of evidence,
- summary-first data presentation.

## 2. Data-heavy views

Tables and charts should adapt to smaller screens by:

- stacking columns when necessary,
- keeping primary columns visible,
- moving secondary metadata into expandable details,
- ensuring status badges remain readable.

The system must not hide critical status information in a collapsed or inaccessible area.

## 3. Keyboard and focus requirements

The interface should support:

- full keyboard navigation for all core workflows,
- visible focus states,
- predictable tab order,
- skip links for major navigation containers,
- proper form labelling and error announcements.

## 4. Screen reader requirements

The UX should include:

- accessible labels on buttons and controls,
- clear status announcements for approvals, execution changes, and errors,
- descriptive table headers,
- meaningful alt or text summaries for non-text evidence panels,
- logical form and section ordering.

## 5. Colour and status design

Do not rely on colour alone to communicate:

- vulnerability severity,
- approval status,
- action state,
- execution success and failure.

Status should use a combination of:

- iconography,
- labels,
- text descriptions,
- position in workflow,
- contrast-safe styling.

## 6. Regulatory and usability considerations

The UX should support:

- low vision readability,
- strong contrast,
- flexible text scaling,
- reduced motion or simplified transitions where possible,
- clear separation of risk-critical and informational content.

## 7. Accessibility examples by product

### Business Partner

Examples:

- financial summary cards with text labels,
- clear approval state labels,
- action status with accessible names,
- tasks with due date and owner visible in text form.

### AI Hacker

Examples:

- severity shown as text, not only colour,
- finding status labelled clearly,
- evidence and remediation panels with visible labels,
- secure and permission-aware state cues.

## 8. Summary

Responsive and accessible design is critical for both products. The UI must remain professional, legible, and operationally clear across desktops, tablets, and mobile devices while ensuring every important status is conveyed with text and structure, not just colour.
