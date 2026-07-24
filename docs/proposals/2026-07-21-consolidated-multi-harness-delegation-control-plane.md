# Proposal: consolidate delegation-triage into a multi-harness control plane

- **Date:** 2026-07-21
- **Status:** draft for stakeholder ratification; no implementation or activation authorized
- **Selected direction:** one delegation product with a versioned Signal Layer dependency
- **Recommended release posture:** local-first, distributable by design; stakeholder ratification
  remains open
- **Closure target:** an accepted product boundary and staged authorization plan, not a router
  implementation
- **Audience:** maintainers of delegation-triage, Signal Layer, and provider-specific harness
  adapters
- **Post-read action:** accept, revise, park, or reject the product boundary and the Phase 0/1
  authorization request in section 14
- **Authority:** documentation only. This proposal does not authorize installation, deployment,
  routing changes, external model calls, telemetry migration, monitoring, deletion, or cleanup.

## 1. Decision requested

Ratify **delegation-triage as the canonical product and routing-domain authority**, with:

1. a provider-neutral policy and resolver core;
2. provider- and harness-specific adapters for native Codex, Claude, and Gemini/Antigravity
   routes;
3. a first-class orchestration-learning component owned by delegation-triage;
4. Signal Layer as a versioned dependency for generic append-only evidence mechanics and authored
   observation → interpretation → intervention → outcome chains;
5. generated, stamped, drift-checked deployments instead of independently edited installed
   copies; and
6. manual and recommendation-only routing before any separately authorized automatic mode.

This is **Option 2** from the 2026-07-21 consolidation audit. It rejects both continued
installation-by-installation patching and a monorepo that would merge generic Signal Layer
concerns into the routing product.

If ratified, this proposal supersedes the *deferral decision* in the
[provider-neutral router proposal](2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md),
but preserves that proposal's adapter invariants, authentication boundary, and requirement that
the router not impersonate provider enforcement. It does not supersede the existing Claude,
policy-core, or Antigravity proposals; those become implementation lineage and migration inputs.

## 2. Claim labels and source posture

This proposal applies the user-level Codex epistemic criteria and the package's own
[epistemic vocabulary](../../EPISTEMICS.md):

- **Observed** means directly inspected in a tracked file, installed artifact, or command result.
- **Source-supported** means the cited document states the claim.
- **Inference** means a conclusion drawn from observations; it is not stated directly by a
  source.
- **Recommendation** means a proposed design or action.
- **User decision** means the stakeholder selected Option 2 on 2026-07-21.
- **Open decision** means the proposal deliberately does not choose for the stakeholder.

The proposal uses *corroborated for a named decision*, never universal proof. Provider capability,
model quality, cost, cache, permission, and availability claims remain bounded by provider,
version, harness, transport, profile, environment, and date.

## 3. Source and dependency map

### 3.1 Normative delegation-triage sources

| Source | Role in this proposal |
|---|---|
| [README](../../README.md), especially “How to read this repo” and “The discipline” | Establishes the current canonical package, five operational surfaces, and evidence-graded route loop. |
| [CONTRACT](../../CONTRACT.md) §§1–6 | Supplies the whether-to-delegate test, control-surface distinction, fit-line contract, precedence, and feedback loop. |
| [ROUTES](../../ROUTES.md) | Supplies the current Claude-family task ontology and evidence-backed route priors; it is not treated as a provider-neutral catalog. |
| [STATE](../../STATE.md) | Supplies the volatile-fact and expiry model: expired state becomes Unchecked rather than silently remaining true. |
| [WARRANTS](../../WARRANTS.md), especially W-018 and W-019 | Supplies typed evidence, explicit falsifiers, curated-prior posture, and minimum flip discipline. |
| [EPISTEMICS](../../EPISTEMICS.md) | Supplies the package's claim labels and bounded corroboration vocabulary. |
| [Probe contract](../../probes/README.md) and [known weaknesses](../../probes/KNOWN-WEAKNESSES.md) | Supply attestation, tally, negative-evidence, provenance, inheritance, and route-drift failure modes. |
| [Agent deployment manifest](../../agents/MANIFEST.md) | Supplies the current hash-stamped deployment intent and documents known deployment drift. |
| [ROADMAP](../../ROADMAP.md) | Supplies existing open probes and deferred-work discipline; it will require revision after ratification. |
| [LINEAGE](../../LINEAGE.md) | Connects the package to its accepted SEAS canonical-home decisions. |

