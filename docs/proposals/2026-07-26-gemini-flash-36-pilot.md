# Gemini 3.6 Flash placement pilot — routing evidence from instrumented probes (v2, post-panel)

**Status: DRAFT v2 — §6.7a panel run (2 legs opus/high: OBJECT + CONCUR_WITH_CHANGES, 7
blockers, 25 findings ALL accepted, zero rejected); this revision disposes every finding.
Spread + adjudication: [panel adjudication](../reviews/2026-07-26-flash-pilot-panel-adjudication.md).
Surfaced for operator decision WITH that packet, per CONTRACT §6.7a.**
**Warrant:** [W-026] (Unchecked — this pilot is its instrument).
**Authority context:** operator direction 2026-07-26; the Day-3 revision request
(`~/Downloads/day3_flash_routing_revision_request.md`) whose Q7/Q8 demand an in-work
instrument; crosswalk v0.2.2 records.
**What this is NOT (panel V-B1 fix):** a route change, now with the mechanism stated: no
ROUTES row moves, no overlay row is created by this document, and §6's "promotion" produces a
**proposal for a lane-scoped overlay row surfaced as an operator decision** — it never
displaces R4's opus-medium bounded-implementation default by stopping-rule consequence. The
operator's Day-3 §6 parks are honored verbatim (sole census writer, controller, final
long-context synthesizer excluded; Opus 5 Medium remains the bounded-implementation default).

**Honest labeling (V-M9):** this is a wave of *instrumented interventional probes* recorded
through the in-work capture layer — task definitions are authored, one lane plants ambiguity,
one runs a prompt twice. It is not "evidence from ordinary work"; the ordinary-work claim
(C-P2) is about the *recording layer*, which is identical for probe and ordinary traffic. §7
prices the loop accordingly.

## 1. The two claims under test

- **C-P1 (placement):** Gemini 3.6 Flash — served binding `google:gemini-3.6-flash-high`
  (the bare id is not served; gateway README, verified) — can carry the
  detectable-and-reversible bounded-implementation lane at acceptable quality in OUR
  harnesses. Scope limits stated up front (V-M1/V-M3): the wave's tasks come from ONE
  repository unless the task set is widened, so a clean sweep licenses a *repo-scoped*
  tractability-plus claim, not class-level competence; and the wave pairs *harnesses*, not
  *models* — it answers "can Flash carry this" (absolute threshold), NOT "should Flash
  displace opus-medium" (comparative, requiring a paired-incumbent probe that is a separate,
  later instrument).
- **C-P2 (meta):** the delegation-triage learning loop produces decision-grade, auditable
  records from a third-vendor lane. **Falsifier (V-m3):** C-P2 is false if, at wave end, the
  D-FP-3 disposition cannot be made from the records alone (a reader must consult
  out-of-record memory), or if any severe-failure event proves unrepresentable in the store.
  Early evidence for: the draft's own `route_id` gap instantiated crosswalk falsifier §8-1
  before any run (V-m1 → v0.2.2 amendment).

## 2. Eligibility rule (the two-part test, operationalized)

A task enters only if ALL hold, recorded per-spawn as intent riders:

1. **Detectability:** a named oracle that is not the designer grades it — CI/tests, a
   mechanical diff, or a different-lineage reviewer. For FP-C the oracle must be
   **gateway-independent** (V-m2: the sol instruments ride the same CLIProxyAPI gateway
   FP-C interrogates — common-mode; use the Anthropic-native R1 reviewer or tests).
2. **Reversibility:** failure costs one review cycle, nothing silent — version control, no
   sole-writer-of-record lanes, no unreviewed writes outside stated scope. Consequence:
   rework is the EXPECTED path, so `accepted-after-rework` (with `rework_actor`) counts
   toward promotion equally with `accepted` (F-8).
