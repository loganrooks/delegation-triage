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
| framing/advisor checkpoint (R15) | demote advisor fable → opus | 0 | 1 (P-20260717 pair: counsel-assisted + advisor-preamble symmetry caveat) | 0 | **0 clean** — no flip [W-019]; direction: fable leg preferred (severity-weighted, author-adjudicated); verdicts diverged, both legs' uniques adopted → complementarity robust |
| harness-compensation (NEW) | route framing reviews to fable-authored-contract + opus executor | 0 | 0 | 0 | registered (P-20260717-harness-compensation-registration), pending trigger; flip needs ≥2 clean concordant [W-019] |

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
| [P-20260712-signal-layer-proposal-f-review-pair](records/P-20260712-signal-layer-proposal-f-review-pair.md) | review gates (cross-tier, deviated: author-adjudicator; operator-directed opus leg) | 07-12 | parent-session transcript + committed synthesis (signal-layer b3aea1b) |
| [P-20260717-signal-layer-framing-probe-pair](records/P-20260717-signal-layer-framing-probe-pair.md) | framing/advisor checkpoint (cross-tier; CLOSED deviated: counsel-assisted adjudication, author-rec adopted; advisor-preamble symmetry caveat Unchecked) | 07-17 | pre-registered before legs ran; prompt byte-identity attested; model ids measured from subagent JSONLs; operator ruling in session transcript |
| [P-20260717-harness-compensation-registration](records/P-20260717-harness-compensation-registration.md) | harness-compensation (SYSTEM probe: fable-authored contract + compensated opus vs bare fable; REGISTERED, pending trigger = next signal-layer gate review) | 07-17 | registration only — rubric + predictions PH-1..3 pre-registered; operator-authorized 2026-07-17 |
| [P-20260717-sol-code-reviewer-b20-known-answer](records/P-20260717-sol-code-reviewer-b20-known-answer.md) | review gates (cross-vendor known-answer, deviated: blinding breach via worktree refs at call 42; author-adjudicator; minors axis prompt-confounded — amended) | 07-17 | subagent JSONL + goal ledgers as key; MAJOR-1 repro re-run first-hand; prompt texts compared verbatim |
| [P-20260717-sol-fable-b16-paired-review](records/P-20260717-sol-fable-b16-paired-review.md) | review gates (cross-vendor paired, IDENTICAL charter, blinded, archive-frozen tree; deviated: author-adjudicator only) — resolves the B20 prompt-confound hypothesis; sol-unique MAJOR fable missed | 07-17 | both leg JSONLs + adjudicator first-hand repros + fix commit 5255883 (PR #25) |
| [P-20260717-sol-fable-b23-sequential-lanes](records/P-20260717-sol-fable-b23-sequential-lanes.md) | review gates (cross-vendor SEQUENTIAL lanes — no dominance reading licensed; lane-yield + false-positive data only): sol 2 VITAL + 0 false-pos (n=3 streak), fable pre-clear data-loss MAJOR, codex force_download unique | 07-17 | ledger rows rev-20260718T02563*/rev-20260718T025704 + adjudicator first-hand repros + fix commits 562dc0a/935e4d4 (PR #27) |