### 3.2 Existing proposals and implementation evidence

| Source | Dependency or constraint carried forward |
|---|---|
| [Cross-runtime routing and Claude delegation](2026-07-17-cross-runtime-routing-and-claude-delegation.md) | One canonical doctrine, planned/requested/observed provenance, content-free events, bounded manager state, recovery, and root disposition. |
| [Capability-based Claude execution profiles](2026-07-19-capability-based-claude-execution-profiles.md) | Semantic authority profiles, workspace bindings, warnings rather than paternalistic prohibitions, and runtime assurance distinct from requested policy. |
| [Composable Claude capability and scope policy](2026-07-20-composable-claude-capability-and-scope-policy.md) | Provider-neutral policy identity, private bindings, directional policy comparison, cache-affecting changes, and provider-specific compilation. |
| [C0 package-boundary amendment](../reviews/2026-07-20-c0-provider-neutral-package-boundary-amendment.md) | Keeps pure policy primitives separate from Claude presets and runtime behavior. |
| [C0 execution record](../reviews/2026-07-20-c0-policy-core-execution-record.md) | Establishes that the policy core exists but is uninstalled and non-activating; records validator gaps and independent remediation. |
| [Deferred multi-harness router](2026-07-20-provider-neutral-multi-harness-delegation-router-deferred.md) | Supplies the common adapter operations, provider/authentication separation, and reopening conditions. |
| [Gemini Flash adapter proposal](2026-07-20-codex-managed-antigravity-gemini-flash-adapter.md) | Supplies the Antigravity boundary, model discovery, provider-specific assurance, generated-state limits, and stepping-stone architecture. |
| [Gemini Flash MVP execution record](../reviews/2026-07-20-gemini-flash-mvp-execution-record.md) | Establishes one usable but deliberately incomplete adapter and records late telemetry capture and unknown observed provider identity. |
| [Cross-runtime cold-reader review](../reviews/2026-07-17-cross-runtime-routing-proposal-review.md) | Supplies prior corrections concerning canonicality, provenance, isolation, lifecycle, and phased authorization. |
| [Composable-policy Fable audit disposition](../reviews/2026-07-20-composable-claude-capability-and-scope-policy-fable-audit-disposition.md) | Supplies already-dispositioned architecture, authority, portability, and observability challenges. |

### 3.3 Accepted external lineage

