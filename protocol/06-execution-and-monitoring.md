# 06 — Execution and deterministic monitoring

## Purpose

Execute the effective [contract](04-session-activation.md), observe progress without
model-driven polling, and enforce resource and safety limits. Use execution,
checkpoint, budget, and event records from [templates](../templates/).

## Before work starts

Record the active contract revision, baseline versions, owner, dependencies,
approval references, budgets, and current consumption. Define:

- Observable events and state transitions.
- Resource ceilings, warning thresholds, measurement sources and freshness.
- Heartbeat or liveness expectations only where an actual mechanism exists.
- Deadlines, maximum retries, retry backoff, and escalation destinations.
- The permitted response to each event and the preauthorized safe-stop procedure.
- Who operates monitoring and what happens if monitoring or accounting fails.

If hard budget enforcement is needed but unavailable, use smaller bounded units
with conservative reservations and human checkpoints, or block execution. A
promised future measurement is not a resource ceiling.

## Execution states

Track contract revisions and attempts separately from the work item's outcome:

| State | Meaning and permitted transition |
| --- | --- |
| `READY` | Activation gates passed; execution may enter `RUNNING`. |
| `RUNNING` | Work is within its current authority and budget; may checkpoint, pause, fail, or become `AWAITING_VALIDATION`. |
| `BLOCKED` | A prerequisite is absent; record the blocker and owner. Resume only after the prerequisite and authority are rechecked. |
| `PAUSED` | Work has deliberately stopped at a checkpoint; resumption requires a recorded decision and valid bounds. |
| `AWAITING_VALIDATION` | A versioned candidate and execution evidence are available; no completion claim yet. |
| `FAILED` | An attempt failed; preserve evidence. A permitted retry is a new attempt, not an erased failure. |
| `STOP_REQUESTED` | A permitted stop was issued; actual quiescence has not necessarily been verified. |
| `STOPPED` | Quiescence is verified within a stated scope; unresolved external effects remain explicit. |

Transitions must record time, actor, reason, contract revision, artifact versions,
and evidence. These execution states are not evidence labels. Acceptance and
terminal disposition follow [07](07-validation.md) and [08](08-handoff-and-closure.md).

## Monitoring without LLM polling

Use the first available authorized mechanism:

1. Event subscriptions or completion notifications feeding deterministic handlers.
2. A non-model watcher or scheduled observer checking explicit state, counters,
   deadlines, or artifact versions at a recorded interval and finite lifetime.
3. Human-operated checkpoints with a written observation schedule and conditions
   under which execution must pause until the next check.

Do not keep a model session awake to repeatedly ask for status, inspect unchanged
output, sleep and retry, or read an agent until it finishes. If all observation
mechanisms are unavailable, checkpoint and wait for a human or an actual event;
do not manufacture a monitoring loop.

A watcher has a named owner, bounded lifetime, minimum necessary access,
deduplication keys, and an explicit cleanup condition. It observes facts and
performs only preauthorized deterministic responses. It cannot grant approval,
reinterpret an objective, transfer ownership, or restart arbitrary workers.
Verify that monitoring is actually operating before relying on it.

## Event-response policy

Define concrete thresholds in the contract; the following is the policy shape,
not a set of assumed numeric defaults:

| Event | Deterministic response |
| --- | --- |
| Successful process exit or output arrival | Record evidence and versions; queue validation, not automatic acceptance. |
| Failure | Preserve failure details and partial effects; apply only the bounded authorized retry policy. |
| Warning threshold | Record consumption and notify once per threshold crossing; do not extend the budget. |
| Hard ceiling, approval expiry/revocation, or lost safeguard | Prevent new affected actions and enter the preauthorized pause/safe-stop path. |
| Missing heartbeat or stale observation | Mark liveness unknown, investigate through the observer or human; do not assume failure or launch a duplicate writer. |
| Ownership collision or unexpected baseline change | Block contested writes and escalate to the coordinator. |
| New substantive evidence or a decision requiring judgment | Deliver a bounded evidence packet for a decision; a model may reason about that event, not poll for the next one. |

Use hysteresis, deduplication, or bounded retry intervals where needed to prevent
alert storms. Record failed delivery and route to the agreed fallback. A monitor's
failure cannot silently disable a required safety gate.

## Budgets, retries, and checkpoints

- Account for setup, execution, failed attempts, monitoring, validation, and recovery
  against aggregate limits. Record concurrent reservations to avoid oversubscription.
- Before a new attempt or expensive action, check remaining allowance and approval
  scope. Retries require a hypothesis or recorded transient condition and a finite
  cap; repeating unchanged failures indefinitely is prohibited.
- Where accounting is delayed, reserve a conservative upper bound for in-flight
  work. If consumption cannot be bounded safely, pause before further commitments.
- Checkpoint at meaningful boundaries and before risky transitions: current
  versions, completed steps, open actions, evidence, failures, consumption, owner,
  and exact next safe step. A checkpoint is not permission to resume.
- Changes to the plan or authority follow [04](04-session-activation.md); dependency
  deltas follow [05](05-inter-agent-communication.md).

## Efficiency measurements

Optimize bounded objectives, relevant evidence retrieval, delta updates, and
event-driven observation before shortening essential context. Report actual model
input/output and cached-token counts only when the accounting source supplies
them, with provider-specific semantics, observation window, and missing usage.
Message counts, bytes, elapsed time, model invocations, and estimated tokens are
proxies; label them as such. Never present proxy reductions as measured token or
cost savings. Include the quality and validation outcome in efficiency comparisons.

## Exit gate

Submit the exact candidate and evidence to [07 — Validation](07-validation.md).
If blocked, failed, cancelled, or unsafe to continue, preserve state and follow
[08 — Handoff and closure](08-handoff-and-closure.md), without asserting completion.
