# PROBE — 2026-07-05 sonnet-MEDIUM sweep probe (R1 medium vs PROBE-R1-high; first effort datum on sweeps)

- probe_id: P-20260705-sonnet-medium-sweep · grandfathered: true
- class: sweeps/retrieval, effort axis (W-006 medium track) · configs: sonnet×medium vs
  sonnet×high, identical lane contract + window (Jun 16–Jul 05), 12-lead caps, Workflow
  `agent()` (model/effort per-call)
- blinded: yes (lanes blind to each other) · adjudicator: author
- **attestation:** workflow journal + archived lane reports —
  SEAS:proposals/2026-07-05-adversarial-survey-memo.md §Wave-3 (+ `wave3-lane-{R1,PROBE-R1-high}.md`,
  `wave3-workflow-result.json`; extraction verbatim from `journal.jsonl`)
- measured: *"scanned 180 vs 185; leads 12 vs 12; overlap 3/12; tokens 191.5k vs 192.6k (≈1.006×)
  — the effort dial moved token cost ~0 on this observation-dominated class"*; *"neither lane
  dominated"* — medium uniquely surfaced 2606.23583 (refuting the high lane's own coverage
  overclaim, caught BECAUSE the pair existed); high uniquely held the ledger-convergence cluster;
  low overlap read as breadth-under-cap [reasoned], not tier
- **tally:** feeds W-006 medium-revert counter: **0/1**; medium = live candidate under balanced
  when paired, default under budget-conscious. Instrument: `explorer-light` pin (minted same day).
