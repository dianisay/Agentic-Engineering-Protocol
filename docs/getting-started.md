# Getting started

If you have no checkout yet, use the
[copy-paste bootstrap prompt](../README.md#copy-paste-this-prompt-to-get-started)
or [setup and verification](../README.md#setup-and-verification) first.

1. **Establish authority.** Name the approved workspace and output directory,
   access restrictions, protected artifacts, approval boundaries, compute and
   time limits. Do not assume that a working directory is safe to modify.
2. **Choose a host.** List the session and file capabilities actually
   available through its supported interface; note scope, permissions,
   persistence, and whether notifications exist. Failure or missing access is
   unknown, not an empty inventory.
3. **Run an audit.** Select the Auditor role or provide
   [its instructions](../.github/agents/auditor.agent.md) in a chat. Complete
   [the audit template](../templates/audit-report.md) following
   [the audit protocol](../protocol/01-audit.md). Include abandoned or
   apparently irrelevant sessions without deleting them.
4. **Approve a plan.** Use the Planner and
   [master plan template](../templates/master-plan.md). Select priorities from
   the owner's goals and evidence; research alternatives and specify testable
   gates before new results. Preserve decisions and their rationale.
5. **Route and activate.** Use [routing](../protocol/03-session-routing.md)
   and [worker contracts](../templates/worker-contract.md). A new session
   needs a reason; the same session can continue a coherent scope with adequate
   context. Manual relays are an honest fallback, not an automatic session.
6. **Coordinate and verify.** Workers may contact relevant peers directly.
   Run a temporary Critic when independence adds value; run a Validator only
   when an artifact is stable. Preserve decision evidence and failures.

Suggested prompt:

> In `<WORKSPACE_ROOT>`, audit the projects and sessions I have authorized.
> Write planning outputs only under `<OUTPUT_DIRECTORY>`. Identify what the
> host can actually list, inspect, message, or create; preserve existing
> artifacts and report inaccessible evidence. Do not start workers or perform
> consequential actions until I approve a plan.

Replace placeholders with actual authorized values. Do not send sensitive
paths or content to third parties without consent. The
[sample](../examples/sample-project/README.md) shows a completed fictional
audit and plan.

## Configure roles and session capabilities

The five role files deliberately omit a `tools` list: supported tool names and
permissions depend on the host. **Omitting this list does not make an agent
read-only**; it may inherit tools available to the host. Instructions alone
are not an access-control boundary.

For a compatible VS Code installation, open this repository as a workspace and
select a discovered custom agent using the supported agent interface. Follow
the [official custom-agent documentation](https://code.visualstudio.com/docs/agent-customization/custom-agents)
to configure the tools available for that host, using its current documented
names or editor suggestions rather than assumed aliases. Check whether the
target project is accessible within the approved workspace and scope. For a
different host, follow its corresponding supported setup or provide the role
instructions manually.

Before using a role, verify effective tool access and the permitted resources:

- Give the Auditor, Planner, and temporary Critic only authorized read access;
  for the Critic, also verify that writes and side effects are unavailable.
- Give a Validator read access and only explicitly authorized, nondestructive,
  isolated test capabilities. Give an Orchestrator or worker only the
  capabilities needed for the approved contract.
- Check separately whether the host can list or inspect sessions, deliver
  messages, and create sessions. Record successful checks, permissions, and
  limitations in the routing plan; selecting an agent does not establish these
  capabilities or delivery guarantees.
- If the host cannot enforce the necessary boundary, use a suitably isolated
  environment or an authorized human/manual reviewer instead. Do not present
  behavioral instructions as enforced permissions.
