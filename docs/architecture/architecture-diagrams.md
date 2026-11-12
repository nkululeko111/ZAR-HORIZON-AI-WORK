# Architecture diagrams

This document contains the core Mermaid diagrams for the proposed architecture. Each diagram reflects the shared platform model, the two specialist product domains, and the execution safety constraints described in the architecture package.

## 1. Overall platform architecture

```mermaid
flowchart LR
    User[End User] --> Web[Next.js Web App]
    Web --> API[FastAPI Platform API]
    API --> Auth[Identity & Access]
    API --> Tenancy[Tenant / Workspace / Policy]
    API --> BP[AI Business Partner Domain]
    API --> Hacker[AI Hacker Domain]
    BP --> ToolsBP[Business Tools & Integrations]
    Hacker --> ToolsHack[Security Tool Registry & Isolated Worker]
    API --> Audit[Audit & Evidence Store]
    API --> AI[AI Provider Abstraction]
    API --> DB[(PostgreSQL)]
    API --> Obj[(Object / Document Storage)]
    BP --> DB
    Hacker --> DB
    ToolsHack --> Sandbox[Isolated Security Execution Boundary]
    Sandbox --> Evidence[Evidence Store]
```

### Explanation

The platform API sits between the web app and the core shared services. The business and security domains each have their own execution logic and permission model, while the shared platform provides identity, policy, storage, AI abstraction, and audit support.

## 2. Business Partner component architecture

```mermaid
flowchart TD
    Input[Business Information / Uploaded Data] --> Ingest[Data Ingestion]
    Ingest --> Normalize[Data Normalisation & Quality]
    Normalize --> Context[Business Context Manager]
    Context --> Finance[Financial Analysis Engine]
    Context --> Reason[Business Intelligence & Reasoning]
    Context --> Research[Research Capabilities]
    Finance --> Recommend[Recommended Action]
    Reason --> Recommend
    Research --> Recommend
    Recommend --> Approval[Backend Approval Checks]
    Approval --> Exec[Tool Execution Engine]
    Exec --> Verify[Execution Verification]
    Verify --> Report[Evidence-backed Report]
    Report --> Audit[Execution and Audit Records]
    Context --> Docs[Document Generator]
    Docs --> Report
```

### Explanation

The Business Partner keeps business context and financial logic separate from the LLM reasoning layer. Business calculations are deterministic and auditable, while the reasoning layer interprets results and recommends action.

## 3. AI Hacker component architecture

```mermaid
flowchart TD
    Onboard[Customer Onboarding] --> Authz[Authorisation Management]
    Authz --> Assets[Asset Registry]
    Assets --> Scope[Scope & Exclusions Manager]
    Scope --> Plan[Assessment Planning]
    Plan --> Recon[Reconnaissance Engine]
    Recon --> Web[Web App Testing Engine]
    Recon --> API[API Testing Engine]
    Web --> Validate[Vulnerability Investigation]
    API --> Validate
    Validate --> Evidence[Evidence Collection]
    Evidence --> Classify[Finding Classification & Confidence]
    Classify --> Attack[Attack-Path Analysis]
    Attack --> Remediate[Remediation Guidance]
    Evidence --> Verify[Retesting & Verification]
    Verify --> Report[Security Reporting]
```

### Explanation

The Hacker architecture keeps assessment planning and evidence validation tightly coupled to authorised scope and approval policies. Findings are not treated as valid until they are validated and tied to evidence.

## 4. Agent execution lifecycle

```mermaid
sequenceDiagram
    participant U as User
    participant O as Orchestrator
    participant P as Policy Engine
    participant A as Approval Engine
    participant T as Tool Registry
    participant E as Execution Engine
    participant V as Verification
    participant S as Evidence Store

    U->>O: Request task
    O->>P: Validate product, tenant, user context
    P-->>O: Permission status
    O->>T: Identify required tools
    alt Approval required
        O->>A: Request approval
        A-->>O: Approved/Denied
    end
    O->>E: Execute permitted action
    E->>S: Record execution event and output
    E->>V: Validate outcome
    V-->>O: Verified or failed result
    O-->>U: Report outcome and evidence
```

