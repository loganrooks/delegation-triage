# B-3 — Intent/outcome record: three-schema crosswalk (v0 draft)

**Status: DRAFT — authored by the fable campaign session (R2 class), panel-gated per
CONTRACT §6.7a before operator sign-off.** Binding constraints: north star
[§6-as-amended](2026-07-24-evidence-commons-north-star.md) (RATIFIED 2026-07-24) and the
[panel adjudication](../reviews/2026-07-24-decision-panel-adjudication.md)'s §6 corrections.

## 0. What this is

One **intent record** (written at the routing decision point) and one **outcome record**
(written at completion), specified as a *crosswalk* over the three capture systems that
already exist — not a fourth competing schema. Producers keep writing their native formats;
the crosswalk defines the canonical field, per-source mapping, and the normalization each
source needs. A record that can be *projected* from a native format is conformant; nothing
requires rewriting a working writer on day one.

**The three sources** (all measured, not assumed):

| # | source | native home | measured in |
|---|---|---|---|
| S1 | Claude Code platform OTel | `api_request` / `subagent_completed` events | [P-20260724-otel…](../../probes/records/P-20260724-otel-routing-observability-substrate.md) |
| S2 | spawn ledger (signal-layer hooks) | `~/.claude/observability/ledger/spawns-*.jsonl` (locator class: `claude-user-dir:`) | portfolio review §0 V5–V10 |
| S3 | Codex orchestration-learning v1 | `route_planned` / `disposition` events, strict allowlist validator | [P-20260724-codex…](../../probes/records/P-20260724-codex-telemetry-substrate.md); value vocabularies sampled firsthand 2026-07-24 |

## 1. Identity layer (§6-1: scopes + rekey, not bare "stable IDs")

