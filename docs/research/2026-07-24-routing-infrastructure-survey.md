# Survey: routing infrastructure, reference designs, and what the platform already gives us

- **Date:** 2026-07-24
- **Author:** Claude Code (Opus 5), root session
- **Purpose:** situate delegation-triage against existing auto-routers before deciding how routing
  tables get grounded, updated, audited, and learned from
- **Status:** first pass. Breadth over depth; every load-bearing claim carries its check and its
  limit
- **Authority:** research evidence only. Nothing was implemented, installed, configured, or
  activated. No routing change follows from this document.

## 0. Method and its limits

**Checked first-hand** (raw output, no summarizing layer): GitHub issue corpora via `gh` (my own
filtering), local `lectern` execution, local `claude`/`codex` state inspection.

**Checked through a summarizing layer** (`WebSearch`, `WebFetch` — both answer a prompt against the
page rather than returning bytes): everything else, including the OpenTelemetry field list in §4.
Per [`claims-discipline`] and the `summarizer-fabrication` kind in
[`KNOWN-WEAKNESSES.md`](../../probes/KNOWN-WEAKNESSES.md), those are **Reported** and the
load-bearing ones name their verification step inline.

**Not covered:** conference talks and podcasts (see §8), vendor-internal postmortems, private
Discord/Slack practice, and non-English sources beyond what surfaced incidentally.

---

## 1. Reference designs

