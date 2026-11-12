# Day 14 decisions

## 1. Summary

Day 14 focused on defining the quality, security, deployment, and operational process framework for the repository. The work is documentation-only and intentionally avoids product implementation, runtime changes, and production deployment actions.

## 2. Key decisions captured

- A layered testing model is defined for unit, integration, end-to-end, regression, performance, and reliability testing.
- Business Partner testing requires deterministic financial logic and evidence-backed recommendations.
- AI Hacker testing requires strong negative tests, scope enforcement, and evidence integrity.
- Shared platform security controls emphasise backend enforcement, tenant isolation, and approval-based execution.
- AI agent security focuses on prompt injection, tool misuse, output trust, and untrusted documents.
- Deployment is described as a phased model with local, test, staging, and production stages.
- Monitoring, backup, recovery, and incident response are documented as operational policy requirements.

## 3. Important limits

This documentation does not claim any production deployment or monitoring platform is live or operational. It also does not claim that real security scanning, real agent execution, or external testing has been performed.

## 4. Founder decisions still required

- final cloud provider and region,
- production database hosting,
- secret-management provider,
- backup retention and retention periods,
- RPO and RTO decisions,
- incident notification responsibilities,
- production alerting and support model.

## 5. Final status

The repository now contains a documented testing, security, deployment, monitoring, and recovery strategy that matches the project’s governance-first and no-runtime-change scope.
