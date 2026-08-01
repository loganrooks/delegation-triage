# PROGRAMME.md charter draft — two-leg review + adjudication (2026-08-01)

Artifact under review: `PROGRAMME.md` v1 (untracked working-tree draft of 2026-07-31).
Legs: (1) Claude-lineage reviewer (opus×high, teammate) — pointer accuracy · thinness ·
adoption-record compliance against SEAS's own cite-vs-adopt text; (2) cross-vendor
**gpt-5.6-sol × xhigh** via `codex exec` (read-only sandbox; the sol-design-reviewer pin
does not resolve outside a gateway session — the teammate spawn failed on model resolution
and was force-stopped via TaskStop, itself a finding: a teammate with an unresolvable
model pin cannot process protocol shutdowns) — design soundness, failure modes,
alternatives, cross-vendor blind spots. Both verdicts: **CONCUR_WITH_CHANGES**.

## Adjudication (all findings ACCEPTED; charter v2 + same-pass propagation carry them)

- **No consumer / not a real boot surface** (Claude B3 ≈ sol HIGH-4, concordant): v2 adds
  P-C — CLAUDE.md boot-pointer section, new root `AGENTS.md` (cross-vendor entry), §0
  boot-and-refresh rule (re-read after compaction/resume, before lane-affecting changes;
  handoffs record the charter commit); adapter surfaces owed in LANES.md until rebuild.
- **Pace key classified but did not govern** (sol HIGH-1 ≈ Claude M16): v2 §0 defines the
  amendment transaction — ratification log as canonical locator, effectiveness rule,
  same-pass bounded to one commit with cross-repo dependents as owed LANES rows,
  `review_by: 2026-08-31` with the STATE expiry semantics, operator-absence fallback
  (`decision_due`, no channel reopening by default).
- **Pointers can re-mean silently** (sol HIGH-2 ≈ Claude M8/M9): v2 §2 types every pointer
  (binds-to / orients-to / status-map / volatile), adds the precedence rule (floors
  constrain, direction ranks, conflict halts to operator), and links every binds-to
  target.
- **Lane-board = unversioned cross-repo cache, already carrying drift** (sol HIGH-3 ≈
  Claude B2/M6): lane-board split out to `LANES.md` with owner/as-of/source per row and
  header state; the two v1 copies corrected at source — the stale "unowned `sol-*`" claim
  (superseded by ratified D-2; CLAUDE.md line fixed too) and the verbatim W-026 FP-0a
  clause (now a pointer).
- **Disconfirmer self-reporting/gameable** (sol MEDIUM ≈ Claude B3): v2 §3 P-D is
  behavioral (work-selection vs §1, LANES freshness; flips LANES header to `needs-review`
  + queues disposition; token citation clears nothing) and imports SEAS's citation guard
  into §0, marked as adopted text.
- **Claude-leg accuracy fixes, all applied:** LINEAGE.md adoption entry written this pass
  (B1); adopted decision corrected to SEAS ADR-0023 with ADR-0022/0024 as lineage (M4);
  §1 now carries all three ratified doctrine revisions incl. the ROUTES.md
  carrier→commentary demotion (M7); D-1's compatibility contract attributed to the
  decision-panel adjudication (M14); XV-1 pointed at its home (pilot §1/§6 + W-026
  mirror), applier noted (M13); basis sentence corrected — the gap is direction, not a
  sizing-hole (M5, M11 down-labeled to account-with-anchor); unverifiable "duplicated
  premise" warrant dropped (M10); proposals README hedge + stale Gemini-pilot row fixed
  (M12); betrayal paragraph marked adopted (M17); `probes/TEMPLATE.md` field actually
  added, making the ratified proposal's perfect-tense statement true (the leg's Q3
  finding: the propagation had never happened).
- **Sol's hybrid alternative adopted in posture:** PROGRAMME stays manually ratified;
  LANES.md is the fast surface and a named candidate for generation once the P1 rollup
  exists — generation covers state, never ratification.

Verbatim reports follow.

---

## Leg 1 — Claude-lineage (opus×high): pointer accuracy · thinness · adoption record

VERDICT: CONCUR_WITH_CHANGES (3 blockers, 8 majors, 5 minors)

