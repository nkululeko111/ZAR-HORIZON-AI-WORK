# Day 10 API decisions

## 1. Summary

This document summarises the Day 10 API and tool contract decisions for the ZAR HORIZON AI @WORK platform, AI Business Partner, and AI Hacker products. It preserves the documentation-only scope defined for the exercise and does not claim implementation.

## 2. API design standards

- Use RESTful resource design under `/api/v1`.
- Require structured JSON request and response bodies.
- Standardise error responses with code, message, details, status, and correlation ID.
- Enforce tenant, workspace, product, and entitlement checks on every request.
- Support idempotency and request correlation across state-changing operations.
- Keep authentication at the shared platform boundary.
- Require backend approval for sensitive actions.

## 3. Shared platform endpoint groups

The shared platform API supports:

- authentication and identity,
- organisation and workspace management,
- roles and permissions,
- product entitlements and subscription status,
- agent execution and execution history,
- approvals and approval history,
- documents and evidence,
- notifications and integrations.

## 4. Business Partner endpoint groups

The Business Partner API supports:

- business profile and operating context,
- financial record import and analysis,
- revenue, expense, cash-flow, and profitability summaries,
- budget comparison and performance analysis,
- business action proposals and execution,
- task and document management,
- market research and supplier discovery.

## 5. AI Hacker endpoint groups

The AI Hacker API supports:

- customer and asset registration,
- authorisation and scope definition,
- assessment creation and lifecycle management,
- finding and evidence retrieval,
- remediation and retesting flows,
- final assessment reporting.

## 6. Agent tool contract standard

The shared tool standard requires:

- explicit name, owner, purpose, and scope,
- input and output schemas,
- permission and tenant requirements,
- approval requirements,
- risk classification,
- timeout and idempotency,
- evidence and audit requirements,
- deny-by-default registry behaviour.

The standard tool invocation lifecycle is:

Request → Validate input → Verify identity → Verify tenant → Verify product permissions → Check policy → Check approval → Execute → Capture result → Verify → Record audit event.

## 7. Business Partner tool catalogue

The initial Business Partner catalogue prioritises deterministic financial and operational tools while delaying broader research and quotation capability until the product is mature.

Core tools include:

- `get_business_profile`
- `get_financial_summary`
- `get_revenue_expense_breakdown`
- `calculate_cash_flow`
- `calculate_profitability`
- `compare_budget_actuals`
- `propose_business_action`
- `execute_approved_action`
- `verify_business_action`

## 8. AI Hacker tool catalogue

The initial AI Hacker catalogue is purpose-limited to authorised security assessment and evidence management. It excludes unrestricted shell execution, arbitrary network scanning, and unbounded exploitation.

Core tools include:

- `register_assessment_asset`
- `validate_authorisation`
- `validate_assessment_scope`
- `create_assessment_plan`
- `capture_security_evidence`
- `classify_security_finding`
- `generate_remediation_guidance`
- `request_retest`
- `generate_security_report`

## 9. Approval and asynchronous execution model

- Proposed actions are stored as structured records before execution.
- Approval must match the exact action payload and scope.
- Material changes require new approval.
- Long-running operations are asynchronous and return execution IDs and status URLs.
- Background jobs carry tenant, workspace, and product context securely.
- Final success requires verification and evidence capture.

## 10. Security and authorisation controls

- Platform-level authentication boundary.
- Strict tenant and workspace validation.
- Product entitlements and permission checks.
- Structured validation and output filtering.
- Rate limiting and abuse prevention.
- Sensitive evidence protections and credential isolation.
- Audit logging and idempotency enforcement.
- Security worker boundaries.
- LLM cannot directly access unrestricted database connections, secrets, or arbitrary shell environments.

## 11. Major technical risks

- Approval logic needs clear policy enforcement and role-based escalation.
- External integration authorisation still requires product policy decisions.
- Long-running security research and assessment operations must clearly separate policy checks from execution workers.
- Evidence retention and classification requirements need a formal policy decision.
- Some product-specific operational policies may need founder or legal review before implementation.

## 12. Decisions requiring founder approval

- final approval delegation and escalation model,
- evidence retention duration and access classification,
- security policy for high-risk testing methods,
- external integration onboarding policy,
- final scope of MVP tool catalogue and future tool additions.

## 13. Files created

- [docs/api/api-design-standards.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/api-design-standards.md)
- [docs/api/shared-platform-api-specification.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/shared-platform-api-specification.md)
- [docs/api/business-partner-api-specification.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/business-partner-api-specification.md)
- [docs/api/ai-hacker-api-specification.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/ai-hacker-api-specification.md)
- [docs/api/agent-tool-contract-standard.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/agent-tool-contract-standard.md)
- [docs/api/business-partner-tool-catalogue.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/business-partner-tool-catalogue.md)
- [docs/api/ai-hacker-tool-catalogue.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/ai-hacker-tool-catalogue.md)
- [docs/api/execution-and-approval-api-contracts.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/execution-and-approval-api-contracts.md)
- [docs/api/asynchronous-execution-and-webhooks.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/asynchronous-execution-and-webhooks.md)
- [docs/api/api-security-and-authorisation.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/api-security-and-authorisation.md)
- [docs/api/openapi-and-type-contract-strategy.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/openapi-and-type-contract-strategy.md)
- [docs/api/api-decision-register.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/api-decision-register.md)
- [docs/api/day-10-api-decisions.md](C:/Users/User/Documents/ZAR-HORIZON-AI-WORK/docs/api/day-10-api-decisions.md)

## 14. Confirmation

This work remains documentation-only. No runtime code, application logic, API endpoint implementation, database schema, infrastructure, or dependency changes were created. The repository contains design artifacts only, as required by the task.
