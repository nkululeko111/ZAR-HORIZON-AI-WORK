# Screen inventory

## 1. Shared platform screens

| Screen name | Product | Purpose | Persona | Main info | Primary action | Secondary actions | API dependency | Permission requirement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Platform landing | Shared | product entry and account choices | new user | product overview | sign up / sign in | view offerings | none | public |
| Account creation | Shared | create identity and account | new user | personal info | create account | sign in | auth API | public |
| Organisation picker | Shared | select or create organisation | user | memberships | continue | create org | org API | authenticated |
| Workspace selector | Shared | choose active workspace | user | workspace list | select workspace | create workspace | workspace APIs | authenticated |
| Product selector | Shared | choose active product | user | product access | choose product | manage entitlements | product APIs | authenticated |
| Account and settings | Shared | manage user profile and account | user | account settings | update profile | notifications, security | auth/profile APIs | authenticated |
| Approval inbox | Shared | review pending approvals | owner/admin | actions waiting for decision | approve/reject | filter list | approvals API | approval permission |

## 2. Business Partner screens

| Screen name | Product | Purpose | Persona | Main info | Primary action | Secondary actions | API dependency | Permission requirement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Business dashboard | Business Partner | operational summary | founder/manager | KPI snapshot | review insights | import data, open tasks | financial and action APIs | partner access |
| Business profile | Business Partner | define business context | founder/manager | business details | update business profile | view objectives | business profile API | partner access |
| Financial import | Business Partner | import records | company owner | source data state | import records | review mapping | financial import API | financial permissions |
| Financial overview | Business Partner | review revenue and expense | owner/finance | summary data | view trends | change period | financial summary APIs | financial permissions |
| Cash-flow summary | Business Partner | review cash movement | owner/finance | inflow/outflow | view cash risk | compare periods | financial API | partner access |
| Profitability | Business Partner | review margins | manager | profit metrics | view margin drivers | export report | profitability API | partner access |
| Business intelligence detail | Business Partner | issue/opportunity review | business owner | findings and evidence | review action | approve or reject | analysis API | partner access |
| Proposed action detail | Business Partner | review and approve action | owner | action, params, evidence | approve or reject | request changes | approval API | approval permission |
| Task workspace | Business Partner | manage tasks | manager | task list | create/update task | review status | task APIs | task permission |
| Document centre | Business Partner | generated docs | owner/manager | document list | open or create | export | document APIs | document access |
| Activity feed | Business Partner | review execution history | user | recent events | inspect items | filter by status | execution API | partner access |

## 3. AI Hacker screens

| Screen name | Product | Purpose | Persona | Main info | Primary action | Secondary actions | API dependency | Permission requirement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Security overview | AI Hacker | overall security health | CTO/admin | active assessments, findings | open assessment | review warnings | assessment APIs | security access |
| Asset register | AI Hacker | asset management | security admin | asset list | register asset | review details | asset APIs | asset permission |
| Asset detail | AI Hacker | understand an asset | admin/assessor | asset summary | review authorisation | edit metadata | asset API | asset access |
| Authorisations and scope | AI Hacker | set policy boundaries | admin/assessor | scope and restrictions | approve details | edit exclusions | authorisation API | authorisation permission |
| Assessment workspace | AI Hacker | live assessment orchestration | assessor | findings, status, evidence | view progress | pause/cancel | assessment APIs | assessment access |
| Finding detail | AI Hacker | review vulnerability evidence | assessor/CTO | findings and severity | validate status | update classification | finding APIs | finding access |
| Evidence centre | AI Hacker | review proof and logs | assessor | evidence list | inspect evidence | attach metadata | evidence APIs | evidence access |
| Remediation panel | AI Hacker | fix tracking | dev/security | guidance and status | request retest | update status | remediation APIs | remediation permission |
| Reports centre | AI Hacker | final customer-deliverable output | admin/CTO | reports and history | review final report | export or share | report API | report access |
| Activity log | AI Hacker | operational review | admin | recent actions | inspect timeline | filter by status | activity APIs | audit access |

## 4. Screen inventory notes

- All screens should support loading, empty, and error states.
- Every user-facing action should indicate whether it is a read-only, approval-required, or execution-required step.
- Product identity and permissions must be represented in the navigation and header.
- Screens with sensitive output must support permission-aware data visibility.
