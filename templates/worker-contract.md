# Worker contract

- Contract ID, version, and status: [values]
- Sponsor, worker, and decision authority: [roles or neutral identifiers]
- Validity: [start; end or completion condition]

## Objective and acceptance

- Objective and scope: [specific deliverable and boundaries]
- Measurable acceptance: [metric, threshold, evaluation method, dataset or
  scenario, environment, and required evidence]
- Deliverables and destination: [neutral path or URI; format; versioning]
- Out of scope and prohibited actions: [details]

## Authoritative inputs and history

| Input | Path or URI | Version and hash | Authority or owner | Access and use restrictions |
|---|---|---|---|---|
| [input] | [neutral reference] | [version; hash algorithm and digest, or unavailable] | [role] | [conditions] |

- Input verification and conflict handling: [how to compare; escalation role]
- Prior attempts: [approach; observed result; failure or stop reason; evidence;
  whether retry is authorized]
- Dependencies and readiness: [prerequisite; owner; evidence; fallback]

## Authority and boundaries

| Action | Authorized scope | Conditions and approval | Explicit exclusions |
|---|---|---|---|
| Read | [resources] | [access conditions] | [excluded resources] |
| Write | [paths or artifacts] | [conditions] | [excluded paths] |
| Communicate | [recipients and topics] | [approved methods and conditions] | [prohibited disclosures] |
| Create or execute | [resources or operations] | [authorization and conditions] | [prohibited operations] |

- Protected artifacts: [paths or identifiers; no-modify/no-delete rules;
  handling and preservation requirements]
- Tools and capabilities: [verify availability and authorization before use;
  approved alternatives or manual process if unavailable]
- Human approval required: [actions; approving role; evidence of explicit
  approval; do not proceed while pending]

## Research and execution

- State-of-the-art questions and relevance: [questions and decision impact]
- Primary sources and versions: [original references and dates; access limits]
- Baselines and alternatives: [methods, comparison criteria, tradeoffs, evidence]
- Planned checks: [tests or evaluations; expected result; limitations]
- Reporting cadence and channel: [conditions; verified channel or manual fallback]

## Budgets, gates, and stop rules

- Budget and accounting: [time, compute, spend, calls, or other resources; limits]
- Entry conditions: [authorized inputs, dependencies, and approvals]
- Review and completion gate: [criteria; evidence; reviewer; decision authority]
- Stop or pause immediately on: [boundary breach, approval gap, budget limit,
  unsafe result, conflicting input, or task-specific conditions]
- On stop: [preserve state and evidence; notify authorized role; do not expand
  scope or resume without required approval]
- Failure or blocked path: [report, escalation, and permitted fallback]

## Agreement and changes

- Sponsor authorization: [role; decision; date or pending]
- Worker acknowledgment: [role; date or pending]
- Changes to scope, budget, authority, or criteria: [approval process and log]
