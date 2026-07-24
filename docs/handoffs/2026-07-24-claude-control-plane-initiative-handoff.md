# Handoff: Claude review of the delegation control-plane initiative

- **Date:** 2026-07-24
- **Status:** ready for Claude Code proposal review; implementation plan not yet authorized by this
  artifact
- **Closure target:** a reviewed and dispositioned product architecture, followed by a separately
  approved implementation plan
- **Immediate product horizon:** Claude Code and Codex
- **Later extension horizon:** additional providers and harnesses through stable adapter contracts
- **Preparation boundary:** documentation and local verification only; no Claude invocation,
  installation, deployment, paid probe, route activation, cleanup, commit, or push was performed
  while preparing this handoff

## 1. Objective

Transfer the initiative to Claude Code with enough repository-grounded context to review the
existing proposals before planning or implementing the next phase.

Claude is not being handed a settled implementation plan. Its first responsibility is to review
the proposal set, identify conflicts and missing requirements, and recommend a coherent revision
that serves the product direction below. Planning and execution follow only after that review is
dispositioned.

## 2. Product thesis

`delegation-triage` should become a mainstream-harness delegation product whose primary value is:

1. a condensed, citable knowledge base of routing claims, warrants, failure modes, and dated
   capability facts;
2. transparent route selection that states the task class, provider, model, effort, harness,
   authority, evidence, uncertainty, and fallback;
3. first-class integration with Claude Code and Codex, including installation, drift checks, and
   readable explanations in both environments;
4. customization through project overlays, operator objectives, and explicitly versioned policy;
5. learning from sanitized delegation events, task traces, validation results, overrides, and
   later defects without treating telemetry as self-authorizing policy; and
6. adaptation to model releases, retirements, pricing changes, harness changes, and accumulated
   local evidence through a governed promotion and rollback process.

The product is not a universal model leaderboard. Capability is situated: task, provider, model,
harness, transport, tools, authority, context, validation, operator objective, and date all matter.

## 3. Required read order

1. Repository operating guidance: [`../../CLAUDE.md`](../../CLAUDE.md).
2. Proposal status and lineage: [`../proposals/README.md`](../proposals/README.md).
3. Leading architecture:
   [`../proposals/2026-07-21-consolidated-multi-harness-delegation-control-plane.md`](../proposals/2026-07-21-consolidated-multi-harness-delegation-control-plane.md).
4. Cross-runtime lineage:
   [`../proposals/2026-07-17-cross-runtime-routing-and-claude-delegation.md`](../proposals/2026-07-17-cross-runtime-routing-and-claude-delegation.md).
5. Capability and authority policy:
   [`../proposals/2026-07-20-composable-claude-capability-and-scope-policy.md`](../proposals/2026-07-20-composable-claude-capability-and-scope-policy.md).
6. Historical profile baseline:
   [`../proposals/2026-07-19-capability-based-claude-execution-profiles.md`](../proposals/2026-07-19-capability-based-claude-execution-profiles.md).
7. Provider-neutral deferral lineage:
   [`../proposals/2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md`](../proposals/2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md).
8. Current operational surfaces: [`../../CONTRACT.md`](../../CONTRACT.md),
   [`../../ROUTES.md`](../../ROUTES.md), [`../../STATE.md`](../../STATE.md),
   [`../../WARRANTS.md`](../../WARRANTS.md), and [`../../EPISTEMICS.md`](../../EPISTEMICS.md).
9. Probe rules and known failure modes: [`../../probes/README.md`](../../probes/README.md),
   [`../../probes/INDEX.md`](../../probes/INDEX.md), and
   [`../../probes/KNOWN-WEAKNESSES.md`](../../probes/KNOWN-WEAKNESSES.md).
10. Implementation evidence:
    [`../reviews/2026-07-20-c0-policy-core-execution-record.md`](../reviews/2026-07-20-c0-policy-core-execution-record.md),
    [`../reviews/2026-07-20-gemini-flash-mvp-execution-record.md`](../reviews/2026-07-20-gemini-flash-mvp-execution-record.md),
    and
    [`../../probes/records/P-20260720-claude-profile-actual-runtime.md`](../../probes/records/P-20260720-claude-profile-actual-runtime.md).

## 4. Proposal review assignment

Review the proposal set before authoring an implementation plan.

### Questions the review must answer

1. Does the consolidated proposal express the product thesis in section 2 without overstating
   current implementation or empirical support?
2. What is the correct separation among:
   - provider-neutral task ontology and policy primitives;
   - provider-specific model evidence and routing priors;
   - harness-specific capability, transport, permission, and lifecycle manifests; and
   - project or operator overlays?
