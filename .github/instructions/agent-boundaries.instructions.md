---
applyTo: "agents/**/*.py,agents/**/*.toml,docs/**/*.md"
---

# Agent boundaries and approval instructions

- The shared platform can host shared infrastructure, but it does not share authority across products.
- AI Business Partner and AI Hacker must remain separate operational domains with distinct permissions and capabilities.
- Business Partner workflows must not inherit offensive security tools, execution privileges, or Hacker-specific testing scopes.
- AI Hacker workflows must require explicit authorisation, testing scope, evidence capture, and controlled execution.
- High-risk decisions must be tied to the exact action and parameters; do not rely on broad trust or implicit approval.
- Do not invent new tool registries, permissions, or execution models without checking the approved architecture and API documentation.
- Keep audit trails and evidence handling explicit and reviewable.

Before making changes in the agent domains, read `docs/architecture/`, `docs/api/`, `docs/products/`, and the relevant product spec documents.
