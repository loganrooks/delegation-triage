# P-20260725-batch-tier-rulings — re-route event: batch A–D operator rulings (Cowork fable leg)

**Date:** 2026-07-25 (00:4x UTC) · **Class:** availability/re-route event (ruling, not a scored
probe — moves no flip counter) · **Recorded by:** fable leg, Cowork continuation session
**Basis presented to operator:** docs/reviews/2026-07-24-post-opus5-routing-issues.md (21-item
audit; opus-escalated R7 lane over policy @ b141210 + routing-evidence CSVs), concordant with
W-025's independent packet reading.

## Rulings (verbatim options chosen via decision panel)

- **A — "all four" xhigh drops:** R2 fallback → opus high (+reviewer gate), R3 fallback → opus
  high, R13 fallback → opus high (+reviewer gate), R15 fallback → opus high, **and R10 pin
  xhigh → high**. All marked Provisional; probes stay open. Evidence: every opus xhigh-over-high
  delta ≤ +0.5 (inside CSV read error) except out-of-class DeepSWE; authoring cuts favor high
  (FrontierCode Main −4.4). R10 note: was the last live xhigh opus pin and carried the F2
  `thinking:disabled`+xhigh HTTP-400 exposure — both retired with the drop.
- **B — R14 collapsed into R15:** row tombstoned; the advisor-TOOL encryption scope note moved
  into R15; long-horizon executor lanes route on their base class rows.
- **C — budget-conscious profile deleted until needed** (deltas predated opus-5 repricing and the
  07-24/25 re-routes; re-derivation recipe pointer left in the profiles table).
- **D — subagent-spawn cap adopted** as a cross-class constraint (default 4 or stated reason),
  per O5-PG "delegates more readily" via W-025.

## Coupled edits (one pass, this commit)

ROUTES.md only — no pin frontmatter involved (R10 has no agent pin; R15's fable pin unchanged).
Issues-doc statuses appended in the same commit.

- **attestation:** operator selections captured in-session (decision panel, Cowork); edits
  verified by grep after write. Self-reported execution.
- **tally:** feeds W-024 (context) and W-002/W-003/W-010/W-022 route history; no probe counters move.
