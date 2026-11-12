---
applyTo: "apps/web/**/*.{ts,tsx,css},apps/web/**/*.mdx,packages/**/*.{ts,tsx}"
---

# Frontend instructions

- Treat the web app as a presentation layer only; do not assume the UI is a trust boundary.
- Respect the existing Next.js + React + TypeScript + Tailwind setup in `apps/web`.
- Keep interface changes small, testable, and aligned with the approved UX and product documentation.
- Do not create pages, flows, routes, or components beyond the approved design scope.
- Do not treat Business Partner and AI Hacker as equivalent domains in the UI; each product should remain clearly separated in permissions and presentation.
- Prefer existing component patterns and repository conventions over adding packages or wrappers.
- If a change affects shared platform UX, check the approved UX and architecture docs before proceeding.
- Never rely on a frontend-only security check; all critical permissions and approval logic must be enforced in the backend and/or platform model.

For product work, read `docs/ux/`, `docs/products/`, and `docs/architecture/` before proposing changes.
