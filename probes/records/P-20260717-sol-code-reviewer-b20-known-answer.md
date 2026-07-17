# PROBE — 2026-07-17 sol-code-reviewer B20 known-answer test

- probe_id: P-20260717-sol-b20-known-answer
- task class / ROUTES row: review gates (code review lane) — first live firing of the
  `sol-code-reviewer` pin (gpt-5.6-sol, high, CLIProxyAPI gateway)
- configs compared (model × effort × surface × harness): single leg —
  gpt-5.6-sol × high × Agent-tool typed spawn (`sol-code-reviewer`) × charter-pinned prompt
  (diff-scoped, file:line + concrete-failure-scenario required, severity-ranked, verdict line).
  Scored against a **known answer key**, not a paired leg: fable-high adversarial review
  (7 findings) + codex connector rounds 1–2 (4 findings) of the SAME artifact, all findings
  later confirmed/fixed/merged (arxiv-mcp-pro PR #24 → main `d5f1369`; goal/STATE.md D-031).
- harness/contract hash (if pinned): not hashed; prompt verbatim in parent transcript
- blinded?: **INTENDED yes, ACTUALLY NO after tool call 42** — see deviations. The review
  worktree was detached at the pre-fix commit `2c324ac` and contained no `goal/` ledgers, but
  a git worktree shares the parent repo's object DB and refs: sol ran
  `git log --oneline --all` (call 42) and then READ the three fix commits (`af997dd`,
  `e291eb5`, `be329f4`) and the merged squash (`d5f1369`) — calls 43–46, 51. Everything
  demonstrated at call ≤41 is clean; everything first demonstrated after is contaminated.
- frozen tree?: yes — read-only worktree at `2c324ac` (PR #24 commit 1 of 4)
- adjudicator: author (parent session that also ran the original B20 pipeline) — deviation
- router: fable[1m] × high × Agent-tool typed spawn (operator-directed experiment: "you can
  try delegating the review as well … to gpt-5.6-sol")
- **attestation:** subagent transcript JSONL at
  `/private/tmp/claude-501/-Users-rookslog-Development-arxiv-mcp-server/d708c558-f626-4806-88d2-a198d216de3a/tasks/a4679dffe4f379365.output`
  (55 tool calls; tool-call ordering + repro scripts extracted and audited in the parent
  session); ground truth = `arxiv-mcp-server/goal/STATE.md` D-031 +
  `goal/ledger/reviews.jsonl` rows `rev-20260717T194523` (fable), `rev-20260717T201312`,
  `rev-20260717T205805` (codex). MAJOR-1 repro re-run FIRST-HAND by adjudicator
  (`completion_gap=0.000027s` at interval 0.300s) — not taken on the subagent's word.
- verdict: sol returned **DO-NOT-SHIP** with 4 MAJOR + 1 MINOR. Ground truth: fable said
  SHIP-WITH-FIXES (1 MAJOR + 6 minors); codex filed 4 P2s over two rounds. All 5 sol
  findings correspond to real, later-fixed defects — **zero false positives**.

## Scoring vs the answer key (contamination-adjusted)

| Ground-truth finding | Caught by sol? | Clean or contaminated? |
|---|---|---|
| fable MAJOR-1: cross-lane fail-open serialization gap | YES (sol MAJOR-1) | **CLEAN** — reproduced at calls 36–37, before call 42; sol's forced-interleaving repro (mock `_cross_process_gate` → OSError, async+sync race) measured a 0.000024s gap, independently re-measured by adjudicator at 0.000027s |
| codex P2-1: reindex/read race (cleared index visible to concurrent search) | YES (sol MAJOR-2) | **contaminated at repro time** (call 49 > 42); line of inquiry demonstrably pre-dated contamination (diffed `index_paper_by_id`/`handle_reindex` vs HEAD^ at calls 22, 31) but no finding was *demonstrated* pre-42 — scored partial |
| codex P2-2: shared `arxiv.Client` cross-thread `requests.Session` | YES (sol MAJOR-4) | **contaminated at repro time** (call 54 > 42); strong pre-42 evidence of independent pursuit: call 30 WebFetched the arxiv-py 2.4.0 source specifically for Client session/delay state — scored partial |
| codex P2-3: README/CHANGELOG doc drift | YES (sol MINOR-5) | **CLEAN** — found at calls 38–41 (< 42); sol additionally cited the AGENTS.md changelog requirement, which codex did not |
| codex round-2: lock must be held until worker exits (cancellation hole) | anticipated (sol MAJOR-3: orphaned `to_thread` worker survives handler cancellation; "keep an index-exclusion lock held until the worker—not merely the handler coroutine—actually exits") | **CONTAMINATED** — stated after reading `be329f4`, whose commit HEADLINE is literally "hold the reindex lock until the worker exits"; no pre-42 evidence. (Note the answer key excluded this one anyway: the specific hole was introduced by fix commit `e291eb5`. Sol's variant — no lock at all at `2c324ac`, so an orphaned worker overlaps anything — is real at the reviewed tree but largely subsumed by MAJOR-2.) |
| fable minors 2–7 (6 items) | ~1/6: sol's MAJOR-4 IS the substantive core of fable's MINOR-4 (shared cross-thread `requests.Session`), elevated a tier; the other 5 unmatched | see the prompt-confound amendment below — the minors axis of this probe is CONFOUNDED |

**Clean-catch summary: 2/5 answer-key items caught demonstrably blind (incl. the single
hardest one, fable's MAJOR-1, with a working repro fable itself did not produce); 2 more
matched with pre-contamination inquiry evidence but post-contamination demonstration;
1 contaminated; 0 false positives; 0/6 fable minors.** Method note: sol was the only lane
of the three that shipped *executable reproductions* with its findings (fable argued from
code reading; codex from inspection).

- unique catches (per leg): single leg — nothing outside the answer key beyond the AGENTS.md
  citation detail on the doc-drift finding.
- tokens / cost (if observable): NOT observable — gateway reported `subagent_tokens=0`;
  55 tool calls, ~8 min wall clock.
- **tally:** feeds W-001 (review gates — independence/second-voice value, cross-vendor
  arm) and is the FIRST attested datum for the `sol-code-reviewer` pin specifically;
  count after this record: sol-code-reviewer known-answer n=1 (clean-blind catch of the
  hardest item + zero false positives; blind protocol failed partway). Not yet a
  routing-changing n.
- deviations from clean protocol (named):
  1. **Blinding breach via shared object DB** — a `git worktree` is NOT a frozen snapshot:
     `--all` refs expose the future. Next time export with
     `git archive <sha> | tar -x -C <dir>` (or clone `--depth 1` at the SHA and delete
     other refs) so the answer cannot be looked up.
  2. Author-adjudicator (same session built the fixes being used as ground truth).
  3. Single leg, not paired; answer key stands in for the comparison legs.
  4. Cost leg unobservable (gateway token reporting absent).
  5. **PROMPT CONFOUND on the minors axis (operator-caught, amended 2026-07-17).** The
     sol prompt was NOT the fable prompt. Verbatim comparison (both prompts on disk —
     fable's in the parent-session pre-compaction transcript, sol's in this record's
     attestation) shows three asymmetries: (a) fable's prompt contained finding-grain
     leading questions that directly cue ≥3 of its 6 minors — "is recording on
     StopIteration/exception ever WRONG, e.g. double-counting when the library made zero
     requests?" = NIT-7; tests "pin … single shared clock across lanes" = MINOR-2;
     "client swap changing page_size behavior" cues MINOR-4's docstring half — sol got
     an uncued 4-point charter; (b) sol's prompt SUPPRESSED polish-tier findings by rule
     ("every finding must carry … a CONCRETE failure scenario … No vague 'could be a
     problem' findings") — docstring drift and cosmetic races cannot satisfy it; that
     clause likely bought the 0-false-positive result AND the minors deficit; (c) fable
     was ordered to rank on an explicit VITAL/MAJOR/MINOR/NIT ladder, sol's ladder was
     mentioned once in passing. RESIDUAL non-prompt gap: fable's MINOR-3, MINOR-5, and
     NIT-6 were uncued in fable's prompt too and sol matched none. The MAJORs axis is
     NOT confounded in sol's favor — the leading questions, had they mattered there,
     would cut the other way (fable's prompt also cued the concurrency attack surface).
     **Scoring correction:** "0/6 fable minors" overstated — sol's MAJOR-4 is the
     substantive core of fable's MINOR-4 elevated a tier, so ~1/6 matched, 5 unmatched
     of which 3 are prompt-confounded. **Design rule for the next firing: IDENTICAL
     prompt text across lanes (or the connector-style zero-shot floor for both); a
     known-answer probe's minors axis is uninterpretable without it.**
- record locator(s) + minimal verbatim excerpt(s):
  - Sol final verdict (from the transcript): "VERDICT: DO-NOT-SHIP … a forced interleaving
    reproduced a 0.000024s gap with a configured 0.300s interval."
  - Contamination point (call 42): `git -C /tmp/b20-prefix-review log --oneline --all
    --decorate -10`, immediately followed by `git show` of `af997dd`, `e291eb5`, `be329f4`,
    `d5f1369`.
  - Adjudicator first-hand re-run of sol's MAJOR-1 repro:
    `completion_gap=0.000027s interval=0.300s` (parent session, 2026-07-17).
