# Design system foundations

## 1. Purpose

This document defines the initial reusable design language for the shared platform and the two product lines. The goal is to capture reusable structure and patterns without prematurely constructing a large design system.

## 2. Reusable navigation patterns

### Shared navigation

Common components:

- top bar with product switcher,
- workspace selector,
- notifications,
- approvals counter,
- account menu,
- global search or quick actions.

These should be shared across both products.

### Product-specific navigation

Product-specific sidebars should include only the relevant product sections.

- Business Partner: Overview, My Business, Financials, Business Intelligence, Tasks and Actions, Documents, Research, Activity, Settings
- AI Hacker: Security Overview, Assets, Authorisations and Scope, Assessments, Findings, Evidence, Remediation, Reports, Activity, Settings

## 3. Core UI components

### Navigation

- left sidebar or top navigation,
- contextual breadcrumbs,
- section headers and page actions,
- filter chips for lists and data views.

### Cards

Use cards for:

- KPI summaries,
- business or security status,
- recent tasks,
- evidence summaries,
- recent activity.

Recommended card structure:

- title,
- contextual status badge,
- metric or summary values,
- optional primary action,
- secondary link or details.

### Data tables

Use tables for:

- financial summaries,
- finding lists,
- activities,
- assessment statuses,
- task lists.

Table requirements:

- clear headers,
- accessible sorting,
- visible status labels,
- multi-row action affordances,
- empty and loading states.

### Charts and visual summaries

Use simple charts only where they add clarity.

Recommended types:

- small trend lines,
- bar charts for comparisons,
- donut or progress visuals for limited metrics,
- not over-designed dashboards that obscure the key message.

### Status indicators

Status should be explicit and readable in text. Components should include:

- proposed,
- approved,
- executing,
- completed,
- failed,
- blocked,
- verified,
- pending validation,
- expired.

### Forms

Shared form patterns should include:

- single-column focus on simple tasks,
- two-column layout for broader forms,
- clear validation messaging,
- required-field indicators,
- step-based forms for onboarding and scope setup.

### Dialogs and approval panels

Approval and confirmation patterns should include:

- exact action summary,
- request metadata,
- evidence panel,
- risk or sensitivity label,
- approve and reject controls,
- secondary cancel or exit option.

### Activity feeds

Use activity feeds where the user needs operational visibility.

Examples:

- action history,
- security execution timeline,
- findings update stream,
- approval log.

### Evidence panels

Evidence panels should show:

- evidence title,
- source,
- timestamp,
- relevance,
- linked finding or action,
- confidence or validation status.

### Agent interaction components

Recommended agent interaction surfaces:

- natural-language input area,
- structured action summary panel,
- supporting evidence area,
- action recommendation carousel or list,
- direct approval or follow-up actions.

The UI should not be purely a chat box. It should combine interaction with structured workflow visibility.

### Notifications

Shared notification patterns should support:

- approval required,
- execution complete,
- execution failed,
- evidence available,
- report ready,
- scope warning.

## 4. Shared vs product-specific components

### Shared across platform

- top bar,
- workspace selector,
- product selector,
- notification centre,
- approval centre,
- account settings,
- standard cards,
- table patterns,
- forms,
- status badges,
- activity feed shell.

### Product-specific components

Business Partner:

- financial summary panels,
- business intelligence analysis cards,
- recommendation and action detail panels,
- task/action lifecycle status.

AI Hacker:

- scope and authorisation panels,
- security assessment status board,
- evidence timeline,
- severity and validation classification blocks,
- retesting workflow components.

## 5. Design system principles

- start with reusable structural patterns, not a large decorative system,
- keep product differences explicit,
- reduce cognitive load by showing only relevant actions,
- prefer explicit labels over vague visual metaphors,
- ensure all status can be understood without relying on colour alone.

## 6. Summary

The design system should be modest and intentional. Reusable patterns should support the shared platform, while each product keeps a clearly distinct operational identity.
