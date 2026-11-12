# Business Partner testing

## 1. Purpose

The Business Partner domain requires strict quality control because it manipulates business decisions, financial flows, and operational recommendations. It must not be treated as a generic chatbot workflow.

## 2. Core quality rules

- Financial arithmetic must be deterministic and testable.
- LLM reasoning must not be treated as the source of truth for arithmetic.
- Recommendations must distinguish verified values, estimates, and assumptions.
- External actions require approval and replay-safe execution records.
- Duplicate external actions must be prevented.
- Results must be explainable and traceable to source data.

## 3. Financial test categories

### Arithmetic correctness

Tests should cover:

- revenue and expense calculations,
- gross margin and net margin,
- profitability ratios,
- cash-flow projections,
- VAT and tax implications where applicable,
- pricing and cost scenarios,
- sales and operating assumptions.

### SME and South African scenarios

The Business Partner should use realistic scenarios with:

- rand-denominated values,
- VAT-aware calculations where relevant,
- SME cash-flow constraints,
- incomplete records,
- duplicate or inconsistent transactions,
- missing supplier or customer records,
- uncertain or partial financial narratives.

### Data quality validation

Tests should cover:

- duplicate records,
- missing fields,
- mismatched dates,
- inconsistent currency or unit assumptions,
- inconsistent period boundaries,
- imported files with missing or malformed values.

## 4. Approval and action verification

Business Partner actions must be tested for:

- approval enforcement,
- exact action scoping,
- duplicate prevention,
- execution verification after external actions,
- logging of source attribution and assumptions,
- ability to halt or reject unsafe recommendations.

## 5. Evidence expectations

Any recommendation should be traceable to:

- the input data used,
- the calculation method,
- the assumptions made,
- whether the figure is verified or estimated,
- the document or evidence source where applicable.

## 6. Professional boundaries

The system must not present itself as a replacement for a chartered accountant, tax professional, or regulated adviser. It should clearly state the limits of its recommendations and the need for human review on material financial decisions.
