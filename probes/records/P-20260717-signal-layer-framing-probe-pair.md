# PROBE — 2026-07-17 signal-layer framing checkpoint pair (fable×opus, advisor class) — PRE-REGISTERED

- probe_id: P-20260717-signal-layer-framing-probe-pair
- **status: PENDING — this section written BEFORE either leg returned (pre-registration;
  outputs and adjudication appended below when they exist)**
- task class / ROUTES row: **framing / advisor checkpoint** (R15 advisor lane; R8-adjacent) —
  the class P-20260712 registered as UNPROBED-in-paired-form. First paired firing.
- question: does the fable premium show up when the review contract is OPEN (framing
  questions, no lens pre-specification), where tight contracts plausibly compressed the
  differential in P-20260712?
- configs compared: roster `advisor` agent (effort **xhigh** pinned in frontmatter,
  `tools: []` — snapshot-only, no tool trajectories to diverge) — leg 1 default model
  (**fable**) vs leg 2 Agent-tool `model: opus` override (the R15 fallback config named in
  the agent def itself). Same agentType, same system prompt, same effort both legs.
- harness/contract: byte-identical prompt, artifacts EMBEDDED verbatim (both legs see the
  identical snapshot by construction). Canonical prompt file + hash:
  scratchpad `framing-probe-prompt.txt`, sha256
  `8fddeded0580245569845862c70fdac293be8b993192a8343272cf7e98f95926`, 35,847 bytes.
  Leg-prompt byte-identity to be ATTESTED post-spawn by extracting both tool-call params
  from the parent transcript and hashing (result recorded below when done).