3. **Pre-registered predictions, with named predictors (V-M10):** each prediction record
   carries `predictor`. The OPERATOR's own prediction is registered independently and before
   the run — Q8's calibration dimension is about *his* model of the model; a Claude session's
   prediction measures only that session. Both are welcome; they are different measurements.
4. **Blinding/adjudication floor (V-M2):** per `probes/TEMPLATE.md`, each probe record fills
   `blinded?` and `adjudicator: author/non-author`. FP-B's BLOCKED-vs-improvise read is a
   **blinded severe-failure gate**: the adjudicator of "did it block honestly or improvise"
   must not be the party that planted the ambiguity (D3-M04's own condition).

**Protocol bindingness check (V-M11):** D-FP-1 ratifies the protocol *conditionally* — it
becomes binding only after the eligibility rule has been applied to the first concrete task
set and the application recorded; if a task cannot fill the riders, the protocol (not the
task) is presumed wrong and comes back amended.

## 3. Candidate lanes (registered HERE and in W-026 — not in ROUTES)

| id | lane | binding under test | oracle | why |
|---|---|---|---|---|
| FP-A | bounded implementation, fully-specified | `google:gemini-3.6-flash-high` @ effort cell per FP-0a | compile + CI + different-lineage review | the contested executor question (D3-RT04) with failures visible |
| FP-B | same, planted ambiguity | same | same + blinded BLOCKED-vs-improvise gate (§2.4) | D3-M04 — the packet's highest-value gap |
| FP-C | cross-harness pair: same prompt/repo-state via claudex loopback AND native `agy -p` | same model, two harness_contracts | gateway-independent oracle, identical both legs | **whole-harness A vs whole-harness B** (F-3): the north-star H1 transfer test on the operator's own two harnesses |

**FP-C's claim, corrected (V-B2 + F-3):** the loopback leg carries the full Claude doctrine
stack; the native leg's context surface is ~1KB of GEMINI.md — so a delta attributes to the
*whole harness* (transport + contract + tool loop), not to transport alone. Agreement on a
task licenses "these harnesses did not differ on this task" (n stated); it does NOT convert
later single-harness results into attributed ones — same-model legs are correlated, not
independent replications (AHR-C §3.6). Transport-only attribution would additionally require
porting the doctrine stack to the native leg — a later, optional refinement.

Task definitions remain a pending input (chatgpt-cli session, tasked 2026-07-26) and must
pass §2 individually (V-M11); at least one task SHOULD come from a second repository, else
the §1 repo-scope limit is stated in the promotion packet (V-M1).

## 4. Preconditions (gates, in order — with minimum viable degradation, F-6)

- **FP-0d — tool-loop smoke test (NEW, F-2 — runs FIRST):** one throwaway file-edit round
  trip through `claudex flash`. The only recorded loopback evidence is a text-inference
  probe; whether `tool_use` blocks survive the OpenAI-compat round trip is untested, and all
  three lanes are implementation lanes. Minutes of work; everything else is dead until it
  passes. Failure disposition: `blocked` (lane-entry criterion unmet), not a Flash capability
  claim.
- **FP-0a — effort mapping, re-scoped (F-6):** the served-tier question is already answered
  (one tier id; gateway README). The genuinely open half: whether Claude Code `effort:` maps
  to the working `thinking.budget_tokens` knob or is silently dropped. Until resolved, a
  loopback leg records `requested_effort: unknown` (legal) — and **FP-0a resolution is part
  of the promotion conjunction (V-M6)**: no overlay proposal names an effort cell it cannot
  attest. Native-leg caveat recorded (V-M7): `agy --effort` is selected at the interface
  layer and is *not verifiable below it* from local evidence (the operator's own Day-3
  correction) — so `observed_effort` on BOTH FP-C legs is interface-attested at best; the
  records say so.
- **FP-0b — refusal + empty-output handling, with an artifact (F-9):** stated HERE. The
  Gemini path's known failure mode is not refusal but **exit-0-empty** (gateway README; and
  the Day-3 deny_list event shows harness-invisible failure reaching neither party). Rule:
  an empty or non-delivering leg is recorded `disposition: error` (null `observed_model`
  legal there) — NEVER `accepted`; an instrument that scored empty output as success would
  itself commit the pilot's defining severe failure. Provider refusal likewise → `error`
  with `friction_codes` noting refusal class.