BLOCKERS — (1) "Lineage recorded both ends" false as written: LINEAGE.md contains no
adoption entry; resolve same-commit, and re-word the SEAS half as owed-with-owner. (2)
Lane-board Housekeeping repeats the superseded "unowned `sol-*`" claim (ratified D-2
external overlay, MANIFEST.md:35-36; phrasing lifted from CLAUDE.md's stale line — the
exact drift the preamble promises to prevent, present in the first lane-board). (3) No
consumer: zero references to PROGRAMME.md from CLAUDE.md/README/SKILL/CONTRACT; SEAS
hard-core #7(ii) requires P-C + P-D and the draft kept only P-D — the disconfirmer is
unfalsifiable in practice.

MAJORS — (4) §3 adopts ADR-0022 but the charter pattern's decision is ADR-0023
(signal-layer INHERITANCE.md:129: the marker names the adopted id). (5) The basis's
"no surface at session-start × slow" is contradicted by CLAUDE.md itself; the defensible
claim is that no surface carried *direction*. (6) The FP-0a lane cell is a verbatim copy
of WARRANTS.md:812-814, a supersede-in-place clause — replace with a pointer. (7) §1
drops the ratified ROUTES.md carrier→commentary revision while §2 restates
pre-ratification doctrine. (8) §2's "no content here to amend" is false — item 6
characterizes XV-1/D-1/§6 in the draft's own words, two of them incorrectly. (9) Item 6
says "by pointer" and delivers unlinked labels. (10) [UNCERTAIN] the thinness warrant
cites a panel finding ("duplicated premise was the false claim") not present in the
adjudication record; leg reports are transcript-only. (11) "measured the gap" over-labels
a narrative; "four ratified reviews" unresolvable (five files dated 2026-07-31). (12) The
proposal map is characterized as authoritative-for-status but is stale (Gemini row "DRAFT
v3 awaiting D-FP-1/2/3" vs ratified 9385c17; overlay hedge "If ratified" under a RATIFIED
heading).

MINORS — (13) XV-1 attributed to its applier (pilot-closure adjudication) not its home
(pilot §1/§6, W-026 mirror). (14) D-1's compatibility contract belongs to the
decision-panel adjudication, not the portfolio review. (15) "four-status amendment
discipline" loose (statuses ≠ amendment rules). (16) No review_by/expiry, in a repo where
STATE rows expire by design. (17) §3's betrayal paragraph is near-verbatim SEAS text —
mark as adopted, don't present as locally authored.

