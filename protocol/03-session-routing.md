# 03 — Session capabilities and routing

## Purpose

Match planned work to an actually available execution context without assuming
session management, parallelism, isolation, messaging, or persistence features.
Routing selects a destination; [04](04-session-activation.md) grants the bounded
worker contract. Use routing and capability records from [templates](../templates/).

## Capability inventory

For the current operating environment, record the following logical capabilities:

| Capability | Questions to establish |
| --- | --- |
| Session identity and discovery | Can contexts be identified reliably, inspected within permission, and distinguished from historical records? |
| Lifecycle | Can a context be created, resumed, paused, cancelled, or closed? Which operations actually affect running work? |
| Execution and isolation | What actions can it perform, where can it write, and what isolation or access limits are enforceable? |
| Durable state and evidence | What survives interruption? Can evidence and approval references be retrieved in full? |
| Communication | Are direct messages supported? Are delivery, acknowledgement, ordering, and sender identity observable? |
| Events and scheduling | Can completion or threshold events trigger bounded monitoring without model polling? |
| Resource accounting | Which time, cost, usage, or external-effect measurements are real, delayed, estimated, or unavailable? |
| Validation separation | Can another context or human independently review the exact output version? |
| Human control | How are approvals authenticated, blockers escalated, and revocations delivered? |

Record each capability's scope, permissions, limits, evidence label, observation
time, and fallback. Existence of a documented feature is not confirmation that the
current account or context can use it. If needed, use a harmless, authorized probe
with a stated expected result; do not test lifecycle operations on active workers
or trigger consequential effects merely to discover support.

## Routing procedure

1. Read the work item's capabilities, acceptance criteria, budget, prerequisites,
   and approval requirements from [02](02-portfolio-planning.md).
2. Compare candidate contexts on verified capability fit, access, available
   capacity, relevant retained context, independence needs, and coordination cost.
   Do not route solely by a role name or a worker's self-described expertise.
3. Inspect the chosen destination's current assignment and write ownership without
   changing it. An apparently idle context may still own pending work. Unknown
   state is not permission to repurpose it.
4. Choose one of the routes below and record the reason, rejected alternatives,
   relevant capability evidence, destination identity, and unresolved limitations.
5. Ensure required isolation, authority enforcement, durable evidence, and
   validation can be achieved. If a necessary safeguard is unavailable, block the
   route rather than approximating it silently.
6. Forward the route and work item for explicit contract activation under [04](04-session-activation.md).

## Route choices

- **Existing context, same objective:** Reuse only when retained context is useful,
  its current assignment is compatible, the owner accepts the amendment, and
  approval remains valid. Do not interrupt or redirect an active worker merely
  because it is discoverable.
- **New bounded context:** Prefer this for an independent objective or when context
  contamination would impair judgment. Creation requires an available and
  authorized lifecycle capability; a requested role is not a fabricated session.
- **Sequential execution in the current context:** Use when separation is not
  essential and parallel contexts are unavailable or unnecessary. Maintain
  distinct work-item records and complete one ownership boundary before another.
- **Human-mediated execution:** A human carries the same contract, messages,
  artifacts, and evidence between available contexts. Preserve sender identity
  and provenance; transcription is not a fresh approval.
- **Blocked:** Use when the outcome requires capabilities, permissions, independence,
  or safeguards that cannot currently be provided.

## Fallback ladder

Degrade convenience, not safety or evidence requirements:

1. Use supported direct lifecycle, messaging, and event capabilities where verified.
2. If direct messaging is unavailable, exchange durable addressed records using an
   authorized shared location or human relay, following [05](05-inter-agent-communication.md).
3. If parallel execution is unavailable, serialize independent work. Recalculate
   deadlines, dependencies, and budgets; obtain renewed approval where required.
4. If event monitoring is unavailable, use deterministic scheduled observation
   where supported, or agreed human checkpoints under [06](06-execution-and-monitoring.md).
5. If persistent execution is unavailable, use short bounded units with durable
   checkpoints and a human-operated continuation.
6. If isolation or independent validation is mandatory but unavailable, stop the
   affected route until a suitable environment or independent human is available.

The same templates and gates apply to manual and automated routes. Do not invent
commands, claim delivery without evidence, replace a missing capability with
unapproved access, or simulate independent validation by renaming the same worker.

## Retry and continuity

Before rerouting a failed or disconnected attempt, establish whether it still
runs and whether it has produced partial side effects. Preserve its identity,
contract, failure evidence, and owned artifacts. Do not launch a duplicate writer
while its status or ownership is unresolved.

If a replacement is necessary, follow the explicit ownership handoff in
[08](08-handoff-and-closure.md). Revalidate capability assumptions, remaining
budget, approvals, and baseline versions; routing an old contract to a new
environment is not automatically safe.

## Exit gate

The route names a real destination, demonstrates required capabilities or explicit
manual substitutes, preserves existing workers, and identifies the contract and
validation path. Otherwise return a bounded blocker to planning.