- prompt shape: minimal and unconstrained — four framing questions ("what should we be
  asking that we haven't / strongest unraised objection / wrong approach anywhere / further
  grey areas") + ONE closing recommendation per the advisor contract; NO lenses, NO attack
  checklist. No model/tier named in the prompt; probe not disclosed to legs.
- artifacts under review: signal-layer memo
  `proposals/2026-07-12-F-portability-attribution-design.md` + Proposal F rev.2
  `proposals/2026-07-05-F-portability-lane.md`, **frozen at commit `3a76e51`**, working
  tree clean for both files at assembly time (checked: `git status --porcelain <files>`
  empty, `git rev-parse HEAD` recorded — attested this time, unlike P-20260712).
- blinded?: legs mutually blind (parallel, independent, no cross-visibility).
  **Adjudicator-blinded:** outputs presented to the operator as Leg A / Leg B; label→tier
  mapping sealed in the line below (operator: adjudicate before reading it).
  - SEALED MAPPING (coin-flipped via $RANDOM): Leg A = fable · Leg B = opus
- adjudicator: **OPERATOR** (pre-committed) — fixes P-20260712's author-adjudicator
  deviation. The main loop (author of both artifacts AND this prompt) collects outputs
  verbatim, computes mechanical stats only (tokens, word counts), and renders NO quality
  judgment before the operator's.
- router: operator ordered the probe verbatim ("run the framing probe", 2026-07-17),
  accepting the standing offer from the P-20260712 postscript. Fable spawn count: one —
  operator-ordered, inside the fable-usage-requires-ask discipline.
- clean-protocol checklist (target: first CLEAN framing-class firing): frozen tree ✓
  attested · non-author adjudicator ✓ (operator) · identical lens load ✓ (zero lenses both
  legs, identical prompt) · blinded adjudication ✓ (coin-flipped labels, sealed mapping).
  Residual deviation, named: prompt authored by the artifact author (framing-question
  selection could steer; mitigated by using the operator's own question set verbatim from
  the 2026-07-12 session).
- pre-registered analysis plan: operator judges per-leg (a) which leg surfaced the most
  decision-changing framing item, (b) any item unique to one leg that changes the
  ratification decision, (c) overall preference or no-preference. Tally rule: feeds the
  framing-class row (NEW — not the W-001 review-gate counter); W-019 discipline applies
  unchanged (no route change below ≥2 clean concordant firings in THIS class).

---

## Outcome (appended post-run)

- leg outputs: saved VERBATIM at signal-layer
  `proposals/reviews/2026-07-17-framing-probe-leg-A.md` and `…-leg-B.md`
  (blinded labels; this record holds the sealed mapping above).
- leg-prompt byte-identity attestation: **ATTESTED** — both Agent tool-call `prompt`
  params extracted from the parent transcript post-spawn and hashed: identical, sha256
  `55890c695919befbbd9bab77e73876dda402beffe6f2f4ca8115025ab4a77903`, 35,846 bytes each
  (canonical prompt file differs only by its trailing newline: 35,847 bytes). Measured
  2026-07-17, extraction script inline in parent transcript.
- tokens/cost (Reported, harness usage counters): Leg A 26,368 subagent tokens / 333s ·
  Leg B 26,378 / 281s — volumes near-identical again (delta 10 tokens); 0 tool uses
  both legs (snapshot-only by design). Whole probe ≈53k subagent tokens, inside the
  60–80k estimate.
- **DEVIATION (2026-07-17, named):** adjudication is **COUNSEL-ASSISTED**, not clean.
  Sequence: operator asked "help me adjudicate" → main loop offered a structural aid +
  the three questions → operator asked for per-item recommendations ("guide me through
  this") → main loop offered a cold-read Q3 first to salvage one uncontaminated datum →
  operator declined ("i dont really understand what you are asking of me here even") →
  main loop rendered full per-item counsel on the design substance, and several items
  from BOTH legs were adopted into Proposal F rev.3 + the DF-2 extraction before the
  three rulings were given. **Blinding of the tier mapping is still intact** (counsel
  was rendered on substance; the sealed line above stays sealed until the operator
  rules), but the no-judgment-before-operator clause is breached. Tally consequence:
  this firing does NOT count toward the framing-class clean-firing counter (W-019);
  it still yields item-level data (verdict divergence, unique-catch yield per leg —
  both legs contributed adopted uniques: Leg A #7/#8/#9 and Leg B §2b/§3.1/§3.2 all
  land in rev.3).
- **operator adjudication (2026-07-17, counsel-assisted, CLOSED):**
  - Q1 (most decision-changing item): no independent operator ruling; the author's
    severity-weighted analysis named Leg A #7 (DF-2 precedence inversion — verified
    against `signal.py:182`) the highest-severity unique catch, and the demand test
    (convergent; B led, A raised independently) the biggest frame-shift.
  - Q2 (uniques changing the ratification): YES on both sides — Leg B's §3.1/§3.2/§2b
    restructured what rev.3 ratifies (DF-1 demotion, DF-2 extraction, R8); Leg A's #7
    corrected the extracted fix itself, #8/#9 hardened the gate.
  - Q3 (preference): **operator ruling: prefer Leg A — by explicit adoption of the
    author's disclosed recommendation** ("I'll go with your recommendation and prefer
    Leg A"), after stating they lacked domain familiarity to rule independently.
    Author's reasoning (on record in the session): sole-reviewer counterfactual +
    severity weighting — only-B world ships the precedence inversion (permanent
    mis-attribution on an append-only ledger); only-A world keeps reversible governance
    imperfections. Author biases disclosed BEFORE the ruling: unblinded (held the
    sealed mapping) + same-lineage-as-Leg-A.
- **UNSEALED:** Leg A = **fable** (`claude-fable-5`), Leg B = **opus**
  (`claude-opus-4-8`) — measured from the subagent transcripts
  (`subagents/agent-a2edcab22db58ec63.jsonl` / `…a3fe845cc1de63cf5.jsonl`), stamped
  into both leg files.
- **Symmetry caveat (found at stamping):** the fable leg's final message opened with
  "The advisor endorsed the analysis and the ranking" — yet its transcript records
  ZERO tool_use blocks. Server-side-and-invisible vs unsubstantiated: **Unchecked**,
  not resolvable from the artifact. If real, the legs were not config-symmetric (the
  opus lane has no advisor loop) and the fable leg's output benefited from an extra
  review pass. Weakens any tier attribution of the preference beyond the deviations
  already named.
- **tally (framing-class row — NEW row, firing 1): NOT CLEAN** (counsel-assisted
  adjudication; author-preference adopted; symmetry caveat above). Clean-firing count
  stays **0** — no route change (W-019: ≥2 clean concordant firings required).
  Direction-only yield: fable leg preferred on severity-weighted unique-catch yield;
  **verdicts DIVERGED** (ratify-with-changes vs HOLD — first verdict-divergent pair in
  the corpus); unique catches near-disjoint and BOTH sets adopted into the artifact →
  **complementarity, not superiority, is the robust finding.** Token volumes
  near-identical (delta 10).
- **process lessons (feed ROUTES/WARRANTS next pass):**
  1. Operator-adjudicated probes need domain scaffolding: pre-agree a scoring rubric,
     or accept author-adjudication-with-disclosure at pre-registration time — don't
     discover mid-probe that the adjudicator can't rule (this probe's actual failure
     mode).
  2. Tight-lens panels and open-contract framing reviews catch near-disjoint defect
     sets: the six-review rev.1 panel (tight lenses) missed the precedence inversion an
     open-contract leg caught; ratification gates should pair both contract types.
  3. Findings alleging text-vs-code conflict get primary-source verification before
     disposition (done here; it's what made Leg A #7 load-bearing).
  4. Snapshot-only legs should have their raw final messages hashed at relay time, and
     preamble/deliverable boundaries pre-declared — the "advisor endorsed" preamble
     discovery shows verbatim-relay claims need mechanical backing.