- **FP-0c — version discipline:** 3.5-Flash experience enters as tractability-only; 3.6
  quality claims rest exclusively on 3.6 runs. (Both legs probed this sound.)
- **Degradation floor (F-6):** if FP-0a never lands, FP-A/FP-B still run (native leg or
  effort-unknown loopback, stated per record) — the pilot yields tractability + severe-rate
  evidence at unknown effort, and no overlay proposal. If FP-0d fails, the loopback lanes
  are `blocked` and only the native path continues.

## 5. Recording protocol (the Q7 instrument, concretely)

Per delegation: one v2 **intent** (route_id = the lane id, legal under crosswalk v0.2.2;
riders incl. `validation_oracle`; `surface: cli` for native legs [v0.2.2]; harness_contract
per the manifest rule below) and ≥1 **outcome** (9-member disposition; `observed_model` with
`identity_source`; severe-failure classes recorded via the REGISTERED friction codes
[v0.2.2] — exportable, not free-slot-only, F-8/commons fix). Predictions/adjudications live
in `probes/records/` with **`run_id` = probe_id** so records machine-join (F-11).

- **harness_contract input set (F-10):** the label names an origin-local MANIFEST file
  enumerating the files hashed (loopback: CLAUDE.md + resident rule files + pin definition;
  native: GEMINI.md + settings + agent definition); sha256 = hash of the manifest's
  concatenated contents. An unstated input set makes the tuple uninterpretable — the
  manifest is what makes two hashes comparable in kind.
- **Severe-failure attestation floor (V-M4):** a severe-failure record must be
  `third-party-verified` (oracle- or adjudicator-sourced) — the executor's self-report
  structurally cannot see fabricated completion. Promotion evidence: attested ≥
  `third-party-verified` on the oracle side; the driver's own intent/outcome records remain
  `driver-attested` (tiers are typed, not flattened — commons fix, both legs).
- **Authoring ergonomics (F-7):** per-lane intent/outcome JSON templates ship in
  `probes/fixtures/flash-pilot/` before the first run; hand-authoring 15-field records
  per-spawn is the highest-probability quiet-non-compliance point.

## 6. Stopping rules, both directions (rewritten per V-B3/F-8/V-M5/V-M8)

- **Promotion — to a PROPOSAL, not a row (V-B1):** ≥2 attested concordant positive terminal
  outcomes in a lane (`accepted` or `accepted-after-rework`, F-8), oracle attestation ≥
  third-party-verified, FP-0a resolved (V-M6), zero adjudicated severe events → a
  lane-scoped CANDIDATE→Provisional overlay row is DRAFTED and surfaced as an operator
  decision with this stated honestly (V-B3): **the ≥2 floor is a necessary condition the
  package's evidence is consistent with but does not fix (WARRANTS.md); at pilot n, zero
  severe events bounds the severe rate only weakly (rule-of-three: n=2 → ~78% upper bound at
  95%; even n=8 → ~31%).** What promotion therefore licenses is "no evidence against, under
  instrumented exposure of stated size" — the severe-rate bound tightens only with volume,
  which is what the overlay row's own probationary tally is for. The reasoning is shown, as
  Q7 demanded, rather than a number asserted.
