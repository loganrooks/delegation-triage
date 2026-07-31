# PROBE — harness-compensated opus vs bare fable (SYSTEM probe) — REGISTERED, PENDING TRIGGER

- probe_id: P-20260717-harness-compensation-registration
- **status: REGISTERED 2026-07-17 — fires at the next operator-ordered gate-level
  document review in signal-layer** (candidates: DF-2 fix proposal review, Proposal F
  rev.3 pre-ratification review, first W-F1 evidence-memo gate). Nothing runs until the
  operator orders that review.
- question: **can a fable-authored harness carry opus to fable-grade framing review?**
  — the registered open question in `~/.claude/delegation.md` §Instrumentation ("can
  fable AUTHOR the contract/harness … and have non-fable executors deliver fable-grade
  results?"). First deliberate firing. P-20260717 (framing pair) is the motivating
  data: the tier margin came down to one catch of a compilable class, and the fable
  leg's own output hinted its edge may be partly loop, not model (advisor-preamble
  caveat).
- class / tally row: **harness-compensation (NEW class row)**. W-019 discipline
  unchanged: no route change below ≥2 clean concordant firings in THIS class.
- operator authorization: given 2026-07-17 (operator "sure" to the explicit proposal
  naming one fable contract-author spawn + one bare-fable review leg) — satisfies
  fable-usage-requires-ask at registration; firing needs no separate re-ask beyond the
  operator ordering the gate review itself. Fable spawn budget: exactly two (author +
  leg F), once.

## Design — a SYSTEM probe, asymmetric by construction

This compares **agent-harness systems, not models on identical prompts**; byte-identity
across legs is deliberately NOT a goal here. Instead each leg's full config is frozen
and hashed at firing.

