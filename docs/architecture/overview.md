# Architecture overview

ZAR HORIZON AI @WORK uses a shared platform with two independent specialist systems.

## Shared platform

The Next.js web application and FastAPI service provide the future home for identity, organisation
and workspace management, audit events, shared configuration, and integrations. PostgreSQL is the
initial persistence layer. Workspaces carry an organisation identifier, and sessions enforce a
composite organisation/workspace relationship so a session cannot reference a workspace owned by
another organisation.

## Independent agent boundaries

The Business Partner and Hacker are separate Python packages with distinct configuration prefixes,
service entry points, and tool registries. Their tool registries are empty in this foundation.
Neither package imports the other's code. The shared platform does not grant specialist permissions;
future integrations must explicitly authorize the appropriate agent and tenant.

This keeps business workflows and permissions separate from security assessment capabilities while
allowing both products to reuse platform-level identity, storage, and audit foundations. Agent
orchestration and tools are intentionally not implemented.

## Initial runtime topology

The development Compose stack contains only PostgreSQL, the platform API, and the web application.
The agent packages remain independently deployable application boundaries and are not started by
Compose until they have real, reviewed service requirements.
