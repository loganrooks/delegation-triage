# Opus 5 — routing-policy update proposal

**Status:** draft for operator ratification; **no implementation or activation authorized**. No route,
warrant, or roster pin was edited in producing this.
**Date:** 2026-07-24 · **Author:** Claude (Opus 5, Cowork session) · **Evidence:**
[`docs/research/2026-07-24-opus-5-evidence.md`](../research/2026-07-24-opus-5-evidence.md)
**Trigger:** operator request — "update the roster to reflect the release of Opus 5."

---

## 0. Summary of what actually needs to change

Opus 5 launched **today**, 2026-07-24. The headline is not a capability re-ranking — `ROUTES.md`
already orders fable above opus, and that ordering survives the evidence. The two things that
genuinely need action are (a) a **stale installed artifact**, and (b) a **breaking API change** that
can hard-fail existing xhigh routes.

| # | Finding | Class | Action needed |
|---|---|---|---|
| F1 | Installed plugin is an older build than the repo | Propagation defect | Rebuild + reinstall |
| F2 | `thinking: disabled` + `xhigh`/`max` → HTTP 400 | Breaking change | Audit adapters before use |
| F3 | Vendor says do not reuse prior-model effort settings | Warrant expiry | Re-grade effort warrants as `Unchecked` |
| F4 | Fable/Opus cost-reliability gap widened | Prior shift | Probe, do not re-route yet |
| F5 | Sonnet-vs-Opus difficulty split has fresh independent support | Prior confirmation | No change; cite it |

---

## F1 — The installed skill is stale (highest-priority, non-obvious)

The `delegation-triage` skill currently **loaded in Cowork** is served from
`dist/delegation-roster-0.3.0.plugin`, not from this working tree. Its `SKILL.md` still carries:

- a flat **"Model priors"** table (`Strategy… → Fable/high` · `Deep adjudication, coding… → Opus/high`
  · `Broad search… → Sonnet/high`), which this repo has **superseded** with the 15-row evidence-graded
  `ROUTES.md`; and
- on-demand references to `references/models/opus-4-8.md`, `fable-5.md`, `sonnet-5.md` — a
  `references/` directory that **does not exist in this working tree at all**.

Consequence: routing guidance actually being applied in live sessions is the 0.3.0 snapshot, missing
R1's cross-vendor candidate, R7's 2026-07-17 sonnet-first re-pointing, R9's avoid-ruling, and R14/R15
entirely. **Editing `ROUTES.md` will not change what any session loads until the plugin is rebuilt
and reinstalled.** This is the same class of defect as the config-drift incident on dionysus the same
day: the authored source was correct and the deployed artifact was not.

`Resolved` — `dist/delegation-roster-0.3.0.plugin` is the only file in the tree containing the string
`opus-4-8`, and the loaded skill's text matches it rather than `SKILL.md`.

**Proposed:** treat rebuild-and-reinstall as a precondition for any other change here. A routing
update that lands only in the repo is a no-op against live behaviour.

