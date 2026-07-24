# agents/ MANIFEST — canonical definitions + recorded deployments

**Canonicality (ADR-0022 A5):** the definitions in THIS directory are canonical; every deployed
copy is a recorded deployment stamped here with a content hash. Drift = diffable, never
discoverable-by-accident. Roster changes register at session START — a deploy without a restart
is a silent no-op; stamp the deploy AND note the restart.

**Deploy step (until a sync script exists, documented-manual):** copy changed definitions to the
target, re-hash (`shasum -a 256 agents/*.md`), update the deployments table, restart the session.
`--check` equivalent: re-hash the target and diff against this table.

## Canonical candidates (0.1.0-stage1-draft, hashed 2026-07-10)

| definition | model × effort | sha256 | provenance |
|---|---|---|---|
| reviewer.md | **opus × high** (operator re-route 2026-07-24: "opus 5 is now the model… you can get away with opus high for reviews"; fable retained for orchestration/decomposition/brainstorming classes. Supersedes the ADR-0022 D3 scheduled flip — executed early on a quality ruling, not the availability cliff. Registers at next session start) | 2369d9d3e53dc16c4aaadca63468c31a067bf7fbe763fd920360d528c7727c46 | flip applied 2026-07-24 (fable leg, campaign session, operator in-session ruling); prior: fable × high per ADR-0022 A3, sha a9b8d343… |
| explorer.md | **sonnet × high**, read-only | 535c022b380e95623bb05d7208d35bb5b6460efd90cbf0d0f2d02adfe4344cc7 | carries the 2026-07-10 operator correction (facts + follow-ups, never judgments) **+ the 2026-07-17 sonnet-first ruling [W-023]**. **Canonicality repair 2026-07-24 (review D-1):** the 07-17 ruling reached ROUTES R7, W-023, and the DEPLOYED pin but never this file, which stayed `model: opus` and was stamped `abf2e469…` — so canonical contradicted the route row citing it, and `install.py claude-code` would have silently reverted the ruling in the live roster. Repaired by promoting the deployed frontmatter to canonical (bodies were byte-identical; only `description` + `model:` differed). Root cause: commit `2e3b059` changed the route + warrant without the coupled pin edit — the failure mode CLAUDE.md's profile↔pin rule exists to prevent |
| explorer-light.md | sonnet × medium, read-only | 4389ba1abcc7f53113da1f6e46d65b990531fdd973fd2532e95e412e2f580413 | minted 2026-07-05 as the sonnet-medium probe instrument (W-006) |
| implementer.md | opus × **medium** (re-pointed 2026-07-24, operator ruling; Provisional — effort-frontier probe P-20260724 open, now medium-incumbent vs xhigh-challenger) | ae60398f86f73461a9fe8660a914ceb98aac87b75cb72047eac62e0c85d05a52 | W-004, W-024; ruling record P-20260724-r4-r5-reroute-opus5-effort |
| implementer-light.md | opus × **low** (re-pointed 2026-07-24, same ruling; Provisional) | 164a1da571d8f072e0d397a68f2d1dea19f2aa96f58f4f08e9a20645e5938b1a | W-005, W-024; sonnet demotion probe re-scoped (sonnet high vs opus low, count 1/3) |
| orchestrator.md | fable × high | 39bcd0c45edb246dd75cd9baa32614ff4aaeceaed300bc654d6c7a55161aff14 | minted 2026-07-10 after the effort-inheritance firing; post-window pin adjudication OWED (STATE.md) |
| advisor.md | fable × xhigh, tool-less | 6f1811a5b7f46a36444d66db7da2d0e12e15a216734f6ce8a94ff20485598250 | adopted 2026-07-10 from the Cowork `delegation-roster` fork 0.2.2 (its advisor.md sha `3d3eae34…76e766`), operator-claimed design; route R15 (CANDIDATE, W-022). Basis: subagent advisor = plaintext on any model (tool caveats out of scope); xhigh reason: single bounded turn, judgment-dense checkpoint. Disconfirmer: R15's owed local probe (incl. high-vs-xhigh pair) grading advice quality/actionability — parity at high demotes the pin. Window management is project-side (graceful degradation, operator 2026-07-10): no dates in the definition |

Excluded from the roster migration: `knowledge-store.md` (a reference specification that was
sitting in the deployment directory, not an agent definition — left where it lives; flagged for
the operator to relocate).

## Recorded deployments

