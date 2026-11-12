# Day 11 UX decisions

## 1. Summary

This document summarises the UX, navigation, and wireframe decisions for the shared platform, AI Business Partner, and AI Hacker products. It aligns the user experience with the earlier product, architecture, database, API, and MVP documentation and keeps the scope within a documentation-only UX exercise.

## 2. Overall UX direction

- shared platform shell with consistent identity, workspace switching, and approval visibility,
- separate product experiences for Business Partner and AI Hacker,
- practical, evidence-based interaction patterns,
- structured workflows rather than chat-only interfaces,
- clear separation between proposed, approved, executing, completed, failed, and verified states,
- explicit handling of incomplete or missing data,
- product-specific navigation and business/security-specific dashboards.

## 3. Shared platform experience

The shared platform provides:

- onboarding,
- identity and account management,
- organisation and workspace management,
- product selection and entitlement visibility,
- approvals and notifications,
- settings and account controls.

The shared experience must remain neutral and consistent while preserving a product-specific operating focus once inside a product.

## 4. Business Partner dashboard and navigation

The Business Partner experience is designed around:

- business health overview,
- financial status,
- opportunity and issue identification,
- evidence-backed business intelligence,
- action approval and execution tracking,
- tasks, documents, and research.

The MVP navigation is intentionally focused and realistic for a founder or small business operator.

## 5. AI Hacker dashboard and navigation

The AI Hacker experience is designed around:

- asset and authorisation management,
- scope and assessment readiness,
- assessments and evidence,
- findings and validation,
- remediation and retesting,
- final report generation.

It is built around policy, control, and evidence, not unrestricted interactive testing.

## 6. Main user journeys

The design includes complete journeys for:

- new entrepreneur onboarding,
- business import and performance review,
- profitability investigation and recommendation,
- action approval and execution,
- evidence review and result verification,
- asset registration and authorisation,
- assessment planning and execution,
- finding validation and remediation,
- retest and final report review.

The journeys are documented in the product-specific UX journey files.

## 7. Approval and execution experience

The design keeps approval and execution status visible at all times:

- proposed action,
- pending approval,
- approved,
- executing,
- failed or partially successful,
- verified.

The UX must not blur the difference between a recommendation and an executed action.

## 8. Screen inventory and wireframes

The repository contains a complete screen inventory and low-fidelity wireframes for:

- shared platform onboarding and settings,
- Business Partner dashboard and action flows,
- AI Hacker asset, assessment, and finding flows.

The wireframe content is captured in the UX file set.

## 9. Responsive and accessibility considerations

The UX is designed to be:

- desktop-first,
- readable on tablet,
- usable on mobile,
- keyboard-accessible,
- focus-visible,
- screen-reader friendly,
- robust against colour-only status communication.

## 10. Major UX risks

- a unified “AI dashboard” could hide the product distinctions,
- approval flows could become too generic or too easy to skip,
- financial summaries and security status could feel more certain than the underlying data supports,
- low-fidelity design could be mistaken for a final visual design,
- a pure chat experience would underrepresent operational workflows and evidence review.

## 11. Decisions requiring founder approval

- final brand or visual direction,
- preferred level of automation in the product workflows,
- final product-specific severity and approval styling,
- final approval delegation and escalation model,
- final set of future and deferred UX capabilities.

## 12. Files created

- [docs/ux/ux-strategy-and-design-principles.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/ux-strategy-and-design-principles.md)
- [docs/ux/user-personas-and-permissions.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/user-personas-and-permissions.md)
- [docs/ux/shared-platform-onboarding-journey.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/shared-platform-onboarding-journey.md)
- [docs/ux/business-partner-user-experience.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/business-partner-user-experience.md)
- [docs/ux/ai-hacker-user-experience.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/ai-hacker-user-experience.md)
- [docs/ux/business-partner-user-journeys.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/business-partner-user-journeys.md)
- [docs/ux/ai-hacker-user-journeys.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/ai-hacker-user-journeys.md)
- [docs/ux/approval-and-execution-experience.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/approval-and-execution-experience.md)
- [docs/ux/screen-inventory.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/screen-inventory.md)
- [docs/ux/low-fidelity-wireframes.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/low-fidelity-wireframes.md)
- [docs/ux/responsive-and-accessibility-requirements.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/responsive-and-accessibility-requirements.md)
- [docs/ux/design-system-foundations.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/design-system-foundations.md)
- [docs/ux/ux-decision-register.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/ux-decision-register.md)
- [docs/ux/day-11-ux-decisions.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux/day-11-ux-decisions.md)

## 13. Confirmation

This task remained a documentation-and-wireframe exercise only. No frontend components, routes, CSS, JavaScript, application pages, or runtime code were implemented. The work is limited to the design specification files under [docs/ux/](/C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/ux).
