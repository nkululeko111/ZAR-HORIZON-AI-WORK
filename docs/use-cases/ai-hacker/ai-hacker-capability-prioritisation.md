# AI Hacker Capability Prioritisation

## 1. Purpose

This document prioritises the AI Hacker capabilities according to their business value, technical complexity, customer relevance, risk, and requirement for human oversight. The purpose is not to declare a final MVP but to identify the strongest early capability set and the areas that still need broader validation.

## 2. Prioritisation matrix

| Capability | Target customer segment | Problem addressed | Security value | Technical complexity | Required tools | Required integrations | Human oversight | Operational risk | Potential measurable outcome | Suggested priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Asset discovery and reconnaissance | all segments | unknown external footprint | high | medium | medium | low | medium | low-medium | clearer exposure map and target inventory | Foundational capability |
| Web application security review | software companies, SaaS, digital businesses | release risk and app exposure | very high | high | high | medium | high | medium | fewer risky release issues and better pre-release security posture | Foundational capability |
| API security review | software companies, SaaS, fintech | unauthorised access and data exposure | very high | high | high | medium | high | medium | fewer auth and data exposure issues | Foundational capability |
| Network and infrastructure assessment | MSPs, digital SMEs, IT teams | exposed services and misconfiguration | high | medium-high | medium | medium | medium | medium | better network exposure understanding | High-value capability |
| Cloud configuration review | SaaS, cloud-hosted businesses | cloud exposure and permission drift | high | high | high | high | high | medium | lower cloud misconfiguration risk | High-value capability |
| Identity and access review | all digital users, SaaS, fintech, MSP | privilege weakness and access control gaps | very high | medium-high | medium | medium | high | medium | fewer privilege abuse and account takeover risks | Foundational capability |
| Vulnerability intelligence and validation | all segments | false positives and weak triage | very high | medium-high | medium | low | high | low-medium | better prioritisation and fewer wasted efforts | Foundational capability |
| Attack path and risk analysis | all segments with meaningful exposure | isolated issues without practical context | high | high | medium | low | high | medium | clearer risk prioritisation and decision support | High-value capability |
| Remediation guidance | all segments | weak remediation execution | high | medium | low-medium | low | medium | low | faster fix quality and better follow-through | Foundational capability |
| Retesting and verification | all segments | unverified fixes | very high | medium | medium | low | medium | low-medium | stronger trust in security outcomes and fewer false closures | Foundational capability |
| Security report generation | all segments | poor stakeholder communication | high | low-medium | low | low | medium | low | clearer decision-making and better customer communication | Foundational capability |
| Continuous monitoring | enterprise and managed service customers | recurring risk drift | medium-high | high | high | high | high | medium | earlier detection of new risk exposure | Later-stage capability |

## 3. Priority categories

### Foundational capabilities

These should be core to the first product definition because they are directly tied to real security pain and repeatable workflow value.

- asset discovery and reconnaissance
- web application security review
- API security review
- identity and access review
- vulnerability intelligence and validation
- remediation guidance
- retesting and verification
- security report generation

### High-value capabilities

These are strong strategic capabilities but may require more customer validation and more careful workflow design before being treated as part of the initial launch wedge.

- network and infrastructure assessment
- cloud configuration review
- attack path and risk analysis

### Later-stage capabilities

These are credible product capabilities, but they are not the best starting point for initial market entry.

- continuous monitoring

### Research required

The following areas require more customer validation and technical specification before becoming core product claims:

- broad cloud security automation without clearly defined access boundaries,
- highly aggressive or intrusive testing methods,
- continuous monitoring service models,
- deep privilege escalation validation across varied environments,
- deliverables that depend on highly specialised human security interpretation.

## 4. Recommended initial capability set

The most credible initial capability set is:

1. asset discovery and reconnaissance,
2. web application assessment,
3. API security assessment,
4. identity and access review,
5. vulnerability validation and evidence management,
6. remediation guidance,
7. retesting and verification,
8. security reporting.

This set is the strongest early wedge because it is:

- aligned to clear customer pain,
- practical and recognisable to technical buyers,
- likely to create immediate value,
- more credible than a generic “scan everything” story,
- aligned with the founder-approved AI Hacker vision.

## 5. Conclusion

The AI Hacker should not begin with a vague promise of general security automation. It should begin with the most practical, evidence-based, and trusted security workflows: discovery, validation, remediation guidance, and retesting. These are exactly the capability areas that the customer will understand and that can support an honest, defensible product story.
