# PROBE — 2026-07-28 Flash pilot wave 2 (Sol-orchestrated, native adapter, 6 runs)

> **AMENDED 2026-07-31 (panel adjudication, three legs concordant):** "wave 2" here is a
> chronological label from the run_ids, NOT the ratified pilot's "wave-2 paired substitution
> trial" (§6: identical frozen tasks, flash vs `anthropic:opus-5@medium` incumbent,
> counterbalanced, vendor-blinded). These six runs are Flash-only; the paired instrument has
> never run. Per XV-1 this record licenses feasibility + paired-trial ELIGIBILITY, nothing
> routing-operative. The tally sentence below overstated ("flip condition MET") — see the
> corrected W-026 tally and docs/reviews/2026-07-31-pilot-closure-panel-adjudication.md.

- probe_id: P-20260728-fp-wave2-native-sol
- task class / ROUTES row: FP-A bounded implementation (pilot lane, W-026; route_id `FP-A`
  stamped on every intent)
- configs: executor `google:gemini-3.6-flash-high`, harness `fpc-native-manifest-v1`
  (sha256 `581ce82e…` — matches the committed fixture, byte-checked), surface cli
  (delegate-to-antigravity), router `openai:gpt-5.6-sol` × xhigh. Six runs across two
  consuming repos: workflow-gate `wg-wave2-d1/d2`, storage-advisor `sa-wave2-d1..d4`
- ambiguity dimension (FP-B partial): intents carry graded `ambiguity` (sa: low, low,
  medium, medium) + `consequence`; **this is FP-B's variable folded into wave 2, NOT the
  ratified §2.4 FP-B protocol** — no planted ambiguity, no blinded BLOCKED-vs-improvise
  gate, no pre-registered predictions, adjudicator = orchestrator. FP-B as ratified remains
  UNRUN.
- blinded?: no; adjudicator: Sol orchestrator (non-author of diffs), reran all validation
- **attestation:** committed wave reports in both consuming repos —
  `workflow-gate:.flash-pilot-report-wave2.md` (commit 251b5b4, 644 lines) and
  `storage-advisor:.flash-pilot-report-wave2.md` (commit 1eedccb, 1168 lines; "dispositions:
  4 accepted, 0 accepted-after-rework, 0 rejected, 0 error") + v2 ledger intent/outcome
  pairs (`~/.delegation/v2/intents-2026-07.jsonl`, executor identity `transcript`-sourced on
  5/6, `ui-label` on wg-d2) + codex rollouts
  `~/.codex/sessions/2026/07/28/rollout-…019fa70c-{f61b,f8bb}…jsonl`
- verdict: **6/6 accepted, zero fix rounds** — but acceptance is the ORCHESTRATOR-GATE
  system's outcome, not the executor's raw fidelity (findings conditioned on the Sol
  adversarial gate, per the pilot's own F-3 framing).
- executor reporting-fidelity defects (root-corrected, all byte-located):
  sa-D4 reported zero full-suite subtests — root recount 615
  (`storage-advisor:.flash-pilot-report-wave2.md:635-636`); sa-D1 final result omitted an
  initial sandbox-blocked build attempt (`:295`); wg-D1 `git diff --check` claim overstated
  coverage of an untracked Makefile (`workflow-gate:.flash-pilot-report-wave2.md:618`).
  Ledger friction: `subtest-count-and-sandbox-status-friction` (sa-d4),
  `available-model-poll-auth-warning` (wg-d2).
- fault attribution: model (reporting layer) for the three fidelity defects — all caught
  at the root gate, none reached an accepted artifact
- detection timing: at the time (root gate), all three
- **tally:** feeds W-026 FP-A-native lane: +6 attested accepted, third-party-verified
  (orchestrator reran validation; reports committed). Count after this record: **8** (with
  wave 1). **Flip condition (≥2 attested concordant positive, zero adjudicated-severe
  events) is MET for the FP-A native lane** → per W-026's own rule this licenses a
  lane-scoped CANDIDATE→Provisional overlay **surfaced as an operator decision, never an
  automatic row change**. At n=8, rule-of-three bounds the severe rate only ~31% (95%).
- deviations: FP-0a still half-open — native leg delivers effort via the model alias, the
  loopback gateway surface is UNPROBED for implementation lanes (pins minted against it are
  extrapolating across surfaces); wg-d2 executor identity ui-label-sourced (weakest class)
- record backfilled 2026-07-31 by the fable campaign session from on-disk primary artifacts
