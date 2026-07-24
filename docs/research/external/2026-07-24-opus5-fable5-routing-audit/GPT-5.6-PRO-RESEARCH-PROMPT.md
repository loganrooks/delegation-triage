# Research prompt: auditable Fable 5 / Opus 5 routing table

Conduct a decision-grade investigation of **when to use Claude Fable 5 versus Claude Opus 5, at which effort level, in which harness, and with which worker models**. Execute the research now; do not return only a plan.

The output must be **audit-ready**. Every load-bearing factual or quantitative claim must have an inline citation to the most direct source available:

- PDFs: exact page plus table/figure/section, with a stable link.
- Web documentation: exact page title, section heading, and access date.
- Repositories: commit, file, line, issue, or PR.
- Practitioner reports: direct post/thread plus date and configuration.
- Calculations: show source values, formula, units, and rounding.
- Do not place unsupported claims beside a generic bibliography. A source list is not a substitute for claim-level grounding.

Create a **claim ledger** containing: claim ID, epistemic status, direct support, contrary evidence, source role, scope conditions, confidence basis, calculation, and revision trigger. Create a **source inventory** qualifying each source as vendor, independent evaluation, implementation artifact, practitioner report, or community signal, and note incentives, dependence, version, date, and access limits. Preserve failed searches and missing evidence. Distinguish verified fact, source report, synthesis, inference, recommendation, speculation, and unknown.

Treat orchestration as a taxonomy, not one capability. Distinguish:

- solo execution where agents would add overhead;
- bounded search/research fan-out;
- fixed peer teams;
- blocking lead–subagent workflows;
- asynchronous lead with long-lived workers;
- dynamic decomposition and replanning;
- implementation orchestration across repository areas;
- debugging with competing hypotheses;
- writer–verifier or implementer–reviewer workflows;
- sequential tool/API automation;
- days-scale project management;
- homogeneous versus mixed-model teams.

For each task family, analyze **Low, Medium, High, XHigh, and Max** where evidence exists. Do not assume higher effort is better. Reconstruct and graph effort-performance curves with exact source references; identify plateaus, regressions, uncertainty, and missing cells. Distinguish **lead effort from worker effort**.

Produce:

1. Best current answer first.
2. A detailed routing table with task subtype, coupling, decomposition difficulty, time horizon, context topology, solo/team choice, controller model and effort, worker model and effort, harness, concurrency cap, alternative route, downshift/escalation triggers, verification policy, cost/latency implications, failure modes, evidence strength, and revision trigger.
3. Separate performance profiles for Opus 5 and Fable 5.
4. A direct analysis of the Opus 4.8 async-orchestration failure and whether Opus 5 truly delegates better or merely benefits from being a stronger worker/integrator.
5. Mixed policies such as Fable controller + Opus Medium implementers and Opus High controller + lower-cost scouts.
6. A controlled local evaluation that isolates controller quality by holding tasks, workers, prompts, tools, budgets, concurrency, and verification constant.
7. Downloadable artifacts: report, claim ledger, source inventory, chart data, and copies or stable links to load-bearing sources.

Read load-bearing sources beyond snippets. Seek negative and contradictory evidence. Do not generalize benchmark results beyond their model–effort–harness–task conditions. Flag vendor-only conclusions. If independent evidence is too immature, say so and design the test that would resolve the uncertainty.
