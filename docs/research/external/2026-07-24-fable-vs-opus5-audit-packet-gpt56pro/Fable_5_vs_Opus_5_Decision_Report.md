# Fable 5 versus Opus 5: decision-grade routing by effort, harness, and worker mix

**Version:** 1.0 audit edition  
**Evidence cutoff:** 24 July 2026  
**Executing model:** GPT-5.6 Pro  
**Primary mode:** research + decision support + audit + local operational evaluation  
**Decision unit:** model × effort × harness × worker pool × task family × verification policy  

> **Scope note.** This report uses the evidence located in this pass; it is not presented as an exhaustive search. It distinguishes vendor-reported results, verified implementation facts, practitioner evaluations, inference, recommendation, speculation, and unknown. The AHR-C 2.0 requirements for claim tracing, configuration-level attribution, negative evidence, and verified artifacts govern the method [AHR-C §§3.1-3.5, 6.1-6.10, 11.1-11.13, 12.4, 13.3].

> **Important deployment distinction.** Several Fable-system-card capability figures are reported for a “Fable/Mythos 5” card configuration or the underlying core model. Deployed Fable adds classifier/fallback behavior. The report therefore does not silently treat every core-model figure as the complete served Fable product.

# 1. Best current answer

**Recommendation:** make **Opus 5** the default solo model and default bounded controller. Route to **Fable 5** only when the hard part is sustained organization rather than merely difficult execution: persistent asynchronous workers, changing decomposition, repeated inter-agent communication, multi-day state, or integration across a moving work graph. Start Fable at **High**, not Max; use **XHigh** when the controller repeatedly has to replan, reconcile conflicts, or recover failed work. Use Opus workers at **Medium** for contained implementation and Sonnet/cheaper workers for breadth. Treat every Max route as a locally tested exception.

