# WARRANTS — the evidence register (load on demand, never per-spawn)

Typed records, one per warrant. Labels and grades per [`EPISTEMICS.md`](EPISTEMICS.md) (house
vocabulary; a model-card or vendor number is Concordant/Reported, never Corroborated). Every
record: claim · label + grade + downgrades · resolvable locators with **quoted primary excerpts**
(never lane summaries — the PATCH-W6-01 lesson: a column conflation survived two summary layers
and was caught only by a blinded cross-vendor diff) · flip condition · probe tally
(attested vs self-reported; tallies maintained in [`probes/INDEX.md`](probes/INDEX.md)).
**Update discipline:** supersede in place, same pass as the post-mortem; a record without a flip
condition is a guess and must say so.

**Attestation (D5):** a probe verdict counts toward a flip tally only if *attested* — verifiable
from a durable artifact (raw legs on disk, transcript JSONL, commit); blinded/frozen-tree status
recorded per probe. Self-reported outcomes are recorded but tallied separately; **n=1 never flips
a row** [W-019].

## KNOWN-REPOS locator key (repo-qualified prefixes; identity = name + origin, hints are env-specific)

| prefix | repo (origin remote) | local hint (this machine) |
|---|---|---|
| `bridgewright:` | loganrooks/bridgewright-discovery | ~/Development/bridgewright |
| `prix-guesser:` | loganrooks/prix-guesser | ~/Development/prix-guesser |
| `signal-layer:` | (no remote — local-only, flagged) | ~/Projects/signal-layer |
| `AHR:` | (no remote — local-only, flagged) | ~/Projects/AgenticHarnessResearch/agentic-harness-research |
| `workflow-gate:` | loganrooks/workflow-gate | ~/Development/workflow-gate |
| `SEAS:` | loganrooks/SelfEvolvingAgentialSystems | ~/Projects/SelfEvolvingAgentialSystems |
| `claude-user-dir:` | (untracked user dir — deployment target, weakest provenance class) | ~/.claude |

---

### W-001 — Review gates: fable-high with ≥2 independent lenses; neither Anthropic tier dominates
- **Claim:** On adversarial review gates, fable-high and opus (high or xhigh) produce convergent
  verdicts with unique catches on BOTH sides; independence (a second voice, incl. cross-vendor or
  within-tier) buys more unique substance than raising tier or effort; fable-high holds the route
  in-window, with ≥2 independent lenses on high-stakes artifacts.
- **Label · grade:** Corroborated · Moderate.
- **Downgrades:** small n (6 pairings); two pairings carry author-adjudicator confounds; one
  unfrozen tree; severity-calibration differences confound the dominance reading; all local task
  classes are research/governance artifacts (code review thin).
- **Locators + excerpts:**
  - bridgewright:registers/reviews/2026-07-03-signal-layer-v3-adoption-gate.md (clean: hash-pinned
    contract, blinded, frozen tree): *"Neither leg dominated; the demotion flip condition ('opus
    catching equal blockers') is approximately met on substance but confounded by
    severity-calibration differences and n=1."* and *"The single sharpest catch of the gate (E1's
    written-vs-intended inversion, warranted by measuring the live shards) came from fable at
    HIGH — lower effort than opus's xhigh."*
  - AHR:research/routing/k1-firing-2026-07-03.md (deviated: unfrozen tree, author-adjudicator):
    *"Two independent same-day firings, same reading: neither tier dominates; independence buys
    more than tier."*
  - bridgewright:registers/reviews/2026-07-03-warrant-verifier-proposal-paired-review.md (blinded,
    frozen, xhigh-vs-xhigh): *"Both reviewers, independently: REVISE-THEN-ADOPT"*; fable-only
    *"L3-1 (MAJOR): the Kind enum is not a partition"*; opus-only *"L3-a (MAJOR): the parsimony
    CUT — defer the Dung acceptability solver."*
  - bridgewright:registers/reviews/2026-07-02-exploratory-phase-program-review.md (frozen `main @
    2c8862c`, blind; lens-load confound 6-vs-3): finding 8, *"ONBOARDING still taught the
    forbidden narrowing … **C-unique** (L6.1) — B's coherence probe covered other files and missed
    it."*
  - prix-guesser:.handoffs/2026-07-03-external-grounding-postmortem-FINDINGS.md §7 (identical
    contract at HIGH, blinded; author-adjudicator + author-model deviations disclosed): *"verdicts
    convergent, neither leg dominated, and the author-model reviewer showed no leniency toward the
    author — its sharpest catch was against the author's own grading key."*
  - signal-layer:proposals/reviews/2026-07-05-regate-A-leg{1,2}.md (within-tier G=2, blinded
    fable-high pair): leg 1 *"VERDICT: REVISE (narrow)… the discharge record is nearly clean
    (14/15 DISCHARGED, 1 PARTIAL)"* — legs convergent on all blocker-class defects, unique catches
    both sides → independence demonstrated WITHIN one tier.
- **Flip condition:** demote fable-high → opus when a **clean** pairing (frozen tree, non-author
  adjudicator, identical lens load) shows opus catching equal blockers AND severity calibration
  not confounding — per W-019: never on n=1; ≥2 attested concordant clean firings, ~3/side if
  variance stays high. Counter to date: approximately-met-but-confounded ×2 (07-03 gate; K1
  deviated) → NO demotion. Direction fable-vs-opus on this class: **Contested** pending the
  operator triage initiative (2026-07-03).
