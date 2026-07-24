# PROBE — 2026-07-24 Claude Code OTel routing-observability substrate

- probe_id: P-20260724-otel-routing-observability-substrate
- task class / ROUTES row: n/a — **platform-capability probe**, not a routing-outcome probe. It
  establishes what the harness can observe about a delegation, not which tier should run one.
- configs compared (model × effort × surface × harness): three headless `claude -p --model sonnet`
  runs on Claude Code `2.1.218`, console OTel exporter; run 2 and run 3 each spawned one
  `explorer-light` subagent (sonnet × medium pin); run 3 added `OTEL_LOG_TOOL_DETAILS=1`
- harness/contract hash (if pinned): n/a
- blinded?: n/a (deterministic capability observation)
- frozen tree?: n/a
- adjudicator: author (root session); all facts are machine output, not judgment
- router: main-loop Claude Code Opus 5 (session effort), operator-authorized step 1 of the
  2026-07-24 fused observability plan
- **attestation:** raw console-exporter logs on disk at
  `<session scratchpad>/otel-probe/{smoke,subagent,details}.log`; every quoted attribute below was
  extracted from those bytes by a local script, not summarized by a model
- verdict: **substrate confirmed, with one assumption falsified and a better join key found**
- tokens / cost (if observable): 7 `api_request` records; **total `cost_usd` = 0.8064** (smoke
  0.3039 · subagent 0.2753 · details 0.2272). The smoke run cost $0.30 for a two-token reply —
  50,630 cache-creation tokens dominate a cold headless start.
- **tally:** feeds no W-record flip counter. Registers the substrate for the observability design
  and supplies detectors for two existing KNOWN-WEAKNESSES kinds; count after this record: n/a.
- deviations from clean protocol (named): none for the capability claims. `query_source` values
  observed here are `sdk`/`agent:custom` because the driver was headless `-p`; an interactive
  session may differ and was not tested.

## Why this probe

The [2026-07-24 routing-infrastructure survey](../../docs/research/2026-07-24-routing-infrastructure-survey.md)
§4 claimed — from a summarizing web fetch, labeled **Reported** — that Claude Code already emits
per-call `model`, `effort`, `query_source`, and **`agent.name`**, and proposed joining an intent log
to that stream on `session.id` + `agent.name`. The survey named its own verification step. This is
that step.

## Observed facts

1. **Telemetry emits with no persistent configuration change.** Environment variables only
   (`CLAUDE_CODE_ENABLE_TELEMETRY=1`, `OTEL_METRICS_EXPORTER=console`, `OTEL_LOGS_EXPORTER=console`);
   `~/.claude/settings.json` was not edited. One trivial prompt produced 70 `claude_code.*` records.

2. **`claude_code.api_request` carries the routing pair.** Verbatim from the smoke run:

   ```text
   model: "claude-sonnet-5",  effort: "xhigh",  query_source: "sdk",
   cost_usd: 0.303921,  cost_usd_micros: 303921,  duration_ms: 1964,
   input_tokens: 2, output_tokens: 9, cache_read_tokens: 0, cache_creation_tokens: 50630,
   session.id / prompt.id / request_id / client_request_id present
   ```

3. **Effort is populated, and it is the pin's effort.** The `explorer-light` subagent's own
   `api_request` reported `effort: "medium"` — matching the roster pin — while the driver's calls
   reported `effort: "xhigh"`. Both runs 2 and 3 reproduce this.

4. **FALSIFIED — `agent.name` is not the join key.** For a user-defined roster agent, the
   `api_request` reports `agent.name: "custom"` and `query_source: "agent:custom"`. The roster type
   never appears. `OTEL_LOG_TOOL_DETAILS=1` **does not** un-redact it (run 3, verified: the only
   `agent.name` value present in the entire stream is `custom`, and no `subagent_type` string
   appears anywhere).

5. **A better join key exists, and is undocumented in the page the survey read.**
   `claude_code.subagent_completed`, verbatim:

   ```text
   agent_type: "explorer-light",     agent.source: "userSettings",   is_built_in: false,
   model: "claude-sonnet-5",         final_model: "claude-sonnet-5", model_swapped: false,
   total_tokens: 28685,  total_tool_uses: 0,  duration_ms: 2137,  is_async: false,
   session.id + prompt.id present
   ```

6. **A headless `-p` run defaulted to `effort: "xhigh"`** with no effort requested and
   `--model sonnet` given. Not investigated further; recorded because it is a live instance of the
   documented `effort-inheritance over-provisioning` kind, and because it made a two-token reply
   cost $0.30.

## What this changes

- **The design's join key moves** from `api_request.agent.name` (redacted, useless) to
  `subagent_completed.agent_type` (exact roster-pin identity). Per-call `effort` still comes from
  `api_request`, correlated within a `prompt.id`.
- **Two free detectors for existing weakness kinds.** `model_swapped` + `final_model` detects
  `provenance-misreport` (observed n=2) mechanically rather than by transcript grep.
  `api_request.effort` per `query_source` detects `effort-inheritance over-provisioning`
  (observed n=2) at emit time rather than by operator catch.
- **`agent.source: "userSettings"`** names where the executed definition came from — directly
  relevant to the canonical-vs-deployed roster divergence recorded as D-1/D-2 in the
  [2026-07-24 control-plane review](../../docs/reviews/2026-07-24-control-plane-initiative-claude-review.md).

## What remains unverified

1. **Concurrent-subagent attribution.** With one subagent the `agent:custom` `api_request` is
   unambiguously attributable. With several concurrent custom agents in one `prompt.id`, nothing
   observed here distinguishes their `api_request` rows. An intent-log spawn ordinal or a timing
   join is required, and is untested.
2. **Interactive-session `query_source` values.** Only headless `-p` was exercised; the
   documented `main` / `subagent` / `auxiliary` values were not observed.
3. **Whether `agent_type` stays unredacted under an OTLP exporter** rather than console, and under
   an organization-managed telemetry policy.
4. **Why the headless run took `xhigh`** — inheritance, default, or flag interaction. Not probed.
5. Nothing here bears on any model's capability. No routing row may move on this record.
