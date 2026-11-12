# Attack Path and Risk Analysis

## 1. Purpose

This document defines how the AI Hacker converts isolated security weaknesses into meaningful risk narratives. A single issue may be important, but a real security assessment must explain how multiple issues may combine into a realistic path to compromise, service disruption, or data loss.

## 2. Core principle

Security risk is not simply the number of vulnerabilities. It is the combination of:

- exposure,
- exploitability,
- asset sensitivity,
- access privilege,
- business impact,
- human and process controls,
- and the likelihood of a practical compromise path.

## 3. Attack path model

The AI Hacker should evaluate whether the following patterns matter in combination:

- exposed public service plus weak authentication,
- public web application plus sensitive data exposure,
- cloud misconfiguration plus excessive identity permissions,
- weak access controls plus unprotected API service,
- vulnerable admin interface plus poor segmentation,
- misconfigured infrastructure plus outdated software or exposed admin pathways.

### Example attack path types

#### Public service to privileged compromise

- an exposed application with weak access controls,
- vulnerable auth or session handling,
- insufficient segregation of roles,
- resulting risk of account takeover or privilege misuse.

#### Internet-exposed app to data exposure

- public web app or API,
- sensitive configuration or data exposed,
- poor output handling or missing auth controls,
- business impact includes data leak and reputational risk.

#### Cloud exposure to identity abuse

- public cloud resource exposure,
- excessive permissions,
- weak identity boundaries,
- risk of privileged misuse or broader compromise.

## 4. Correlation logic

The AI Hacker should correlate findings across:

- application layers,
- infrastructure and network layers,
- identity and access controls,
- cloud configuration,
- API design and authorisation,
- business workflows and sensitive data.

The goal is to identify whether weaknesses are isolated or part of a larger exploitable chain.

## 5. Business impact assessment

Each attack path should be evaluated in terms of:

- impact on customer data,
- impact on business continuity,
- impact on operational trust,
- risk of financial harm,
- risk of regulatory or legal exposure,
- the speed and cost of remediation,
- the likelihood of exploitation in the real environment.

## 6. Practical exploitability assessment

A key requirement is to distinguish between a theoretical issue and a practically exploitable issue.

Questions to answer:

- Is the service externally reachable?
- Is the vulnerable path reachable by an attacker?
- Are the conditions realistic in the actual environment?
- Does an attacker need a previously compromised account or an admin position?
- Is any privileged access required for the path to matter?
- Could the issue be chained with another valid weakness?

## 7. Risk prioritisation model

The product should prioritise attack paths based on:

- probability of exploitation,
- severity if compromised,
- exposure to public networks,
- sensitivity of the affected system,
- whether the path enables broader compromise,
- whether the risk has clear business impact.

## 8. Risk categories

The product should track findings in a way that separates:

- a low-risk isolated configuration issue,
- a medium-risk weakness with possible user impact,
- a high-risk issue with clear business impact,
- a critical exposure that enables compromise or large-scale loss.

## 9. Output format for attack path analysis

Each attack path should include:

- scenario name,
- involved assets,
- initial condition or exposure,
- step-by-step path,
- required privileges or conditions,
- business impact,
- confidence level,
- recommended mitigation priority.

## 10. Example attack-path narrative

A publicly exposed application includes an auth weakness, the user roles are poorly separated, and an API endpoint exposes sensitive data. The combined path creates a realistic risk where an attacker could access data or perform unauthorised action if the weakness is successfully exploited. The path matters because it affects customer trust, data exposure, and potential operational disruption.

This is the kind of risk narrative the AI Hacker should produce, not just a list of individual issues.

## 11. Limits and caution

The product must not overstate risk. It should explicitly label:

- what is validated,
- what is inferred,
- what remains unvalidated,
- what assumptions are still open.

A path is only meaningful when supported by evidence and scope control.

## 12. Summary

Attack-path analysis is the bridge between vulnerability discovery and business risk. It allows the AI Hacker to move beyond static issue lists and provide a realistic understanding of how security weaknesses can matter in the real environment, while still respecting the need for evidence, scope control, and human oversight.