- **Leg O — harness-compensated opus (xhigh):**
  1. **Contract authored by fable**, in a separate prior spawn, from the defect-class
     corpus only (probe records, panel syntheses, process-lessons blocks) — **the
     target artifact is NOT in the author-spawn's context**; contract text frozen +
     sha256-hashed before the target artifact's final text is embedded anywhere.
  2. Staged passes: (i) extract every normative ruling from the design memo/basis docs
     into a list; (ii) contradiction sweep — each ruling diffed against the proposal's
     decisions AND against inlined cited code; (iii) the open framing questions.
  3. **Mechanical context-curation rule (fixed now, so curation can't steer):** every
     `file:line` the artifact cites is inlined ±15 lines, verbatim, no selection
     judgment.
  4. Second opus pass prompted solely to attack pass-1's blind spots; leg output =
     unioned findings.
- **Leg F — bare fable (xhigh):** the P-20260717 minimal open contract verbatim (four
  framing questions + ONE recommendation), artifact embedded, snapshot-only, no tools.
- Blinding: labels coin-flipped for any operator-facing table; **acknowledged weak** —
  output structure (staged vs essay) may self-identify the system. Recorded, not
  pretended away.
- Relay integrity (P-20260717 lesson 4): each leg's raw final message sha256-hashed at
  relay time; hashes in the outcome section.

## Adjudication (chosen NOW, per probe-adjudication-needs-domain-scaffolding)

**Author-adjudication-with-disclosure against this pre-agreed rubric; the operator
countersigns the scored table, not the raw artifacts.**
- **R1 — verified-finding count:** findings surviving primary-source verification
  (text-vs-code claims checked against the code, quotes against the docs).
- **R2 — highest-severity unique catch:** severity = potential for permanent
  data-plane damage or wrong ratification; scoring reasoning shown in full.
- **R3 — adopted count:** findings adopted into the artifact's next revision at
  disposition time.
- **R4 — cost (reported, not scored):** tokens per leg × prices at firing date
  (including Leg O's author-spawn amortization note).

## Pre-registered predictions

- **PH-1:** compensated opus ≥ bare fable on R1.
- **PH-2 (decisive):** every bare-fable finding is either (a) also found by
  compensated opus, or (b) of a class NOT encoded in the fable-authored contract. Any
  finding the contract *should* have elicited that compensated opus still missed ⇒
  harness-compensation FAILS for that class — the premium is not compilable there.
- **PH-3:** the (b)-set — fable-unique, un-encoded classes — is the measured
  **lens-discovery premium** this round; count it. Zero ⇒ the premium was fully
  compilable this cycle; each member otherwise becomes a new contract lens (the
  amortization loop).

## Caveats registered at pre-registration

n=1 per firing; artifact class = governance documents only (no generalization to code
review from this probe); the contract author sees corpora containing fable's own past
catches — favorable to the compilation hypothesis, disclosed; xhigh both legs (effort
is controlled, harness is the manipulated variable).

---

## Outcome (appended at firing)

- **FIRED 2026-07-27** (session `9c589b4e…`, signal-layer). Trigger: the W-F1a rev.2
  re-review — the operator-ordered gate review the registration names (P1 was scored
  REFUTED at the 2026-07-17 gate; the pre-registered consequence is revision +
  re-review; the operator's "No-go pending revision" ruling ordered it). Firing
  needed no separate re-ask per the registration terms above.
- **Target artifact:** signal-layer `tests/evidence/w-f1a-capability-split-rev2.md`
  (authored 2026-07-27, post-registration — could not have leaked into the corpus).
- **Contract authored** by fable spawn (generic Agent, effort session-inherited —
  surface stated per CONTRACT §3), corpus-only, all `w-f1a*` files excluded from its
  context by explicit prompt exclusion (compliance = Reported by prompt construction,
  not transcript-audited). Contract v1 frozen BEFORE any leg saw it:
  sha256 `f5a4c8f9483cdd6fa42bae2674322bdcd011ea975a767db09fc8822a725e7bf8`
  (13,263 bytes, `/tmp/sl-gpt-window-20260727/out/hc-contract-v1.frozen.txt`; author
  raw final message sha256 `6efa32658c73cda437e692e742f72fd109b806752c350f708f0dedc1b9b550b1`).
  16 defect classes (DC-1..16), staged passes, claims-discipline output rules.
- **Leg O prompt** (contract + embedded target + MECHANICAL ±15-line inlining of all
  30 target citations, basename-resolved, fixture copies excluded, zero unresolved):
  sha256 `ebee80efe0e3af45ff406c2b89d51b0e796e3bc895d7e103f512c468235d3380` (96,051
  bytes). Legs run as Workflow `wf_932e17c4-eb4`: pass 1 opus/xhigh + pass 2
  opus/xhigh critic (blind-spot attack on pass 1).
- **Leg F prompt** (P-20260717 minimal open contract adapted to the re-score
  decision, target embedded, snapshot-only): sha256
  `a36bda84e60791c30859219266d33f6d63cea1de7a35a7b2f719fc0b92fb7dde` (26,030 bytes);
  fable/xhigh, same workflow.
- **Independent evidence available for R1 scoring** (gathered OUTSIDE both legs,
  before they returned): two blind rev.2 pre-reviews already exist — gpt-5.6-sol/high
  (FAILS-P1, 3 new blockers) and Claude roster reviewer opus/high (FAILS-P1, 3
  blockers, partially overlapping). Leg findings can be scored for verification
  survival against these + primary sources.
- **Deviation, named at firing:** the registration's Leg F clause says "the
  P-20260717 minimal open contract verbatim"; the four framing questions + ONE
  recommendation structure is preserved verbatim, but the frame sentence necessarily
  changed (ratify-a-proposal → re-score-P1) and the embedded artifact is one document,
  not two. Recorded as an adaptation, not silent.
- **Legs COMPLETE 2026-07-27** (workflow `wf_932e17c4-eb4`; 3 agents, 0 errors,
  223,735 subagent tokens total; a mid-run operator pause interrupted the pass-2
  critic's start — resumed, all three finished). Raw outputs extracted from the
  workflow journal and hashed at relay [per relay-integrity lesson, P-20260717 #4]:
  - **Leg F (fable/xhigh, bare):** sha256 `30f1fe7c…8fc2f8` (10,556 B) —
    `/tmp/sl-gpt-window-20260727/out/hc-leg-a814413e.md`
  - **Leg O pass 1 (opus/xhigh, contract):** sha256 `f6c562d3…53abcb` (16,494 B) —
    `…/hc-leg-a3ec6cca.md`
  - **Leg O pass 2 (opus/xhigh, blind-spot critic):** sha256 `5c96e2c8…e15e44`
    (38,775 B) — `…/hc-leg-ae7c0701.md`; Leg O output = pass 1 ∪ pass 2 per design.
- Structure note (Reported from journal excerpts, pre-adjudication): Leg O returned
  numbered severity-tagged findings mapped to contract defect classes (F-1..F-16+
  with per-DC checklist accounting, including a claimed third-absence-state finding
  and a citation-overreach catch on the memo's `input_tokens` warrant); Leg F
  returned the four framing answers + one recommendation. Token asymmetry: Leg O
  ~145k+38k two-pass vs Leg F ~60k single-pass — cost reported under R4, not scored.
- **RELAY CORRECTION (2026-07-28):** the workflow journal's `result` for Leg O pass 1
  captured only the LAST assistant text block (16,494 B) — the full output was two
  blocks (VERDICT + F-1..F-11 in the first). Reassembled from the transcript:
  `hc-leg-O-pass1-FULL.md`, 37,619 B, sha256 `df506b9ce28e96e1…cf611cee`. The earlier
  leg-O hash row above covers the truncated portion only. Lesson filed: journal
  `result` = final block, not final message — reassemble multi-block outputs from
  transcripts before hashing.

## R1–R4 scoring (2026-07-28, author-with-disclosure — COUNTERSIGNED: operator, 2026-07-31
in-session, "yes" to the pilot-closure package whose first item was this countersign ask)

Verification bar for R1: a finding counts if (i) byte-checked true by the author
against primary source this session, or (ii) independently concordant with one of
the two blind rev.2 pre-reviews (which were themselves byte-verified). Sampled, not
exhaustive — unverified findings listed as pending, not counted.

- **R1 (verified-finding count): Leg O 10 · Leg F 6.**
  Leg O verified: F-2 parse-error normalization (≡ sol#2, byte-true at
  `obs-subagent-stop.py:169-175`); F-5/F-9 missing joins/sourceless shape members
  (≡ claude F5 envelope class); F-12 input_tokens citation overreach (checked: no
  inlined window shows the `b["in"]` mapping); F-13 date-stamp collision (true,
  trivial); F-16 precedence never stated (true); F-18 phantom stops carry null
  `agent_type` — Q3's per-type denominators exclude them (byte-true: the branch
  guard at `obs-subagent-stop.py:172` requires `not agent_type`); F-19 resolver
  contract cited as pre-registered against a passage specifying a DIFFERENT object
  (byte-true: proposal `:254-256` = per-field status enum, not byte-fetch); F-22
  permission_mode warrant cites an example its own inventory refutes (≡ claude F6 +
  author's Codex byte-check); F-23 licence clause omits the W-F1d machine_id /
  BLOCKED-waiver gate (byte-true against lane `:248-252`); F-25 FAIL limbs
  attributed to §3a but living in P1 (byte-true). Pending-unverified: ~16 more.
  Leg F verified/validated: #3 universal-solvent objection (validated by the rev.3
  round — both independent reviewers found COND-COMMON/scheme-tagging used as
  euphemism); #4 battery-as-regression-suite (≡ sol#6/claude F8); #6 matrices
  single-verifier, demand source re-derivation (vindicated — the claude rev.2 review
  re-derived and found the envelope misses); #7a tokens_input_uncached rests on a
  reasoned claim, one measurement retires it (vindicated — claude F2 measured the
  Codex side and refuted the fill); #1/#2 the two ex-ante frozen-wording rulings
  (materialized: the operator had to rule exactly such a fork — "score over three").
- **R2 (highest-severity unique catch): Leg O — F-19.** Unique (neither independent
  review caught it); consequence class = wrong ratification: Q5's PASS rides a
  byte-fetch resolver signature no ratified text authorizes, and W-F2 would have
  been built against it with P3 scored on a self-licensed deliverable. Leg F's best
  unique = the ex-ante ruling demand (#1/#2) — decision-hygiene value, materially
  shaped the gate, but no direct artifact-damage path. Reasoning disclosed: severity
  rubric weighs permanent/ratification damage over process hygiene.
- **R3 (adopted count): 0 · 0 at this scoring — structurally deferred.** rev.3
  deliberately did NOT disposition probe-leg findings (its declared gap 5); adoption
  is scored at rev.4 disposition. Early signal: F-18/F-19/F-22/F-23 are rev.4
  candidates on their face.
- **R4 (cost, Reported from harness counters):** Leg O ≈ 145k (pass 1) + ~79k
  (pass 2, workflow-total remainder) ≈ 184k+; Leg F ≈ 60k; contract author spawn
  (fable, generic Agent) unmeasured separately. Whole firing ≈ 224k workflow +
  author spawn. Plan-included capacity, both vendors.

## Pre-registered prediction verdicts (author-scored, operator countersigns)

- **PH-1 (compensated opus ≥ bare fable on R1): CORROBORATED** — 10 vs 6, and the
  O-set is byte-concrete where the F-set is framing-level.
- **PH-2 (decisive — no contract-encoded class that compensated opus missed):
  CORROBORATED on this firing.** Every Leg F finding of an encoded class has an O
  counterpart (F #7b precedence → O F-10/F-16; #7a → O F-12; #4 circularity → O F-3
  under DC-8/DC-9; #6's demanded source-diff → O executed it as DC-3). No
  should-have-elicited miss found. Harness compensation HOLDS for the encoded
  classes, n=1.
- **PH-3 (lens-discovery premium): NONZERO — 2 classes.** (i) ex-ante
  frozen-wording/scoring-protocol rulings (which reading governs; per-feature vs
  binary scoring) — no DC covers it; (ii) blind adversarial-battery authorship as a
  review-protocol requirement. Both become candidate contract lenses (the
  amortization loop). The fable premium this round concentrated in gate-design
  judgment, not defect-finding — consistent with the operator's 07-24
  fable-retained-classes ruling (orchestration/brainstorming/long-horizon).
- **Tally (harness-compensation class, firing 1): counts, with caveats** — author
  adjudicated (disclosed at registration: author-with-disclosure IS the pre-agreed
  protocol, so this firing is CLEAN under its own terms pending operator
  countersign); n=1; governance-document class only; Leg O pass-1 relay truncation
  corrected before scoring. W-019: no route change until ≥2 clean concordant
  firings — this is firing 1.
