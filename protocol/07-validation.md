# 07 — Independent validation and gates

## Purpose

Determine whether the exact delivered outcome satisfies its contract, with
independence proportional to risk and evidence sufficient to reproduce or inspect
the decision. Worker self-checks are useful inputs, not independent acceptance.
Use the [validation report](../templates/validation-report.md) for gate results
and the [evidence manifest](../templates/evidence-manifest.md) for claim evidence.

## Validation boundary and independence

The validator must not be the author of the candidate being accepted. Use an
independent worker context or qualified human with no write ownership of that
candidate. A renamed role in the same producing context does not create
independence. Disclose shared assumptions, evidence sources, or other limitations
that could produce correlated errors.

The validator needs access to the contract, acceptance criteria, full authorized
evidence, baseline, exact candidate versions, relevant failures, and required
approvals. Its contract normally permits reading and bounded checks, not editing
the candidate or performing release. Validation that itself incurs consequential
cost or effects requires the same scoped approval rules as execution.

If adequate independence or evidence access is unavailable, record validation as
blocked and use an independent human or another suitable route under
[03](03-session-routing.md). Do not relax the gate silently.

## Validation procedure

1. **Freeze the candidate reference.** Record content versions or digests and the
   applicable environment. Prevent untracked mutation during checking; if this
   cannot be enforced, verify versions before and after each relevant check.
2. **Reconstruct the obligation.** Map each acceptance criterion and authority
   constraint to evidence and a validation method. Confirm that criteria have not
   been weakened after observing an unfavorable result.
3. **Inspect provenance.** Verify that observations correspond to the candidate,
   baseline, input, and environment claimed. Check original results, failure
   records, and supersession links rather than relying solely on summaries.
4. **Run proportionate checks.** Start with focused checks covering the change;
   include integration or regression checks where dependencies or risk justify
   them. Use existing applicable methods where available. Record commands or
   procedures actually used, inputs, expected/observed results, duration, and exit
   status when meaningful. Do not invent checks or assume unavailable tooling.
5. **Challenge the result.** Test relevant edge cases, failure behavior, boundary
   conditions, and alternative explanations. Verify baseline comparisons under
   matched conditions and distinguish correlation from causal evidence.
6. **Inspect constraints.** Check artifact ownership, scope, approvals, resource
   ceilings, information handling, licensing, and any external effects.
7. **Record findings.** For each criterion, give a gate result, evidence label from
   [01](01-audit.md), evidence links, limitations, severity, and remediation owner.
8. **Issue the decision.** State exactly what is accepted, rejected, or blocked,
   for which versions and environment, and which actions remain unauthorized.

## Gate results

Gate results are separate from evidence labels:

- **PASS:** The criterion is met with the required evidence in the stated scope.
- **FAIL:** Evidence establishes that the criterion is not met.
- **BLOCKED:** A required check cannot be completed or necessary evidence is missing.
- **NOT APPLICABLE:** The criterion does not apply, with a recorded justification
  accepted by the authority responsible for that criterion.

`SUPPORTED`, `SELF-REPORTED`, `CONFLICTING`, and `UNVERIFIED` do not satisfy a
criterion that requires `CONFIRMED` evidence. A successful check in a different
environment is not a target-environment pass. A failure confidently observed is
still `FAIL`.

## Required gates

| Gate | Required decision |
| --- | --- |
| Scope and ownership | Were changes confined to the contract and rightful write owner? |
| Correctness and usefulness | Does the outcome satisfy the actual acceptance criteria, not merely produce an artifact? |
| Reproducibility and provenance | Can the claim be inspected or reproduced with stated versions, inputs, and limitations? |
| Regression and compatibility | Is relevant existing behavior preserved, or are approved changes explicit? |
| Authority and consequences | Were required approvals valid, and are external effects, costs, and safeguards reconciled? |
| Operational readiness | Are limitations, recovery, monitoring, and handoff adequate for the intended next use? |

Additional domain-specific gates may be added by the human or approved plan; this
generic protocol does not assume a particular technical domain.

Passing validation does not authorize release, publication, deletion, architecture
adoption, further expensive computation, or physical action. Those remain separate
human-authorized gates. An authorized human may explicitly narrow the intended
outcome or accept a documented residual risk where policy permits; retain the
original failed/blocked gate and create a scoped decision. Do not relabel an
unperformed check as passed or waive non-waivable safeguards.

## Remediation and revalidation

Return actionable findings to the candidate's owner through
[05](05-inter-agent-communication.md). The validator does not fix the candidate
while claiming independent acceptance of its own fix. If a validator becomes an
implementer, another independent validator is required for the affected output.

Each revision creates a new candidate reference. Preserve original failures,
link fixes to findings, rerun affected checks and necessary regressions, and
reconcile stale approvals or environment changes. Reuse unchanged evidence only
with a documented relevance argument; do not carry a pass forward automatically.

## Exit gate

Proceed to [08 — Handoff and closure](08-handoff-and-closure.md) with a versioned
validation decision. Accepted completion requires all mandatory gates to pass or
be legitimately not applicable. Otherwise the outcome remains failed, incomplete,
or blocked, with explicit remediation or safe-stop disposition.
