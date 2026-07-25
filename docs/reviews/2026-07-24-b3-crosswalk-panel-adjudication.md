# B-3 crosswalk panel — spread + adjudication (2026-07-24)

**Artifact under review:** [B-3 v0 draft](../proposals/2026-07-24-intent-outcome-record-crosswalk.md)
(intent/outcome record crosswalk). **Panel per CONTRACT §6.7a + §6.8** (commons-alignment lens
mandatory). Run `wf_c594690d-a44`, 2 legs, both `reviewer` pins at **opus/high**, read-only,
independent, ~20 min each. Adjudicator: the authoring fable session (author-adjudicator confound
disclosed — mitigated by firsthand re-measurement of every load-bearing finding before
disposition, commands in the per-finding notes below).

## Verdict spread

| leg | lens | verdict | findings |
|---|---|---|---|
| schema-correctness | every mapping cell vs live sources | **OBJECT** | 3 BLOCKER · 7 MAJOR/MINOR |
| consumer-viability | E-1 analyzer · Codex producer · W3 consent legibility | **CONCUR_WITH_CHANGES** | 3 BLOCKER · 7 MAJOR/MINOR |

Both legs independently endorse the architecture (crosswalk-not-fourth-schema, two-level
`task_class`, attestation enum, v2-as-new-stream, ownership boundary *as a goal*) and
independently reject the field-level tables. Both converged, unprompted, on the same diagnosis:
**the draft was built from key NAMES and schema SHAPE, not from value distributions** — every
blocker is a field whose name suggested one semantics and whose live values carry another.

## Adjudication — dispositions (all findings ACCEPTED; none rejected)

Adjudicator re-measured each load-bearing claim against the primary sources before accepting
[per: delegation]. Live sources: `claude-user-dir: observability/ledger/spawns-2026-0{6,7}.jsonl`
(4,693 records), `codex-user-dir: telemetry/orchestration-learning/events.jsonl` (222 events),
`codex-user-dir: skills/orchestration-learning/scripts/orchestration_learning.py` (validator).

| # | finding (merged across legs) | firsthand check | disposition in v0.2 |
|---|---|---|---|
| A1 | **BLOCKER** — S2 `effort_spawner` is the PARENT's effort, not the child's | ✓ explorer-light: 50 spawn-req effort_spawner high/xhigh/medium vs 60 stops all `effort_child: medium` | S2 intent-side `requested_effort` → ∅; new optional `router_effort` field (useful: effort-inheritance detector); outcome ← `effort_child` |
| A2 | **BLOCKER** — non-exportable list 3-of-11+; `project_key` is PLAINTEXT project names exported as the pseudonym | ✓ top values: `rookslog` 290, `bridgewright` 192, `workflow-gate` 69…; `last_message_head` 1,040 non-empty prose | §5 inverted from blocklist to **export allowlist** (names AND value shapes); `project_key` non-exportable, pseudonym derived by HMAC at projection |
| A3 | **BLOCKER** — disposition enum matches 0/96 live values; `revise` (19%) and `park` homeless; root-vs-delegate rework distinction destroyed | ✓ 12 distinct values, `accept` 52 · `revise` 18 · `park` 4; zero enum members present | enum widened + explicit 12→enum mapping table published; `terminal` flag + `outcome_ordinal` (handles `revise` and the measured 1:N run_ids); new `rework_actor` |
| A4 | **MAJOR** — S3's `CODE_RE` is a character class, not a vocabulary; §6-4 floor claimed satisfied by a mechanism that doesn't deliver it | ✓ line 133 `^[A-Za-z0-9][A-Za-z0-9._:+/@-]{0,127}$`; `observation_code` 92 distinct/96 | v2 cross-origin fields require **registered vocabularies**; S3 `*_code` values project as `other`+preserved free slot (origin-local); §5 states the name-vs-value distinction explicitly |
| A5 | **MAJOR** — S2 intent↔outcome unjoinable on any named key; S3 `run_id` is 1:N; `run_id` values carry project names | ✓ `tool_use_id_at_stop` None 1258/1258; 4 run_ids with >1 disposition; run_id samples are feature-named | S2 declared **two partitions** with honest join table; `outcome_ordinal`; run_id hashed on export (`run_pseudonym`) |
| A6 | **MAJOR** — effort enum can't express `unknown`(21/58 observed)/`unspecified`/null; `max` unobserved | ✓ | `unknown`/`unspecified` added as honest members; `max` retained with stated reason (legal API value, ROUTES R8 reserves it) |
| A7 | **MAJOR** — three S1 cells contradict the OTel probe (no `subagent_type` in stream; no `project_key` attribute; one `effort` field read as both intent and outcome); **S1 is not enabled** — a capability, not a live stream | ✓ settings.json env has no telemetry keys | S1 column restated strictly from the probe's verbatim attribute blocks; marked **prospective-on-enablement**; enablement named a migration precondition |
| A8 | **MAJOR** — `tokens` REQ unsupplyable by S3 (cache fields not in allowlist; in/out present 4–5/96); S2 `observed_model` wrongly ∅ (`resolved_model` 650, `models_in_transcript` 1,872 non-empty) | ✓ key inventory | tokens → nullable; S2 model cells mapped with `identity_source: transcript` |
| A9 | **MAJOR** — rekey rule unimplementable (no rotation path, no record fields, needs the paths §5 forbids); **shared salt = dictionary attack** over low-entropy paths | ✓ `os.O_CREAT\|os.O_EXCL` write-once salt; no rotation code | rekey record fields specified (v2-only); local path→pseudonym retention table stated; **shared-salt struck** — cross-origin join is per-pair reveal only |
| A10 | **BLOCKER** — §6.4 ownership boundary is **nominal**: S3 owner is an unremoted local git dir, no owner statement, version = a Python constant; a single v2 line in `events.jsonl` bricks v1 audit/summarize/writes | ✓ `append_event`→`read_events` validates every line; `schema_version != 1` raises | v2 store path named (separate file); S3-owner cooperation stated as a §6.3 precondition; boundary recorded as *currently nominal* — C-5 must stand up the governance it assumes |
| A11 | **MAJOR** — every ROUTES-conformance field (`route_id`,`warrant_ids`,`rung`,`surface`,`harness_contract`) is ∅ in all three sources ⇒ **E-1 is blocked on the intent-writer**, and "E-1 begins the day B-3 lands" (portfolio review) is false as drafted | ✓ validator allowlist has no such fields | Stated plainly in §6; portfolio review corrected by addendum [per: propagation]; intent-writer scoping surfaced to operator (see "Decisions surfaced" below) |
| A12 | **MINOR** — measured-claim errors: 58 not 59 task classes; S2 `task` dict has no class-bearing subkey; `ts` are epoch STRINGS; S3 `event_id` is UUID4 not ULID; §4 has no tier for projected records; `spawn_ordinal` dropped vs two prior artifacts; no price-lineage slot (W5); `harness_contract` hash alone can't resolve W6 disputes | ✓ 58 distinct; UUID4 sample; env keys | all corrected; `projection` field added (separate from attestation) + `platform-derived` tier; `spawn_ordinal` restored REQ; `price_lineage` slot reserved; `harness_features` struct added |

