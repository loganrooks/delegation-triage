# B-7 intent-writer — R1 conformance review, adjudication (2026-07-26)

**Artifact:** delegation-runtime `intent-writer/` at commit `6dcfaee` (+ `49c354f` SPEC fix).
**Gate:** single R1 leg per the ratified D-B3-2 verification plan — `reviewer` pin @
**opus/high**, one lens (crosswalk conformance, over-strictness explicitly in scope),
read-only, re-runnable probe scripts left in the session scratchpad. Adjudicator: the driving
fable session (author-adjudicator confound as in the B-3 panel; mitigated the same way —
firsthand reproduction of load-bearing findings before disposition).

**Verdict: OBJECT — accepted.** 1 BLOCKER + 6 MAJOR + 6 MINOR; all thirteen findings
ACCEPTED (none rejected). The reviewer's own framing holds: repair, not redesign — the
envelope, all enums, fail-closed name discipline, and §6.0 store separation were probed sound
(19-item "found sound" list in the leg report).

## Firsthand verification (adjudicator, before acceptance)

Reproduced against a fresh scratch store with targeted CLI probes [per: delegation]:
F-1 (repo path + host:port accepted into `validation_oracle`/`closure_target`/
`confounder_codes`), F-3 (flag-path terminal `accepted` outcome written with
`observed_model: null`), F-5 (duplicate `(run_id, outcome_ordinal=0)` accepted), F-11
(`parked` + `terminal: true` accepted). F-4/F-7/F-8 accepted from the leg's cited code lines
plus prior firsthand read of the lock/append code (mechanism unambiguous). F-2/F-9/F-10/F-13
accepted from quoted code + crosswalk text. Leg report treated as Reported until these checks.

## Dispositions

| finding | severity | adjudication |
|---|---|---|
| F-1 free-code rule applied to 2/6 named fields | BLOCKER | code fix: `reason_code` treatment (registered-or-`other` + `*_free`) for `validation_oracle`, `closure_target`, `friction_codes[]`, `confounder_codes[]`. Crosswalk **[v0.2.1]** states write-time application (§2 riders row, §5.3) — the reviewer's export-scoped defeater was weighed and rejected: exportable-by-construction is the cheaper invariant |
| F-2 `orphan` undefined in schema | MAJOR | crosswalk amended (§3 row): defined as native-v2, writer-stamped, non-exportable. Writer behavior (already writer-owned, never caller-asserted) now conformant |
| F-3 `observed_model` REQ-in-name-only | MAJOR | code fix + crosswalk **[v0.2.1]** null carve-out: null legal only on `error/blocked/interrupted/abandoned`; CLI flag path must refuse the silent default |
| F-4 `spawn_ordinal` resets across month files | MAJOR | code fix: scan all store files (duplicate-id check already pays this cost) |
| F-5 join key not unique | MAJOR | code fix + crosswalk §3 header **[v0.2.1]**: reject duplicate `(run_id, outcome_ordinal)` at write and validate |
| F-6 `features` open map | MAJOR | code fix + crosswalk **[v0.2.1]**: closed to exactly the three members; extension by amendment only. Nested-name spelling (`harness_contract.features`) recorded |
| F-7 short append wedges the store | MAJOR | code fix: `os.ftruncate` to pre-write size on short write, inside the lock |
| F-8 stale-lock reclaim breaks mutual exclusion | MINOR | code fix: pid+nonce sentinel, unlink only on match |
| F-9 `note_hash` unrepresentable | MINOR | code fix: optional field added |
| F-10 `observed_model` lacks `raw` | MINOR | code fix + crosswalk §3 row notes optional `raw`. The nested-name export concern is a projector/C-5 test obligation, noted there |
| F-11 §3a pairings unenforced on natives | MINOR | code fix + crosswalk §3a **[v0.2.1]**: the table binds native records |
| F-12 two over-strictness cases | MINOR | split: `task_class.class` null-until-publication UPHELD (fail-closed side wins; now explicit in §2a **[v0.2.1]**); `router_model: human` legalized (reviewer's side wins; §2 row amended) |
| F-13 `validate --file` weaker | MINOR | README line documenting scope; no code change |

## Also surfaced by this gate (not a reviewer finding)

The run-1 "429 failure" was **not zero-output**: the first implementer spawn wrote the full
916-line implementation (attested: its agent transcript's Write call at 2026-07-25T03:01:13Z
matches the untracked file's mtime to the second) and died before tests/report. Run-2 audited
it, caught a REIMPLEMENT-constraint violation in it (near-verbatim S3 lock transcription),
rewrote that portion, and built the remaining deliverables. Ledger note: run-1's terminal
`error` disposition is true but flattens artifact salvage — logged as an E-1 schema-fitness
observation (cross-run salvage is invisible to per-run dispositions).

## Outcome

Fix list dispatched to the implementer (same R4 route, resumed teammate context); re-review
scope on the fix commit: the thirteen findings' probes plus regression of the found-sound
list. B-7 is not DONE until the fix commit passes re-check; the run-2 terminal outcome record
is written only then [per: claims-discipline].