- [SEAS ADR-0022](https://github.com/loganrooks/SelfEvolvingAgentialSystems/blob/main/decisions/ADR-0022-delegation-triage-offshoot-adoption.md)
  adopts the pace-layered package, evidence loop, expiry semantics, and canonicality inversion.
- [SEAS ADR-0024](https://github.com/loganrooks/SelfEvolvingAgentialSystems/blob/main/decisions/ADR-0024-delegation-triage-home-and-stage2-execution.md)
  selects this dedicated repository as the platform-agnostic home with per-platform adapters.
- [Signal Layer design](https://github.com/loganrooks/signal-layer/blob/main/signal/DESIGN.md),
  especially §§2, 3, 5, 7, and 8, supplies append-only evidence mechanics, separation of
  observation from interpretation, reflexivity guards, code/data-plane separation, and the
  declared intellectual lineage.

### 3.4 Local operational inputs that are not durable dependencies

The audit also inspected the installed orchestration-learning skill and event schema, Codex
harness observability documentation, the live Claude observability read contract, Codex OTel
status, and a local untracked Signal Layer companion design dated 2026-07-13. These are
**operational evidence and deliberative input**, not portable dependencies. The companion design
is explicitly unratified and therefore cannot settle code ownership. Any accepted content from
these sources must be promoted into tracked specifications, fixtures, or migration records before
implementation relies on it.

## 4. Observed problem

### 4.1 Canonical intent does not currently guarantee canonical operation

**Observed:** the README and SEAS ADRs name this repository as canonical; the installer copies
selected files to consumer locations and asks a maintainer to paste hashes into the manifest.
The current manifest itself describes manual deployment and records an unreconciled Cowork fork.
The Codex target emits guidance rather than installing a versioned Codex package.

**Observed during the 2026-07-21 audit:** the installed Claude deployment had 35 of 61 checked
files missing or different from the working repository. Individual files did not drift in one
direction: some installed surfaces matched the repository while route, state, warrant, and agent
surfaces differed from one another.

**Inference:** repository canonicality is presently a social declaration plus a partial checksum
workflow. It is insufficient to ensure that a running harness consumes one coherent release.

### 4.2 Provider routes are adjacent vertical slices, not one product

**Observed:** the repository now contains a shared C0 policy core, a substantial Codex-managed
Claude adapter candidate, and a minimal Antigravity adapter. Native Codex subagents remain governed
by a separately installed Codex skill rather than the repository's route/state/warrant surfaces.

**Source-supported:** the deferred-router proposal named multiple stable adapters, recurring
manual selection cost, duplicated lifecycle code, comparable evidence, and a third provider or
native harness as reopening triggers. At least manual-selection friction, duplicated concepts,
and the third-harness condition are now present. Runtime stability remains uneven.

**Recommendation:** reopen the router design now, but stage implementation so unstable provider
capabilities do not become false universal abstractions.

### 4.3 Observability is useful but fragmented

**Observed during the audit:** the orchestration-learning store passed its integrity audit with
221 events across 100 runs. The refreshed projection contained 93 route-planned and 96 disposition
events. It also reported 26 unknown route-provenance cases, 24 validator gaps, 8 schema-drift
events, and an unset retention policy.

**Observed:** Codex semantic harness events, Codex OTel, Claude spawn/signal data, manual probe
records, and orchestration-learning events use separate writers and projections. The Gemini MVP
record explicitly says its route and disposition events were written together after integration,
so their timestamps do not establish the actual decision sequence.

**Inference:** there is no single cross-platform chain from task classification through requested
route, observed execution, validation, disposition, later defect evidence, and governed policy
change.

### 4.4 Evidence and doctrine can lag one another

**Source-supported:** CONTRACT §6 requires post-mortems to update routes, warrants, state, and
probe records in the same pass. The probe discipline says n=1 never flips a route and requires
attestation and a tally.

**Observed:** the working tree contains uncommitted adapters, plans, reviews, and probe evidence,
while the released README still identifies version 0.3.0 and the public roadmap predates much of
the current design work. Uncommitted work may be more recent or more researched, but it is not a
release and cannot safely be treated as canonical.

## 5. Product boundary

### 5.1 Delegation-triage owns the routing domain

The canonical product owns:

- task classification and task-packet contracts;
- route policy, provider-neutral capability requirements, and validation requirements;
- warrants, provider/model evidence, flip conditions, and probe registrations;
- provider/harness adapter protocol and adapter manifests;
- route resolution and explanation;
- delegation lifecycle, result, reconciliation, and disposition envelopes;
- orchestration-learning mechanical event schema and diagnostics;
- deployment generation, release manifests, drift checks, rollback receipts, and release channels;
  and
- privacy and retention policy for delegation-domain events.

### 5.2 Signal Layer owns generic epistemic infrastructure

Signal Layer remains a separate repository and owns:

- generic append-only authored Signal events;
- observation/interpretation/intervention/outcome separation;
- sole-writer, idempotency, append, projection, and schema-evolution mechanics that are truly
  domain-independent;
- generic evidence references and pull-based diagnostic surfacing; and
- the reflexivity and anti-metric-fixation guards of its design.

Delegation-triage may depend on a versioned Signal Layer library or command interface. Signal
Layer does not own provider catalogs, routing policy, task classes, adapter semantics, or policy
promotion rules. Conversely, delegation-triage does not fork Signal Layer's generic authored
ledger.

### 5.3 Data stays local by default

The first release uses a local private data plane. It does not require a central database,
cross-machine synchronization, remote telemetry, transcript capture, or Dionysus integration.
Provider-specific raw logs retain their own private lifecycle and do not enter the portable
learning ledger.

A future exporter may send allowlisted, pseudonymous mechanical events only after a separate
privacy, retention, identity, and failure-mode proposal. Cross-project aggregation is not a
prerequisite for a coherent local product.

## 6. Canonical source, release, and deployment model

### 6.1 Canonicality is promotion, not recency

The newest file, latest probe, or most recently researched branch is a **candidate**, not the
canonical policy. A candidate becomes canonical only through this sequence:

1. record the observation and its provenance;
2. separate interpretation and alternative hypotheses;
3. run the warranted falsification or paired probe when the decision requires it;
4. update the affected warrant and candidate policy together;
5. obtain the required human or maintainer disposition;
6. merge a coherent change into the canonical branch;
7. mint a versioned release manifest; and
8. generate and validate consumer deployments from that release.

No telemetry reducer, provider adapter, or installer may promote policy automatically.

### 6.2 Structured authority and human-readable projections

**Recommendation:** introduce a small versioned structured policy source for fields that require
machine consistency:

- route and task-class IDs;
- required capabilities and validation class;
- provider/harness/transport selectors;
- profile and authority identities;
- warrant references;
- fallback behavior; and
- volatile capability facts with observation and expiry metadata.

Human-readable route and state tables remain first-class review surfaces, but deterministic checks
must be able to establish that coupled fields agree. Warrants remain authored evidence records;
they are not flattened into an opaque score.

The exact representation—JSON, TOML, or a constrained Markdown-plus-sidecar format—is an open
implementation decision. Phase 0 must compare migration cost, reviewability, deterministic
rendering, and diff quality before selecting it.

### 6.3 Release manifest

Every release records:

- core policy version and semantic hash;
- warrant-set and task-ontology versions;
- adapter protocol version;
- included adapter versions;
- generated artifact hashes;
- supported schema versions and migration readers; and
- minimum compatible Signal Layer interface.

Dirty or uncommitted candidates cannot be installed as a stable release. They may be installed
only through an explicit development or preview channel whose manifest names the source revision
and dirty-state digest.

### 6.4 Deployment manifest and drift behavior

Each installed target records:

- release and adapter versions;
- policy and artifact hashes;
- capability snapshot and observation time;
- active overlay and its precedence;
- installation and verification receipts;
- reload or restart requirement and completion state; and
- local deviations, if permitted.

The deployment manager supports `plan`, `apply`, `check`, and `rollback`. Apply is transactional:
stage, validate, atomically activate, run target checks, and retain a bounded rollback receipt.

Drift produces a contextualized warning by default. Integrity contradictions—such as one target
claiming a release while its hashes differ—produce a degraded status and require explicit
operator acceptance before recommendation-only or automatic routing relies on that target.
Warnings may be configured or disabled; the system does not prohibit an informed operator from
continuing.

## 7. Provider-neutral routing without false equivalence

### 7.1 Three independent layers

Routing is resolved from:

1. **Task policy:** task class, risk, required judgment, information channel, authority, output,
   and validation contract.
2. **Provider/model evidence:** model family, exact model identifier, effort/thinking controls,
   strengths, weaknesses, cost or quota class, evidence grade, scope, expiry, and falsifier.
3. **Installed route manifests:** host harness, transport, provider adapter, authentication and
   billing class, exact discoverable models, tools, permission controls, lifecycle features, and
   assurance level available in this environment.

A model family is not a route. `Sonnet through native Claude Code`, `Sonnet through a Codex-managed
Claude process`, and a foreign model exposed through another harness are distinct routes even if
their marketing model name matches.

### 7.2 Adapter contract

Every adapter remains directly invocable and implements the portable lifecycle already proposed:

| Operation | Portable contract |
|---|---|
| `doctor` | Report installed runtime, authentication class, exact models, supported controls, capability freshness, and degradation without generating model work. |
| `compile` | Convert task policy and private bindings into a provider request while reporting unresolved dimensions. |
| `start` | Create one durable attempt with planned and requested provenance. |
| `observe` | Report sanitized lifecycle and independently observed facts without copying requested facts into observed fields. |
| `resume` | Continue a compatible semantic task and warn about profile, model, authority, and cache consequences. |
| `materialize` | Write one accepted result to an exact manager-owned artifact boundary. |
| `reconcile` | Compare declared ownership and effects with observed project and provider state. |

Provider-specific residue stays in the adapter. If adding a provider repeatedly requires changes
to the provider-neutral reducer or task policy schema, the adapter boundary has failed and must be
reconsidered.

### 7.3 Capability and model discovery

Adapters publish time-bounded manifests rather than relying on a static global model list. Each
claim records:

- `documented`, `requested`, `observed`, `derived`, `unknown`, or `unavailable` source status;
- provider, harness, transport, adapter, and runtime version;
- observation timestamp, `valid_until`, and recheck trigger;
- assurance boundary for filesystem, network, tools, external writes, descendants, and host
  effects; and
- the evidence or probe supporting the claim.

The resolver only recommends among currently compatible manifests. Missing evidence remains
unknown; it is not converted into permission, denial, or provider equivalence.

### 7.4 Routing modes

- **Manual:** enumerate compatible routes and explain differences; the operator chooses.
- **Recommendation-only:** rank compatible routes under an explicit objective and show the
  warrants, uncertainty, cost/quota posture, and fallback.
- **Automatic:** separately proposed and authorized only after recommendation quality, override
  behavior, failure recovery, and rollback pass a pre-registered pilot.

Manual direct adapter invocation remains available in every mode.

## 8. Cross-platform observability and orchestration learning

### 8.1 One mechanical event contract

Delegation-triage promotes the useful parts of the current orchestration-learning schema into a
versioned product component. Provider and harness heads translate local envelopes into a common
allowlisted event family:

- `route_planned`;
- `route_requested`;
- `attempt_started`;
- `attempt_observed` or checkpoint;
- `consultation`;
- `validation_observed`;
- `disposition`;
- `outcome_followup`; and
- `deployment_health` or capability-drift observations.

Planned, requested, observed, validated, and accepted identities remain separate. Late capture is
marked late; timestamps are never rewritten to imply causal order.

### 8.2 Privacy boundary

The portable ledger stores no prompt text, transcript text, assistant messages, command text,
tool input/output, stdout/stderr, raw hook payload, secrets, credentials, account identity, or raw
filesystem paths. It stores bounded categorical facts, numeric measurements exposed directly by
the provider, versioned pseudonymous identifiers, missingness, and typed receipts.

Capture failure never blocks primary work. It returns a degraded receipt and leaves an auditable
gap. Unknown provider fields reject or degrade at the adapter boundary rather than entering the
core unchecked.

### 8.3 Mechanical evidence is not interpretation

Reducers may produce descriptive cohorts with denominators, missingness, confounders, and
assurance coverage. They may not author a mechanism, universal model ranking, policy verdict, or
route edit.

The learning loop is:

1. mechanical event or diagnostic;
2. authored Signal observation;
3. competing interpretations and mechanism hypotheses;
4. proposed intervention with predicted effects and rollback condition;
5. human disposition;
6. explicit policy change and versioned release; and
7. later outcome evidence, including escaped defects and regressions.

This boundary preserves Signal Layer's observer-inside-the-system and metric-fixation cautions
while keeping routing-domain authority in delegation-triage.

### 8.4 Retention and derived state

Phase 1 must choose retention for mechanical, derived, provider-local, and authored lanes. Derived
projections are rebuildable and never the source of truth. Retention expiration, compaction, or
migration may not silently erase the evidence needed to reconstruct an active policy decision.

Cross-project export remains off until pseudonym-key ownership, erasure, re-identification risk,
schema compatibility, and failure recovery receive separate approval.

## 9. Epistemic and research programme

The product must be engineered in dialogue with relevant technical and philosophical work without
turning literature names into decorative authority.

### 9.1 Existing commitments carried forward

- Fallibilism: routes are defeasible priors with explicit flip conditions.
- Severe testing: evidence is useful when the check could have exposed a named error.
- Pace layering: doctrine, route policy, volatile capability state, and runtime events change at
  different rates.
- Reflexivity: the router and its metrics are part of the system they influence.
- Mechanism pluralism: observations do not arrive pre-interpreted; alternatives and residue stay
  visible.
- Anti-Goodhart posture: cost, latency, acceptance, and token counts are diagnostics, not single
  optimization targets.
- Situated capability: model performance is conditioned by task, harness, tools, authority,
  context, validation, and operator objective.

These commitments are source-supported by the package's warrants and Signal Layer design. The
Signal Layer design's §8 lineage points to cybernetics, unanticipated consequences, metric
fixation, mechanism accounts, hermeneutics, robustness, and leverage points, but it explicitly
says fuller research remains pending. Therefore those names are orientation, not load-bearing
evidence in this proposal.

### 9.2 Required research practice

Before a theoretical claim changes product behavior, maintainers must create a bounded claim
record containing:

- the primary source and exact claim;
- the proposed translation into a design or routing hypothesis;
- rival interpretations and scope limits;
- an observable implication or falsifier;
- the operational decision the claim could change; and
- the evidence threshold for promotion.

Empirical model comparisons require matched task packets, harness and authority accounting,
independent validation, missing-data disclosure, and later-defect follow-up. Sparse heterogeneous
runs may generate hypotheses; they do not license universal model rankings.

### 9.3 Research agenda

The initial literature and design review should cover, without assuming agreement among them:

- decision theory under uncertainty and value of information;
- experimental design, sequential evidence, heterogeneous treatment effects, and evaluator noise;
- human-in-the-loop automation and calibrated reliance;
- capability-based security, policy compilation, and assurance cases;
- event sourcing, provenance, reproducible deployment, and schema evolution;
- cybernetics and second-order observation;
- Goodhart/Campbell-style metric effects and specification gaming;
- philosophy of scientific mechanisms, robustness, and situated knowledge; and
- organizational learning, incident analysis, and safe rollback.

This agenda is a research workstream, not an excuse to delay reversible engineering that has
already met its decision threshold.

## 10. User experience and maintainability

The product should expose a small operator surface:

- `doctor` — what is installed, fresh, compatible, degraded, or unknown;
- `route` — classify and explain compatible choices;
- `delegate` — execute one explicit route or accept a recommendation;
- `status` — show lifecycle, validation, and disposition without content leakage;
- `resume` — continue with cache/profile/authority warnings;
- `evidence` — show the warrant and bounded outcome basis;
- `deploy plan|apply|check|rollback` — manage stamped installations; and
- `learn audit|diagnose` — inspect event integrity, cohort coverage, and open hypotheses.

Progressive disclosure keeps routine use short while making provenance, assurance, and low-level
diagnostics available. Warnings are contextual and configurable. They do not infantilize users or
silently override explicit choices.

Provider adapters share a conformance kit but may expose provider-specific diagnostics. The core
must not become a least-common-denominator shell that hides useful native capabilities.

## 11. Migration from current state

Migration is additive and reversible:

1. **Inventory:** record the canonical commit, dirty candidate surfaces, installed target hashes,
   provider runtimes, live skill versions, event-store schemas, and current retention state.
2. **Stabilize lineage:** disposition and commit coherent existing Claude, C0, and Gemini work;
   do not release directly from the current mixed worktree.
3. **Define compatibility:** version the adapter and event protocols; add dual-read fixtures for
   existing orchestration-learning events and current adapter records.
4. **Build deployment health first:** make release and installed drift visible before changing
   route behavior.
5. **Preview channel:** install a stamped preview beside or over the current target with an exact
   rollback receipt and reload instructions.
6. **Manual router:** discover manifests and explain routes without automatic selection.
7. **Automatic event capture:** wire adapter lifecycle boundaries to the mechanical recorder;
   compare automatic records with current manual records.
8. **Recommendation pilot:** run pre-registered representative cohorts with explicit overrides
   and root validation.
9. **Stable promotion:** only after compatibility, privacy, rollback, and pilot exit criteria pass.

No migration rewrites or deletes the existing ledgers. Legacy readers remain available until a
separate migration record demonstrates history, identity, projection, privacy, and rollback
preservation.

## 12. Options rejected or deferred

### 12.1 Continue patching installed skills

Rejected as the product architecture. It is fast for one incident but retains divided ownership,
manual coupling, and silent cross-surface drift.

### 12.2 Merge delegation-triage and Signal Layer into one repository

Rejected for now. A monorepo would centralize location while coupling provider routing, generic
epistemic infrastructure, authored signals, and runtime data lifecycles. A versioned interface
gives one routing authority without one undifferentiated codebase.

### 12.3 Build automatic cross-provider routing first

Deferred. The observed adapters have different maturity and assurance. Automatic selection before
deployment health, common provenance, and recommendation evidence would automate uncertainty
rather than manage it.

### 12.4 Central hosted telemetry

Deferred. A local-first mechanical ledger and authored Signal bridge can answer the first product
questions without introducing credential, privacy, retention, synchronization, and service
operation requirements.

## 13. Risks, mitigations, and falsifiers

| Risk or disconfirming observation | Mitigation or decision consequence |
|---|---|
| The shared core must change whenever a provider adapter is added. | Narrow the protocol or split the supposedly portable field; repeated firing falsifies the adapter boundary. |
| Routing metadata and ceremony cost more than delegation saves. | Measure decision latency and maintenance work; remove fields or stop the pilot if repeated use does not amortize the burden. |
| Cohorts remain too sparse or heterogeneous to support recommendations. | Keep manual routing and curated warrants; do not manufacture rankings. |
| Generated projections become harder to review than the current Markdown. | Preserve human-authored evidence, test deterministic rendering, and retain a rollback path to the current surfaces. |
| Provider capability discovery becomes stale or overclaims assurance. | Time-bound every capability, report unknown separately, and require dated runtime probes for enforcement claims. |
| Telemetry changes behavior or encourages metric gaming. | Keep observations separate from interpretation, use multiple outcomes, preserve negative evidence, and prohibit automatic policy mutation. |
| A privacy fixture appears in a portable event or diagnostic. | Stop activation, preserve the failing fixture, repair the allowlist boundary, and rerun the privacy suite before resuming. |
| Signal Layer integration creates recurring cross-repository release blocks. | Reduce the dependency to a stable generic interface or vendor a reviewed compatibility shim with explicit lineage; do not fork silently. |
| Operators routinely bypass the router because direct adapters are clearer. | Treat bypass as product evidence; simplify the router rather than prohibiting direct invocation. |
| Drift warnings are ignored or too noisy. | Separate integrity contradictions from informational change, allow warning configuration, and measure whether checks prevent actual misroutes. |

The pilot fails if, after a pre-registered operating window, it does not reduce at least one of:
route ambiguity, provenance loss, deployment drift, validator gaps, or repeated integration work—
or if it creates greater maintenance and review cost than the failures it prevents.

## 14. Phased authorization

### Phase 0 — ratification and source stabilization

**Requested authorization after proposal review:** documentation and repository hygiene only.

- disposition this proposal and the unratified Signal Layer companion design;
- mark the deferred router proposal as superseded or retained according to the disposition;
- produce an authoritative source/ownership map;
- inventory and disposition the existing mixed worktree into coherent candidate changes;
- define stable, preview, and development release semantics; and
- write an implementation plan with exact files, tests, migration boundaries, and rollback.

No install, activation, provider call, or telemetry migration occurs in Phase 0.

### Phase 1 — deployment integrity and common contracts

Separately authorize:

- release and deployment manifests;
- transactional `plan/check/apply/rollback` behavior;
- adapter and event protocol schemas;
- compatibility readers and fixtures;
- a non-generative `doctor`; and
- drift and reload reporting.

This phase does not change routing decisions.

### Phase 2 — manual multi-harness routing

- adapter discovery for native Codex, Codex-managed Claude, and Codex-managed Antigravity;
- explicit route compilation and direct invocation;
- shared lifecycle/result envelopes; and
- root-controlled validation and disposition.

### Phase 3 — cross-platform learning plane

- automatic lifecycle event capture;
- orchestration-learning migration or compatibility bridge;
- Signal reference bridge;
- retention and privacy enforcement; and
- cohort diagnostics with missingness and confounders.

### Phase 4 — recommendation-only resolver

- evidence-backed route explanation;
- operator objectives and constraints;
- override and counterfactual logging; and
- pre-registered representative pilot.

### Phase 5 — automatic routing, if warranted

Requires a new proposal, security/privacy review, explicit stakeholder approval, rollback, and
evidence that recommendation-only routing is reliable enough for the named task and authority
classes. Automatic policy learning remains out of scope unless separately proposed.

## 15. Verification requirements

Each implementation phase must include:

- schema validation, malformed-input, unknown-field, and compatibility tests;
- privacy fixtures proving forbidden bytes do not enter portable records;
- planned/requested/observed non-aliasing tests;
- provider-head conformance and provider-residue tests;
- deterministic release and deployment-manifest tests;
- interrupted apply and rollback tests;
- stale capability and expiry tests;
- event idempotency, concurrency, partial-write, and projection-rebuild tests;
- root validation and undeclared-effect reconciliation;
- a fresh drift check against actual installed targets when activation is authorized; and
- a reader test showing a new maintainer can add a fixture adapter without changing the core.

Claims about runtime enforcement require dated actual-runtime probes. Fake CLIs corroborate
adapter logic only. Claims about improved routing require comparable quality and later-defect
evidence, not process exit or first-pass acceptance alone.

## 16. Open stakeholder decisions

1. **Release closure target:** local-first and distributable by design, as recommended, or a
   third-party installer in the first release?
2. **Structured source format:** JSON, TOML, or constrained Markdown plus sidecars?
3. **Retention:** duration and size budgets for mechanical, derived, provider-local, and authored
   data?
4. **Pseudonym keys:** ownership, backup, rotation, and erasure behavior?
5. **Release authority:** who may ratify warrants, route changes, and stable releases?
6. **Recommendation threshold:** what pilot horizon and evidence bar permit recommendation-only
   routing for each task/risk class?
7. **Signal Layer interface:** library, command protocol, or compatibility bridge for the first
   release?
8. **Public packaging:** whether orchestration-learning ships as a subpackage, plugin, or both?

Unanswered decisions remain explicit. Phase 0 may research and propose them but may not silently
choose high-impact defaults.

## 17. Recommended disposition

**Accept for architecture ratification and Phase 0 planning, with implementation still gated.**

The existing repository remains the canonical routing home. Signal Layer remains a separate
generic evidence dependency. The current adapters and learning tools become migration inputs,
not competing authorities. The first product milestone should establish deployment integrity,
provider manifests, and one mechanical evidence contract before attempting automatic routing.

## 18. Proposal audit record

The 2026-07-21 proposal audit performed these bounded checks:

| Check | Observation | Scope limit |
|---|---|---|
| Claude deployment check through the repository installer | 61 files checked; 35 reported missing or different | Point-in-time local deployment observation; it may change after a later install. |
| Orchestration-learning ledger audit | 221 events accepted by the version-1 integrity audit | Schema validity does not establish that every route was captured or correctly attributed. |
| Orchestration-learning projection refresh | 100 runs; 93 planned routes; 96 dispositions; 26 unknown-provenance, 24 validator-gap, and 8 schema-drift codes | Descriptive counts from heterogeneous work; not comparative model-quality evidence. |
| Provider CLI presence | Codex, Claude Code, and Antigravity clients were locally available | Presence does not establish authentication, quota, model, permission, or runtime assurance for every route. |
| Proposal relative-link check | 23 relative links resolved | External links and untracked local deliberative inputs were not converted into durable dependencies. |
| Package warrant/link check | Passed: 80 Markdown files, 23 warrant records defined and cited | This checks structural integrity, not substantive truth. |
| Package volatile-state check | Failed only on the four pre-existing July 19 expiries: scarcity mode, fable window, reviewer pin, and orchestrator pin | Those values remain Unchecked; this proposal does not refresh or rely on them. |

No adapter, installation, route, policy, runtime, or telemetry schema was changed by this proposal.
