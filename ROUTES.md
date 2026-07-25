# ROUTES — the per-spawn surface

This table is a curated, evidence-graded prior router by design — no learned router at our data
scale [W-018]; effort defaults follow the dial's measured shape (high = sweet spot; top tiers per
stated reason) [W-016, W-017; both `Unchecked for opus-5` since 2026-07-24 — renewal probes open]. Read together with [`STATE.md`](STATE.md) (active profile ·
scarcity mode · expiry — expired state = Unchecked). Warrants load on demand from [`WARRANTS.md`](WARRANTS.md) by W-ID; a route whose
warrant says Contested or Conjecture is a probe to run, not a prior to trust. Precedence:
**project overlay > profile delta > this table** (CONTRACT §5). Route effort is delivered only by
a roster pin or a per-call `{model, effort}` surface — generic spawns inherit session effort
(CONTRACT §3).

| # | Task class | Route | Fallback (no-fable) | Warrants |
|---|---|---|---|---|
| R1 | Review gates / adversarial verification | **opus high** (`reviewer` pin re-pointed 2026-07-24, operator ruling: "opus 5 is now the model… you can get away with opus high for reviews" — fable retained for orchestration/decomposition/brainstorming/driving-long-horizon-work classes (operator clarification 2026-07-24), see R13) — keep ≥2 independent lenses on high-stakes artifacts · **cross-vendor lens CANDIDATE:** `sol-code-reviewer` (gpt-5.6-sol high) for code / `sol-design-reviewer` (xhigh) for design — gateway (`claudex`) sessions only; n=1 deviated known-answer datum (P-20260717-sol-b20: blind catch of the hardest MAJOR w/ executable repro, 0 false positives) | same; xhigh per stated reason; fable per stated operator request | W-001, W-019 |
| R2 | Architecture / design / contract & rubric authoring | **fable high** | opus high + reviewer gate (xhigh dropped 2026-07-25, operator ruling — FrontierCode Main favors high by 4.4; Provisional) | W-002 |
| R3 | Front-end design | **fable high** | opus high (xhigh dropped 2026-07-25, operator ruling; Provisional) | W-003 |
| R4 | Coding / agentic implementation | **opus medium** (`implementer` pin re-pointed 2026-07-24, operator ruling "opus medium for most things" — **Provisional**: adopts the O5-SC leg of a still-**Contested** vendor pair [W-024(c)]; xhigh/high per stated reason) — **effort-frontier probe stays OPEN (P-20260724), now testing incumbent medium vs xhigh challenger; the ruling does not close it**; 2nd concordant reading (documentary) [W-025(a)] | same; xhigh per stated reason | W-004, W-020, W-024, W-025 |
| R5 | Mechanical, fully-specified edits | **opus low** (`implementer-light` pin re-pointed 2026-07-24, operator ruling — **Provisional**; W-024(b): low's shape is benchmark-dependent and unmeasured on mechanical edits); sonnet demotion probe re-scoped to sonnet high vs opus low | same; high per stated reason | W-005, W-024 |
| R6 | Sweeps / retrieval | **sonnet high** (`explorer-light` runs the medium probe); diverse lanes over higher tier | same | W-006 |
| R7 | Deep-read / adversarial verify / synthesis | **sonnet high** default (`explorer` pin re-pointed 2026-07-17, operator ruling — sonnet-first, harness carries the discipline); escalate **opus high** per stated judgment-discrimination reason (adversarial refutation, methods adjudication, many-source conflicting synthesis); xhigh per stated reason. Escalation is evidence-driven: cheap-tier output failing review = the trigger | same | W-007, W-016, W-023 |
| R8 | Hardest frontier forks | **fable xhigh**; `max` reserved | opus xhigh + multi-lens panel | W-008, W-017 |
| R9 | Sonnet 5 at xhigh | **AVOID pending probe** (cost-efficiency posture, not a capability claim) | — | W-009 |
| R10 | Structured epistemics compilation (claim → typed record) | **opus high** (xhigh dropped 2026-07-25, operator ruling batch-A — was the last live xhigh opus pin, carried the F2 `thinking:disabled`+xhigh HTTP-400 exposure; HLE delta +0.4 inside read error; Provisional) or cross-vendor xhigh; sonnet candidate for kind-typing ONLY | same | W-010 |
| R11 | fable-medium as implementer | **PARKED** | — | W-011 |
| R12 | Browser-automation legs (hostile web surfaces) | **CANDIDATE — Class B, unadjudicated:** sonnet-5 high, extended thinking ON | session model (current practice stands) | W-012 |
| R13 | Multi-lane wave orchestration (design + synthesis of a delegated wave) | **fable high** (`orchestrator` pin; enumerated class) — **scope-refinement CANDIDATE [W-025(b)]:** external taxonomy scopes fable's premium to *persistent-async / dynamic-decomposition / days-scale* orchestration, with **opus high** for *bounded* fan-outs (known lanes, one synthesis); surfaced to the operator via panel, not executed — fable-row moves stay blocked (W-024(d): no controller-isolation measurement exists) | opus high + reviewer gate on the synthesis (xhigh dropped 2026-07-25, operator ruling batch-A; concordant W-025 bounded-fan-out tier; Provisional) | W-002, W-024, W-025 |
| R14 | *(merged into R15, 2026-07-25 operator ruling batch-B)* | Row retired: its opus-only rationale held only for the encrypted advisor **TOOL**; the plaintext advisor **SUBAGENT** path (W-022) is the shipped pattern — see R15 and the advisor-tool constraint below. Long-horizon executor lanes route on their base class row | — | W-022 |
| R15 | Strategy checkpoint (advice-only, curated snapshot, single bounded turn) | **CANDIDATE — fable xhigh** (`advisor` pin; subagent → plaintext on any model, the advisor TOOL (encrypted output, fails transcript-ground-truth) remains excluded — subagent path only (absorbed from retired R14); xhigh reason: single turn pays effort once, judgment-dense; local probe owed, incl. a high-vs-xhigh pair) | opus high (ruled 2026-07-25: capability drop vs the fable-xhigh pin, not a substitution — O5-SC HLE opus xhigh only +0.4 over high; Provisional) | W-022 |

**Class discriminator (R1 vs R7):** R1 = a VERDICT on a finished artifact (gate); R7 =
verification embedded in a reading/synthesis task. "Adversarially verify X" where X ships → R1;
where X informs your own synthesis → R7.

**Cross-class constraints:** dual-use-adjacent + unattended + API ⇒ **not fable** unless the
harness handles `stop_reason: refusal` or opts into fallback (W-013) · **any unattended run
handles refusal on ALL three models** — sonnet-5 has its own HTTP-200 refusal surface (W-013) ·
ZDR / no-30-day-retention workloads ⇒ **fable excluded** (W-013) · every fable route and every
ingested fable benchmark states its **fallback configuration** (W-014) · fixed-step
transformations prefer scripts over agents (W-021; CONTRACT §2) · **judgment floors at sonnet:**
where the deliverable is a claims-discipline verdict (R7 verification; the judgment layer of any
task), do NOT route below sonnet — haiku carries coverage but fails the judgment layer
(P-20260720 logs-verification triad, n=1 post-hoc: haiku overclaimed and missed the one
load-bearing discrepancy, while both sonnet legs caught it and scoped what they could not check).
Pure coverage / retrieval (R6) is not covered by this floor. · **subagent-spawn cap (adopted 2026-07-25, operator ruling batch-D, per O5-PG via W-025):** opus-5 orchestrating spawns state an explicit concurrency cap (default 4) or a stated reason for more — Opus 5 delegates more readily than 4.8.

**Cowork/consumer note:** where no pin or per-call effort surface exists (Cowork), the effort
column is ADVISORY — generic spawns inherit session effort; state "effort: session-inherited" per
spawn and treat effort-critical routes accordingly (CONTRACT §3). Model IS pinnable per-call in
Cowork (incl. fable — observed 2026-07-10); scarcity mode still governs fable use.

## Profile deltas (the `Active:` selector lives in STATE.md)

A profile is a set of deltas on the table above; warrant and flip columns never change with budget
stance. A profile that changes a pinned route also needs the pin edited — flip both in one commit
until a profile-flipper exists.

| Profile | Deltas vs base |
|---|---|
| **balanced** | none |
| **budget-conscious** | deleted 2026-07-25 (operator ruling batch-C) — deltas predated opus-5 repricing and the 07-24/25 re-routes; re-derive from docs/reviews/2026-07-24-post-opus5-routing-issues.md #1–#3 when first needed |
| **quality-max** | define when first needed |
