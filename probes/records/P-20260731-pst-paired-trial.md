# P-20260731-pst-paired-trial — wave-2 paired substitution trial (pilot §6 C′, the ONLY overlay-row instrument)

- **date:** 2026-07-31
- **class:** bounded implementation, paired arms — 6 frozen tasks (4 workflow-gate @251b5b4,
  2 storage-advisor @cc38138), ≤3 owned files, deterministic oracle each
- **arms:** `google:gemini-3.6-flash-high` (native antigravity adapter, fpc-native-manifest-v1,
  under gate G1–G4 + G3 preamble) vs incumbent `anthropic:opus-5@medium` (roster implementer,
  R4, same gate). Counterbalanced (T1/T3/T5 flash-first, T2/T4/T6 opus-first); byte-identical
  vendor-neutral packets; diffs vendor-blinded at adjudication (arm-X = lexicographically
  smaller diff sha256).
- **pre-registration:** `docs/proposals/2026-07-31-paired-substitution-trial.md` (task-set
  freeze commit f77370f; HOLD released at c30550d after the gate spot-check).
- **attestation:** driver-attested throughout — every acceptance is the DRIVER's fresh oracle
  rerun (never the worker's claim), scope by `git status --short`, G4 hidden-effects sweep per
  leg; model identity per accepted leg: opus transcript-attested (`claude-opus-5` in subagent
  JSONL API records ×6), flash provider-log-attested (`gemini-3.6-flash-high` resolver lines in
  adapter run_dirs ×6). Blinded adjudication by a fresh non-author reviewer
  (opus×high), verbatim on file: `docs/reviews/2026-07-31-pst-blinded-adjudication.md`; blind
  mapping sealed (chmod 600) until after delivery, now
  `probes/fixtures/pst-20260731/MAPPING-UNSEALED.md`. All artifacts (packets, envelopes, 12
  diffs, flash run reports, interrupted-attempt diffs): `probes/fixtures/pst-20260731/`.
  Ledger: 12 intents + all attempt outcomes in `~/.delegation/v2/intents-2026-07.jsonl`
  (runs `pst-{flash,opus}-t{1..6}-20260731`; XV-10 denominator = all intents, all terminal).
- **tally:** feeds W-026. Moves NO flip counter and proposes NO overlay row — the
  pre-registered decision rule terminated it: acceptance 6/6 vs 6/6 is a metric tie, and
  "any metric tie → no row". Severe counter unchanged (0 severe events this trial, either arm).

## Measured results

| metric | flash arm | opus arm |
|---|---|---|
| acceptance (terminal) | 6/6 | 6/6 |
| severe events | 0 | 0 |
| rework rounds | 0 | 0 |
| attempts spent for 6 accepts | 15 (6 adapter-cwd scratch landings, 3 network errors) | 10 (4 network casualties across two outages) |
| blinded quality verdicts | better on 0 | better on 5 (T4 control: equivalent) |
| wall per accepted run | 48s–290s (batch logs) | ~3–14 min spawn→report |
| cost | not metered (CCPA) | 104,576 output tok / ~15.0M input (cache-dominated), transcripts |

**Decision-rule outcome: NO overlay row** (tie on acceptance; quality verdicts reinforce).
Symmetric clause: nothing recorded against R4 — incumbent had no severe events and no
acceptance deficit.

## The discriminating finding (blinded adjudication)

The arms are **indistinguishable on fully-specified edits** — T4's patches differ by one
identifier; T3's source patches are byte-identical (same git blob) — and **separate entirely
on open-ended test authoring**: on every discriminable task the adjudicator found the flash
deliverable contains tests that cannot fail on the regression the packet was about (T1
concurrent return values discarded; T2 `project_of` passes under substring matching; T3
neither handle-close pinned — half the packet's objective; T5 report verdicts unasserted),
while the opus deliverable carries anti-vacuity guards (barriers, redirect-assertions,
mutation checks) at ~1.7× the lines and occasional over-delivery. The adjudicator's blind
style clustering (Style A/B) maps exactly to opus/flash on all five discriminable tasks —
recovered with zero vendor knowledge. (One internal slip in its score line, "Style B took
T6", contradicts its own label attribution; per-task verdict lines govern.)

**Vacuous-green is invisible to the current gate by construction** — a green suite is what a
vacuous test produces. The adjudicator's proposed G5 (for test-authoring packets: mutate or
revert the behavior under test, require the NEW tests to go red) would have flagged all four
instances at the cost of one extra suite run per task. Gate-evolution candidates recorded:
G5 mutation check · post-suite runtime-effects assertions (`git status --porcelain`
unchanged; no new `$TMPDIR` entries — would have caught opus-side T3 temp-dir leak and T6
repo-root execution, the two amendment-required findings) · within-file constraint checks
(T1 flash breached "beyond imports" without declaring a DEVIATION).

## Infrastructure notes (fault-attributed environment, not model)

- Adapter cwd bug (signal `obs-20260731T200828-ee7d76`): 6 scratch landings this trial
  (t1×2, t3×2, t4, t6) vs 3 correct first-landings — G3 preamble self-blocked cleanly all 6
  times, zero contamination. The delegator-answer envelope (workspace path prepended to the
  frozen packet, packet bytes verbatim — symmetric with the opus arms' spawn prompts, which
  always carried the workspace path) resolved it 4/4.
- Two multi-hour network outages killed 7 opus spawn attempts and 3 flash runs mid-trial;
  all relaunched fresh (never resumed — CONTRACT §3 model-pin hazard), interrupted-but-
  complete work preserved to `.diff` files and workspaces reset to baseline before relaunch.
  **Independence blemish, disclosed:** the preserved t4 attempt-1 diff sat in the shared
  parent dir and the T4 replacement worker found and read it (its report discloses this and
  states it started fresh from the verified-clean tree). Impact on results: none assessed —
  T4 is the fully-determined control, judged "equivalent", and the flash arm produced the
  same edit with no such access — but preserved partial work should be quarantined OUTSIDE
  the workers' visible tree next time.
- Adapter preflight requires prompt files mode 0600 (one instant rejection, my delivery error).
- Report-delivery friction: opus implementer spawns WITHOUT the DELIVERY clause stranded
  their reports as plain text 3/3 (nudge recovered all); spawns WITH the clause delivered
  first-try 3/3 — replicates the explorer-pin measurement (e763f85) on the implementer lane.
- Packet errata found by workers, affecting both arms equally: T5 cited cli.py:352 for the
  dispatch (actually the argparse def; dispatch at :104); T3's function line refs off by 3–4.
- Flash reporting fidelity, again: two "verbatim" validation quotes omitted the
  `(skipped=1)` suffix; one claimed exit 0 on a run its own note describes as failed.
  Driver reruns were authoritative in every case (the standing rule held).

## Post-closure addenda (2026-07-31 evening)

- **Independent concordant second read.** The FIRST adjudicator spawn — recorded above as a
  mid-stream-stall casualty — turned out to have completed all bundle reading before the
  stall; the shutdown message resumed it from its intact transcript and it delivered a full
  independent adjudication before terminating (verbatim:
  `docs/reviews/2026-07-31-pst-blinded-adjudication-second-read.md`). **Verdict directions
  identical on all six tasks; same signature clustering with the same de-blinded mapping;
  same two gate headliners.** Unique adds folded in: T1 packet fault (`.planning/STATUS.md`
  named in the objective but not ownable — both arms, neither flagged it); T5-opus
  redaction test near-vacuous under its own mock; T1-flash unbounded `join()`. Post-resume
  model transcript-attested `claude-opus-5` — the spawn pin HELD through resume (n=1
  counter-instance to the CONTRACT §3 rebill hazard; treat that hazard as
  surface-dependent). Process lesson: for read-only reviewers a final-turn stall leaves the
  expensive work intact in the transcript — the relaunch redid ~250k tokens of reading a
  resume would have skipped.
- **Zombie-session forensics corroborate integrity.** On shutdown, the outage-casualty
  sessions (t2, t2b, t5, t6, t6b opus) each delivered read-only terminal reports attesting
  zero writes in their lifetimes, with clean-tree observations at their session starts and
  correct flag-don't-touch handling of the successor arms' work they found in the shared
  workspaces. Their "contamination" warnings dissolve under the relaunch design (one arm =
  one workspace = one run_id; successive sessions are ATTEMPTS of the same arm, and each
  accepted attempt verified a clean tree pre-edit) — but they were the right warnings for a
  session lacking that context to raise.

## Countersign

Pre-registered: operator countersigns adjudication outcomes. **COUNTERSIGNED 2026-07-31
(operator, in-session, as-is — after both concordant blind reads were on file).**
