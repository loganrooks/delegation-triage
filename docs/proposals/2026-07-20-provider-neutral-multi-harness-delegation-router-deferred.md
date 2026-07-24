# Deferred proposal: provider-neutral, multi-harness delegation router

- **Date:** 2026-07-20
- **Status:** deferred design direction; not approved for implementation
- **Audience:** future maintainers of the delegation core and provider adapters
- **Closure target:** a compatibility boundary that current work can preserve without building the
  router
- **Authority:** documentation only; no implementation, installation, deployment, route change,
  paid model call, credential change, or policy activation
- **Reopen when:** at least two provider adapters are stable enough that manual selection,
  duplicated lifecycle code, or cross-provider measurement is a demonstrated operational cost

## 1. Decision

Preserve a path to a provider-neutral delegation router, but do not build it in the current
release.

Current work should ship as complete, manually selected vertical slices:

1. the non-activating composable policy core;
2. the Codex-managed Claude adapter and its provider-specific runtime behavior; and
3. if separately approved, a minimal Codex-managed Antigravity adapter for Gemini Flash.

Each slice may have its own launcher, capability probes, recovery rules, and provider-specific
tests. They should share only stable contracts whose meaning is already known. The future router
will select among adapters; it will not replace their enforcement or pretend their runtimes are
interchangeable.

This proposal records the extension seam and the conditions for reopening the work. It does not
add router implementation to the current policy-core plan or authorize a Gemini adapter.

## 2. Why this is deferred

The current [cross-runtime proposal](2026-07-17-cross-runtime-routing-and-claude-delegation.md)
deliberately limits its first implementation to Codex-managed Claude sessions. The
[composable-policy proposal](2026-07-20-composable-claude-capability-and-scope-policy.md) then
separates requested policy, authority, private bindings, presentation, and runtime assurance.
Those boundaries are useful foundations, but neither an uninstalled contract core nor one
provider adapter supplies enough operational evidence to justify an automatic multi-provider
router.

Building the router now would require decisions about provider availability, subscription versus
usage-based billing, model equivalence, capability drift, cache behavior, permission semantics,
session resumption, and cross-provider quality evidence. Those decisions are broader than the
current closure target and would delay the capability needed now.

Deferral must not become accidental lock-in. The current release therefore preserves the small
set of invariants in §5.

## 3. Intended future outcome

A future orchestrator should be able to receive one bounded task packet and deliberately select:

- the host harness: Codex, Claude Code, or Antigravity;
- the transport: native child agent, official headless CLI, or an explicitly supported SDK/server;
- the model and reasoning or thinking setting;
- the authentication and billing class;
- the compiled authority profile and workspace bindings;
- the session, recovery, artifact, resource, and observation policy; and
- the validation and final-disposition contract.

Selection may remain manual, become recommendation-only, or become automatic under a later policy.
No routing mode may silently substitute a foreign-model-in-host route for the model's native
harness. For example, an OpenAI model running inside Claude Code through a gateway is a different
execution route from the same model running through Codex.

## 4. Options considered

### 4.1 Extend one provider wrapper until it becomes the router

This is initially fast, but provider assumptions leak into task packets, permission names, session
records, and error handling. Later adapters either impersonate the first provider or require a
large migration. Reject this as the long-term architecture.

### 4.2 Build the full shared framework before adding Gemini

This maximizes early uniformity but generalizes from provider documentation and one partially
probed adapter. It expands the current release into routing policy, adapter discovery, lifecycle
orchestration, and migration work before the second provider has produced operational evidence.
Defer this option.

### 4.3 Complete provider adapters behind a minimal common contract

This is the selected direction. A provider adapter is complete in itself and can be invoked
manually. It also conforms to a small provider-neutral boundary for packets, authority,
provenance, results, and disposition. Shared implementation is extracted only after two adapters
demonstrate identical semantics rather than merely similar names.

## 5. Compatibility invariants for current work

Current and near-term work should preserve these constraints:

1. **Separate task intent from delivery.** Objective, non-goals, ownership, validation, and output
   belong to the task packet. CLI flags and provider session identifiers belong to the adapter.
2. **Keep policy provider-neutral.** The policy core describes capabilities and scopes. An adapter
   compiles them into provider controls and reports unresolved or unavailable dimensions.
3. **Keep bindings private.** Absolute paths, credential locations, and provider session handles do
   not enter portable semantic or authority identities.
4. **Separate planned, requested, and observed provenance.** Requested model or permission flags
   are not evidence of the delivered runtime.
5. **Treat capabilities as adapter claims with assurance.** A shared name such as `sandboxed` or
   `read-only` does not imply equivalent enforcement across providers.
6. **Use official authentication boundaries.** An adapter invokes an official client or supported
   SDK. It does not extract, copy, proxy, or reinterpret subscription OAuth credentials.
7. **Do not require automatic routing.** Every adapter remains directly and deterministically
   invocable when the router is absent.
8. **Use compatible lifecycle states.** Adapters may expose provider-specific detail, but they can
   map start, running, terminal, interrupted, failed, and unreconciled states into a common result
   envelope without inventing success.
9. **Keep root verification authoritative.** A worker result never integrates itself, regardless
   of provider or harness.
10. **Bound generated state.** Provider adapters use the same manager-owned accounting discipline
    while retaining provider-specific logs and retention behavior.

These are compatibility constraints, not an instruction to extract a shared framework during C0.

