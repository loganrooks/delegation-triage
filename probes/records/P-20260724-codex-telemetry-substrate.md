# P-20260724-codex-telemetry-substrate — Codex-side capture surface (B-5: the field-union third leg)

**Date:** 2026-07-24 · **Class:** platform-capability probe (NOT a routing outcome — moves no
flip counter)
**Router:** fable leg, 2026-07-24 campaign session; explorer lane at sonnet/high (R7 default,
`explorer` pin), 29 tool uses / ~182s / ~112k harness-reported subagent tokens.

## What this closes

The portfolio review ([`docs/reviews/2026-07-24-portfolio-decomposition-fable-review.md`](../../docs/reviews/2026-07-24-portfolio-decomposition-fable-review.md))
accepted R-B on a **2-of-3-leg** field-union test with the Codex leg **Unchecked ("~/.codex
absent")**. That absence claim is **superseded**: `~/.codex` exists with 493 session JSONLs
(553MB, subagent-reported), and the third leg is now measured.

## Findings (attestation per item)

1. **Session transcripts carry per-turn routing intent** — `turn_context.payload` includes
   `model` and `effort`/`reasoning_effort`; multi-agent `spawn_agent` function calls carry
   `{agent_type, model, reasoning_effort, message}` in one record. *Subagent-reported with
   resolvable locators (sessions/2026/07/24 + 07/04 rollout files); parent not re-checked.*
2. **`~/.codex/delegations/…/state/runs/…/metadata.json` is the richest single artifact
   found**: `requested {model, effort, max_budget_usd, max_turns, permission_mode}` vs
   `observed_model {status, value}`, per-model usage incl. `costUSD`, `num_turns`,
   `stop_reason`, tool inventory, sandbox/profile governance fields + manifest sha256. n=1
   run on disk. *Parent-verified firsthand same day (python parse; values reproduced:
   requested fable/high/$8.00/30 turns → observed claude-fable-5, $4.799322, 27 turns,
   end_turn).*
3. **A purpose-built routing-intent ledger already exists on the Codex side:**
   `~/.codex/telemetry/orchestration-learning/events.jsonl` — 222 events:
   `route_planned` 94 · `disposition` 96 · `consultation` 25 · `checkpoint` 4 ·
   `hypothesis` 2 · `policy_decision` 1. `route_planned` carries **23 fields** incl.
   `task_class`, `requested_/planned_{model,effort,role}`, `reversibility`, `consequence`,
   `ambiguity`, `validation_oracle`, `falsifier_code`, `nearest_alternative`,
   `closure_target`, `expected_advantage_code`, `packet_completeness_code`,
   `write_scope_count`, `schema_version`; `disposition` carries 12 incl. `rework_count`,
   `validator_outcome`, `friction_codes`, `confounder_codes`. *Parent-verified firsthand
   same day (key lists reproduced by python parse of lines 1–2 + full Counter over 222).*
4. **OTel:** live `config.toml` has no `[otel]`/telemetry lines; an opt-in
   `otel-local.config.toml` profile exists (`codex --profile otel-local`, OTLP-HTTP
   :4318); `telemetry/otel/status.json` shows a pipeline that ran at least once
   (last request 2026-07-10, `degraded: free_disk_guard`). Plus Claude-Code-style hook
   mirroring in `telemetry/harness-events.jsonl` (45,269 lines). *Subagent-reported.*

## Consequence for R-B and B-3 (recorded, executed as a review addendum)

R-B's ACCEPT stands, but its supporting note "the union is small (~14 intent fields)"
is **amended by measurement**: the Codex side already operates a `schema_version`'d intent
ledger *richer* than the proposed record (~25–30 union fields). B-3's schema work therefore
changes shape: **reconcile with the existing orchestration-learning schema** (adopt, map, or
supersede field-by-field) rather than minting names fresh. Three schemas now need one
crosswalk: platform OTel (P-20260724-otel-routing-observability-substrate), the spawn ledger
(`~/.claude/observability/`), and the Codex orchestration-learning ledger.

## Blind spots (inherited from the leg, declared there in full)

1/493 session files read in full (schema rests on n=1 + targeted greps); sqlite stores
(`logs_2.sqlite`, `state_5.sqlite`…) unopened; single delegations run on disk; whether the
otel-local profile was active for any sampled session unchecked.

- **attestation:** explorer subagent report (sonnet/high) with resolvable locators; the two
  load-bearing finds (items 2–3) parent-verified firsthand same day; items 1 and 4 remain
  subagent-reported and are tallied as such.
- **tally:** moves no counter. Feeds B-3 (schema reconciliation) and the portfolio review's
  R-B amendment.
