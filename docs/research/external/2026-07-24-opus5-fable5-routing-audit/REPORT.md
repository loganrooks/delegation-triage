# Opus 5 versus Fable 5: orchestration, effort scaling, and routing

**Version:** 2.0 — audit-ready revision  
**Status:** Supersedes the earlier uncited report  
**Evidence cutoff:** 24 July 2026  
**Executing model:** GPT-5.6 Thinking  
**Core evidence:** Anthropic system cards and official model documentation  
**Independent evidence:** No controlled independent Opus 5–Fable 5 orchestration study was located in this pass  
**Decision unit:** model–effort–harness–worker-mix–task combination

> **Correction and audit note.** The earlier downloadable report was not adequately grounded. It listed sources but did not attach exact pages, figures, and source roles to its load-bearing claims. This revision adds inline page/figure citations, local copies of the three source PDFs, rendered source pages, a claim ledger, provenance-bearing CSV data, and explicit labels for inference and recommendation.

## Citation key

- **O5-SC** — *Claude Opus 5 System Card*, Anthropic, 24 July 2026.
- **O48-SC** — *Claude Opus 4.8 System Card*, Anthropic, May 2026.
- **F5-SC** — *Claude Fable 5 & Claude Mythos 5 System Card*, Anthropic, June 2026.
- **O5-PG** — official Anthropic page, *Prompting Claude Opus 5*.
- **F5-PG** — official Anthropic page, *Prompting Claude Fable 5*.
- **PRICE** — official Anthropic pricing page.

Every quantitative claim below links to an exact PDF page and figure. The adjacent **page image** link opens the rendered page directly. The complete source PDFs and checksums are listed in [SOURCE_INVENTORY.md](SOURCE_INVENTORY.md).

---

# 1. Best current answer

## 1.1 What is established

**Verified vendor-reported result:** Opus 5 no longer displays the specific asynchronous-orchestration regression reported for Opus 4.8 on BrowseComp.