### Explanation

The lifecycle is shared across both products. Approval and policy checks happen before execution, and verification occurs after execution. This pattern prevents the LLM from being treated as the decision boundary.

## 5. Business Partner data flow

```mermaid
flowchart LR
    User[User / Business Owner] --> Ingest[Data Ingestion]
    Ingest --> Validate[Validation & Normalisation]
    Validate --> Context[Business Context Store]
    Context --> Finance[Financial Analysis]
    Finance --> Insight[Business Intelligence]
    Insight --> Action[Recommended Action]
    Action --> Approve[Approval Policy]
    Approve --> Tool[Approved Business Tool]
    Tool --> Verify[Execution Verification]
    Verify --> Report[Business Outcome Report]
    Report --> Audit[Audit + Evidence Records]
```

### Explanation

Business Partner data flows from raw inputs into normalised business context, then into analysis and recommendation. The flow keeps source data, assumptions, and calculations separate so that financial explanations remain grounded in evidence.

## 6. AI Hacker assessment flow

```mermaid
flowchart LR
    Customer[Customer + Assets] --> Onboard[Onboarding]
    Onboard --> Scope[Scope & Exclusions]
    Scope --> Plan[Assessment Plan]
    Plan --> Recon[Permitted Reconnaissance]
    Recon --> Test[Web / API Testing]
    Test --> Findings[Finding Validation]
    Findings --> Evidence[Evidence Collection]
    Evidence --> Risk[Risk & Impact Analysis]
    Risk --> Report[Security Report]
    Report --> Remediate[Remediation Guidance]
    Remediate --> Retest[Retesting & Verification]
```

### Explanation

The Hacker assessment flow is bounded by scope, permissions, and evidence. Nothing moves directly from test execution to final report without validation and evidence capture.

## 7. Tenant and product data boundaries

```mermaid
flowchart TB
    TenantA[Organisation A] --> W1[Workspace A1]
    TenantA --> W2[Workspace A2]
    TenantB[Organisation B] --> W3[Workspace B1]

    W1 --> BP1[Business Partner Data]
    W2 --> BP2[Business Partner Data]
    W3 --> BP3[Business Partner Data]

    W1 --> H1[AI Hacker Data]
    W2 --> H2[AI Hacker Data]
    W3 --> H3[AI Hacker Data]

    Platform[Shared Platform]
    Platform --> Identity[Identity & Policy]
    Platform --> Audit[Shared Audit Records]
    Platform --> Secrets[Secret Store]

    BP1 -. blocked .-> H1
    BP2 -. blocked .-> H2
    BP3 -. blocked .-> H3
    H1 -. blocked .-> BP1
    H2 -. blocked .-> BP2
    H3 -. blocked .-> BP3
```

### Explanation

Each organisation is isolated at the tenant and workspace layers. Product data is separated by domain. Shared platform services remain common, but they do not grant shared authority across the specialist product domains.

## 8. Initial deployment topology

```mermaid
flowchart TB
    Internet[Client / User]
    Internet --> Web[Next.js Frontend]
    Web --> API[FastAPI API]
    API --> DB[(PostgreSQL)]
    API --> Worker[Background Workers]
    API --> Obj[(Object / Document Storage)]
    API --> AI[AI Provider Connectors]
    API --> Audit[Audit & Evidence Services]

    API --> HackerWorker[Isolated AI Hacker Worker]
    HackerWorker --> Tools[Approved Security Tools]
    Tools --> Evidence[Evidence Store]
    HackerWorker --> Sandbox[Restricted Network & Scoped Execution]
```

### Explanation

The deployment model keeps the application stack small and realistic. The main runtime is the shared platform, while the security execution worker remains a separate runtime boundary with limited network and tool access.
