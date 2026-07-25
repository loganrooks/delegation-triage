# Post-Opus-5 routing-table issues — audit and dispositions

**Date:** 2026-07-24 (committed 07-25 pass) · **Produced by:** fable leg, Cowork session (operator prompt: "there is
still a lot of issues with that routing table, given that opus 5 has released")
**Method:** R7 lane escalated to opus (stated reason: Contested vendor-source adjudication) over the
current policy snapshot @ `b141210` + the external audit corpus
(`routing-evidence/2026-07-24-opus5-fable5-routing-audit/`: REPORT.md, CLAIM_LEDGER.md, effort/orchestration
CSVs from the three system cards). Effort deltas carry the CSV's stated ±0.5-pt read precision.
**Already applied same day (not re-reported):** R1→opus high, R4→opus medium, R5→opus low,
fable-permanent STATE rows, W-004/005/010/016/017 re-graded `Unchecked for opus-5`.

Legend: **M** mechanical (no judgment) · **OP** operator ruling owed · **PR** probe owed ·
**APPLIED** = landed in the 2026-07-25 mechanical pass (this commit).

| # | Where | Issue | Evidence | Disposition |
|---|---|---|---|---|
| 1 | budget-conscious profile | `fable → R1 only` restricts fable to a class that no longer routes to it (R1→opus 07-24); premise (fable = costly tier) superseded by plan inclusion — binding constraint is a usage ceiling, not dollars | STATE `scarcity-mode` fable-permanent | **OP** — which classes fable retains under budget stance. Profile flagged STALE (APPLIED) |
| 2 | budget-conscious profile | `R7 → opus high` delta *raises* cost above base (base R7 = sonnet high since 07-17, W-023) | ROUTES R7 | **APPLIED** — delta deleted (cost-monotone) |
| 3 | budget-conscious profile | `R5 → sonnet high` economics computed against opus-high base; base now opus low; cost order inverted (sonnet intro $2/$10 vs opus-5 $5/$25) | P-20260724-r4-r5 record; STATE price-opus-5 | **OP + PR** — folds into open sonnet-high-vs-opus-low demotion probe (1/3) |
| 4 | R14 | `opus-4.8 advisor` — last live stale-model reference; plaintext-advisor fact measured on 4.8 only | WARRANTS W-022 | **APPLIED** — re-labeled `opus advisor`, opus-5 output format `Unchecked` |
| 5 | R14 vs R15 | R14's opus rationale rests on the advisor-TOOL encryption fact, yet the same row cites W-022's subagent-plaintext scope — and the package ships that subagent (R15, fable). R14's reason doesn't license excluding fable when the lane uses the subagent | ROUTES R14/R15 | **OP** — collapse R14 into R15 + base-class rows, or scope R14 explicitly to the tool |
| 6 | R13/R14 wording | Operator's fourth retained class ("driving long-horizon work") was not folded into any row | P-20260724-r1-reroute record | **APPLIED** (wording, in R1/STATE/MANIFEST strings) · **OP** remains: which row *carries* it (widen R13 vs re-route R14) |
| 7 | R10 | opus xhigh pin: closest CSV proxy (HLE no-tools) High 56.0 → XHigh 56.4 = +0.4 (inside read error); W-010 `Unchecked for opus-5`; R10 is now the **only live xhigh opus pin**, so proposal F2's `thinking: disabled`+xhigh HTTP-400 lands here alone; F4 flags AA-Omniscience hallucination +14pt as "precisely disqualifying" for this class | effort CSV; opus-5 proposal F2/F4 | **OP** (demote to high) **+ PR** |
| 8 | R2/R3 fallbacks | opus xhigh: CSV *refutes* xhigh>high on authoring-adjacent cuts (FrontierCode Main 48.0→43.6 = −4.4; Extended 58.5→56.9 = −1.6); REPORT.md: "High captures most of the reported gain" | effort CSV; REPORT.md §effort | **OP** — fallback → opus high (Concordant · Low–Moderate) |
| 9 | R13 fallback | opus xhigh + reviewer gate: REPORT routes *bounded* orchestration (R13's shape) to Opus 5 High; xhigh reserved for dynamic replanning. No Opus-5 lead-orchestrator effort sweep exists ("Opus 5 Medium is the best orchestrator" NOT established) — primary (fable high) correctly frozen | REPORT.md §7.2 | **OP** — fallback tier only |
| 10 | R15 fallback | opus xhigh is below the fable-xhigh pin (fable HLE 54.4→57.8 = +3.4, largest fable gain in CSV — pin SUPPORTED) and only +0.4 over opus high | effort CSV | **APPLIED** (annotation) · **OP** (tier) |
| 11 | R11 PARKED | Premise obsolete: W-011 conjectures fable-medium ≈ opus-*xhigh* implementation; table no longer routes xhigh for implementation. Against the new incumbent, fable medium is dominated on score AND sticker (FC Main 49.8 vs 53.4; $10/$50 vs $5/$25) | effort CSV; C16 | **OP** — close refuted-in-premise vs re-park vs new incumbent |
| 12 | Preamble | Licensing sentence cited W-016/W-017, both now Unchecked; also by the table's own rule, standing routes R2/R3 (W-002/W-003 Conjecture · Low, tally 0/0) and R4 (W-024(c) Contested) rest on non-prior-grade warrants | ROUTES preamble | **APPLIED** (Unchecked caveat) · **OP** — may standing routes rest on Conjecture warrants? |
| 13 | MANIFEST 0.3.0 stamp | "stale opus-4-8 references gone (unpack-grep)" was spelling-scoped — R14's `opus-4.8` survived it | MANIFEST :43 | **APPLIED** — claim corrected |
| 14 | MANIFEST :21/:37 | Notes rest on the superseded window premise | STATE fable-permanent | **APPLIED** (:21) · :37 superseded by 0.4.0 build row |
| 15 | STATE | No `price-fable-5` row (fable $10/$50 reachable only via a parenthetical); `price-opus-4.8-fast` now an orphan anchor (no route references 4.8) | C16 | **APPLIED** (row added) · **OP** — retire vs retain-as-historical the 4.8 row |
| 16 | Cross-class constraints | No subagent-spawn-cap constraint: O5-PG reports Opus 5 "delegates more readily", recommends explicit criteria / deterministic caps (suggested default 4) — with R1/R4/R5 all opus now, no row carries this | REPORT.md C15 | **OP** — new cross-class constraint (Concordant) |
| 17 | W-008 / R8 | Cut-name hazard: W-008's +5.3pp is FrontierCode *Diamond*; O5-SC *Main* gives fable +0.8, Extended +0.7. Direction survives (fable xhigh peaks all five CSV tasks) | effort CSV | **M** (add disambiguation note to W-008) — deferred to next WARRANTS pass, recorded here |
| 18 | R9 | Zero Sonnet-5 effort values in the audit corpus; proposal F5 concurs untouched. Pricing shift narrows the escalation premium → strengthens AVOID | CSVs (absence) | **No change · PR** (W-009's flip remains an unrun on-harness probe) |
| 19 | R7 escalation | "escalate opus high" corroborated (+0.4/+0.5 xhigh deltas inside read error; only DeepSWE +1.7 is real and out-of-class) | effort CSV | **No change** (optionally cite in W-023) |
| 20 | R5 external tension | REPORT §7.1 routes "lower-value mechanical work" to Sonnet 5 where R5 pins opus low; no source measures mechanical edits | REPORT.md §7.1; W-024(b) | **PR** — feeds the open demotion probe; does not flip |
| 21 | MANIFEST structure | Two `## Recorded deployments` headings, different schemas; section header still says "0.1.0-stage1-draft, hashed 2026-07-10" though four rows re-hashed 07-24; D-3 (`sol-*` unowned definitions) still open | MANIFEST | **M** (hygiene, next MANIFEST pass) · D-3 **OP** already registered |

## Decision queue (operator, batchable)

**A. CSV-backed fallback-tier drops** — R2/R3 fallback opus xhigh→high (#8), R13 fallback tier (#9),
R15 fallback tier (#10), R10 pin xhigh→high (#7). One ruling covers all four; every xhigh survival
in the CSVs is ≤ +0.5 except out-of-class DeepSWE.
**B. R14 collapse into R15 + base rows, tool-scope note retained (#5)** — removes the last
architectural duplication; the subagent path already exists and is cheaper to reason about.
**C. Budget-conscious profile re-derivation (#1, #3)** — or delete the profile until someone needs it.
**D. Subagent-cap cross-class constraint (#16)** — adopt the deterministic-cap sentence.
**E. Housekeeping rulings** — R11 close-vs-repark (#11); price-opus-4.8-fast retire-vs-keep (#15);
Conjecture-warrant policy (#12); D-3 sol-* adopt-or-drop.

## Probe queue (open, unchanged by this pass)

P-20260724-r4-effort-frontier (medium-incumbent vs xhigh-challenger — first run landed this session,
see the record's Run 1); sonnet-high-vs-opus-low demotion (R5, 1/3); W-009 sonnet-xhigh; R10 effort
pair if not demoted by ruling.

## Rulings applied 2026-07-25 (post-audit decision panel)

Batch A ruled "all four": #7 #8 #9 #10 APPLIED (R10 pin xhigh→high; R2/R3/R13/R15 fallbacks→high, Provisional). Batch B: #5 APPLIED (R14 tombstoned into R15). Batch C: #1 #3 SUPERSEDED (budget-conscious profile deleted until needed). Batch D: #16 APPLIED (cap-4 cross-class constraint). Record: probes/records/P-20260725-batch-tier-rulings.md.