| target | stamped | status |
|---|---|---|
| `~/.claude/` (agents + skill home) | **2026-07-24 @ `65773b1` (release-class: clean tree)** | 66/66 files `ok` (`install.py claude-code --check`: behind 0 · drift? 0 · diverged 0 · missing 0 · **extra 3** = the unowned `sol-*` trio, D-2 open). Carries the same-day R1 (reviewer→opus high) and R4/R5 (implementer→opus **medium**, implementer-light→opus **low**) re-routes; roster hashes = canonical table above. **Restart required and NOT yet performed at stamp time** — the stamping session continues on the old registered pins and delivers new-route spawns per-call via Workflow `agent()` (CONTRACT §3). Supersedes the same-day preview deploy below. |
| `~/.claude/agents/` (superseded by the `65773b1` release deploy above) | **2026-07-24 @ `f467634` + UNCOMMITTED worktree (review D-2 repair deploy)** | 64/64 files current (`ok 64 · behind 0 · diverged 0 · missing 0`); roster hashes = the canonical table above. **Restart required and NOT yet performed at stamp time** — roster registers at session START. ⚠️ **Dirty-source deploy:** the source tree carried uncommitted changes, so this is a preview-class deployment, not a release; its bytes are not reconstructable from `f467634` alone. **What it repaired:** the deployed `ROUTES.md` and `STATE.md` were `DIVERGED` — bytes that existed in **no commit in repository history** (hand-edited: an R1 phrasing never committed, the `mediumw` typo, a pre-ruling R7, and a `STATE.md` stripped of its format-contract comment and `<!--vf:-->` sync tags). Adjudicated before overwrite: both were strictly **lossier** than canonical, carrying nothing canonical lacked. Pre-overwrite copies preserved outside the repo. |
| `~/.claude/agents/` — **UNOWNED DEPLOYED DEFINITIONS (review D-3, open)** | discovered 2026-07-24 | `sol-advisor.md`, `sol-code-reviewer.md`, `sol-design-reviewer.md` are live in the deployment, **never tracked in this repo**, absent from the canonical table above — while `ROUTES.md` **R1 routes to two of them** and three `P-20260717-sol-*` probe records turn on their behaviour. `install.py --check` was structurally blind to them until 2026-07-24 (it inspects only files it would itself write); it now reports them as `EXTRA`. **Operator decision owed:** adopt into the canonical roster, or keep external and drop the R1 citation. Adoption is not automatic — their `model: sol` pins resolve only through a private CLIProxyAPI gateway (`claudex`), so shipping them from a public MIT package is a packaging decision, not a filing one. |
| `~/.claude/agents/` (superseded) | 2026-07-10 @ `0fa9ee8` (install.py claude-code — first scripted deploy) | roster: 7 definitions incl. `advisor` (new; hashes = canonical table above); skill home `~/.claude/skills/delegation-triage/` current @ `0fa9ee8` (31 files, `install.py claude-code --check` clean); **restart pending at stamp time** — advisor registers at next session START. History: Stage-2 deploy from `14c3311` same day (routing-table archived, guard re-pointed to STATE.md); ROUTES+WARRANTS interim re-sync @ `cf95ea1` |
| SEAS `harness/agents/` | 2026-07-10 | superseded records (marked in-file per ADR-0010 convention); TRIAGE.md re-scoped to consumer-side pointer + overlay |
| Cowork `delegation-roster` plugin (installed) | — | **UNRECONCILED FORK, discovered 2026-07-10:** a GPT-5.6-Pro repackaging of the PRE-package routing table + probe corpus (its routing-evidence.md cites the same bridgewright/prix-guesser/signal-layer records) — 7 agents (ours + an `advisor` @ fable/**xhigh**) + a skill with a routes/evidence split but **NO STATE layer** (volatile facts deliberately omitted → no expiry mechanism; its fable pins will silently outlive the 07-12 window — the C-012 failure mode in a third home). Stage-2 reconciliation owed: regenerate from canonical or diff-and-stamp; until then it is a live drifting copy in exactly the environment (Cowork) the proposal diagnosed as blind. |

## Recorded deployments

| date | artifact | sha256 | source commit | notes |
|---|---|---|---|---|
| 2026-07-24 | dist/delegation-roster-0.3.0.plugin (Cowork) | e21a552c19828b4f7b8d2c66414668e31815456da4c1c06f383f2c866d6d5798 | 29c4461 | rebuilt post R1-reroute + fable-permanent; carries the 15-row ROUTES incl. R14/R15; stale opus-4-8 references gone (verified by unpack-grep). Delivered to operator for Cowork-UI install — INSTALL PENDING, sessions pick it up after install |
