# Portfolio decomposition and recommendation attack — Fable review

- **Date:** 2026-07-24
- **Reviewer:** Claude Code (Fable 5), architect/decomposer session, per the
  [2026-07-24 Fable decomposition packet](../handoffs/2026-07-24-fable-decomposition-packet.md)
- **Unit of review:** the portfolio (first review to take it as the unit, per review F-1)
- **Verdict on the portfolio split:** **REVISE** — accept the split's direction, correct its
  count: **two products, not three artifacts** (§2, R-A)
- **Authority:** review, decomposition, and planning only. Nothing here was implemented,
  installed, deployed, activated, committed, pushed, cleaned up, or deleted. No route row moved.
  No paid probe ran. This session spawned **zero subagents** (§0.2).
- **Packet compliance:** packet §§1–6 and 8–9 were read. **Packet §7 and §10 were not read** —
  section boundaries were located by header grep first, and reads were bounded to lines 1–190
  and 225–260.

---

## 0. Method

### 0.1 Verification performed

Every claim below marked *observed* reproduces from these commands, run 2026-07-24 from the
repository root on the current dirty worktree.

| # | Command | Result |
|---|---|---|
| V1 | `python3 check_state.py` | exit 0 — "checked 9 dated entries, 2 exempt … OK" (packet §3.1's green-gate claim reproduces) |
| V2 | `python3 check_wids.py` | exit 0 — "95 md files · 24 W-records defined · 24 cited: OK" |
| V3 | `python3 install.py claude-code --check` | exit 0 — "checked 64 files: ok 64 · behind 0 · drift? 0 · diverged 0 · missing 0 · **extra 3**" (the three `sol-*` definitions) |
| V4 | `PYTHONPATH=adapters/codex/delegate-to-claude/scripts:adapters/codex/scripts python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests` | "Ran 223 tests … OK" |
| V5 | count `kind` over `~/.claude/observability/ledger/spawns-*.jsonl` | `subagent-stop` 3,219 · `subagent-start` 2,016 · `spawn-req` 670 · `spawn-res` 649 · `denial` 9 |
| V6 | structured-task count over the same ledger | **15 of 670** `spawn-req` records carry a `task` dict; its only observed subkeys are `kind/project/gate/tier/lens/vendor` — **the schema has no field that could hold a task class, route ID, or W-ID** |
| V7 | regex over full `spawn-req` payloads | `W-0\d\d`: **0** matches. Loose route-row pattern (`\bR\d+\b`): ~10 matches. The packet's "5 cite a route row or W-ID" is concordant in magnitude but **not reproducible as an exact count** — no method was recorded (§6, finding SG-2) |
| V8 | per-month, per-kind counts | the start-vs-req gap exists in **both** months (June 1,346 vs 385; July 670 vs 285) — not a hook-installed-later artifact |
| V9 | per-session join of req and start legs | 61 sessions; 55 have both legs; **within those 55, 1,872 starts vs 670 reqs** — the gap is intra-session. Only 144 of 2,016 starts sit in request-less sessions |
| V10 | `spawn-req` records with non-empty `err` | 1 of 670 — hook crashes do not explain the gap |

### 0.2 Why this session spawned no subagents

Stated per [`CONTRACT.md`](../../CONTRACT.md) §1 and §4 [per: delegation]: the assignment is
portfolio-level judgment, and F-1's finding is precisely that contract-pinned single-document
spawns *cannot see the portfolio*. Delegating lanes of this review would re-create the failure it
exists to correct. No leg needed a new information channel (all sources are local files read
firsthand), parallelism (reading order was dependency-ordered), or isolation. The delegation test
fails on all four prongs; the work stayed in-session. Fit line for the session itself: the
routing of this spawn is packet §7 material and was deliberately not read.

Claim labels follow [`EPISTEMICS.md`](../../EPISTEMICS.md); **observed** / **inferred** /
**recommended** are separated inline throughout.

---

## 1. Verdict on the portfolio split

**REVISE.** The prior review's direction is right and its falsifier survives attack — but the
three-artifact framing overstates one leg, and correcting it changes two decomposition items.

**What survives (observed + inferred):** the doctrine package (811 lines of Markdown, consumed by
reading) and the delegate-to-claude runtime (8,916 uncommitted Python lines driving paid external
processes, 0 completed worker turns) have different consumers, failure modes, verification
regimes, and evidence burdens — review F-3's table, checked against
[`CONTRACT.md`](../../CONTRACT.md) §3 and the untracked `adapters/codex/delegate-to-claude/`
tree. I attempted the F-3/R-A falsifier (produce a Claude Code workflow needing the packet
schema, policy compiler, or reconciliation engine) and could not: inside Claude Code the harness
owns process lifecycle and permissions (roster pins, Workflow `agent()`, hooks, settings), so
every candidate workflow reduced to reading surfaces plus native controls. **Falsifier not
produced; the split stands.**

**What does not survive (inferred):** "three artifacts with **independent release cadence**"
(review §6). The Claude Code integration is `install.py claude-code` plus `adapters/claude-code/`
plus the roster — it lives in this repo, ships with the doctrine release, and has no release
cadence of its own ("~0 new code" by the review's own diagram). Calling it a third artifact
invites a third repo, a third manifest, and a third drift surface for a thing that is an *adapter
directory*. The correct cut is:

```
Product 1 — delegation-triage (this repo):
  doctrine · demand ontology · warrants · state · probes
  + thin per-harness adapters (claude-code, cowork, codex CONSUMER fragment) behind install.py
Product 2 — delegate-to-claude runtime (charter: the cross-runtime proposal):
  packets · policy compiler · sessions · reconciliation · resource governance
  consumes Product 1 as versioned data; home = operator decision D-3 (§4)
```

**Consequence the count-correction buys:** D-6 (the tracked `ci.yml` step that requires the
untracked `adapters/codex/**` tree — [`CLAUDE.md`](../../CLAUDE.md) "Land them in one commit or
neither") stops being a commit-sequencing puzzle and becomes a *fork of the split decision*: if
the runtime exits the repo, the answer is **neither** — the adapter-test step leaves `ci.yml`
with the tree. See decision D-3 and item C-2.

---

## 2. Disposition of R-A through R-F

Each attacked via its stated falsifier first, per the packet's instruction.

### R-A — Split the portfolio three ways → **REVISE (two products)**
Falsifier ("produce one Claude Code workflow that needs the packet schema, policy compiler, or
reconciliation") attacked and **not produced** (§1). The load-bearing assumption holds. What
fails is not the assumption but the count: the Claude Code integration is not an independent
release artifact. Disposition: accept the doctrine/runtime split; fold the Claude Code
integration back into the doctrine package's adapters, where it already lives.

### R-B — Doctrine owns the capture spec; ship one writer; no plugin interface → **ACCEPT**
The falsifier is the union test ("write the union across signal-layer hooks + Claude Code OTel +
Codex OTel; large or churny ⇒ shared implementation wins"). **Two of three legs run in this
session, firsthand:**

- *signal-layer leg (observed, V5/V6):* the `spawn-req` payload is 16 keys (`cwd, description,
  effort_env_spawner, effort_spawner, model_requested, parent_agent_id, permission_mode,
  project_key, prompt_head, prompt_path, prompt_sha256, run_in_background, subagent_type, task,
  tool_name, tool_use_id`) plus a 7-key envelope.
- *Claude Code OTel leg (attested, [P-20260724](../../probes/records/P-20260724-otel-routing-observability-substrate.md)):*
  `api_request` carries `model, effort, query_source, cost, tokens, session.id, prompt.id`;
  `subagent_completed` carries `agent_type, agent.source, model, final_model, model_swapped,
  total_tokens, duration_ms`.
- *Codex OTel leg:* **Unchecked.** No `~/.codex/config.toml` exists on this machine (observed);
  the survey's `[otel]` claim is Reported via DeepWiki. Cheapest completion: item B-5.

**Result of the run legs:** the routing-relevant union is small — the observed side is already
oversupplied by the platform, and the missing intent side is ~14 fields (§3, Q3). Nothing churny
appeared. R-B's assumption survives the two-thirds of its own test that could be run today.
**One design constraint the test surfaced (observed, V9, new):** a request-side *tool hook*
covers only ~1/3 of subagent starts even inside sessions where it runs (1,872 starts vs 670 reqs
intra-session; stops even exceed starts, 3,219 vs 2,016). Inference: the hook's spawn surface
(the Task tool) is a subset of the surfaces that start subagents (Workflow `agent()`, skills,
resumes). **The one writer must therefore sit with the driver's decision (the fit-line emission
point), not on a single tool hook** — otherwise the intent log inherits the same blindness the
ledger just demonstrated. Labeled: coverage numbers observed; the surface-subset mechanism is
inferred, not confirmed.

### R-C — Defer packaging, decide schema now → **ACCEPT**
Falsifier ("show packaging is the expensive one") not produced: packaging here is demonstrated
cheap — `install.py` already targets three platforms deterministically (observed: V3;
[`README.md`](../../README.md) Quickstart), and repackaging moves no data. The schema is the
asymmetric-cost object: today there are zero external writers (observed: the ledger's schema has
no route field to migrate, V6), so schema decisions are at their cheapest point they will ever
be. Scope note: "schema" means the ~14-field intent record and the coupled-fields sidecar (§3
Q3/Q5) — **not** the consolidated proposal §6.2's full structured policy source, and per the
[survey](../research/2026-07-24-routing-infrastructure-survey.md) §3, never warrants or probe
records ("Those are authored arguments").

### R-D — Route rows become demand + selector + binding → **ACCEPT, with one refinement**
Falsifier ("a harness where demand doesn't transfer") attacked and not produced: across Claude
Code, Codex, Cowork, and the Antigravity slice, the task ontology (verdict-on-artifact, sweep,
mechanical edit, synthesis) transfers; only bindings and surfaces change — a single-model harness
binds demand trivially but the demand still names what the work needs.
**Refinement (inferred from W-023 + survey §6):** not every left-column entry is a measured
demand. R7's sonnet-first default is an **operator policy conditioned on harness discipline** —
[`WARRANTS.md`](../../WARRANTS.md) W-023: *"policy, not a measured capability claim"*; the survey:
*"the person-level variable is … how much discipline the operator's harness carries."* The
demand→binding representation must carry a third element: **the harness-contract assumption under
which the binding holds** (e.g. "sonnet suffices *given* the pin's claims-discipline contract").
Projecting a binding without its harness assumption is exactly how another operator inherits a
route that is wrong for them.

### R-E — The research wave doubles as observability dogfood → **REVISE (falsifier produced)**
The falsifier asks for "a cheaper validation path." **It exists:** natural delegation traffic.
This environment produced 670 recorded spawn requests in ~6 weeks with zero bespoke effort
(observed, V5/V8); the package's own probe discipline already prefers natural triggers — W-023:
*"run the paired probe at the next naturally-arising deep-read fan-out (no bespoke spend)"*; both
2026-07-24 probes are registered "pending trigger = next naturally-arising task"
([`probes/INDEX.md`](../../probes/INDEX.md)). Deploy the intent record and the next work-week of
ordinary delegation validates capture at marginal cost zero. What natural traffic does *not*
supply is deliberate tier variance — but tier variance serves route comparison, not capture
validation, and route comparison is governed by the registered paired probes, not by a wave.
Designing a research fan-out *so that telemetry has variance* spends research budget to feed the
measurement apparatus — the tail wagging the dog. Dogfooding an independently-justified wave
remains right *when one is justified*; none currently is (§5).

### R-F — Fix the 8 defects before new architecture → **ACCEPT as executed; falsifier fired on 1 of 8**
Overtaken by events: all eight are closed or dispositioned (packet §3.1; independently
reproduced — V1–V4, plus [`agents/MANIFEST.md`](../../agents/MANIFEST.md)'s D-1/D-2 repair
stamps, read firsthand). The residue is instructive: of the two open items, **D-6's resolution
depends on the architecture decision** (§1) — the falsifier ("show a defect whose fix depends on
it") fires on exactly one of eight. The assumption was 7/8 true and the sequencing was still
right, because the seven independent fixes were the urgent ones.

---

## 3. Answers to the packet §4 questions

**Q1 — Is the portfolio split right?** Revise to two products (§1). Alternatives considered:
the review's three-artifact cut (rejected: manufactures a release surface for an adapter
directory), ratify-consolidated-as-one-product (rejected: F-3's conflation is the source of the
surface area — I checked §5.1's ownership list against what the doctrine package actually needs
and eight of its nine bullets serve the runtime), park-everything (rejected: the runtime charter
costs one document and preserves genuinely strong invariants — the cross-runtime proposal's
planned/requested/observed provenance discipline).

**Q2 — What is the product: the method or the routing answers?** **The method — and the answers
ship as the worked example, never as defaults.** Review F-6(a) adopted, sharpened by the survey's
two findings I checked against the reference-design table: no surveyed system has a warrant
layer, and Arch-Router independently converged on named-route-plus-description — so the
defensible differentiator is the evidence discipline, not the bindings. This decides Q3's sizing:
a release is the versioned method + schemas + one operator's fully-conditioned evidence base
(README already says this: *"a working instrument, published with its lab notebook"*). It is
**not** a priors distribution service, so no apparatus for aggregating community bindings is
needed in this phase — which is also what W-018's transfer-regime argument implies *a fortiori*
for other people's n=1–3.

**Q3 — Observability coupling.** **Own the spec; ship one driver-side writer; build no plugin
interface; do not depend on signal-layer.** Grounds: the R-B union test (§2). Signal-layer is
private (observed: [`WARRANTS.md`](../../WARRANTS.md) KNOWN-REPOS marks it *"no remote —
local-only, flagged"*), so a dependency blocks the public path and would force `/signal` on
strangers; instead signal-layer's obs-hooks become *one local instance* of the published capture
spec. The consolidated proposal's §1.4 "Signal Layer as a versioned dependency" is thereby scoped
to this operator's deployment, not the product. The intent record (recommended, ~14 fields):

```
{v, ts, session_id, spawn_ordinal, task_class, route_id, rung,
 warrant_ids[], requested_model, requested_effort, surface,
 router_model, routes_sha256, why}          # bounded prose; no prompt text (privacy boundary kept)
```

Join to the platform stream on `(session.id, subagent_completed.agent_type, ordinal)` — the
ordinal answers P-20260724's named concurrent-attribution limit. Free detectors ride along:
`model_swapped` (provenance-misreport), per-`query_source` `effort` (effort-inheritance).

**Q4 — Route representation; what survives projection to Codex?** Demand + binding +
harness-assumption (§2 R-D). What survives projection: the R1–R8 left column restated as demands;
the class discriminator (R1-vs-R7); the cross-class constraints that are demand-side ("judgment
floors at sonnet", "diverse lanes over higher tier", "fixed-step transformations prefer
scripts"); the delegation test itself; and the *pattern* of constraint rows (refusal handling,
fallback purity) though their Claude-family contents do not. What does not survive: bindings,
effort-dial specifics, fable scarcity machinery, and the non-task rows — R9 is a pricing posture,
R11 a parked experiment, R12/R14/R15 unadjudicated candidates, R14/R15 Claude-Code plumbing
(observed: [`ROUTES.md`](../../ROUTES.md) rows as listed). These leave the task-class table for
typed registers *before* projection (item B-1).

**Q5 — Situational routes: the mechanism.** The operator's policy is conditional; a frontmatter
pin is a constant. Mechanism (recommended — **no value is picked here**, per packet §8):

1. **A route row becomes a rung table:** ordered rungs, each `condition → (model, effort) →
   delivery surface`. Example shape for R7 (values illustrative only): *default rung* →
   cheaper-tier pin; *named-discriminator rung* ("thinking-involved", "judgment-discrimination
   reason") → higher pin or per-call override; *evidence rung* ("cheap-tier output failed
   review") → escalation. The conditions already exist in R7's prose; the mechanism types them.
2. **Delivery:** rungs differing only in *model* can share one pin plus the Agent tool's
   per-call `model` override (observed: the deployed `explorer` description documents exactly
   this). Rungs differing in *effort* need distinct pins or a Workflow `agent()` call — effort
   has no per-call surface (observed: [`STATE.md`](../../STATE.md) `platform-no-per-call-effort`).
   So **the pin set is the image of the rung tables** — pins stop being where policy lives and
   become compiled artifacts of the routes surface.
3. **Coupling made deterministic:** the sidecar (Q3) carries the rung tables; CI checks pin
   frontmatter == rung-table image. D-1's failure class (route row and pin diverging for a week)
   becomes a build failure. Per the demonstrated base rate of self-accusing integrity checks
   (packet §3.1's `DRIFT?` lesson), the check needs an explicit undecidable state for
   mid-edit/dirty conditions — report, don't accuse.
4. **The fit line names the rung** it took and the condition that selected it; the existing
   guard hook (which already parses STATE's `Active:` line) can verify the rung exists and its
   window is unexpired — zero tokens.

The `explorer` value question then reduces to: which rungs does R7 have, and which pin carries
each — an operator sign-off on a one-page rung table (decision D-4), with W-023's paired probe
(still 0/n) as the evidence path for the default rung.

**Q6 — Sequencing and wave design.** See §4 (ordered items) and §5 (wave: none — revised from
the packet's 5–6-lane suggestion, per R-E).

**Q7 — Why did a deployed instrument go unused for 670 delegations?** Two answers, one narrow
and one structural.
*Narrow (observed, V6):* the 2.2% does not measure non-use. The capture schema **has no field
that can hold a route citation** — the 15 tagged records tag `kind/project/gate/tier/lens/vendor`,
and `prompt_head` is truncated while the fit line lives in the visible plan. The ledger measures
the absence of an intent *channel*, not the absence of instrument *use*. Whether drivers actually
consulted ROUTES per spawn is **unmeasured** — and honesty requires saying the number cannot
currently distinguish a fully-consulted instrument from decoration.
*Structural (inferred across §3.1's defect set):* every one of the eight defects, and this gap,
shares one shape — **a stated convention with no deterministic enforcement point**: the
profile↔pin coupling rule existed and was violated silently (D-1); the expiry mechanism fired and
nothing forced the disposition (D-7); the fit-line discipline existed and nothing captured it.
What makes the next instrument different is not another rule but an enforcement point per rule:
the intent writer (capture), the sidecar CI check (coupling), the guard-hook rung check
(citation), CI `check_state` (already landed). Item B-4 makes this audit systematic.

---

## 4. Operator decisions surfaced (five-point form)

Per [per: decision-presentation]. A single "yes" to each authorizes its full cascade
[per: propagation]; the cascades are itemized in §5's table.

**D-1 · Ratify the two-product split.**
*What:* adopt §1's cut — doctrine package (with in-repo adapters) and a separately-chartered
delegate-to-claude runtime; the consolidated proposal is revised to the doctrine scope and the
cross-runtime proposal becomes the runtime charter. Yours because it sets product boundaries and
supersession, which review authority cannot. *Options:* (a) two products (recommended); (b) the
review's three artifacts; (c) ratify consolidated as one product; (d) park everything.
*Recommendation:* (a), for §1's reasons. *Load-bearing assumption:* no Claude Code workflow needs
the runtime's machinery — attacked, not falsified (§2 R-A). *Flip:* someone produces such a
workflow → fold the runtime back in as (c).

**D-2 · `sol-*` adopt-or-drop** (review D-3 residue; blocks B-1's rewrite of R1's candidate row).
*What:* the three deployed, unowned `sol-*` reviewer definitions that R1 cites are adopted into
`agents/` (bringing a private-gateway dependency into a public MIT package) or kept external with
R1's candidate text rewritten to name them as external instruments. *Options:* adopt · keep
external + rewrite R1 (recommended) · drop the candidate row. *Recommendation:* keep external —
the gateway (`claudex`) cannot ship publicly, and the probe records already carry the evidence;
R1 can cite the probes without the package owning the pins. *Assumption:* citation-without-
ownership is legible to consumers. *Flip:* if the cross-vendor lens is promoted from CANDIDATE to
default on accumulating evidence (n=3 streak already: [`probes/INDEX.md`](../../probes/INDEX.md)
B23 row), ownership pressure returns and adoption should be re-opened.

**D-3 · Runtime home** (decides D-6's resolution — item C-2).
*What:* the untracked `adapters/codex/delegate-to-claude` + `delegate-to-antigravity` + shared
`scripts/tests` trees move to their own repository, or land here in one commit with `ci.yml`.
*Options:* own repo (recommended) · stay in-repo as a marked separate package. *Recommendation:*
own repo — public-MIT vs operator-specific runtime posture, independent verification regime, and
D-6 dissolves ("neither": the adapter-test CI step exits with the tree). *Assumption:* the
runtime's evidence loop doesn't need this repo's CI. *Flip:* if the operator prefers one
maintenance surface (the repo-operating-model memory favors installers/CI over manual steps but
is silent on repo count), in-repo-with-own-CI is acceptable; then D-6 resolves "one commit."

**D-4 · R7 rung table sign-off** (the mechanism of Q5 applied to the explorer question — value
assignment deliberately not made here, per packet §8). *What:* approve rungs + pin mapping for
R7. *Options:* the Q5 mechanism with values assigned by you · keep the static pin and accept the
mechanism's absence. *Recommendation:* assign values via the rung table, and let W-023's owed
paired probe (0/n) test the default rung at the next natural deep-read fan-out. *Assumption:* the
conditional policy you stated ("sonnet medium budget default, higher when thinking is involved")
is stable enough to type. *Flip:* if per-spawn conditions prove too noisy to name, the rung table
degrades gracefully back to a default + stated-reason escalation — today's R7 prose.

---

## 5. Decomposition of the next phase

Owner-classes: **operator** (decision) · **root** (this-session-class judgment work, in-repo) ·
**delegated** (roster-pinned spawn; fit line per CONTRACT §4) · **script** (deterministic).
No item below requires a paid probe; C-3 is explicitly parked.

| # | Item | Owner | Surface | Depends on | Exit criterion |
|---|---|---|---|---|---|
| A-1 | Disposition D-1…D-4 (this document §4) | operator | this review | — | dispositions recorded; proposals/README updated in the same pass |
| B-1 | Route-table cleanup: move R9 (pricing posture), R11 (parked), R12/R14/R15 (candidates) into typed registers; ROUTES keeps task classes + constraints only | root | ROUTES.md + new registers | A-1(D-2 for R1 text) | `ROUTES.md` contains only task-class rows; `check_wids` green; every moved row keeps its warrant + flip condition |
| B-2 | Demand+binding+assumption rewrite of R1–R8; one-page Codex projection | root | ROUTES.md + `projections/codex.md` | B-1 | a Codex driver can resolve demand→binding for its harness with zero Claude-Code residue; W-023-style policy bindings carry their harness assumption |
| B-3 | Intent record + sidecar: ~14-field schema, one **driver-side** writer, sidecar of coupled fields, CI check pins==rung-image with an explicit undecidable state | root (schema) + script (checker) | new sidecar + hook/CI | B-1, B-2 | one ordinary spawn produces an intent record joinable to `subagent_completed` on (session, agent_type, ordinal); a D-1-class divergence fails CI; dirty-state reports without accusing |
| B-4 | Enforcement-point audit: every stated rule → its deterministic check, or an explicit "convention-only" label | root | one table in docs/ | — | table exists; top 3 unenforced rules either get checks or a recorded acceptance |
| B-5 | Codex OTel leg of the union test (read-only; completes R-B's falsifier) | delegated (explorer-class, read-only) or root | research note | — | field list observed from a live Codex config or primary docs, cited; union doc updated; "large/churny" verdict recorded either way |
| B-6 | Rung-table mechanism doc + R7 instance for D-4 | root | design doc + ROUTES R7 | B-3 design, D-4 | operator has signed a rung table; pins edited only after sign-off, both in one commit |
| C-1 | Runtime charter: re-scope the cross-runtime proposal as Product 2's founding document; mark consolidated §§5.1/6/8/14 as transferred | root | proposals/ | A-1(D-1) | charter names its own evidence burden and verification regime; both ends of each supersede/amend link updated [per: propagation] |
| C-2 | D-6 resolution per D-3: runtime tree exits (strip ci.yml adapter step) **or** tree+CI land in one commit | script/root | git + ci.yml | A-1(D-3) | `git ls-files` consistent with every path `ci.yml` references; `main` green |
| C-3 | Version-3 runtime probe (composable-policy §17.3) | — **PARKED** | — | operator authorization | n/a — registered, not scheduled; no paid probe is authorized |
| E-1 | Natural-traffic dogfood: next work-week of ordinary delegation runs with intent records; feeds the 2026-08-07 review | root (ongoing) | intent writer | B-3 | ≥1 work-week of spawns with intent records; P-D(c) re-measured against a channel that can actually hold the citation |
| E-2 | Registered probes stay on natural triggers (R4 effort frontier; R7 pair; R15 pair) | per-probe | existing registrations | — | unchanged — no bespoke spend; outcomes propagate same-pass per CONTRACT §6.6 |

Ordering: A-1 → {B-1 → B-2 → B-3 → B-6, C-1 → C-2}; B-4 and B-5 are independent and can start
immediately. E-1 begins the day B-3 lands.

**Wave design: none.** The packet's suggested 5–6-lane tier-spanning research fan-out is
declined for R-E's reasons (§2): its two purposes (telemetry variance, dogfood traffic) are
served free by natural traffic plus the registered natural-trigger probes, and no decomposition
item above is blocked on an empirical unknown that a wave would resolve. The single genuinely
open empirical question (B-5, Codex OTel) is one read-only lane, not a wave. **What would change
this:** a D-1…D-4 disposition that surfaces a decomposition-blocking unknown natural traffic
cannot answer — e.g. if B-5 finds the Codex field set large/churny, R-B flips to
shared-implementation and *that* design comparison would justify a small paired-lane wave, whose
telemetry should then be instrumented (R-E's kernel, correctly ordered). Relatedly: this
initiative has now spent three contract-pinned reviews plus one portfolio review against zero new
runtime evidence since 2026-07-20. **This should be the last review-shaped artifact until new
evidence exists** — the next premium spend belongs to B-5/E-1's yield or the operator-gated C-3,
not another review round.

---

## 6. Findings, typed

| ID | Type | Finding |
|---|---|---|
| OD-1 | observed defect (mild) | The spawn-ledger capture schema cannot record a route citation — no field for task class/route/W-ID exists (V6). The instrument-unused reading of the 2.2% is therefore structurally overdetermined; the number cannot measure consultation. |
| OD-2 | observed defect (mild) | `subagent-stop` (3,219) exceeds `subagent-start` (2,016) (V5): the ledger's event kinds have asymmetric coverage — stops exist without starts. Strengthens the packet's own "no rate off this ledger is trustworthy" and adds a second axis to the gap explanation. |
| SG-1 | source gap | The Codex OTel leg of the R-B union test is Unchecked — no local Codex config exists to inspect; the survey's claim is Reported via a summarizing layer. Cheapest closure: item B-5. |
| SG-2 | source gap (packet) | Packet §3.2's "5 cite a route row or W-ID" is not reproducible from the ledger with any obvious method (V7: 0 by W-ID regex, ~10 by loose route regex, 15 structured tags with no route field). Magnitude concordant; the counting method should be recorded or the figure down-labeled — the package's own D-5 standard, applied to the packet. |
| DR-1 | design risk | Integrity checks mis-accusing (demonstrated base rate: `DRIFT?`'s same-day false positive against itself, packet §3.1) — carried as a hard requirement into B-3: every new deterministic check ships with an undecidable state that reports without accusing or failing. |
| DR-2 | design risk | A tool-hook intent writer would inherit the ledger's ~3× intra-session blindness (V9); the writer must sit at the driver's decision point or cover every spawn surface. Mechanism inferred, not confirmed — confirm during B-3 by comparing writer output to `subagent_completed` counts over one week. |
| SD-1…4 | stakeholder decisions | D-1 split ratification · D-2 `sol-*` · D-3 runtime home · D-4 R7 rung table (§4). |
| IQ-1 | implementation question | Sidecar format (JSON vs constrained-Markdown-plus-sidecar) — consolidated §16.2, now scoped to ~14 intent fields + rung tables only; decide inside B-3 by diff-quality comparison, not beforehand. |
| IQ-2 | implementation question | Spawn ordinal semantics for concurrent same-type spawns (P-20260724 unverified item 1) — settle inside B-3 with a two-concurrent-spawn test. |

---

## 7. What this session could not verify, and the cheapest path to each

1. **Codex OTel field set** — Unchecked (SG-1). Path: B-5, read-only.
2. **The "5 cite" count** (SG-2). Path: the packet author records the method, or the figure is
   restated as "0–15 depending on method, channel structurally absent."
3. **The mechanism of the intra-session capture gap** — the surface-subset explanation is
   inferred (DR-2). Path: one week of B-3 writer output diffed against `subagent_completed`.
4. **W-024's chart readings and the Contested effort shape** — vendor-side, taken as labeled
   (Concordant, ±0.5 reading error per
   [PROVENANCE](../research/external/2026-07-24-opus5-fable5-routing-audit/PROVENANCE.md)); not
   re-read here. Resolution path is already registered (P-20260724-r4-effort-frontier, natural
   trigger). No route row was moved, consistent with packet §8.
5. **Survey issue-corpus claims** (RouteLLM/claude-code-router clusters) — first-hand per the
   survey's own method note but not re-run here; nothing in this decomposition is load-bearing on
   them beyond direction.
6. **Whether `agent_type` survives an OTLP (non-console) exporter** — P-20260724's named limit;
   inherit into B-3's exit criterion.

## 8. Disagreements with the prior session, stated directly

1. **Three artifacts → two products** (§1, R-A): the review's own diagram shows the Claude Code
   leg is an adapter, not a product; giving it independent release cadence manufactures drift
   surface — the exact pathology (unreconciled forks, hand-edited deployments) this repo just
   spent a day repairing.
2. **The research wave** (packet Q6 / R-E): declined; the cheaper validation path the falsifier
   asked for exists and is already this package's stated practice.
3. **R-F's framing**: right sequencing, but its independence assumption failed on D-6, and the
   correct resolution of D-6 *follows* the architecture decision rather than preceding it.
4. **Packet §3.2's citation figure** (SG-2): a measurement without its method, inside a packet
   enforcing exactly that standard — small, and worth naming because the standard is the product
   (Q2).
