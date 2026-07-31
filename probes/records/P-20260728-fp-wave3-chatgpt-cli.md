# PROBE — 2026-07-28 Flash pilot wave 3 (chatgpt-cli EXP-002 preflight, 5 event-chains)

- probe_id: P-20260728-fp-wave3-chatgpt-cli
- task class / ROUTES row: FP-A lane stretch — read-only review + bounded implementation +
  independent-grader roles (W-026)
- configs: executor `google:gemini-3.6-flash-high`, harness `fpc-native-manifest-v1`
  (sha `581ce82e…`), router `openai:gpt-5.6-sol` × high, session `998B27B6…`. Tasks: d1
  read-only preflight contract review, d2 bounded EXP-002 preflight implementation (+fix
  round), d3 independent EXP-002 grader (+fix round). Target project: chatgpt-cli
  (`chatgpt-cli:` in KNOWN-REPOS; EXP-002 = its capture experiment per
  `chatgpt-cli:docs/status.md`).
- blinded?: no; adjudicator: Sol orchestrator
- **attestation:** v2 ledger + codex `orchestration-learning/events.jsonl` — two independent
  ledgers, machine-joined by run_id, dispositions CONCORDANT (d1 accept/pass; d2
  revise/fail → fix1 error/`partial-artifact-unverified`; d3 revise/fail → fix1
  accept-after-revision/pass). **No committed wave-3 report located in chatgpt-cli or
  elsewhere** (swept 2026-07-31) — artifact-level attestation absent; ledger-concordance
  only.
- verdict: **first-pass acceptance 1/3 tasks; final: 2 accepted (1 after rework), 1 error.**
  The d2 implementation chain ended in `error` with validator
  `partial-artifact-unverified` — a failed fix round left standing, honestly terminalized
  (the liveness-discipline pattern, not a silent drop).
- **severe-code tension, adjudicated here (COUNTERSIGNED: operator, 2026-07-31 in-session —
  "yes" to the closure package whose first item was this countersign ask):** both first-pass
  rejections carry friction code `undetected-omission` — a code in the crosswalk's SEVERE
  set, whose W-026 clause retires the lane on a single adjudicated severe event. But the
  dispositions show both omissions were **detected at the root gate** (revise, validator
  fail) — on the crosswalk's own semantics (severe = escaped detection), these are
  detected-omissions mislabeled with the severe code's name. Adjudication (this record):
  detection timing = at the time (root gate); **lane retirement NOT triggered**; the code
  choice is a vocabulary defect to fix in C-5 (a `detected-omission` / gate-caught sibling
  is missing from the registry, so recorders reach for the severe code).
- fault attribution: d2/d3 first-pass = model (omission class), caught by harness gate;
  d2-fix1 error = unadjudicated (no located artifact distinguishes model vs environment)
- detection timing: at the time (root gate) for both omissions; unknown for d2-fix1
- **tally:** feeds W-026 as caution-side evidence, count unchanged (no committed artifact →
  below the attestation floor for positive tally; the 2 gate-caught omissions and 1 error
  are recorded against the lane's risk profile). Grader/implementation roles at this
  fidelity need the delegator re-derivation discipline the executor pins already carry.
- deviations: no wave report committed (unlike waves 1–2); d2-fix1 `observed_model: null`
  in the v2 outcome
- record backfilled 2026-07-31 by the fable campaign session from the two ledgers
