# PROBE — 2026-07-03 prix-guesser post-mortem verify gate (fable-high vs opus-high, identical effort)

- probe_id: P-20260703-pg-postmortem-gate · grandfathered: true
- class: review gates (W-001), identical-effort pairing at HIGH · configs: `reviewer` pin with
  opus override @ high (leg 1, deliberate cross-tier independence from the fable author) vs
  `reviewer` pin fable @ high (leg 2, operator-directed)
- blinded: yes (legs blind to each other) · frozen tree: yes (frozen pre-fix draft) ·
  adjudicator: **author** (disclosed) · deviation: **fable leg = author-model**
- **attestation:** gate record —
  prix-guesser:.handoffs/2026-07-03-external-grounding-postmortem-FINDINGS.md §7
- verdict/yield: both **COMMIT-WITH-FIXES**, convergent on the sole shared MAJOR; fable +1 unique
  MAJOR (*"the draft's 'NEVER-TRUE-AS-FRAMED' grade contradicted its own verdict key's 'at any
  prior time' clause"*) + ~5 precision minors; opus +1 unique status-hedge minor; *"the
  author-model reviewer showed no leniency toward the author — its sharpest catch was against the
  author's own grading key."*
- **tally:** feeds W-001 (attested-deviated: author-adjudicator + author-model); demotion counter
  unmoved.
