# P-20260724 — B-3 crosswalk panel (R1 outcome observation; moves no counter)

- **What ran:** two-leg review panel on the B-3 crosswalk v0 draft per CONTRACT §6.7a+§6.8.
  Both legs `reviewer` pin @ **opus/high** via Workflow `agent()` per-call surface (dual-knob
  delivery — effort NOT session-inherited). Run `wf_c594690d-a44`; lenses: schema-correctness,
  consumer-viability. ~20 min, ~100k tokens, 26+38 tool calls per leg.
- **Outcome proxy:** verdicts OBJECT + CONCUR_WITH_CHANGES; 20 findings (6 BLOCKER). **All 12
  merged load-bearing findings survived adjudicator firsthand re-measurement — zero false
  positives.** Every disposition applied in crosswalk v0.2. Both legs independently converged
  on the same root-cause diagnosis (tables built from key names, not value distributions).
- **Routing note:** first panel run after the operator's effort correction (xhigh→high for
  opus-5 review legs); at high, both legs produced fully-grounded value-level counts
  (e.g. 1258/1258 null joins, 0/96 enum match) — no depth deficit observed vs the prior
  xhigh panel. Unpaired observation, not a comparison.
- **attestation:** parent-verified — adjudicator re-ran the measurement commands against the
  live ledgers/validator source firsthand before accepting each finding (commands in the
  adjudication doc's per-finding rows); leg outputs themselves treated as Reported until then.
- **tally:** none — moves no counter. Single-route R1 outcome observation (no paired
  comparison leg; no fable leg, so it feeds neither side of W-001's fable-vs-opus pairing).
  Kept for the instrumentation ledger + as R1 opus/high supporting context.
- **Artifacts:** [adjudication](../../docs/reviews/2026-07-24-b3-crosswalk-panel-adjudication.md) ·
  [amended draft](../../docs/proposals/2026-07-24-intent-outcome-record-crosswalk.md) ·
  workflow journal `wf_c594690d-a44` (session transcript dir).
