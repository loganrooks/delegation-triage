# ROUTES — the per-spawn surface

Curated, evidence-graded prior router by design — no learned router at our data scale [W-018];
effort defaults follow the dial's measured shape [W-016, W-017 — both `Unchecked for opus-5`,
renewal probes open]. Read with [`STATE.md`](STATE.md) (active profile · scarcity · expiry —
expired entry = Unchecked). Warrants load on demand from [`WARRANTS.md`](WARRANTS.md) by W-ID — a
route whose warrant says Contested or Conjecture is a probe to run, not a prior to trust.
Provenance, ruling quotes, dates, and evidence for every row live in
`ROUTE-HISTORY.md` (canonical repo only, not packaged into adapters) — load only when auditing
a route, never for routing.
Precedence: **project overlay > profile delta > this table** (CONTRACT §5). Route effort is
delivered only by a roster pin or a per-call `{model, effort}` surface — generic spawns inherit
session effort (CONTRACT §3).

**Fable-retained classes** (operator 2026-07-24): orchestration · decomposition · brainstorming ·
driving long-horizon work.

| # | Task class | Route | Fallback (no-fable) | Warrants |
|---|---|---|---|---|
| R1 | Review gates / adversarial verification | **opus high** (`reviewer` pin); keep ≥2 independent lenses on high-stakes artifacts · cross-vendor lens CANDIDATE: gpt-5.6-sol high for code (`sol-code-reviewer`) / sol xhigh for design (`sol-design-reviewer`) — gateway (`claudex`) sessions only | same; xhigh per stated reason; fable per stated operator request | W-001, W-019 |
| R2 | Architecture / design / contract & rubric authoring | **fable high** | opus high + reviewer gate (Provisional) | W-002 |
| R3 | Front-end design | **fable high** | opus high (Provisional) | W-003 |
| R4 | Coding / agentic implementation | **opus medium** (`implementer` pin; Provisional — W-024(c) Contested, effort-frontier probe open); xhigh/high per stated reason | same; xhigh per stated reason | W-004, W-020, W-024, W-025 |
| R5 | Mechanical, fully-specified edits | **opus low** (`implementer-light` pin; Provisional — W-024(b)); sonnet demotion probe open | same; high per stated reason | W-005, W-024 |
| R6 | Sweeps / retrieval | **sonnet high** (`explorer-light` runs the medium probe); diverse lanes over higher tier | same | W-006 |
| R7 | Deep-read / adversarial verify / synthesis | **sonnet high** default (`explorer` pin); escalate **opus high** per stated judgment-discrimination reason (adversarial refutation, methods adjudication, many-source conflicting synthesis); xhigh per stated reason; escalation is evidence-driven — cheap-tier output failing review is the trigger | same | W-007, W-016, W-023 |
| R8 | Hardest frontier forks | **fable xhigh**; `max` reserved | opus xhigh + multi-lens panel | W-008, W-017 |
| R9 | Sonnet 5 at xhigh | **AVOID pending probe** (cost-efficiency posture, not a capability claim) | — | W-009 |
| R10 | Structured epistemics compilation (claim → typed record) | **opus high** (Provisional) or cross-vendor xhigh; sonnet candidate for kind-typing ONLY | same | W-010 |
| R11 | fable-medium as implementer | **PARKED** | — | W-011 |
| R12 | Browser-automation legs (hostile web surfaces) | **CANDIDATE — Class B, unadjudicated:** sonnet-5 high, extended thinking ON | session model (current practice stands) | W-012 |
| R13 | Multi-lane wave orchestration (design + synthesis of a delegated wave) | **fable high** (`orchestrator` pin; enumerated class) · scope-refinement CANDIDATE [W-025(b)], unexecuted: opus high for bounded fan-outs | opus high + reviewer gate on the synthesis (Provisional) | W-002, W-024, W-025 |
| R14 | *(merged into R15, 2026-07-25)* | Long-horizon executor lanes route on their base class row; the advisor-TOOL constraint lives in R15 | — | W-022 |
| R15 | Strategy checkpoint (advice-only, curated snapshot, single bounded turn) | **CANDIDATE — fable xhigh** (`advisor` pin; SUBAGENT only — the advisor TOOL returns encrypted output and fails transcript-ground-truth, W-022); local probe owed, incl. a high-vs-xhigh pair | opus high (capability drop, not a substitution; Provisional) | W-022 |

**Class discriminator (R1 vs R7):** R1 = a VERDICT on a finished artifact (gate); R7 =
verification embedded in a reading/synthesis task. "Adversarially verify X" where X ships → R1;
where X informs your own synthesis → R7.

**Cross-class constraints:** dual-use-adjacent + unattended + API ⇒ **not fable** unless the
harness handles `stop_reason: refusal` or opts into fallback (W-013) · **any unattended run
handles refusal on ALL three models** — sonnet-5 has its own HTTP-200 refusal surface (W-013) ·
ZDR / no-30-day-retention workloads ⇒ **fable excluded** (W-013) · every fable route and every
ingested fable benchmark states its **fallback configuration** (W-014) · fixed-step
transformations prefer scripts over agents (W-021; CONTRACT §2) · **judgment floor at sonnet:**
where the deliverable is a claims-discipline verdict (R7 verification; the judgment layer of any
task), do NOT route below sonnet; pure coverage / retrieval (R6) is not covered by this floor ·
**subagent-spawn cap:** opus-5 orchestrating spawns state an explicit concurrency cap (default 4)
or a stated reason for more.

**Cowork/consumer note:** where no pin or per-call effort surface exists (Cowork), the effort
column is ADVISORY — generic spawns inherit session effort; state "effort: session-inherited" per
spawn (CONTRACT §3). Model IS pinnable per-call in Cowork (incl. fable); scarcity mode still
governs fable use.

## Profile deltas (the `Active:` selector lives in STATE.md)

A profile is a set of deltas on the table above; warrant and flip columns never change with budget
stance. A profile that changes a pinned route also needs the pin edited — flip both in one commit
until a profile-flipper exists.

| Profile | Deltas vs base |
|---|---|
| **balanced** | none |
| **budget-conscious** | deleted 2026-07-25 — re-derive when first needed (see ROUTE-HISTORY.md) |
| **quality-max** | define when first needed |