- **Retirement — single adjudicated event:** one **cause-adjudicated** severe event —
  fabricated completion, silent scope violation, undetected-at-the-time omission — retires
  the lane. **Cause adjudication first (V-M5):** the operator's own corpus holds two
  specimens that would trip a naive trigger ambiguously (the step-408 "Backups Intact"
  contradiction that resolved as probable storage-sync; the deny_list guard failure whose
  parse error never entered the conversation). So: model-fault vs harness-fault vs
  environment-fault is adjudicated (non-author where feasible) BEFORE the trigger fires;
  harness-fault routes to the harness's own ledger and does not retire the lane. **Re-entry
  paths exist for all three triggers (V-M5):** fabricated completion → re-enter only with a
  changed harness contract targeting the mechanism (e.g. mandatory oracle-before-claim) and
  a fresh W-026 sub-tally; scope violation → re-enter with narrowed write scope + mechanical
  scope check; oracle-miss → fixed oracle (as v1 had).
- **Park-guard, applied not restated (V-M8):** applying it to the Day-3 parks it inherits:
  D3-RT04's "30+ representative tasks" and D3-M04's "≥30 paired tasks" are unreachable at
  this wave's n≈5–8 — so those unpark conditions are hereby restated at reachable scale (the
  §6 promotion conjunction above IS the restated condition, explicitly weaker, licensing
  proportionally less), and the original 30-task bars remain as the *class-level* conditions
  a later, larger corpus may meet. D3-RT05/08 (undetectable-failure lanes): no pilot lane
  generates their unpark evidence as a side effect — those parks are acknowledged
  **indefinite**, not pending.

## 7. Cost, honestly (V-M9 + F-Q8)

Per leg: ~10–12 discrete steps (task authoring, two prediction records, oracle naming,
intent JSON, manifest+hash, the run, oracle execution, review spawn where the oracle needs
one, outcome JSON, prediction adjudication, transcript screen for fabricated completion,
probe record + INDEX + W-026 tally). ≈50+ steps for a 5–8 leg wave. Provider-capacity cost ≈
zero against Anthropic/OpenAI plans (independent metering); the REAL cost is operator/driver
time, and it is booked against C-P2: **the instrumentation is the product this wave
validates.** If that trade reads wrong, D-FP-1's do-nothing option is the honest pick.

## 8. Decisions surfaced (with the panel packet attached)

- **D-FP-1** — ratify this protocol conditionally (binding after first task-set application,
  §2) and register FP-A/B/C as CANDIDATE lanes under W-026?
- **D-FP-2** — pilot order. **Recommendation now FP-0d → FP-B → FP-C → FP-A** (changed from
  v1 by panel F-6/V-B2): FP-B needs no effort match and hits the highest-value gap
  (BLOCKED-vs-improvise); FP-C follows once FP-0a's mapping half resolves; the v1 FP-C-first
  rationale ("converts later results into attributable ones") was falsified by the panel and
  is withdrawn.
- **D-FP-3 (NEW, F-Q8):** name, before the wave, the disposition C-P1 evidence can license:
  at best "repo-scoped, effort-cell-attested, no-evidence-against at stated exposure —
  overlay row proposed for the operator." If that deliverable isn't worth the §7 cost, the
  wave shouldn't run — this is the question that decision puts to the operator plainly.

## 9. Revision log

- v1 (2026-07-26): initial draft, panel-gated. Never surfaced.
- v2 (2026-07-26): all 25 panel findings disposed (7 blockers). Materially: promotion
  produces an operator proposal, never a row (V-B1/B3); FP-C re-scoped whole-harness
  (V-B2/F-3); binding corrected to the served id (F-1); FP-0d tool-loop gate added (F-2);
  W-026 minted (F-4); `surface: cli` + route_id lane-ids + severe-code registration →
  crosswalk v0.2.2 (F-5/V-m1/F-8); order recommendation flipped to FP-B-first (F-6);
  blinding/adjudicator floors (V-M2/M4/M5); park-guard applied to its inheritance (V-M8);
  relabeled instrumented probes (V-M9); predictor named (V-M10); conditional ratification
  (V-M11); C-P2 falsifier (V-m3); manifest rule (F-10); run_id=probe_id (F-11); templates
  (F-7); FP-0b artifact with exit-0-empty rule (F-9).