- Opus 4.8: 84.3% as a 10M-token single agent versus 83.0% with asynchronous subagents. The rounded labels imply **−1.3 percentage points**. [O48-SC p. 210, Fig. 8.11.1.A](sources/Claude_Opus_4.8_System_Card.pdf#page=210) · [page image](evidence/opus48-p210.png)
- Fable/Mythos 5: 88.0% as a 10M-token single agent versus 93.3% with asynchronous subagents, a **+5.3-point** gain. [F5-SC p. 272, Fig. 8.15.1.A](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=272) · [page image](evidence/fable5-p272.png)
- Opus 5: 90.5% as a 10M-token single agent versus 93.4% with asynchronous subagents. The rounded chart labels imply **+2.9 points**; Anthropic’s accompanying prose reports **+2.8 points**, likely because it used unrounded values. [O5-SC pp. 163–164, Figs. 8.11.1.A–B](sources/Claude_Opus_5_System_Card.pdf#page=163) · [p. 163 image](evidence/opus5-p163.png) · [p. 164 image](evidence/opus5-p164.png)

![BrowseComp async uplift](assets/browsecomp_async_uplift_audited.png)

**Verified vendor-reported result:** On this search benchmark, Opus 5’s async system reaches essentially the same endpoint as Fable/Mythos 5: 93.4% versus 93.3%. Because the results come from separate cards and configurations, the 0.1-point difference is not a defensible superiority claim. [O5-SC p. 163](sources/Claude_Opus_5_System_Card.pdf#page=163) · [F5-SC p. 272](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=272)

## 1.2 What is inferred rather than established

**Inference:** Opus 5 looks like a stronger **manager–worker hybrid**, whereas Fable 5 still looks more specialized for extracting value from extensive distributed work.

Why that reading is plausible:

1. Opus 5 begins from a higher single-agent BrowseComp baseline, 90.5% versus Fable/Mythos 5’s 88.0%, yet both finish around 93.3–93.4% with async subagents. [O5-SC p. 163](sources/Claude_Opus_5_System_Card.pdf#page=163) · [F5-SC p. 272](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=272)
2. Fable/Mythos 5 receives the larger marginal gain from asynchronous organization, +5.3 points versus approximately +2.8/+2.9 for Opus 5. Same sources.
3. On ProgramBench, Fable/Mythos 5’s five-agent team is reported to reach the 60% threshold 3.2× faster and finish 7.9 points above the solo system, while Opus 5’s five-agent team reaches the threshold 2.2× faster and the async lead ultimately reaches the highest final score. [F5-SC p. 276, Fig. 8.15.2.A](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=276) · [page image](evidence/fable5-p276.png); [O5-SC p. 166, Fig. 8.11.2.A](sources/Claude_Opus_5_System_Card.pdf#page=166) · [page image](evidence/opus5-p166.png)
4. Anthropic’s official model guidance describes Fable as “significantly more dependable” at dispatching and sustaining parallel subagents, while the Opus 5 guide says it coordinates teams well but delegates more readily than prior models and may need deterministic spawning caps. [F5-PG, “Capability improvements,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) · [O5-PG, “Multi-agent coordination” and “Controlling subagent spawning,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

**Competing reading:** The larger Fable uplift may partly reflect its lower solo baseline, different card vintage, different effort/configuration, or benchmark-specific search behavior. The public evidence does not isolate the lead model while holding worker model, prompts, tools, and budgets constant. Therefore, “Fable is the better orchestrator” remains a conditional interpretation, not a verified general fact.

## 1.3 Provisional routing conclusion

**Recommendation, not a measured universal ranking:**

- **Opus 5 Medium** — default candidate for bounded implementation work with clear tests.
- **Opus 5 High** — initial candidate for bounded orchestration: known decomposition, two to four independent workstreams, explicit integration point.
- **Opus 5 XHigh** — difficult debugging, repository-wide investigation, dynamic replanning, or recovery after failed trajectories.
- **Fable 5 High/XHigh** — long-lived teams, evolving work graphs, repeated inter-agent communication, days-scale projects, or cases where preserving the controller role is itself important.
- **Solo execution** — preferred when the task is tightly coupled or too small to repay delegation overhead.

These routes are conditional hypotheses derived from vendor evaluations and official behavior guidance. They require local validation before becoming a production routing policy.

---

# 2. What “orchestration” means in the cited evaluations

The reports evaluate different harness structures; they should not be collapsed into one generic “multi-agent” category.

## 2.1 Fixed N-agent peer team

In the Opus 5 card, five or ten peer agents work concurrently. A designated lead coordinates and submits the result, but every agent sees the full task and has identical tools. On ProgramBench, each agent works in its own repository checkout and can share code through Git. [O5-SC pp. 167–168, §8.11.3](sources/Claude_Opus_5_System_Card.pdf#page=167) · [p. 167 image](evidence/opus5-p167.png) · [p. 168 image](evidence/opus5-p168.png)

The Fable/Mythos 5 card defines a similar three-, five-, or ten-agent peer-team harness. [F5-SC pp. 277–278, §8.15.3](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=277) · [p. 277 image](evidence/fable5-p277.png) · [p. 278 image](evidence/fable5-p278.png)

**Interpretive limit:** A strong fixed-team result is not pure evidence of lead-agent managerial ability because the harness supplies the team size and every peer has the full task.

## 2.2 Asynchronous lead with long-lived subagents

In the Opus 5 harness, the lead retains task tools, can spawn long-lived subagents without blocking, can check their status and delete them, and receives worker results as messages. Workers see only the instructions supplied by the lead rather than the original task. [O5-SC p. 168, §8.11.3](sources/Claude_Opus_5_System_Card.pdf#page=168) · [page image](evidence/opus5-p168.png)

The Fable/Mythos 5 async harness is similar, but its ProgramBench configuration caps concurrency at four subagents and twenty subagents total; BrowseComp has no such cap. [F5-SC p. 278, §8.15.3](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=278) · [page image](evidence/fable5-p278.png)

This is the most relevant public setup for the concern that Opus 4.8 “did everything itself,” because the lead may either delegate or retain direct access to the work.

## 2.3 Blocking orchestrator

The Fable/Mythos 5 blocking orchestrator has no task tools of its own and must wait for dispatched subagents. [F5-SC p. 277, §8.15.3](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=277) · [page image](evidence/fable5-p277.png)

Its lower performance than the non-blocking designs is therefore evidence about the **harness architecture**, not simply model intelligence. Anthropic attributes the disadvantage to synchronization barriers and repeated context establishment. [F5-SC p. 273](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=273) · [page image](evidence/fable5-p273.png)

---

# 3. BrowseComp: exact results and interpretation

## 3.1 Absolute results

| Model | 10M single agent | Async lead + subagents | Best fixed peer team | Blocking orchestrator |
|---|---:|---:|---:|---:|
| Opus 4.8 | 84.3 | 83.0 | 85.4 | 88.5 |
| Fable/Mythos 5 | 88.0 | 93.3 | 92.2 | 89.9 |
| Opus 5 | 90.5 | 93.4 | 93.6 | not reported |

Sources: [O48-SC p. 210, Fig. 8.11.1.A](sources/Claude_Opus_4.8_System_Card.pdf#page=210); [F5-SC p. 272, Fig. 8.15.1.A](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=272); [O5-SC p. 163, Fig. 8.11.1.A](sources/Claude_Opus_5_System_Card.pdf#page=163).

![BrowseComp absolute performance](assets/browsecomp_absolute_audited.png)

## 3.2 What changed from Opus 4.8

The Opus 4.8 async lead scored below its own 10M solo baseline, while its fixed five-agent and blocking orchestrator configurations scored above it. [O48-SC pp. 210–211](sources/Claude_Opus_4.8_System_Card.pdf#page=210) · [p. 210 image](evidence/opus48-p210.png) · [p. 211 image](evidence/opus48-p211.png)

That supports a narrower statement than “Opus 4.8 was bad at orchestration”:

> Opus 4.8’s flexible async-lead configuration did not convert delegation into additional BrowseComp accuracy, despite other more constrained multi-agent structures producing gains.

The model’s official prompting guide also said Opus 4.8 favored reasoning over tool calls and tended to spawn fewer subagents by default. [O48-PG, “Tool use triggering” and “Controlling subagent spawning,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)

## 3.3 Opus 5’s repaired profile

Opus 5’s async lead scores 93.4%, above its 90.5% solo baseline; its low-effort async workers still score 92.0%. [O5-SC p. 163, Fig. 8.11.1.A](sources/Claude_Opus_5_System_Card.pdf#page=163) · [page image](evidence/opus5-p163.png)

Anthropic reports that every tested Opus 5 multi-agent variant matches or exceeds the best solo variant and that the ten-agent team reaches 93.6%. [O5-SC p. 164](sources/Claude_Opus_5_System_Card.pdf#page=164) · [page image](evidence/opus5-p164.png)

**Verified conclusion:** The earlier negative async result is not reproduced.

**Unknown:** The cards do not report how much task work the lead itself performed, how often it duplicated worker work, or whether its delegations were well calibrated.

## 3.4 Why the result does not prove equivalence with Fable

The Opus 5 section used a **pre-release model configuration, an unreleased effort configuration, and no safeguards classifiers**. Anthropic says the numbers are useful for relative rather than absolute comparisons among its Opus 5 harnesses. [O5-SC p. 168, §8.11.4](sources/Claude_Opus_5_System_Card.pdf#page=168) · [page image](evidence/opus5-p168.png)

The Fable results were gathered in another card with its own harness limits and maximum-effort settings. [F5-SC pp. 277–278](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=277)

Therefore, comparing 93.4 to 93.3 is useful as an approximate signal, but not as a controlled one-decimal ranking.

---

# 4. ProgramBench: a different orchestration profile

ProgramBench contains 200 program-reconstruction tasks. Both cards exclude 34 tasks whose reference binaries score below 0.9, leaving 166 “golden” tasks. [O5-SC p. 165](sources/Claude_Opus_5_System_Card.pdf#page=165) · [page image](evidence/opus5-p165.png); [F5-SC pp. 275–276](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=275) · [p. 275 image](evidence/fable5-p275.png)

## 4.1 Opus 4.8

The three-agent team reaches a 60% hidden-test pass rate about **1.8× faster** than the solo system. The async curve lies between the fixed team and single agent. [O48-SC p. 213, Fig. 8.11.2.A](sources/Claude_Opus_4.8_System_Card.pdf#page=213) · [page image](evidence/opus48-p213.png)

## 4.2 Fable/Mythos 5

The five-agent team:

- reaches the 60% threshold **3.2× faster**;
- finishes **7.9 percentage points higher** than the solo system.

[F5-SC p. 276, Fig. 8.15.2.A](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=276) · [page image](evidence/fable5-p276.png)

## 4.3 Opus 5

The five-agent team:

- reaches the same 60% threshold **2.2× faster**;
- leads earlier in the trajectory;
- while the async-subagent curve ultimately reaches the highest final score.

[O5-SC p. 166, Fig. 8.11.2.A](sources/Claude_Opus_5_System_Card.pdf#page=166) · [page image](evidence/opus5-p166.png)

## 4.4 Interpretation

**Inference:** Fable/Mythos 5 shows the clearer gain from fixed parallelism on this naturally decomposable coding benchmark. Opus 5 shows competent parallel speedup plus strong late integration by the async lead.

**Alternative explanations and limits:**

- The compared team sizes differ from Opus 4.8’s.
- The cards use separate model vintages and configurations.
- The curves do not isolate the coordinator from the workers.
- Program reconstruction is only one kind of implementation orchestration.
- More agents consume more total tokens; the latency improvement is not a free efficiency gain. Opus 5 explicitly shows the score–token tradeoff on p. 167; Fable shows it on p. 277. [O5-SC p. 167](sources/Claude_Opus_5_System_Card.pdf#page=167) · [F5-SC p. 277](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=277)

---

# 5. Effort-performance profile

The effort graphs below are reconstructed from the numeric labels in the official Opus 5 system-card figures. They are normalized within each task because the benchmarks use different scales. The underlying transcribed values and exact source references are in [assets/effort_values_with_provenance.csv](assets/effort_values_with_provenance.csv).

![Opus 5 effort profile](assets/opus5_effort_profile_audited.png)

![Fable/Mythos 5 effort profile](assets/fable5_effort_profile_audited.png)

## 5.1 Opus 5: Medium can outperform higher efforts on implementation

FrontierCode Main:

| Effort | Low | Medium | High | XHigh | Max |
|---|---:|---:|---:|---:|---:|
| Opus 5 | 41.9 | **53.4** | 48.0 | 43.6 | 48.0 |

FrontierCode Extended:

| Effort | Low | Medium | High | XHigh | Max |
|---|---:|---:|---:|---:|---:|
| Opus 5 | 55.8 | **63.6** | 58.5 | 56.9 | 58.9 |

[O5-SC p. 151, Figs. 8.4.A–B](sources/Claude_Opus_5_System_Card.pdf#page=151) · [page image](evidence/opus5-p151.png)

**Verified result:** On these autonomous patch-generation tasks, the relationship between effort and score is sharply non-monotonic.

**Interpretation, not directly measured:** Higher effort may increase reconsideration, scope expansion, redesign, or over-verification. This reading is consistent with Anthropic’s official guidance that Opus 5 verifies without prompting, can expand scope, and can waste tokens when legacy verification scaffolding remains. [O5-PG, “Task scope and over-verification” and “Self-correction,” accessed 24 July 2026](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

## 5.2 Long-horizon coding improves through XHigh, then slightly regresses

DeepSWE 1.1:

| Effort | Low | Medium | High | XHigh | Max |
|---|---:|---:|---:|---:|---:|
| Opus 5 | 57.7 | 66.9 | 68.0 | **69.7** | 68.8 |
| Fable 5 | 59.6 | 65.4 | 68.6 | **69.9** | 69.7 |

[O5-SC p. 150, Fig. 8.3.A](sources/Claude_Opus_5_System_Card.pdf#page=150) · [page image](evidence/opus5-p150.png)

This supports XHigh for capability-sensitive long-horizon coding, but not a blanket Max default.

## 5.3 Search mostly plateaus by High

BrowseComp at a fixed 10M-token budget:

| Model | Low | Medium | High | XHigh | Max |
|---|---:|---:|---:|---:|---:|
| Opus 5 | 84.4 | 88.9 | 90.2 | 90.7 | 90.8 |
| Fable/Mythos 5 | 83.0 | 87.1 | 87.3 | 88.0 | 88.0 |

[O5-SC p. 160, Fig. 8.10.2.B](sources/Claude_Opus_5_System_Card.pdf#page=160) · [page image](evidence/opus5-p160.png)

For Opus 5, High captures most of the reported gain. XHigh and Max add only 0.5 and 0.6 points over High while costing more in the card’s price axis.

## 5.4 Reasoning without tools peaks around XHigh

HLE without tools:

| Model | Low | Medium | High | XHigh | Max |
|---|---:|---:|---:|---:|---:|
| Opus 5 | 47.8 | 54.2 | 56.0 | **56.4** | 56.3 |
| Fable 5 | 50.3 | 53.6 | 54.4 | **57.8** | 56.5 |

[O5-SC p. 158, Fig. 8.10.1.B](sources/Claude_Opus_5_System_Card.pdf#page=158) · [page image](evidence/opus5-p158.png)

Again, Max is not uniformly best.

## 5.5 What the effort evidence does not establish

The published Opus 5 multi-agent section does **not** provide a clean Low/Medium/High/XHigh/Max sweep of the **lead orchestrator**. Its principal runs use an unreleased pre-release effort configuration. [O5-SC p. 168](sources/Claude_Opus_5_System_Card.pdf#page=168)

Therefore:

- “Opus 5 Medium is a strong implementer” is directly supported on some coding tasks.
- “Opus 5 Medium is the best orchestrator” is not established.
- High as the bounded-controller default and XHigh for difficult orchestration are provisional routing inferences.

---

# 6. Task-conditional performance profile

The table separates direct evidence from routing judgment.

| Task/workflow | Evidence-backed profile | Provisional route | Confidence |
|---|---|---|---|
| Contained autonomous implementation | Opus 5 Medium leads its own higher efforts on both FrontierCode sets. [O5-SC p. 151](sources/Claude_Opus_5_System_Card.pdf#page=151) | Opus 5 Medium; escalate after failed tests or unresolved ambiguity | Moderate |
| Long-horizon coding | Opus 5 and Fable peak around XHigh on DeepSWE; Fable narrowly leads. [O5-SC p. 150](sources/Claude_Opus_5_System_Card.pdf#page=150) | Opus 5 High/XHigh; Fable XHigh when the project is also organizationally complex | Moderate |
| Bounded search fan-out | Both async systems reach ~93.3–93.4 on separate BrowseComp cards. [O5-SC p. 163](sources/Claude_Opus_5_System_Card.pdf#page=163); [F5-SC p. 272](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=272) | Opus 5 High lead with lower-effort workers | Moderate |
| Hard-tail search | Fable reports multi-agent latency gains concentrated on difficult problems; Opus 4.8 reports a similar hard-tail pattern. [F5-SC p. 274](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=274); [O48-SC pp. 211–212](sources/Claude_Opus_4.8_System_Card.pdf#page=211) | Fan out only when difficulty or breadth justifies coordination overhead | Moderate |
| Large parallel program reconstruction | Fable’s five-agent team shows 3.2× threshold speedup and +7.9 pp final gain; Opus 5 shows 2.2× and strong async final integration. [F5-SC p. 276](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=276); [O5-SC p. 166](sources/Claude_Opus_5_System_Card.pdf#page=166) | Fable controller for maximal distributed throughput; Opus workers | Low–moderate |
| Writer–verifier | Anthropic says Opus 5 coordinates teams well with effective writer–verifier patterns. [O5-PG](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) | Opus 5 High controller; Medium writer; fresh verifier | Low–moderate |
| Dynamic, long-lived team | Anthropic describes Fable as significantly more dependable at sustaining subagents and ongoing communication. [F5-PG](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) | Fable High/XHigh | Moderate as vendor guidance; low as independent evidence |
| Small or tightly coupled task | Both cards show coordination costs in tokens; Fable’s easy BrowseComp items can lose per-problem speed because overhead offsets parallelism. [F5-SC p. 274](sources/Claude_Fable_5_and_Mythos_5_System_Card.pdf#page=274) | Solo Opus 5 Medium/High | Moderate |
| Sequential tool/API workflow | Opus 5 leads Fable on the system card’s AutomationBench summary, 26.0 versus 17.4 at the headline settings. [O5-SC p. 148, Table 8.1.A](sources/Claude_Opus_5_System_Card.pdf#page=148) · [page image](evidence/opus5-p148.png) | Start solo with Opus 5 Medium/High; do not add agents unless work can truly run independently | Low–moderate |
| Cost-sensitive controller | Current base pricing is $5/$25 per MTok input/output for Opus 5 and $10/$50 for Fable 5. [PRICE, model pricing, accessed 24 July 2026](https://platform.claude.com/docs/en/about-claude/pricing) | Prefer Opus 5 unless Fable’s coordination advantage changes verified outcome enough to repay 2× token rates | High for price; low–moderate for total-workflow value |

---

# 7. Routing table: first extensive draft

## 7.1 Solo work

| Conditions | Primary route | Alternative | Escalation trigger |
|---|---|---|---|
| Small, clear, testable code change | Opus 5 Medium | Sonnet 5 for lower-value mechanical work | Failed tests, hidden architectural coupling |
| Complex but tightly coupled implementation | Opus 5 High | Opus 5 XHigh | Repeated incorrect root-cause model |
| Deep architecture or recovery | Opus 5 XHigh | Fable High/XHigh | Work graph becomes multi-track and persistent |
| Routine professional/tool workflow | Opus 5 Medium | Opus 5 High | State-tracking failures or ambiguous business rules |

## 7.2 Bounded orchestration

| Orchestration subtype | Controller | Workers | Conditions |
|---|---|---|---|
| Search across independent source classes | Opus 5 High | Opus/Sonnet Low–Medium | Clear partitions; one synthesis pass |
| Competing debugging hypotheses | Opus 5 High/XHigh | Opus 5 Medium investigators | Workers can test independently |
| Two to four repository areas | Opus 5 High | Opus 5 Medium owners | Stable interfaces; explicit integration contract |
| Writer plus independent verifier | Opus 5 High or deterministic harness | Medium writer + fresh Medium/High verifier | Acceptance criteria and machine evidence available |
| Broad migration inventory | Opus 5 High | Lower-cost scouts | Inventory is separable; controller owns final plan |

**Guardrail:** Opus 5’s official guide says it delegates more readily than prior models and recommends explicit criteria or deterministic caps. [O5-PG, “Controlling subagent spawning”](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

Suggested controller instruction:

> Delegate only genuinely independent, sizeable workstreams. Do not duplicate work assigned to an active worker unless independent replication is explicitly valuable. Keep the default concurrency cap at four. Retain responsibility for decomposition, integration, critical-path work, stopping, and final verification.

## 7.3 Dynamic and long-lived orchestration

| Conditions | Primary route | Alternative | Why |
|---|---|---|---|
| Work graph changes repeatedly | Fable 5 High | Opus 5 XHigh | Fable’s official profile emphasizes ambiguity handling and sustained subagents |
| Persistent agents communicate over many rounds | Fable 5 High/XHigh | Opus 5 XHigh | Stronger vendor evidence for ongoing coordination |
| Days-long autonomous project | Fable 5 XHigh | Fable High if XHigh adds low value | This is Fable’s intended workload |
| Large distributed implementation with clear modules | Fable High controller + Opus Medium workers | Opus High controller + Opus Medium workers | Test whether Fable’s manager premium repays token cost |
| Controller must stay out of implementation | Fable High/XHigh | Deterministic orchestration policy around Opus 5 | Opus 5’s strong worker behavior may otherwise pull it into execution |

---

# 8. Failure modes and controls

## 8.1 Opus 5

**Officially reported/guided risks:**

- delegates more readily than prior models;
- can expand scope;
- verifies its own work and can over-verify when prompts add redundant checking;
- may waste cost on small delegated tasks.

[O5-PG, “Task scope and over-verification,” “Controlling subagent spawning,” and “Self-correction”](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

**Controls:**

- deterministic worker cap;
- delegation threshold based on independence and expected work size;
- no generic “use a subagent to double-check” instruction;
- acceptance tests and explicit stop condition;
- report adjacent issues without silently expanding scope.

## 8.2 Fable 5

**Officially reported/guided risks:**

- long turns and extended autonomous runs;
- higher effort can gather context and deliberate beyond what routine work needs;
- higher effort may add tidying, refactoring, or abstractions beyond scope.

[F5-PG, “Longer turns by default” and “Consider all effort levels”](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)

**Controls:**

- use High rather than XHigh by default unless capability sensitivity is demonstrated;
- explicit scope and no-premature-abstraction instruction;
- checkpoints on long projects;
- worker lifecycle and stopping rules;
- budget limits covering total team tokens, not only controller tokens.

---

# 9. What evidence would actually settle the routing question

The public cards use same-model teams and therefore confound controller and worker quality. A local experiment should hold workers constant.

## 9.1 Controller conditions

- Fable 5 High
- Fable 5 XHigh
- Opus 5 Medium, exploratory
- Opus 5 High
- Opus 5 XHigh

## 9.2 Fixed worker pool

Use identical workers in all controller conditions, for example:

- Opus 5 Medium implementers;
- Sonnet Low/Medium scouts;
- fixed tool access;
- fixed concurrency and token ceilings.

## 9.3 Representative orchestration tasks

1. bounded search fan-out;
2. ambiguous research where decomposition must be discovered;
3. multi-package implementation with stable interfaces;
4. tightly coupled implementation where the right choice is not to delegate;
5. debugging with competing hypotheses;
6. writer–verifier workflow;
7. evolving migration with dependencies discovered mid-run;
8. long-lived project with worker failure and reassignment.

## 9.4 Required metrics

- verified task success;
- severe failure rate;
- solo baseline;
- useful work by lead versus workers;
- duplicate work;
- unnecessary workers;
- instruction quality;
- integration defects;
- replanning events;
- recovery after worker failure;
- latency and tail latency;
- total input/output/cache/tool cost;
- human intervention;
- verification burden;
- context growth and compaction effects.

## 9.5 Decision rule

Select the lowest-cost configuration that satisfies the required verified-success and severe-failure thresholds. Do not reward delegation as an end in itself. A controller that correctly declines to spawn workers on a tightly coupled task should score well.

---

# 10. Evidence quality and unresolved questions

## 10.1 Evidence strengths

- Exact primary vendor figures are available.
- Harness definitions and caveats are described.
- Effort curves provide task-specific evidence against monotonic assumptions.
- The key Opus 4.8 async regression and Opus 5 repair are directly inspectable.

## 10.2 Evidence weaknesses

- Core evidence is vendor-produced rather than independent.
- Card-to-card comparisons are not one controlled experiment.
- Opus 5’s multi-agent configuration was pre-release and used an unreleased effort setting.
- Same-model teams confound controller and worker quality.
- No public lead-effort sweep was located.
- No mature real-repository comparison holding workers constant was located.
- Search and program reconstruction do not cover all orchestration regimes.

## 10.3 Revision triggers

Revise the routing table when any of the following appears:

- a controlled Opus 5 versus Fable controller experiment with identical workers;
- lead-effort sweeps;
- production logs measuring duplicate work and worker utilization;
- pricing or usage-limit changes;
- new model snapshots;
- local results showing a different cost-to-verified-outcome frontier.

---

# 11. Audit resources

- [Claim ledger](CLAIM_LEDGER.md)
- [Source inventory, roles, checksums, and limitations](SOURCE_INVENTORY.md)
- [Web source notes](WEB_SOURCE_NOTES.md)
- [Orchestration values with provenance](assets/orchestration_values_with_provenance.csv)
- [Effort values with provenance](assets/effort_values_with_provenance.csv)
- [GPT-5.6 Pro research prompt with mandatory audit protocol](GPT-5.6-PRO-RESEARCH-PROMPT.md)

This report uses AHR-C’s requirements to preserve model, effort, harness, task, source role, uncertainty, and verification conditions, and to distinguish observed results from synthesis, inference, and recommendation. [AHR-C §§3.1–3.5, 6.1–6.8, 11.2–11.11, 13.1–13.6]