| ID | scope | rule | S1 | S2 | S3 |
|---|---|---|---|---|---|
| `event_id` | one record, immutable | ULID at write; never reused | — (absent: derive at ingest, flagged `derived`) | — (same) | `event_id` ✓ as-is |
| `run_id` | one delegated unit (spawn→outcome) | joins intent↔outcome; unique within origin | `session.id`+`prompt.id` composite (derived) | `tool_use_id` | `run_id` ✓ (caveat: human-chosen strings can collide across origins — unique only with `origin`) |
| `origin` | one producing installation | self-chosen namespace string + keypair fingerprint when sharing starts; local records may omit (implied `local`) | absent — stamp at ingest | absent — stamp at ingest | absent — stamp at ingest |
| `project_pseudonym` | one project × one origin | HMAC(project, origin-key). **Explicitly NOT cross-origin stable** (panel finding: S3's machine-local salt makes same-project-two-machines two IDs — that is *correct behavior* for a pseudonym; the error was calling it a stable ID). Cross-origin join is an explicit operator act (reveal or shared salt), never a default | `project_key` ≈ | `project_key` ✓ | `project_id` ✓ semantics kept, renamed |
| `session_id` | one driver session | opaque within origin | `session.id` ✓ | envelope `session` ✓ | absent (nullable) |

**Rekey rule:** an origin MAY rotate its project key; it then emits a `rekey` record mapping
old→new pseudonyms, signed by the origin key. Consumers treat unmapped old pseudonyms as
distinct forever — rekeying without the mapping record is deliberate unlinking, and legal.

## 2. Intent record (route-decision point — the driver writes it, not a hook: DR-2)

Canonical fields → source mappings. `∅` = source cannot supply; nullable unless marked REQ.

| field | REQ | semantics | S1 | S2 | S3 |
|---|---|---|---|---|---|
| `v` | ✓ | crosswalk version (`"2"`; native `schema_version` preserved alongside) | ∅ | ∅ | `schema_version` |
| `ts` | ✓ | ISO-8601 UTC | ✓ | ✓ (normalize the epoch-float variants — measured in V5) | `ts` |
| `event_id`,`run_id`,`origin` | ✓ | §1 | §1 | §1 | §1 |
| `task_class` | ✓ | demand-ontology term. **Two-level: `class` (closed enum, from ROUTES rows + the W-025 orchestration families) + `class_free` (producer's native term, preserved)** — S3's 59 observed values (measured: `bounded-implementation` 8 · `web-research` 6 · `review` 5 …) map onto ~12 classes without loss because the native term rides along | ∅ | `task` dict (15/670 records) | `task_class` |
| `route_id` | | ROUTES row (or overlay row) consulted; `none-consulted` is a legal, honest value — **this is the field whose absence made the 2.2% unmeasurable** | ∅ | ∅ | ∅ (new in v2) |
| `warrant_ids[]` | | W-records load-bearing for the choice | ∅ | ∅ | ∅ (new) |
| `rung` | | rung-table row fired (B-6; empty until it exists) | ∅ | ∅ | ∅ (new) |
| `requested_model` | ✓ | **normalized binding id** (`vendor:model` — e.g. `anthropic:claude-opus-5`, `openai:gpt-5.6-terra`) + `requested_model_raw` preserved. Needed now: S3 shows live alias drift, measured — `terra`/`gpt-5.6-terra`/`gpt-5-6-terra` are one binding in three spellings | `model` | `model_requested` | `requested_model` |
| `requested_effort` | ✓ | `low/medium/high/xhigh/max/session-inherited` | `effort` | `effort_spawner` | `requested_effort` |
| `requested_role` | | agent-type / roster pin name | `subagent_type`-adjacent | `subagent_type` | `requested_role` |
| `surface` | ✓ | delivery surface (pin / per-call / generic / teams / cowork) — CONTRACT §3's control-surface question, made a field | ∅ | derivable (`tool_name`+`subagent_type`) | ∅ (new) |
| `harness_contract` | ✓ | **content hash of the in-force contract** (prompt contract + skill + gate config), plus a human label. The R-D refinement made a field; v2-only everywhere (§6-2) | ∅ | `prompt_sha256` (partial: prompt only) | ∅ (new) |
| `router_model` | | who decided (self-route vs driver vs human) | ∅ | `parent_agent_id` ≈ | ∅ |
| `reason_code` | | **enumerated** decision-reason vocabulary + optional `note_hash` (§6-4: no free text; adopts S3's `*_code` convention — `falsifier_code`, `expected_advantage_code` map in directly) | ∅ | ∅ | `falsifier_code`, `expected_advantage_code`, `nearest_alternative` |
| S3 riders | | `reversibility`, `consequence`, `ambiguity`, `validation_oracle`, `closure_target`, `write_scope_count` — adopted as optional canonical fields (they encode the CONTRACT §1 delegation test better than anything we had) | ∅ | ∅ | ✓ native |

## 3. Outcome record

| field | REQ | semantics | S1 | S2 | S3 |
|---|---|---|---|---|---|
| ids + `v`,`ts`,`origin` | ✓ | §1; `run_id` joins to intent | ✓ | ✓ | ✓ |
| `observed_model` | ✓ | normalized binding + `identity_source` (transcript / API / UI-label — UI labels are the weakest class, per package doctrine) | `final_model`+`model_swapped` ✓ | ∅ (join to S1) | `observed_model`+`observed_identity_source` ✓ |
| `observed_effort` | | as delivered | ✓ | ∅ | `observed_effort` |
| `tokens{in,out,cache_r,cache_w}` | ✓ | ints | ✓ | ∅ | `input_tokens`/`output_tokens` |
| `cost_usd` | | when the platform reports it (S1 `cost`; Codex delegations `costUSD` — measured n=1) | ✓ | ∅ | ∅/delegations ✓ |
| `disposition` | ✓ | closed enum: `accepted / accepted-after-rework / discarded / blocked / error / abandoned` (S3's `disposition`+`validator_outcome`+`rework_count` map in; S2's stop-without-req asymmetry means S2 alone can only say `completed-unknown` — honest value, allowed) | partial (`subagent_completed`) | stop event | ✓ richest |
| `rework_count` | | int | ∅ | ∅ | ✓ |
| `validator` | | what checked the output (reviewer gate id / tests / human / none) + outcome | ∅ | ∅ | `validator_outcome` |
| `friction_codes[]`,`confounder_codes[]` | | adopted from S3 verbatim | ∅ | ∅ | ✓ |
| `attestation` | ✓ | §4 enum | `platform-emitted` | `platform-emitted` | `self-reported` |

## 4. Attestation enum (§6-3: vocabulary defined HERE — it existed nowhere)

Distinct axis from EPISTEMICS claim-grades (which grade *claims*; this grades *how a record's
content was produced*):

- `platform-emitted` — written by the platform/harness, no model or human in the write path
  (S1, S2 hook legs)
- `self-reported` — the acting agent wrote it about its own work (S3 today; tallied
  separately, per standing probes rule)
- `driver-attested` — the routing driver (not the executor) wrote it at decision time —
  the intent-writer target class (DR-2)
- `third-party-verified` — an independent leg re-checked the load-bearing values
  (parent-verified probe items; panel legs)
- `reproduced` — an independent origin re-ran the runnable artifact and matched
  (commons tier; unused locally today, reserved)

Ordering is informational, not a trust score; consumers filter by tier, never average across.

## 5. Sensitive/routing separation (§6-4 floor — Codex's posture generalized)

Adopt S3's mechanism as the norm: **closed allowlist + validator rejection of
content-bearing fields.** Routing-relevant = every field in §§1–3. Content-bearing (prompts,
paths, transcripts, code, free-text notes) is *structurally absent* — where context is
needed, a `*_hash` or enumerated code stands in. The S2 fields that violate this
(`prompt_head`, `cwd`, `description`) are marked **non-exportable** in the crosswalk: they
never project into a v2 record. Consent-to-share = the §§1–3 field list, verbatim.

## 6. Migration (§6's v2-with-dual-read, made concrete)

1. **v2 is a new stream, not an edit.** No v1 writer changes; the S3 validator keeps
   rejecting unknown fields — correctness, not obstruction (panel: fields enter as v2, never
   appended to v1).
2. **Projectors, not rewrites:** three read-side projectors (S1/S2/S3 → v2), each stamping
   `origin`, deriving missing ids (flagged `derived`), normalizing model aliases and
   timestamps. Stdlib-only, fixture-tested — these fixtures ARE C-5's conformance suite seed.
3. **Dual-read window:** consumers read v2 ∪ projected-v1 until the intent-writer (the one
   NEW writer: driver-side, `driver-attested`, carrying `route_id`/`warrant_ids`/`surface`/
   `harness_contract` — the four fields no existing source can supply) is deployed and the
   projectors are boring.
4. **Ownership boundary:** this package owns the crosswalk + projector specs; S3's native
   schema stays owned by its Codex-side skill — proposals to *its* v2 go through that owner
   (D-1 compatibility contract, C-5). Nothing here edits it.

## 7. What this deliberately does not do

No registry, no transport, no aggregation semantics (L3). No rung-table fields beyond the
nullable `rung` slot (B-6 owns that). No live writer implementation — the intent-writer is
its own build item with its own review. No claim that the 59-value S3 task vocabulary maps
losslessly — the two-level design preserves the native term precisely because it might not.

## 8. Falsifiers / review targets for the panel

- A routing decision the intent record cannot express without free text → §2's enums are
  wrong, not the discipline.
- A v1 S3 record that cannot project into v2 without loss beyond the declared
  non-exportables → the crosswalk table has a hole.
- The two-level task_class proving to be where all the information hides (everyone routes on
  `class_free`) → the closed enum is decorative and the ontology work is unfinished.
- An attestation case the five tiers cannot type (e.g. platform-emitted but
  model-postprocessed) → the enum needs a sixth value, define it then.