That recommendation is stronger than “Fable is the manager, Opus is the worker,” because the public evidence does **not** isolate Fable-versus-Opus-5 controller quality. Anthropic’s homogeneous-team experiments change lead and worker capability together, while the best manager-isolation benchmark located uses a fixed worker pool but has no Opus 5 row, one reported run, and a Fable fallback condition. The specialized-manager reading is therefore a vendor-supported inference, not a verified general fact. [P-O5, p. 168, §8.11.4 Multi-agent harnesses and methodology](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=168); [P-F5, p. 275, §8.15.3 Multi-agent harnesses](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=275); [R-CLAW, commit 630efd8a0d1dc8189718226c7da158cbe4c2fe64, ClawArena-Team/README.md, lines 8-41](https://github.com/aiming-lab/ClawArena/blob/630efd8a0d1dc8189718226c7da158cbe4c2fe64/ClawArena-Team/README.md).

## 1.1 Default routing policy

| Situation | First route | Worker route | Why | Escalate when |
|---|---|---|---|---|
| Small, tightly coupled, or sequential | Solo Sonnet 5 / Opus 5 Low-Medium / Sol Medium | None | Agent overhead and context duplication are unlikely to repay | hidden coupling or failed verification |
| Contained implementation with clear tests | **Opus 5 Medium solo** | None | Opus peaks at Medium on both FrontierCode Main and Extended in the reported sweep | repeated failed patch, architectural uncertainty |
| Difficult but coherent implementation/debugging | **Opus 5 High**, then XHigh | Optional fresh Opus Medium verifier | High/XHigh improve hard-task reasoning without assuming Max | causal model fails, evidence conflicts |
| Bounded research/search fan-out | **Opus 5 High controller** | Sonnet Low/Medium or Opus Low/Medium scouts | Stable partitions; controller mostly synthesizes | work graph changes or workers require persistent communication |
| Stable implementation across 2-4 repo areas | **Opus 5 High controller** | **Opus 5 Medium implementers** | Separates planning/integration from the reported Medium implementation sweet spot | interface drift or integration defects dominate |
| Persistent async team, dynamic replanning, days-scale project | **Fable 5 High**, then XHigh | Opus Medium implementers; Sonnet High scouts/reviewers | Strongest available vendor evidence for sustained delegation and long-lived workers | Fable premium does not improve verified outcome |
| Cost-sensitive broad work | Opus High or Sol High controller | Sonnet / Terra / Luna workers | Worker volume dominates cost; keep premium reasoning in integration | cheap workers omit important evidence or severe failures rise |
| OpenAI-native homogeneous parallelism | GPT-5.6 Sol High/XHigh with Responses multi-agent beta | Same request model/tools | Strong alternative complete configuration; current built-in multi-agent is homogeneous | mixed workers or mature peer communication are required |

**No-action baseline:** keep the task solo and add deterministic verification. The burden of proof is on the team route. Fable’s card reports a median 0.8× per-problem speedup on the easy BrowseComp bucket—i.e. a slowdown—while harder items benefit. [P-F5, p. 272, difficulty-bucket analysis](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=272).

## 1.2 Effort policy

- **Low:** scouting, narrow transformations, deterministic tool work, and cheap first-pass workers. Do not use Low as the controller for ambiguous high-coupling projects unless a local evaluation validates it.
- **Medium:** the default Opus implementation setting. It is the best reported Opus 5 effort on FrontierCode Main (53.4) and Extended (63.6), exceeding Opus XHigh by 9.8 and 6.7 percentage points respectively in those exact task-harness conditions. [P-O5, p. 151, Figs. 8.4.A-B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=151).
- **High:** default controller effort for bounded orchestration and default Fable pilot effort. It captures most of the Opus BrowseComp gain: 90.2 at High versus 90.7 XHigh and 90.8 Max. [P-O5, p. 160, Fig. 8.10.2.B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=160).
- **XHigh:** use for deep reasoning, difficult root-cause work, dynamic replanning, or long-horizon integration. Both Opus and Fable peak at XHigh on DeepSWE before slight Max regressions. [P-O5, p. 150, Fig. 8.3.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=150).
- **Max:** capability-ceiling or locally proven route, not a default. CursorBench provides contrary evidence where Max is best, but at large cost and with small model gaps; this is precisely why effort must be task-specific. [W-CURSOR, “CursorBench 3.2,” §“leaderboard and methodology,” accessed 24 July 2026](https://cursor.com/cursorbench).

**Lead effort and worker effort are separate decisions.** Claude Code custom subagents can override both model and effort, while agent-team teammates can use specified models but inherit the lead’s effort. Therefore custom subagents or script-backed workflows are the cleanest current harness for mixed policies and controlled tests. [W-CODE-SUBAGENTS, “Create custom subagents,” §“Supported frontmatter fields,” accessed 24 July 2026](https://code.claude.com/docs/en/sub-agents); [W-CODE-MODEL-CONFIG, “Model configuration,” §“Configure effort level,” accessed 24 July 2026](https://code.claude.com/docs/en/model-config); [W-CODE-TEAMS, “Orchestrate teams of Claude Code sessions,” §“Specify teammates and models,” accessed 24 July 2026](https://code.claude.com/docs/en/agent-teams).

## 1.3 Confidence

- **High confidence:** current list prices; exact benchmark values transcribed from official figures; the specific Opus 4.8 async regression; current harness semantics; the absence of a public lead-effort sweep in the cited Opus 5 card.
- **Moderate confidence:** Opus Medium is a strong first setting for bounded implementation; High is a reasonable bounded-controller default; teams help the decomposable hard tail more than easy tasks.
- **Low-to-moderate confidence:** Fable is the better controller for dynamic long-lived teams. Anthropic says so directly, and Fable’s homogeneous async results are strong, but the causal controller comparison is missing.
- **Unknown:** the cost-per-verified-result crossover between Fable and Opus for the user’s workload; the best lead effort for each orchestration family; Fable-versus-Opus with identical Opus/Sonnet/Sol workers.

# 2. What the evidence establishes—and what it does not

## 2.1 Established within the reported conditions

1. **Effort is non-monotonic.** Opus 5 peaks at Medium on the two FrontierCode sets, whereas Opus and Fable peak at XHigh on DeepSWE and then slightly regress at Max. On BrowseComp, Opus nearly plateaus by High and Fable/Mythos by XHigh. [P-O5, p. 151, Figs. 8.4.A-B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=151); [P-O5, p. 150, Fig. 8.3.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=150); [P-O5, p. 160, Fig. 8.10.2.B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=160).
2. **Opus 5 repairs the direction of the Opus 4.8 async BrowseComp result.** Opus 4.8 async is 83.0 versus 84.3 solo (−1.3 pp); Opus 5 async is 93.4 versus 90.5 solo (+2.9 pp from rounded labels; accompanying prose reports +2.8 from unrounded values). [P-O48, p. 210, Fig. 8.11.1.A](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf#page=210); [P-O5, p. 163, Fig. 8.11.1.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=163).
3. **Fable/Mythos gets a larger within-card async uplift.** 93.3 − 88.0 = +5.3 pp, versus Opus’s approximately +2.8/+2.9 pp. This is a descriptive comparison, not a causal manager ranking. [P-F5, p. 270, Fig. 8.15.1.A](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=270); [P-O5, p. 163, Fig. 8.11.1.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=163).
4. **The async endpoints are effectively tied at the displayed precision.** Opus 93.4 and Fable/Mythos 93.3 differ by only 0.1 pp across different cards/configurations. That difference cannot bear a superiority claim.
5. **Easy-task overhead is real.** Fable’s card reports 0.8× median speedup for easy BrowseComp items, 1.6× for hard items, and a 4.4× summed-latency speedup in the hard bucket. [P-F5, p. 272, difficulty-bucket analysis](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=272).
6. **Current list rates strongly favor Opus as the default controller.** Opus is $5/$25 per million input/output tokens versus Fable $10/$50; both ratios are exactly 0.5. Sonnet is cheaper, and GPT-5.6 Sol is $5/$30. [W-A-PRICE, “Pricing,” §“model pricing table,” accessed 24 July 2026](https://platform.claude.com/docs/en/about-claude/pricing); [W-OAI-GPT56, “GPT-5.6: Frontier intelligence that scales with your ambition,” §“Availability and pricing,” accessed 24 July 2026](https://openai.com/index/gpt-5-6/).

## 2.2 Not established

- It is **not established** that Fable delegates better than Opus 5 when both receive identical workers, prompts, tools, budgets, and verification. The vendor cards change the complete homogeneous configuration. [P-O5, p. 168, §8.11.4 Multi-agent harnesses and methodology](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=168); [P-F5, p. 276, §8.15.4 Methodology](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=276).
- It is **not established** that Opus Medium is the best lead effort. Medium’s strong evidence is implementation-specific; the multi-agent runs use an unreleased effort configuration. [P-O5, p. 151, Figs. 8.4.A-B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=151); [P-O5, p. 168, §8.11.4 Multi-agent harnesses and methodology](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=168).
- It is **not established** that Max is best for difficult tasks. Several official curves plateau or regress, while CursorBench has contrary Max wins. The answer is task-and-harness conditioned.
- It is **not established** that a five- or ten-agent benchmark team translates into a production software team. The cards count total tokens and derive critical-path latency under cache assumptions; they do not publish all operational failure distributions. [P-O5, p. 168, §8.11.4 Multi-agent harnesses and methodology](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=168); [P-F5, p. 276, §8.15.4 Methodology](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=276).
- It is **not established** that Sonnet or Sol are weak managers. The evidence located is simply less manager-specific. They remain important price/performance baselines.

# 3. Orchestration is a taxonomy, not one capability

| Orchestration family | Structural question | Preferred first harness | Model implication |
|---|---|---|---|
| Solo execution | Can one coherent context do the work without coordination overhead? | Single agent + deterministic checks | Opus Medium/High; Sonnet/Sol for lower-value work |
| Bounded search/research fan-out | Are source classes independent and known before launch? | Named subagents or script workflow | Opus High controller, cheap scouts |
| Fixed peer team | Do peers need independent full-task views and direct messages? | Agent teams / custom peer harness | Use sparingly; 3-5 peers, stable tasks |
| Blocking lead–subagent | Must the lead wait for each fresh worker? | Supervisor-worker | Usually inferior to async/persistent or solo |
| Async lead with long-lived workers | Will workers receive multiple tasks and feedback over time? | Persistent subagents | Fable High/XHigh is the premium hypothesis |
| Dynamic decomposition/replanning | Is the task graph unknown and changing? | Fable lead + external ledger; script stable stages | Controller quality matters most |
| Repository-area implementation | Are modules genuinely independent with explicit contracts? | Worktrees + named workers + integration lead | Opus High lead, Opus Medium workers |
| Competing-hypothesis debugging | Can independent investigators falsify different causal models? | Blind investigators + decisive rerun | Opus High/XHigh lead |
| Writer–verifier / implementer–reviewer | Can production and checking be separated? | Fresh verifier context + capped repair | Heterogeneous reviewer helps error diversity |
| Sequential tool/API automation | Does every action depend on the previous state? | Single agent + deterministic state machine | Do not parallelize by default |
| Days-scale project management | Are memory, worker lifecycle, and reprioritization persistent? | Async lead + external project ledger | Fable High/XHigh candidate |
| Homogeneous vs mixed team | Is simplicity worth confounding lead and worker quality? | Homogeneous for clean deployment; mixed for economics/causal tests | Separate controller and worker effort where possible |

Claude Code’s official architecture guide explicitly distinguishes subagents, agent view, agent teams, and dynamic workflows. Agent teams are experimental; token costs scale with each context and coordination has diminishing returns. Dynamic workflows externalize intermediate state into a rerunnable script, which makes them preferable to free-form teams for large repeatable audits or migrations. [W-CODE-AGENTS, “Run agents in parallel,” §“Choose an approach,” accessed 24 July 2026](https://code.claude.com/docs/en/agents); [W-CODE-TEAMS, “Orchestrate teams of Claude Code sessions,” §“Agent teams are experimental,” accessed 24 July 2026](https://code.claude.com/docs/en/agent-teams); [W-CODE-TEAMS, “Orchestrate teams of Claude Code sessions,” §“Choose an appropriate team size,” accessed 24 July 2026](https://code.claude.com/docs/en/agent-teams); [W-CODE-WORKFLOWS, “Orchestrate subagents at scale with dynamic workflows,” §“How a workflow runs,” accessed 24 July 2026](https://code.claude.com/docs/en/workflows).

# 4. Reconstructed effort-performance curves

All values below were manually transcribed from exact numeric labels in rendered official figures and cross-checked against extracted PDF text. They are reported scores, not recomputed benchmark runs. The CSV preserves every point, source page, figure, and harness note: `data/effort_curves.csv`.

![Figure 1. FrontierCode Main: Opus 5 peaks sharply at Medium; Fable peaks at XHigh and regresses at Max.](../charts/effort_frontiercode_main.png)

*Figure 1. FrontierCode Main: Opus 5 peaks sharply at Medium; Fable peaks at XHigh and regresses at Max. Source: [P-O5, p. 151, Figs. 8.4.A-B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=151).*

![Figure 2. FrontierCode Extended: the same Opus Medium peak appears; Fable peaks at XHigh.](../charts/effort_frontiercode_extended.png)

*Figure 2. FrontierCode Extended: the same Opus Medium peak appears; Fable peaks at XHigh. Source: [P-O5, p. 151, Figs. 8.4.A-B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=151).*

![Figure 3. DeepSWE v1.1: both Opus and Fable peak at XHigh, then slightly regress at Max.](../charts/effort_deepswe.png)

*Figure 3. DeepSWE v1.1: both Opus and Fable peak at XHigh, then slightly regress at Max. Source: [P-O5, p. 150, Fig. 8.3.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=150).*

![Figure 4. HLE without tools: Opus nearly plateaus at XHigh; Fable peaks at XHigh then drops.](../charts/effort_hle_no_tools.png)

*Figure 4. HLE without tools: Opus nearly plateaus at XHigh; Fable peaks at XHigh then drops. Source: [P-O5, p. 158, Fig. 8.10.1.B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=158).*

![Figure 5. BrowseComp: Opus captures most of its gain by High; Fable/Mythos plateaus by XHigh.](../charts/effort_browsecomp.png)

*Figure 5. BrowseComp: Opus captures most of its gain by High; Fable/Mythos plateaus by XHigh. Source: [P-O5, p. 160, Fig. 8.10.2.B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=160).*

## 4.1 Plateau and regression audit

| Benchmark / model | Best reported effort | Best score | Plateau or regression | Decision implication |
|---|---:|---:|---|---|
| FrontierCode Main / Opus 5 | Medium | 53.4 | −5.4 pp at High, −9.8 at XHigh, −5.4 at Max | Medium is the first implementation setting to test |
| FrontierCode Extended / Opus 5 | Medium | 63.6 | −5.1 at High, −6.7 at XHigh, −4.7 at Max | Higher effort can actively hurt this harness |
| DeepSWE / Opus 5 | XHigh | 69.7 | Max −0.9 | XHigh before Max |
| DeepSWE / Fable 5 | XHigh | 69.9 | Max −0.2 | Max adds no demonstrated value here |
| HLE / Fable 5 | XHigh | 57.8 | Max −1.3 | XHigh ceiling candidate |
| BrowseComp / Opus 5 | Max | 90.8 | High is only 0.6 lower | High is the economic default absent hard-tail value |
| BrowseComp / Fable/Mythos 5 | XHigh/Max tie | 88.0 | Max +0.0 | Do not pay Max by reflex |

**Interpretation, not mechanism proof:** Opus’s FrontierCode reversal may reflect over-deliberation, plan churn, or task-harness interaction; the public figure does not identify the cause. Anthropic separately warns that Opus 5 already verifies its work and that legacy prompts can cause over-verification. That guidance supports a plausible mechanism but does not prove it caused the benchmark curve. [W-A-OPUS, “Prompting Claude Opus 5,” §“Task scope and over-verification,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5).

## 4.2 Lead effort versus worker effort

The public matrix is mostly missing. Opus 5 has one informative async cell with lower-effort workers: 92.0 versus 90.5 for the 10M solo baseline, while the normal async configuration reaches 93.4. This shows that low-effort workers can be useful, but it does not reveal the lead-effort setting or a full controller × worker interaction. [P-O5, p. 163, Fig. 8.11.1.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=163); [P-O5, p. 168, §8.11.4 Multi-agent harnesses and methodology](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=168).

| Lead effort | Worker effort | Public evidence | Production reading |
|---|---|---|---|
| Unknown prerelease Opus setting | Low | BrowseComp async 92.0 | Cheap workers can add breadth; not enough to set a universal worker effort |
| Unknown prerelease Opus setting | Unknown normal setting | BrowseComp async 93.4 | Strong complete configuration, controller attribution unresolved |
| Fable/Mythos Max | Max | BrowseComp async 93.3; ProgramBench team gains | Capability ceiling, expensive; no lower lead/worker sweep |
| Fable High/XHigh | Opus Medium | No public controlled cell | Recommended experiment, not verified result |
| Opus High | Sonnet/Terra Low-High | No controlled public cell | Recommended breadth experiment |

# 5. Direct analysis of the Opus 4.8 async-orchestration failure

## 5.1 Observation

In the Opus 4.8 BrowseComp figure, the 10M-token solo agent scores 84.3, the asynchronous lead with subagents scores 83.0, the five-agent fixed peer team scores 85.4, and the blocking orchestrator scores 88.5. Therefore the failure was **not “multi-agent cannot help Opus 4.8.”** It was a specific negative result for the flexible async architecture: 83.0 − 84.3 = −1.3 pp. [P-O48, p. 210, Fig. 8.11.1.A](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf#page=210).

The fixed five-agent system used about 20% of the 10M solo latency while scoring higher, and the benefit concentrated in the difficult tail; easy problems did not gain. ProgramBench likewise showed the three-agent team reaching the 60% threshold about 1.8× faster. [P-O48, p. 210, Fig. 8.11.1.A](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf#page=210); [P-O48, p. 211, Figs. 8.11.1.B-C](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf#page=211); [P-O48, p. 213, Fig. 8.11.2.A](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf#page=213).

## 5.2 Plausible mechanisms—none directly proven

1. **Controller decomposition failure.** The async lead may have created poor workstreams, omitted context, or integrated returns weakly.
2. **Controller–worker role confusion.** A strong worker model may continue doing task work instead of preserving a managerial state, leading to duplicate or incoherent exploration.
3. **Fresh-context or communication loss.** Worker prompts may omit relevant global context or the lead may not retain the right worker state.
4. **Search overhead and easy-item dilution.** Async spawning adds coordination cost even where one agent can answer quickly; the difficulty-bucket results support this general possibility.
5. **Noise and benchmark-specific interaction.** No uncertainty interval for the displayed difference is provided, and BrowseComp search is not representative of all implementation orchestration.

The blocking orchestrator’s 88.5 score is important contrary evidence. It suggests that Opus 4.8 could exploit delegated search when the harness supplied stronger synchronization/structure, so the failure cannot be reduced to “weak worker capability.”

## 5.3 What changed with Opus 5

Opus 5 reverses the within-card direction: 90.5 solo, 92.0 async with low-effort workers, 93.4 normal async, 92.7 five-agent, and 93.6 ten-agent. The ten-agent system is reported at 5.9× the solo latency speed and +3.1 pp, while async adds approximately +2.8/+2.9 pp. [P-O5, p. 163, Fig. 8.11.1.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=163); [P-O5, p. 164, Fig. 8.11.1.B and discussion](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=164).

**Strongest warranted conclusion:** Opus 5 no longer shows the same negative async BrowseComp symptom. **Unwarranted conclusion:** Opus 5 is proven to delegate better. The whole homogeneous configuration improved; the lead, workers, integrator, and prerelease effort changed together. The card also says the runs used a prerelease model, an unreleased effort configuration, and no safety classifiers. [P-O5, p. 168, §8.11.4 Multi-agent harnesses and methodology](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=168).

## 5.4 Does Opus 5 delegate better or merely integrate stronger workers?

The available evidence supports three live readings:

- **Better-controller reading:** the positive async delta and low-effort-worker cell indicate improved decomposition and synthesis.
- **Stronger-worker/integrator reading:** Opus 5’s solo baseline is already 90.5, so worker returns and final synthesis may simply be better even if managerial policy is unchanged.
- **Harness-fit reading:** the prerelease effort and updated prompts/scaffold may be responsible for much of the improvement.

A same-worker controller swap is the discriminating test. The local evaluation package is designed exactly for that uncertainty.

![BrowseComp orchestration uplift](../charts/browsecomp_orchestration_uplift.png)

*Figure 6. Within-card changes from each card’s 10M solo baseline. Source values: [P-O48, p. 210, Fig. 8.11.1.A](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf#page=210); [P-F5, p. 270, Fig. 8.15.1.A](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=270); [P-O5, p. 163, Fig. 8.11.1.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=163).*

# 6. Separate performance profiles

## 6.1 Claude Opus 5

**Best use:** economical frontier solo executor, bounded controller, integrator, and recovery model.

**Evidence-backed strengths**

- Strong single-agent baseline and positive multi-agent BrowseComp endpoints. [P-O5, p. 163, Fig. 8.11.1.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=163).
- Sharp Medium sweet spot on FrontierCode Main and Extended. [P-O5, p. 151, Figs. 8.4.A-B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=151).
- XHigh peak on DeepSWE and near-plateau on HLE/BrowseComp, giving a rational escalation ladder. [P-O5, p. 150, Fig. 8.3.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=150); [P-O5, p. 158, Fig. 8.10.1.B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=158); [P-O5, p. 160, Fig. 8.10.2.B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=160).
- Current base token rates are half Fable’s. [W-A-PRICE, “Pricing,” §“model pricing table,” accessed 24 July 2026](https://platform.claude.com/docs/en/about-claude/pricing).

**Risks and controls**

- Anthropic says Opus 5 already verifies its work and can over-verify when prompts add redundant verification. Remove inherited “always double-check with a subagent” scaffolding; verify through acceptance tests rather than recursive self-review. [W-A-OPUS, “Prompting Claude Opus 5,” §“Task scope and over-verification,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5).
- Constrain scope and spawning. Use a deterministic default cap and a delegation threshold based on independence and expected work size.
- Do not infer controller skill from homogeneous teams; log lead work, worker utilization, duplicate tasks, and integration defects.

**Effort profile**

| Effort | Route | Avoid when | Evidence level |
|---|---|---|---|
| Low | Cheap scout, narrow transform, deterministic worker | ambiguity or high integration cost | Low-moderate |
| Medium | Default contained implementation/tool work | dynamic project management | Moderate, task-specific |
| High | Default bounded controller and difficult coherent work | small routine task | Moderate |
| XHigh | Debugging, architecture, replanning, recovery | latency/cost dominates and High is adequate | Moderate for hard-task ceiling; low for lead orchestration |
| Max | Local capability-ceiling exception | default production routing | Contrary evidence substantial |

## 6.2 Claude Fable 5

**Best use:** premium controller for persistent async organization, evolving task graphs, and multithreaded long-horizon work—conditional on operational eligibility and local value.

**Evidence-backed or officially declared strengths**

- Anthropic describes Fable as significantly more dependable at dispatching and sustaining parallel subagents and ongoing communication. This is official vendor guidance, not independent proof. [W-A-FABLE, “Prompting Claude Fable 5,” §“Capability improvements,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5).
- The card’s async BrowseComp configuration gains +5.3 pp over its 10M solo baseline, and fixed teams concentrate speedup in difficult items. [P-F5, p. 270, Fig. 8.15.1.A](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=270); [P-F5, p. 272, difficulty-bucket analysis](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=272).
- Five-agent ProgramBench reaches the 60% threshold 3.2× faster in prose and finishes 7.9 pp above solo. [P-F5, p. 274, Fig. 8.15.2.A](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=274).
- Official guidance emphasizes long turns, autonomous runs, tool-grounded progress, and async long-lived subagents. [W-A-FABLE, “Prompting Claude Fable 5,” §“Longer turns by default,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5); [W-A-FABLE, “Prompting Claude Fable 5,” §“Ground progress claims during long runs,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5); [W-A-FABLE, “Prompting Claude Fable 5,” §“Parallel subagents,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5).

**Risks and controls**

- Long turns and hours-scale runs demand larger timeouts, streaming/progress, external state, and budget limits. [W-A-FABLE, “Prompting Claude Fable 5,” §“Longer turns by default,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5).
- Ground every progress claim in tool evidence; the official guide supplies an explicit instruction because fabricated status is a recognized risk. [W-A-FABLE, “Prompting Claude Fable 5,” §“Ground progress claims during long runs,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5).
- Define action boundaries and operational gates. The same official page documents classifier/fallback behavior; record the actual served model, refusal/fallback, latency, and cost rather than assuming a Fable response.
- Do not use Fable workers by default just because Fable is the controller. Its 2× list rates make mixed teams the economically important test. [W-A-PRICE, “Pricing,” §“model pricing table,” accessed 24 July 2026](https://platform.claude.com/docs/en/about-claude/pricing).

**Effort profile**

| Effort | Route | Avoid when | Evidence level |
|---|---|---|---|
| Low | Routine bounded work only after validation | orchestration is the reason to buy Fable | Low |
| Medium | Routine Fable work where High is too slow | hard dynamic coordination without evidence | Low-moderate |
| High | Default premium-controller pilot | Max-by-default | Moderate vendor guidance |
| XHigh | Dynamic replanning, hardest integration, long-lived team recovery | stable separable work | Moderate for hard-task curves; low for controller causal effect |
| Max | Ceiling experiment | general production controller | Several official regressions/plateaus |

## 6.3 Claude Sonnet 5

Sonnet is the lower-cost Claude worker and baseline. Its official card reports Max BrowseComp 84.7, comparable to Opus 4.8’s 84.3 under the card’s large-budget setting, but its DeepSWE curve remains below Opus/Fable. [P-S5, p. 122, BrowseComp figure/discussion](https://www-cdn.anthropic.com/480e0bb54327b9622282e9c39a83a4f490ed377e/Claude%20Sonnet%205%20System%20Card.pdf#page=122); [P-O5, p. 150, Fig. 8.3.A](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=150).

Use Sonnet for high-volume retrieval, inventory, mechanical implementation, review checklists, and independent breadth. Escalate worker effort to High/XHigh when worker interpretation is load-bearing; otherwise keep controller synthesis on Opus or Fable. Current Anthropic pricing makes Sonnet materially cheaper, but the promotional date must be tracked. [W-A-PRICE, “Pricing,” §“model pricing table,” accessed 24 July 2026](https://platform.claude.com/docs/en/about-claude/pricing).

## 6.4 GPT-5.6 Sol

Sol is a credible solo/controller alternative, especially where OpenAI tools, programmatic tool calling, artifact generation, or a homogeneous one-request multi-agent beta fit the stack. OpenAI currently lists Sol at $5 input / $30 output per million tokens and describes built-in multi-agent as a beta in which subagents share the request model and tools. [W-OAI-GPT56, “GPT-5.6: Frontier intelligence that scales with your ambition,” §“Availability and pricing,” accessed 24 July 2026](https://openai.com/index/gpt-5-6/); [W-OAI-MULTI, “Multi-agent,” §“Overview / How Multi-agent works,” accessed 24 July 2026](https://developers.openai.com/api/docs/guides/responses-multi-agent).

CursorBench 3.2 reports Sol Max 67.2 at $5.69/task versus Opus Max 70.0 at $8.23/task and Fable Max 70.5 at $17.32/task. Formula: $5.69 / $8.23 = 0.6914, so Sol Max costs about 69% of Opus Max in this benchmark while scoring 2.8 pp lower. This is a complete model–harness result on proprietary tasks, not a universal value ranking. [W-CURSOR, “CursorBench 3.2,” §“leaderboard and methodology,” accessed 24 July 2026](https://cursor.com/cursorbench).

OpenAI’s launch page reports strong benchmark and partner results, but those are vendor-curated and use heterogeneous harnesses. Use Sol as a local common-task baseline, not as a conclusion imported from the launch table. [W-OAI-GPT56, “GPT-5.6: Frontier intelligence that scales with your ambition,” §“Availability and pricing,” accessed 24 July 2026](https://openai.com/index/gpt-5-6/).

# 7. Detailed routing table

The machine-readable table is `data/routing_table.csv` and the workbook sheet **Routing Table** preserves every requested field. The cards below reproduce all routing fields in a readable audit form.

## RT-01 — Solo execution: Small deterministic change, narrow transformation, or one-step answer

- **Coupling / decomposition / horizon:** Tightly coupled / atomic / None / Minutes.
- **Context topology:** Single shared context.
- **Solo/team choice:** Solo.
- **Controller:** Sonnet 5 or GPT-5.6 Terra; Opus 5 when failure cost is material at **Low or Medium**.
- **Workers:** None at **n/a**.
- **Harness / concurrency cap:** Single agent with deterministic tools/tests / 0.
- **Alternative route:** Opus 5 Medium solo.
- **Downshift trigger:** Clear acceptance test, low ambiguity, cheap rollback.
- **Escalation trigger:** Hidden coupling, failed test, unresolved requirement.
- **Verification policy:** Machine check or exact diff; no model-only self-approval.
- **Cost/latency:** Team overhead is likely negative; cheapest acceptable solo route.
- **Principal failure modes:** Unnecessary fan-out, context duplication, over-verification.
- **Evidence strength / status:** Moderate; Recommendation from evidence + engineering judgment.
- **Evidence IDs:** P-F5 p272; W-CODE-AGENTS; W-CODE-TEAMS.
- **Revision trigger:** Representative local tasks show team reduces verified latency or severe failures.

## RT-02 — Solo implementation: Contained autonomous patch with clear tests and bounded surface

- **Coupling / decomposition / horizon:** Moderate, local / Low / Tens of minutes to hours.
- **Context topology:** Repository-local, coherent.
- **Solo/team choice:** Solo first.
- **Controller:** Opus 5 at **Medium**.
- **Workers:** None at **n/a**.
- **Harness / concurrency cap:** Claude Code / coding agent with tests / 0.
- **Alternative route:** GPT-5.6 Sol High or Fable High for capability-sensitive tail.
- **Downshift trigger:** Mechanical change and strong tests -> Sonnet 5 High or Sol Medium.
- **Escalation trigger:** Architecture uncertainty, repeated failed patch, repo-wide root cause.
- **Verification policy:** Held-out tests, lint/typecheck, diff review; human review for consequential code.
- **Cost/latency:** Opus Medium is a strong efficiency point; higher effort can regress on FrontierCode.
- **Principal failure modes:** Scope expansion, redesign after a valid plan, redundant checks.
- **Evidence strength / status:** Moderate (vendor figure + independent CursorBench direction); Task-conditioned recommendation.
- **Evidence IDs:** P-O5 p151 Figs 8.4.A-B; W-CURSOR; W-A-OPUS.
- **Revision trigger:** Local patch suite shows High/XHigh higher verified success at acceptable cost.

## RT-03 — Solo implementation: Complex but tightly coupled architecture or debugging

- **Coupling / decomposition / horizon:** High / High but non-parallel / Hours.
- **Context topology:** One evolving causal model.
- **Solo/team choice:** Solo or one fresh verifier, not broad team.
- **Controller:** Opus 5 at **High; XHigh after failure**.
- **Workers:** Optional fresh Opus 5 Medium verifier at **Medium**.
- **Harness / concurrency cap:** Single lead plus bounded verifier / 1.
- **Alternative route:** GPT-5.6 Sol High/XHigh; Fable High if work graph becomes dynamic.
- **Downshift trigger:** Root cause localized and testable.
- **Escalation trigger:** Competing plausible causes or repeated causal-model failure.
- **Verification policy:** Reproduce bug, invariant tests, adversarial regression tests.
- **Cost/latency:** XHigh only when the extra reasoning changes decisions; Max not default.
- **Principal failure modes:** Overthinking, tunnel vision, verifier correlation.
- **Evidence strength / status:** Low-moderate; Inference requiring local validation.
- **Evidence IDs:** P-O5 p150/p158; W-A-OPUS; W-OAI-GUIDANCE.
- **Revision trigger:** Paired debugging trials favor another model-effort combination.

## RT-04 — Bounded research fan-out: Independent source classes, jurisdictions, repositories, or hypotheses

- **Coupling / decomposition / horizon:** Low / Known in advance / Minutes to hours.
- **Context topology:** Isolated worker contexts; one synthesis context.
- **Solo/team choice:** Team.
- **Controller:** Opus 5 at **High**.
- **Workers:** Sonnet 5 or Opus 5 at **Low/Medium for retrieval; High for interpretation**.
- **Harness / concurrency cap:** Claude Code custom subagents or dynamic workflow / 3-5.
- **Alternative route:** GPT-5.6 Sol multi-agent when homogeneous workers are acceptable.
- **Downshift trigger:** Fewer than three truly independent workstreams.
- **Escalation trigger:** Work graph changes, cross-worker dependencies emerge, project persists across rounds.
- **Verification policy:** Source-class coverage checklist, duplicate/contradiction detection, citation verifier.
- **Cost/latency:** Parallelism can reduce wall time but increases total tokens; cheap workers are usually sufficient.
- **Principal failure modes:** Duplicate searches, shallow summaries, synthesis omission.
- **Evidence strength / status:** Moderate; Evidence-backed provisional route.
- **Evidence IDs:** P-O5 p163-168; P-F5 p270-276; W-CODE-SUBAGENTS; W-CODE-WORKFLOWS.
- **Revision trigger:** Controller-swap local eval shows Fable materially improves verified synthesis.

## RT-05 — Fixed peer teams: Independent peers each receive full task and compare or merge results

- **Coupling / decomposition / horizon:** Low to medium / Harness-defined / Hours.
- **Context topology:** Full-task replicated contexts + peer messages.
- **Solo/team choice:** Team only when diversity/replication is valuable.
- **Controller:** Opus 5 or Fable 5 peers; deterministic merger at **High/XHigh**.
- **Workers:** Same model or mixed if harness supports at **High/XHigh; keep consistent within test**.
- **Harness / concurrency cap:** Claude Code agent teams (experimental) or custom fixed peer harness / 3-5.
- **Alternative route:** Subagents plus deterministic synthesis.
- **Downshift trigger:** Shared mutable files or sequential dependencies.
- **Escalation trigger:** Need direct peer debate or independent replication.
- **Verification policy:** Independent outputs before communication; conflict log; final machine check.
- **Cost/latency:** Linear token growth and diminishing returns; strong endpoints in vendor BrowseComp.
- **Principal failure modes:** Same-file conflicts, group convergence, redundant work.
- **Evidence strength / status:** Moderate for benchmark; low for production generalization; Conditional recommendation.
- **Evidence IDs:** P-O5 p163-164; P-F5 p270-271; W-CODE-TEAMS.
- **Revision trigger:** Local repeated trials show stable gain after total-cost accounting.

## RT-06 — Blocking lead-subagent: Lead dispatches one worker, waits, then continues

- **Coupling / decomposition / horizon:** Medium / Known or sequentially discovered / Minutes to hours.
- **Context topology:** Fresh worker contexts; lead bottleneck.
- **Solo/team choice:** Usually avoid.
- **Controller:** Opus 5 High if required at **High**.
- **Workers:** Opus 5 Medium / Sonnet 5 High at **Medium/High**.
- **Harness / concurrency cap:** Blocking supervisor-worker / 1.
- **Alternative route:** Async long-lived subagents or solo lead.
- **Downshift trigger:** One side task only -> named subagent.
- **Escalation trigger:** Multiple independent workstreams or recurring worker context.
- **Verification policy:** Checkpoint after each return; preserve source/tool evidence.
- **Cost/latency:** Synchronization and repeated context establishment can dominate.
- **Principal failure modes:** Lead idle time, context restarts, long latency tail.
- **Evidence strength / status:** Moderate for Fable benchmark architecture; Negative routing recommendation.
- **Evidence IDs:** P-F5 p270-276; P-O48 p210.
- **Revision trigger:** Operational constraints make async impossible and blocking proves reliable.

## RT-07 — Asynchronous lead with long-lived workers: Persistent research/engineering workers with repeated messages and evolving subtasks

- **Coupling / decomposition / horizon:** Medium / Medium-high / Hours.
- **Context topology:** Long-lived isolated contexts + lead integration context.
- **Solo/team choice:** Team.
- **Controller:** Fable 5 at **High; XHigh for capability-sensitive tail**.
- **Workers:** Opus 5 implementers; Sonnet 5 scouts at **Opus Medium; Sonnet High/Medium**.
- **Harness / concurrency cap:** Async Claude Code subagents with explicit checkpoints and messaging / 4 default; raise only with measured utilization.
- **Alternative route:** Opus 5 XHigh controller with same workers.
- **Downshift trigger:** Work graph stabilizes and worker communication becomes one-shot.
- **Escalation trigger:** Repeated replanning, cross-worker coordination, days-scale persistence.
- **Verification policy:** Tool-grounded status, worker deliverables, integration tests, fresh final verifier.
- **Cost/latency:** Fable controller premium can be offset by cheaper workers; long-lived context improves cache economics.
- **Principal failure modes:** Long turns, scope drift, fabricated progress, worker starvation.
- **Evidence strength / status:** Moderate vendor evidence; independent controller comparison missing; Vendor-supported inference.
- **Evidence IDs:** P-F5 p270-276; W-A-FABLE sections Delegation/Parallel subagents; R-CLAW.
- **Revision trigger:** Same-worker controller swap finds Opus equal/better on verified cost or Fable premium fails to repay.

## RT-08 — Dynamic decomposition and replanning: Unknown work graph; streams created, merged, terminated as evidence arrives

- **Coupling / decomposition / horizon:** Variable / Very high / Hours to days.
- **Context topology:** Evolving graph with selective shared state.
- **Solo/team choice:** Team.
- **Controller:** Fable 5 at **XHigh; High as economic starting point**.
- **Workers:** Mixed: Opus 5 Medium/High, Sonnet 5 High, deterministic tools at **Task-specific**.
- **Harness / concurrency cap:** Fable lead + long-lived subagents; script-backed dynamic workflow for repeatable stages / 4-6 with budget and liveness controls.
- **Alternative route:** Opus 5 XHigh + deterministic planner/workflow.
- **Downshift trigger:** Decomposition becomes stable and separable.
- **Escalation trigger:** Integrator repeatedly loses global objective or workers require active reallocation.
- **Verification policy:** Task graph audit, dependency checks, explicit stopping and rollback criteria.
- **Cost/latency:** Highest coordination overhead; use only when topology—not raw task difficulty—is the bottleneck.
- **Principal failure modes:** Runaway fan-out, stale plans, hidden dependencies, forgotten workstreams.
- **Evidence strength / status:** Low-moderate; mainly vendor behavior guidance; Provisional recommendation / speculation bounded by test.
- **Evidence IDs:** W-A-FABLE; W-CODE-WORKFLOWS; P-F5 p275-276.
- **Revision trigger:** Controlled dynamic-task suite reverses manager ranking.

## RT-09 — Implementation orchestration: Independent repository areas with explicit interfaces

- **Coupling / decomposition / horizon:** Low-medium if boundaries are real / Medium / Hours to days.
- **Context topology:** Per-area checkout/worktree plus integration branch.
- **Solo/team choice:** Team.
- **Controller:** Opus 5 at **High**.
- **Workers:** Opus 5 at **Medium implementers; High for ambiguous modules**.
- **Harness / concurrency cap:** Custom subagents/worktrees; controller owns interface contract and merge / 2-4.
- **Alternative route:** Fable High controller + same Opus workers for larger evolving migrations.
- **Downshift trigger:** One module or shared-file hot spot.
- **Escalation trigger:** Interfaces change repeatedly or integration failures dominate.
- **Verification policy:** Worker-local tests, API contract tests, integrated regression suite, human diff review.
- **Cost/latency:** Opus Medium workers exploit implementation sweet spot; avoid Fable workers unless tail capability is needed.
- **Principal failure modes:** Merge conflict, interface drift, duplicated refactors, weak integration.
- **Evidence strength / status:** Moderate for worker effort; low for controller choice; Mixed evidence + recommendation.
- **Evidence IDs:** P-O5 p151; P-F5/P-O5 ProgramBench; W-CODE-SUBAGENTS/TEAMS.
- **Revision trigger:** Repo-scale paired trials show Fable controller reduces integration defects enough to repay cost.

## RT-10 — Debugging with competing hypotheses: Multiple plausible root causes can be tested independently

- **Coupling / decomposition / horizon:** Low during investigation, high at resolution / Medium / Hours.
- **Context topology:** Independent hypothesis contexts; shared evidence board.
- **Solo/team choice:** Team of investigators + one integrator.
- **Controller:** Opus 5 at **High; XHigh if evidence conflicts**.
- **Workers:** Opus 5 Medium or Sonnet 5 High at **Medium/High**.
- **Harness / concurrency cap:** Agent team or subagents with blind initial hypotheses / 3-4.
- **Alternative route:** Fable High for repeated hypothesis generation/reallocation.
- **Downshift trigger:** Reproduction isolates one subsystem.
- **Escalation trigger:** Workers converge prematurely or evidence invalidates decomposition.
- **Verification policy:** Each worker must propose falsifier and execute test; integrator reruns decisive test.
- **Cost/latency:** Parallelism valuable only if tests are independent.
- **Principal failure modes:** Anchoring, correlated hypotheses, evidence cherry-picking.
- **Evidence strength / status:** Low-moderate; harness guidance, not model head-to-head; Method recommendation.
- **Evidence IDs:** W-CODE-TEAMS section competing hypotheses; P-O5 effort profiles.
- **Revision trigger:** Local debugging benchmark measures no benefit over solo.

## RT-11 — Writer-verifier: Draft plus independent factual/citation/acceptance verification

- **Coupling / decomposition / horizon:** Sequential but separable roles / Low / Minutes to hours.
- **Context topology:** Fresh verifier context with source packet.
- **Solo/team choice:** Two-stage team or deterministic verifier.
- **Controller:** Opus 5 at **High for synthesis; Medium for bounded writing**.
- **Workers:** Sonnet 5 High, Opus 5 Medium, or GPT-5.6 Sol High as heterogeneous verifier at **High for verification**.
- **Harness / concurrency cap:** Explicit writer -> verifier -> repair loop with capped retries / 1 writer + 1 verifier.
- **Alternative route:** One Opus 5 Medium with deterministic checks when risk is low.
- **Downshift trigger:** All claims machine-verifiable and low consequence.
- **Escalation trigger:** Material contradictions, high-stakes decision, weak source coverage.
- **Verification policy:** Verifier sees acceptance criteria and primary evidence, not writer rationale; human adjudication for load-bearing disputes.
- **Cost/latency:** Fresh verification adds cost but is more defensible than broad swarm.
- **Principal failure modes:** Verifier deference, shared-family correlated error, endless repair loop.
- **Evidence strength / status:** Low-moderate; official guidance plus evaluation methodology; Recommended control pattern.
- **Evidence IDs:** W-A-OPUS; AHR-C §§11.7-11.9; W-CODE-SUBAGENTS.
- **Revision trigger:** Calibrated human sample shows verifier fails to catch severe errors.

## RT-12 — Implementer-reviewer: Code implementation then independent review/test attack

- **Coupling / decomposition / horizon:** Sequential / Low-medium / Hours.
- **Context topology:** Implementer repo context; reviewer fresh diff/test context.
- **Solo/team choice:** Two-stage.
- **Controller:** Opus 5 at **High**.
- **Workers:** Opus 5 Medium implementer + Sonnet 5 High or Sol High reviewer at **Medium / High**.
- **Harness / concurrency cap:** Subagents or separate sessions; reviewer cannot edit until findings logged / 1+1.
- **Alternative route:** Opus 5 Medium solo with tests.
- **Downshift trigger:** Mechanical patch and exhaustive tests.
- **Escalation trigger:** Security, data migration, or architecture-sensitive change.
- **Verification policy:** Review checklist, hidden tests, mutation/adversarial tests; human approval for release.
- **Cost/latency:** Cheaper heterogenous reviewer may improve error diversity.
- **Principal failure modes:** Rubber-stamp review, shared blind spot, reviewer rewriting instead of testing.
- **Evidence strength / status:** Low-moderate; Recommendation.
- **Evidence IDs:** P-O5 p151; W-CURSOR; AHR-C evaluation clauses.
- **Revision trigger:** Paired review experiment shows no severe-failure reduction.

## RT-13 — Sequential tool/API automation: Stateful sequence where next action depends on prior tool result

- **Coupling / decomposition / horizon:** High / sequential / Low-medium / Minutes to hours.
- **Context topology:** One state ledger.
- **Solo/team choice:** Solo or deterministic workflow.
- **Controller:** Opus 5 or GPT-5.6 Sol at **Medium; High for ambiguous rules**.
- **Workers:** None or deterministic stage tools at **n/a**.
- **Harness / concurrency cap:** Single agent + explicit state machine / programmatic tool calling / 0.
- **Alternative route:** Sonnet 5 High for routine low-risk flows.
- **Downshift trigger:** Deterministic graph can be scripted.
- **Escalation trigger:** Independent research branches appear.
- **Verification policy:** Read-after-write, idempotency, transaction log, external end-state check.
- **Cost/latency:** Multiple agents usually add overhead without parallel benefit.
- **Principal failure modes:** State loss, duplicate side effects, stale reads.
- **Evidence strength / status:** Moderate for architecture; model comparison low-moderate; Architecture-first recommendation.
- **Evidence IDs:** P-O5 p148 Table 8.1.A; W-OAI-GPT56; W-CODE-AGENTS.
- **Revision trigger:** Local workflow trials show another route improves verified completion.

## RT-14 — Days-scale project management: Persistent evolving project with memory, worker lifecycle, checkpoints, and reprioritization

- **Coupling / decomposition / horizon:** Mixed / Very high / Days to weeks.
- **Context topology:** Long-lived worker memories + external project ledger.
- **Solo/team choice:** Team.
- **Controller:** Fable 5 at **High initially; XHigh on replanning/recovery checkpoints**.
- **Workers:** Mixed: Opus 5 Medium implementers, Sonnet 5 High scouts/reviewers, deterministic tools at **Task-specific; keep routine work below XHigh**.
- **Harness / concurrency cap:** Async lead + long-lived subagents + external task/memory system + scheduled verification gates / 4 active; queued backlog; explicit total worker budget.
- **Alternative route:** Opus 5 XHigh controller inside deterministic project-management scaffold.
- **Downshift trigger:** Project decomposes into stable work packages.
- **Escalation trigger:** Repeated missed dependencies, stalled workers, integration failures.
- **Verification policy:** Daily/phase evidence audit, acceptance tests, rollback checkpoints, human approval at irreversible gates.
- **Cost/latency:** Fable price premium is concentrated in controller; worker mix controls total spend; longest latency tails.
- **Principal failure modes:** False status, scope drift, forgotten dependencies, unbounded spend.
- **Evidence strength / status:** Low-moderate; vendor positioning and harness guidance; Vendor-supported recommendation requiring local pilot.
- **Evidence IDs:** W-A-FABLE long-horizon/delegation/progress; W-CODE-WORKFLOWS; R-CLAW.
- **Revision trigger:** 30-task local longitudinal pilot shows no coordination advantage or unacceptable refusal/availability burden.

## RT-15 — Homogeneous teams: Same model and effort for lead and workers

- **Coupling / decomposition / horizon:** Varies / Varies / Varies.
- **Context topology:** Multiple similar contexts.
- **Solo/team choice:** Use for clean benchmark comparison or simple deployment.
- **Controller:** Opus 5 or Fable 5 at **Match worker effort only when experiment requires**.
- **Workers:** Same as controller at **Same as controller**.
- **Harness / concurrency cap:** Vendor-style fixed/async team / Benchmark-specific.
- **Alternative route:** Mixed team that separates controller and worker economics.
- **Downshift trigger:** Worker tasks are routine.
- **Escalation trigger:** Worker capability is the bottleneck.
- **Verification policy:** Report lead and worker effort separately; preserve failures.
- **Cost/latency:** Simple but confounds controller and worker quality; expensive with Fable.
- **Principal failure modes:** Cannot attribute gain, correlated errors, needless premium workers.
- **Evidence strength / status:** High for confounding diagnosis; Evaluation warning.
- **Evidence IDs:** P-O5 p168; P-F5 p275-276; AHR-C §11.2.
- **Revision trigger:** Published controller-swap study resolves attribution.

## RT-16 — Mixed-model teams: Premium controller + efficient implementation workers

- **Coupling / decomposition / horizon:** Medium / High / Hours to days.
- **Context topology:** Manager context plus task-specialized worker contexts.
- **Solo/team choice:** Team.
- **Controller:** Fable 5 at **High/XHigh**.
- **Workers:** Opus 5 at **Medium implementers; High for ambiguous modules**.
- **Harness / concurrency cap:** Claude Code custom subagents with per-worker model/effort overrides / 3-5.
- **Alternative route:** Opus 5 High controller + same workers.
- **Downshift trigger:** Controller spends most time doing implementation rather than organization.
- **Escalation trigger:** Work graph churn, cross-worker communication, integration defects.
- **Verification policy:** Controller cannot mark worker task done without tests/evidence; independent final verifier.
- **Cost/latency:** Economic hypothesis: buy Fable only for management tokens; not publicly validated head-to-head.
- **Principal failure modes:** Manager overreach, workers under-scoped, integration blind spot.
- **Evidence strength / status:** Low; plausible mixed policy, not controlled public result; Explicit experimental policy.
- **Evidence IDs:** W-A-FABLE; P-O5 p151; W-CODE-MODEL-CONFIG.
- **Revision trigger:** Controller-isolation A/B shows cost per verified success is worse than Opus controller.

## RT-17 — Mixed-model teams: Strong controller + low-cost scouts / breadth workers

- **Coupling / decomposition / horizon:** Low / Known / Minutes to hours.
- **Context topology:** Many isolated retrieval contexts.
- **Solo/team choice:** Team.
- **Controller:** Opus 5 at **High**.
- **Workers:** Sonnet 5 or GPT-5.6 Terra/Luna at **Low/Medium/High depending source interpretation**.
- **Harness / concurrency cap:** Custom subagents or cross-provider workflow / 3-6.
- **Alternative route:** GPT-5.6 Sol multi-agent homogeneous.
- **Downshift trigger:** Retrieval volume small.
- **Escalation trigger:** Workers must make high-stakes interpretive judgments.
- **Verification policy:** Controller samples primary sources; deterministic dedupe and citation checks.
- **Cost/latency:** Largest cost savings when worker volume dominates; cross-provider integration adds engineering/privacy burden.
- **Principal failure modes:** Cheap-worker omissions, inconsistent formats, transport friction.
- **Evidence strength / status:** Low-moderate; Economic recommendation.
- **Evidence IDs:** W-A-PRICE; W-OAI-GPT56; P-S5; W-CODE-SUBAGENTS.
- **Revision trigger:** Trace replay shows quality loss outweighs savings.

## RT-18 — High-stakes audit / decision support: Consequential factual synthesis with contradictory evidence

- **Coupling / decomposition / horizon:** Medium / High / Hours to days.
- **Context topology:** Source-class partitions + central claim ledger.
- **Solo/team choice:** Bounded team with human adjudication.
- **Controller:** Opus 5 or Fable 5 at **High/XHigh**.
- **Workers:** Heterogeneous researchers/verifiers at **High where interpretation is load-bearing**.
- **Harness / concurrency cap:** Bounded fan-out + writer-verifier + human sign-off / 3-5.
- **Alternative route:** GPT-5.6 Sol High/XHigh with same controls.
- **Downshift trigger:** Low consequence and direct primary evidence.
- **Escalation trigger:** Material disagreement, legal/financial/safety consequence, unresolved citations.
- **Verification policy:** Claim-level source links, calculation audit, human validation of load-bearing judgments.
- **Cost/latency:** Verification burden dominates model price; optimize cost per acceptable verified result.
- **Principal failure modes:** Citation laundering, false consensus, correlated model judges.
- **Evidence strength / status:** Methodological; Governance requirement.
- **Evidence IDs:** AHR-C §§6-7,10-13.
- **Revision trigger:** User risk tolerance or authoritative evidence changes.

## RT-19 — Long-context work: One coherent corpus with global dependencies and little parallelism

- **Coupling / decomposition / horizon:** High / Low but global context needed / Hours.
- **Context topology:** Single large context.
- **Solo/team choice:** Solo.
- **Controller:** Opus 5 or GPT-5.6 Sol; Fable for extreme ambiguity at **High/XHigh**.
- **Workers:** Optional retrieval scouts only at **Low/Medium**.
- **Harness / concurrency cap:** Single long-context agent with indexed evidence / 0-2.
- **Alternative route:** Fable High/XHigh for multithreaded ambiguity.
- **Downshift trigger:** Corpus can be partitioned without cross-links.
- **Escalation trigger:** Context exceeds reliable recall or contradictory source classes require independent checks.
- **Verification policy:** Evidence map, retrieval recall checks, source citations.
- **Cost/latency:** Parallel agents duplicate corpus tokens; long-input pricing/caching matters.
- **Principal failure modes:** Lost cross-document dependency, context dilution, expensive duplication.
- **Evidence strength / status:** Low-moderate; Conditional recommendation.
- **Evidence IDs:** W-A-FABLE ambiguity; W-OAI-GPT56; model specs.
- **Revision trigger:** Local long-context retrieval tests show stable superiority.

## RT-20 — Artifact / multimodal production: Documents, spreadsheets, slides, visual QA, or computer-use refinement

- **Coupling / decomposition / horizon:** Medium-high / Medium / Hours.
- **Context topology:** Artifact state + visual feedback loop.
- **Solo/team choice:** Solo creator plus verifier; avoid broad team.
- **Controller:** GPT-5.6 Sol or Opus 5; Fable for complex enterprise bundles at **High/XHigh**.
- **Workers:** Sonnet 5 / Sol Terra for extraction or QA at **Medium/High**.
- **Harness / concurrency cap:** Artifact toolchain with render-and-verify loop / 1-2.
- **Alternative route:** Fable High for long-running multithreaded enterprise workflow.
- **Downshift trigger:** Template fill or simple transformation.
- **Escalation trigger:** Many linked artifacts, contradictory source data, repeated visual defects.
- **Verification policy:** Render/open every artifact; formula/link/reference validation.
- **Cost/latency:** Sol has strong current vendor/practitioner evidence for artifacts; harness matters more than raw model.
- **Principal failure modes:** Polished but wrong output, broken formulas, layout defects.
- **Evidence strength / status:** Low-moderate; vendor/practitioner reports; Cross-model recommendation.
- **Evidence IDs:** W-OAI-GPT56; P-F5 enterprise guidance; AHR-C §12.4.
- **Revision trigger:** Representative artifact suite with blinded human scoring changes ranking.

# 8. Harness selection

## 8.1 Named custom subagents: default for controlled mixed teams

Use when each worker has a stable role, should have isolated context, and should return a summary/artifact to one lead. The current docs support separate system prompts, tool/permission restrictions, model overrides, and effort overrides through subagent/model configuration. This is the best current fit for Fable-controller + Opus-worker experiments because it exposes the variables that must be held constant. [W-CODE-SUBAGENTS, “Create custom subagents,” §“Supported frontmatter fields,” accessed 24 July 2026](https://code.claude.com/docs/en/sub-agents); [W-CODE-MODEL-CONFIG, “Model configuration,” §“Configure effort level,” accessed 24 July 2026](https://code.claude.com/docs/en/model-config).

## 8.2 Agent teams: direct peer communication, with experimental risk

Use when peers need to debate, share discoveries directly, or independently attack hypotheses. Do not use for sequential dependencies, shared-file hot spots, or small tasks. The feature is experimental; teammates can use specified models but inherit lead effort, and the docs warn of coordination overhead and diminishing returns. Start with three to five. [W-CODE-TEAMS, “Orchestrate teams of Claude Code sessions,” §“Agent teams are experimental,” accessed 24 July 2026](https://code.claude.com/docs/en/agent-teams); [W-CODE-TEAMS, “Orchestrate teams of Claude Code sessions,” §“Specify teammates and models,” accessed 24 July 2026](https://code.claude.com/docs/en/agent-teams); [W-CODE-TEAMS, “Orchestrate teams of Claude Code sessions,” §“Choose an appropriate team size,” accessed 24 July 2026](https://code.claude.com/docs/en/agent-teams).

## 8.3 Dynamic workflows: large repeatable fan-out

Use for codebase-wide audits, migrations, source sweeps, or cross-check pipelines where the orchestration should be inspectable and rerunnable. The runtime stores intermediate results in script variables instead of flooding the lead context. This reduces free-form manager burden and makes Opus competitive with Fable for stable graph stages. [W-CODE-WORKFLOWS, “Orchestrate subagents at scale with dynamic workflows,” §“How a workflow runs,” accessed 24 July 2026](https://code.claude.com/docs/en/workflows).

## 8.4 Blocking supervisor-worker: narrow exception

Use only when the work is inherently sequential or the environment cannot support async execution. Fable’s reported blocking setup is substantially below its async endpoint, while Opus 4.8’s blocking setup is contrary evidence that architecture effects can reverse by model/configuration. [P-F5, p. 270, Fig. 8.15.1.A](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=270); [P-O48, p. 210, Fig. 8.11.1.A](https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf#page=210).

## 8.5 OpenAI Responses multi-agent: homogeneous beta alternative

Use when workstreams divide cleanly and a single request with one model/tool set is operationally attractive. It is not a substitute for a mixed Claude team experiment because current subagents share the request model and tools. [W-OAI-MULTI, “Multi-agent,” §“Overview / How Multi-agent works,” accessed 24 July 2026](https://developers.openai.com/api/docs/guides/responses-multi-agent).

# 9. Mixed policies to test

## 9.1 Fable High controller + Opus Medium implementers

**Use when:** integration, worker lifecycle, and task-graph management are harder than each implementation unit. **Why plausible:** Fable has the strongest vendor manager positioning; Opus Medium has the strongest reported bounded implementation sweet spot. **Why unverified:** no controlled public mixed cell was located. **Control:** keep the Fable controller from writing code unless it is critical-path integration; cap active workers at four; require worker-local and integrated tests. [W-A-FABLE, “Prompting Claude Fable 5,” §“Capability improvements,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5); [P-O5, p. 151, Figs. 8.4.A-B](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=151); [W-CODE-MODEL-CONFIG, “Model configuration,” §“Configure effort level,” accessed 24 July 2026](https://code.claude.com/docs/en/model-config).

## 9.2 Fable XHigh controller + Sonnet High breadth workers

**Use when:** the project is long-lived and information-heavy, but individual scouting/review tasks are bounded. **Value hypothesis:** spend premium tokens on prioritization/replanning, not on every source fetch. **Main risk:** worker omissions force expensive controller rework. **Verification:** controller samples primary evidence and uses a fresh high-quality verifier for load-bearing claims.

## 9.3 Opus High controller + Opus Medium implementers

**Use when:** repo partitions are stable and the controller is principally planning, interface management, and integration. This is the default mixed Claude implementation route because it requires no unproven Fable premium. Escalate the controller to XHigh only after integration or replanning failures.

## 9.4 Opus High controller + lower-cost scouts

**Use when:** source retrieval, inventory, or triage dominates worker volume. Sonnet, Terra, or Luna can be used as scouts if the harness records provider/model/effort and the Opus controller verifies primary evidence. Cross-provider workers add schema, privacy, transport, caching, and failure-handling burden; count those costs.

## 9.5 Fable “sandwich”: architect/controller → efficient implementers → Fable/Opus verifier

This is an explicit experiment, not an evidence-backed default. It may be valuable where requirements and final integration are the rare hard parts. It may also duplicate premium reasoning and create correlated review. Compare it against Opus High controller + fresh heterogeneous verifier, not against an artificially weak baseline.

# 10. Controlled local evaluation

## 10.1 What was executed

A runnable control-plane harness was created and executed in **fixture mode**. It generated 80 synthetic trajectories (10 tasks × 2 pilot repeats × 4 primary controller labels), verified that every task/repeat pair had one identical control fingerprint across controller cells, wrote aggregate/control-balance CSVs, and passed three unit tests. No live Anthropic or OpenAI model call was available in this environment, so the fixture results are explicitly marked synthetic and are **not** performance evidence.

Files: `local_eval/README.md`, `evaluation_config.json`, `task_manifest.jsonl`, locked prompts, schema, `run_eval.py`, `analyze.py`, `test_harness.py`, and fixture outputs.

## 10.2 Primary causal design

**Controller cells:** Fable High, Fable XHigh, Opus High, Opus XHigh.  
**Fixed workers:** Opus 5 Medium.  
**Held constant:** tasks, task order randomization procedure, controller prompt, worker prompt, tools, permissions, budgets, context packet, cache policy, concurrency cap four, total spawn cap twelve, timeouts, infrastructure retry, verifier, acceptance tests, and worker seeds.  
**Repeated trials:** five per task/cell after a two-repeat pilot, with paired seeds.  
**Holdout:** 30% of tasks untouched until prompts/rubrics freeze.  
**Primary outcome:** cost per acceptable verified result.  
**Severe failures:** unauthorized side effect, false completion, lost/overwritten work, broken invariant, fabricated citation, or budget/concurrency breach.  

This isolates controller quality in the sense relevant to the question: all worker capability and harness resources remain fixed, so differences in decomposition, messaging, replanning, integration, stopping, or verification can be attributed to the controller cell subject to stochastic uncertainty. [R-CLAW, commit 630efd8a0d1dc8189718226c7da158cbe4c2fe64, ClawArena-Team/README.md, lines 8-41](https://github.com/aiming-lab/ClawArena/blob/630efd8a0d1dc8189718226c7da158cbe4c2fe64/ClawArena-Team/README.md) provides independent support for the fixed-worker logic, while AHR-C §§11.2-11.11 requires configuration control, repeated trials, failure preservation, and human validation.

## 10.3 Task families

The manifest covers bounded research fan-out, fixed peers, async long-lived workers, dynamic replanning, repo-area implementation, competing-hypothesis debugging, writer-verifier, sequential automation, a simulated days-scale project, and a mixed-team control. Real deployment decisions should replace or supplement these fixtures with representative user tasks; public benchmarks cannot substitute for the target distribution.

## 10.4 Metrics and analysis

- Acceptable verified success and severe-failure rate.
- Cost and wall-clock time to verified result, including all controller/worker/tool/human-review costs.
- Controller versus worker tokens and critical-path latency.
- Duplicate work, delegation errors, integration defects, stale dependencies, and replan quality.
- Human review minutes, intervention count, refusal/fallback events, served model, and infrastructure failures.
- Paired contrasts by task and repeat; medians/P90s; bootstrap intervals; task-family heterogeneity. No universal scalar without an explicit utility function.

## 10.5 Decision thresholds

Adopt Fable as the controller only if it produces a practically meaningful reduction in severe failures or time/cost per verified result, not merely longer plans or higher model-judge scores. A sensible starting rule is:

- **Fable wins:** ≥10% lower cost per acceptable verified result or a material severe-failure reduction, with no operational gate failure.
- **Opus wins:** non-inferior verified success within the predeclared margin and lower cost/latency/verification burden.
- **No decision:** confidence intervals span the practical margin, task-family effects conflict, or controller fingerprints drift.

These thresholds are recommendations and should be adjusted to the user’s values before live trials.

# 11. Cost and latency implications

## 11.1 List-rate arithmetic

- Opus versus Fable input: $5 / $10 = **0.50**.
- Opus versus Fable output: $25 / $50 = **0.50**.
- Therefore a same-token Fable team costs exactly 2× Opus at base rates; real workflows can differ because Fable may use fewer/more tokens, cache differently, trigger fallback, or improve completion enough to reduce retries. [W-A-PRICE, “Pricing,” §“model pricing table,” accessed 24 July 2026](https://platform.claude.com/docs/en/about-claude/pricing).

## 11.2 CursorBench complete-configuration arithmetic

- Fable Max versus Opus Max: $17.32 / $8.23 = 2.1045 → **2.10× cost** for 70.5 − 70.0 = **+0.5 pp**.
- Fable Max versus Opus High: $17.32 / $3.91 = 4.4297 → **4.43× cost** for 70.5 − 66.7 = **+3.8 pp**.
- Sol Max versus Opus Max: $5.69 / $8.23 = 0.6914 → **69% of the cost** for 67.2 − 70.0 = **−2.8 pp**.

These ratios are benchmark-specific and omit uncertainty intervals. They demonstrate why effort and model choice cannot be justified by score alone. [W-CURSOR, “CursorBench 3.2,” §“leaderboard and methodology,” accessed 24 July 2026](https://cursor.com/cursorbench).

![CursorBench score-cost](../charts/cursorbench_score_cost.png)

*Figure 7. Current CursorBench 3.2 reported configurations. Source: [W-CURSOR, “CursorBench 3.2,” §“leaderboard and methodology,” accessed 24 July 2026](https://cursor.com/cursorbench).*

## 11.3 Team cost model

For a team, compute total model cost as the sum over controller and workers, not “controller price × one.” A minimal audit formula is:

`Total USD = Σ[(uncached_input_MTok × input_rate) + (cache_write_MTok × write_rate) + (cache_read_MTok × read_rate) + (output_MTok × output_rate)] + tool_cost + human_review_cost`

Then divide by acceptable verified outcomes, not by attempts. Report both total compute and critical-path wall time; vendor cards derive critical-path latency and make cache assumptions. [P-O5, p. 168, §8.11.4 Multi-agent harnesses and methodology](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf#page=168); [P-F5, p. 276, §8.15.4 Methodology](https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf#page=276).

# 12. Failure modes and controls

| Failure | Most exposed route | Detection | Control |
|---|---|---|---|
| Overdelegation / tiny tasks | Opus or Fable free-form lead | worker utilization, duplicate rate | deterministic cap; minimum task-size rule |
| Controller becomes another implementer | Opus/Fable mixed team | lead token/tool share, missing global state | role contract; controller-owned task graph and integration |
| False progress/completion | long Fable runs | claim-to-tool evidence audit | required evidence pointer for every status |
| Stale worker context | persistent async | contradiction with current dependency graph | versioned task packets; update messages; stale-result rejection |
| Same-file conflict | peer implementation team | merge conflict / overwritten work | worktrees; file ownership; avoid peer team |
| Group anchoring | fixed peers | correlated hypotheses before evidence | blind first pass; adversarial falsification |
| Over-verification | Opus 5 | redundant checks, token spike | remove legacy verification prompt; one independent verifier |
| Runaway cost | all teams, especially Fable Max | token/spawn/latency budget alarms | per-phase budgets; queue; early stop; no quality retry |
| Refusal/fallback confound | Fable deployed surface | served model, stop reason, latency | log fallback; analyze intent-to-treat and served-model results |
| Model-judge bias | writer/verifier evaluations | human disagreement sample | blind, calibrate, adjudicate load-bearing cases |

# 13. Failed searches, negative evidence, and missing cells

The following are preserved as failures or non-findings, not transformed into substantive absence:

- **M-001 — Which model is the better controller with identical workers?** Status: Unknown. Why missing: Anthropic teams change lead and workers together; ClawArena lacks Opus5 and uses one run/fallback. Highest-value test: Controller-swap local evaluation with fixed Opus5 Medium workers and paired seeds.
- **M-002 — What is the optimal lead effort for each orchestration taxonomy cell?** Status: Unknown/partial. Why missing: No public lead effort sweep; only solo effort curves and one low-worker async cell. Highest-value test: Factor controller effort High/XHigh first, add Medium/Max only if pilot curve warrants.
- **M-003 — Does Fable controller premium repay cost in real repository orchestration?** Status: Unknown. Why missing: No controlled mixed-team study with cost, integration defects, and repeated trials. Highest-value test: Paired repo tasks with fixed workers, identical worktrees/tools, blinded verification.
- **M-004 — How often do Fable safeguards/refusals/fallbacks affect benign target workloads?** Status: Unknown and workload-specific. Why missing: No task-stratified public refusal dataset for the user workload. Highest-value test: Shadow run representative benign prompts; log stop_reason, fallback, served model, latency, cost.
- **M-005 — What are tail latency and variance by effort/team size?** Status: Mostly unknown. Why missing: Cards show selected aggregate/critical-path curves; raw distributions unavailable. Highest-value test: At least five repeated trials per cell, report median/P90/P95 and failure distribution.
- **M-006 — How do Sonnet 5 and Sol perform as identical workers under Fable vs Opus controllers?** Status: Unknown. Why missing: No public crossed controller x worker study. Highest-value test: Secondary worker strata after primary fixed-worker experiment.
- **M-007 — Do days-scale projects preserve objective and state without human intervention?** Status: Unknown. Why missing: Vendor positioning and anecdotes, no public longitudinal controlled study. Highest-value test: Instrumented 48-72 hour project simulations with injected worker failure and plan changes.

Tool/retrieval failures included: official PDF pages could not be opened through the web PDF renderer (`(400) OK`), so stable PDFs were downloaded, hashed, rendered locally, and visually inspected; an arXiv PDF download and a local GitHub clone failed DNS resolution, so the HTML/abstract and pinned raw repository file were used; the full text/configuration of a social post about a Fable-controller/Sonnet-worker result was not recoverable and was demoted to a hypothesis signal; an unsourced “advisor” performance claim was excluded. See `data/search_log.csv`.

# 14. Decision implications and revision triggers

## 14.1 Production adoption sequence

1. Keep a solo Opus Medium/High baseline with deterministic verification.
2. Add Opus High controller + fixed Opus Medium workers on tasks with real independence.
3. Run the same-worker Fable High/XHigh controller swap on a representative holdout.
4. Adopt Fable only in task families where verified value repays controller premium and operational constraints.
5. Add Sonnet or Sol/Terra worker strata only after controller ranking stabilizes; otherwise worker changes confound the answer.
6. Re-evaluate after model snapshot, pricing, Claude Code team/workflow semantics, fallback/safeguards, or task distribution changes.

## 14.2 Highest-value revision triggers

- A controlled Opus5/Fable5 fixed-worker manager study.
- A published lead-effort × worker-effort matrix.
- Local severe-failure or cost-per-verified-result differences exceeding the predeclared margin.
- Changes to Fable classifier/fallback/data terms or availability in the target account.
- Claude Code agent teams graduating from experimental status or changing effort/model inheritance.
- OpenAI multi-agent adding per-subagent model/effort routing.
- A benchmark revision or representative local task mix that reverses the effort curve.

# 15. Claim ledger

The machine-readable ledger is `data/claim_ledger.csv`; every record includes the requested epistemic status, direct support, contrary evidence, source role, scope, confidence basis, calculation, and revision trigger.

## C-001 — Opus 5 base input and output token rates are exactly half Fable 5 rates as of 2026-07-24.

- **Epistemic status:** Verified external fact
- **Direct support:** W-A-PRICE, Pricing model table, accessed 2026-07-24.
- **Contrary evidence:** None for list rates; total task cost can reverse because token volume, caching, fallback, tools, verification, and retries differ.
- **Source role:** Vendor pricing documentation
- **Scope conditions:** Anthropic API base token rates in USD; date-sensitive.
- **Confidence basis:** Direct official current price table.
- **Calculation:** Input: $5 / $10 = 0.50; output: $25 / $50 = 0.50.
- **Revision trigger:** Pricing or promotional terms change.

## C-002 — On FrontierCode Main and Extended in the Opus 5 card, Opus 5 scores highest at Medium, not High/XHigh/Max.

- **Epistemic status:** Vendor-reported observation
- **Direct support:** P-O5 p.151, Figs. 8.4.A-B. Main: 41.9, 53.4, 48.0, 43.6, 48.0. Extended: 55.8, 63.6, 58.5, 56.9, 58.9.
- **Contrary evidence:** CursorBench 3.2 rises from Opus Medium 64.3 to Max 70.0; DeepSWE rises through XHigh.
- **Source role:** Vendor system card using Cognition benchmark
- **Scope conditions:** Autonomous patch generation in Cognition FrontierCode harness; mean@5; does not establish universal implementation optimum.
- **Confidence basis:** Exact numeric figure labels and sharp non-monotonic differences.
- **Calculation:** Main Medium minus XHigh = 53.4 - 43.6 = +9.8 pp; Extended Medium minus XHigh = 63.6 - 56.9 = +6.7 pp.
- **Revision trigger:** Representative local implementation suite shows higher effort reliably improves verified success.

## C-003 — For DeepSWE v1.1, both Opus 5 and Fable 5 peak at XHigh and slightly regress at Max.

- **Epistemic status:** Vendor-reported observation
- **Direct support:** P-O5 p.150, Fig. 8.3.A. Opus 69.7 XHigh vs 68.8 Max; Fable 69.9 vs 69.7.
- **Contrary evidence:** Other tasks, including CursorBench, peak at Max; Opus4.8 and Sonnet5 DeepSWE continue rising to Max.
- **Source role:** Vendor system card
- **Scope conditions:** DeepSWE v1.1 harness only.
- **Confidence basis:** Exact figure values.
- **Calculation:** Opus regression 68.8 - 69.7 = -0.9 pp; Fable regression 69.7 - 69.9 = -0.2 pp.
- **Revision trigger:** New DeepSWE version or released-config replication changes curve.

## C-004 — BrowseComp single-agent performance mostly plateaus by High for Opus 5 and by XHigh for Fable/Mythos 5.

- **Epistemic status:** Synthesis from vendor-reported observation
- **Direct support:** P-O5 p.160, Fig. 8.10.2.B. Opus High 90.2, XHigh 90.7, Max 90.8; Fable High 87.3, XHigh 88.0, Max 88.0.
- **Contrary evidence:** High-to-XHigh can still matter for rare hard cases; cost/latency labels should be considered.
- **Source role:** Vendor system card
- **Scope conditions:** BrowseComp, single agent, fixed 10M-token budget.
- **Confidence basis:** Small marginal score changes after High/XHigh.
- **Calculation:** Opus Max - High = +0.6 pp; Fable Max - XHigh = 0.0 pp.
- **Revision trigger:** Hard-tail or utility-weighted analysis finds material gains hidden by average score.

## C-005 — Opus 4.8 async lead with subagents scored below its own 10M-token solo BrowseComp baseline.

- **Epistemic status:** Vendor-reported observation
- **Direct support:** P-O48 p.210, Fig. 8.11.1.A: async 83.0; solo 10M 84.3.
- **Contrary evidence:** Opus4.8 fixed five-agent 85.4 and blocking orchestrator 88.5 both exceeded solo; the failure is harness-specific.
- **Source role:** Vendor system card
- **Scope conditions:** Opus4.8 BrowseComp async harness; not all multi-agent work.
- **Confidence basis:** Direct exact labels.
- **Calculation:** 83.0 - 84.3 = -1.3 percentage points.
- **Revision trigger:** Same-harness replication with current snapshot or released historical config.

## C-006 — Opus 5 no longer reproduces the specific Opus 4.8 negative async BrowseComp result.

- **Epistemic status:** Cross-version synthesis
- **Direct support:** P-O5 p.163 Fig. 8.11.1.A: async 93.4 vs solo 90.5; P-O48 p.210: async 83.0 vs solo 84.3.
- **Contrary evidence:** Cards use different vintages/configurations; Opus5 runs were pre-release, unreleased effort, no safety classifiers.
- **Source role:** Vendor system cards
- **Scope conditions:** Direction of async uplift on BrowseComp only.
- **Confidence basis:** Sign of within-card delta changes from negative to positive.
- **Calculation:** Opus5 rounded delta = 93.4 - 90.5 = +2.9 pp; Opus4.8 = -1.3 pp.
- **Revision trigger:** Released Opus5 async reproduction or other orchestration tasks show regression.

## C-007 — Fable/Mythos 5 receives a larger within-card async BrowseComp uplift than Opus 5.

- **Epistemic status:** Calculation from vendor-reported observations
- **Direct support:** P-F5 p.270: 93.3 vs 88.0; P-O5 p.163: 93.4 vs 90.5.
- **Contrary evidence:** Fable starts from lower solo baseline; cards are not one controlled experiment; Opus prose uses unrounded +2.8.
- **Source role:** Vendor system cards
- **Scope conditions:** Within-card rounded score deltas; not controller quality.
- **Confidence basis:** Transparent arithmetic with caveats.
- **Calculation:** Fable +5.3 pp; Opus +2.9 pp rounded (p.164 prose +2.8); difference ≈2.4-2.5 pp.
- **Revision trigger:** Same-task, same-worker, same-budget controller swap.

## C-008 — The 93.4 Opus 5 and 93.3 Fable async endpoints are approximately tied and do not support a one-decimal superiority claim.

- **Epistemic status:** Synthesis / interpretation
- **Direct support:** P-O5 p.163 and P-F5 p.270.
- **Contrary evidence:** Numerically Opus is 0.1 higher, but configuration and card differences dominate that gap.
- **Source role:** Cross-source synthesis
- **Scope conditions:** Separate vendor cards, different model/configuration vintages.
- **Confidence basis:** Gap is tiny relative to uncontrolled differences and unknown variance.
- **Calculation:** 93.4 - 93.3 = 0.1 pp.
- **Revision trigger:** Controlled head-to-head with uncertainty intervals.

## C-009 — Public homogeneous-team results do not isolate controller quality from worker and integrator quality.

- **Epistemic status:** Verified methodological limitation
- **Direct support:** P-O5 p.168 and P-F5 pp.275-276 describe same-model/effort team configurations; AHR-C §11.2 requires configuration-level attribution.
- **Contrary evidence:** ClawArena-Team isolates managers with a fixed worker pool, but has no Opus5 row and uses one run/fallback.
- **Source role:** Vendor methodology + independent repository artifact
- **Scope conditions:** Attribution of causal manager quality.
- **Confidence basis:** Lead and worker variables change together in reported Anthropic teams.
- **Calculation:** Not applicable.
- **Revision trigger:** Published same-worker controller-swap experiment includes Opus5 and Fable5.

## C-010 — Anthropic officially characterizes Fable 5 as more dependable at dispatching and sustaining parallel subagents.

- **Epistemic status:** Official vendor claim
- **Direct support:** W-A-FABLE, section Capability improvements, accessed 2026-07-24.
- **Contrary evidence:** No independent controlled Opus5-vs-Fable5 manager study located; claim may reflect internal setup and product positioning.
- **Source role:** Vendor web guidance
- **Scope conditions:** Declared product behavior, not independently verified prevalence or superiority.
- **Confidence basis:** Direct official wording; institutional interest explicitly qualified.
- **Calculation:** Not applicable.
- **Revision trigger:** Independent same-worker study contradicts or quantifies the claim.

## C-011 — ClawArena-Team is designed to isolate manager quality by holding a fixed locally served worker pool constant.

- **Epistemic status:** Verified implementation-artifact claim
- **Direct support:** R-CLAW commit 630efd8..., README lines 8-9 and 23-33.
- **Contrary evidence:** Benchmark tasks are procedurally generated/authored partly by the capability measured; one run per manager; Fable uses refusal fallback; Opus5 absent.
- **Source role:** Independent benchmark repository
- **Scope conditions:** Benchmark design, not current Fable-vs-Opus5 ranking.
- **Confidence basis:** Pinned commit and explicit design description.
- **Calculation:** 41 scenarios, 258 rounds, 72 staged updates as reported.
- **Revision trigger:** Repository methods or leaderboard updated with repeated Opus5 runs.

## C-012 — Multi-agent overhead can make easy problems slower even when hard-tail problems benefit.

- **Epistemic status:** Vendor-reported observation
- **Direct support:** P-F5 p.272: median per-problem speedup 0.8x on easy bucket and 1.6x on hard bucket; summed hard-bucket latency 4.4x. P-O48 p.211 reports similar hard-tail pattern.
- **Contrary evidence:** Fixed teams can improve aggregate score and latency on sufficiently hard/decomposable sets.
- **Source role:** Vendor system cards
- **Scope conditions:** BrowseComp difficulty buckets and specific harnesses.
- **Confidence basis:** Direct reported stratified result.
- **Calculation:** 0.8x means 20% slower per easy problem relative to baseline.
- **Revision trigger:** Task-specific overhead measurements show different break-even point.

## C-013 — In the Fable BrowseComp experiment, the blocking orchestrator underperformed non-blocking fixed and async designs.

- **Epistemic status:** Vendor-reported observation
- **Direct support:** P-F5 p.270-271: blocking 89.9, fixed 10-agent 92.2, async 93.3; p.271 discusses synchronization/context costs.
- **Contrary evidence:** Opus4.8 blocking was its strongest reported setup, so the architecture effect is model/configuration-specific.
- **Source role:** Vendor system cards
- **Scope conditions:** Fable/Mythos 5 BrowseComp harness.
- **Confidence basis:** Direct exact scores and methodology.
- **Calculation:** Async - blocking = 93.3 - 89.9 = +3.4 pp.
- **Revision trigger:** Production blocking harness with persistent context shows equal reliability/value.

## C-014 — Fable/Mythos 5 five-agent ProgramBench reached 60% about 3.2x faster and finished 7.9 percentage points above solo.

- **Epistemic status:** Vendor-reported observation
- **Direct support:** P-F5 p.274, Fig. 8.15.2.A and prose.
- **Contrary evidence:** Chart annotation rounds near 3.3x; program reconstruction is one naturally decomposable benchmark; more agents use more tokens.
- **Source role:** Vendor system card
- **Scope conditions:** Five-agent fixed team, ProgramBench.
- **Confidence basis:** Direct prose and figure; rounding discrepancy preserved.
- **Calculation:** Reported directly; use 3.2x prose, not 3.3x rounded annotation.
- **Revision trigger:** Released-config replication or repository task suite.

## C-015 — Opus 5 five-agent ProgramBench reached 60% about 2.2x faster, while async reached the highest final score.

- **Epistemic status:** Vendor-reported observation
- **Direct support:** P-O5 p.166, Fig. 8.11.2.A.
- **Contrary evidence:** Pre-release model/unreleased effort; not a controller-isolation test.
- **Source role:** Vendor system card
- **Scope conditions:** ProgramBench, Opus5 multi-agent configurations.
- **Confidence basis:** Direct figure/prose.
- **Calculation:** Reported directly.
- **Revision trigger:** Released configuration or representative repo-scale replication.

## C-016 — No public Low/Medium/High/XHigh/Max sweep of the Opus 5 lead orchestrator was located in this pass.

- **Epistemic status:** Documented non-finding
- **Direct support:** P-O5 p.168 states multi-agent runs used an unreleased effort configuration; search log records targeted searches.
- **Contrary evidence:** Internal unpublished data may exist; absence from located public sources is not proof of absence.
- **Source role:** Vendor methodology + search record
- **Scope conditions:** Public evidence located by 2026-07-24.
- **Confidence basis:** Direct methodology and repeated targeted search.
- **Calculation:** Not applicable.
- **Revision trigger:** Anthropic or independent evaluator publishes lead-effort sweep.

## C-017 — Claude Code custom subagents can use a different model and effort from the lead, while agent-team teammates can use different models but inherit the lead effort.

- **Epistemic status:** Verified official implementation fact
- **Direct support:** W-CODE-SUBAGENTS Supported frontmatter fields; W-CODE-MODEL-CONFIG effort override; W-CODE-TEAMS Specify teammates and models.
- **Contrary evidence:** Feature behavior is version-dependent; environment variables can override frontmatter effort.
- **Source role:** Vendor harness documentation
- **Scope conditions:** Current Claude Code docs as of 2026-07-24; actual version must be recorded.
- **Confidence basis:** Direct configuration documentation.
- **Calculation:** Not applicable.
- **Revision trigger:** Claude Code version changes semantics.

## C-018 — Claude Code agent teams are experimental and known to have coordination/resumption/shutdown limitations.

- **Epistemic status:** Verified official implementation fact
- **Direct support:** W-CODE-TEAMS, opening section, accessed 2026-07-24.
- **Contrary evidence:** Feature may improve in later versions.
- **Source role:** Vendor harness documentation
- **Scope conditions:** Current experimental feature.
- **Confidence basis:** Direct official documentation.
- **Calculation:** Not applicable.
- **Revision trigger:** Feature graduates or documented limitations change.

## C-019 — OpenAI Responses API multi-agent is currently a beta homogeneous harness whose subagents share the request model and tools.

- **Epistemic status:** Verified official implementation fact
- **Direct support:** W-OAI-MULTI, Overview/How Multi-agent works, accessed 2026-07-24.
- **Contrary evidence:** Custom external orchestration can mix providers/models; beta semantics may change.
- **Source role:** Vendor API documentation
- **Scope conditions:** Responses API built-in multi-agent beta.
- **Confidence basis:** Direct official description.
- **Calculation:** Not applicable.
- **Revision trigger:** API adds per-subagent model/tool overrides or leaves beta.

## C-020 — CursorBench 3.2 shows Fable Max at 70.5% and $17.32/task versus Opus Max 70.0% and $8.23/task.

- **Epistemic status:** Practitioner-reported observation
- **Direct support:** W-CURSOR leaderboard, accessed 2026-07-24.
- **Contrary evidence:** Proprietary tasks, Cursor harness, no uncertainty intervals in leaderboard; 0.5pp may be noise.
- **Source role:** Practitioner/harness vendor evaluation
- **Scope conditions:** CursorBench 3.2 complete configurations.
- **Confidence basis:** Direct current leaderboard values with source incentives qualified.
- **Calculation:** Cost ratio = 17.32 / 8.23 = 2.1045 -> 2.10x; score delta = 70.5 - 70.0 = +0.5 pp.
- **Revision trigger:** Benchmark version, repeated-trial intervals, or local tasks change.

## C-021 — CursorBench 3.2 shows GPT-5.6 Sol Max at 67.2% and $5.69/task, below Opus Max score but at lower task cost.

- **Epistemic status:** Practitioner-reported observation
- **Direct support:** W-CURSOR leaderboard.
- **Contrary evidence:** Harness and prompts differ by provider; OpenAI vendor page reports other benchmark advantages.
- **Source role:** Practitioner/harness vendor evaluation
- **Scope conditions:** CursorBench 3.2.
- **Confidence basis:** Direct leaderboard values.
- **Calculation:** Cost ratio Sol Max / Opus Max = 5.69 / 8.23 = 0.6914 -> 69%; score delta = 67.2 - 70.0 = -2.8 pp.
- **Revision trigger:** Local coding tasks or new benchmark version.

## C-022 — The strongest current answer is to default to Opus 5 for most bounded production work and reserve Fable for cases where coordination topology is itself the hard part.

- **Epistemic status:** Recommendation / synthesis
- **Direct support:** C-001 to C-021, especially Opus Medium implementation peak, Opus async repair, Fable vendor delegation profile, and cost differential.
- **Contrary evidence:** Fable can win hardest-task endpoints; current independent controller evidence is immature; local work may have different failure costs.
- **Source role:** Cross-source decision synthesis
- **Scope conditions:** General first-pass policy before local validation; assumes Fable is operationally admissible.
- **Confidence basis:** Multiple source roles agree on cost and task-conditioned capability; manager-specific conclusion remains qualified.
- **Calculation:** No scalar ranking; routing is conditional.
- **Revision trigger:** Controlled same-worker local evaluation or product/pricing change.

## C-023 — Opus 5 Medium implementers under a Fable High/XHigh controller is a plausible mixed policy, not a publicly verified superiority result.

- **Epistemic status:** Recommendation / experimental hypothesis
- **Direct support:** P-O5 p.151 supports Medium implementation; W-A-FABLE supports manager specialization; W-CODE-MODEL-CONFIG permits mixed effort/model subagents.
- **Contrary evidence:** No controlled public mixed Fable-controller/Opus-worker comparison located.
- **Source role:** Synthesis across vendor evidence and harness implementation
- **Scope conditions:** Claude Code or custom harness with identical worker prompts/tools; only after privacy/availability gates.
- **Confidence basis:** Component evidence is direct; composition effect is unmeasured.
- **Calculation:** Economic hypothesis: spend Fable rates only on controller tokens.
- **Revision trigger:** Local controller-swap A/B.

## C-024 — Opus 5 High controller plus lower-cost Sonnet 5 or GPT-5.6 Terra/Luna scouts is a plausible breadth policy.

- **Epistemic status:** Recommendation / experimental hypothesis
- **Direct support:** W-A-PRICE and W-OAI-GPT56 pricing; W-CODE-SUBAGENTS mixed configuration; P-S5 worker capability evidence.
- **Contrary evidence:** Cross-provider orchestration adds transport, privacy, schema, and verification burden; cheap workers can omit sources.
- **Source role:** Economic synthesis
- **Scope conditions:** Independent retrieval/scouting tasks with controller verification.
- **Confidence basis:** Cost differential is direct; quality/value must be locally measured.
- **Calculation:** No universal cost ratio because token mix and provider differ.
- **Revision trigger:** Trace replay or local fan-out evaluation.

## C-025 — Max should not be the default effort for either Opus 5 or Fable 5.

- **Epistemic status:** Recommendation from non-monotonic evidence
- **Direct support:** C-002 to C-004; W-A-FABLE effort guidance; W-OAI-GUIDANCE recommends comparing XHigh/Max on representative workloads.
- **Contrary evidence:** CursorBench and some hard tasks peak at Max; rare severe failures may justify it.
- **Source role:** Cross-source synthesis
- **Scope conditions:** Default production routing, not capability ceiling tests.
- **Confidence basis:** Multiple official curves show plateaus/regressions and high cost.
- **Calculation:** Task-specific deltas shown in effort_curves.csv.
- **Revision trigger:** Local value-weighted curve shows Max dominates after severe-failure cost.

## C-026 — Sonnet 5 is best treated as a lower-cost worker/baseline rather than the default controller for the hardest dynamic orchestration.

- **Epistemic status:** Recommendation / inference
- **Direct support:** P-S5 task results, W-A-PRICE, CursorBench cost/score curve, lack of manager-isolation evidence.
- **Contrary evidence:** Sonnet may be sufficient for many bounded teams and can outperform older Opus on some cost frontiers.
- **Source role:** Cross-source synthesis
- **Scope conditions:** Hard dynamic orchestration; not routine teams.
- **Confidence basis:** Cost advantage direct, manager superiority absent.
- **Calculation:** Current promotional rate $2/$10 vs Opus $5/$25 and Fable $10/$50.
- **Revision trigger:** Controlled manager benchmark adds Sonnet5 and shows parity.

## C-027 — GPT-5.6 Sol is a strong cost-performance alternative for solo/controller work, but its built-in multi-agent beta is not directly comparable to Claude mixed-model subagents.

- **Epistemic status:** Synthesis
- **Direct support:** W-OAI-GPT56; W-OAI-MULTI; W-CURSOR; W-AA-OPUS5.
- **Contrary evidence:** Custom OpenAI/external harnesses can mix models; vendor benchmark tables use heterogeneous scaffolds.
- **Source role:** Vendor docs + practitioner/evaluator evidence
- **Scope conditions:** Current built-in Responses multi-agent beta and reported complete configurations.
- **Confidence basis:** Direct implementation semantics and independent-ish/practitioner scores.
- **Calculation:** See CursorBench and pricing CSVs.
- **Revision trigger:** OpenAI adds per-worker routing or controlled common-harness study.

## C-028 — Fable suitability has non-performance gates: classifiers/fallback behavior, long runtimes, and any current data-retention or availability constraints must be checked in the target account.

- **Epistemic status:** Recommendation grounded in official behavior guidance
- **Direct support:** W-A-FABLE sections on classifiers/fallback and longer turns; current product documentation should be checked at deployment.
- **Contrary evidence:** Some workloads never trigger safeguards and tolerate long turns.
- **Source role:** Vendor documentation
- **Scope conditions:** Operational deployment, especially dual-use domains and unattended runs.
- **Confidence basis:** Direct documented behaviors; account-specific rates unknown.
- **Calculation:** Not applicable.
- **Revision trigger:** Product policy, account access, fallback, or retention terms change.

## C-029 — The controlled local evaluation should hold tasks, workers, prompts, tools, budgets, concurrency, and verification constant while swapping only the controller model/effort.

- **Epistemic status:** Methodological recommendation
- **Direct support:** C-009/C-011 and AHR-C §§11.2-11.11.
- **Contrary evidence:** A fully factorial test is expensive; some controller-specific prompt tuning may be needed after a locked common-prompt phase.
- **Source role:** Methodology/governance + benchmark design
- **Scope conditions:** Evaluation intended to isolate controller quality.
- **Confidence basis:** Direct causal-identification logic.
- **Calculation:** Primary design: 4 controller cells x >=5 repeats x representative tasks, paired worker seeds.
- **Revision trigger:** Pilot shows prompt non-equivalence or budget infeasibility; preregister adaptation.

## C-030 — No controlled independent Opus 5-versus-Fable 5 manager study with identical workers was located in this pass.

- **Epistemic status:** Documented non-finding
- **Direct support:** Search log; R-CLAW lacks Opus5; vendor cards confound lead/worker.
- **Contrary evidence:** Private evaluations may exist; search was targeted, not exhaustive.
- **Source role:** Search record
- **Scope conditions:** Publicly retrievable evidence through 2026-07-24.
- **Confidence basis:** Repeated query classes across official, repository, arXiv, practitioner sources.
- **Calculation:** Not applicable.
- **Revision trigger:** New study, repository row, or disclosed internal evaluation.

# 16. Source inventory

The complete machine-readable inventory is `data/source_inventory.csv`. Load-bearing PDFs are copied into `sources/` with SHA-256 hashes; dynamic web sources have stable links and access dates.

## P-O5 — Claude Opus 5 System Card

- **Role / author:** Vendor system card / Anthropic
- **Version/date / accessed:** 2026-07-24 / 2026-07-24
- **Stable URL:** https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf
- **Local copy / hash:** sources/Claude_Opus_5_System_Card.pdf / fed3c0e6d150a6ba855f0f117a632d2b27dbb5886fd42815caa92e3e20db1d25
- **Exact locations:** pp. 148, 150-151, 158, 160, 163-168; Tables/Figures 8.1.A, 8.3.A, 8.4.A-B, 8.10.1.B, 8.10.2.B, 8.11.1.A-B, 8.11.2.A, §8.11.4
- **Incentives/conflicts:** Vendor launch document; selects evaluations and framing; product interest.
- **Dependence:** Several benchmark results incorporate external benchmark owners but are reported by Anthropic; multi-agent runs are Anthropic-controlled.
- **Access limits:** Public PDF. Multi-agent configuration was pre-release, unreleased effort, no safety classifiers; raw trajectories unavailable.
- **Source function:** Opus effort curves, orchestration, pricing-independent task profile
- **Notes:** Rendered and visually inspected locally; exact pages archived.

## P-F5 — Claude Fable 5 & Claude Mythos 5 System Card

- **Role / author:** Vendor system card / Anthropic
- **Version/date / accessed:** 2026-06 / 2026-07-24
- **Stable URL:** https://www-cdn.anthropic.com/57a52ea7d8f0e54e8a542e908266086df425cdf5/Claude%20Fable%205%20%26%20Claude%20Mythos%205%20System%20Card.pdf
- **Local copy / hash:** sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf / f95d413845ad8624f384ba026963f2bad2158f10f2626575bb45e823e3c2e0ca
- **Exact locations:** pp. 256-257, 270-276; Figs. 8.4.A-B, 8.15.1.A-C, 8.15.2.A, §§8.15.3-8.15.4
- **Incentives/conflicts:** Vendor launch document; product interest; many headline results use Mythos core model or Fable deployment layer depending section.
- **Dependence:** External benchmark references sometimes imported; orchestration experiments vendor-run.
- **Access limits:** Public PDF; raw trajectories and repeated-trial variance for multi-agent results not published.
- **Source function:** Fable effort curves, async/fixed/blocking orchestration, long-horizon claims
- **Notes:** Rendered and visually inspected locally; distinguish Fable deployment from Mythos core where relevant.

## P-O48 — Claude Opus 4.8 System Card

- **Role / author:** Vendor system card / Anthropic
- **Version/date / accessed:** 2026-05 / 2026-07-24
- **Stable URL:** https://www-cdn.anthropic.com/0b4915911bb0d19eca5b5ee635c80fef830a37ea.pdf
- **Local copy / hash:** sources/Claude_Opus_4.8_System_Card.pdf / 97f11ae3fb305c7105c958599bcf90f216669543393220f674610ddb83ee611a
- **Exact locations:** pp. 210-213; Figs. 8.11.1.A-C, 8.11.2.A
- **Incentives/conflicts:** Vendor system card; product interest.
- **Dependence:** Vendor-run multi-agent evaluation; same benchmark family as later cards but different model/configuration vintage.
- **Access limits:** Public PDF; raw trajectories unavailable.
- **Source function:** Specific Opus 4.8 async regression and ProgramBench baseline
- **Notes:** Do not generalize one async BrowseComp result to all orchestration.

## P-S5 — Claude Sonnet 5 System Card

- **Role / author:** Vendor system card / Anthropic
- **Version/date / accessed:** 2026 / 2026-07-24
- **Stable URL:** https://www-cdn.anthropic.com/480e0bb54327b9622282e9c39a83a4f490ed377e/Claude%20Sonnet%205%20System%20Card.pdf
- **Local copy / hash:** sources/Claude_Sonnet_5_System_Card.pdf / 05e46bff69885e22af07efda202ea323c4bffc4453250d2041003fba9505e2c4
- **Exact locations:** pp. 115-123, 135-136
- **Incentives/conflicts:** Vendor system card; product interest.
- **Dependence:** Some external evaluation rows; vendor-selected comparisons.
- **Access limits:** Public PDF; no public Sonnet-5 controller-isolation study located.
- **Source function:** Sonnet worker/baseline profile
- **Notes:** Rendered and visually inspected locally.

## W-A-FABLE — Prompting Claude Fable 5

- **Role / author:** Vendor web documentation / Anthropic
- **Version/date / accessed:** dynamic / 2026-07-24
- **Stable URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5
- **Local copy / hash:** stable link only / not captured; dynamic page
- **Exact locations:** Sections Capability improvements; Longer turns by default; Ground progress claims during long runs; Parallel subagents
- **Incentives/conflicts:** Official behavior guidance and product positioning; not independent evaluation.
- **Dependence:** May summarize internal testing and early testers without methods.
- **Access limits:** Dynamic page can change silently; accessed date recorded.
- **Source function:** Vendor claim that Fable sustains subagents; long-run controls
- **Notes:** Use as declared behavior/guidance, not proof of comparative production reliability.

## W-A-OPUS — Prompting Claude Opus 5

- **Role / author:** Vendor web documentation / Anthropic
- **Version/date / accessed:** dynamic / 2026-07-24
- **Stable URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- **Local copy / hash:** stable link only / not captured; dynamic page
- **Exact locations:** Sections Task scope and over-verification; Controlling subagent spawning; Self-correction; Multi-agent coordination
- **Incentives/conflicts:** Official behavior guidance; product interest.
- **Dependence:** Internal observations without full public methods.
- **Access limits:** Dynamic page; accessed date recorded.
- **Source function:** Opus over-verification/scope/spawn controls
- **Notes:** Supports harness controls, not universal behavior rates.

## W-A-PRICE — Pricing

- **Role / author:** Vendor web documentation / Anthropic
- **Version/date / accessed:** dynamic / 2026-07-24
- **Stable URL:** https://platform.claude.com/docs/en/about-claude/pricing
- **Local copy / hash:** stable link only / not captured; dynamic page
- **Exact locations:** Page title Pricing; model pricing table
- **Incentives/conflicts:** Official commercial pricing; authoritative for listed rates, not total workflow value.
- **Dependence:** None for declared prices.
- **Access limits:** Prices/promotions can change; date-sensitive.
- **Source function:** Token-rate calculations
- **Notes:** All rates USD per million tokens.

## W-CODE-AGENTS — Run agents in parallel

- **Role / author:** Vendor harness documentation / Anthropic
- **Version/date / accessed:** dynamic / 2026-07-24
- **Stable URL:** https://code.claude.com/docs/en/agents
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Section Choose an approach / comparison of subagents, agent view, agent teams, workflows
- **Incentives/conflicts:** Official product documentation; encourages use of Claude Code features.
- **Dependence:** Describes intended behavior, not comparative model quality.
- **Access limits:** Dynamic; version-dependent.
- **Source function:** Harness taxonomy
- **Notes:** Useful for architecture selection.

## W-CODE-SUBAGENTS — Create custom subagents

- **Role / author:** Vendor harness documentation / Anthropic
- **Version/date / accessed:** Claude Code current as of access / 2026-07-24
- **Stable URL:** https://code.claude.com/docs/en/sub-agents
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Introduction; Supported frontmatter fields; concurrency/context/resume sections
- **Incentives/conflicts:** Official product documentation.
- **Dependence:** Implementation behavior may change by Claude Code version.
- **Access limits:** Dynamic; local version should be recorded in an actual experiment.
- **Source function:** Separate contexts, model/tool permissions, mixed worker configuration
- **Notes:** Pair with model-config page for effort override.

## W-CODE-MODEL-CONFIG — Model configuration

- **Role / author:** Vendor harness documentation / Anthropic
- **Version/date / accessed:** dynamic / 2026-07-24
- **Stable URL:** https://code.claude.com/docs/en/model-config
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Section Configure effort level / Skill and subagent frontmatter
- **Incentives/conflicts:** Official product documentation.
- **Dependence:** Version-dependent feature.
- **Access limits:** Dynamic; Max/ultracode session-only and precedence rules apply.
- **Source function:** Per-subagent effort override in mixed policy
- **Notes:** Record actual Claude Code version in local evaluation.

## W-CODE-TEAMS — Orchestrate teams of Claude Code sessions

- **Role / author:** Vendor harness documentation / Anthropic
- **Version/date / accessed:** experimental feature / 2026-07-24
- **Stable URL:** https://code.claude.com/docs/en/agent-teams
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Experimental status; Specify teammates and models; Best practices; Choose team size
- **Incentives/conflicts:** Official experimental product documentation.
- **Dependence:** Behavior and limitations are version-dependent.
- **Access limits:** Experimental; known resumption, coordination, shutdown limitations.
- **Source function:** Peer-team model/effort inheritance, 3-5 team-size guardrail
- **Notes:** Teammates can use specified models but inherit lead effort.

## W-CODE-WORKFLOWS — Orchestrate subagents at scale with dynamic workflows

- **Role / author:** Vendor harness documentation / implementation artifact description / Anthropic
- **Version/date / accessed:** requires Claude Code v2.1.154+ / 2026-07-24
- **Stable URL:** https://code.claude.com/docs/en/workflows
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Introduction; How a workflow runs; Behavior and limits; Cost
- **Incentives/conflicts:** Official feature documentation.
- **Dependence:** Version and product-surface dependent.
- **Access limits:** Dynamic page; workflow runtime constraints may change.
- **Source function:** Script-backed fan-out, context isolation, scale limits
- **Notes:** Better for repeatable high-volume stages than free-form manager conversations.

## W-OAI-GPT56 — GPT-5.6: Frontier intelligence that scales with your ambition

- **Role / author:** Vendor launch/evaluation page / OpenAI
- **Version/date / accessed:** 2026-07-24 / 2026-07-24
- **Stable URL:** https://openai.com/index/gpt-5-6/
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Sections coding, end-to-end knowledge work, availability and pricing, benchmark tables
- **Incentives/conflicts:** Vendor launch page; curated benchmark mix and partner quotes; strong product interest.
- **Dependence:** Some scores from partner/third-party benchmarks; harness conditions differ.
- **Access limits:** Raw traces mostly unavailable; benchmark table cannot be treated as one controlled comparison.
- **Source function:** Sol cross-comparison, pricing, current availability, multi-agent beta
- **Notes:** Use official facts for declared behavior and label performance as vendor-reported.

## W-OAI-GUIDANCE — Model guidance

- **Role / author:** Vendor API documentation / OpenAI
- **Version/date / accessed:** dynamic / 2026-07-24
- **Stable URL:** https://developers.openai.com/api/docs/guides/latest-model
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** GPT-5.6 key features; Max reasoning effort; Multi-agent beta
- **Incentives/conflicts:** Official guidance; product interest.
- **Dependence:** Dynamic implementation.
- **Access limits:** Beta multi-agent semantics may change.
- **Source function:** Sol effort and multi-agent route
- **Notes:** Officially recommends comparing Max and XHigh on representative workloads.

## W-OAI-MULTI — Multi-agent

- **Role / author:** Vendor API documentation / OpenAI
- **Version/date / accessed:** beta / 2026-07-24
- **Stable URL:** https://developers.openai.com/api/docs/guides/responses-multi-agent
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Overview; When to use Multi-agent; How Multi-agent works
- **Incentives/conflicts:** Official beta documentation.
- **Dependence:** All subagents share request model/tools, limiting mixed-model attribution.
- **Access limits:** Beta; no controlled public Fable/Opus cross-provider manager test.
- **Source function:** OpenAI harness contrast
- **Notes:** Useful homogeneous alternative when independent workstreams divide cleanly.

## W-AA-OPUS5 — Opus 5: Fable 5 level intelligence at a lower cost per task

- **Role / author:** Independent evaluator with pre-release vendor support / Artificial Analysis
- **Version/date / accessed:** 2026-07-24 / 2026-07-24
- **Stable URL:** https://artificialanalysis.ai/articles/opus-5
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Opening summary and key takeaways
- **Incentives/conflicts:** Commercial evaluator; received pre-release support from Anthropic; independence qualified.
- **Dependence:** Uses Artificial Analysis benchmark suite and cost model; some shared benchmark inputs with vendor narratives.
- **Access limits:** Not a controller-isolation study; raw full trajectories not all public.
- **Source function:** Independent-ish solo cost/intelligence cross-check
- **Notes:** Supports economic parity direction, not orchestration ranking.

## W-CURSOR — CursorBench 3.2

- **Role / author:** Practitioner/implementation evaluation / Cursor
- **Version/date / accessed:** 3.2; current on access / 2026-07-24
- **Stable URL:** https://cursor.com/cursorbench
- **Local copy / hash:** stable link only / not captured
- **Exact locations:** Leaderboard table, methodology, changelog
- **Incentives/conflicts:** Harness vendor evaluating models used/sold in its product; proprietary tasks.
- **Dependence:** Complete model+harness configurations; not model-only.
- **Access limits:** No public per-task raw trajectories in this pass; uncertainty intervals not shown in leaderboard.
- **Source function:** Effort-cost curve cross-check and Sol/Sonnet alternatives
- **Notes:** Treat small score gaps cautiously.

## R-CLAW — ClawArena-Team README at commit 630efd8a0d1dc8189718226c7da158cbe4c2fe64

- **Role / author:** Independent implementation artifact / benchmark repository / Aiming Lab / ClawArena authors
- **Version/date / accessed:** commit 630efd8a0d1dc8189718226c7da158cbe4c2fe64 / 2026-07-24
- **Stable URL:** https://github.com/aiming-lab/ClawArena/blob/630efd8a0d1dc8189718226c7da158cbe4c2fe64/ClawArena-Team/README.md
- **Local copy / hash:** stable commit link only / not captured
- **Exact locations:** README lines 8-41: overview, fixed worker pool, leaderboard, single-run and fallback notes
- **Incentives/conflicts:** Benchmark authors; benchmark is procedurally generated/authored partly by the capability it measures.
- **Dependence:** One reported run per manager; Fable condition used recommended refusal fallback to Opus 4.8; no Opus 5 row.
- **Access limits:** Cannot settle Fable vs Opus 5; repository clone failed in local environment, pinned raw file inspected via web.
- **Source function:** Design of manager-isolation evaluation and evidence gap
- **Notes:** Strong methodological inspiration, weak direct ranking evidence for current question.

## AHR-C — Agentic Harness Research Constitution

- **Role / author:** Project methodology/governance / Project owner
- **Version/date / accessed:** 2.0, adopted 2026-07-18 / 2026-07-24
- **Stable URL:** user-supplied project source
- **Local copy / hash:** sources/AHR-C_v2.0_Adopted_Constitution.md / to be computed in manifest
- **Exact locations:** §§3-7, 8, 10-13
- **Incentives/conflicts:** Methodological authority for this project, not external factual evidence.
- **Dependence:** None for external claims.
- **Access limits:** User-supplied; cannot support empirical model claims.
- **Source function:** Audit method, epistemic statuses, evaluation design, verification
- **Notes:** Cite as [AHR-C §...] only for methodology.

# 17. Search trail

- **S-001 [Official model cards]** `Claude Opus 5 / Fable 5 / Opus 4.8 / Sonnet 5 system card PDFs` — Result: Four official PDFs retrieved, hashed, rendered, and inspected. Disposition: Load-bearing Failure/gap: web.open/web.screenshot on official PDF URLs returned (400) OK; local download/render used instead. Impact: No substantive evidence loss; exact pages preserved locally.
- **S-002 [Effort settings]** `Opus 5 Fable 5 Low Medium High XHigh Max benchmark curves` — Result: Five effort curves transcribed for Opus/Fable; no lead-orchestrator effort sweep. Disposition: Load-bearing for task curves Failure/gap: Lead effort remains missing; effort is behavioral, not a strict token budget. Impact: Controller effort recommendations remain provisional.
- **S-003 [Orchestration]** `Opus 5 Fable 5 BrowseComp async fixed peer blocking orchestrator ProgramBench` — Result: Exact scores/methodology located. Disposition: Load-bearing Failure/gap: Raw trajectories/variance/lead work share unavailable. Impact: Can compare configurations within cards, not isolate causal manager quality.
- **S-004 [Controller isolation]** `Fable 5 Opus 5 manager benchmark identical workers controller swap` — Result: ClawArena-Team manager-isolation design found; no Opus5 row. Disposition: Methodological load-bearing, ranking non-load-bearing Failure/gap: One run, fallback, synthetic/procedural tasks, no Opus5. Impact: Independent evidence is insufficient to rank current controllers.
- **S-005 [Repositories]** `ClawArena Team repository fixed workers manager leaderboard` — Result: README inspected at commit 630efd8a0d1dc8189718226c7da158cbe4c2fe64. Disposition: Included with limitations Failure/gap: Local git clone failed: DNS could not resolve github.com. Impact: Pinned raw file still supplied implementation evidence; no code execution attempted.
- **S-006 [Independent evaluation]** `Opus 5 Fable 5 Artificial Analysis cost per task intelligence` — Result: Release-day article and headline scores/costs located. Disposition: Qualified independent evaluator Failure/gap: Evaluator had pre-release vendor support; not orchestration-specific. Impact: Useful solo economics cross-check only.
- **S-007 [Practitioner coding]** `CursorBench 3.2 Opus 5 Fable 5 Sonnet 5 GPT-5.6 Sol effort cost score` — Result: Current leaderboard values and methods located. Disposition: Included as practitioner/harness evaluation Failure/gap: Proprietary tasks, no visible confidence intervals/raw traces. Impact: Supports cost/effort shape; small gaps treated cautiously.
- **S-008 [Claude behavior guidance]** `Prompting Claude Fable 5 delegation long-running subagents effort` — Result: Exact sections on delegation, long turns, progress grounding, async subagents. Disposition: Load-bearing vendor guidance Failure/gap: No independent effect sizes. Impact: Fable-manager conclusion flagged vendor-only/inference.
- **S-009 [Claude behavior guidance]** `Prompting Claude Opus 5 over-verification scope subagent spawning` — Result: Exact sections located. Disposition: Load-bearing harness controls Failure/gap: Behavior rates not quantified publicly. Impact: Used for guardrails, not prevalence.
- **S-010 [Claude harnesses]** `Claude Code subagents agent teams dynamic workflows model effort overrides` — Result: Taxonomy, experimental team limits, model/effort inheritance, workflow behavior located. Disposition: Load-bearing implementation facts Failure/gap: Dynamic docs and version dependence. Impact: Local eval protocol records exact Claude Code version.
- **S-011 [OpenAI comparison]** `GPT-5.6 Sol official model guidance pricing multi-agent beta` — Result: Current launch, model guidance, model page, and multi-agent docs located. Disposition: Load-bearing for Sol cross-comparison Failure/gap: Vendor benchmark mix uses different harnesses; beta multi-agent homogeneous. Impact: Sol treated as alternative complete configuration, not one-to-one manager ranking.
- **S-012 [Practitioner mixed team]** `Fable orchestrator Sonnet workers 96% score 46% cost` — Result: Vendor/practitioner post signal located. Disposition: Community/practitioner signal only; excluded from load-bearing conclusions Failure/gap: Full configuration, task distribution, raw data, repeated trials not recoverable. Impact: Used only to motivate mixed-policy test, not claim superiority.
- **S-013 [Advisor claims]** `Fable advisor 92% 63% Opus advisor benchmark` — Result: No primary source meeting citation standard located. Disposition: Excluded Failure/gap: Claim provenance/configuration missing. Impact: Not included in conclusions.
- **S-014 [Lead-worker effort matrix]** `Opus 5 controller effort worker effort Low Medium High XHigh Max multi-agent sweep` — Result: Opus low-effort worker async cell found; no full matrix. Disposition: Partial evidence Failure/gap: Most cells missing. Impact: Separate lead and worker effort in routing table; mark missing cells.
- **S-015 [Mixed-model public studies]** `Fable controller Opus 5 Medium workers controlled evaluation` — Result: No controlled public study located. Disposition: Documented non-finding Failure/gap: Private/internal evaluations inaccessible. Impact: Mixed policies explicitly labelled experiments.
- **S-016 [PDF retrieval]** `Open official system card PDF in web tool and screenshot pages` — Result: Tool returned (400) OK for direct PDF open. Disposition: Tool failure, not evidence absence Failure/gap: Web PDF screenshot unavailable. Impact: Downloaded official PDFs to sandbox; rendered with pdfium and inspected.
- **S-017 [arXiv full PDF]** `ClawArena-Team arXiv PDF` — Result: Local download failed due DNS/network resolution. Disposition: Tool failure; HTML abstract and pinned repo inspected Failure/gap: Full PDF not archived locally. Impact: Repository artifact used for exact design; paper claims not overextended.
- **S-018 [Search stopping]** `Additional generic versus pages, affiliate comparisons, unsourced social rankings` — Result: Low-method sources screened and rejected. Disposition: Excluded Failure/gap: Search not exhaustive by design. Impact: Stopped when load-bearing questions had direct evidence or documented gaps.

**Stopping rule:** searching stopped when each load-bearing question had either direct primary/methodologically disclosed evidence plus limiting evidence, or a documented non-finding whose resolution requires local/private data. Additional generic versus pages and unsourced commentary were unlikely to improve the decision and risked replacing missing evidence with source volume [AHR-C §§6.5-6.6, 7.2-7.5].

# 18. Artifact map

- `report/Fable_5_vs_Opus_5_Decision_Report.pdf` — final report.
- `report/Fable_5_vs_Opus_5_Decision_Report.docx` — editable report.
- `report/Fable_5_vs_Opus_5_Decision_Report.md` — source report with relative links.
- `Fable_5_vs_Opus_5_Audit_Workbook.xlsx` — routing, claims, sources, curves, calculations, search, evaluation design.
- `data/` — CSV/JSON chart data and ledgers.
- `charts/` — effort/orchestration/cost charts.
- `local_eval/` — runnable controller-isolation harness and synthetic control-plane fixture output.
- `sources/` — copied system cards, AHR-C, and SHA-256 manifest; web sources are stable links in the inventory.
- `evidence_pages/png/` — rendered exact source pages used for visual verification.