- **Probe tally:** attested-clean 3 · attested-deviated 4 · self-reported 0 — scope: ALL probes
  feeding this warrant, incl. the within-tier regate pair; the demote counter in probes/INDEX.md
  scopes to cross-tier firings only (2 clean / 3 deviated) — reconciled 2026-07-10, review F1.
  New 2026-07-17 (deviated: blinding breach + author-adjudicator): first cross-VENDOR datum on a
  CODE-review artifact — `sol-code-reviewer` (gpt-5.6-sol high) known-answer test vs the B20
  fable+codex ground truth (probes/records/P-20260717-sol-code-reviewer-b20-known-answer.md):
  blind-clean catch of the hardest item (fable's cross-lane MAJOR, WITH an executable repro no
  other lane produced) + the doc-drift minor; 0 false positives; ~1/6 fable minors (amended —
  sol's MAJOR-4 = fable's MINOR-4 elevated; the remaining minors gap is PROMPT-CONFOUNDED:
  fable's prompt cued ≥3 of its minors via leading questions and sol's prompt suppressed
  polish-tier findings by rule — operator-caught, record §deviations item 5); the other matches
  contaminated by a worktree-refs blinding breach. Thins the "code review thin" downgrade
  by one datum; supports the independence>tier direction on the MAJORs axis only; NOT yet
  routing-changing (n=1, deviated). Protocol lessons: known-answer trees must be `git archive`
  exports, never worktrees (shared refs expose the answer via `git log --all`); paired review
  legs must run IDENTICAL prompt text or the minors axis is uninterpretable.
  Second 2026-07-17 datum (deviated: author-adjudicator ONLY — blinding, prompt-parity, and
  frozen-tree all clean): fable×sol paired review of B16 under a byte-identical charter
  (probes/records/P-20260717-sol-fable-b16-paired-review.md): substance convergent on the top
  MAJOR (both with own httpx probes), verdicts split on severity calibration only
  (DO-NOT-SHIP vs SHIP-WITH-FIXES); **sol-unique second MAJOR fable missed** (version-suffix
  parser mangling old-style arXiv ids), fable-unique subtler test/namespace defects; the B20
  minors gap CONFIRMED prompt-caused (sol produced 5 polish-tier findings once in scope).
  sol-code-reviewer n=2, zero false positives across both. Independence>tier further
  corroborated cross-vendor at same tier/effort.

### W-002 — Architecture / design / contract & rubric authoring: fable high
- **Claim:** Durable-artifact authoring (contracts, rubrics, designs) is where fable's judgment
  premium is best spent; output outlives fable access and cheaper executors run it later.
- **Label · grade:** Conjecture · Low (policy-backed). Basis is operator policy
  (claude-user-dir:decisions/0004 enumerated classes; 0008 durable-artifact doctrine) + vendor
  capability positioning — no local paired measurement of authoring quality exists.
- **Locators + excerpts:** claude-user-dir:decisions/0004…0008 (policy records, quoted at deploy
  time); registered open question in the consuming programme's delegation doctrine: *"can fable
  AUTHOR the contract/harness … and have non-fable executors deliver fable-grade results?"* —
  every contract-driven run is data.
- **Flip condition:** a fable-authored contract + opus executor underperforms an opus-authored
  baseline on the same task class (paired, attested).
- **Probe tally:** attested 0 · self-reported 0 (accumulating via the open question).

### W-003 — Front-end design: fable high
- **Claim:** Fable-high is the best route for front-end design artifacts.
- **Label · grade:** Conjecture · Low — enumeration (0004) + delegation-doctrine prior, **not a
  local measurement**; the route says so rather than borrowing confidence [PATCH-W2-01].
- **Locators:** claude-user-dir:decisions/0004.
- **Flip condition:** a paired eval (fable-high vs opus-xhigh) on a real front-end artifact,
  judged on rendered output + design quality, shows opus matching fable → demote.
- **Probe tally:** attested 0 · self-reported 0.

### W-004 — Coding / agentic implementation: opus xhigh
- **Claim:** Coding/agentic implementation defaults to the capability-bound tier at xhigh;
  mis-routing cost is high there.
