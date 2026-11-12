# Shared platform MVP requirements

## Objective

Define the shared platform foundations required for both the AI Business Partner and AI Hacker to operate safely, reliably and in a commercially viable way.

The shared platform must support both specialist products without creating cross-product authority or capability inheritance.

## Shared platform requirement classes

### Required for first release

These are needed before either product can be considered operational in a meaningful way.

- authentication and user identity management;
- organisation and workspace management;
- multi-tenancy and tenant boundaries;
- user roles and permissions;
- basic subscription and entitlements foundation;
- audit logs for actions and approvals;
- execution history for agent tasks;
- approved tool and workflow policy controls;
- document storage and retrieval;
- notification framework;
- AI provider abstraction layer;
- basic integration foundation with secure credential handling;
- approval workflow engine for high-risk actions;
- workspace and data separation by product.

### Required before commercial launch

These should be in place before broad commercial activation, even if initial pilots can proceed with a simpler setup.

- stronger role-based authorisation model;
- tighter tenant-level security controls;
- integration lifecycle and credential rotation management;
- more robust permission checks for each specialist product;
- advanced audit and evidence retention policy;
- customer-facing approval and escalation flows;
- operational monitoring and failure handling.

### Can be deferred

These are useful but not required for the first release.

- rich advanced reporting dashboards;
- advanced automation orchestration beyond the product’s initial workflows;
- deep custom integration marketplace;
- extensive analytics and BI features for the platform itself;
- broader workflow templates across all possible product segments.

### Not required

These are outside the MVP foundation and should not be created as shared assumptions.

- shared product authority between AI Business Partner and AI Hacker;
- a common permission model that overrides domain safety boundaries;
- unrestricted cross-product data access;
- platform-level permissions that let one product operate as the other.

## Product boundary rule

The shared platform is shared at the infrastructure and control-layer level, but not at the authority level. The Business Partner must not inherit security-test permissions, and the AI Hacker must not inherit the business-operational permissions of the Business Partner.

## Requirement details

### Authentication

Required for first release.

Needed to support user identity, organisation membership and role-based access.

### Organisation management

Required for first release.

Needed to support tenancy and customer separation.

### Multi-tenancy

Required for first release.

Needed to isolate data, permissions and execution logs by organisation.

### User roles and permissions

Required for first release.

Must be product-aware and role-aware so the Business Partner and AI Hacker do not share capabilities.

### Subscription and usage foundations

Required for first release.

Needed to support customer onboarding and entitlement controls.

### Audit logs

Required for first release.

Needed for both business and security actions, especially the AI Hacker.

### Execution history

Required for first release.

Needed for workflow review, debugging and trust-building.

### Notifications

Required for first release.

Needed for approval requests, task updates, security findings, and completion status.

### Document storage

Required for first release.

Needed to store operating records, reports, task outputs and customer-facing documents.

### AI provider abstraction

Required for first release.

Needed to keep model use configurable and separate from product logic.

### Tool execution controls

Required for first release.

Needed to constrain which tools, actions and integrations each product may use.

### Approval management

Required for first release.

Needed to gate sensitive business actions and security testing actions.

### Integration foundations

Required for first release.

Needed to allow data import and selected workflows while keeping credentials and permissions scoped.

## Shared platform conclusion

The shared platform MVP is not a single application layer for both products. It is the minimum control, identity, productivity and audit layer needed to support two independent specialist product engines with separate permission models and operational boundaries.