## Commons-alignment (CONTRACT §6.8) — adjudicated

Both legs returned structured verdicts; they agree on the shape:

- **Moves toward:** crosswalk-over-rewrite (commitment #1, pays at n=1); two-level task_class
  (#3, no scalar collapse); attestation enum with `self-reported` tallied separately (#4) and
  anti-averaging rule; refusal of cross-origin-stable pseudonyms (the strongest privacy decision
  in the draft); v2-as-new-stream verified necessary against the validator source.
- **Foreclosure findings (argued, not asserted):** as drafted, **W3 (passive contributor) was
  foreclosed** — the consent screen would have been a falsehood (A2, A4); **W5 (budget user)
  softly foreclosed** — no price lineage and §6.1 makes late addition a v3 (A12); **W6 (dispute)
  at risk** — the decisive `harness_contract` field empty at launch everywhere (A11), and a bare
  hash tells disputants only that contracts differ, not how. v0.2 addresses all three *because
  the lens was mandatory* — this is the second consecutive panel where the §6.8 foreclosure
  check caught what the correctness lens alone would have shipped.

## What the panel could not check (declared)

Both legs are Claude-lineage (opus/high ×2) — no cross-vendor leg; the gateway was not available
to the workflow run. Single-vendor spread disclosed per §6.7a. The value-level re-derivation in
v0.2 was performed by the adjudicator (author), not a third leg — the standing remedy (projector
fixtures built from live corpora, C-5) is the durable check.

## Decisions surfaced to the operator (with this packet)

**D-B3-1 — sign off crosswalk v0.2?** Recommendation: YES. All 20 panel findings accepted and
firsthand-verified; the architecture both legs endorsed is unchanged; the field tables are now
value-grounded. Load-bearing assumption: the live corpora sampled (4,693 S2 + 222 S3 records)
are representative of future traffic. Flip: a routing decision v0.2's enums cannot express
(falsifier §8.1). Do-nothing: v0 stays DRAFT and E-1's outcome-side join stays unbuilt too.

**D-B3-2 — scope the intent-writer now?** The panel showed E-1's routing-conformance half is
blocked on it (A11). Recommendation: register it as the next build item (driver-side,
`driver-attested`, the four ∅ fields), scoped small — a per-spawn JSONL writer in the driver
session, no daemon. Options: (a) register + build next session [recommended]; (b) fold into
C-5; (c) defer — accepts that "did routing follow ROUTES" stays unmeasurable. Load-bearing
assumption: the driver session can write at spawn time without harness changes (the S2 hook
path proves the write point exists). Flip: if the write point requires harness cooperation we
don't have, (b) becomes right.