3. Should provider routing be represented as one common task table with provider/harness
   projections, separate provider tables sharing a task ontology and warrants, or another
   reviewable structure? Reject a flattened table if it erases provider or harness conditions.
4. How should Claude Code and Codex consume the same canonical release while retaining native
   controls and useful local interfaces?
5. What minimum installation, release, deployment, drift, rollback, and restart contracts are
   required before either harness can call itself supported?
6. Which existing proposal is authoritative for each requirement, and where do proposals conflict,
   duplicate one another, or leave gaps?
7. Which decisions can be made from current evidence, which require stakeholder choice, and which
   require a dated runtime or comparative probe?

### Review output contract

Write a durable review under `docs/reviews/` containing:

- an overall `accept`, `revise`, `park`, or `reject` recommendation;
- one disposition for every proposal in [`../proposals/README.md`](../proposals/README.md);
- a cross-proposal requirements and supersession ledger;
- findings classified as observed defect, source gap, design risk, stakeholder decision, or
  implementation question;
- a recommended architecture with alternatives and tradeoffs;
- an exact list of proposal sections that must change before planning;
- a boundary between immediate Claude Code/Codex work and later provider extensions; and
- verification performed, unresolved uncertainty, and any additional evidence required.

Do not implement while performing this review. Preserve the current mixed worktree and do not
rewrite historical proposals or evidence to make the lineage look cleaner.

## 5. Multi-provider and multi-harness routing requirement

The next architecture must support different routing views without creating independent,
silently drifting doctrines.

At minimum, distinguish:

| Layer | Owns |
|---|---|
| Task policy | Whether to delegate, task class, risk, required judgment, authority, output, and validation contract. |
| Provider/model evidence | Exact model identity, documented and observed capabilities, cost/quota posture, evidence grade, scope, expiry, weakness, and falsifier. |
| Harness manifest | Installed runtime, transport, authentication class, model availability, effort controls, tools, permissions, lifecycle, observability, and assurance. |
| Route projection | Compatible provider × model × harness choices for a task, with explanation, uncertainty, fallback, and warrant references. |
| Overlay | Project-specific task classes, constraints, objectives, and local evidence under explicit precedence. |

Claude Code and Codex are the immediate supported consumers. Other harnesses should be addable
without changing the provider-neutral core for provider-specific residue. The Antigravity work is
useful migration evidence but is not the immediate product center.

## 6. Installation and release requirement

The current installation surfaces are asymmetric:

- Claude Code receives a copied skill and roster through `install.py claude-code`;
- Codex receives a generated guidance fragment through `install.py codex`;
- the repository's richer Codex-managed Claude adapter is an uncommitted candidate and is not the
  same artifact as the installed user-level preview skill.

The reviewed design must define:

1. one canonical source and versioned release manifest;
2. generated Claude Code and Codex packages or adapters;
3. `plan`, `check`, `apply`, and `rollback` semantics;
4. stable, preview, and development channels;
5. installation receipts, hashes, source revision, dirty-state rules, and capability snapshots;
6. reload or restart requirements and confirmation;
7. drift severity and behavior; and
8. how a consumer reads provider-specific routes and common warrants without copying an
   independently editable policy fork.

Installation and activation remain separate decisions. A successful build or deterministic test
does not authorize deployment.

## 7. Learning and customization requirement

The product should learn from use while keeping observations, interpretations, and policy changes
separate.

Required chain:

1. sanitized mechanical event;
2. validation and later-outcome evidence;
3. authored observation;
4. competing interpretations and confounders;
5. proposed intervention with predicted effects and rollback;
6. human disposition;
7. explicit warrant, route, state, or profile change; and
8. versioned release plus later follow-up.

Portable records must not contain prompt text, transcript text, assistant messages, command text,
tool input/output, secrets, credentials, account identity, or raw filesystem paths. Missingness,
late capture, requested-versus-observed differences, parent-model effects, packet quality, retries,
and validator gaps remain visible.

Customization must support project overlays and operator objectives without allowing a lower-trust
repository to broaden hard authority boundaries or silently activate a new route.

## 8. New-model intake and displacement requirement

Claude Opus 5 is the first required exercise of a reusable model-change workflow. Treat its release
as a candidate and a trigger, not as evidence that every Opus 4.8, Sonnet 5, or Fable 5 route should
change.

The workflow must cover:

1. **Detect:** record the provider announcement, exact model ID, release date, migration guide,
   pricing, lifecycle, and source status.
2. **Manifest:** record provider, harness, transport, runtime version, authentication/billing
   class, available controls, assurance, observation time, expiry, and recheck trigger.
