# ROUTES — the per-spawn surface

This table is a curated, evidence-graded prior router by design — no learned router at our data
scale [W-018]; effort defaults follow the dial's measured shape (high = sweet spot; top tiers per
stated reason) [W-016, W-017]. Read together with [`STATE.md`](STATE.md) (active profile ·
scarcity mode · expiry — expired state = Unchecked). Warrants load on demand from [`WARRANTS.md`](WARRANTS.md) by W-ID; a route whose
warrant says Contested or Conjecture is a probe to run, not a prior to trust. Precedence:
**project overlay > profile delta > this table** (CONTRACT §5). Route effort is delivered only by
a roster pin or a per-call `{model, effort}` surface — generic spawns inherit session effort
(CONTRACT §3).

| # | Task class | Route | Fallback (no-fable) | Warrants |
|---|---|---|---|---|
| R1 | Review gates / adversarial verification | **fable high** (`reviewer` pin) — keep ≥2 independent lenses on high-stakes artifacts | opus high; xhigh per stated reason | W-001, W-019 |
| R2 | Architecture / design / contract & rubric authoring | **fable high** | opus xhigh + reviewer gate | W-002 |
| R3 | Front-end design | **fable high** | opus xhigh | W-003 |
| R4 | Coding / agentic implementation | **opus xhigh** (`implementer` pin) | same | W-004, W-020 |
| R5 | Mechanical, fully-specified edits | **opus high** (`implementer-light` pin); sonnet = open demotion probe | same | W-005 |
| R6 | Sweeps / retrieval | **sonnet high** (`explorer-light` runs the medium probe); diverse lanes over higher tier | same | W-006 |
| R7 | Deep-read / adversarial verify / synthesis | **opus high**; xhigh per stated reason | same | W-007, W-016 |
| R8 | Hardest frontier forks | **fable xhigh**; `max` reserved | opus xhigh + multi-lens panel | W-008, W-017 |
| R9 | Sonnet 5 at xhigh | **AVOID pending probe** (cost-efficiency posture, not a capability claim) | — | W-009 |
| R10 | Structured epistemics compilation (claim → typed record) | **opus xhigh** or cross-vendor xhigh; sonnet candidate for kind-typing ONLY | same | W-010 |
| R11 | fable-medium as implementer | **PARKED** | — | W-011 |
| R12 | Browser-automation legs (hostile web surfaces) | **CANDIDATE — Class B, unadjudicated:** sonnet-5 high, extended thinking ON | session model (current practice stands) | W-012 |
| R13 | Multi-lane wave orchestration (design + synthesis of a delegated wave) | **fable high** (`orchestrator` pin; enumerated class) | opus xhigh + reviewer gate on the synthesis, stated reason | W-002 |
| R14 | Advisor-augmented executor lanes (long-horizon lanes where most turns are mechanical but the plan is crucial) | **CANDIDATE — unadjudicated, no local probe:** sonnet executor + **opus-4.8 advisor** (plaintext = auditable advice; a fable advisor via the advisor TOOL is encrypted — fails transcript-ground-truth unless the advice is expendable; scope: the tool only — an advisor SUBAGENT returns plaintext on any model, W-022) | run the lane per its base class row | W-022 |

**Class discriminator (R1 vs R7):** R1 = a VERDICT on a finished artifact (gate); R7 =
verification embedded in a reading/synthesis task. "Adversarially verify X" where X ships → R1;
where X informs your own synthesis → R7.

**Cross-class constraints:** dual-use-adjacent + unattended + API ⇒ **not fable** unless the
harness handles `stop_reason: refusal` or opts into fallback (W-013) · **any unattended run
handles refusal on ALL three models** — sonnet-5 has its own HTTP-200 refusal surface (W-013) ·
ZDR / no-30-day-retention workloads ⇒ **fable excluded** (W-013) · every fable route and every
ingested fable benchmark states its **fallback configuration** (W-014) · fixed-step
transformations prefer scripts over agents (W-021; CONTRACT §2).

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
| **budget-conscious** | R6 → sonnet **medium** (runs the open probe; record outcomes) · R7 → opus **high**, xhigh per-spawn with stated reason · R5 → **sonnet high** (runs the demotion probe) — **session-scoped toggle: BYPASS the implementer-light pin with a generic sonnet spawn (state it); do NOT edit pin frontmatter mid-session (registers only at restart — review lens 2 F4)** · fable → R1 only; other enumerated classes need operator request · paired probes: keep only naturally-duplicable free ones |
| **quality-max** | define when first needed |
