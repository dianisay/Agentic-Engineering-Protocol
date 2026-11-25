# Orchestration audit report

Replace bracketed prompts with observations or `not assessed`. Record evidence,
not inferred capabilities; redact sensitive content and use neutral identifiers.

## Audit context and scope

- Audit ID and date: [ID; date and time zone]
- Auditor and independence: [role or pseudonym; relationship to subjects]
- Objective and decisions supported: [purpose]
- In scope: [projects, resources, environments, time period]
- Out of scope: [exclusions and reasons]
- Access exercised: [access level, resources, authorization, restrictions]
- Access not obtained or not attempted: [what and why]
- Method and constraints: [inspection method, sampling, time or resource limits]

## Capability map

Record each operation separately for every relevant interface. A capability is
verified only for the specific scope, identity, and conditions tested. Use
`VERIFIED`, `UNSUPPORTED` (with evidence), or `UNVERIFIED`; absence of a test
does not establish that an operation is unsupported.

| Interface and identity | Operation | Scope and conditions | Status | Test or source and date | Result, limitations, and fallback |
|---|---|---|---|---|---|
| [interface; identity] | Enumerate | [scope] | [status] | [reference] | [result] |
| [interface; identity] | Inspect | [scope] | [status] | [reference] | [result] |
| [interface; identity] | Message | [scope; recipient authorization] | [status] | [reference] | [result] |
| [interface; identity] | Create | [resource type; scope; authorization] | [status] | [reference] | [result] |
| [interface; identity] | [other operation] | [scope] | [status] | [reference] | [result] |

## Findings

| ID | Observation and impact | Evidence reference | Confidence | Scope or limitation | Action and owner |
|---|---|---|---|---|---|
| [ID] | [finding] | [reference] | [value below] | [boundary] | [action; role] |

Confidence values: `CONFIRMED`, `SUPPORTED`, `SELF-REPORTED`, `CONFLICTING`,
`UNVERIFIED`, `SUPERSEDED`. Explain the basis and any differing evidence;
confidence does not replace capability status.

## Access and risk review

- Authorized versus observed access: [comparison; evidence]
- Sensitive or protected resources and handling: [identifiers; restrictions]
- Access gaps, expired permissions, and escalation route: [details]
- Risks, impact, and mitigation: [risk; likelihood/impact if assessed; owner]
- Open questions and follow-up checks: [question; owner; due condition]

## Outcome

- Summary and decisions: [findings and approved actions]
- Unresolved conflicts or limitations: [details]
- Evidence location and retention: [neutral reference; access conditions]
- Review and approval: [reviewer role; date; decision or pending]
