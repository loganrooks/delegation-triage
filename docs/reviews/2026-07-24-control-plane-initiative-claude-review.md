# Claude review of the delegation control-plane initiative

> **Path note (2026-07-24):** `adapters/codex/delegate-to-*` paths in this document refer to the
> runtime trees as they lived in this repository's worktree at writing time. They moved to the
> `delegation-runtime` repository (D-3, 2026-07-24) and were flattened to its root — read
> `adapters/codex/X` as `X` there. Quoted paths are preserved verbatim.

- **Date:** 2026-07-24
- **Reviewer:** Claude Code (Opus 5), root session, read-only
- **Target:** the proposal set named in the
  [2026-07-24 control-plane initiative handoff](../handoffs/2026-07-24-claude-control-plane-initiative-handoff.md)
- **Overall recommendation:** **REVISE** — restructure the portfolio before ratifying any single
  proposal
- **Authority:** review evidence only. Nothing here was implemented, installed, deployed,
  committed, or activated. No paid model call, no subagent, no network write.
- **Scope note:** the handoff asked seven questions (§4). This review answers them, and then
  reviews the premises the questions presuppose, per the operator's explicit instruction to go
  beyond the assignment.

---

## 0. Summary

The proposal set is unusually rigorous *within each document*. Its dispositions are honest, its
epistemic labels are used correctly, and the prior Sol and Fable reviews found real defects that
were really fixed. I found no dishonesty and little sloppiness in the design work itself.

The problem is one level up. **Every review in this repository was scoped to the artifact handed
to it. Nobody has reviewed the portfolio.** The result is a body of design whose size is set by
the ambition of the product thesis rather than by the evidence available to it — while the live
instrument it is supposed to govern has been quietly broken for at least five days in ways the
proposals' own machinery is designed to prevent and the proposals' own diagnostics did not report.

Two headline results:

1. **Eight live, verified defects (§2)** — including a canonical roster pin that contradicts the
   route table it is cited by, a deployed skill file that was hand-edited and now serves a
   *different* routing doctrine than canonical, three live agents the package does not own, and a
   CI step that fails on the first import. Every one is a propagation or hygiene failure that the
   package's own rules already forbid. None of them is fixed by a release-manifest control plane.
2. **Eight framing findings (§3)** — the largest being that `delegation-triage` is currently two
   different products sharing one name, and that the ratio of uncommitted design and code (≈17,500
   lines) to the instrument it governs (811 lines) to the evidence base beneath it (1,053 lines) is
   roughly 21 : 1 : 1.3.

The recommended disposition is not to reject the consolidated architecture. Most of its
*constraints* are right. It is to **split the portfolio into three artifacts with independent
release cadence and independent evidence burdens** (§6), and to spend the next work-week on the
verified defects rather than on Phase 0.

---

## 1. Verification performed

Every observation below is reproducible from a clean checkout at `main` with the current dirty
worktree, run from the repository root on 2026-07-24.

| # | Command | Result |
|---|---|---|
| V1 | `python3 check_state.py` | exit 1; 4 expired entries (`scarcity-mode`, `fable-window-end`, `reviewer-pin`, `orchestrator-pin`, all `valid_until 2026-07-19`) |
| V2 | `python3 check_wids.py` | PASS — 82 md files, 23 W-records defined and cited |
| V3 | `python3 install.py claude-code --check` | `checked 61 files: 35 not current` — **30 MISSING, 5 DRIFT, 26 OK** |
| V4 | `diff <(git show HEAD:ROUTES.md) ~/.claude/skills/delegation-triage/ROUTES.md` | deployed copy contains text present in **no commit** in repository history |
| V5 | `git log --all -S"two opus reviewers tackling different lenses"` and `-S"mediumw"` | both empty — the deployed strings were never in the repository |
| V6 | `diff agents/explorer.md ~/.claude/agents/explorer.md` | canonical `model: opus`; deployed `model: sonnet` |
| V7 | `shasum -a 256 agents/*.md` vs [`agents/MANIFEST.md`](../../agents/MANIFEST.md) | all 7 match the manifest table |
| V8 | `find ~/.claude/agents -name '*.md'` | 10 definitions; 3 (`sol-advisor`, `sol-code-reviewer`, `sol-design-reviewer`) are not in `agents/` and were never tracked (`git log --all --diff-filter=A -- 'agents/*sol*'` empty) |
| V9 | `PYTHONPATH=adapters/codex/delegate-to-claude/scripts python3 -m unittest discover -s adapters/codex/delegate-to-claude/tests` | **211 tests, 1 error** (`ModuleNotFoundError: No module named 'delegation_policy'`) |
| V10 | same with `PYTHONPATH=…/delegate-to-claude/scripts:adapters/codex/scripts` | 223 tests, OK |
| V11 | `PYTHONPATH=adapters/codex/scripts python3 -m unittest discover -s adapters/codex/tests` | 74 tests, OK |
| V12 | antigravity suite | 10 tests, OK |
| V13 | `git ls-files adapters` | 6 tracked files; the entire `adapters/codex/{scripts,tests,delegate-to-claude,delegate-to-antigravity}` tree is untracked |
| V14 | `git diff .github/workflows/ci.yml` | adds a CI step that runs the command in V9 |
| V15 | `claude --version` | `2.1.218 (Claude Code)`; this review session reports model `claude-opus-5` |
| V16 | line counts | `docs/` 8,539 · untracked adapter Python 8,916 · package core (`ROUTES`+`STATE`+`CONTRACT`+`WARRANTS`+`EPISTEMICS`+`SKILL`) 811 · `probes/` 1,053 |

