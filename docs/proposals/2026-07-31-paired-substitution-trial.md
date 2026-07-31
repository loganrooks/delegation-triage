# Paired substitution trial — pre-registration (pilot §6 wave-2 instrument, C′)

Status: PRE-REGISTERED 2026-07-31 under the operator-ratified pilot-closure package (C′).
**Launch condition: FP-B complete without an operator lane-retirement** (F10; the operator's
package "yes" covers design + launch-after-FP-B, no re-ask — unless FP-B goes severe, which
re-opens everything). This is the ONLY instrument that can produce an FP-A overlay-row
proposal (pilot XV-1; W-026 flip clause as corrected 2026-07-31).

## Design (per pilot §6, made concrete)

- **Arms:** `google:gemini-3.6-flash-high` (native adapter, fpc-native-manifest-v1) vs
  incumbent `anthropic:opus-5@medium` (R4 route, roster implementer surface). Identical
  frozen task set, oracle digests pinned at freeze; order counterbalanced (half the tasks
  flash-first, half opus-first, assignment fixed at freeze); patches vendor-blinded at
  adjudication (vendor markers stripped before the adjudicator sees diffs).
- **Tasks:** 6 bounded implementation tasks (≤3 owned files, deterministic oracle) drawn
  from ≥2 consuming repos, disqualifying any task either model's lineage has already
  touched in waves 1–3 (contamination screen; exclusions logged per XV-6).
- **Adjudication:** non-author, vendor-blind; every outcome gets fault-attribution +
  detection-timing rows (D-C5-1); operator countersigns.
- **Success criteria + decision rule (pre-registered, sol-4):** per arm — acceptance rate,
  rework rounds, severe events, cost (tokens/USD where metered), wall latency. An overlay
  row for the flash lane is proposed ONLY if: flash acceptance ≥ incumbent AND flash severe
  = 0 AND flash cost ≤ incumbent (any metric tie → no row; mixed result → no row, findings
  recorded). Symmetrically: incumbent severe events or acceptance < flash are recorded
  against R4's row with the same weight (the asymmetric-burden fix is the point).
- **Effort-cell naming gate (V-M6/V-M7):** the proposal may name `gemini-3.6-flash-high`
  as an effort cell only if FP-0a resolves by trial end (gateway→provider mapping attested,
  or native interface-selection explicitly accepted by the operator as the attestation
  floor, recorded as such). Otherwise the row names the model without an effort claim.
- **Minimum n:** 6 per arm, all terminal (XV-10 closure rule: denominator = all intents).

## Records

v2 intents/outcomes per run (`pst-{flash,opus}-t{1..6}-<date>`); one probe record for the
trial; W-026 + (if proposed) the overlay draft surfaced as a five-point operator decision
with a fresh §6.7a panel.
