# UX decision register

## 1. Purpose

This register captures the primary UX design decisions for the Day 11 work. It should be read alongside the product, architecture, API, and MVP documentation.

## 2. Decision log

### UX-001: shared platform shell with separate product experiences

Decision:
- The platform will have a shared shell for identity, workspace, product switching, approvals, and notifications.

Why:
- A common operating layer reduces friction while preserving product boundaries.

Status:
- accepted for MVP design.

### UX-002: product distinction is visible in the interface

Decision:
- AI Business Partner and AI Hacker will have distinct navigation, widgets, and workflows.

Why:
- The product domains are intentionally different and must not look like a single generic AI dashboard.

Status:
- accepted.

### UX-003: approval state is always visible and explicit

Decision:
- The interface must make proposed, approved, executing, failed, and verified states distinct and easy to read.

Why:
- Sensitive action workflows are core to the platform design.

Status:
- accepted.

### UX-004: missing and partial data must be shown honestly

Decision:
- Dashboards and reports should show incomplete data states, not implied completeness.

Why:
- Financial and security products depend on trustworthy evidence and transparency.

Status:
- accepted.

### UX-005: AI Hacker distinguishes registered, authorised, and validated status

Decision:
- The UX must clearly separate registered assets from authorised assets and validated vulnerabilities.

Why:
- This is critical for security and legal discipline.

Status:
- accepted.

### UX-006: Business Partner experience uses structured workflows, not chat-only interfaces

Decision:
- The product experience combines natural-language input with structured operational views.

Why:
- Business action requires clarity, evidence, and approval visibility.

Status:
- accepted.

### UX-007: accessibility is a design requirement, not a secondary concern

Decision:
- Keyboard support, readable contrast, and non-colour status indicators are mandatory.

Why:
- These workflows must be usable in real operational settings.

Status:
- accepted.

### UX-008: minimal but reusable design system

Decision:
- Build a deliberately small set of shared design foundations and product-specific modules rather than a broad early design system.

Why:
- The product is still in MVP and early design validation.

Status:
- accepted.

## 3. Open UX decisions

### Decision needed: final branding direction

The design recommends a professional neutral aesthetic but does not define a final brand identity. The founder may choose a later visual identity once the product direction is finalised.

### Decision needed: level of workflow automation in the UI

The design assumes guided workflows rather than full autonomy. Final product expectations should be agreed before deeper UI design.

### Decision needed: customer-facing severity and risk styling

The secure product needs a final rule set for how severity and approval states are labelled and styled in customer-facing views.

## 4. Summary

The UX direction is intentionally disciplined, evidence-based, and operational. It respects the MVP, keeps the products distinct, and makes approval, evidence, and execution state visible at all times.
