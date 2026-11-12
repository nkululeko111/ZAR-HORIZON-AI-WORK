# Low-fidelity wireframes

## 1. Purpose

This document contains text-based, low-fidelity wireframes for the shared platform and the two product experiences. These are layout proposals, not implemented UI.

## 2. Shared platform wireframes

### 2.1 Sign-up and onboarding

```text
+-----------------------------------------------------------+
| ZAR HORIZON AI @WORK                        [Sign in] |
+-----------------------------------------------------------+
| Overview | Product offerings | Pricing / Learn more       |
|                                                           |
| [Create account]      [Sign in existing account]          |
|                                                           |
| Name            | [____________________________]          |
| Email           | [____________________________]          |
| Password        | [____________________________]          |
|                                                           |
| [Continue]                                                |
+-----------------------------------------------------------+
```

### 2.2 Organisation and workspace selector

```text
+-----------------------------------------------------------+
| Workspace / Organisation                      [User] |
+-----------------------------------------------------------+
| Current workspace: Northshore Business                    |
| Organisation: Northshore Holdings                        |
|                                                           |
| [Create organisation]   [Join existing organisation]   |
|                                                           |
| Workspaces                                                |
| - Northshore Business      [Active]                       |
| - Security Operations      [Select]                      |
| - New workspace            [Create]                      |
+-----------------------------------------------------------+
```

### 2.3 Product selector

```text
+-----------------------------------------------------------+
| Product selector                                          |
+-----------------------------------------------------------+
| [AI Business Partner]     [AI Hacker]                     |
| Business operations       Security assessment workflow    |
| personalised business     authorised assessment tools     |
| activity & finance        evidence & reporting           |
|                                                           |
| Active entitlement: yes        Status: ready               |
| Next step: choose workspace and continue                  |
+-----------------------------------------------------------+
```

### 2.4 Account and settings

```text
+-----------------------------------------------------------+
| Account & settings                              [Save] |
+-----------------------------------------------------------+
| Profile information                                       |
| Name: [____________]                                      |
| Email: [____________]                                     |
| Role: [Founder   v]                                      |
|                                                           |
| Organisation membership                                   |
| - Northshore Holdings      [Owner]                        |
| - Security Operations       [Member]                      |
|                                                           |
| Notification preferences                                  |
| [ ] Approvals                                              |
| [ ] Execution results                                      |
| [ ] Security findings                                      |
+-----------------------------------------------------------+
```

## 3. Business Partner wireframes

### 3.1 Main dashboard

```text
+--------------------------------------------------------------------------+
| Business Partner                     [Search]  [Approvals 3] [User]      |
+--------------------------------------------------------------------------+
| Overview | My Business | Financials | BI | Tasks | Documents | Research | Activity |
+--------------------------------------------------------------------------+
| Business health summary                                                  |
| Revenue: R245k   Expenses: R176k   Cash: R62k   Margin: 28%              |
| +---------------------------------------------------------------+      |
| | Issue: Profitability down 11% vs prior month                |      |
| | Opportunity: Reduce shipping spend in top 3 categories      |      |
| | Recommended next action: review supplier terms              |      |
| +---------------------------------------------------------------+      |
|                                                                       |
| Tasks & approvals | Recent agent activity                              |
| - Review supplier terms | Action: Cash-flow review complete            |
| - Approve quote draft   | Action: Budget variance flagged                 |
| - Complete monthly close| Task: Generate monthly report                 |
|                                                                       |
| KPIs / charts                                                          |
| [Trend: Revenue]   [Trend: Expenses]  [Cash-flow]                     |
+--------------------------------------------------------------------------+
```

### 3.2 Financial overview

```text
+--------------------------------------------------------------------------+
| Financials                            [Select period] [Import data]     |
+--------------------------------------------------------------------------+
| Revenue | Expenses | Cash flow | Profitability | Budget vs actual       |
|                                                                       |
| Summary card row                                                       |
| Revenue: R245k | Expenses: R176k | Net margin: 28% | Cash: R62k        |
|                                                                       |
| Source data: imported | Derived metrics: calculated | AI notes: labelled |
|                                                                       |
| [Last 30 days] [Quarter] [Year]                                        |
|                                                                       |
| Detailed table                                                          |
| Category | Actual | Budget | Variance | Source                          |
| Sales    | R120k   | R110k  | +R10k   | Imported ledger                 |
| Payroll  | R40k    | R45k   | -R5k    | Imported ledger                 |
| Shipping | R22k    | R18k   | +R4k    | Imported ledger                 |
+--------------------------------------------------------------------------+
```

### 3.3 Business intelligence detail

```text
+--------------------------------------------------------------------------+
| Business intelligence                     [Ask a question] [Run analysis] |
+--------------------------------------------------------------------------+
| Question: Why is profitability down this month?                          |
|                                                                       |
| Summary                                                                |
| Profitability fell 11% because shipping and payroll costs rose above plan.|
|                                                                       |
| Evidence                                                                |
| - Shipping spend increased 18% over prior month                         |
| - Staff costs increased by 7%                                            |
| - Revenue remained flat for the same period                             |
|                                                                       |
| Issues                                                                 |
| 1. Shipping costs above target                                          |
| 2. Payroll variance in the current period                               |
|                                                                       |
| Opportunities                                                           |
| - renegotiate freight terms, compare suppliers                           |
| - review staffing schedule and utilisation                              |
|                                                                       |
| Recommended action                                                      |
| [Propose action] [Save to tasks] [Generate document]                   |
+--------------------------------------------------------------------------+
```

