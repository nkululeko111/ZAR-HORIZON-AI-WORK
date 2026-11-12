# Entity relationship diagrams

This document contains conceptual ER diagrams for the logical database model. These are design diagrams, not implemented schemas.

## 1. Shared platform and identity

```mermaid
erDiagram
    USER ||--o{ MEMBERSHIP : has
    ORGANISATION ||--o{ MEMBERSHIP : contains
    ORGANISATION ||--o{ WORKSPACE : owns
    USER ||--o{ SESSION : authenticates
    ORGANISATION ||--o{ SUBSCRIPTION : has
    SUBSCRIPTION ||--o{ ENTITLEMENT : grants
    PRODUCT ||--o{ PLAN : defines
    PLAN ||--o{ ENTITLEMENT : supports
    ORGANISATION ||--o{ USAGE_EVENT : records
    USER ||--o{ USER_REQUEST : creates
```

### Explanation

This diagram captures the organisational and identity layer, including membership, workspaces, subscription and entitlement, and usage tracking.

## 2. Tenant and workspace relationships

```mermaid
erDiagram
    ORGANISATION ||--o{ WORKSPACE : owns
    ORGANISATION ||--o{ ROLE : defines
    ROLE ||--o{ PERMISSION : grants
    USER ||--o{ MEMBERSHIP : belongs_to
    MEMBERSHIP }o--|| ROLE : has
    WORKSPACE ||--o{ PRODUCT_SCOPE : contains
    PRODUCT_SCOPE ||--o{ TOOL_DEFINITION : permits
```

### Explanation

The platform keeps user membership and workspace access separate from product capability authorisation. A user may belong to an organisation without automatically gaining every product capability.

## 3. Business Partner

```mermaid
erDiagram
    BUSINESS_PROFILE ||--o{ BUSINESS_OBJECTIVE : has
    BUSINESS_PROFILE ||--o{ FINANCIAL_ACCOUNT : owns
    FINANCIAL_ACCOUNT ||--o{ TRANSACTION : contains
    REPORTING_PERIOD ||--o{ BUDGET : defines
    REPORTING_PERIOD ||--o{ VARIANCE_RECORD : compares
    BUSINESS_PROFILE ||--o{ CUSTOMER : manages
    BUSINESS_PROFILE ||--o{ SUPPLIER : manages
    BUSINESS_PROFILE ||--o{ TASK : tracks
    BUSINESS_PROFILE ||--o{ QUOTATION : generates
    BUSINESS_PROFILE ||--o{ ANALYSIS_RUN : runs
    ANALYSIS_RUN ||--o{ RECOMMENDATION : creates
    RECOMMENDATION ||--o{ PROPOSED_ACTION : leads_to
    PROPOSED_ACTION ||--o{ ACTION_OUTCOME : results_in
```

### Explanation

The Business Partner model links business context, financial facts, analyses, recommendations, and final action outcomes.

## 4. AI Hacker

```mermaid
erDiagram
    SECURITY_CUSTOMER ||--o{ AUTHORIZATION_RECORD : has
    SECURITY_CUSTOMER ||--o{ ASSET : owns
    ASSET ||--o{ APPLICATION : contains
    ASSET ||--o{ API : contains
    SECURITY_CUSTOMER ||--o{ ASSESSMENT : runs
    ASSESSMENT ||--o{ ASSESSMENT_RUN : contains
    ASSESSMENT_RUN ||--o{ TOOL_INVOCATION : executes
    ASSESSMENT ||--o{ VULNERABILITY_FINDING : reports
    VULNERABILITY_FINDING ||--o{ REMEDIATION_RECORD : requires
    VULNERABILITY_FINDING ||--o{ FINDING_EVIDENCE : supported_by
    REMEDIATION_RECORD ||--o{ RETEST_RECORD : validates
```

### Explanation

The Hacker model preserves the chain from authorisation and scope to assessment, evidence, validation, and retesting.

## 5. Agent execution, approvals and evidence

```mermaid
erDiagram
    USER_REQUEST ||--o{ EXECUTION_RUN : produces
    EXECUTION_RUN ||--o{ EXECUTION_STEP : contains
    EXECUTION_RUN ||--o{ TOOL_INVOCATION : uses
    TOOL_INVOCATION ||--o| TOOL_RESULT : returns
    APPROVAL_REQUEST ||--o| APPROVAL_DECISION : resolves
    EXECUTION_RUN ||--o{ VERIFICATION_RECORD : verifies
    EXECUTION_RUN ||--o{ EVIDENCE_REFERENCE : attaches
    EVIDENCE_RECORD ||--o{ EVIDENCE_REFERENCE : referenced_by
    AUDIT_EVENT ||--o{ RESOURCE_EVENT : logs
```

### Explanation

This diagram represents the execution and governance layer: requests, tool execution, approval gating, evidence linkage, and verification.

## 6. Product data boundaries

```mermaid
erDiagram
    ORGANISATION ||--o{ BUSINESS_PARTNER_RECORD : owns
    ORGANISATION ||--o{ AI_HACKER_RECORD : owns
    BUSINESS_PARTNER_RECORD }o--|| ORGANISATION : tenant_scope
    AI_HACKER_RECORD }o--|| ORGANISATION : tenant_scope
    BUSINESS_PARTNER_RECORD ||--o{ BUSINESS_PARTNER_EVIDENCE : linked_to
    AI_HACKER_RECORD ||--o{ AI_HACKER_EVIDENCE : linked_to
    BUSINESS_PARTNER_RECORD }o--|| PLATFORM_POLICY : restricted_by
    AI_HACKER_RECORD }o--|| PLATFORM_POLICY : restricted_by
```

### Explanation

This diagram makes clear that the two product domains are separate despite sharing the same platform and infrastructure. The platform policy layer governs access and separation.
