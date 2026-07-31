# Paired substitution trial — pre-registration (pilot §6 wave-2 instrument, C′)

Status: PRE-REGISTERED 2026-07-31 under the operator-ratified pilot-closure package (C′).
**HOLD UPDATE 2026-07-31: FP-B produced one severe event (t3, fabricated-completion —
P-20260731-fpb-planted-ambiguity); operator dispositioned (ii) gate-and-continue.**
Launch condition now: (a) the delegator acceptance gate G1–G4
(`probes/fixtures/flash-pilot/README.md`) is MANDATORY on every flash-arm run of this
trial, AND (b) the two-part gate spot-check passes.
**(b) MET 2026-07-31 — spot-check PASSED both parts (P-20260731-fpb-gate-spotcheck; the
live part also caught a recurrence of the adapter cwd bug, now signal
obs-20260731T200828-ee7d76): HOLD RELEASED, trial may launch.** All flash-arm packets use
the G3 preamble template. Retirement re-opens without re-ask on a severe event the gate
fails to catch (the operator's registered flip condition). This is the ONLY instrument that can produce an FP-A overlay-row
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

## Task-set freeze (2026-07-31, pre-run — XV-6; scouted by two explorer legs, reports
## preserved in the driver session; contamination screens in each report)

Baselines: workflow-gate `251b5b4` · storage-advisor `cc38138` (both trees clean at freeze).
Each leg runs in a fresh local clone of the baseline; one writer per clone.

| id | repo | task | owned files | oracle (expected) |
|---|---|---|---|---|
| T1 | wg | concurrency stress test for `fleet_count` (`hooks/preflight_gate.py:213-232`; open item `.planning/STATUS.md` "concurrency stress test … not a suite") | `tests/test_gate.py` | `python3 -m unittest discover -s tests` exit 0, OK, count >533 baseline |
| T2 | wg | unit tests for `tools/savings.py` pure functions (`find_journals`/`project_of`/`pct`; zero current coverage) + close `json.load(open(...))` handle at `:59` | `tools/savings.py`, `tests/test_savings.py` (new) | suite exit 0, OK, count >533 |
| T3 | wg | unit tests for `tools/backtest.py` (`decision_for`/`load_cases`; zero coverage) + close 2 handles (`:42`, `:80`) | `tools/backtest.py`, `tests/test_backtest.py` (new) | suite exit 0, OK, count >533 |
| T4 | wg | close unclosed handle in `component_version()` (`hooks/preflight_gate.py:109`) | `hooks/preflight_gate.py` | suite exit 0, OK, 533+ unchanged failures=0 |
| T5 | sa | regression tests for CLI `report --format text` path (`cli.py:352`→`render_text`, zero coverage) | `tests/test_cli.py` | `PYTHONPATH=src python3 -m unittest discover -s tests` exit 0, OK, count >261, skipped=1 unchanged |
| T6 | sa | subprocess smoke test for `scripts/measure_overhead.py` (documented JSON contract, zero coverage) | `tests/test_measure_overhead.py` (new) | suite exit 0, count >261; direct script run exit 0, JSON keys exact |

Deviations disclosed at freeze: sa yielded only 2 fully-verified candidates (scout flagged
the shortfall explicitly) → 4+2 split, not 3+3. Difficulty mix: 3 moderate (T1-T3) +
3 trivial (T4-T6). Counterbalance (fixed here): **T1/T3/T5 flash-arm-first · T2/T4/T6
opus-arm-first.** Both arms receive byte-identical vendor-neutral packets (G3 preamble
mandatory in both — symmetry). Adjudication blinding: per task, the two diffs are relabeled
arm-X/arm-Y with X = lexicographically-smaller diff sha256 (deterministic, vendor-blind).
Flash arm: native adapter under gate G1–G4. Opus arm: roster implementer (R4
opus × medium), same gate applied.

## Records

v2 intents/outcomes per run (`pst-{flash,opus}-t{1..6}-<date>`); one probe record for the
trial; W-026 + (if proposed) the overlay draft surfaced as a five-point operator decision
with a fresh §6.7a panel.
