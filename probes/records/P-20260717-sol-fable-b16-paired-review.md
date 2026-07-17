# PROBE — 2026-07-17 fable × gpt-5.6-sol paired review, identical charter (B16)

- probe_id: P-20260717-sol-fable-b16-paired
- task class / ROUTES row: R1 review gates (code review) — the clean paired firing the
  amended P-20260717-sol-b20 record called for
- configs compared (model × effort × surface × harness): fable × high (`reviewer` pin)
  vs gpt-5.6-sol × high (`sol-code-reviewer` pin), both via Agent-tool typed spawns,
  **byte-identical prompt text** (verbatim in parent transcript): explicit
  VITAL/MAJOR/MINOR/NIT ladder for both, polish-tier declared in-scope for both, six
  symmetric attack surfaces, no finding-grain leading questions — the three confounds
  named in P-20260717-sol-b20 §deviations-5 all removed.
- harness/contract hash (if pinned): not hashed; both prompts byte-identical by
  construction (single string, two spawns in one tool block)
- blinded?: yes — legs launched concurrently in one block, blind to each other; tree =
  `git archive` export of commit `aa3a66a` to /tmp/b16-review, **no .git directory**
  (the B20 worktree-refs hole closed by construction; verified: "no .git — frozen
  export, refs unreachable", no goal/).
- frozen tree?: yes (archive export + REVIEW-DIFF.txt of main..aa3a66a)
- adjudicator: author (parent session authored the design and delegated the
  implementation) — deviation, same as prior local firings
- router: fable[1m] × high × Agent-tool typed spawns (operator-directed: "proceed with
  B16, run fable and sol on the same charter")
- **attestation:** both leg transcripts under
  `/private/tmp/claude-501/-Users-rookslog-Development-arxiv-mcp-server/d708c558-f626-4806-88d2-a198d216de3a/tasks/`
  (fable `a2928ef0f8d392c51.output`, sol `a93c24aa2f0705df8.output`); adjudicator
  re-verified both MAJORs first-hand (httpx wire probe: `C#` → `search_query='(C'`;
  parser probe: `solv-int/9501001v1` → `sol`) before accepting; fix round =
  arxiv-mcp-pro commit `5255883` on PR #25.
- verdict: **substance convergent, verdicts split on severity calibration** — sol
  DO-NOT-SHIP (2 MAJOR + 3 MINOR + 2 NIT), fable SHIP-WITH-FIXES (1 MAJOR + 4 MINOR +
  3 NIT). Same pattern W-001 records for fable-vs-opus pairings.

## Leg-by-leg

Convergent (independent, both with own probes): the top MAJOR (URL under-encoding —
`#` truncates at fragment dropping categories/dates/max_results, `&` splits params,
`+` decodes to spaces; both legs ran httpx.URL/Request probes); the untested
record-after contract (both: revert leaves suite green); total_results fallback
undisclosed; stale "space = AND" comment.

- unique catches (per leg):
  - **sol-unique: a second MAJOR** — `split("v")[0]` mangles old-style ids
    (`solv-int/9501001v1` → `sol`; also silent vN-strip vs deleted path's
    get_short_id()). Fable missed it entirely. Plus: category-token injection surface
    (`cs.AI&max_results=1000` passes validation), published-field serialization change
    (isoformat → raw Z).
  - **fable-unique:** undocumented error-text change for non-date queries; the vacuous
    revert-sentinel (test patches `config.get_arxiv_client` but deleted code bound the
    symbol into search's namespace — subtle namespace-binding analysis); dead fixture
    param; return_total Union-shape nit (REJECTED by adjudicator — deliberate design).
    Fable also independently re-verified the 144,990-vs-4,148 headline claim live.
- **Prompt-confound hypothesis RESOLVED (operator's, from P-20260717-sol-b20):**
  with polish-tier explicitly in scope and an explicit ladder, sol produced 5
  minor/nit-tier findings vs 0-ish under the B20 prompt — the B20 minors gap was
  substantially prompt-caused, as hypothesized. Under identical charters the two legs'
  finding-count and tier-spread are comparable (7 vs 8).
- Method note (consistent across both sol firings, n=2): sol ships executable
  reproductions per finding; fable mixes probe-backed and read-backed findings but
  found the subtler test-harness/namespace defects. Complementary, neither dominates.
- tokens / cost (if observable): fable leg 118,457 subagent tokens / 25 tool uses /
  ~17 min; sol leg token count NOT observable (gateway reports 0) / 30 tool uses /
  ~6.4 min wall.
- **tally:** feeds W-001; count after this record: attested-clean +0 / attested-
  deviated +1 (author-adjudicator remains; blinding + prompt-parity CLEAN this time —
  only the adjudicator deviation stands). sol-code-reviewer n=2 (both: real MAJORs,
  zero false positives; this one under a clean blind). Independence>tier direction
  further corroborated: a second same-tier lane caught a MAJOR the fable lane missed.
- deviations from clean protocol (named): author-adjudicator only. (Blinding: clean.
  Prompt parity: clean. Frozen tree: clean.)
- record locator(s) + minimal verbatim excerpt(s):
  - sol: "VERDICT: DO-NOT-SHIP … `paper_id.split(\"v\")[0]` is not a version-suffix
    parser: a feed ID such as `solv-int/9501001v1` becomes `sol`"
  - fable: "VERDICT: SHIP-WITH-FIXES … a query like `R&D management` yields a URL
    where httpx splits at `&` … (observed: `httpx.URL(...).params` →
    `[('search_query', '(R'), …]`)"
  - Adjudicator re-verifications in parent transcript (2026-07-17): wire-params probe
    + version-strip probe, then post-fix probe (`'C#' → wire search_query='(C#)'`).