Q-answers — Thinness: two genuine copies (2, 6); the P1 acceptance-criteria cell is the
watch-item (proposal's list, nothing brings it along on revision). Pointer accuracy:
every relative link resolves (check_wids exit 0, PROGRAMME.md in scope); failures are all
characterization (1, 2, 9, 12, 13, 14, 15); "no hook writes records" Corroborated at
second hand from the panel adjudication. TEMPLATE.md: the field is absent, so the draft's
"due" is honest — and the RATIFIED proposal states it in the perfect tense
("added … as a requested field"), a propagation that never happened: the proposal is the
document needing correction. Adoption record vs SEAS rule: substantively satisfied
(what/basis/disconfirmer/supersedable); defects — wrong adopted id (4), wrong basis
sentence (5), marker exists only as prose (no frontmatter `adopts:`, no decisions index;
honest options: add greppable marker, or state convention-only plainly).

Probed and found sound: link integrity (check_wids OK, 154 files; check_state OK); §1
blockquote matches the ratified decision ask; ratification status of the cited proposal;
XV-1 substance vs WARRANTS.md:770-772; §6 as the one binding constraint; CLAUDE.md
sizing-principle quote verbatim; the delegation.md drift precedent; supremacy clause
substance; vision-by-pointer divergence stated with a reason that checks out.

Not certified: direction merits (took ratification as given); commons alignment; cost;
pace-tier choice; lane completeness; the three passive-first leg reports (transcript-only);
SEAS beyond PROGRAMME/INHERITANCE/ADR filenames; the v2 ledger claims (second-hand).

---

## Leg 2 — cross-vendor gpt-5.6-sol × xhigh (codex exec, read-only) — verbatim

*(sole transformation: the report's absolute-path citation links are rewritten to plain code spans for check_wids compliance; text otherwise unedited)*
# Adversarial Design Review — `PROGRAMME.md`

## Verdict: **CONCUR_WITH_CHANGES**

A root charter is appropriate for slow direction and governance. The current draft, however, does not yet make its pace rules or session-boot contract operational. The **HIGH** findings should be resolved before ratification.

## Findings

### HIGH — The pace key classifies edits but does not govern them

> “a faster edit never overrides a slower section”  
> “operator ratification with dated record”

**Observed:** The draft assigns actors and pace labels, but does not define where a ratification record lives, what makes it effective, how “same-pass” is bounded, how concurrent edits are rejected, or what revision a session must have read. Unlike the SEAS source, it also has no `review_by`, ratification-record pointer, or explicit edit-history mechanism. Existing CI checks state expiry, evidence integrity, and builds—but no charter lifecycle or amendment invariant. Draft §0 (`PROGRAMME.md:18`), SEAS frontmatter (SEAS `PROGRAMME.md:1`), CI (`.github/workflows/ci.yml:15`)

**Failure mode:** Session A boots revision X; the operator ratifies new direction at X+1; A later updates a different lane row from its stale context. Git may merge cleanly, even though the resulting board operationalizes superseded direction. After the phase checkpoint, operator absence leaves no defined state: the old ranking might continue indefinitely or become implicitly non-binding.

**Required change:** Define an amendment transaction:

- canonical locator and minimum shape for dated operator statements;
- effective revision/commit;
- mandatory re-read or base-revision check before lane-affecting changes;
- precise meaning of “same pass,” including cross-repository updates;
- a `review_by` or event-triggered `decision_due` state;
- explicit fallback when the operator is unavailable at the checkpoint.

Mechanical checks need not adjudicate policy meaning, but they should reject missing lifecycle metadata and expired review state.

---

### HIGH — Moving pointers can amend the effective charter without touching it

> “same-pass pointer updates when a target supersedes; no content here to amend”

**Observed:** Section 2 is classified as slow, but several targets retain independent amendment regimes. For example, the north star permits architectural hypotheses to change “without a disposition.” The pointer can therefore remain byte-identical while the doctrine reached through it changes. Draft §0/§2 (`PROGRAMME.md:24`), north-star statuses (`docs/proposals/2026-07-24-evidence-commons-north-star.md:9`)

**Failure mode:** A target changes legitimately under its own faster rules, indirectly changing the charter’s operational meaning. The rule that a faster section cannot override a slower one does not resolve this because the change occurred outside `PROGRAMME.md`.

**Required change:** Type every normative pointer:

- `binds-to` or `adopts` — pin section, decision ID, status, and effective revision;
- `orients-to` — follows current text but cannot authorize work;
- `status-map` — informational;
- `volatile` — intentionally follows head.

Also add cross-document precedence: for example, direction ranks eligible work, while binding contracts and normative floors constrain it; an unresolved conflict halts authorization and requests operator disposition.

---

### HIGH — The lane-board is an unversioned cross-repository cache

> “Lane-board (fast; same-pass updates, no ceremony)”

**Observed:** Rows have no owner, `as_of`, source revision, freshness boundary, or authoritative status location. P1’s implementation home is explicitly the separate `delegation-runtime` repository, so its reality cannot be atomically updated with this board. Draft §4 (`PROGRAMME.md:87`), P1 ownership decision (`docs/proposals/2026-07-31-passive-first-reprioritization.md:19`)

**Failure mode:** Two sessions or repositories advance independently. Both can make locally correct updates from different snapshots, while `now`, `next`, and `gate` become a plausible but false composite. Detecting staleness after two sessions is late; downstream work may already have been selected from it.

**Required change:** Move volatile execution state into a separate checked or generated `LANES.md`/`STATUS.md`. Each row should carry:

- owner and authoritative repository/artifact;
- source revision or external status locator;
- `as_of` and re-check trigger;
- state such as `current`, `unchecked`, `blocked`, or `decision_due`.

Keep `PROGRAMME.md` as the slow charter and point to the fast surface.

---

### HIGH — It is not yet a cross-vendor boot surface, and boot has no refresh boundary

> “Doctrine pointers (what a session boots from, in order)”

**Observed:** No project-root `AGENTS.md` exists. `CLAUDE.md` still directs sessions first to the older initiative handoff; the Codex adapter starts with `ROUTES.md` and `STATE.md`; the Cowork package similarly omits `PROGRAMME.md`. Thus the charter is not reached by the checked native entry surfaces. Draft §2 (`PROGRAMME.md:53`), Claude entry (`CLAUDE.md:16`), Codex adapter (`adapters/codex/AGENTS-fragment.template:6`), Cowork adapter (`adapters/cowork-plugin/SKILL.template:22`)

The draft also defines only session-start reading. It does not require refresh after compaction, resume, handoff, lane selection, or before landing a lane-affecting change.

**Failure mode:** Claude-centric sessions may inherit the intended convention culturally, while Codex, Gemini, Cowork, resumed sessions, and compacted sessions operate from different snapshots. A handoff can faithfully preserve a lane state that became obsolete after the handoff was written.

**Required change:**

1. Add a one-line charter pointer to every native development entry surface.
2. Record `programme_revision`, direction-decision ID, and lane snapshot in durable handoffs.
3. Require comparison/re-read after resume or compaction, before selecting new work, and before integration.
4. Keep consumer routing adapters distinct if ordinary package consumers are not meant to load programme governance.

---

### MEDIUM — The adoption disconfirmer is self-reporting and citation-gameable

> “if two consecutive working sessions find the lane-board stale”  
> “or find §1 uncited by any live work”

**Observed:** “Working session,” “interval,” “live work,” and the place where a finding is recorded are undefined. If sessions stop reading the charter, no session necessarily “finds” it stale. Conversely, rote citations can keep the test green without direction affecting decisions. The SEAS source explicitly warns that citation presence does not substitute for conformance; that guard did not survive into this adoption. Draft §3 (`PROGRAMME.md:78`), SEAS supremacy guard (SEAS `PROGRAMME.md:48`)

**Required change:** Replace citation presence with a durable behavioral check:

- record charter/lane revision at boot and handoff;
- ask whether selected or deferred work actually matches the priority order;
- make two consecutive stale observations automatically mark the lane surface `Unchecked` or `needs-review`;
- queue operator disposition without allowing a token citation to clear the condition.

## Strongest alternative

The strongest alternative is a **generated root briefing surface** derived from authoritative proposal status, decision metadata, and lane sources. It would provide freshness stamps and detect divergence without creating another manually maintained authority.

Its weakness is decisive: programme intent and ratification cannot be safely inferred from metadata. A purely generated charter would turn a normative decision into a build artifact.

The best design is therefore a hybrid:

- **`PROGRAMME.md`:** manually ratified slow direction, pace protocol, adoption record, and typed pointers.
- **Generated/checked `LANES.md` or `STATUS.md`:** fast operational state with owners, revisions, and freshness.
- **Vendor-native entry files:** thin pointers to those two surfaces.

Extending `STATE.md` is weaker because it is an every-spawn volatile routing surface and is deliberately omitted from some packaged deployments. Expanding the proposals README is also weaker: it indexes design authority but does not provide operational state or native boot integration.

## Cross-vendor blind spots

1. `PROGRAMME.md` is a convention, not a generally auto-discovered instruction filename.
2. “Same pass” assumes a single repo/session transaction; cross-vendor work commonly spans independent processes, worktrees, and repositories.
3. Citation-based compliance is especially easy for agents to optimize cosmetically.
4. Claude-lineage concepts such as session boot and distillation have been imported without their local invocation or recording mechanism.

## Verification and boundary

- Read the full draft, SEAS comparator, reprioritization, north star, proposal map, state, roadmap, README, Claude guidance, adapters, and CI/check implementations.
- `python3 check_state.py`: **OK** — 9 dated entries, 3 exempt.
- `python3 check_wids.py`: **OK** — 154 Markdown files, 26/26 W-records cited.
- `git diff --check`: exit 0.
- Those checks corroborate link/state integrity only; they do not test charter governance.
- Read-only review: no files were changed; final worktree status matched the initial status.
