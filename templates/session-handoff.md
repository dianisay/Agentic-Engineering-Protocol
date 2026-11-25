# Session handoff

- Handoff ID and status: [in progress / ready for review / closed]
- Sender and recipient roles: [roles or neutral identifiers]
- Scope and objective: [work covered; exclusions]
- As-of date and version: [date; version]
- Work item and effective contract: [ID; revision; amendment history]
- Baseline and current execution state: [versions; state; observation evidence]
- Write ownership: [artifact or partition; current owner; proposed recipient;
  transfer authority; quiescence evidence or unknown]

## Ready for review

Complete before declaring the work ready; use `not available` with a reason where
necessary rather than implying an unperformed check.

- Claims and outcomes: [each claim; scope; confidence and evidence reference]
- Version and integrity: [artifact version; hash algorithm and digest, or reason
  unavailable; how to identify exact reviewed state]
- Validation: [method, evaluator, environment, inputs, commands or procedure,
  results, date, and evidence; distinguish failed and unrun checks]
- Validation record: [link to the completed
  [validation report](validation-report.md), or pending with reason]
- Limitations and unresolved issues: [unknowns, exclusions, risks, conflicts]
- Files changed or delivered: [neutral path or URI; role; version or digest]
- Protected or untouched files: [identifiers and restrictions]
- Freeze boundary: [exact artifacts/version and effective time; permitted actions
  while under review; approval required to change; how changes invalidate review]
- Dependencies and pending approvals: [item; owner; state; next action]
- Reviewer request: [decision, acceptance criteria, reviewer role, and deadline
  or trigger]

Confidence values: `CONFIRMED`, `SUPPORTED`, `SELF-REPORTED`, `CONFLICTING`,
`UNVERIFIED`, `SUPERSEDED`. Explain the basis and cite evidence.

## Continuity and safe stop

Capture the [handoff packet requirements](../protocol/08-handoff-and-closure.md#handoff-packet).

- Approval validity: [approval IDs/revisions; expiry/revocation state; pending
  requests; actions not authorized for the recipient]
- Resource reconciliation: [consumed, reserved, remaining; units; accounting
  gaps; accountable owner]
- Pending operations and external effects: [process/job/session IDs; actual state
  and observation time; partial/uncommitted outputs; unknown effects]
- Watchers and ongoing safeguards: [owner; lifetime; authorized cleanup;
  safeguards that must remain operating]
- Recovery and exact next safe action: [environment; reproduction references;
  access limits; prerequisite and authority needed to continue]
- Failure and decision history: [original records; rejected alternatives;
  supersession links; unresolved contradictions]
- Retention and handling: [authorized readers; preservation/removal policy]

## Review outcome and closure

- Review decision and authority: [accepted / changes requested / blocked; role;
  date; reference]
- Changes since freeze and revalidation: [none or details; new version and review]
- Remaining actions and owner: [action; role; due condition]
- Closure decision: [closed / not closed; authorized role; date; rationale]
- Final artifact and evidence locations: [neutral references; access and
  retention conditions]
- Terminal disposition and operational status: [completed and accepted /
  transferred / blocked or paused / failed / cancelled; remaining live or unknown
  operations and owner; administrative closure is separate]
- Reopening trigger: [event or human decision; linked new attempt/revision]
