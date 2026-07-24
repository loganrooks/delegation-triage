# Claude Opus 5 — Evidence Gathering for Model-Routing Policy

Research date: 2026-07-24 (day of Opus 5's public launch). Compiled for routing-policy input only — no routing recommendations are made here.

## 1. Sources table

| # | URL | Publisher | Vendor / Independent | Date accessed / published |
|---|-----|-----------|----------------------|---------------------------|
| S1 | https://www.anthropic.com/news/claude-opus-5 | Anthropic | Vendor (primary announcement) | Published 2026-07-24; accessed 2026-07-24 |
| S2 | https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5 | Anthropic (Claude Platform Docs) | Vendor (official API/model docs) | Accessed 2026-07-24 |
| S3 | https://platform.claude.com/docs/en/build-with-claude/effort | Anthropic (Claude Platform Docs) | Vendor (official API docs) | Accessed 2026-07-24 |
| S4 | https://platform.claude.com/docs/en/about-claude/models/overview | Anthropic (Claude Platform Docs) | Vendor (official spec table) | Accessed 2026-07-24 |
| S5 | https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5 | Anthropic (Claude Platform Docs) | Vendor (official docs) | Accessed 2026-07-24 |
| S6 | https://www.vals.ai/benchmarks/swebench | Vals AI | Independent (third-party benchmark operator, standardized bash-only harness) | Page marked "Updated 7/22/2026"; accessed 2026-07-24 |
| S7 | https://artificialanalysis.ai/models/claude-opus-5-xhigh | Artificial Analysis | Independent (third-party benchmark aggregator) | Accessed 2026-07-24 |
| S8 | https://artificialanalysis.ai/models/claude-opus-5 | Artificial Analysis | Independent | Fetch returned no readable content (likely JS-rendered); not usable as a citation |
| S9 | https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/ | TechCrunch (Russell Brandom) | Independent journalism | Published 2026-07-24; accessed 2026-07-24 |
| S10 | https://officechai.com/ai/claude-opus-5-benchmarks/ | OfficeChai | Independent journalism, reporting vendor-supplied figures | Published 2026-07-24; accessed 2026-07-24 |
| S11 | https://officechai.com/ai/claude-opus-5-becomes-top-model-in-the-world-on-artificial-analysis-intelligence-index-beats-fable-5/ | OfficeChai | Independent journalism, reporting independent (Artificial Analysis) data | Published 2026-07-24; accessed 2026-07-24 |
| S12 | https://tech.yahoo.com/ai/claude/articles/claude-opus-5-outscores-fable-182843985.html (via Decrypt) | Yahoo Tech / Decrypt (Jose Antonio Lanz) | Independent journalism, reporting vendor-supplied benchmark figures with some independent context | Published 2026-07-24; accessed 2026-07-24 |
| S13 | https://threatfrontier.com/articles/anthropics-own-benchmark-why-the-rumored-opus-5-is-being-aimed-at-matching-not-beating-its-flagship-fable-5 | ThreatFrontier.com | Independent, but **pre-launch rumor piece based on unconfirmed leaks** | Published 2026-07-21 (3 days before launch); accessed 2026-07-24 — superseded by actual launch, used only for background/methodology caveats |
| S14 | https://www.lennysnewsletter.com/p/claude-opus-5-review-this-model-is | Lenny's Newsletter / "How I AI" podcast (Claire Vo) | Independent practitioner review | Published 2026-07-24; accessed 2026-07-24 — qualitative/anecdotal, no extractable numeric scores (video/podcast format) |
| S15 | WebSearch aggregation (llm-stats.com, claudefa.st, various) | Multiple secondary aggregators | Independent but derivative (not fetched directly, used only for cross-checking context window / pricing, which were separately confirmed via S4 and S7) | Accessed 2026-07-24 |

**Not fetched / could not verify directly:** CNBC, Bloomberg, 9to5Mac, Fortune, kie.ai, TestingCatalog articles appeared in search results but were not fetched (time/scope-bounded); VentureBeat fetch returned empty content. Anthropic's Opus 5 system card (https://www.anthropic.com/claude-opus-5-system-card) was referenced by S1 but not fetched — it likely contains more detailed safety/cyber/bio evaluation tables than were captured here.

---

## 2. Official specs (source: S1, S2, S3, S4, S5 — all vendor)

| Spec | Value |
|---|---|
| Model string | `claude-opus-5` |
| Release date | 2026-07-24 |
| Context window | 1,000,000 tokens (this is **both** the default and the maximum — no smaller-context variant exists) |
| Max output | 128,000 tokens (synchronous Messages API); up to 300k output tokens on the Batch API with beta header `output-300k-2026-03-24` |
| Pricing | $5 / MTok input, $25 / MTok output — **unchanged from Opus 4.8** |
| Fast mode pricing | $10 / MTok input, $50 / MTok output (~2.5x speed, API-only at launch; not on Bedrock/Google Cloud/Microsoft Foundry) |
| Reliable knowledge cutoff | May 2026 |
| Training data cutoff | May 2026 |
| Data retention | No data-retention requirement for general access (not a "Covered Model") — contrasts with Fable 5/Mythos 5, which carry mandatory 30-day retention |
| Thinking default | On by default (adaptive); this is a **behavior change** from Opus 4.8, where thinking was off unless explicitly enabled |
| Prompt cache minimum | 512 tokens (down from 1,024 on Opus 4.8) |
| Availability | Claude API, AWS Bedrock, Google Cloud, Microsoft Foundry |

### Effort/thinking-level controls — confirmed real API parameter

The routing policy's "high" and "xhigh" terms map directly onto a real, current API parameter: `output_config.effort`. Per S2/S3, Opus 5 supports the **full effort ladder**: `low`, `medium`, `high` (default, equivalent to omitting the parameter), `xhigh`, `max`. No beta header is required. This same 5-level ladder is shared by Fable 5, Mythos 5, Opus 5, Opus 4.8, Opus 4.7, Sonnet 5, and Sonnet 4.6 (older models support a subset).

Behavior notes specific to Opus 5:
- `thinking: {"type": "disabled"}` is only accepted when effort is `high` or below; setting it with `xhigh` or `max` returns an HTTP 400 error (a breaking change from Opus 4.8).
- Anthropic's own guidance (S3): "Start with `xhigh` for coding and agentic work, and use `high` for most other intelligence-sensitive workloads. `low` and `medium` effort are stronger on Claude Opus 5 than on earlier Opus models... run a fresh effort sweep on your evals rather than reusing [prior model] settings."
- At `xhigh`/`max`, Anthropic recommends a large `max_tokens` (start at 64k) since it's a hard cap on thinking + response combined.
- Effort affects **all** output tokens (text, tool calls, thinking), not just visible response length — lowering effort also reduces tool-call counts.
- Claude Code's "ultracode" mode is not a separate API effort level; it pairs `xhigh` with standing multi-agent permissions.

---

## 3. Benchmarks, with figures and sources

**Legend:** [V] = vendor-reported (Anthropic), [I] = independent, [A] = anecdotal/testimonial (customer quote in vendor material — counted as vendor-adjacent, not independent).

| Benchmark | Opus 5 | Opus 4.8 | Sonnet 5 | Fable 5 | GPT-5.6 Sol | Source / conditions |
|---|---|---|---|---|---|---|
| SWE-bench Verified (bash-only harness, 500 tasks) [I] | **97.00%** | 88.60% (one entry; a second "Opus 4.8" entry shows 91%/84%/71%/67% by difficulty tier — see Gaps) | 84%/77%/76%/67% by task-length tier (<15m / 15m–1h / 1–4h / >4h); no single blended % extracted | 95.00% | 96.20% | S6, Vals AI, independent standardized bash-tool harness |
| SWE-bench Verified by difficulty (Opus 5) [I] | 98% / 97% / 90% / 100% across the same 4 tiers | — | — | 96%/95%/93%/100% | 97%/95%/98%/100% | S6 |
| Frontier-Bench v0.1 (agentic coding, % tasks passed) [V] | 43.3% | 18.7% | — | 33.7% | 34.4% | S1 (Anthropic footnote: internal run, mini-SWE-agent harness, GKE backend, mean reward over 5 attempts/task; Opus 4.8 served as safety-classifier fallback for Opus 5 and Fable 5), reported numerically by S12 |
| CursorBench 3.2 (max effort) [V] | "within 0.5%" of Fable 5's peak score, at ~half the cost per task; beats all models at given cost on high/xhigh/max effort | — | — | peak reference point | — | S1 — no absolute numeric score published, only relative gap |
| ARC-AGI 3 (novel-problem solving, % solved) [V] | 30.2% ("3x the next-best model") | not meaningfully scored per Anthropic | — | not tested | 7.8% | S1 (qualitative "3x" claim), numeric figures via S12 |
| GDPval-AA v2 (real professional work, Elo) [V, corroborated I] | 1,861 (max effort) | — | — | 1,747 | 1,736 | S1/S12 (vendor claim "&gt;100 points clear of both"); this benchmark is co-branded with Artificial Analysis (AA-prefixed), so the same figure recurs in S7's independent evaluation set, but the specific 1,861/1,747/1,736 triplet was sourced via journalism (S12) citing Anthropic's launch chart, not directly re-derived from AA's own page text |
| Zapier AutomationBench [V/A] | Pass rate ~1.5x next-best model at matching cost; beats every competitor's best result even at Opus 5's cheapest effort setting; CEO-quoted 100% on a specific churn-prevention task | — | — | — | — | S1, customer testimonial |
| OSWorld 2.0 (computer use) [V] | Outperforms every model at every price point; clears Fable 5's peak score at ~1/3 the cost | — | — | reference peak | — | S1 — no absolute numeric score extracted |
| Life sciences — organic chemistry (spectroscopy → structure) [V] | +10.2 percentage points vs Opus 4.8 | baseline | — | — | — | S1, internal Anthropic benchmark |
| Life sciences — protein variant function prediction [V] | +7.7 percentage points vs Opus 4.8 | baseline | — | — | — | S1, internal Anthropic benchmark |
| Cybersecurity — OSS-Fuzz (vulnerability discovery vs. exploit development) [V] | Close to Mythos 5 on *discovery*; "far behind" Mythos 5 on *exploit development* | — | — | — | — | S1 — chart-based, no extracted numeric values |
| Automated behavioral-misalignment audit (lower = better) [V] | 2.30 — lowest (best) of recent Claude models | higher | higher | higher | — | S1, S10 — Anthropic's own alignment metric, not independently verified |
| AA Intelligence Index v4.1 (composite: GDPval-AA v2, τ³-Banking, Terminal-Bench v2.1, SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, AA-LCR) [I] | **61** (max effort, #1 of 586 models) / 60 (xhigh effort, #2/191 in-class) | not directly captured | not directly captured | 60 | 59 | S7, S11 — independent composite index; individual GPQA Diamond / Terminal-Bench v2.1 / τ-bench sub-scores are inputs to this index but their standalone numeric values were not exposed in the fetched page (chart-rendered, not text) |
| AA-Briefcase (agentic knowledge work, Elo) [I] | 1,720 | — | — | "146-point lead" implies ~1,574 | — | S7 — independent, Anthropic itself cites the "146-point lead over Fable 5" framing |
| AA-Omniscience (knowledge reliability / hallucination) [I] | +7 pts accuracy vs Opus 4.8, but still behind Fable 5; hallucination rate **+14 points, to 50%** | baseline | — | ahead of Opus 5 | — | S7 — independent; notable negative trade-off (see §4) |
| AA Coding Agent Index / SWE-Atlas-QnA [I] | Joint first place (Coding Agent Index, running inside Claude Code at xhigh); highest score of any model on SWE-Atlas-QnA | — | — | — | — | S7 — independent, no absolute numbers extracted |
| Output speed [I] | 50.7 output tokens/sec — "notably slow," rank #119 of 191 in-class models | — | faster (Sonnet is the "speed" tier per S4) | — | — | S7 — independent |
| Time to first token [I] | 43.85s — "at the higher end" (median for class: 2.86s) | — | — | — | — | S7 — independent |
| GPQA Diamond, AIME, standalone τ-bench, Terminal-Bench v2.1 (isolated, non-composite scores) | **Not established** — these appear only as unlabeled inputs to AA's composite Intelligence Index; no standalone Opus-5-specific numeric figure was retrievable in this pass | | | | | See §6 Gaps |

---

## 4. Differential strengths / weaknesses (evidence bearing on routing priors)

**Coding / agentic implementation — strong evidence of improvement, both vendor and independent:**
- Vendor: Frontier-Bench v0.1 score more than doubled vs. Opus 4.8 (43.3% vs 18.7%); official docs (S2) list "agentic coding and long-horizon tasks... completing multi-file features, larger refactors, and end-to-end feature work without leaving stubs or placeholders" as one of the largest capability jumps.
- Independent: SWE-bench Verified 97.00% (S6) — highest of all models tested, ahead of Fable 5 (95.00%) and GPT-5.6 Sol (96.20%); joint-first on AA's Coding Agent Index and top score on SWE-Atlas-QnA (S7).
- This is consistent evidence supporting continued/strengthened routing of coding and long-horizon implementation work to the Opus tier.

**Long-horizon multi-step work:**
- Vendor docs explicitly recommend `xhigh` effort "for long-running agentic and coding tasks (over 30 minutes) with token budgets in the millions" (S3). S2 lists "multi-agent coordination... running teams of subagents with effective writer-verifier patterns and few cases of agents overwriting each other's work" as a named capability improvement. No independent long-horizon-specific benchmark (e.g., METR-style autonomous-task-length eval) was located for Opus 5 in this pass — this is a gap, not a confirmed independent finding.

**Adversarial review / critique:**
- Vendor docs (S2) explicitly list "Code review and bug-finding — surfacing real bugs at a high rate per pass with few false positives, and staying accurate at lower effort levels" as a named capability improvement. Customer testimonial (AJ Orbach, S1) describes self-directed browser-based verification behavior (checking pages at multiple widths, catching UI bugs before handoff). No independent adversarial-review benchmark was found.
- Countervailing signal: AA-Omniscience hallucination rate rose 14 points to 50% (S7, independent) even as raw accuracy improved — this is a real, independently measured caveat for any use case (like adjudication) where confident-but-wrong output is costly. This is the single most decision-relevant negative finding in the independent data.

**Broad search-and-extraction:**
- DeepSearchQA is named by Anthropic as a category where Opus 5 is "best and most cost-efficient" (S1), but no numeric figure was extracted (chart-only). AA-LCR (long-context reasoning) is one input to the independent Intelligence Index but not isolated. **Not established** as a clear differentiator versus Sonnet 5 specifically — no source directly compared Opus 5 vs. Sonnet 5 on a search/extraction-labeled benchmark.

**Instruction following:**
- IFBench appears in AA's evaluation list (S7) as a tracked metric but no Opus-5-specific score was retrievable. Vendor claims "consistent instruction following... throughout the [1M token] window" (S2) — qualitative, vendor-only.

**Cost-efficiency:**
- This is the most heavily and consistently evidenced theme across vendor and independent sources alike: same per-token price as Opus 4.8 ($5/$25), half of Fable 5's price ($10/$50), while independently benchmarked as beating Opus 4.8 substantially and matching/exceeding Fable 5 on several axes (S1, S6, S7, S10, S11, S12 all converge on this framing).
- Important counterpoint from independent data (S7): in absolute terms Opus 5 is "particularly expensive when comparing to other models of similar [intelligence] price" and "notably slow" (50.7 tok/s, rank 119/191) — the cost-efficiency claim is about cost/intelligence-per-completed-task, not raw per-token price or latency, both of which remain high in absolute terms. A routing policy optimizing for latency-sensitive or high-volume low-value work should not read "cost-efficient" as "cheap" or "fast" in absolute terms.

**Sonnet 5 boundary (bounded/routine work prior):**
- Independent SWE-bench data (S6) shows a real, substantial gap: Sonnet 5's difficulty-tiered resolution rates (84%/77%/76%/67%) trail Opus 5's (98%/97%/90%/100%) at every tier, most sharply on the hardest tasks. Sonnet 5 is priced at $3/$15 (introductory $2/$10 through 2026-08-31) vs. Opus 5's $5/$25 (S4). This is consistent evidence for keeping a difficulty/stakes-based split between Sonnet and Opus, though it does not by itself establish where the line should sit.

**Cybersecurity (not one of the routing policy's stated axes, but relevant to any security-adjacent work):**
- Opus 5 is explicitly positioned by Anthropic as behind Mythos 5 on offensive cybersecurity (exploit generation blocked by policy, not just capability) and close to but behind Mythos 5 on vulnerability discovery (S1). No independent cyber-capability evaluation of Opus 5 was found.

---

## 5. Fable 5 relationship (structural finding, most relevant to the routing table's top tier)

This is the most consequential structural finding for the routing policy: **"Fable 5" is not a peer or sibling of Opus 5 — it is Anthropic's superordinate flagship tier, positioned above Opus in the current five-name lineup (Haiku → Sonnet → Opus → Fable/Mythos).**

Per official docs (S4, S5):
- Anthropic's current lineup has Haiku 4.5, Sonnet 5, Opus 5, and a top "Mythos-class" tier containing **Claude Fable 5** (`claude-fable-5`, publicly/generally available) and **Claude Mythos 5** (`claude-mythos-5`, invitation-only via "Project Glasswing," shares Fable 5's capabilities but without Fable 5's safety-refusal classifiers, targeted at vetted cybersecurity/critical-infrastructure users).
- Fable 5 and Mythos 5 share specs: 1M context, 128k max output, but are priced at **$10/$50 per MTok — exactly double Opus 5's $5/$25.**
- Anthropic's own "Choosing a model" guidance (S4) states: "start with Claude Opus 5 for complex agentic coding and enterprise work. For workloads that need the highest available capability, use Claude Fable 5" — i.e., Anthropic itself frames Fable 5 as the higher-capability-ceiling option, with Opus 5 as the default/practical workhorse.
- Fable 5 carries mandatory 30-day data retention as a "Covered Model" (S5) — Opus 5 does not have this requirement (S1, S2). This is a real operational/legal difference for any routing rule involving sensitive data.
- Fable 5 includes safety classifiers that can return `stop_reason: "refusal"`; typical fallback on refusal routes to Opus 4.8 (or now the new "default" fallback mode) (S5). Opus 5's own classifiers are described as ~85% less likely to trigger than Fable 5's (S1), and Opus 5 refusals fall back to Opus 4.8.
- Independent journalism (S12, citing Anthropic and general reporting) notes Fable 5 has had real availability disruptions since its June 9, 2026 launch: pulled globally for roughly 19 days (June 12 – July 1, 2026) amid a US export-control dispute over a jailbreak vulnerability, and for a period afterward was credits-only rather than included in standard plans. This bears on reliability if a routing policy's top tier depends on Fable 5 being consistently reachable.
- On several specific benchmarks, Opus 5 is reported (both vendor and independent, S1/S7/S11) to *match or slightly exceed* Fable 5 (e.g., AA Intelligence Index: Opus 5 max = 61 vs. Fable 5 = 60; SWE-bench Verified: Opus 5 97.00% vs. Fable 5 95.00%) — at half Fable 5's price and without Fable 5's data-retention/refusal-classifier overhead. Anthropic's own framing is that Opus 5 delivers performance "close to" but still generally understood as just under Fable 5's ceiling, positioned as the more practical, cheaper, less-restricted everyday choice.

**Implication for the routing policy (evidence only, not a recommendation):** if the policy's "Fable 5" entry was written assuming Fable 5 is a peer/alternative to Opus at similar cost, that assumption does not match the current lineup — Fable 5 is priced 2x Opus 5, carries mandatory data retention, and has a track record of availability disruptions. Opus 5 is independently benchmarked as competitive with or ahead of Fable 5 on several specific measures at half the cost.

---

## 6. Gaps and unverifiable items

- **No standalone GPQA Diamond, AIME, or isolated τ-bench score for Opus 5** was retrievable in this pass. These exist only as unlabeled inputs to Artificial Analysis's composite Intelligence Index (v4.1); the composite score (61 max effort / 60 xhigh effort) is confirmed, but per-benchmark breakdowns were rendered as interactive charts not present in the fetched text. Recommend a follow-up fetch of AA's "Intelligence Breakdown" view or the Anthropic system card if these specific figures are needed.
- **Terminal-bench v2.1 standalone score:** same limitation — confirmed as an index input, no isolated Opus-5 figure found.
- **Vals.ai data timestamp inconsistency:** the vals.ai SWE-bench page (S6) is marked "Updated: 7/22/2026," two days before Anthropic's official 2026-07-24 announcement. This is not necessarily an error — Anthropic's post references "early-access customers" and "early-access testing" prior to general availability, so Vals AI may have benchmarked a pre-GA build — but the discrepancy could not be resolved from available sources and should be treated as a minor provenance caveat. The relative ranking (Opus 5 > GPT-5.6 Sol > Fable 5 > Opus 4.8) is corroborated by multiple independent and vendor sources regardless.
- **Duplicate "Claude Opus 4.8" row in vals.ai's table** (one entry at 88.60%, another at 91%/84%/71%/67% by tier) suggests two different configurations (possibly effort levels or harness variants) were tested under the same label; the source did not disambiguate, so Opus 4.8's exact SWE-bench Verified figure should be treated as approximate (high-80s to low-90s%) rather than a single precise number.
- **No independent, non-Anthropic-affiliated cybersecurity or biosecurity evaluation of Opus 5** was found. All cyber/bio safety claims (OSS-Fuzz vulnerability-discovery-vs-exploit gap, "behind Mythos 5") trace to Anthropic's own testing, described as conducted "alongside private-sector and government partners" without those partners or their methodology being independently published in sources reviewed here.
- **No LMSYS/Chatbot Arena Elo or other crowd-preference ranking** for Opus 5 was located in this search pass.
- **No long-horizon/autonomous-task-length evaluation (e.g., METR-style "task length at 50% success")** specific to Opus 5 was found — relevant given the routing policy's interest in "long-horizon implementation" as an Opus prior.
- **Direct head-to-head Opus 5 vs. Sonnet 5 comparison on "broad search, extraction, routine bounded work"** (the specific axis the routing policy uses to justify Sonnet's lane) was not found in either vendor or independent sources. The clearest evidence bearing on the Opus/Sonnet boundary is the SWE-bench Verified difficulty-tiered gap (§4), which is a coding-difficulty signal, not a search/extraction signal.
- **Independent, quantified practitioner reports beyond Vals AI and Artificial Analysis are thin**, as expected for a same-day release. The one independent practitioner review located (Lenny's Newsletter / Claire Vo, S14) is qualitative only (video/podcast, no extracted transcript with numbers) — it flags a verbosity issue ("Claude Slop") and one specific case of the model refusing to touch a merge conflict, plus a general "neurotic" personality characterization, but provides no benchmark table usable for evidence grading.
- **CNBC, Bloomberg, Fortune, 9to5Mac, kie.ai, TestingCatalog** articles appeared in search results with seemingly consistent framing (price, positioning vs. Fable 5) but were not fetched directly in this pass and are not cited as sources above; treat any claims attributed to them elsewhere as unverified.
- Given the model launched the same day as this research (2026-07-24), by definition there has been **no time for extended independent production-use evaluation**, replication studies, or adversarial red-teaming write-ups from outside Anthropic. This absence is itself decision-relevant: confidence in the more favorable independent numbers (Vals AI, Artificial Analysis) should be treated as provisional pending replication over the following weeks.
