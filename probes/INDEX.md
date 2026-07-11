# probes/INDEX — running tallies (derived; records are the source of truth)

Updated in the same pass as any new record [CONTRACT §6.5]. Counts include only **attested**
outcomes; deviated-protocol firings are counted but marked; self-reported outcomes sit in their
own column and never move a flip counter.

**Column semantics (uniform, per review 2026-07-10 lens 1 F1/F2 + lens 2 F3):** the three count
columns tally **probes bearing on THIS counter's condition** (e.g. for a demote counter,
cross-tier firings only — within-tier or unrelated probes feeding the same W-record appear in the
W-record's own tally, whose scope is "all probes feeding the warrant"). The `threshold / status`
column states how many of those probes MET the flip condition. On any discrepancy, `records/` is
the source of truth; a records→counter script check is deferred until first observed drift
(recorded do-less decision, integration record).

## Flip counters

| W-record | counter | attested-clean | attested-deviated | self-reported | threshold / status |
|---|---|---|---|---|---|
| W-001 review gates | demote fable-high → opus (cross-tier firings only) | 2 (sl-v3 gate; verifier xhigh-pair) | 3 (program-review; prix-guesser; K1) | 0 | condition approximately-met-but-confounded ×2 (sl-v3, K1) → NO demotion; needs ≥2 clean concordant unconfounded [W-019]; direction Contested |
| W-005 implementer-light | demote opus-high → sonnet | 1 | 0 | 0 | **1/3** |
| W-006 sweeps | re-tier sonnet → opus (load-bearing miss) | 2 (seeding pair; demand-intake pair) | 0 | 0 | misses **0/2** so far (flip at ≥2 of next 5) |
| W-006 sweeps (medium) | revert medium → budget-conscious-only | 1 (wave-3 pair) | 0 | 0 | misses **0/1** (flip at ≥2) |
| W-010 compilation | open sonnet composition demotion | 1 (3-leg probe) | 0 | 0 | parity **0/1**; opens on a definitions-fixed re-run ≥ parity |

## Records (chronological)

| record | class | date | attestation |
|---|---|---|---|
| [2026-07-02-bridgewright-program-review](records/2026-07-02-bridgewright-program-review.md) | review gates | 07-02 | review record + raw legs |
| [2026-07-03-warrant-verifier-xhigh-pair](records/2026-07-03-warrant-verifier-xhigh-pair.md) | review gates | 07-03 | review record + raw legs |
| [2026-07-03-prix-guesser-postmortem-gate](records/2026-07-03-prix-guesser-postmortem-gate.md) | review gates | 07-03 | review record (§7) |
| [2026-07-03-signal-layer-v3-gate](records/2026-07-03-signal-layer-v3-gate.md) | review gates | 07-03 | fused gate record, hash-pinned contract |
| [2026-07-03-k1-firing](records/2026-07-03-k1-firing.md) | review gates (deviated) | 07-03 | kit record + workflow journal |
| [2026-07-03-sonnet-implementer-light](records/2026-07-03-sonnet-implementer-light.md) | mechanical edits | 07-03 | commit + review diff |
| [2026-07-03-sweeps-paired-probe](records/2026-07-03-sweeps-paired-probe.md) | sweeps | 07-03 | raw-byte lane audit |
| [2026-07-03-warrant-compilation-3leg](records/2026-07-03-warrant-compilation-3leg.md) | epistemics compilation | 07-03 | probe result + sealed key hash |
| [2026-07-05-signal-layer-regate-pair](records/2026-07-05-signal-layer-regate-pair.md) | review gates (within-tier) | 07-05 | verbatim leg extractions |
| [2026-07-05-sonnet-medium-sweep-probe](records/2026-07-05-sonnet-medium-sweep-probe.md) | sweeps (effort) | 07-05 | workflow journal + archived lanes |
| [2026-07-10-survey-orchestrator-routing-postmortem](records/2026-07-10-survey-orchestrator-routing-postmortem.md) | R13 routing post-mortem (first `router:`-logged record) | 07-10 | run audit, operator-caught |
| [2026-07-10-stage2-execution-routing-override](records/2026-07-10-stage2-execution-routing-override.md) | routing post-mortem | 07-10 | session transcript + operator messages |
