# Fictional plan: documentation search

**Objective:** make an approved manual searchable by topic. **Status:** proposed;
no task, benchmark, job or session was actually run.

1. Obtain the permitted manual revision and an owner-approved, held-aside list
   of representative queries and relevance judgments. Record versions and
   selection method. This is a prerequisite for all comparisons.
2. Research a simple keyword baseline and one justified alternative using
   primary documentation or literature. Record source dates, applicability,
   privacy implications, and reasons for rejection. If sources are unavailable,
   mark the research incomplete rather than inventing evidence.
3. In an isolated output directory, a bounded worker builds and tests the
   simplest baseline. A separate worker may prepare judgments only if artifact
   ownership and independence are clear.
4. **Illustrative gate:** for each approved query, report whether at least one
   judged relevant result appears in the first five results, plus the total,
   failures, and reproducibility information. The owner must set any numeric
   threshold before evaluation; this example specifies none.
5. Freeze candidate version and hand off to an independent validator. If the
   gate fails, retain failures and decide the smallest justified revision.
   Request owner approval before publishing or sharing documents externally.

**Dependencies:** approved manual → judgments and baseline → validation →
publication decision. **Budget and stop:** owner sets resource limits before
activation; stop on missing data, changed scope, or unauthorized disclosure.
Use [the master plan template](../../templates/master-plan.md) and
[worker contract](../../templates/worker-contract.md) for a real plan.

The [fictional continuation](sample-contract.md) assumes these missing inputs
and decisions have been resolved. It supplies an illustrative owner-selected
threshold and bounded approval, not a result or permission for actual work.
