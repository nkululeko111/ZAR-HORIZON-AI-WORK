# Security testing and assurance

## 1. Purpose

This document defines a controlled security assurance model for the project. It does not permit real offensive testing against external targets or live systems.

## 2. Security assurance principles

- Security assurance is a controlled engineering and governance activity.
- The project must validate controls in isolated environments.
- Negative tests must prove the system rejects out-of-scope actions.
- Evidence must be captured and reviewed.
- The system must fail closed when policy or scope is ambiguous.

## 3. Assurance scope

The project should validate:

- authentication and authorization flows,
- tenant and workspace boundaries,
- product separation,
- permission enforcement,
- approval workflow integrity,
- evidence handling,
- secret management patterns,
- background job restrictions,
- logging and audit integrity.

## 4. Example negative tests

- a Business Partner workflow attempts a Hacker action,
- a user without workspace access tries to retrieve or modify records,
- an approval request is replayed after an approval change,
- an AI Hacker action is attempted outside the approved scope,
- a model attempts a privileged action without matching backend enforcement,
- a secret value appears in logs or reports.

## 5. Future fixtures and controls

The project should maintain isolated security fixtures such as:

- intentionally vulnerable local services,
- test-only targets and containers,
- mock vendors and integrations,
- evidence-capture validation environments.

These fixtures must remain isolated and should never be deployed to public or production networks.
