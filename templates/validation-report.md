# Independent validation report

Use [07 validation](../protocol/07-validation.md). Keep gate outcomes separate
from [evidence labels](../protocol/01-audit.md#common-evidence-and-claim-contract).

## Candidate, gate, and authority

- Report ID, revision, and date: [values; time zone]
- Work item and contract: [ID; effective revision; acceptance criteria reference]
- Validator and independence: [role; relationship to author; shared assumptions;
  independence limitations]
- Candidate and baseline: [artifact locators; versions; digest algorithm and
  digest or reason unavailable]
- Frozen gate: [criteria version; freeze time; decision authority]
- Mutation checks: [versions before/after checks; changes or none]
- Permitted test scope: [read access; isolated test location; authorized actions;
  approval references; prohibited side effects]
- Environment and inputs: [versions; configuration; workload; provenance;
  restrictions; unavailable information]

## Criterion results

Copy a row for every criterion, including the required gates in the protocol.

| Gate / criterion ID | Expected result and method | Observed result | Gate outcome | Evidence label and reference | Limitation / finding / remediation owner |
|---|---|---|---|---|---|
| [scope, correctness, provenance, regression, authority, readiness, or domain criterion] | [threshold; check] | [observation or unrun reason] | [PASS / FAIL / BLOCKED / NOT APPLICABLE] | [label; exact-version evidence] | [details; severity; owner] |

- Procedures actually run: [commands or steps; duration; exit status; raw evidence]
- Checks not run: [criterion; reason; effect on acceptance]
- NOT APPLICABLE justification: [criterion; authority acceptance reference]
- Counterevidence and previous failures: [references; relevance]

## Decision and follow-up

- Overall result and exact scope: [passed / failed / blocked; version/environment;
  unresolved mandatory gates]
- Residual risks: [risk; owner; authorized decision if applicable]
- Remediation and revalidation: [finding; candidate owner; affected checks;
  successor report; preserve prior results]
- Publication or release authority: [separate approval reference or not authorized]
- Handoff: [record location; retention; next safe action]