3. **Compatibility:** assess tokenizer, context, output, thinking/effort, tools, caching, refusal,
   fallback, retention, and prompt-behavior changes.
4. **Candidate mapping:** identify the exact task classes and incumbent routes the new model might
   complement, displace, or leave unchanged.
5. **Probe design:** use matched packets, authority, harness, validation, and later-defect
   follow-up. Vendor benchmarks are source-supported inputs, not local route verdicts.
6. **Disposition:** accept for a named route, canary, retain as fallback, park, or reject. Record
   alternatives and remaining uncertainty.
7. **Promotion:** update warrants, routes, state, profiles, manifests, installers, documentation,
   and rollback in one governed release.
8. **Monitor and retire:** schedule rechecks for price, availability, capability, harness support,
   deprecation, and displaced incumbents.

Primary starting sources:

- [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview);
- [What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5);
- [Model IDs and versioning](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions);
- [Claude Code changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).

Current preparation observation: Claude Code 2.1.218 was installed during this audit, while the
official changelog adds Opus 5 support in 2.1.219. Re-check this at takeover time; do not treat the
observation as durable availability.

## 9. Execution-profile requirement

The existing repository candidate has useful named profiles and a composable non-activating policy
core, but routine implementation still maps to `acceptEdits`, while unattended execution maps to
`auto`.

Review and redesign the normal implementation path so task-specific command templates, path
ownership, sandbox/network policy, Git controls, and reconciliation can be compiled without using
`auto` as the default escape hatch. Keep unattended classifier-mediated operation as a later,
separately activated capability.

Task class and worker model selection must remain separate from authority. A profile describes what
the worker may do; the route explains why that model and effort fit the task.

## 10. Skill and harness integration requirement

Review the skill surfaces as product interfaces, not incidental copies:

1. The core `delegation-triage` skill should provide a concise, progressive-disclosure entry point
   into the canonical task policy, provider/harness route projections, volatile state, warrants,
   and feedback contract.
2. Codex's `delegate-to-claude` skill should remain a manager-specific workflow that compiles a
   bounded task packet and authority profile, invokes the Claude adapter, preserves evidence, and
   leaves disposition and final verification with the Codex root.
3. Claude Code should receive native delegation guidance and generated agent/profile definitions
   that use the same canonical release without importing Codex-only orchestration instructions.
4. Installed skill directories must be generated or copied from a versioned source package,
   stamped, drift-checkable, and replaceable through preview/stable channels. They must not become
   independently edited canonical homes.
5. Skill instructions must distinguish routing policy from execution authority, requested from
   observed runtime facts, and deterministic validation from worker self-report.
6. References should expose task-packet, profile, recovery, model-intake, installation, and
   evidence-writing procedures without making the always-loaded skill body a second monolithic
   manual.

The review must identify which skill assets belong in the provider-neutral core, the Claude Code
adapter, and the Codex adapter, and how their generated documentation stays mutually consistent.

## 11. Known outstanding state

1. `check_state.py` currently fails on four entries that expired 2026-07-19: scarcity mode, the
   Fable window, reviewer pin, and orchestrator pin. Expired values are Unchecked and the documented
   fallbacks govern.
2. The working tree is a mixed, uncommitted candidate containing adapters, policy code, proposals,
   reviews, plans, probes, fixtures, generated bytecode, and tracked documentation changes.
3. The leading consolidated proposal remains unratified.
4. The current Claude deployment drift check reported 35 of 61 files missing or different.
5. The Codex user-level preview skill and repository adapter are different implementations with no
   canonical installation path between them.
6. The version-3 Claude profile runtime probe has not executed a worker turn; runtime permission,
   sandbox, MCP, and materialization claims remain incomplete.
7. A stale `codex/delegate-phase1a` worktree registration is marked prunable. Preserve it until its
   branch and evidence are dispositioned.
8. The current README still contains historical authorization language that must be reconciled
   after proposal review rather than silently edited into a new decision.

## 12. Planning and later execution boundary

After the review is accepted:

1. revise and ratify the consolidated proposal;
2. inventory and disposition the mixed worktree into coherent candidate changes;
3. author root-owned implementation plans with exact files, tests, migration boundaries, and
   rollback;
4. give Claude workers bounded execution packets rather than asking them to recreate the plan;
5. use isolated worktrees for independent writers;
6. require specification review before quality review for every implementation slice;
7. keep paid retry, installation, activation, route promotion, commit, and push decisions explicit;
   and
8. verify the integrated result from the canonical repository, not from worker summaries.

The transfer to Claude Code changes who drives the next session. It does not itself settle open
architecture, authorize automatic learning, or promote Opus 5 into the routing table.