**Amendment (2026-07-24, fable leg — per the campaign handoff's known-defects list):**
(a) *Blast-radius bound:* F1 corrupts guidance only for sessions that consult the installed
skill by default. Explicitly-routed lanes, sessions reading `ROUTES.md` as plain files, and
non-roster harnesses (dionysus GSD) are unaffected — so this is the highest-priority item
*within* this proposal, not a global precondition for other campaign work. (b) *The
"missing R14/R15 entirely" detail is `Unchecked`:* a byte-grep of the packed 0.3.0 plugin found
7 `R14|R15` matches, unresolvable without unpacking — the sub-claim may overstate. Neither
correction changes the rebuild recommendation. (c) *F2 audit executed 2026-07-24:* zero files
under `adapters/`, `agents/`, or `templates/` mention thinking at all → **clean bill**, the
proposed probe P-20260724-A is satisfied with no offenders. (d) *Rebuild procedure exists:*
`python3 install.py cowork` (README:29) — B2 is unblocked and mechanical.

---

## F2 — Breaking change: `thinking: disabled` is incompatible with `xhigh`/`max`

Vendor docs (S2/S3) state that on Opus 5, `thinking: {"type": "disabled"}` is accepted **only** at
effort `high` or below; combining it with `xhigh` or `max` returns **HTTP 400**. This is a behaviour
change from Opus 4.8, where thinking was off unless explicitly enabled — on Opus 5 thinking is
**on by default (adaptive)**.

This intersects directly with live routes. **R4** (coding/agentic implementation) and **R10**
(structured epistemics compilation) both route to **opus xhigh**. Any call path that pins xhigh while
also disabling thinking — carried over from an Opus 4.8-era template where disabling was the default
posture — will now fail closed rather than degrade.

Exposure in this repo is **plausible but unconfirmed**: `adapters/codex/delegate-to-claude/` passes
`--effort xhigh` in at least 11 test sites. Whether any production path also sets a thinking-disabled
flag was **not established** in this pass — the adapter directories are untracked and were not
audited line by line.

`Reported` (vendor documentation, not independently exercised). **Flip condition:** a live xhigh call
with thinking disabled that returns 200 would refute this.

**Proposed probe P-20260724-A:** grep every adapter and roster pin for a thinking-disable flag
co-occurring with `xhigh`/`max`; if found, fix before the next xhigh spawn. Cheap, mechanical,
`implementer-light` class.

---

## F3 — Effort warrants inherited from Opus 4.8 expire, they do not carry over

Anthropic's own guidance (S3, quoted verbatim in the evidence file): *"`low` and `medium` effort are
stronger on Claude Opus 5 than on earlier Opus models… run a fresh effort sweep on your evals rather
than reusing [prior model] settings."*

Under this package's epistemics, that is decisive about **status**, not about direction. Every
effort-shaped warrant grounded in Opus 4.8 measurements — **W-004** (coding xhigh), **W-005**
(mechanical edits opus high), **W-010** (epistemics compilation xhigh), and especially **W-016/W-017**
(the dial's measured shape; "high = sweet spot") — was corroborated against a model whose effort
ladder the vendor now says behaves differently. Those warrants should read **`Unchecked` for
opus-5**, exactly as an expired `STATE.md` entry does. They are not falsified; they are unrenewed.

The practical bite is on **W-016**. "High is the sweet spot" is the single most load-bearing effort
claim in the table, and the vendor's statement is specifically that the *lower* rungs improved — which
is the direction that would move the sweet spot, if it moved.

Note the one place vendor guidance now *agrees* with an existing route: *"Start with `xhigh` for
coding and agentic work."* That is `Concordant` support for **R4**, and worth recording as such — but
vendor concordance is not corroboration and should not upgrade W-004's grade.

**Proposed probe P-20260724-B:** a paired high-vs-xhigh run on one R4-class task and one R7-class
task under opus-5, scored on the existing rubric. This is the minimum to renew W-016 rather than
silently assume it.

---

## F4 — The fable/opus gap moved, but this is a probe, not a re-route

`ROUTES.md` routes R1, R2, R3, R13, R15 to **fable high/xhigh** with opus as fallback. That ordering
is *not* contradicted by the evidence and should stand for now. What changed is the cost and
reliability of exercising it:

- Opus 5 holds pricing at **$5/$25 per MTok**, unchanged from Opus 4.8 — while Fable 5 sits at
  roughly **2x** that (S4, S5). `Reported`.
- Fable 5 is a **Covered Model** with mandatory 30-day data retention; Opus 5 is not (S5, S1, S2).
  This is a hard operational difference for any lane touching sensitive material, and it is a
  *categorical* distinction rather than a benchmark delta. `Concordant`.
- Independent aggregators put Opus 5 at or slightly above Fable 5 on two specific measures — Vals AI
  SWE-bench Verified **97.00% vs 95.00%**, and Artificial Analysis Intelligence Index **61 vs 60** at
  max effort (S6, S7). `Reported`, single-source per figure, **not** `Corroborated`.
- Fable 5 availability has been disrupted since its 2026-06-09 launch, including a reported global
  pull of ~19 days (2026-06-12 → 07-01) (S12, journalism). `Reported` — **single-source, uncorroborated,
  and load-bearing if used**. Do not act on this without a second source.

Two countervailing facts that argue against demoting fable on this evidence: Artificial Analysis also
flags Opus 5 as **slow (50.7 tok/s)** and reports a **rising hallucination rate** (+14 points, to 50%
on AA-Omniscience) (S7). For **R1 review gates** and **R10 epistemics compilation** — the two classes
where a confident wrong answer is most expensive — a higher hallucination rate is precisely
disqualifying. The cheap-and-competitive story and the hallucination story point opposite ways.

`Contested`. **Proposed:** no route change. Log as an open fork; if fable scarcity forces the
fallback rows anyway, capture that as a natural experiment rather than a decision.

---

## F5 — The sonnet/opus split holds, with better evidence than before

Independent difficulty-tiered SWE-bench data (S6) has Sonnet 5 at 84/77/76/67% across task-length
tiers against Opus 5's 98/97/90/100%, with the gap widening on the hardest tasks. This is
consistent with the existing R6/R7 sonnet-first posture *and* with R7's escalation clause
("escalate opus high per stated judgment-discrimination reason"). It supports keeping a
difficulty-based split; it does **not** establish where the line sits, and should not be used to
move it. No change proposed.

**R9** (`Sonnet 5 at xhigh — AVOID pending probe`) is untouched by this release; it is a
cost-efficiency posture about Sonnet, and no Sonnet 5 change was found.

---

## 6. What was NOT done

- `ROUTES.md`, `WARRANTS.md`, `STATE.md`, and all roster pins are **unmodified**.
- No warrant was re-graded in place — F3 proposes re-grading; it does not apply it.
- The installed plugin was **not** rebuilt or reinstalled.
- The Opus 5 **system card** (referenced by S1) was not fetched; it likely carries safety and
  long-horizon agentic evaluation tables not represented here. This is the largest known gap.
- No `references/models/opus-5.md` note was authored, because the `references/` tree does not exist
  in this working copy — see F1. Authoring one would mean guessing at a layout that lives only inside
  the 0.3.0 package.

## 7. Decision requested

1. **F1 rebuild/reinstall** — accept / defer. Blocks the rest from having any live effect.
2. **F2 adapter audit** — accept / defer. Cheap; failure mode is a hard 400 on coding routes.
3. **F3 warrant re-grade to `Unchecked`** — accept / reject. This is the honest reading of the
   package's own expiry rule, but it does mark several load-bearing warrants as unrenewed at once.
4. **P-20260724-B effort sweep** — schedule / defer.
5. **F4** — confirm "no change, log the fork" is the right disposition.