### 3.4 Action approval

```text
+--------------------------------------------------------------------------+
| Proposed action approval                                     [Reject] |
+--------------------------------------------------------------------------+
| Action: Renegotiate freight supplier terms                                |
| Business objective: reduce shipping cost by 8% within 30 days            |
| Parameters: supplier list, target spend, expected outcome                 |
| Risk: Medium                                                             |
| Evidence: cost review, shipping trend, supplier comparison               |
| Approval expires: 24h                                                    |
|                                                                       |
| [Approve]   [Request changes]   [Cancel]                                 |
+--------------------------------------------------------------------------+
```

### 3.5 Task and activity workspace

```text
+--------------------------------------------------------------------------+
| Tasks and actions                          [New task] [Filter]          |
+--------------------------------------------------------------------------+
| Status filter: proposed | approved | executing | completed | failed      |
|                                                                       |
| Task / action | Owner | Due | Status | Outcome                               |
| Review supplier quotes | Alex | 2026-11-12 | Approved | pending          |
| Update monthly report | Sam | 2026-11-13 | Executing | in progress       |
| Renegotiate freight terms | Owner | 2026-11-14 | Verified | complete        |
+--------------------------------------------------------------------------+
```

## 4. AI Hacker wireframes

### 4.1 Main dashboard

```text
+--------------------------------------------------------------------------+
| Security overview                        [Approve] [Reports] [User]      |
+--------------------------------------------------------------------------+
| Summary cards                                                           |
| Assets: 14 | Active assessments: 3 | Findings: 8 | Remediation: 2        |
|                                                                       |
| Warnings                                                                |
| - 2 assets have expired authorisation                                   |
| - 1 assessment scope is pending re-approval                             |
|                                                                       |
| Recent findings                                                         |
| High: SQL injection, API user enumeration                                |
| Medium: missing security headers                                        |
|                                                                       |
| Assessment progress                                                     |
| [Assessment A] Ready | [Assessment B] Running | [Assessment C] Completed  |
+--------------------------------------------------------------------------+
```

### 4.2 Asset detail and authorisation

```text
+--------------------------------------------------------------------------+
| Asset detail                                     [Edit] [History] |
+--------------------------------------------------------------------------+
| Asset: merchant-api.internal                                            |
| Type: API                                                               |
| Owner: Platform team                                                    |
| Authorisation: Active | Scope: Approved | Window: 10:00-18:00 (UTC)      |
|                                                                       |
| Scope details                                                           |
| Included: /api/v1/orders, /api/v1/users                                  |
| Excluded: admin endpoints, internal management routes                    |
| Techniques allowed: API testing, unrestricted web testing not allowed    |
|                                                                       |
| Status: Ready for assessment                                             |
+--------------------------------------------------------------------------+
```

### 4.3 Assessment workspace

```text
+--------------------------------------------------------------------------+
| Assessment: API review                              [Submit] [Pause] |
+--------------------------------------------------------------------------+
| Target | Scope | Findings | Evidence | Remediation                       |
|                                                                       |
| Status: Running                                                         |
| Started: 09:10 | ETA: 12:00 | Current phase: API validation            |
|                                                                       |
| Evidence feed                                                           |
| - Request/response capture logged                                       |
| - Rate limit validation complete                                         |
| - Candidate issue identified                                             |
|                                                                       |
| Finding summary                                                         |
| [High] Authorization bypass                                                |
| [Medium] Missing rate limit policy                                       |
+--------------------------------------------------------------------------+
```

### 4.4 Finding detail

```text
+--------------------------------------------------------------------------+
| Finding: Authorization bypass                              [Validate] |
+--------------------------------------------------------------------------+
| Asset: merchant-api.internal                                             |
| Severity: High | Confidence: High | Status: Pending validation           |
|                                                                       |
| Summary                                                                 |
| Token validation for beta endpoints allows one account to access another.|
|                                                                       |
| Evidence                                                                |
| - Request sample captured                                                |
| - Response payload with privileged data                                 |
| - Reproduction notes                                                     |
|                                                                       |
| Impact                                                                  |
| Potential unauthorised access to customer data                           |
|                                                                       |
| Remediation suggestions                                                  |
| [Generate guidance] [Request retest]                                    |
+--------------------------------------------------------------------------+
```

### 4.5 Remediation and report

```text
+--------------------------------------------------------------------------+
| Remediation and report                         [Request retest] [Export] |
+--------------------------------------------------------------------------+
| Finding: Authorization bypass                                            |
| Remediation status: In progress | Validation: pending                    |
|                                                                       |
| Guidance                                                                 |
| - Enforce signed access check against session scoping                    |
| - Validate rbac scope on each privileged endpoint                        |
| - Add regression tests for access enforcement                            |
|                                                                       |
| Retest status                                                            |
| Not yet requested                                                         |
|                                                                       |
| Final report status                                                      |
| Draft report ready for approval                                           |
+--------------------------------------------------------------------------+
```

## 5. Notes on wireframe intent

- These wireframes emphasise usability, not final styling.
- Data-heavy screens should prioritize action, status, and evidence before decorative elements.
- The wireframes deliberately maintain product distinctions and avoid presenting any security testing as unrestricted.