| System | Routing signal | Policy surface | Explains itself? | Adding a model |
|---|---|---|---|---|
| [RouteLLM](https://github.com/lm-sys/RouteLLM) (LMSYS) | learned classifier over Chatbot Arena preference pairs | a trained checkpoint + a cost threshold | no — a scalar win-probability | retrain |
| [Arch-Router](https://arxiv.org/abs/2506.16655) (Katanemo) | 1.5B model maps query → user-declared *route* | **JSON list of `{name, description}` routes, each bound to a preferred model** | yes — names the route it matched | edit config, no retraining |
| [vLLM semantic-router](https://github.com/vllm-project/semantic-router) | embedding similarity + classifiers, serving-layer | YAML config, per-model overrides | partial — decision logs | config |
| [OpenRouter Auto](https://openrouter.ai/docs/guides/routing/routers/auto-router) | vendor-side (NotDiamond) | one dial: `cost_quality_tradeoff` 0–10 | **no** — response reports *which* model, never *why* | vendor's pool |
| [LiteLLM](https://github.com/BerriAI/litellm) router | declarative rules, fallbacks, load balance | YAML/py config | rules are readable; no evidence layer | config |
| [claude-code-router](https://github.com/musistudio/claude-code-router) | rule config + optional custom JS router | JSON config, per-scenario keys (background/think/longContext/subagent) | log viewer, retrofitted | config |
| **delegation-triage** | the orchestrating model reads a table and states a fit line | **Markdown: task class → model × effort, + fallback + warrant IDs** | yes — fit line cites a route row and a W-ID | edit a row |

**The most important result in this table is the convergence.** Arch-Router is the current
research answer to "make routing interpretable," and independently arrived at the same shape as
`ROUTES.md`: *named routes carrying natural-language descriptions, bound to preferred models,
authored by the user, extensible without retraining.* Its paper's stated motivation — that
benchmark-optimal routing "fails to capture subjective evaluation criteria" — is the same
complaint that motivates this package.

Two differences, both in our favour and both worth naming:

1. **Arch-Router routes by *query semantics*; we route by *task class and judgment demand*.**
   Theirs answers "what is this prompt about" (travel, image editing, bug fixing). Ours answers
   "what does this work demand of the worker" (a verdict on a finished artifact; coverage without
   judgment; adversarial refutation). The second is the harder and more transferable abstraction —
   query topic is a proxy for it.
2. **Nobody surveyed has a warrant layer.** Every system above binds route → model. None records
   *why that binding*, *on what evidence*, *at what confidence*, *expiring when*. That is
   `WARRANTS.md` + `STATE.md`, and as far as this survey found, it does not exist anywhere else in
   the routing ecosystem.

**Inference (not observed):** the differentiator is not the table. It is the evidence discipline
attached to the table. Any competitor can ship a routing config; almost nobody ships a falsifier.

---

## 2. What the filed-issue corpora actually say

Both corpora below were fetched with `gh` and filtered by me — first-hand.

### RouteLLM — 40 issues, open and closed

The dominant clusters, by count: *"how do I train a router"* (#65, #82, #67, #60, #42 — with
"same question here" pile-ons across two years), *"training scripts aren't available"*,
*"can I use my own embedding model"* (#84, #62, #50), *"following the demo it doesn't work"* (#78),
*"routing to local models problem"* (#79). Maintainer answers repeatedly point to the paper.

**Zero issues ask why a particular routing decision was made.** Not because it is transparent —
because it isn't answerable, so nobody asks. Users instead ask for the one thing that would let
them own the policy themselves: the training pipeline.

### claude-code-router — 400 issues fetched, 81 matching routing/transparency terms

This is the closest analogue to our situation (routing inside a coding harness) and its failure
modes are specific and repeated:

- **Routing silently not firing.** #1564: "Subagent routing never fires: marker is only read from
  `body.system[]`, but Claude Code sends agent…" — the config said one thing, the router did
  another, and nothing surfaced it.
- **Silent fallback swallowing the decision.** #1535: a model "exposed as discoverable model but
  unroutable — all requests fall into…"; #1520 (zh): with built-in routing on, custom rules'
  fallback stops working.
- **Routing to models that don't exist or aren't accessible.** #1299, #1297, #1296, #1237 — four
  separate reports of "selected model may not exist or you may not have access."
- **Retrofitted observability demand.** #1288 "Add Live Logs view"; #1226 "Visualize button in Log
  Viewer"; #1242 "add a troubleshooting reference for model routing, context drift."
- **Undefined model returned by the router** (#1321, a race in provider init).

**The shape of the complaint is not "the router chose badly." It is "the router did something
other than what my config says, and I had no way to see it."** Transparency is being asked for as
*decision-provenance*, not as *decision-justification*. That is a much cheaper thing to supply —
and it is the thing our §2-of-the-review defects show we currently also fail at, since the
deployed table and the canonical table disagreed for days without surfacing.

### The community-calibration prior art, and its pathologies

Reported (search layer, corroborate before building on): Chatbot Arena — the largest existing
crowdsourced model-preference corpus — is documented as suffering **prompt contamination** (public
prompts leaking into training crawls), **selective disclosure** (a provider testing many private
variants and publishing the best), **style bias** (longer, more formatted answers win pairwise
votes at equal substance), and **direct optimization** (training on Arena data raising ArenaHard
win rate 23.5% → 49.9%). See [Willison's summary of the April 2025
criticism](https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/).

Every one of those is a Goodhart failure of a *voluntary, aggregated, community* signal — i.e. the
exact class of system §6 proposes. They are not reasons not to build it. They are the design
constraints it must be built against, and they are enumerable in advance, which is unusual and
valuable.

---

## 3. Is a Markdown table sufficient?

Sufficient for **the consultation surface**, yes — and the convergence in §1 is evidence for it,
not against. Arch-Router's policy config is a JSON list of `{name, description}`; ours is a table
with the same information plus a fallback column and warrant IDs, and it is readable by the agent
that has to act on it without a parsing step.

Insufficient for **three specific jobs**, all of which are already firing:

1. **Coupled-field integrity.** `ROUTES.md` R7 says the `explorer` pin was re-pointed; the pin file
   says otherwise. A table cannot check that. This is a *deterministic* check over a *typed* field,
   and it needs the field to be typed.
2. **Joining decisions to outcomes.** A fit line in prose can't be joined to a telemetry row.
3. **Per-harness projection.** "`fable high` via the `reviewer` pin" is not a statement another
   harness can execute.

**Recommended shape — sidecar, not replacement.** Keep the Markdown table as the human/agent
surface. Add a machine-readable sidecar containing *only the coupled fields*: route ID, task class,
capability demand, binding `(provider, model, effort, surface)`, fallback, warrant IDs,
`valid_until`. Generate the table's binding columns from the sidecar, or check them against it —
either direction works; drift between them must fail CI. This is the same relationship
`STATE.md` already has with `check_state.py`, extended one column further.

**What this buys, concretely:** D-1 from the review becomes a CI failure instead of a five-day
silent regression; the Codex projection becomes a rendering of the sidecar rather than a second
table to maintain; and each route row becomes joinable to telemetry by ID.

**What to resist:** promoting warrants, probe records, or the epistemic vocabulary into structured
data. Those are authored arguments. Their value is that a human wrote down what would falsify
them; a schema cannot hold that and will quietly encourage a score instead.

---

## 4. The platform already emits most of what we want to learn from

This is the largest practical finding in the survey, and it contradicts an assumption running
through the whole proposal set.

> **VERIFIED 2026-07-24, and partially falsified — see
> [P-20260724](../../probes/records/P-20260724-otel-routing-observability-substrate.md).** The
> substrate is real and richer than described here, but **`agent.name` is redacted to `custom` for
> roster agents and is NOT a usable join key** (`OTEL_LOG_TOOL_DETAILS=1` does not un-redact it).
> The join key is `claude_code.subagent_completed.agent_type`, an event absent from the docs page
> below. `effort` IS populated per call and matches the pin. Read this section together with that
> probe record; where they disagree, the probe governs.

**Reported** (from [Claude Code monitoring docs](https://code.claude.com/docs/en/monitoring-usage)
via a summarizing fetch — **verify against a live OTel stream before building on the exact field
names**): Claude Code already exports OpenTelemetry metrics including `claude_code.cost.usage` and
`claude_code.token.usage`, and both carry these attributes:

- `model` — the model identifier
- `effort` — `low` / `medium` / `high` / `xhigh` / `max`
- `query_source` — `main` / `subagent` / `auxiliary`
- `agent.name` — **the subagent type**
- `skill.name`, `plugin.name`, `mcp_server.name`, `mcp_tool.name`

Plus events: `claude_code.api_request` (model, effort, cost_usd_micros, input/output/cache tokens,
`agent.name`), `claude_code.api_refusal` (**`category`, `server_fallback_hop`** — directly relevant
to W-013's refusal-handling constraint), `claude_code.tool_result` (with `subagent_type`),
`claude_code.permission_mode_changed` (with `trigger` values including `auto_gate_denied` and
`auto_opt_in` — directly relevant to the handoff's §9 question about `auto` as an escape hatch),
and `workflow.run_id` / `workflow.name` on every event.

Codex has an equivalent `[otel]` section in `config.toml` emitting session events stamped with
`conversation.id` and `model` (Reported).

**Observed locally:** OTel is **not currently enabled** on this machine — no `OTEL_*` in the
environment, nothing in `~/.claude/settings.json`.

### What follows

The consolidated proposal (§8.1) specifies a bespoke mechanical event family — `route_planned`,
`route_requested`, `attempt_started`, `attempt_observed`, `validation_observed`, `disposition`,
`outcome_followup`. Set that against what the platform gives free:

| Proposed event | Already emitted? |
|---|---|
| `attempt_started` / `attempt_observed` | yes — `claude_code.api_request` per call, attributed to `agent.name` + `effort` |
| cost/token accounting | yes — `cost.usage`, `token.usage`, per model × effort × agent |
| refusal | yes — `api_refusal` with category and fallback-hop |
| `route_requested` | **partially** — the *delivered* model/effort is emitted; the *requested* one is not |
| `route_planned` | **no** — task class, W-ID, why. This is the only genuinely missing field |
| `validation_observed` / `disposition` | **no** — but these are authored judgments, not mechanical facts |

So the observability question — *"is there enough across the platform, or should we expose other
metrics?"* — has a sharper answer than the proposals assume: **the observed side is already
oversupplied and unused; the intent side is what's missing, and it is one small record.**

The design that follows is roughly ten lines of contract rather than a learning plane:

```
at spawn:  append {session_id, agent.name, task_class, route_id, warrant_ids,
                   requested_model, requested_effort, surface, why} → intent log
at rest:   join intent log ⋈ OTel (session.id, agent.name)
           → planned vs requested vs observed, with cost, tokens, refusals, for free
```

The join key already exists on both sides. `agent.name` in OTel *is* the roster pin, which *is* the
route binding. Nothing needs to be invented; the two halves need to be introduced to each other.

**Named limit:** this join is per-session and per-agent-name. It cannot attribute two spawns of the
same agent type in one session to different task classes without an explicit correlation ID, and
`agent.name` is absent for generic model-pinned spawns. Both are knowable in advance and neither is
fatal — the intent log can carry a spawn ordinal.

---

## 5. Where routing decisions get their ground, and who owns it

Three grounding sources, and they are not interchangeable:

| Source | What it licenses | Failure mode | Current handling |
|---|---|---|---|
| **Literature** | design priors and methodology — e.g. W-018's "our data scale is a different statistical regime", W-019's flip thresholds | over-transfer: a benchmark-scoped result imported as an operational guarantee | good — W-018/W-019/W-021 are correctly labeled `Reported`/`Concordant` with the transfer gap named |
| **Vendor cards / release notes** | what the provider claims, and dated availability | treated as capability rather than assertion; silent expiry | good — `EPISTEMICS.md` forces `Concordant`/`Reported`, never `Corroborated`; `STATE.md` expires them |
| **Local experience** | what *this* harness × task × operator observed | n=1 generalization; confounds | good — probe records, flip thresholds, attestation |

**Should delegation-triage own the research?** It should own the **claim records**, not the
research process. The distinction matters:

- **Own:** the typed record — claim, label, grade, downgrades, quoted primary excerpt, flip
  condition, tally. That's `WARRANTS.md` and it works.
- **Do not own:** literature discovery, PDF reading, note-taking, cross-project reuse. That is a
  general research capability, it is missing (signal `obs-20260724T200653-d754ba`), and building a
  second half-version of it inside a routing package is how the routing package stops being 811
  lines.

The seam between them is already specified: `WARRANTS.md`'s KNOWN-REPOS prefix key plus the D6
quoted-excerpt rule, which is what keeps each warrant evaluable *without* access to the source
repo. That rule is the right interface to a research ecosystem that doesn't exist yet — it degrades
gracefully today and upgrades cleanly later.

**What is missing and is genuinely ours:** a *question register*. Right now the routing questions
this project generates (R7's unrun paired probe, R15's high-vs-xhigh pair, whether R9 is a route at
all) live scattered across warrant flip conditions and probe tallies. A one-screen register of open
routing questions — each with the decision it would change and the cheapest check that would move
it — is the artifact you hand to a research capability when one exists, and the artifact that keeps
the package honest until then.

---

## 6. Cycles: project → user → community

The user's framing — small learning cycles inside a project, larger meta-learning cycles above it —
maps onto three scopes that already half-exist:

| Scope | Surface today | What changes | Cadence |
|---|---|---|---|
| **Project** | `CONTRACT.md` §5 overlay | project-local task classes and pins | per-session |
| **User** | `ROUTES.md` + `STATE.md` + profiles | bindings, scarcity stance, prices | weekly-ish |
| **Community** | — | *priors* over bindings, conditioned on context | slow |

Two design commitments make this coherent rather than a leaky hierarchy:

**(a) Propagation is by promotion, never by accumulation.** A project overlay row that survives
locally does not become a user-level row because it fired often; it becomes one when someone writes
the warrant. The existing flip discipline (n=1 never flips; ≥2 attested concordant) is exactly the
right gate and should govern promotion between scopes as well as within one.

**(b) Each scope's evidence carries its conditioning.** This is what makes community sharing
possible at all, and it's where every existing leaderboard fails. A finding is not "sonnet high
beats opus high for sweeps." It is "for *this task class*, under *this harness*, with *this prompt
contract*, at *this date*, on *n=2 attested paired lanes*, the cheaper tier was not distinguishable
— and here is the falsifier that wasn't sought." The package already writes findings this way. That
format *is* the translatability layer the user is describing; it doesn't need to be invented, it
needs to be made portable.

**Person-specific vs project-specific tuning — is it conceivable?** Almost certainly, and the
existing corpus already shows one axis of it: the R7 sonnet-first ruling is an *operator policy*
(W-023 labels it exactly that — "policy, not a measured capability claim"), grounded in a belief
about how much the harness carries. Another operator with weaker prompt contracts would rationally
route the same class higher. So the person-level variable is not taste; it is **how much discipline
the operator's harness carries**, which is measurable — and it predicts which tier they should
default to. That is a genuinely interesting hypothesis and the community layer is what would test
it.

---

## 7. Auditability without token cost

The user's constraint — offer "why this model, this effort" without spending extra tokens — is
already mostly solved by the existing design, and the survey suggests the remaining gap is small.

**What exists:** `CONTRACT.md` §4 requires one fit line before every spawn, citing the route row or
W-ID. That is a citation to a constitution, produced by the agent that is already thinking about
the task. Marginal cost: one line.

**What the survey says about it:** this is *ahead* of every system in §1. OpenRouter tells you which
model answered, never why. claude-code-router users are filing feature requests for log viewers to
reconstruct after the fact what a fit line states before the fact.

**The three gaps, cheapest first:**

1. **The citation isn't checkable.** A fit line saying "per R7" is not verified against R7. A hook
   already parses `STATE.md`'s `Active:` line at spawn time; the same hook could check that a
   claimed route row exists and that its `valid_until` hasn't passed. Cost: zero tokens, it's a
   deterministic check.
2. **The citation isn't recorded.** See §4 — it goes in the intent log, which is what makes it
   auditable later rather than merely visible now.
3. **The constitution isn't versioned at the point of citation.** "per R7" is ambiguous across
   edits. A content hash of the routes sidecar in the intent record fixes this and costs nothing at
   spawn time.

**On the "routing constitution" framing:** it already exists and is called `CONTRACT.md` — the
delegation test, the control-surface table, the fit-line requirement, precedence, escalation. What
it lacks is the property a constitution needs most: **being cited by identifier at the point of
action, in a form that can be checked later.** Sections are cited in prose today. Numbering the
clauses so a fit line can say `per CONTRACT §3` and a checker can resolve it is a small change with
outsized auditability return.

---

## 8. Talks and `lectern` — verdict

**Observed, first-hand, today:**

- `lectern doctor` → all OK (`lectern 0.0.1`, python 3.14.2, ffmpeg present, state store OK).
  YouTube discovery reports `OPTIONAL (not configured; set YOUTUBE_API_KEY)`.
- `lectern ingest --transcriber-command` exists and works. Passing a bare `whisper` invocation
  fails (`did not emit valid JSON`) — the contract is that the command emits a JSON **object** on
  stdout with `segments` (or at minimum non-empty `text`).
- With a six-line adapter (`whisper --output_format json --output_dir $D "$IN" && cat $D/*.json`)
  the pipeline advanced past parsing to segment validation, failing only with
  `must include at least one segment` — because the repository fixture is **synthetic tones, not
  speech** (`generate_synthetic_talk.py` builds the wav from `_append_tone`). The plumbing accepts
  whisper's schema; the fixture is simply not an ASR test.

**Verdict:** lectern is usable today for local media with a trivial adapter. It is *not* usable
today for the thing this project would want — pulling talks from YouTube — without a
`YOUTUBE_API_KEY`, and there is no bundled ASR.

**Recommendation: pin it, with a named unblock.** Talks are a genuinely different evidence class
from papers — practitioners say things on stage they never write down, which is exactly the
"beyond the benchmarks" signal the user is after. But the two blockers (API key, adapter) plus
transcript-quality verification make it a side quest right now. The unblock is small and specific:
one API key, one committed adapter script, one real talk ingested and spot-checked for transcript
fidelity. Revisit when the routing-question register (§5) has questions that only talks answer.

---

## 9. What this survey did not settle

1. **The OTel field names in §4 are Reported through a summarizing fetch.** Before any design
   depends on them, enable OTel locally against a file/collector exporter and read the actual
   attribute set off a real spawn. That check is cheap, non-destructive, and would upgrade the
   central finding of this survey from Reported to Corroborated.
2. **Whether `effort` is populated for subagent spawns in practice**, or only where the platform
   "supports" it — the docs hedge (`effort: Effort level (if supported)`). This matters a lot: it
   is the difference between the effort-inheritance weakness kind being detectable automatically
   or not.
3. **Whether Arch-Router-style query classification would outperform the orchestrator's own
   classification** on our task ontology. Untested; probably not worth testing until the ontology is
   cleaned.
4. **Nothing here is a paired probe.** No routing claim in this document should move a flip
   counter; it is design evidence, not routing evidence.

---

## Sources

- [Arch-Router paper (arXiv 2506.16655)](https://arxiv.org/abs/2506.16655) ·
  [Arch-Router-1.5B model card](https://huggingface.co/katanemo/Arch-Router-1.5B)
- [RouteLLM (GitHub)](https://github.com/lm-sys/RouteLLM) ·
  [RouteLLM paper (arXiv 2406.18665)](https://arxiv.org/abs/2406.18665)
- [vLLM semantic-router (GitHub)](https://github.com/vllm-project/semantic-router) ·
  [Workload-Router-Pool vision paper](https://arxiv.org/pdf/2603.21354)
- [LLMRouter (GitHub)](https://github.com/ulab-uiuc/LLMRouter)
- [claude-code-router (GitHub)](https://github.com/musistudio/claude-code-router)
- [OpenRouter Auto Router docs](https://openrouter.ai/docs/guides/routing/routers/auto-router) ·
  [OpenRouter model-routing blog](https://openrouter.ai/blog/insights/model-routing/)
- [Claude Code monitoring & OpenTelemetry docs](https://code.claude.com/docs/en/monitoring-usage)
- [Criticism of the Chatbot Arena (Willison)](https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/)
- [Codex CLI observability & telemetry (DeepWiki)](https://deepwiki.com/openai/codex/9.4-observability-and-telemetry)