- **Label · grade:** Reported · Moderate — vendor literal guidance (*"Start with xhigh for coding
  and agentic use cases"* — vendor docs, quoted at table seed 2026-07-02), adopted as default; no
  local corroboration yet (the flip is the first local check) [PATCH-W2-05]. Independent
  direction-only support: W-020.
- **Locators:** vendor effort documentation (seed record:
  workflow-gate:.planning/research/2026-07-02-model-effort-triage/lane-vendor.md); W-020.
- **Lead (added 2026-07-10, routing-gaps survey, review F10):** the reported Opus 4.8 xhigh→max dip
  on FrontierCode-Diamond (W-016 hypothesis note; [C-009]) is the *shape* of this flip condition —
  but on a code-QUALITY benchmark, at secondary/noise-unbounded grade, so it is a lead to watch, NOT
  a flip (the flip requires the result reproduced in OUR ledger). Corroborates-in-direction the
  `max`-reserved posture (W-008/W-009).
- **Flip condition:** a HAL-style non-monotonic effort result reproduced in OUR ledger on
  implementation tasks → tier the default down.
- **Probe tally:** attested 0 · self-reported 0.

### W-005 — Mechanical, fully-specified edits: opus high; sonnet demotion probe OPEN
- **Claim:** implementer-light work survives review at sonnet-high under a fully-specified
  contract; the opus-high pin is provisionally held pending the demotion count.
- **Label · grade:** Corroborated · Low (n=1; imprecision).
- **Locators + excerpts:** claude-user-dir git commit `44b91df` (probe run 1, 2026-07-03,
  operator-directed): sonnet-high executed the ADR-0010 enrollment cascade (10-file commit incl.
  verbatim 63-line ADR body, gitignore surgery, 2 table edits) — **survived review with 0
  deviations** (fable-authored fully-specified contract; reviewer diffed 4 artifacts vs spec
  bytes; 48.7k subagent tokens / 17 tool calls / 84 s). Attested: commit + review diff.
- **Flip condition:** 3 sonnet implementer-light runs survive review → demote the pin.
  **Count: 1/3.**
- **Probe tally:** attested-clean 1 · self-reported 0.

### W-006 — Sweeps / retrieval: sonnet, diverse lanes over higher tier; medium probe live
- **Claim:** On sweep/retrieval lanes under a strong harness contract, sonnet misses no
  load-bearing sources vs opus at ~⅓ the overlap cost; coverage is bought by adding diverse
  lanes, not raising tier; an opus sweep needs a stated judgment-discrimination reason. Sonnet
  MEDIUM is a live candidate (effort dial moved token cost ≈0 on this observation-dominated
  class).
- **Label · grade:** Corroborated · Moderate.
- **Downgrades:** n=2 paired probes + 1 medium probe; single project-family task classes;
  vendor-card support is Reported (self-party).
- **Locators + excerpts:**
  - bridgewright:experiments/demand-intake/results/lane-audit-2026-07-03.md (paired sonnet-high vs
    opus-high, identical lane contract, file-level source diff; raw-byte audit): *"Tier 1 —
    main-loop spot-checks: 16 items, 15 faithful, 1 attribution error"*; sonnet lane uniquely held
    the headline-grade exhibit (Cline #8910 — *"✓ VERBATIM exact"*), no sonnet load-bearing miss.
  - SEAS:proposals/2026-07-05-adversarial-survey-memo.md §Wave-3 (sonnet-medium vs sonnet-high,
    blinded, identical contract + window): *"scanned 180 vs 185; leads 12 vs 12; overlap 3/12;
    tokens 191.5k vs 192.6k (≈1.006×) … neither lane dominated"* — medium uniquely surfaced
    2606.23583, refuting the high lane's own negative claim.
  - Sonnet-5 system card §8.9 (vendor-primary, delegated read 2026-07-03, pages not spot-checked):
    HLE-with-tools sonnet-5 57.4 vs opus-4.8 57.9; multi-agent 86.6 > single 84.7 — Reported.
  - claude-user-dir:decisions/0007 D1 (the seeding paired probe, 2026-07-02: 3/26 URL overlap;
    sonnet surfaced the run's most load-bearing sources).
- **Flip condition:** ≥2 of the next 5 paired probes show sonnet missing load-bearing sources →
  re-tier. **Count: 0/2.** Track medium separately: ≥2 medium probes with a load-bearing miss vs
  the high leg → medium reverts to budget-conscious-only. **Count: 0/1.**
- **Interactions:** corroborated-in-direction by W-022's vendor guidance (`low` effort typical
  "like subagents"; haiku listed for "sub-agent tasks") — vendor points even further down the
  dial than the medium probe has tested.
- **Probe tally:** attested-clean 3 · self-reported 0.

### W-007 — Deep-read / adversarial verify / synthesis: opus
- **Claim (scoped per review lens 1 F5):** opus's judgment-stage output survived a severe check
  in the seeding session (caught a summarizer-fabricated negative; all gradings survived
  adversarial verification) — that is what is Corroborated. The comparative routing claim (opus
  over a cheaper tier on this class) is **untested locally**; the flip condition is the test.
- **Label · grade:** Corroborated · Low for the scoped claim (single session; no paired demotion
  probe yet).
- **Locators:** claude-user-dir:decisions/0007 D2 (2026-07-02, run wf_482d074d-787).
- **Flip condition:** a paired probe (cheaper tier vs opus, identical harness) on a
  judgment-heavy synthesis/verify task shows the cheaper tier reproducing opus's load-bearing
  findings → open a demotion probe [PATCH-W2-02].
- **Probe tally:** attested 1 (seeding session) · self-reported 0.

### W-008 — Hardest frontier forks: fable xhigh; `max` reserved
- **Claim:** On the hardest forks, fable **high→xhigh** buys a real gain (FrontierCode-Diamond
  24.0→29.3, ~+5.3pp — xhigh is the sweet spot); **xhigh→max** adds only ~+1.6pp (29.3→30.9) for ≫
  cost and community-reported instability, so `max` is reserved. *(Tier labels **RENDERED from the
  primary figure 2026-07-10** — FPD-1 DISCHARGED; the earlier "small gain high→xhigh" framing was a
  label error — the ~1.6pp step is xhigh→max, and high→xhigh is the larger ~+5.3pp step. Route
  direction unchanged and now better-grounded — C-007/C-008.)*
- **Label · grade:** Reported · Moderate (upgraded from Low on the 2026-07-10 primary render).
  Vendor FrontierCode Diamond per-tier curve rendered from fig 8.4.A: Fable 11.5/17.8/24.0/29.3/30.9,
  Opus 8.2/5.9/8.7/13.4/11.4 (low→max); STRONG community on `max` instability. Downgrades: still
  vendor/Anthropic-scaffold data (Reported, never Corroborated per house vocab); harness choice moves
  agentic scores >20 pts at fixed model, so the ~+5.3-pt high→xhigh gain (or ~+1.6-pt xhigh→max)
  transfers only insofar as our fork harness resembles the eval scaffold [PATCH-W2-03]; Tier-A
  *independent* effort-resolved fable data still absent — the render is the vendor figure itself, not
  an independent source (PATCH-W1-12); the figure discloses NO error bars (per-tier deltas carry no
  stated uncertainty).
- **Locators + excerpts:** system-card **figure 8.4.A** (FrontierCode Diamond) — **RENDERED
  2026-07-10** via Chrome from the Anthropic first-party CDN PDF (p.256/317; opus visual read,
  high-confidence): SEAS:reports/2026-07-10-routing-gaps-survey/lanes/L5-fig-render.md. Caption
  (verbatim): *"[Figure 8.4.A] FrontierCode (Diamond) pass rate across reasoning effort levels with
  mean output tokens per task on a log scale…"*. **Outcome:** the cold render matched all 15 cells of
  the three prior secondary transcriptions AND passed both independent anchors (Opus best = xhigh
  13.4%, GPT-5.5 best = med 6.3%, per cognition.ai/blog/frontier-code) — so the chart-series-conflation
  risk (review lens 1 F4) and the transcription-independence worry (review F3) are both **DISCHARGED**,
  and the FPD-1 tier-label correction is primary-backed [C-007, C-008]. Two figure facts of record:
  the x-axis is **cost** (avg $/task, log scale), not an effort-tier axis (a cost-vs-score Pareto plot
  with per-point tier labels); and the figure shows **no error bars** (feeds W-016/C-009 — the Opus
  non-monotonicity direction is confirmed from the primary, but no variance is disclosed to clear the
  noise bound). Original seed locators:
  workflow-gate:.planning/research/2026-07-02-model-effort-triage/lane-community.md: *"Below max,
  the dial barely moves. Thinking is adaptive. The model ignores budget it doesn't need."* (Huryn,
  1,000+ timed runs — lane-vouched direct fetch). Max-instability point: lane-synthesized from the
  Huryn primary (productcompass.pm), NOT a verbatim primary quote — relabelled per review lens 1
  F3; primary re-read owed if this fragment ever becomes load-bearing.
- **Flip condition:** independent effort-resolved fable fork data showing xhigh's marginal gain
  (a) real off vendor scaffold and (b) worth its instability → confirm; high ≈ xhigh
  off-scaffold → demote to fable high.
- **Probe tally:** attested 0 · self-reported 0.

### W-009 — Sonnet 5 at xhigh: avoid pending probe (cost-efficiency posture)
- **Claim:** Sonnet-5 xhigh's $/task rises steeply for diminishing return per dollar on agentic
  work — an AVOID as cost posture, NOT a capability inversion (the re-read showed vendor curves
  monotone through max; the claimed "max inversions" sit within ~1 binomial SE on 150 tasks).
- **Label · grade:** Provisional · Low — synthesis across third-party (AA efficiency inversion,
  direction confirmed / magnitude derived [PATCH-W2-06]; CodeRabbit dial ≈2× cost ~0 score;
  Epoch xhigh<max n=1) and vendor-primary (monotone curves, figures spot-checked 2026-07-03), all
  harness-conditioned; cost axes recomputed at list rates, not measured spend.
- **Locators:** Sonnet-5 system card Figs 8.4.A/8.5.A (spot-checked 2026-07-03); AA GDPval
  article 2026-06-30; Epoch (RC-04); CodeRabbit post. Noise-bound rule applies to any successor
  claim (probes/KNOWN-WEAKNESSES.md, point-estimate-naivety).
- **Flip condition:** our paired probe shows sonnet-xhigh yield worth the turns.
- **Probe tally:** attested 0 (on-harness probe never run — that probe IS the flip) ·
  self-reported 0.

### W-010 — Structured epistemics compilation: opus/cross-vendor xhigh; sonnet kind-typing only
- **Claim:** Claim→typed-record compilation needs the top tier for composed dispositions; sonnet
  matches xhigh-level kind-typing agreement but under-reproduces composed dispositions.
- **Label · grade:** Corroborated · Moderate (one attested 3-leg blinded probe, frozen fixtures,
  pre-registered bars; n=1 series).
- **Locators + excerpts:** bridgewright:experiments/warrant-compilation/results/PROBE-RESULT.md
  (C-068): *"Primary κ(O,X) on primary_kind = 0.471, raw 53% → falls in the REVISE band"*;
  *"Disposition reproduction: O 9/14 (64%), X 9/14 (64%)"*; *"κ(O,S)=0.516 … leg-S reproduction
  6/14 (43%)"* — sonnet kind-typing κ ≈ the xhigh-xhigh κ itself; composition over-conservative.
- **Flip condition:** definitions-fixed re-run shows sonnet composition ≥ xhigh-parity → open the
  demotion; a 2nd weak sonnet composition run → close the kind-typing candidacy too.
- **Probe tally:** attested-clean 1 · self-reported 0.

### W-011 — fable-medium as implementer: PARKED
- **Claim:** fable-medium might implement at opus-xhigh quality for less; capability is
  vendor-prose-supported, the cost advantage is NOT supported (inference: breaks even only under
  ~40% of fable's tokens; one REPORTED long-agent task ran ~4× opus).
- **Label · grade:** Conjecture · Very-Low. Contested economics; nobody has measured the pairing.
- **Locators:** vendor FrontierCode prose; W-015's decomposition; USAMO effort-cost curve.
- **Flip condition:** a measured fable-medium vs opus-xhigh cost-per-task pairing in our ledger.
- **Probe tally:** attested 0 · self-reported 0.

### W-012 — Browser-automation legs: CANDIDATE sonnet-5 high, thinking ON (Class B, unadjudicated)
- **Claim:** Sonnet-5 is the most injection-resistant browser agent measured (attack success
  without safeguards 0.93%/1.01% thinking/none vs opus-4.8 31.5%/17.8%, sonnet-4.6 50.7%; 0% with
  deployed Browser-Use safeguards; computer use 2.25% vs 7.14%); thinking-ON is
  measured-protective; high-not-xhigh is doctrine (observation-dominated class + W-009).
- **Label · grade:** Reported · Moderate for the PI ordering (vendor-primary, tables spot-checked
  2026-07-03; the eval targets Claude-in-Chrome + Cowork); the ROUTE itself is **unadopted** —
  current practice (session model drives) stands until operator adjudication.
- **Locators:** Sonnet-5 system card §5.2.2.3–4.
- **Flip condition (for the candidate):** operator adjudication; or independent PI data reversing
  the ordering. High-vs-xhigh PI delta: Unchecked (card resolves no effort tiers for browser/GUI).
- **Probe tally:** attested 0 · self-reported 0.

### W-013 — Safety-refusal & compliance constraints (cross-class)
- **Claim:** (i) The real-time classifier layer is fable-ONLY; API default on trigger = hard block
  (`stop_reason: "refusal"`, unbilled); fallback is opt-in. (ii) Generic over-refusal ordering
  fable < opus < sonnet-5 (API benign over-refusal 0.01% / 0.35% / 0.59%) — vendor-only, no
  independent data. (iii) Sonnet-5 has its own HTTP-200 refusal surface — unattended runs handle
  refusal on ALL three models. (iv) ZDR / no-30-day-retention ⇒ fable excluded (Covered Model);
  sonnet-5 supports ZDR. Hence: dual-use-adjacent + unattended + API ⇒ not fable unless the
  harness handles refusal or opts into fallback; default opus. Wrong-refusal-costly benign volume
  prefers opus over sonnet-5.
- **Label · grade:** Reported · Moderate (vendor-primary; Table 4.1.2.A numbers re-confirmed in
  the Sonnet-5 card via delegated deep-read 2026-07-03; direction independently unverified;
  HTTP-200 wire-mechanics sub-claim rests on RC-08 alone).
- **Locators:** anthropic.com/news/redeploying-fable-5; Sonnet-5 system card Table 4.1.2.A +
  Claude Code cyber tests (malicious refusal 92.4% vs 76.6%; dual-use benign 97.3%→91.6%);
  vendor ZDR/Covered-Model page (RC-25).
- **Flip condition:** independent over-refusal measurements reversing the ordering; or vendor
  wire-mechanics documentation contradicting RC-08.
- **Probe tally:** attested 0 · self-reported 0 (constraint row, not a performance prior).

### W-014 — Fallback purity (ingestion + routing guard)
- **Claim:** Any fable route and any ingested fable benchmark must state its fallback
  configuration — headline fable scores can silently include Opus-served tasks (AA's include 2%),
  and post-redeploy third-party benchmarks have scored classifier interceptions as capability
  failures (BridgeBench: 9/12 debugging tasks intercepted, scored 0).
- **Label · grade:** Reported · Low–Moderate (RC-26 vendor/AA; RC-22 relay — primary 403'd
  [PATCH-W1-13]).
- **Locators:** AA fable methodology note (RC-26); RC-22 field record (relay). **Concrete dated
  exemplar (2026-07-10 routing-gaps survey):** BridgeBench "9/12 debugging tasks intercepted, scored
  0" (BridgeMind X post 2026-07-02, via TechTimes/Decrypt; X primary returned an empty body) —
  classifier fallbacks scored as capability zeros, fallback target (Opus 4.8) stated; relay-level,
  low-track-record source; the live board later showed Fable 5 at 86.2 not the claimed 25.9
  (unresolved) [C-012]. Do not cite its numbers as capability data — it is a guard exemplar, not a
  benchmark datum.
- **Flip condition:** none needed — this is a hygiene invariant; retire only if classifier +
  fallback mechanics are removed upstream.
- **Probe tally:** n/a (guard).

### W-015 — Cost facts: fable ≈2.5× opus per identical work; tokenizer ratio ≈1.0
- **Claim:** Fable's effective cost ≈2.5× opus measured per identical audit, decomposing as 2×
  sticker × ~1.25 verbosity/thinking × subagents-bill-separately — NOT tokenizer (Opus 4.7+
  shares the newer tokenizer; the ratio cancels).
- **Label · grade:** Reported · Moderate for the 2.5× (single tester, disclosed methodology, not
  independently replicated); Corroborated · Low for the tokenizer ratio (measured locally, n=1
  payload).
- **Locators + excerpts:**
  - workflow-gate:.planning/research/2026-07-02-model-effort-triage/lane-community.md (Huryn
    primary, fetched directly): *"Author ran 7 experiments, 1,000+ timed runs over 4 days …
    Cost: $2.93 vs $1.17 median per audit (~2.5x)"*; one-shot wall-clock 1.48×, audits 1.29×
    median (0.92–1.70×).
  - AHR:research/routing/k1-firing-2026-07-03.md (measured token rider): *"fable-5: 14,769 ·
    opus-4-8: 14,781 → ratio ≈ 0.999."*
  - Hygiene: ccusage-ecosystem fable mispricing (silent under-costing) — don't trust third-party
    cost dashboards on fable rows without checking their price table.
- **Flip condition:** an independent measured audit series putting the multiplier materially off
  2.5× (either direction) → re-derive the decomposition. Prices themselves live in STATE.md,
  dated.
- **Probe tally:** attested 1 (K1 token rider) · external-reported 1 (Huryn).

### W-016 — Effort-dial shape: monotone in score, steep top-tier cost cliff; high = sweet spot
- **Claim:** On real agentic work the dial is monotone-in-score with a steep top-tier COST cliff;
  high ≈ the cost-quality sweet spot; top tiers for high-risk work only.
- **Label · grade:** Provisional · Low — cross-source synthesis (stet.sh GPT-5.5 26 real PRs:
  review-pass 38%→69% high→xhigh at 2.18× cost; OccuBench GPT-5.2 clean-monotone +27.5pp,
  single-run, LLM-simulated + LLM-graded; Sonnet-5-card curves monotone [figures spot-checked
  2026-07-03]; CursorBench live table monotone within family, vendor COI; Huryn: *"Default to
  `high`."*). Direction only, never magnitudes; all scaffold-conditioned.
- **Locators:** AHR:research/routing/w7-effort-evidence-sweep-2026-07-03.md (lane reports);
  cursor.com/cursorbench live table (endpoints cross-check 6/6 vs card Fig 8.5.A); W-020.
- **Interactions:** scoped by W-017 (non-monotonicity is task-class-conditional);
  corroborated-in-direction by W-022's vendor-measured advisor-effort datum (sonnet-medium
  executor + opus advisor ≈ sonnet-default intelligence at lower cost).
- **Hypothesis-to-probe (added 2026-07-10, routing-gaps survey, FPD-3):** two independent secondary
  transcriptions of system-card fig 8.4.A report Opus 4.8 directionally non-monotone on
  FrontierCode-Diamond (xhigh 13.4→max 11.4, −2.0pp; low 8.2→med 5.9) — but no SE is disclosed on a
  50-task × mean@5 set, so the delta is indistinguishable from noise (point-estimate-naivety) [C-009].
  The **monotone default is RETAINED**; this is logged as a hypothesis to probe, not a flip (the bar
  below is our own ledger + a noise bound, which secondary vendor-chart transcriptions do not meet).
  **Render update 2026-07-10:** the dip is now CONFIRMED from the primary figure itself (opus Chrome
  render, both ends: 8.2→5.9 and 13.4→11.4) — no longer secondary-only — **but the figure discloses
  no error bars**, so the render cannot settle whether the dip clears noise; the only remaining paths
  are Cognition's per-trial variance or a local probe. Monotone default still retained (a confirmed
  point-estimate dip with no disclosed variance is not a fired disconfirmer). Note the figure's x-axis
  is cost (log $), so the Opus dip is a cost-vs-score efficiency inversion at `max`.
- **Flip condition:** our own ledger showing non-monotonicity on a class we route (then scope the
  row, per W-017).
- **Probe tally:** attested 0 local · self-reported 0.

### W-017 — Non-monotonicity is task-class-conditional; per-step effort is efficiency-only
- **Claim:** The literature's "more effort hurts" results are scoped: tool/function-SELECTION
  degradation (2604.02155) is hypothesis-only for reasoning-trained models; the "3–7-turn
  plateau" (2602.18998) is RETIRED as worded (paper measures a ~96–112K-token context ceiling);
  "lower effort post-error" (2502.08235) is hypothesis-only (never tested as a control policy).
  Per-step effort variation is viable for efficiency (ARES holds iso-accuracy at ~35–45% fewer
  reasoning tokens, trained router, 20B open agent) — "beats task-level" was never run
  head-to-head.
- **Label · grade:** Provisional · Low–Moderate (methods-read re-grades 2026-07-03, full-text,
  opus explorer; verdicts in AHR synthesis §5).
- **Locators:** AHR:research/routing/effort-routing-synthesis-2026-07-03.md §5; arXiv 2604.02155,
  2602.18998 (contested → UNCERTAIN), 2502.08235, 2603.07915, 2604.10866.
- **Flip condition:** a reasoning-model replication of selection degradation, or a task-level vs
  per-step head-to-head — either re-opens the scoping.
- **Probe tally:** n/a (literature scoping record).

### W-018 — D1 basis: curated priors over a learned router (SHARPENED form only)
- **Claim (the licensed form):** *A curated/training-free prior router matches trained routers; a
  strong single-model baseline is hard to beat.* NEVER "learned routers generally fail." D1
  (keep the curated table; no learned router) rests on parsimony + transfer-regime: their setting
  is thousands of samples / 33 models / single-turn QA; ours is single-digit n / ~4 tiers /
  multi-step.
- **Label · grade:** Concordant · Moderate (full-text methods read 2026-07-10; single source; no
  variance behind "reliably" — means over 5 seeds, no CIs; OpenRouter ran a mismatched pool).
- **Locators + excerpts:** arXiv 2601.07206 (LLMRouterBench); read note
  SEAS:reports/2026-07-10-delegation-routing-litgap/notes/2601.07206-llmrouterbench.md:
  *"training-free Avengers/Avengers-Pro is top-tier and near-Pareto-optimal (ParetoDist ≈ 0)"*;
  best router gain ≈ +4% acc / −31.7% cost vs a hindsight Best-Single (GPT-5, 65.96); *"with
  single-digit per-class samples we cannot even reliably identify the best tier … a completely
  different statistical regime."*
- **Flip condition (P-D3):** ≥2 independent results (or one local probe series on our own ledger)
  showing a trained/simple-learned router beating the curated table on agent-harness classes at
  ≤ our data scale → open a hybrid design.
- **Probe tally:** n/a (design-basis record).

### W-019 — Flip thresholds: n=1 never flips; ≥2 attested concordant floor; ~3/side when flip-prone
- **Claim:** Single-shot outcomes are noisy routing supervision (winner-flip 0.645–0.970 across
  MATH/DROP/GPQA; one draw disagrees with the 25-obs pooled winner 47.1% on DROP; utility
  saturates near 3×3 ≈ 9 obs/pair). Adopted rule: **n=1 never flips a row**; **≥2 attested
  concordant** is the floor (a floor the evidence is *consistent with* but does not fix);
  variance-adaptive toward **~3/side on flip-prone classes**.
- **Label · grade:** Concordant · Moderate (full-text read 2026-07-10). Downgrades: single
  source; construct gap — their flip is a 6-way argmax over independently scored scalars, ours is
  a blinded paired A-vs-B verdict which they never study; their scorer is near-deterministic, so
  our judge-noise makes their numbers an UNDERSTATEMENT of our total noise ("n=1 is noisy" holds
  a fortiori); the 0.97 headline is a max-sensitivity union metric.
- **Locators + excerpts:** arXiv 2606.06924; read note
  SEAS:reports/2026-07-10-delegation-routing-litgap/notes/2606.06924-dars.md: *"gains saturate
  fast — 3×3 = 9 observations already ≈ full 5×5"*; *"it does not license any specific small
  count (esp. not '2') for a paired verdict, which it never studies."*
- **Flip condition:** a paired-verdict stability study (or our own accumulated probe series)
  pinning a different stable count → re-derive the floor.
- **Probe tally:** n/a (methodology record; it governs the other tallies).

### W-020 — Effort datum: High→xHigh lifted first-try reliability (direction-only, tightly scoped)
- **Claim:** On **Opus 4.7 / Claude Code / one web-app spec / one evaluator**, effort High→xHigh
  lifted first-try-perfect runs 5/18→16/18 (28%→89%; 61 pp ± ~13 pp SE; 95% CI ≈ [36, 86]) at
  +9–29% cost; a browser testing tool added 42–68% cost with no functional gain; the gain was
  ATTENUATED OR ABSENT under design-prompt arms (full 0/6→4/6; abridged 1/6→1/6 — review lens 1
  nuance, adopted). Enters warrant cells at Moderate,
  **direction-and-ordering only**; magnitudes do not port across models/harnesses/tasks; the win
  is largely deliberation-clears-environment-faults (Docker/npm), not a broad quality lift.
- **Label · grade:** Concordant · Moderate (full-text methods read 2026-07-10; numbers re-checked
  vs Tables 2 & 5). Downgrades: single author; single unblinded evaluator; observational,
  non-preregistered; n=6/cell; first independent effort-resolved agentic datum — no replication.
- **Locators + excerpts:** arXiv 2607.02436; read note
  SEAS:reports/2026-07-10-delegation-routing-litgap/notes/2607.02436-effort-not-tools.md: *"The
  High-vs-xHigh contrast is entirely within Opus 4.7 / Claude Code"*; *"xHigh did NOT recover
  reliability under a design prompt."*
- **Flip condition:** replication on a second family/spec/blinded scoring failing to reproduce
  the direction → drop to Reported and unwind any row that leaned on it.
- **Probe tally:** n/a (literature record; feeds W-004/W-016).

### W-022 — Vendor model-role guidance: no fable-orchestrator recommendation; the first-party pattern is executor+advisor (added 2026-07-10, post-review, operator-prompted)
- **Claim (composite, negative, scoped):** No official Anthropic surface states "use Fable 5 as
  the orchestrator and Sonnet for subagent/executor work" as a recommendation — **under the
  2026-07-10 vendor-docs lane's logged queries**, with named blind spots (agent-teams doc, the
  Fable 5 launch post, support.claude.com direct fetches). What official surfaces DO state:
  (i) capability prose, not role prescription — *"Claude Fable 5 is significantly more dependable
  at dispatching and sustaining parallel subagents"* (prompting guide); (ii) the model-selection
  matrix lists Opus 4.8/Sonnet 5/Haiku 4.5 as starting options, fable prose-only, and *"Fable 5
  is not the default model"* (Claude Code model-config); (iii) subagents default to **inherit**
  (no vendor pairing); Haiku's example use cases include *"sub-agent tasks"*; effort docs give
  `low` as typical *"like subagents"*; (iv) the productized cost-tiering pattern is `opusplan` —
  *"Opus's reasoning for planning with Sonnet's efficiency for execution"*; (v) the closest
  first-party analog to the operator's pattern is the **advisor tool** (read first-hand
  2026-07-10): *"You currently use Sonnet on complex tasks: Add a higher-tier advisor. Opus keeps
  total cost similar or lower; Claude Fable 5 maximizes the quality lift"* — a mid-generation
  strategic consultation, NOT fan-out orchestration; (vi) the famous lead-agent datum (*"Claude
  Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4
  by 90.2%"*) **predates fable**. The "fable-orchestrator playbook" framing is third-party
  attribution without a located first-party citation.
- **Advisor-tool operational facts (first-hand fetch 2026-07-10, routing-relevant):**
  **fable/mythos advisors return ENCRYPTED advice** (`advisor_redacted_result` — the executor
  reads it server-side; the client/audit trail cannot); **opus-4.8 advisors return plaintext** —
  under this package's transcript-ground-truth discipline, an auditable opus advisor is preferred
  wherever the advice is load-bearing. **Scope (added 2026-07-10, operator-prompted):** these
  encryption/reliability facts attach to the advisor **TOOL** (`advisorModel`, API/harness level)
  ONLY — an advisor **subagent** (an agent pinned to the role, e.g. the Cowork fork's `advisor`)
  returns ordinary plaintext agent output on ANY model, and is the functional equivalent where
  the tool is unavailable or broken; do not extend tool caveats to agent-based advisors (a driver
  made exactly that over-extension during the 2026-07-10 Cowork fork diff — operator-caught). Measured vendor datum: *"pairing a Sonnet executor at
  medium effort with an Opus advisor achieves intelligence comparable to Sonnet at default
  effort, at lower cost"* (feeds W-016's dial economics). Executor-specific steering: nudge
  +7 pp on Haiku, ≈0 on Sonnet, slightly negative on Opus — evidence that **routing/steering
  guidance is router/executor-model-conditional** (gap register G-02). `max_tokens: 2048`
  reduced advisor output ~7× with no detected quality loss (n=40, vendor). Beta, Claude API +
  AWS platform; ~~**Claude Code exposure NOT confirmed by this page** — Unchecked, to verify.~~
  **CONFIRMED 2026-07-10** (routing-gaps survey; booting re-fetch of code.claude.com/docs/en/advisor):
  Claude Code exposes the advisor via `/advisor`, `advisorModel`, `--advisor`, and
  `CLAUDE_CODE_DISABLE_ADVISOR_TOOL`, with an accepted-advisor table (Fable-main accepts ONLY a Fable
  advisor; Sonnet-main accepts a Fable/Opus/Sonnet advisor) [C-001]. **Reliability caveat:** GH #76199
  (2026-07-09) reports `advisorModel: fable` failing deterministically (`error_code: "unavailable"`)
  on any transcript containing a `tool_use` block, while `advisorModel: opus` is unaffected [C-004] —
  reinforces R14's opus-4.8-advisor choice on reliability as well as auditability grounds.
- **Label · grade:** the negative composite: Corroborated · Moderate (a severe hunt that could
  have found it and didn't; blind spots named — NOT corpus-level absence). Individual vendor
  statements: Concordant/Reported · Moderate (first-hand or lane-CONFIRMED fetches; vendor
  self-reports, benchmark ns small).
- **Locators:** package-external lane record (quotes + URLs):
  SEAS:research/2026-07-10-delegation-triage-stage1/vendor-docs-lane.md;
  platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool (fetched in full);
  platform.claude.com/docs/en/about-claude/models/choosing-a-model;
  platform.claude.com/docs/en/build-with-claude/effort; code.claude.com/docs/en/model-config +
  /sub-agents; anthropic.com/engineering/multi-agent-research-system;
  claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them.
- **Interactions:** challenges R13's warrant *reading* — the fable-orchestrator pin is operator
  policy (ADR-0004 enumeration + the effort-inheritance mint), NOT vendor guidance, and W-002/R13
  must not be cited as if vendor-backed; corroborates W-006 and W-016 (see their interaction
  lines).
- **Flip condition:** a first-party page stating the fable-orchestrator recommendation (the named
  blind spots are the first places to look: agent-teams doc, launch post) — **all three named blind
  spots fetched full-text 2026-07-10 (routing-gaps survey); none contains it [C-003]**; or Claude Code
  shipping advisor config (upgrades R14 from CANDIDATE toward adoption testing) — **PARTIALLY MET
  2026-07-10: advisor config confirmed shipped in Claude Code [C-001]; R14's prerequisite is met but
  adoption still requires local probes (G-10).**
- **Probe tally:** n/a (vendor-guidance record); R14 adoption requires local probes.

### W-021 — The delegation test's theory backing (CONTRACT §1)
- **Claim:** (i) A delegated multi-agent network adding no new exogenous information is
  decision-theoretically dominated by a centralized decision-maker with the same information
  (2603.26993). (ii) On fixed-step workflows, deterministic orchestration matched LLM
  orchestration's accuracy at up to 3.5× fewer tokens (2605.09894, COBOL-modernization domain).
- **Label · grade:** Reported · Low (both abstract-only; theory licenses a design *heuristic* —
  delegate only for new information / parallelism / isolation; scripts for fixed steps — not an
  operational guarantee).
- **Locators:** arXiv 2603.26993; arXiv 2605.09894.
- **Flip condition:** a methods read showing the theorem's idealizations exclude our setting, or
  domain-transfer failure evidence → downgrade the heuristic to taste and say so in CONTRACT §1.
- **Probe tally:** n/a (design-basis record).

### W-023 — R7 sonnet-first default (operator ruling)
- **Claim:** deep-read/exploration lanes default to **sonnet high** (`explorer` pin re-pointed
  from opus/high); opus is a per-call escalation requiring a stated judgment-discrimination
  reason (adversarial refutation, methods adjudication, many-source conflicting synthesis) or
  evidence (cheap-tier output failed review). The harness — the pin's claim-discipline contract
  (source-per-claim, declared blind spots, facts-not-judgments) — is what carries baseline
  quality, per the "default down, harness up" doctrine now applied to R7 itself.
- **Label · grade:** Operator ruling (2026-07-17, Bridgewright session) · policy, not a
  measured capability claim. Consistent with prior signal: W-006 (diverse sonnet lanes over
  higher tier for sweeps) and the observed pattern that explorer-light (sonnet/medium) lanes
  repeatedly survived main-loop spot-checks on load-bearing numbers (refresh #3/#4,
  2026-07-10/17, bridgewright). No paired sonnet-vs-opus probe on the R7 class yet.
- **Locators:** `~/.claude/agents/explorer.md` (pin frontmatter + description, 2026-07-17);
  bridgewright refresh #4 spot-check record (`docs/competitive/2026-07-17-competitive-refresh-4.md`).
- **Flip condition:** a sonnet R7 lane failing main-loop verification on a load-bearing claim
  that a paired opus lane (identical harness) gets right → restore opus default or add a
  class-specific carve-out; run the paired probe at the next naturally-arising deep-read
  fan-out (no bespoke spend).
- **Probe tally:** 0 paired on R7 proper; adjacent evidence only (explorer-light spot-checks).
