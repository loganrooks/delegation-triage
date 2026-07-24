All source reading and analysis are complete. Here is the full audit report.

---

# Correction audit — composable Claude policy (rev 3) and C0 contract-core plan

## 1. Audit identity

**Reviewed paths and hashes (observed via `shasum -a 256`, match the packet):**

- `docs/proposals/2026-07-20-composable-claude-capability-and-scope-policy.md` — `bbb76fb05c5e298ebf044220c0f2a4cf72132505c4c98adce60c02ab00a6335e` ✔
- `docs/superpowers/plans/2026-07-20-composable-claude-policy-contract-core.md` — `3d860d04b012fe32be7444a5b33e64dc2005d89fd9e5265090bc735520b73f61` ✔

**Also read:** the Sol revision-2 review and root dispositions; the 2026-07-19 historical proposal record (via its supersession map and the Sol review's citations); `probes/records/P-20260720-claude-profile-actual-runtime.md`; `CONTRACT.md`; `EPISTEMICS.md`; candidate sources `profiles.py`, `runtime_policy.py`, `claude_delegate.py` (parser, `command_resume`, `sanitized_status`), `state_budget.py` (constants), `test_claude_delegate.py` (harness), `test_profiles.py` (test inventory).

**Limitations:** Shell access was revoked after the hash check, so I could not re-run the adapter suite; the plan's "195 tests PASS" baseline is treated as *reported*, not observed. I did not independently fetch Anthropic/MCP documentation; provider-behavior claims below inherit the proposal's "reported" grade. No graph re-indexing or mutation was performed. Model: Fable 5 (effort not exposed).

## 2. Executive verdict

**`REVISE THEN IMPLEMENT`.**

Revision 3 genuinely resolves the Sol review: the four-stage evidence model (requested → compiled → preflight-assessed → runtime-observed) is epistemically clean, the normative schema (§18), extensibility matrix (§18.1), requirement ledger (§19), and cohort split (§15) close POL-002/-004/-011/-012, and the stakeholder decision to keep broader/mixed resumes with independent suppressible notices is implemented without smuggling authority into presentation. The architecture does not need rethinking, and C0 is the right first cohort.

However, the C0 plan as written would **freeze several defective or underspecified identity and comparison semantics into schema version 1** — the one layer every later cohort depends on. The worst are: the semantic hash is defined over canonical bytes that still contain machine-local root paths (contradicting §18's own exclusion rule and destroying cross-machine policy identity); the `resources` defaults (`null` = unbounded) contradict the schema preamble's "absence never means unrestricted"; the confirmation enum contradicts §9.6; and the transition classifier can never produce the `unknown` kind §11.1 requires, while `mcp.mode: readonly` is accepted with no registry to resolve it. All are small, bounded plan/proposal edits. Fix them before execution; do not re-architect.

## 3. Blockers and major findings

### CA-001 — Blocker (C0) — Semantic hash is defined over bytes that include private absolute paths

**Evidence:** Plan Task 2 Step 4: "Canonical JSON uses sorted keys and compact separators. SHA-256 the UTF-8 canonical bytes." Schema roots carry absolute bindings (proposal §7.1: `shared_docs: /absolute/path/...`; plan Task 5 test constructs `policy_with_private_path`). Proposal §18: "The semantic policy hash excludes run-local paths only after binding them to stable root roles and separately recording their private resolved values."
**Failure scenario:** The same `verified-review` policy compiled on two machines (or in two checkouts) yields different `semantic_sha256` because `${workspace}` binds differently; every resume then reports a policy change, and the hash cannot serve as the cross-run contract identity §6.1 promises. Conversely, if a worker "fixes" this by hashing paths, the plan's `test_private_absolute_paths_are_not_authority_atoms` passes while the hash silently leaks path-derived fingerprints into telemetry-adjacent records (POL-010 territory).
**Required change:** Specify in the plan exactly how `canonical_document` detaches path bindings — e.g., replace each bound root value with its symbolic role (`"project": "<bound:project>"`) before hashing, and store resolved values only in a separate private record. Add a RED test: identical policies with different root bindings ⇒ identical `semantic_sha256`; a *changed set of declared root roles* ⇒ different hash. Also decide whether `notices`/`confirmation` are inside the semantic hash (they currently are, so a presentation-only change alters the "semantic" hash while `kind == exact`); either exclude them or add a second `authority_sha256` and say which one resume comparison keys on.
**Timing:** C0 blocker — this is the identity primitive.

### CA-002 — Blocker (C0) — `resources` defaults contradict the default-deny invariant

**Evidence:** §18 preamble: "Omitted authority fields default to `deny` or `unavailable`; absence never means inherit unrestricted authority." §18 body: every `resources` field defaults to `null`. Plan Task 4 Step 3: "`null` resource limit means unbounded."
**Failure scenario:** A custom policy that omits `resources` normalizes to unbounded wall time, processes, logs, and generated state — the exact "absence = unrestricted" the preamble forbids — and the diff engine then classifies adding *any* finite limit as `narrower`, so an operator dropping a limit sees `broader` correctly, but the default posture itself is maximally broad and invisible.
**Required change:** Either (a) make preset/default resources explicitly `unbounded` values that count as authority atoms (so the breadth is visible and diffable), or (b) redefine `null` as `unknown/unset` (not an authority claim) and add a distinct `unbounded` sentinel. Amend §18 or the plan so the two agree, and add a RED test for omitted-`resources` normalization. Note the generated-state dimension must still reconcile with the retained 240 MiB / 192 MiB constants (`state_budget.py:20-21`) — a preset claiming `generated_state_bytes: null`/unbounded contradicts a stakeholder-preserved ceiling.
**Timing:** C0 blocker.

### CA-003 — Blocker (C0) — Confirmation enum contradicts the proposal

**Evidence:** Plan Task 2 Step 3: `CONFIRMATION_MODES = {"ask", "never"}`. Proposal §9.6: "The operator may configure the notice and confirmation as `always`, `once`, or `never`." §11.2 is compatible with either, and §18 uses `ask`/`never`.
**Failure scenario:** C0 freezes `{ask, never}` into schema v1; C3/C4 implement §9.6's `once` for unsandboxed-command confirmation and must break schema v1 or fork the enum.
**Required change:** Reconcile now: either amend §9.6 to `ask`/`never` (and define whether `ask` means every occurrence), or extend `CONFIRMATION_MODES` to include `once` with defined semantics. Note that `once` (for notices too) requires durable "already shown" state — see CA-011.
**Timing:** C0 blocker (one-line enum decision, but frozen afterward).

### CA-004 — Blocker (C0) — `unknown` transition kind is unreachable, and unresolved dimensions are compared as if empty

**Evidence:** §11.1 defines `unknown: the adapter cannot compute the preflight transition.` Plan Task 4 Step 3's classifier yields only `exact/broader/narrower/mixed`. Meanwhile `MCP_MODES` accepts `readonly` although the registry that resolves a readonly bundle to tools is explicitly deferred (R-MCP-001: "C0 schema; later registry plan"); `COMMAND_MODES` and directional comparators never place `unavailable` in the `denied < selected < unrestricted` order.
**Failure scenario:** Two policies with `mcp.mode: readonly, servers: [x]` produce zero resolved MCP atoms; the diff reports `exact` even though the actual bundle content is unknown and may have changed between registry revisions. Similarly `commands: unavailable → selected` has no defined ordering; a worker guesses.
**Required change:** (1) Define ordering for `unavailable` (recommended: below `deny` on the authority scale but flagged as `runtime_change`, since it encodes activation, not refusal). (2) Where a dimension is unresolvable in C0 (`mcp.mode: readonly` with no registry; `commands.mode: selected` with templates the schema can't yet type — see CA-006), the transition report must carry `kind: unknown` or a per-dimension `unresolved` marker mirroring the `explain` field, with a RED test. (3) Add a RED test that produces `unknown`.
**Timing:** C0 blocker — the diff contract is C0's central deliverable.

### CA-005 — Major (C0) — Authority atoms cannot see deny-rule removal or non-root path allows

**Evidence:** Plan Task 2 Step 4 enumerates atoms as *allowed* roles/tools/IDs/destinations/loosenings. §7.1 permits `defaults: {read: allow}` (advanced) plus `hard-deny` path rules, and rules may carry raw `path:` values.
**Counterexample (packet Q3):** Advanced policy A: `filesystem.defaults.read: allow` + rule `deny ~/.ssh`. Policy B: identical minus the deny rule. Atom sets are identical (both contain the host-read atom); `compare_policies` returns `exact`; the operator resumes into a policy that can now read `~/.ssh` with no `authority_change` notice. Second counterexample: an allow rule with a raw `path:` (not a declared root) has no defined atom at all.
**Required change:** Two cheap C0 invariants: (a) allow rules must reference declared named roots (raw `path:` permitted only for denies) — reject otherwise; (b) represent denies as negative atoms (or a parallel deny set) so that a removed deny appears in `added_authority`. Add both as RED tests.
**Timing:** C0 (the schema invariant must exist before v1 freezes); the advanced host-read profile itself remains C6.

### CA-006 — Major (C0) — Command-template element schema is undefined while template IDs are authority atoms

**Evidence:** §18 shows `commands.templates: []` with no element type; §9.1 lists ten normative per-template fields; plan atoms include "command-template IDs" and `test_unsandboxed_template_is_an_authority_atom`.
**Failure scenario:** Template `t1` v1 (`argv: ["pytest","-q"]`, `network: deny`) is later edited to add `network: allowlist`. The atom `command:t1` is unchanged ⇒ `exact` despite a material authority change. Also, a fresh worker cannot write `normalize_policy` for `templates` without inventing the element schema — exactly the "guessing" the plan forbids.
**Required change:** Either (a) define a minimal v1 template element (`id`, `argv`, `sandbox` disposition, `network` disposition) and make the atom content-addressed (`command:<id>@<template-hash>`), or (b) declare `templates` must be empty in schema v1 (rejected otherwise) and defer the element schema to the C3 plan with a schema-version bump. (b) is smaller and honest; recommended.
**Timing:** C0 blocker-adjacent; choose before execution.

### CA-007 — Major (C0 plan text) — Task 7's patching instruction is infeasible under the existing test harness

**Evidence:** Task 7 Step 1: "Patch `subprocess.Popen` and `execute_attempt` in explain tests and assert they are not called." The existing harness invokes the CLI in a **separate process** (`test_claude_delegate.py:143-153` runs `[sys.executable, SCRIPT, ...]`); `unittest.mock.patch` cannot cross that boundary.
**Required change:** Specify in-process invocation for these assertions — import `claude_delegate` and call `main(["explain", ...])` under `mock.patch` — alongside the existing subprocess-level proofs (`args_log` absent, no state root created), which Task 6 already includes. Also define what "run/resume do not call C0" means operationally (e.g., patch `normalize_policy`/`preset_policy` and assert uncalled during an in-process `run` against the fake CLI), since a top-level import in `claude_delegate.py` will import C0 modules on every invocation — importing is acceptable, calling is not; say so.
**Timing:** C0 (plan wording only).

### CA-008 — Major (C0) — The assurance-label source is unspecified

**Evidence:** Plan Task 2 defines the `ASSURANCE` enum; Task 5's explain output contains `"assurance": {"built_in_read": "claude-enforced"}`; §7.4 says the adapter and tests maintain the matrix. But no interface, preset field, or schema dimension carries assurance data, and `CompiledPolicy` has no assurance member.
**Failure scenario:** A fresh worker must invent where assurance lives (schema? preset constant? explain-local table?), and two plausible choices produce different hashes (if put in the document) or unauditable claims (if hardcoded in `policy_explain`).
**Required change:** State it: a static, versioned mapping in `policy_presets.py` (or `policy_explain.py`) from preset × operation-family → assurance label, explicitly *outside* the policy document and hash, with every C0 label being `claude-enforced`, `manager-controlled`, or `unknown` (never `os-enforced`, which no C0 evidence supports).
**Timing:** C0.

### CA-009 — Major (C0) — Whose notice/confirmation settings govern a transition is undefined

**Evidence:** Both `before` and `after` policies carry `notices`/`confirmation` blocks; `compare_policies(before, after)` emits `notice_events` with a `mode`, but the plan never says which side's settings apply (nor what happens when the settings themselves differ mid-transition).
**Failure scenario:** Before-policy has `authority_change: always`; the resume request's policy sets it to `never`. If `after` governs, an attacker-suggested (or merely careless) invocation can suppress the notice for the very transition that broadens authority — the untrusted-configuration hazard §11.2 explicitly excludes.
**Required change:** Define: notice/confirmation modes are taken from operator-owned configuration resolved at the *resume invocation* (the `after` side), but a transition that *changes a notice or confirmation setting itself* is always recorded and, when the change is `always→never`-ward, surfaces under the existing rules of the `before` policy for that one transition. Add a RED test. (This preserves the stakeholder decision — `never` remains fully available — while preventing a single invocation from both broadening authority and silencing its own notice.)
**Timing:** C0.

### CA-010 — Major (pre-first-release) — Registry identity is absent from the compiled policy

**Evidence:** `mcp.servers` is a list of names (§18); registry records carry versions/hashes (§8.2) but nothing binds a compiled policy to a registry revision.
**Failure scenario:** The registry updates server X's bundle (new tool admitted). Two compiled policies before/after the update are byte-identical ⇒ `exact`, no cache warning — yet the resolved tool set (a documented cache-invalidating input) changed.
**Required change:** When the registry lands (C-later), include the resolved registry record version/hash per server in the compiled document; in C0, this is another reason `readonly` must classify as unresolved (CA-004).
**Timing:** Pre-first-release (before any cohort that resolves `readonly`); C0 needs only the CA-004 marker.

### CA-011 — Medium (pre-first-release) — `once` notice semantics require state that nothing owns

**Evidence:** `NOTICE_MODES` includes `once`; C0 "creates no persistent runtime state" (plan Status) and `explain` is stateless.
**Failure scenario:** Two implementations legitimately disagree on "once per what" — per run, per policy hash, per transition kind, per operator lifetime — and where the marker persists.
**Required change:** Define scope (recommended: once per `(category, transition-hash)` per run lineage, persisted in the private run record) in the proposal; C0 may accept and normalize `once` without implementing display.
**Timing:** Pre-first-release (C1).

### CA-012 — Medium (C0, minimal set) — Cross-field invalid states are not enumerated

Examples a worker must currently guess: `commands.mode: selected` with empty `templates`; `network.subprocess: allowlist` with empty `allowed_destinations` (empty allowlist should normalize to `deny`, not remain a distinct hashable state); `mcp.mode: selected` with empty `selected_tools`; `sandbox.unsandboxed_commands` non-empty while `sandbox.mode: off`; `sandbox.mode: required` with `commands.mode: deny` (harmless but should normalize consistently). **Required change:** add a short table of reject-vs-normalize outcomes to the plan and RED tests for at least the first three.
**Timing:** C0.

### CA-013 — Medium (C0 comparator gaps)

`sandbox.mode` (`required < preferred < off`, narrow→broad), `resources.memory.mode` (`enforced < sampled < unknown`? — must be defined), and the allowlist→`unrestricted` collapse (dropping destination atoms while adding the unrestricted atom must classify `broader`, not `mixed`) all lack comparators/tests. Plan Task 4's test list omits the allowlist→unrestricted case entirely. **Timing:** C0 (small additions to Task 4).

## 4. Missing cases and opportunities (beyond the packet)

- **Root-rebinding invisibility.** Same symbolic roots, different absolute bindings ⇒ `exact` with no notice, because resolved paths are (correctly) outside the hash. `context.workspace_identity` covers the workspace but not a re-bound `shared_docs`. Add a per-root binding identity (keyed pseudonym of the resolved path, consistent with §12's telemetry rules) to the `context_change` inputs. *(Pre-first-release.)*
- **Two version namespaces.** Legacy `PROFILE_VERSION = 3` (`profiles.py:14`) and new preset `version: 1` will coexist in `status` output and operator heads. `explain` should label them distinctly ("policy preset revision" vs "legacy profile contract version"). *(C0, cosmetic but cheap.)*
- **Migration fixture is thin.** Task 1's fixture freezes capability flags but not `denied_tools`, the pinned MCP list, or manifest hashes; a drive-by edit to `_GLOBAL_DENIED_TOOLS` would pass the migration test (it is caught only by the existing `test_exact_profile_snapshots`). Acceptable, but say in the plan that the fixture intentionally freezes only the flag surface. Also state explicitly whether the alias appears as a key inside `fixture["profiles"]` (the Step 3 loop implies yes). *(C0 wording.)*
- **Schema-upgrade resume test is unwritable in v1.** §14.1 demands "stable resume across a policy-schema upgrade with no semantic change," but with only version 1 there is nothing to migrate and no migration interface exists. Either add a reserved `normalize_policy` version-dispatch seam now (cheap) or move that verification bullet to the C-cohort that introduces version 2. *(C0 decision.)*
- **Exposed-but-denied fixture opportunity.** §14.1 requires manifest fixtures "based on the actual 2026-07-20 init shape," but the C0 plan never consumes the probe's real init manifest. Since `classify_manifest` treats *any* denied tool's exposure as expected (`profiles.py:171-192` — including `WebFetch`), a C1 fixture should distinguish "expected exposed-but-denied MCP identifiers" from "denied built-ins whose exposure would still be surprising." Not a C0 defect, but record it so C1 doesn't inherit the conflation.
- **Positive product opportunity.** `explain --format json` plus the stable atom vocabulary is a good CI artifact; consider (later) a documented guarantee that atom strings are append-only stable identifiers, since operators will diff them in scripts.

## 5. Sandbox and unsandboxed-execution assessment

**Sound:** §9.4–9.6 are honest. The pitfalls table (§9.5) covers merged settings arrays, `dangerouslyDisableSandbox` retries, sockets/Docker, Apple Events, credentials, aliases, MCP process placement, resource exhaustion, crashes, and test incompatibility, each with a mitigation that respects operator control. The candidate's `SANDBOX_REQUEST` (`runtime_policy.py:18-25`) already encodes `allowUnsandboxedCommands: false`, empty `excludedCommands`, and full network deny, and `--setting-sources ""` suppression is correctly described as narrowing, not proving (`runtime_policy.py:219-224`). Assurance labels prevent the classic dishonesty of calling permission rules "OS enforcement." Unsandboxed execution as a named, per-template, notice-controlled exception is the right product shape.

**Unknown (correctly so, but must stay labeled):** MCP server process containment relative to the Bash sandbox (§17.3, open); whether managed settings can be enumerated without a paid turn; built-in Read/Grep/Glob propagation being best-effort (Sol POL-001, retained via assurance labels); memory/process ceilings on macOS.

**Additional scenarios to add to §9.5 / cohort tests:**
1. *Worker-created hard links inside writable scratch pointing at outside inodes* — later manager materialization or artifact copying could exfiltrate content the read policy never granted. Mitigation: reject `nlink > 1` (or cross-device provenance) during materialization. (C2/C4.)
2. *Process signaling*: §7.3 names it a separate dimension but no schema field, sandbox mapping, or probe covers whether a sandboxed worker can signal unrelated user processes. Add to the C3 probe list and give it an `unknown` assurance label until observed.
3. *Env-var redirection is advisory*: `_scratch_env` (`runtime_policy.py:151-160`) redirects TMPDIR/caches, but tools that ignore those variables will write project-locally; §9.1 declares this an `explain` incompatibility — ensure the C3 probe includes at least one tool known to ignore `TMPDIR`.

**Must be tested before any activation:** the C1/C3 probe lists in §14.2 are adequate; add the three items above.

## 6. C0 plan corrections (task-by-task)

- **Task 1:** State whether the alias is a key in `fixture["profiles"]` (recommend: yes, holding strict-readonly's values). Note the fixture's intentional thinness (flags only). No other change; the snippet's `resolve_profile` arity and field names match `profiles.py:229-337`.
- **Task 2:** (CA-001) define path detachment before hashing + the two hash RED tests; (CA-002) fix `resources` defaults; (CA-003) settle `CONFIRMATION_MODES`; (CA-006) define or forbid non-empty `templates`; (CA-012) add the cross-field normalize/reject table; decide notices-in-hash (CA-001 tail). Clarify whether `system_input_hashes: []` counts as "known" for `cache_inputs_complete` (recommend: no — empty is unknown, absent-by-default).
- **Task 3:** Specify how preset roots are represented unbound (symbolic placeholders), and that presets carry no absolute paths. State the preset `version` increments whenever a later cohort changes a preset document (activation of `commands` at C3 *will* change hashes — say this now so it isn't read as a regression). Add the assurance mapping location (CA-008).
- **Task 4:** (CA-004) add `unknown` production and `unavailable` ordering; (CA-005) deny atoms + root-referenced-allow invariant; (CA-009) governing-side rule; (CA-013) sandbox.mode/memory.mode comparators and the allowlist→unrestricted test. State that preset-to-preset diffs yield `cache_impact: unknown` (null model/effort/runtime), and that the "unchanged cache" test must construct fully-specified policies — otherwise a worker will write a test that can't pass.
- **Task 5:** Define where assurance labels come from (CA-008). Add a test that the explain JSON's `unresolved` list includes any CA-004-unresolved dimension.
- **Task 6:** Fine as written; optionally add `--compare-policy-file` for custom↔custom diffs (later is acceptable). `PRESET_IDS` including the alias in `choices` is correct for compatibility.
- **Task 7:** Rewrite Step 1 per CA-007 (in-process invocation for patch-based proofs; define "does not call C0" as patched-symbol assertions; keep the subprocess-level `args_log`/state-absence proofs).
- **Task 8:** No change. The `check_state.py` four-expired-records carve-out is correctly scoped.

## 7. First-release versus later matrix

| Change | Timing |
|---|---|
| CA-001 hash/path detachment; CA-002 resources defaults; CA-003 confirmation enum; CA-004 unknown/unresolved; CA-005 deny atoms + root-bound allows; CA-006 template decision; CA-007 Task-7 harness; CA-008 assurance source; CA-009 notice governance; CA-012 cross-field table; CA-013 comparators/tests | **C0 blocker** (all are plan/proposal text plus tests; no architecture change) |
| CA-010 registry identity in policy; CA-011 `once` semantics; root-binding identity in `context_change`; migration seam decision; exposed-but-denied fixture split; version-namespace labeling | **pre-first-release** (C1–C3, before the affected surface activates) |
| Hard-link materialization check; process-signaling probe; TMPDIR-ignoring runner probe; `--compare-policy-file`; atom append-only stability guarantee; multi-artifact outputs; Linux matrix | **later** |

Dependency ordering: CA-001/002/003/006 gate everything (frozen schema v1); CA-004/005/013 gate the diff contract; CA-007/008/009/012 gate only C0 execution quality and can land in the same plan revision.

## 8. Alternative architecture assessment

- **Keep fixed version-3 profiles with narrow corrections:** Rejected. The probe already falsified the exact-tool MCP interface as the normal workflow, and the v3 contract cannot express declared roots, notices, or sandbox fallback without per-profile prose duplication — the profile-explosion path §16 correctly rejects. Lifecycle cost exceeds C0's.
- **Expose Claude settings directly:** Rejected. `--settings` merges with inherited layers and array-valued keys concatenate (reported; also acknowledged at `runtime_policy.py:221-223`), so raw settings cannot be the auditable requested-authority contract. The provider-neutral schema is the thing that makes preflight-vs-observed comparison possible at all.
- **Always fresh session across profile changes:** Rejected as a *categorical* rule — it is a stakeholder decision, and rev 3's compromise (permit, notice, always record) is coherent *provided* CA-005/CA-009 land, since those are the two holes through which a broadening resume could pass unnoticed. The Sol POL-003 residual risk (contaminated context gaining effect authority) is real but is now an operator-informed choice with an audit trail, which is the approved product stance; the fresh-session *recommendation* path in §11.2 preserves the safety valve.
- **Container/second OS sandbox:** Rejected for now. It would trade the known native-sandbox gaps (best-effort built-in reads, MCP placement) for a much larger unowned surface (image lifecycle, volume mapping, credential plumbing) and would still not govern built-in file tools, which run in the Claude process. §15's C6 "stronger container/VM isolation" is the right deferral.
- **Skip C0; ship one thin end-to-end review profile:** Tempting but wrong here: the probe showed the failure mode lives in the *contract semantics* (exposure vs authority), not in plumbing. A thin vertical slice would re-encode ad-hoc comparison logic that C1–C6 would then have to unwind. C0's evidence burden (pure functions, no paid calls) is genuinely lower. Keep C0 — but hold it to the corrections above precisely *because* everything else will sit on it.

## 9. Residual risks and open questions

- The plan's 195-test PASS baseline and `check_state.py` carve-out are reported, not re-observed in this audit (shell revoked).
- Whether Claude Code exposes effective managed settings without a paid turn (§17.3) remains the pivotal unknown for C1's `preflight-assessed` honesty.
- MCP process placement relative to the sandbox remains unknown and correctly blocks strict-profile MCP admission.
- The unattended handling of `confirmation: ask` (block vs deny vs fail) is deferred to callers; it must be pinned before C5.
- Cache expectations will be `unknown` for all preset-only workflows until runtime version/model/effort are bound at invocation; operators should be told this is expected, not a defect.
- `PROFILE_VERSION` (legacy) and preset versions will diverge visibly once C1 wires the new core into `run`; the transition story for `metadata.json` (`profile_version` gate at `claude_delegate.py:1132-1143`) belongs in the C1 plan and is currently unwritten.

## 10. Minimum approval conditions

C0 may proceed once a single plan revision (plus two small proposal touch-ups) lands:

1. **Proposal edits (2):** reconcile §9.6's confirmation modes with §18/`CONFIRMATION_MODES` (CA-003); fix the §18 `resources` default so absence is not unbounded authority (CA-002).
2. **Plan edits:** hash/path-detachment specification and RED tests (CA-001, including the notices-in-hash decision); `unknown`/`unavailable` diff semantics with RED test (CA-004); deny-atoms + root-referenced-allow invariant (CA-005); templates-empty-in-v1 or a typed element (CA-006); Task 7 in-process harness wording (CA-007); assurance-mapping location (CA-008); notice-governance rule (CA-009); cross-field normalize/reject table (CA-012); the three comparator/test additions (CA-013).
3. **Re-hash** the revised plan (and proposal if touched) and record the new hashes in the plan's status block; no re-audit is required if the changes are confined to the items above.

Everything else in this report is pre-first-release or later hardening and does not gate C0.