## 6. Provider-adapter boundary

A future adapter should be describable by the following conceptual operations:

| Operation | Portable meaning | Provider-owned behavior |
|---|---|---|
| `doctor` | Report whether a requested route can be attempted | Authentication, binary, model, permission, and capability probes |
| `compile` | Map policy and private bindings to a launch request | CLI settings, tool manifests, sandbox controls, working directories |
| `start` | Create one recorded attempt | Process, native child, SDK, or server invocation |
| `observe` | Return sanitized current and terminal evidence | Stream parsing, process state, runtime manifests, usage counters |
| `resume` | Continue a recorded semantic task when valid | Provider session or conversation semantics and cache caveats |
| `materialize` | Write one accepted result to an exact manager-owned path | Provider output extraction and overwrite policy |
| `reconcile` | Compare declared ownership with observed effects | Git, filesystem, artifact, and provider-state checks |

The future router consumes this boundary. It does not construct raw provider commands itself.
Adapters may initially implement these operations in separate modules or scripts.

## 7. Minimal Antigravity stepping stone

A separately approved Gemini Flash slice should be a Codex-managed Antigravity adapter, not a
partial universal router. Its first complete release should support:

- non-generative `doctor` checks;
- explicit Gemini Flash model selection through the official `agy` client;
- one foreground or manager-owned background attempt with durable stdout, stderr, and metadata;
- read-only investigation and isolated-worktree implementation as distinct requested profiles;
- exact workspace and ownership declarations;
- provider-specific permission and sandbox reporting without claiming equivalence to Claude;
- status, inspection, recovery, result materialization, and reconciliation;
- independent root test and diff verification; and
- the same generated-state accounting and privacy constraints as the Claude adapter.

Google's official
[Antigravity CLI codelab](https://codelabs.developers.google.com/antigravity-cli-hands-on)
documents `agy -p` as a non-interactive automation surface and describes its permission modes.
That supports evaluating the official CLI as a process boundary; it does not prove any particular
local version's write, sandbox, resume, or model-observation semantics. Those require dated probes
before the adapter makes enforcement claims.

The community
[Antigravity for Claude Code](https://github.com/yuting0624/antigravity-for-claude-code) plugin is
useful prior art for headless invocation, background jobs, digest contracts, and failure handling.
It is not an authority for Google authentication, terms, or runtime guarantees, and should not be
copied wholesale into the canonical adapter.

## 8. Authentication and billing boundary

Harness, model provider, authentication, and billing are separate route fields.

- Claude Code may use Claude subscription credentials, Anthropic API credentials, or supported
  cloud providers. Subscription credentials remain inside the official Claude client, consistent
  with Anthropic's [authentication](https://code.claude.com/docs/en/authentication) and
  [credential-use](https://code.claude.com/docs/en/legal-and-compliance) documentation.
- Codex may use ChatGPT subscription access or usage-based API access, as described by OpenAI's
  [Codex authentication documentation](https://learn.chatgpt.com/docs/auth). The route record
  identifies which class was requested without storing credentials.
- Antigravity may use its supported Google authentication or cloud path. The adapter invokes the
  official client and does not expose its credential material to another harness.

Provider documentation and applicable terms control each route. A local wrapper is not permission
to harvest or repurpose OAuth tokens. If a provider's terms or supported automation boundary are
unclear, the route remains unavailable or requires a separately approved, documented risk
decision.

## 9. Evidence and routing learning

The future router may consume privacy-preserving outcome events, but it may not ingest prompt,
transcript, command, credential, or raw tool-output content. Comparable events should include:

- task class and packet-contract version;
- planned, requested, and observed route;
- capability and assurance snapshot;
- terminal state and root disposition;
- validator outcome and rework;
- elapsed time and usage counters when exposed; and
- whether delegation improved correctness, isolation, or wall-clock time.

One outcome can change a probe or hypothesis. It cannot establish a universal model ranking or
silently activate a routing-policy change.

## 10. Reopening triggers and deferred deliverables

Reopen this proposal when one or more of these conditions is observed:

1. both Claude and Antigravity adapters have passed dated runtime probes and repeated real tasks;
2. manual provider selection becomes a recurring source of delay or error;
3. lifecycle, state-budget, or reconciliation code is duplicated with demonstrably identical
   semantics;
4. comparable outcome evidence supports a bounded routing hypothesis; or
5. a third provider or native harness makes pairwise integration materially more expensive than a
   shared router.

When reopened, the work should produce:

- a versioned provider-adapter protocol;
- adapter discovery and capability records;
- manual, recommendation-only, and automatic routing modes;
- explicit cost, quota, quality, cache, and availability policies;
- cross-adapter conformance fixtures;
- migration plans for existing Claude and Antigravity records; and
- a security, privacy, authentication, and provider-terms review.

## 11. Open questions

- Which lifecycle fields are truly portable after two adapters have operational evidence?
- Should native child-agent transports and headless CLI transports share one adapter or be
  separate adapter variants?
- How should subscription quotas be represented when providers expose no hard remaining-limit
  API?
- When is foreign-model-in-host execution useful enough to justify its additional provenance and
  cache complexity?
- What evidence threshold permits recommendation-only routing, and what higher threshold permits
  automatic routing?
- Which components remain repository-local, and which warrant a separately versioned package?

These questions are intentionally deferred. Current implementation must preserve the invariants in
§5, not answer the entire roadmap.