The handoff's own numbers (§11) reproduce exactly where I checked them: `35 of 61`, the four
expired entries. Its Opus-5 availability inference does not (see F-8).

---

## 2. Observed defects

These are **observed**, not inferred, unless marked. Each names its reproduction command from §1.
All eight are outside this review's write set; none was fixed.

### D-1 · Canonical `agents/explorer.md` contradicts `ROUTES.md` R7, and re-deploying would silently revert an operator ruling — **Blocker**

[`ROUTES.md`](../../ROUTES.md) R7 reads "**sonnet high** default (`explorer` pin re-pointed
2026-07-17, operator ruling)". [`WARRANTS.md`](../../WARRANTS.md) W-023 cites the pin frontmatter
as its locator. But canonical `agents/explorer.md` still carries `model: opus` (V6). The deployed
copy carries `model: sonnet` and the full ruling text.

Consequences, in order of severity:

1. **`python3 install.py claude-code` — the documented, README-quickstart deploy command — would
   silently overwrite the deployed `sonnet` pin with the canonical `opus` pin,** reverting the
   2026-07-17 operator ruling in the live roster and raising cost on every R7 spawn. The migration
   step in the consolidated proposal (§11.4–11.5, "build deployment health first", "install a
   stamped preview") walks directly into this.
2. [`agents/MANIFEST.md`](../../agents/MANIFEST.md) stamps `abf2e469…` as canonical for
   `explorer.md` (V7) — the manifest is internally consistent and *stamps the wrong file*. A hash
   manifest cannot detect a value that was never propagated into the thing it hashes.
3. W-023's locator points at a file whose current content contradicts the warrant.

This is a direct violation of [`CLAUDE.md`](../../CLAUDE.md) ("Profile ↔ pin coupling … flip both
in one commit") and [`CONTRACT.md`](../../CONTRACT.md) §6.4. Commit `2e3b059` changed the route row
and the warrant but not the pin.

**Inference (not observed):** the deployed pin was edited by hand at the time of the ruling, and
the canonical edit was never made. I did not find a commit that would have produced the deployed
bytes.

### D-2 · The deployed Claude Code skill serves a routing doctrine that exists in no commit — **Blocker**

`~/.claude/skills/delegation-triage/ROUTES.md` matches no revision in repository history (V4, V5).
It contains:

- R1: "**fable high**   or two opus reviewers tackling different lenses" — a string never committed,
  with a double space and no cross-vendor `sol-*` candidate row;
- R6: the typo `mediumw`;
- R7: `**opus high**` — the *pre-ruling* value, i.e. the deployed table and the deployed pin (D-1)
  now disagree with each other as well as with canonical;
- no `judgment floors at sonnet` cross-class constraint (commit `f467634`).

So the live instrument that every Claude Code spawn in this environment consults is a hand-edited
fork. The consolidated proposal's §5 requirement — installed copies "must not become independently
edited canonical homes" — is not a forward-looking risk. **It already happened, in the reference
deployment, undetected.**

`install.py --check` *did* report `DRIFT` on this file. Nothing forced anyone to run it, and its
output does not distinguish "deployment is behind" from "deployment diverged."

### D-3 · Three live agents are outside the canonical roster while `ROUTES.md` routes to two of them — **Major**

`~/.claude/agents/` holds `sol-advisor.md`, `sol-code-reviewer.md`, `sol-design-reviewer.md` (V8).
None is in `agents/`, in [`agents/MANIFEST.md`](../../agents/MANIFEST.md), or in any commit.
[`ROUTES.md`](../../ROUTES.md) R1 names `sol-code-reviewer` and `sol-design-reviewer` as the
cross-vendor lens CANDIDATE and cites `P-20260717-sol-b20` for them; three probe records
(`P-20260717-sol-*`) turn on their behaviour.

So the package's most actively-probed 2026-07 route depends on agent definitions the package does
not own, cannot hash, and cannot deploy. `install.py --check` is structurally blind to this: it
only checks files it would itself write, so extras are invisible by construction.

### D-4 · The CI step added to `ci.yml` fails on the first import — **Major**

The uncommitted `ci.yml` change (V14) runs exactly the V9 command, which errors:
`policy_presets.py:12` does `from delegation_policy import …` with no path bootstrap, while
`claude_delegate.py:35–36` *does* bootstrap (`parents[2]/scripts`). Library modules therefore only
import through the CLI entrypoint, or with the shared directory on `PYTHONPATH` (V10).

The [package-boundary amendment](2026-07-20-c0-provider-neutral-package-boundary-amendment.md)
verified the direction that passes ("the shared package imports with only `adapters/codex/scripts`
on `PYTHONPATH`") and never verified the direction that fails. This is the provider-neutral core /
adapter boundary having no import contract — the same defect the amendment was written to fix, one
level down, in the layer that CI would have to run.

### D-5 · Test-count claims are not reproducible from their recorded conditions — **Major**

Three artifacts report three different totals for overlapping suites: 195
([boundary amendment](2026-07-20-c0-provider-neutral-package-boundary-amendment.md), and the Fable
audit disposition), 184 ([Sol quality review](2026-07-20-c0-policy-core-sol-quality-review.md)),
223 ([C0 execution record](2026-07-20-c0-policy-core-execution-record.md)). None records the
`PYTHONPATH`, the interpreter, or the discovery root. I reproduce 211/223 depending only on
`PYTHONPATH` (V9/V10), and the untracked `__pycache__` is `cpython-314` while this host's default
is 3.13.13 — so the interpreter differed too.

Per [`claims-discipline`], a measurement nobody can re-run from what was written is an assertion.
This is the package's own standard failing inside the package's own evidence.

### D-6 · Committing the tracked changes alone breaks `main` — **Major**

`ci.yml`, `CLAUDE.md`, `README.md`, and one probe record are modified and tracked; the adapter tree
they depend on is untracked (V13). A commit of the tracked set alone lands a CI step whose test
directory does not exist in the repository. The handoff (§11.2) describes the worktree as "mixed";
it does not name this specific coupling, which is the one that will actually fire.

### D-7 · Volatile state has been expired for five days, and the deployed copy differs — **Major**

Four entries expired 2026-07-19 (V1). By [`STATE.md`](../../STATE.md)'s own reading rule they are
Unchecked: R1 falls to `opus high`, R13 to `opus xhigh + reviewer gate`, scarcity mode is
undetermined. The scheduled `reviewer-pin` flip (STATE Scheduled item 1) did not execute; the pin
still says `fable`. Separately, the deployed `STATE.md` differs from canonical (V3) — and the
deployed spawn-triage guard parses the *deployed* `Active:` line, so the guard and the repository
are reading different state files.

This is the second consecutive availability event to pass with drivers routing on expired state,
which is exactly disconfirmer **P-D5** in [`README.md`](../../README.md)'s dogfood block. The
disconfirmer's stated consequence — "escalate `check_state.py` from convention to enforced gate, or
abandon" — is now due. CI enforces it on push; nothing enforces it at spawn time in a session.

### D-8 · The "35 of 61" figure conflates three different failures — **Medium**

The consolidated proposal §4.1 reads the count as evidence that "repository canonicality is
presently a social declaration." The decomposition (V3) is:

| Class | Count | What it means | Correct response |
|---|---|---|---|
| MISSING | 30 | new probe records + one runtime prompt, never deployed | re-run `install.py`; harmless lag |
| DRIFT, behind | 2 | `WARRANTS.md`, `probes/INDEX.md` match older commits | re-run `install.py` |
| DRIFT, diverged | 3 | `ROUTES.md`, `STATE.md`, `explorer.md` contain content not in history | **decide, then reconcile — D-1/D-2** |

29 of the 30 MISSING are probe records — evidence added since the last deploy, which is the
*expected* state of a package that appends evidence continuously and deploys occasionally. Reading
them as an integrity failure inflates the case for a release-manifest control plane, while the
three genuinely divergent files — the ones that actually change what the live instrument does —
are not distinguished at all. **One aggregate number hid the only part that mattered.**

---

## 3. Framing findings

These go beyond the handoff's questions. They are judgments, not observations; each states what
would change my mind.

### F-1 · Nobody has reviewed the portfolio — **the finding that generates the others**

The review record is genuinely good: the [cross-runtime cold read](2026-07-17-cross-runtime-routing-proposal-review.md)
returned 5 MAJOR; the [Sol composable-policy review](2026-07-20-composable-claude-capability-and-scope-policy-review.md)
and the [Fable audit](2026-07-20-composable-claude-capability-and-scope-policy-fable-audit.md)
returned 4 blockers and 9 majors between them; all were dispositioned in writing.

But look at the Fable audit's §8, "Alternative architecture assessment." It weighs five
alternatives — fixed profiles, raw settings, categorical fresh-session, container isolation, thin
vertical slice — *all of them inside the composable-policy frame*. It never asks whether a
capability compiler for Codex-managed Claude sessions is the right next thing for this package to
own. Neither does any other review, because none was asked to.

This is a structural property of contract-pinned single-lens review: it maximizes rigor per
artifact and cannot detect that the artifact set is mis-scoped. The consequence is F-2.

**What would change my mind:** a review record that took the portfolio as its unit and returned
"proceed."

### F-2 · The design has outrun the evidence by roughly an order of magnitude

| Layer | Lines | Status |
|---|---|---|
| Uncommitted proposals, reviews, plans (`docs/`) | 8,539 | none ratified |
| Uncommitted adapter Python | 8,916 | uninstalled; 0 completed worker turns |
| **The instrument** (`ROUTES`+`STATE`+`CONTRACT`+`WARRANTS`+`EPISTEMICS`+`SKILL`) | **811** | live, and broken per §2 |
| The evidence base (`probes/`) | 1,053 | 19 records, mostly n=1–3 |

The package's central discipline is that doctrine may not outrun evidence: n=1 never flips a row;
expired state reads as Unchecked; a CANDIDATE row is a probe to run, not a prior to trust. That
discipline is enforced meticulously on the 811 lines and **not at all on the 17,455**. Four of
fifteen `ROUTES` rows are CANDIDATE or PARKED and rightly cannot be relied on; a 1,088-line
authority specification with zero completed runtime turns is treated as a foundation.

I am not arguing the design is wrong. I am arguing it is **ungoverned by the package's own
standard**, and that this is the mechanism that produced §2: attention went to specification while
the instrument rotted.

**What would change my mind:** an argument that architecture decisions here are cheaply reversible
(they are more reversible than routes, but 8,916 uninstalled lines is not cheap), or an evidence
threshold for architecture proposals analogous to W-019 for routes.

### F-3 · `delegation-triage` is currently two products sharing one name

Compare what "supporting a harness" means on each side of the immediate horizon:

| | Claude Code | Codex |
|---|---|---|
| What is governed | Claude's own subagent spawns | Codex driving external Claude *processes* |
| The knobs | roster frontmatter, per-call `model`, Workflow `agent()` | CLI flags, settings files, sandbox, permission modes |
| What the package must supply | readable surfaces + a guard hook | session manager, packet schema, policy compiler, reconciliation, resource governance, recovery |
| Current size | 811 lines of Markdown | 8,916 lines of Python |
| Failure mode | a spawn routed to the wrong tier | an orphaned paid process writing outside its declared scope |

The first is a **decision aid the model reads**. The second is a **delegation runtime that drives
paid external processes**. They share a doctrine and nothing else — different consumers, different
failure modes, different verification regimes, different release cadence, different risk. Calling
both "adapters over one core" is what generates the surface area in the consolidated proposal:
every requirement the runtime genuinely needs (release channels, drift severity, rollback receipts,
retention budgets, pseudonym keys, transactional apply) is then imposed on the doctrine package,
which needs none of them.

This is my main architectural disagreement, and §6 is built on it.

**What would change my mind:** a concrete Claude Code workflow that needs the packet schema,
policy compiler, or reconciliation engine. I could not find one; inside Claude Code the harness
already owns process lifecycle and permissions.

### F-4 · The learning plane inverts the demonstrated yield

Consolidated §8 and handoff §7 specify an eight-stage chain from mechanical event to versioned
release. Set that against what the two existing loops have actually produced:

- **Authored probe records** — 19 records, ~3 weeks — produced the R7 re-point (W-023), the
  judgment floor at sonnet, the `orchestrator` pin, the scarcity-miss and effort-inheritance
  weakness kinds, and every live flip counter.
- **Mechanical orchestration-learning events** — 221 events, 100 runs (consolidated §18) — produced
  **zero** route changes, plus 26 unknown-provenance and 24 validator-gap codes, and one record
  ([Gemini MVP](2026-07-20-gemini-flash-mvp-execution-record.md)) stating its own route and
  disposition events were written together after the fact, so their ordering documents late capture
  rather than the decision sequence.

The proposals honour [W-018] verbally ("no reducer may promote policy automatically") while
building the pipeline whose only payoff would be automatic promotion. W-018's argument — our regime
is single-digit n, ~4 tiers, multi-step, a "completely different statistical regime" — applies *a
fortiori* to telemetry: mechanical events are cheaper per unit and carry strictly less of the
judgment that made the 19 records decision-relevant.

**What would change my mind:** name one route decision in the corpus that was blocked, delayed, or
decided wrongly for want of a mechanical event. If that exists, build the capture for exactly that
field. I did not find one.

### F-5 · The routing table is not yet ready to be projected across providers

Handoff Q3 asks whether provider routing should be one table with projections or several tables.
Both framings assume `ROUTES.md`'s *rows* are the portable unit. They are not, in two ways.

**First, the rows are heterogeneous.** Of fifteen: R1–R8 are genuine task classes; R9 ("Sonnet 5 at
xhigh — AVOID pending probe") is a pricing posture filed as a route; R11 is a parked experiment;
R12, R14, R15 are unadjudicated CANDIDATEs, two of them about *advisor plumbing inside Claude Code*
rather than about task shape at all. Projecting that set to Codex exports four rows of noise and
two rows that cannot mean anything outside this harness.

**Second, the portable content is in the left column, not the right.** What survives a provider
change is the task ontology and the discriminators: R1-vs-R7 (verdict on a finished artifact vs
verification inside a synthesis), "judgment floors at sonnet," "diverse lanes over higher tier,"
"fixed-step transformations prefer scripts." Those are claims about *what the task demands*. The
right column — `fable high`, `opus xhigh` — is a binding of that demand to one roster at one date
with one price list, and [`STATE.md`](../../STATE.md) already expires it. The package's own
situated-capability commitment (consolidated §9.1) says this outright and the routing proposals do
not follow it.

So the correct decomposition is neither of the offered options:

```
task class  →  judgment/capability demand  →  [binding]  →  (provider, model, effort, surface)
   portable          portable                  per-harness        volatile, dated, expiring
```

`ROUTES` + `WARRANTS` + `STATE` already implement about 80% of this. The missing 20% is that route
rows name models directly instead of naming demands. Making R1 read "adversarial verdict; needs
top-tier judgment discrimination; ≥2 independent lenses" *and then* binding that to `fable high`
via a per-harness table is a genuinely small change — and it is the change that makes a Codex
projection mean something.

**What would change my mind:** evidence that a second harness's operator wants the bindings rather
than the ontology. That is an empirical question about a user who does not exist yet (F-6).

### F-6 · The product thesis has not decided who the user is

Handoff §2 promises "a condensed, citable knowledge base of routing claims." Two incompatible
readings:

- **(a) The method and the empty instrument** — warrant grading, expiry semantics, flip thresholds,
  the probe loop, the task ontology, the control-surface analysis. Portable, honest, small, already
  written. A second user fills it with their own evidence.
- **(b) The routing answers** — "sweeps go to sonnet high." Not portable: conditioned on this
  operator's model access, prices, subscription window, task mix, and harness, every one of which
  the package itself marks as volatile with a `valid_until`.

The proposals slide between these. "Citable knowledge base" and "research-backed" suggest (b);
"the method is portable … works for any model roster" ([`README.md`](../../README.md)) says (a).
The distinction is load-bearing because it decides what a release *is*. Under (a) a release is a
versioned method plus a schema, and drift in someone else's routing table is none of our business.
Under (b) a release ships priors, and it needs an argument for why one operator's n=1–3 evidence
transfers — an argument the package's own W-018 and §9.1 make hard to give.

My reading: **(a) is the product, (b) is the dogfood.** That is a strength, not a limitation — the
lab notebook is what makes the method credible. But it must be said explicitly, because the whole
telemetry-and-release apparatus is sized for (b).

**What would change my mind:** a named second consumer whose delegation decisions would improve by
adopting our bindings rather than our method.

### F-7 · Specification has passed the point of diminishing return relative to probing

The [composable policy proposal](../proposals/2026-07-20-composable-claude-capability-and-scope-policy.md)
is 1,088 lines across four revisions, governing an adapter whose single authorized runtime contact
[terminated before any model turn](../../probes/records/P-20260720-claude-profile-actual-runtime.md).
That one contact falsified a design assumption (startup exposure ≠ permission-allowed authority).
Its §17.3 lists six open questions; every one is empirical, and none can be closed by more prose:

> Which macOS mechanisms can enforce memory and process ceilings … Can the installed Claude runtime
> expose all effective managed settings without a paid model turn … Are MCP server processes
> launched inside the same enforceable boundary …

Meanwhile the C0 implementation run cost USD 6.86 and the Fable audit USD 4.80 — so the *next*
probe is comparable in cost to another review round, and unlike another review round it can resolve
§17.3. The evidence-to-specification ratio should invert now.

**What would change my mind:** if the next runtime probe is genuinely blocked on a contract
decision. Reading §17.3, it is not — a fresh version-3 run is described as "the smallest next probe"
and is gated only on operator approval.

### F-8 · A Reported vendor fact was carried into the handoff as a local constraint

Handoff §8 records that "Claude Code 2.1.218 was installed during this audit, while the official
changelog adds Opus 5 support in 2.1.219." **Observed here:** `claude --version` reports 2.1.218,
and this session reports model `claude-opus-5` (V15). Whatever 2.1.219 added, Opus 5 resolves on
2.1.218 in this environment.

Small in itself; instructive as a specimen. It is the `route-rule-inheritance` failure kind from
[`KNOWN-WEAKNESSES.md`](../../probes/KNOWN-WEAKNESSES.md) — a conditional external fact promoted
into a handoff as a bare constraint, where a downstream reader would follow it over local
observation. The handoff did say "re-check at takeover time," which is the right instinct; the
recheck is now done and the answer is no.

---

## 4. Answers to the handoff's seven questions

**Q1 — Does the consolidated proposal express the thesis without overstating implementation or
support?** Implementation status: **yes, scrupulously** — "uninstalled," "non-activating," "fake-CLI
tests prove adapter behaviour only" appear consistently and are accurate. Empirical support:
**no, in one direction** — §4.1 reads the drift count as an integrity failure when 29/30 of it is
ordinary deploy lag (D-8), and §8 presents the learning plane as a solution without establishing
the problem (F-4). Neither is dishonest; both are unwarranted emphasis.

**Q2 — The correct separation of layers.** Four layers, not five, and the split is different from
the handoff's table:

1. **Doctrine + task ontology + evidence** — the delegation test, task classes and their
   discriminators, warrants, epistemic labels, probe discipline, flip thresholds. Provider-neutral
   because it is about *tasks and judgment*, not models. This is the product (F-6a).
2. **Capability claims** — dated, expiring, per (provider, model, harness): what this model at this
   effort in this harness has been observed to do. Already `WARRANTS` + `STATE`.
3. **Harness projection** — what surfaces exist here and what they can pin, plus the fallback when
   they cannot. One page per harness. `CONTRACT` §3 is the Claude Code instance of this and it is
   the single most reusable thing the package has.
4. **Execution runtime** — packets, authority compilation, sandboxing, session lifecycle,
   reconciliation. **Not a layer of the doctrine package** (F-3); a separate product that consumes
   layers 1–3 as data.

The handoff's "route projection" layer collapses into a resolver over 1–3 and needs no separate
ownership. Its "overlay" layer already exists as [`CONTRACT.md`](../../CONTRACT.md) §5 and needs
nothing new.

**Q3 — One table with projections, separate tables, or another structure?** **Another structure:**
one task ontology with capability *demands*, bound per-harness. See F-5. Explicitly reject both
offered options — a flattened table erases harness conditions (the handoff is right about that),
and parallel per-provider tables duplicate the ontology, which is the only part that is stable.

**Q4 — How should both harnesses consume one release?** By **reading**, not by installing a
policy fork. Claude Code already does this (skill directory) and Codex should do the same: point at
a checkout or a stamped snapshot, never a copy that can be edited. The binding constraint is not the
mechanism — `install.py --check` already detects divergence — it is that nothing runs it and its
output does not classify direction (D-2, D-8). Fix the classification and the invocation before
designing channels.

**Q5 — Minimum contracts before a harness is "supported."** Four, and they are much smaller than
consolidated §6:
(i) a single deploy command that is idempotent and reports what it would change;
(ii) `--check` that classifies **behind / diverged / extra** and exits non-zero on *diverged*;
(iii) a manifest that records what was deployed, from which revision, and whether the session was
restarted;
(iv) an explicit statement of what the harness can and cannot pin, with the fallback (i.e. layer 3).
Release channels, transactional apply, rollback receipts, and dirty-state digests are runtime-product
requirements (F-3), not doctrine-package requirements.

**Q6 — Which proposal is authoritative for what; where do they conflict?** See §5. The real
conflict is not between documents — they are carefully cross-referenced — but between the
consolidated proposal's *scope* and every other document's scope. It claims the routing domain
including deployment generation, release channels, event schemas, and retention policy (§5.1); the
cross-runtime proposal explicitly forbids a provider-neutral route split in its slice (§6.1); the
deferred router proposal says shared implementation is extracted "only after two adapters
demonstrate identical semantics rather than merely similar names" (§4.3). By that test the router
is not yet reopenable: one adapter has completed zero worker turns and the other has completed one
task with unattested provider identity.

**Q7 — What can be decided now, what needs a stakeholder, what needs a probe?**

| Decidable from current evidence | Needs the stakeholder | Needs a dated probe |
|---|---|---|
| All eight defects in §2 | Portfolio split (§6) | Runtime activation of any authority claim (F-7) |
| `--check` direction classification | Product identity (a) vs (b) (F-6) | Whether `explain` can enumerate managed settings without a paid turn |
| Route-row cleanup (F-5) | Whether the Codex runtime continues at all | R7 sonnet-vs-opus paired probe (W-023, still 0 paired) |
| Committing the worktree in coherent slices | Fable window / scarcity mode (D-7) | R15 advisor high-vs-xhigh pair |

---

## 5. Per-proposal disposition

| Proposal | Disposition | Basis |
|---|---|---|
| [Consolidated multi-harness control plane](../proposals/2026-07-21-consolidated-multi-harness-delegation-control-plane.md) | **REVISE — do not ratify as one product** | Constraints are largely right; scope conflates two products (F-3) and its two empirical arguments are overstated (D-8, F-4). Revise to the split in §6, keep §§7.1–7.3, §8.2–8.3, §13 nearly verbatim. |
| [Cross-runtime routing and Claude delegation](../proposals/2026-07-17-cross-runtime-routing-and-claude-delegation.md) | **ACCEPT as the runtime product's charter** | Its invariants (planned/requested/observed, ownership, recovery, content-free events, root disposition) are the strongest work in the set and survive the split unchanged. Re-scope it as the founding document of the *separate* runtime rather than a slice of the doctrine package. |
| [Composable capability and scope policy](../proposals/2026-07-20-composable-claude-capability-and-scope-policy.md) | **PARK at revision 4; no revision 5** | Contract is sound and reviewed twice. Its open questions are empirical (F-7). Next artifact should be a probe record, not a revision. C0 stays uninstalled. |
| [Capability-based execution profiles](../proposals/2026-07-19-capability-based-claude-execution-profiles.md) | **ACCEPT as historical evidence** (unchanged) | Correctly marked superseded-in-part; no action. |
| [Deferred provider-neutral router](../proposals/2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md) | **RETAIN as active, not superseded** | Its §4.3 test ("identical semantics, not merely similar names") is unmet; its §5 invariants remain the right compatibility boundary. The consolidated proposal should *not* supersede its deferral yet. |
| [Codex-managed Antigravity adapter](../proposals/2026-07-20-codex-managed-antigravity-gemini-flash-adapter.md) | **PARK** | One task, unattested provider identity. Useful as migration evidence exactly as the handoff says; not a third harness for planning purposes. |

Handoff §9 (execution profiles: "stop using `auto` as the default escape hatch") is a **real and
correct requirement** and I am not parking it — but it belongs to the runtime product, and it is
blocked on the same empirical questions as F-7.

---

## 6. Recommended architecture

**Split the portfolio into three artifacts with independent release cadence and independent
evidence burdens.**

```
┌─ delegation-triage  (this repo, stays ~1k lines of Markdown) ───────────┐
│  doctrine · task ontology + judgment demands · warrants · volatile      │
│  state · probe loop · epistemics · per-harness projection (1pp each)    │
│  consumed by READING; installed by copy+stamp; no runtime, no telemetry │
└────────────────────────────┬────────────────────────────────────────────┘
                             │ consumed as data (versioned, hashed)
        ┌────────────────────┴───────────────────┐
┌───────▼─────────────────┐          ┌───────────▼──────────────────────┐
│ Claude Code integration │          │ delegate-to-claude RUNTIME       │
│ skill + roster + guard  │          │ (separate package)               │
│ ~0 new code             │          │ packets · policy compiler ·      │
│                         │          │ sessions · reconciliation ·      │
│                         │          │ resource governance · events     │
└─────────────────────────┘          └──────────────────────────────────┘
```

Why this and not the consolidated single product:

- The doctrine package can ship, and can be honestly described, **today**. It is the thing with a
  three-week evidence record behind it.
- The runtime carries its own risk (paid external processes, filesystem authority, orphan recovery)
  and therefore its own verification regime, without imposing that regime on a Markdown package.
- A third harness costs one page in layer 3, not a new adapter in a monolith.
- The Antigravity work becomes what the handoff already says it is — migration evidence for the
  runtime — with no pressure to make it a peer of Claude Code.

**Alternatives, honestly:**

| Option | Case for | Case against |
|---|---|---|
| **A · Ratify consolidated as-is** | Preserves momentum; one authority; the constraints are good | Locks in F-3; imposes runtime-grade release machinery on an 811-line doctrine package; §2 defects remain unaddressed because none of them is an architecture problem |
| **B · Revise consolidated in place, keep one product, tighten phases** | Least disruption; keeps cross-references intact | The scope conflation is the *source* of the surface area; tightening phases does not remove it |
| **C · Split into three (recommended)** | Right-sizes each artifact's evidence burden; unblocks shipping doctrine; makes Codex support tractable | Costs a re-scope pass over the consolidated proposal and a repo decision for the runtime; some cross-references need rewriting |
| **D · Park the control plane entirely; fix hygiene only** | Cheapest; addresses 100% of observed harm | Abandons genuinely good design work; the Codex ask is real and recurring |

I recommend **C**, with **D's** work-week done first and independently — the §2 fixes are not
contingent on the architecture decision and should not wait for it.

**Sequencing (proposed, not authorized):**

- **Now, no new architecture** — reconcile D-1/D-2/D-3 (each is a *decision*, not an edit: which
  `explorer` pin is intended, which R1 text is intended, whether `sol-*` joins the roster); fix D-4
  by giving the shared package a real import contract; land D-6 by committing the adapter tree and
  its CI step together or neither; refresh or re-expire STATE (D-7); teach `install.py --check` to
  classify behind/diverged/extra and exit non-zero on *diverged*.
- **Then** — re-scope the consolidated proposal to the doctrine package only; convert `ROUTES` rows
  to demand-plus-binding (F-5) and write the Codex projection page; ratify.
- **Then** — charter the runtime from the cross-runtime proposal, and spend the next paid probe on
  §17.3 rather than on another review round.

---

## 7. Proposal sections that must change before planning

| Document | Section | Required change |
|---|---|---|
| Consolidated | §4.1 | Replace the "35 of 61" reading with the three-way decomposition (D-8) and state which class the argument rests on |
| Consolidated | §5.1 | Remove deployment generation, release channels, retention policy, and the event schema from the doctrine package's ownership; assign to the runtime (F-3) |
| Consolidated | §8 | State the decision that mechanical capture would have changed, or downgrade Phase 3 to "capture the fields the authored records already need" (F-4) |
| Consolidated | §14 | Re-cut Phase 0 around the §2 defects; Phases 1–5 become the runtime's roadmap |
| Consolidated | §16 | Add: product identity (a) vs (b) (F-6); portfolio split (F-3) |
| Consolidated | §1 | Do not supersede the deferred router's deferral — its own reopening test is unmet |
| Handoff | §5 table | Replace the five-layer table with the four layers in Q2; drop "route projection" as an owned layer |
| Handoff | §8 | Correct the Opus-5 availability inference (F-8) |
| Handoff | §11 | Add D-1, D-2, D-3, D-4, D-6 to known outstanding state |
| [`ROUTES.md`](../../ROUTES.md) | table | Separate task classes from pricing postures (R9), parked experiments (R11), and instrument-plumbing rows (R14/R15) before any projection (F-5) |

---

## 8. Boundary: immediate vs later

**Immediate (Claude Code + Codex):** the §2 defects; `--check` classification; route-row cleanup;
one Codex projection page; committing the worktree coherently. None requires a new schema, a
release channel, or a paid call.

**Later (needs evidence first):** the policy compiler's activation, any authority claim, automatic
event capture, recommendation-only routing, additional providers, cross-project telemetry, and
every one of consolidated §16's eight open decisions except release authority.

---

## 9. Unresolved uncertainty and evidence still required

1. **Which `explorer` pin is intended (D-1)** — operator decision, not a defect I can resolve.
   Everything downstream (W-023's locator, R7's claim, the manifest stamp) follows from it.
2. **Who edited the deployed `ROUTES.md` and when (D-2)** — I established only that the bytes are
   not in history. The provenance is unrecovered.
3. **Whether `sol-*` should be canonical (D-3)** — depends on whether the gateway dependency
   (`claudex`) is acceptable in a public package. Not mine to decide.
4. **Whether the runtime product should live here or in its own repository** — I recommend its own;
   I have no evidence about your maintenance preferences beyond the repo's own trunk-plus-tags
   pattern.
5. **R7's paired probe is still 0/n** (W-023) — the sonnet-first ruling is an operator policy with
   adjacent evidence only. It is the single most consequential unverified row and D-1 means we
   currently cannot even say which tier is deployed from canonical.
6. **The 2026-08-07 dogfood review** ([`README.md`](../../README.md)) is 14 days out and P-D5's
   disconfirmer has now fired twice (D-7). That review should not be allowed to slip behind the
   control-plane work.

---

## 10. What this review did not do

No implementation, no fix, no commit, no stage, no deploy, no cleanup, no deletion, no paid call,
no subagent, no network write. The mixed worktree is preserved exactly as found. No historical
proposal, review, plan, or probe record was edited. This document is additive.
