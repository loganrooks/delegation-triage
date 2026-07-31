# PROBE — 2026-07-28 Flash pilot wave 1 (codex-orchestrated, native adapter, 2 runs)

- probe_id: P-20260728-fp-wave1-codex-native
- task class / ROUTES row: FP-A bounded implementation (pilot lane, W-026; no ROUTES row)
- configs: executor `gemini-3.6-flash-high` (effort via model alias), native
  `delegate-to-antigravity` adapter, one run per consuming repo — lectern
  (`lectern-flash-pilot-wave1`, fd-close fix, 2 owned files) and bibliometa-cli
  (`bibliometa-flash-wave1`, one-file test slice)
- router: codex-native orchestration (task_class `bounded-implementation`); router model not
  recorded in the codex events (codex-side schema has no router field) — Unchecked
- blinded?: no; adjudicator: orchestrator (non-author of the diffs), root-owned fresh
  verification both runs
- **attestation:** codex ledger `~/.codex/telemetry/orchestration-learning/events.jsonl`
  (route_planned + disposition events, 2026-07-28T03:20–03:24Z: both `disposition: accept`,
  `rework_count: 0`, validator `pass`/`approved`, `observed_model: gemini-3.6-flash-high`) +
  per-repo run reports with root-run validation:
  `lectern:.flash-pilot-report-wave1.md` ("Fresh root-owned verification … `verify: OK`")
  and `bibliometa-cli:.flash-pilot-report-wave1.md` ("Fresh root validation after diff
  review" … "**accepted**"). **Both reports are UNTRACKED in their
  repos as of 2026-07-31** — durable only as loose files; preservation risk named.
- verdict: **2/2 accepted, zero fix rounds.** Both runs first-pass accepted after
  orchestrator diff review + fresh root validation.
- fault attribution: n/a — no failure events
- detection timing: n/a
- unique catches: wave-1 reports contain no reporting-fidelity defects (the miscount/omission
  weaknesses attach to waves 2–3, not this wave)
- **tally:** feeds W-026 FP-A-native lane: +2 attested accepted (third-party-verified —
  orchestrator reran validation; artifact caveat: reports untracked). Count after this
  record: 2.
- deviations: records live codex-side only (no v2 intent/outcome pair in
  `~/.delegation/v2/` for these two run_ids — cross-ledger gap, same class as signal
  obs-20260728T041605-31eb70); reports uncommitted in consuming repos
- record backfilled 2026-07-31 by the fable campaign session from on-disk primary artifacts
  (same-pass-propagation debt: the wave predated its probe record by 3 days)
