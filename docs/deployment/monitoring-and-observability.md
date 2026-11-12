# Monitoring and observability

## 1. Purpose

This document defines the operational monitoring expectations for the repository without assuming the final production environment is already selected.

## 2. Monitoring categories

### Platform monitoring

- application availability,
- API health and latency,
- database health,
- application error rates,
- service crashes and restarts,
- background job status.

### Agent and workflow monitoring

- execution failures,
- long-running jobs,
- approval delays,
- tool execution failures,
- provider availability,
- model token usage and cost,
- execution status correlations.

### Security monitoring

- failed authorisation attempts,
- suspicious access patterns,
- permission or scope violations,
- unusual execution behaviour,
- evidence capture failures,
- unauthorised API usage.

## 3. Logging expectations

Structured logs should include:

- correlation IDs,
- tenant and workspace identifiers where appropriate,
- user or service identity,
- request metadata,
- action type and result,
- execution status and evidence references,
- timing and error details.

Logs must not expose credentials, secrets, or sensitive customer data unnecessarily.

## 4. Observability requirement

The platform should maintain enough traceability for an incident to be investigated without requiring guesswork. This includes execution lineage, tool activity, and evidence references.
