# B-3 — Intent/outcome record: three-schema crosswalk (v0.2)

**Status: RATIFIED — operator sign-off 2026-07-24 (D-B3-1), post-panel.** v0 was panel-gated per CONTRACT
§6.7a (run `wf_c594690d-a44`, 2 legs opus/high: OBJECT + CONCUR_WITH_CHANGES, 6 BLOCKERs);
every finding was firsthand-re-measured and accepted — spread + dispositions in the
[panel adjudication](../reviews/2026-07-24-b3-crosswalk-panel-adjudication.md). Binding
constraints: north star [§6-as-amended](2026-07-24-evidence-commons-north-star.md) (RATIFIED
2026-07-24) and the [decision-panel adjudication](../reviews/2026-07-24-decision-panel-adjudication.md)'s
§6 corrections. **v0.2 rule (panel's procedural finding, adopted): no `✓` in a mapping cell
without a value-level sample behind it** — every cell below is grounded in the live corpora,
re-measured 2026-07-24: S2 = 4,693 ledger records (Jun+Jul), S3 = 222 events, S1 = the OTel
probe's verbatim attribute blocks only.

## 0. What this is

One **intent record** (written at the routing decision point) and one **outcome record**
(written at completion), specified as a *crosswalk* over the three capture systems that
already exist — not a fourth competing schema. Producers keep writing their native formats;
the crosswalk defines the canonical field, per-source mapping, and the normalization each
source needs. A record that can be *projected* from a native format is conformant; nothing
requires rewriting a working writer on day one.

**The three sources:**

| # | source | native home | status | measured in |
|---|---|---|---|---|
| S1 | Claude Code platform OTel | `api_request` / `subagent_completed` events | **prospective — NOT enabled** (`~/.claude/settings.json` env carries no telemetry keys; the probe ran under ad-hoc env vars). Every S1 cell below is a claim about what the stream emits *when enabled*, grounded only in the probe's verbatim attribute blocks. Enablement is a named migration precondition (§6.0) | [P-20260724-otel…](../../probes/records/P-20260724-otel-routing-observability-substrate.md) |
| S2 | spawn ledger (signal-layer hooks) | `~/.claude/observability/ledger/spawns-*.jsonl` (locator class: `claude-user-dir:`) | live; **two disjoint partitions** (§1a) | portfolio review §0 V5–V10; full payload-key inventory + value samples re-measured 2026-07-24 (panel + adjudicator) |
| S3 | Codex orchestration-learning v1 | `route_planned` / `disposition` events, allowlist validator | live; 222 events | [P-20260724-codex…](../../probes/records/P-20260724-codex-telemetry-substrate.md); value vocabularies re-measured 2026-07-24 |

**S3's validator, characterized precisely (panel A4):** the allowlist is closed over field
NAMES; field VALUES are bounded only by `CODE_RE` (`^[A-Za-z0-9][A-Za-z0-9._:+/@-]{0,127}$`) —
a character class, not a vocabulary. Measured: `observation_code` 92 distinct values / 96
events; `falsifier_code` 83/94. Sentences-with-hyphens pass. So S3's mechanism is a floor on
schema *shape*, not on semantic leakage — the §5 export rules below therefore add
value-level constraints; the S3 posture alone does NOT satisfy north-star §6-4.

## 1. Identity layer (§6-1: scopes + rekey, not bare "stable IDs")

| ID | scope | rule | S1 | S2 | S3 |
|---|---|---|---|---|---|
| `event_id` | one record, immutable | unique-at-write; ULID preferred for new writers; existing UUIDs accepted and flagged | — (derive at ingest, `projection` per §4a) | — (same) | UUID4 (measured: `str(uuid.uuid4())`) — accepted, NOT time-sortable; flagged `id_form: uuid4` |
| `run_id` | one delegated unit; **1:N to outcomes** (§3 `outcome_ordinal`) — measured: 4 S3 run_ids carry >1 disposition (max 3), 4 route_planned lack a disposition, 1 disposition lacks a route_planned | joins intent↔outcomes; unique within origin. **Export rule: S3 run_ids are operator-authored and measurably carry project/feature names (`gate2-slice-a-001`, `signal-adapter-001`) — on export, replace with `run_pseudonym` = HMAC(run_id, origin-key); local records keep the native value** | `session.id`+`prompt.id` composite (derived) | see §1a — partition-scoped | native `run_id`, pseudonymized on export |
| `origin` | one producing installation | self-chosen namespace string + keypair fingerprint when sharing starts; local records may omit (implied `local`) | absent — stamp at ingest | absent — stamp at ingest | absent — stamp at ingest |
| `project_pseudonym` | one project × one origin | **HMAC(project, origin-key), derived at projection time — never a passthrough.** Explicitly NOT cross-origin stable. Cross-origin join is an explicit **per-pair reveal** only — the v0 "or shared salt" option is STRUCK (panel A9: HMAC over low-entropy paths + a shared salt = a dictionary attack unmasking every project, not a consented reveal) | ∅ (no project attribute appears in the probe's verbatim blocks — v0's `project_key ≈` cell was ungrounded) | derive from `project_key` at projection; **`project_key` itself is non-exportable** — measured values are plaintext project names (`bridgewright` 192, `workflow-gate` 69, `prix-guesser` 58…) | derive from `project_id`; native value already HMAC-salted, but re-keyed under origin-key at export for uniform semantics |
| `session_id` | one driver session | opaque within origin | `session.id` ✓ (probe block) | envelope `session` ✓ | absent (nullable) |
| `spawn_ordinal` | position within session | **REQ on intent** — restored from portfolio review §Q3 + OTel probe limit #1 (concurrent-subagent attribution is unresolvable without it); v0 dropped it (panel A12) | derived at ingest | derived (per-session counter at projection) | derived |

**Rekey rule (v0.2 — now implementable; panel A9):** an origin MAY rotate its origin-key. To do
so it must hold a **local path→pseudonym retention table** (the paths never leave the machine;
retaining them locally is legal — §5 governs *export*, not local storage). Rotation emits a
`rekey` record — **v2-only, its own event type**, fields: `{v, ts, event_id, origin,
mappings: [{old_pseudonym, new_pseudonym}], sig}` — signed by the origin key. Consumers treat
unmapped old pseudonyms as distinct forever; rekeying without the mapping record is deliberate
unlinking, and legal. (S3's v1 salt is write-once — `os.O_CREAT|os.O_EXCL`, no rotation path —
so v1 records rekey only via re-projection; that is a projector job, not an S3 edit.)

### 1a. S2 is two partitions, not one stream (panel A5 — the honest join table)

Measured: `tool_use_id` exists on spawn-req/res/denial/fail; `tool_use_id_at_stop` is None in
**1,258/1,258** stop records; spawn-req `agent_id` ∩ stop `agent_id` = 0. The two halves do not
join on any key the ledger carries today.

| partition | records | joins within partition | yields |
|---|---|---|---|
| **request-side** | spawn-req ↔ spawn-res on `tool_use_id` (325/336 overlap, Jul) | ✓ | intent record + `resolved_model`, duration, usage-when-present |
| **execution-side** | subagent-start ↔ subagent-stop on `agent_id` (525 shared) | ✓ | outcome record: `effort_child`, `models_in_transcript`, `stop_class`, `agent_def` |

Cross-partition join is **UNAVAILABLE today**; a projector MAY propose a
timestamp+session+agent_type heuristic, but its output is flagged `projection:
heuristic-join` and excluded from conformance claims. Closing this properly is an
intent-writer job (§6.3), not a projection trick.

## 2. Intent record (route-decision point — the driver writes it, not a hook: DR-2)

Canonical fields → source mappings. `∅` = source cannot supply; nullable unless marked REQ.

| field | REQ | semantics | S1 | S2 (request-side) | S3 |
|---|---|---|---|---|---|
| `v` | ✓ | crosswalk version (`"2"`; native `schema_version` preserved alongside) | ∅ | ∅ | `schema_version` |
| `ts` | ✓ | ISO-8601 UTC (S2 native values are epoch **strings**, e.g. `"1782885929.454425"` — normalize at projection) | ✓ | ✓ | `ts` |
| `event_id`,`run_id`,`origin`,`spawn_ordinal` | ✓ | §1 | §1 | §1 | §1 |
| `task_class` | ✓ | demand-ontology term. **Two-level: `class` (closed enum — candidate assignment of all 58 observed values published in §2a before this field is REQ-enforced) + `class_free` (native term, preserved)**. Measured: S3 carries **58** distinct values / 94 route_planned (v0 said 59 — corrected); top: `bounded-implementation` 8 · `web-research` 6 · `review` 5 | ∅ | ∅ — the `task` dict (15/724 spawn-req) has subkeys `kind/project/gate/tier/lens/vendor/round`, none class-bearing (v0's cell was wrong) | `task_class` |
| `route_id` | | ROUTES row (or overlay row) consulted; `none-consulted` is a legal, honest value — **the field whose absence made the 2.2% unmeasurable** | ∅ | ∅ | ∅ (new in v2) |
| `warrant_ids[]` | | W-records load-bearing for the choice | ∅ | ∅ | ∅ (new) |
| `rung` | | rung-table row fired (B-6; empty until it exists) | ∅ | ∅ | ∅ (new) |
| `requested_model` | ✓ | **normalized binding id** (`vendor:model`) + `requested_model_raw` preserved. Needed now: measured live alias drift — `terra`/`gpt-5.6-terra`/`gpt-5-6-terra` are one binding in three spellings | `model` (probe block) | `model_requested` (394/724 non-empty; null = session-inherited, map to `requested_model: null` + `surface: generic`) | `requested_model` |
| `requested_effort` | ✓ | `low/medium/high/xhigh/max/session-inherited/unspecified/unknown`. `unknown`/`unspecified` are honest members — measured: S3 `requested_effort` includes `unspecified`(4)/`unknown`(1). `max` unobserved in either corpus but retained: legal API value, ROUTES R8 reserves it | `effort` — **intent-side ONLY if emitted pre-call; the probe shows one `effort` attribute, so S1 supplies intent-effort OR observed-effort, not both** (v0 double-mapped it — corrected: S1 intent `requested_effort` = ∅, see §3) | **∅** — `effort_spawner` is the PARENT's effort (measured: explorer-light's 50 spawn-reqs carry high/xhigh/medium while all 60 child stops say medium). Child intent-effort is not captured request-side | `requested_effort` |
| `router_effort` | | NEW (from A1): the routing *driver's* own effort at decision time — the effort-inheritance detector's input | ∅ | `effort_spawner` ✓ (722/724) | ∅ |
| `requested_role` | | agent-type / roster pin name | **∅** — probe finding 4: no `subagent_type` in the stream; `agent.name` redacted to `custom`; roster identity exists only on the OUTCOME event | `subagent_type` (706/724) | `requested_role` |
| `surface` | ✓ | delivery surface (pin / per-call / generic / teams / cowork) — CONTRACT §3's control-surface question, made a field | ∅ | derivable (`tool_name`+`subagent_type`+`model_requested` nullity) | ∅ (new) |
| `harness_contract` | ✓ (v2-only) | **content hash of the in-force contract** (prompt contract + skill + gate config) + a human label + **`harness_features` struct** (small closed set: `review_gate: bool`, `claim_tagging: bool`, `tool_profile: ro/rw`, …) so two disputants can see HOW contracts differ without fetching content (panel A12/W6) | ∅ | partial: `prompt_sha256` (prompt only) + `agent_def.{path,sha256}` (1,033 stops carry the executed definition hash — a strictly better partial the v0 missed; execution-side, joins per §1a) | ∅ (new) |
| `router_model` | | who decided (self-route vs driver vs human) | ∅ | `parent_agent_id` ≈ | ∅ |
| `reason_code` | | **registered closed vocabulary** + optional `note_hash`. §6-4 requires enumerated values, and S3's `*_code` convention does NOT supply that (§0 — character class, 92-distinct/96 measured); S3 values project as `reason_code: other` + `reason_code_free` (origin-local, non-exportable unless registered) | ∅ | ∅ | `falsifier_code`, `expected_advantage_code`, `nearest_alternative` — via `other`+free slot until a registered vocabulary exists |
| `price_lineage` | | NEW (from A12/W5): `{binding, price_per_mtok_in, price_per_mtok_out, as_of}` — resolvable to STATE.md price rows; lets any tuple be re-priced later. Reserved NOW because §6.1 makes late addition a v3 | ∅ (stamp at projection from STATE) | ∅ (same) | ∅ (same) |
| S3 riders | | `reversibility`, `consequence`, `ambiguity`, `validation_oracle`, `closure_target`, `write_scope_count` — optional canonical fields (they encode the CONTRACT §1 delegation test). Caveat (A4): `validation_oracle`/`closure_target` are free-code in practice (75 and 48 distinct values) — same `other`+free-slot export rule as `reason_code` | ∅ | ∅ | ✓ native |

### 2a. The closed `class` enum — publication precondition

The candidate ~12-class assignment of all 58 observed S3 values MUST be published (as a table
in this doc or a sibling) before `task_class.class` is enforced as REQ. Panel A12 measured the
risk: the observed vocabulary is compositional along routing-relevant axes — scope
(`implementation`/`bounded-implementation`/`bounded-mechanical-implementation`…) and review
generation (`review`/`rereview` ×6 variants) — and a collapse that discards review-vs-rereview
loses exactly the discriminator a D-4 rung condition would fire on. The enum must preserve
those two axes or state the loss.

## 3. Outcome record

**Cardinality (A3/A5):** one intent record joins 0..N outcome records via `run_id` +
`outcome_ordinal` (int, 0-based). A non-terminal outcome (S3 `revise`) carries
`terminal: false`; exactly one outcome per run may carry `terminal: true`.

| field | REQ | semantics | S1 | S2 (execution-side) | S3 |
|---|---|---|---|---|---|
| ids + `v`,`ts`,`origin`,`outcome_ordinal`,`terminal` | ✓ | §1, §3 header | ✓ | ✓ (partition caveat §1a) | ✓ |
| `observed_model` | ✓ | normalized binding + `identity_source` (transcript / API / UI-label — UI labels weakest, per package doctrine) | `final_model`+`model_swapped` ✓, `identity_source: api` | `models_in_transcript` (1,872 non-empty) `identity_source: transcript`; request-side partition: `resolved_model` (650) `identity_source: api` — v0's ∅ was wrong both ways | `observed_model`+`observed_identity_source` ✓ |
| `observed_effort` | | as delivered; enum incl. `unknown` (measured: S3 `observed_effort` = `unknown` in 21/58 events — the largest observed value) | `effort` ✓ (the ONE S1 effort attribute lands here, not on intent — A7) | `effort_child` ✓ (3,300 non-empty; incl. `low`(1) and nulls → `unknown`) | `observed_effort` |
| `tokens{in,out,cache_r,cache_w}` | | **nullable, REQ-if-available** (v0's REQ was unsupplyable: S3 carries in/out in 4–5/96 and its allowlist has NO cache fields; S2 `usage_from_transcript` 428 non-empty) | ✓ (probe block) | `usage_from_transcript` when parsed | `input_tokens`/`output_tokens` when present |
| `cost_usd` | | when the platform reports it; otherwise reconstructable later from `tokens` × intent `price_lineage` — state coverage honestly: measured absent from ~86% of S2 spawn-res and all S3 v1 core events | ✓ (when enabled) | ∅ mostly | ∅ / delegations `costUSD` (n=1) |
| `disposition` | ✓ | closed enum **v0.2**: `accepted / accepted-after-rework / rejected / parked / interrupted / blocked / error / abandoned / completed-unknown` + `terminal` flag. The 12→enum mapping for all 96 live S3 values is published in §3a — v0's six-member enum matched **0/96** live values (panel A3) | partial (`subagent_completed`) | stop event → `completed-unknown` (honest: the stop hook can't see acceptance) | ✓ via §3a |
| `rework_actor` | | NEW (A3): who performed rework — `root / delegate / none / unknown`. S3's `accept-with-root-revision` vs `accept-after-revision` distinction is the most routing-relevant signal in the set; v0 destroyed it | ∅ | ∅ | derived from disposition string (§3a) |
| `rework_count` | | int | ∅ | ∅ | ✓ |
| `validator` | | what checked the output (reviewer gate id / tests / human / none) + outcome. S3's `validator_outcome` is free-code (36 distinct/96) — projects as `other`+free slot until a registered vocabulary exists (A4 rule) | ∅ | ∅ | `validator_outcome` via `other`+free |
| `friction_codes[]`,`confounder_codes[]` | | from S3; same registered-vocabulary export rule | ∅ | ∅ | ✓ |
| `attestation` | ✓ | §4 enum | `platform-emitted` | **`platform-derived`** (NEW tier — see §4: the hook PARSES a transcript; measured self-declared error telemetry: `stop_class` = `phantom-no-transcript` in 521/~1,250 stops, `transcript_parse_err` 1,468 non-empty across Jun+Jul. Calling that `platform-emitted` overstated it — A12) | `self-reported` |
| `projection` | ✓ on projected records | §4a — how this record came to exist (`native` / `projected-v1` / `heuristic-join`) | projector stamps | projector stamps | projector stamps |

### 3a. S3 disposition mapping (all 12 live values; 96 events)

| S3 value (count) | → `disposition` | `terminal` | `rework_actor` |
|---|---|---|---|
| `accept` (52) | accepted | true | none |
| `revise` (18) | accepted-after-rework *candidate* — **non-terminal interim state** | **false** | unknown |
| `accept-after-revision` (8), `accepted-after-revision` (4 — live spelling drift, normalized), `accept-with-revision` (1), `accept-after-two-revisions` (1) | accepted-after-rework | true | delegate |
| `accept-with-root-revision` (2), `accept-after-root-revision` (2) | accepted-after-rework | true | **root** |
| `park` (4) | parked | false | none |
| `reject` (2) | rejected | true | none |
| `reject-interrupted` (1), `aborted-user-intervention` (1) | interrupted | true | none |

## 4. Attestation enum (§6-3: vocabulary defined HERE)

Distinct axis from EPISTEMICS claim-grades (which grade *claims*; this grades *how a record's
content was produced*):

- `platform-emitted` — written by the platform/harness with no parsing, model, or human in the
  write path (S1 when enabled)
- `platform-derived` — **NEW (A12):** written by platform tooling that *derives* values by
  parsing artifacts, with a known error rate the record itself carries (S2's transcript-parsing
  stop hook: 42% of stops are `phantom-no-transcript`)
- `self-reported` — the acting agent wrote it about its own work (S3 today; tallied
  separately, per standing probes rule)
- `driver-attested` — the routing driver (not the executor) wrote it at decision time —
  the intent-writer target class (DR-2)
- `third-party-verified` — an independent leg re-checked the load-bearing values
  (parent-verified probe items; panel legs)
- `reproduced` — an independent origin re-ran the runnable artifact and matched
  (commons tier; unused locally today, reserved)

Ordering is informational, not a trust score; consumers filter by tier, never average across.

### 4a. `projection` — a separate axis, not an attestation tier (A12)

Every record existing at launch is projector-derived; a consumer filtering by attestation must
not confuse *provenance of content* with *provenance of the record object*. So `projection` is
its own field: `native` (written in v2 by its producer) / `projected-v1` (deterministic
projector over a v1 record — the projector version is stamped) / `heuristic-join` (§1a —
excluded from conformance claims). Attestation describes the original writer either way.

## 5. Sensitive/routing separation (§6-4 floor — v0.2: an export ALLOWLIST, names AND values)

v0 generalized "S3's posture" and enumerated 3 non-exportable S2 fields. Both halves failed
measurement (panel A2/A4): S3's mechanism bounds names, not values; and the live S2 payload
carries at least **11** content/path-bearing fields. v0.2 inverts the construction:

1. **Export is allowlist-only.** A field crosses an origin boundary only if it appears in
   §§1–3 *and* satisfies its value rule (enum member, registered vocabulary, hash, normalized
   binding id, numeric, or bounded flag). Everything else is non-exportable **by default** —
   new native fields are born non-exportable.
2. **The measured S2 non-exportables** (exhaustive over the live payload-key inventory, all 6
   record kinds, Jun+Jul): `prompt_head`, `prompt_path`, `cwd`, `description`, `project_key`,
   `last_message_head`, `transcript_path`, `agent_transcript_path`, `agent_def.path`, `reason`,
   `tool_input_head`, `error_head`, `tool_response_head`, `task.project`. (`agent_def.sha256`
   IS exportable — it is the harness-contract partial.)
3. **Free-code fields** (S3 `*_code`, `run_id`, `validator_outcome`, `validation_oracle`,
   `closure_target`): exportable only as registered-vocabulary members; otherwise they project
   as `other` + an origin-local free slot that does not export, and `run_id` exports only as
   `run_pseudonym` (§1).
4. **Consent-to-share = the §§1–3 field list, verbatim**, and with rules 1–3 in force that
   sentence is now *true*: W3's consent screen can honestly say "your prompts, code, paths,
   and free-text notes are in fields that structurally cannot leave."
5. The projector MUST machine-check rule 2 (a test enumerating live payload keys against the
   allowlist — new keys fail closed). This check is part of C-5's conformance suite.

## 6. Migration (§6's v2-with-dual-read, made concrete)

0. **Preconditions, stated (A7/A10/A11):** (a) S1 requires enabling Claude Code OTel and
   persisting it — today there is NO live S1 stream, and no S1 projector can be
   fixture-tested against history until one accrues; (b) any v2 field reaching S3's native
   stream requires the S3 owner to act (§6.4) — **a single v2 line appended to
   `events.jsonl` bricks v1 `audit`, `summarize`, and all subsequent writes** (measured:
   `append_event` → `read_events` validates every line; `schema_version != 1` raises), so
   **the v2 stream lives in a separate file** (`events-v2.jsonl` beside the v1 store, or the
   driver's own dir), never appended to a v1 store.
1. **v2 is a new stream, not an edit.** No v1 writer changes; the S3 validator keeps
   rejecting unknown fields — correctness, not obstruction.
2. **Projectors, not rewrites:** three read-side projectors (S1/S2/S3 → v2), each stamping
   `origin`, deriving missing ids, normalizing aliases and timestamps, stamping `projection`
   (§4a). Stdlib-only. **Fixtures are built from the live corpora** (222 S3 events, 4,693 S2
   records), not authored — the panel's procedural finding; authored fixtures would have
   reproduced v0's key-name errors. These fixtures ARE C-5's conformance-suite seed.
3. **Dual-read window:** consumers read v2 ∪ projected-v1 until the intent-writer (the one
   NEW writer: driver-side, `driver-attested`, carrying `route_id`/`warrant_ids`/`surface`/
   `harness_contract` — the four fields no existing source supplies) is deployed and the
   projectors are boring. **Stated plainly (A11): E-1 is BLOCKED on that writer.** All five
   ROUTES-conformance fields are ∅ in all three sources; the portfolio review's "E-1 begins
   the day B-3 lands" holds only for the outcome-side join, not the routing-conformance
   question. The intent-writer is a scoped build item surfaced with this draft (see the
   operator packet), not an implied consequence.
4. **Ownership boundary — honest form (A10):** this package owns the crosswalk + projector
   specs; S3's native schema stays owned by its Codex-side skill. **That boundary is
   currently nominal**: the owner is an unremoted local directory with no owner statement and
   no version policy beyond `SCHEMA_VERSION = 1`. C-5 must stand up the governance this
   clause assumes (named owner, versioned schema, conformance fixtures) — until then,
   proposals to S3's v2 have no counterparty and §6.3's window cannot close on the Codex side.

## 7. What this deliberately does not do

No registry, no transport, no aggregation semantics (L3). No rung-table fields beyond the
nullable `rung` slot (B-6 owns that). No live writer implementation — the intent-writer is its
own build item with its own review. No claim that the 58-value S3 task vocabulary maps
losslessly — the two-level design preserves the native term precisely because it might not,
and §2a requires the candidate assignment be published before the closed level is enforced.

## 8. Falsifiers / review targets

- A routing decision the intent record cannot express without free text → §2's enums are
  wrong, not the discipline.
- A v1 S3 record that cannot project into v2 without loss beyond the declared
  non-exportables → the crosswalk table has a hole. *(Exercised by the panel: v0 failed this
  on `disposition` 0/96 — §3a is the repair.)*
- The two-level task_class proving to be where all the information hides (everyone routes on
  `class_free`) → the closed enum is decorative and the ontology work is unfinished. *(Panel
  measured this risk live — §2a is the guard.)*
- An attestation case the six tiers cannot type → the enum needs a seventh value, define it
  then. *(Exercised: v0's five tiers could not type S2's transcript-parsing hook —
  `platform-derived` is the repair.)*
- A consent screen generated from §§1–3 that names an exportable field whose live values
  carry content → §5's allowlist has a hole; the machine-check (§5.5) failed first.
