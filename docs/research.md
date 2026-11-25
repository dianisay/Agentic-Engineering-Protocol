# Research and state of the art

Plans should include a focused research phase appropriate to the actual
problem. Start from the simplest credible end-to-end baseline, identify a
specific unresolved question, search original papers, standards, official
documentation, and reproducible implementations where available, and compare
their conditions with the current task. Record source title, authors or
organization, publication/version date, link, claim, method, evaluation
scope, limitations, license, and what was actually verified. Distinguish an
abstract, an implementation, and independently replicated results.

Choose the smallest decisive experiment or analysis after checking existing
compatible evidence. Record alternatives, negative results, counterevidence,
cost, uncertainty, and a reasoned selection. Do not infer universal superiority
from a benchmark, benchmark aggregate, or a single source. If browsing or
source access is unavailable, state that and use supplied sources; do not
invent citations. Review the literature again when requirements or evidence
materially change, not simply because a newer explanation sounds persuasive.

## Starting points for orchestration design

These are pointers, not claims that a configuration is optimal for your task.
Verify currency, terms, and relevance before relying on them.

| Source | Why useful | Limits |
|---|---|---|
| [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793), 2024 | Studies how agent-computer interface design affects software-engineering tasks. | Benchmark and tooling-specific; not proof for every workflow. |
| [Improving Factuality and Reasoning in Language Models through Multiagent Debate](https://arxiv.org/abs/2305.14325), 2023 | A research example of independent challenge and debate. | Does not establish that extra critics always improve accuracy or cost. |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), 2023, with later updates | Voluntary risk-management and evaluation framing. | Not a certification or proof of compliance for this protocol. |
| [Google SRE: Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/), 2016 | Actionable, low-noise monitoring as an analogy for event-driven coordination. | Service monitoring differs from research and agent workflows. |
| [Custom agents in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-agents) | Current host documentation for `.agent.md` definitions and tool configuration. | Host-specific and subject to change; other hosts differ. |
| [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents), 2024 | Practitioner discussion of simpler workflows and tradeoffs. | Vendor guidance; the page itself notes tooling changes since publication. |

No automatic bibliography updater or literature search is bundled. An
orchestrator should delegate focused research to a Planner or qualified worker
when the decision merits it and record access dates and source versions in
the project plan.
