# 02 — Portfolio research and planning

## Purpose

Turn the [audit](01-audit.md) into a research-grounded portfolio of bounded work
with explicit value, dependencies, alternatives, costs, and acceptance gates.
Planning is not activation, an architecture approval, or a commitment to execute
every idea. Existing workers remain unchanged.

Use the portfolio, research, decision, and work-item records in
[templates](../templates/). Apply the evidence and authority rules from [01](01-audit.md).

## Research the problem and current practice

1. **Frame the decision.** State the outcome, intended users or beneficiaries,
   constraints, current baseline, and questions for which research could change
   the plan. Define what “better” means before selecting an approach.
2. **Plan evidence gathering.** Record the search questions, relevant terminology,
   inclusion/exclusion criteria, source classes, coverage dates, research budget,
   and stopping criteria. Establish whether external retrieval is available and
   authorized. If unavailable, use accessible sources and identify the gap; request
   human-provided references when needed. Never imply that a search was performed
   or invent citations.
3. **Prefer primary, credible sources.** Examine original research and evaluations,
   standards, official specifications, maintained documentation, primary datasets
   where applicable, and original implementation or incident records. Use secondary
   summaries for discovery and context, not as substitutes when primary evidence
   is needed. Assess methodology, independence, conflicts of interest, corrections,
   and relevance; prestigious venues or recent dates alone do not establish truth.
4. **Compare the state of the art.** Identify established baselines, credible
   contemporary alternatives, a simple feasible option, and the no-change option.
   Distinguish reported performance from independently reproduced performance.
   Compare matched objectives, inputs, environments, constraints, and measurement
   methods; do not rank incompatible headline numbers.
5. **Assess usefulness and feasibility.** Explain which findings would help this
   objective, what adaptation would be required, and why additional complexity is
   worthwhile. Record negative findings and plausible reasons not to adopt an
   apparently leading technique.
6. **Bound the conclusion.** State “best supported among the reviewed sources as of
   [date], within [scope]” rather than claiming universal superiority. Label stale,
   inaccessible, conflicting, or untested claims using [01](01-audit.md).

For each retained source record its title, creator or publishing body, locator,
publication/update date, access date, relevant version, source type, supported
claims, methodological limitations, and applicability. Record “unknown” for
unavailable dates. Capture reproduction requirements, availability of supporting
artifacts, dependencies, expected resources, licensing and redistribution limits,
and any unresolved legal or ethical constraints. Public accessibility is not a
license to copy or redistribute.

The research exit condition is sufficient evidence to justify a bounded next
decision, not exhaustive literature collection. A research budget exhaustion
produces an explicitly incomplete review and a decision request, not fictional
certainty.

## Build the portfolio

Create one work item per independently accountable outcome. Each item includes:

- Objective, usefulness, priority rationale, non-goals, and research/evidence links.
- Inputs and exact baseline versions; proposed outputs and artifact boundaries.
- Dependencies and their required states, including human decisions and external
  prerequisites. Distinguish hard prerequisites from convenient sequencing.
- Candidate approach, meaningful alternatives, unresolved assumptions, risks,
  disconfirming tests, and a reversible first step where feasible.
- Acceptance criteria, required independent validation, and stop conditions.
- Logical capability needs, a proposed owner role, reviewers, and possible parallel
  partitions. Final routing belongs in [03](03-session-routing.md).
- Resource estimates as ranges with assumptions: time, compute, financial cost,
  storage, external effects, and coordination load. Separate estimates from
  measured consumption and show uncertainty.
- Required approvals, approval dependencies, and consequences of delay or failure.

Represent dependencies as an acyclic graph. Detect cycles, resource conflicts,
shared-artifact contention, and tasks whose prerequisites are impossible to
verify. Resolve them explicitly before making those tasks ready.

## Select and sequence

1. Rank feasible items by expected value, evidence strength, risk reduction,
   urgency, dependency impact, and total cost. Record the reasoning rather than
   concealing tradeoffs behind an unexplained score.
2. Prioritize inexpensive, discriminating tests when uncertainty could invalidate a
   larger commitment. A proposed experiment still needs any applicable approval.
3. Set portfolio-wide ceilings and reserve capacity for validation, recovery, and
   handoff. Allocate subordinate budgets without assuming unused resources are
   automatically transferable.
4. Select a bounded wave of work. Parallelize only independent outcomes with
   non-overlapping write ownership and adequate review capacity.
5. Mark items as proposed, awaiting evidence, awaiting approval, ready for routing,
   deferred, or rejected with reasons. Preserve rejected alternatives and failed
   hypotheses so later sessions do not unknowingly repeat them.

## Approval and change control

Present consequential choices to the authorized human with alternatives, expected
benefits, downside, resource bounds, and requested approval scope. Architecture
research can recommend a decision; it cannot authorize adoption.

When evidence, goals, dependencies, or costs change materially, append a decision
delta identifying affected items, approvals, and acceptance criteria. Do not
silently rewrite the accepted baseline or direct existing workers to change course.
Apply amendments through [04](04-session-activation.md) and communicate the delta
through [05](05-inter-agent-communication.md).

Token reduction is subordinate to completeness and reliable decisions. Prefer
bounded work, reusable evidence references with full authorized evidence access,
and concise deltas over withholding context or skipping research.

## Exit gate

A work item is ready for [03 — Session routing](03-session-routing.md) only when
its objective, dependencies, evidence gaps, artifact boundary, acceptance criteria,
budget assumptions, and approval requirements are explicit. “Ready for routing”
does not mean “authorized for execution.”
