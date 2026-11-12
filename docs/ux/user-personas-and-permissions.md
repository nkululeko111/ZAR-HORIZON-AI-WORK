# User personas and permissions

## 1. Purpose

This document defines the primary user personas and permissions for the shared platform, the AI Business Partner, and the AI Hacker products. It reflects the documented customer segments and MVP scope without assuming a large enterprise team.

## 2. Shared platform personas

### Individual entrepreneur or founder

Goal:
- Run a business or security assessment with a lean team and minimal overhead.

Typical tasks:
- create organisation and workspace,
- switch between products,
- review approvals,
- manage profile and account settings,
- create business or security actions.

Allowed access:
- own organisation and workspace,
- one or more product entitlements,
- approval for actions in own workspace,
- access to financial and security records within their organisation.

## 3. Business Partner personas

### Business owner / founder

Goal:
- understand the health of the business and take focused action.

Typical tasks:
- review dashboard,
- import financial records,
- ask the agent for analysis,
- approve or reject recommendations,
- track execution outcomes.

Permissions:
- business profile access,
- financial summaries and analysis,
- task and document management,
- approval of approved actions within their business workspace.

### Business manager

Goal:
- manage a functioning business workflow without becoming a financial analyst.

Typical tasks:
- review budgets and cash-flow,
- manage tasks,
- track actions and statuses,
- work with documents and business opportunities.

Permissions:
- read and update relevant business records,
- manage assigned tasks,
- approve actions within the appropriate scope.

### Finance or operations team member

Goal:
- monitor operational metrics and validate data quality.

Typical tasks:
- import and review financial records,
- confirm categories or period data,
- review variances and KPIs,
- support document generation.

Permissions:
- restricted to relevant business data and workflow tasks,
- not necessarily able to approve all external commitments.

## 4. AI Hacker personas

### SaaS founder or company owner

Goal:
- monitor the security posture of a digital product and coordinate assessments.

Typical tasks:
- register assets,
- manage authorisation records,
- review findings and report status,
- approve retesting and report distribution.

Permissions:
- asset ownership and authorisation management,
- assessment read access,
- approved report access and remediation status.

### CTO or technical lead

Goal:
- ensure security scope, testing windows, and remediation follow approved plan.

Typical tasks:
- review assessment scope,
- confirm targets and exclusions,
- coordinate with security providers,
- review remediation progress and report readiness.

Permissions:
- scope and assessment oversight,
- security status data,
- evidence access within the authorised assessment context.

### Developer

Goal:
- fix findings and support technical validation.

Typical tasks:
- review remediation guidance,
- validate patch readiness,
- support retest execution,
- confirm remediation status.

Permissions:
- relevant finding and remediation data,
- no direct system-wide security execution authority beyond the assigned workflow.

### Security practitioner or assessor

Goal:
- investigate, validate, and report findings according to policy.

Typical tasks:
- review assessment plan,
- validate evidence,
- classify findings,
- request retest,
- prepare final report.

Permissions:
- find and evidence work within approved scope,
- approval authority for security-related validation steps under policy.

### Security assessment administrator

Goal:
- ensure compliance, authorisation, and risk review for all assessments.

Typical tasks:
- create/maintain authorisation records,
- review assessment readiness,
- confirm testing windows and restrictions,
- verify final reports and approvals.

Permissions:
- authorisation and scope governance,
- assessment lifecycle controls,
- approval-relevant operations.

## 5. Permission model

### Shared permissions

These are common across the platform:

- view organisation and workspace membership,
- manage own profile,
- view notifications,
- access product-specific dashboards within entitlement.

### Business Partner permissions

Examples:

- view business profile,
- import and manage financial records,
- read and summarise business data,
- create tasks,
- propose and approve business actions,
- generate business documents.

### AI Hacker permissions

Examples:

- register assets,
- manage authorisation records,
- define scope and exclusions,
- run or review assessment workflows,
- validate findings,
- manage remediation and retesting,
- access evidence and final reports within scope.

## 6. Relationship between personas and product boundaries

The experience should clearly prevent the wrong realm from showing inappropriate controls.

Examples:

- a Business Partner user should not see security assessment controls by default,
- a Hacker user should not see financial data or commercial workflow controls,
- a workspace member with restricted permissions should see a reduced or denied action menu.

## 7. Single-user or small-team operating model

The UX should work for a small team or a solo founder.

Requirements:

- low-friction onboarding,
- visible role switching without complexity,
- minimal permission prompts for simple actions,
- explicit escalation for risky or externally impactful actions,
- clear records for all actions and approvals.

## 8. Permission states to display

The interface should visually distinguish:

- active access,
- pending access review,
- denied access,
- expired authorisation,
- approval required,
- membership inactive.

These states need to be explicit and readable without relying on colour alone.

## 9. Summary

The experience should be built around the people actually using the system: founders, operators, security assessors, and small teams. The UX must fit lean organisations while still respecting strict product separation, access controls, and approval expectations.
