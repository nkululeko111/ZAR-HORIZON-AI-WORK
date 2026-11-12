# AI agent security

## 1. Purpose

This document defines the security and reliability controls expected for AI assistants and agentic workflows in ZAR HORIZON AI @WORK.

## 2. Core principles

- An LLM cannot be the final authority on permissions, approvals, or policy enforcement.
- Tool outputs must be treated as untrusted data.
- Every action must be tied to an identity, permission set, approval decision, and evidence trail.
- High-risk actions require explicit review and approval.
- Execution logs must record what happened and why it was allowed.

## 3. Risk categories

### Prompt injection

- user and document content must be considered untrusted,
- tool instructions must be separated from user-supplied content,
- prompt data should not override backend security policy.

### Malicious or untrusted documents

- uploaded files must be classified and scanned where applicable,
- suspicious or harmful content should not be allowed to drive privileged actions,
- evidence and documents should be stored with provenance metadata.

### Tool misuse

- tools must be classified by permission and approval level,
- tool calls must be validated against the active execution context,
- tool outputs must not bypass policy checks.

### Over-scoped permissions

- every tool, action, and workflow must be bound to the correct domain,
- product boundaries must not be merged by accident,
- agent permissions must be scoped to the user, workspace, and product.

## 4. Reliability requirements

The system should protect against:

- hallucinated tool selection,
- incorrect action attempts,
- misleading or incomplete reports,
- unsafe retry behaviour,
- approval bypass attempts,
- excessive or hidden permissions,
- excessive token or usage abuse.

## 5. Evidence handling

Agent execution records should include:

- request context,
- decision rationale,
- tool or workflow selected,
- parameters and action scope,
- approval state,
- output and status,
- evidence references,
- failure and retry information.

This supports audit, post-incident review, and dispute resolution.
