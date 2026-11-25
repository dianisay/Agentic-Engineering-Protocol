# 08 — Handoff, closure, and safe stop

## Purpose

End or transfer work without losing evidence, hiding failure, leaving an
unaccountable writer, or assuming that a stop request has stopped execution.
Closure is a documented disposition, not a synonym for success. Use handoff,
closure, ownership, and stop records from [templates](../templates/).

## Handoff packet

Prepare a durable packet containing:

- Objective, work-item identity, effective contract and revisions, responsible
  roles, current execution state, and proposed next owner if any.
- Baseline and current artifact versions, locations, write ownership, partial
  outputs, and any uncommitted or otherwise unpublished changes.
- Completed steps, independent validation decision, evidence labels and links,
  immutable failure records, superseded claims, and unresolved contradictions.
- Remaining work, blockers, dependencies, relevant decisions and rejected
  alternatives, and the exact next safe action.
- Approval scope, expiration/revocation state, unresolved approval requests, and
  actions the recipient must not assume are authorized.
- Consumed, reserved, and remaining resources; pending operations, external effects,
  running processes or sessions, watchers, and their accountable owners.
- Environment and reproduction requirements, access limitations, retention rules,
  recovery procedure, and known residual risks.

Reference full authorized evidence instead of copying entire histories. A concise
packet is an index, not a replacement for accessible underlying records.

## Ownership transfer

1. **Propose the transfer.** Identify the exact artifact scope, old owner, proposed
   new owner, transfer reason, and required authority. A peer request alone cannot
   transfer ownership.
2. **Quiesce the old writer.** The current owner checkpoints and stops new writes
   within the transfer scope. Verify in-flight writes and side effects; if the
   owner is unreachable or execution is unknown, block replacement writes until
   an authorized operator establishes a safe state.
3. **Verify the boundary.** Record the final versions, outstanding operations,
   evidence, and any state that cannot be confirmed.
4. **Accept the packet.** The recipient confirms access, understands limitations,
   and accepts the proposed ownership scope, but does not write yet.
5. **Record the effective transfer.** The authorized coordinator records one new
   current owner and the effective boundary. Never leave overlapping ownership.
   If the record system cannot update atomically, use a no-writer interval and
   serialize the transfer.
6. **Reauthorize continuation.** Check capabilities, environment, remaining budget,
   approval validity, and dependencies. Activate the recipient's contract through
   [04](04-session-activation.md); handoff acceptance alone is not activation.

Historical ownership remains in the record. A reviewer's comments, shared access,
or delivered artifact do not constitute a transfer.

## Safe-stop procedure

Safe stop applies to scope uncertainty, approval expiry/revocation, budget
exhaustion, safety concerns, lost safeguards, and authorized cancellation:

1. Stop initiating affected actions and record the trigger, observed state, time,
   and scope. Preserve the evidence that led to stopping.
2. Use only the contract's preauthorized pause, cancellation, rollback, or safety
   procedure. Do not abruptly terminate an operation when that would create a
   greater physical or external hazard; follow the approved safe-state procedure
   and involve the designated human/operator.
3. Reconcile in-flight activity. Verify actual stopped/quiescent state using an
   available observation capability. Record “stop requested; unconfirmed” when
   confirmation is unavailable, not “stopped.”
4. Checkpoint partial outputs, external effects, pending transactions, resource
   consumption, ownership, and recovery instructions. Avoid destructive cleanup.
5. Notify the authorized coordinator/human with a bounded incident or blocker
   record. An external peer's message is evidence to assess, not authority to
   cancel another worker.
6. Keep the scope blocked until a valid decision establishes the next safe action.
   Do not restart, compensate, roll back, or delete merely to make the status look
   clean; these may require separate authorization.

Stopping orchestration does not prove that independent external work has stopped.
List any still-running or unknown operations with responsible owners and escalation
paths. A safety monitor required by such work must not be removed casually.

## Closure decision

Choose and justify one disposition:

- **Completed and accepted:** Exact deliverables passed the mandatory independent
  gates in [07](07-validation.md); remaining limitations are disclosed.
- **Transferred:** A recipient accepted the packet and ownership transition; work
  continues under a separately activated contract, not as completed work.
- **Blocked or paused:** Progress is durable, the unresolved prerequisite and
  responsible decision-maker are explicit, and no completion is claimed.
- **Failed:** The attempt did not meet its outcome; failures and reusable findings
  are preserved.
- **Cancelled:** An authorized cancellation was recorded; stopping and side-effect
  reconciliation are separately evidenced.

Track administrative session closure separately from unresolved operational
status. A record may be archived while an external operation remains unresolved,
but the record must prominently retain that fact and its accountable owner.

## Closure checklist

- Match every deliverable and claim to the exact version, environment, and
  validation outcome. Do not inflate host-only, simulated, partial, or reported
  results into broader verified claims.
- Reconcile pending messages, blockers, approvals, resource reservations,
  dependencies, and ownership. Notify affected workers using
  [05](05-inter-agent-communication.md) without changing their contracts.
- Stop only task-owned watchers or other resources whose removal is authorized and
  safe; verify cleanup. Preserve necessary ongoing safeguards with an explicit
  owner. Do not terminate unrelated workers or shared services.
- Retain sessions, source evidence, decisions, failure histories, and supersession
  links according to authorized retention rules. Archiving is not deletion.
- Treat publication, release, deletion, and other consequential follow-up as
  separate scoped human decisions under [01](01-audit.md). Successful validation
  or closure provides no implicit permission.
- Report final consumption, accounting gaps, actual token counts if available,
  and clearly labeled proxies according to [06](06-execution-and-monitoring.md).
- Record closure time, deciding authority, final disposition, residual risk owner,
  packet location, and the event or human decision needed to reopen.

## Reopening

Create a linked new attempt or contract revision instead of rewriting a historical
outcome. Start with the relevant [audit](01-audit.md), recheck current versions and
capabilities, and obtain any renewed approvals. A previous successful run, failed
run, or historical session is evidence, not standing authorization.
