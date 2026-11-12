# Development-readiness scorecard

## Status scale

- **Ready** — sufficient and verified for the stated development activity.
- **Ready with conditions** — usable for limited work after specified conditions or checks.
- **Not ready** — material decisions or controls are missing for the stated activity.
- **Not assessed** — insufficient evidence for a reliable assessment.

This scorecard intentionally avoids one aggregate score that could hide product or security blockers. “Block” identifies the activity blocked, not necessarily all repository work.

| Area | Status | Evidence from repository | Outstanding gaps / next action | Blocks |
|---|---|---|---|---|
| 1. Product definition | Ready with conditions | Product specifications define separate visions, capabilities, and boundaries in `docs/products/`; use cases and MVP recommendations exist | Approve one product, customer, first workflow, exclusions, and acceptance measures; distinguish approved decisions from proposals | Product feature commitment |
| 2. Customer and market understanding | Not ready | Research sources, target profiles, competitive material, interview plans exist; validation tracker has only a header | Conduct and record customer interviews; validate problem urgency, buyer, workaround, and willingness to pay; recheck competitive claims | Commercial scope and claims |
| 3. Business Partner MVP | Ready with conditions | MVP/workflow, API, and UX design propose business-performance analysis, deterministic calculations, evidence, and action approval | Approve source/import path, calculation assumptions, exact action scope, and customer acceptance criteria; validate with SMEs | Financial/action MVP implementation |
| 4. AI Hacker MVP | Not ready | Product/use-case/API/security docs define authorised assessment intent and safety boundaries | Resolve authorization proof, scope model, isolated worker, network restrictions, credentials, emergency stop, evidence/confidence rubric, and independent review | Any automated assessment capability |
| 5. Shared architecture | Ready with conditions | Modular-monolith/shared-platform direction and product separation are documented in `docs/architecture/` | Confirm implementation choices and decision status; specify job context, policy boundaries, and service ownership | Sensitive shared-platform features |
| 6. Database design | Not ready | Initial models/migration and some relational tenancy constraints exist; database design is documented | Decide membership/roles, product entitlements, approval/evidence entities, RLS vs application enforcement, lifecycle and retention | Tenant-sensitive product data |
| 7. API design | Ready with conditions | API standards and product contracts are documented; runtime currently has health/version routes only | Select and freeze only the first workflow contract; decide auth, errors, idempotency, async/cancellation, audit semantics | Product API implementation |
| 8. UX and user journeys | Ready with conditions | User journeys, screens, approval states, and wireframes exist in `docs/ux/` | Validate chosen workflow, visual direction, accessibility/responsive details, uncertain-data presentation, and failure/cancel/verification states | Customer-ready product UI |
| 9. Development environment | Ready with conditions | Node/pnpm, Python/uv, PostgreSQL, Docker Compose, and local docs/configuration are present | Verify clean local setup, compose startup, migration flow, and actual quality commands; no successful run was established in this audit | Reliable team onboarding until verified |
| 10. AI coding-agent governance | Ready with conditions | `AGENTS.md`, Copilot instructions, path-specific rules, Cursor rules, and maintenance docs exist | Clarify approved versus proposed design status; validate tool loading in Copilot/Cursor; retain review of untracked instruction files | No direct code blocker; governance consistency before implementation |
| 11. Testing strategy | Ready with conditions | Test policies, commands, CI workflow, and at least a database tenancy test exist | Run current checks; add tests with each feature; plan E2E/negative security coverage; clarify provisional Python 3.14 matrix treatment | Product acceptance until executed checks exist |
| 12. Security design | Not ready | Security and agent-control documents specify important principles and negative scenarios | Implement and test auth, tenant/product enforcement, approval binding, evidence, secret handling; Hacker worker isolation and stop controls are blockers | Tenant-sensitive or agent-executed features |
| 13. Deployment and operations | Not ready | Local Compose and deployment/monitoring/backup/incident-response documents exist | Choose provider/region, production secrets, retention, RPO/RTO, owners, alerts, rollout/rollback, and test recovery | Staging/production release |

## Interpretation

The project is ready for **engineering-foundation verification, discovery, and bounded design decisions**. It is not ready to begin broad implementation or production work. The hard product/security blockers are concentrated in rows 1–7 and 12; deployment decisions can be deferred until before production.
