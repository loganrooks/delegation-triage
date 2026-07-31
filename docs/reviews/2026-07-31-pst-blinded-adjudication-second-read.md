# PST blinded adjudication — independent second read (2026-07-31, verbatim)

Provenance: the FIRST adjudicator spawn (same brief and bundle as
`2026-07-31-pst-blinded-adjudication.md`'s author) stalled mid-stream on its final
synthesis turn and was recorded as a casualty; the shutdown message later resumed it from
its intact transcript and it completed and delivered this report before approving
termination. Post-resume model identity transcript-attested `claude-opus-5` (the spawn pin
HELD through resume — an n=1 counter-instance to the CONTRACT §3 resume-rebill hazard;
treat the hazard as surface-dependent, not universal). It self-describes as "an independent
second read of the same bundle, not a replacement" — same blinding, no access to
adjudicator-b's report.

**Concordance with the read of record: verdict DIRECTIONS IDENTICAL on all six tasks**
(T1 X · T2 X · T3 Y · T4 equivalent · T5 Y · T6 X), same two-signature clustering with the
same label mapping (Signature A = de-blinded opus, Signature B = de-blinded flash on all
five discriminable tasks), same two gate-implication headliners (T6-Y repo-root execution;
T1-Y within-file constraint breach). Findings unique to this read, folded into the trial
record: the T1 packet fault (both arms — `.planning/STATUS.md` named in the objective but
not ownable, so the open item cannot actually be closed; neither arm flagged it); T5-Y's
redaction test near-vacuous under its own mock; T1-Y unbounded `join()` (deadlock hangs the
suite rather than failing it); T2-X `touch()` docstring contradicting its code; the
unnamed banker's-rounding dependence in T2-Y.

Verbatim below, unedited.

---

BLINDED PST DIFF ADJUDICATION — COMPLETE (this session did finish; delivering before approving shutdown, as an independent cross-check against pst-adjudicator-b)

Blinding note: I did not attempt vendor attribution and formed no confident authorship belief. But two *style signatures* recur consistently and swap labels across tasks, so "arm X" is not one agent — see the profile section, which is written by signature, not by label.

===============================================================
VERDICTS
===============================================================
T1: X better — forces real contention (barrier + clock-aligned processes) and asserts the counter's RETURN values, which Y never does.
T2: X better — Y's tests cannot distinguish segment-match from substring-match in project_of, nor detect dropping the literal "workflows" glob segment.
T3: Y better — pins the file-handle closure the packet asked for (X leaves half the packet's change untested) and exercises real ledger_path resolution instead of mocking it.
T4: equivalent — byte-identical except the handle name (`fh` vs `f`).
T5: Y better — exact full-output equality pins render_text; X's substring assertions stop short of the affordability verdicts.
T6: X better (narrow) — packet-faithful and isolated; Y's second test runs the benchmark against the live repo root.

===============================================================
T1 — fleet_count concurrency
===============================================================
ARM Y findings
1. MAJOR — worker return values are never asserted (t1-armY.diff:48-56, 115-123). `worker()` calls `pg.fleet_count(...)` and discards the result; only the post-hoc line count and one subsequent sequential call are checked. The packet's objective is "must produce a correct count (no lost updates within the window)" — an implementation that appended correctly but returned garbage *during* contention passes every assertion here. Arm X's `assertEqual(max(counts), n)` is the assertion that actually pins it. [Y | implementation | adjudication]
2. MAJOR — no contention is forced (both concurrency tests). No barrier, no clock alignment; the ProcessPoolExecutor test in particular can have worker 1 finish all 10 iterations before worker 8 starts, so the test may pass as a purely sequential one. Overlap is likely but never established, and nothing fails if it doesn't happen. [Y | implementation | adjudication]
3. MAJOR — packet scope violation inside the owned file. The packet says "append a new test class; modify nothing else in it beyond imports"; Y inserts a module-level function `_fleet_count_worker` (t1-armY.diff:21-26) wedged between the import block and the `HERE`/`ROOT` constants. It is needed for ProcessPoolExecutor picklability, so the design forced it — but it is neither an import nor part of the appended class, and no DEVIATION was raised. This is the one finding the delegator's file-level scope check structurally cannot catch. [Y | implementation | adjudication]
4. MINOR — `t.join()` with no timeout (t1-armY.diff:56, 123). In a concurrency test specifically, a regression that deadlocks fleet_count hangs the suite forever instead of failing it. X uses `join(timeout=60)` plus an `is_alive()` assertion.
5. MINOR [UNCERTAIN] — ProcessPoolExecutor + a module-level worker is start-method dependent. Under `spawn` (macOS default) the child re-imports `test_gate`; I traced `_fixup_main_from_name` and it returns early for `unittest.__main__`, so I believe it works, but this was not executed. Under `fork` it is trivially fine. Labelled Underdetermined.

ARM X findings
1. MINOR — `test_concurrent_sessions_do_not_cross_count` (t1-armX.diff:166-189) drops the error-collection discipline X's own `_thread_burst` helper uses: no try/except around `barrier.wait`, so a broken barrier surfaces as a confusing line-count failure (or a FileNotFoundError inside `_lines`) rather than the real cause. [X | implementation | adjudication]
2. MINOR — both arms assert the stale prefix is neither counted nor removed (`len(lines) == stale + n`). That pins the *absence of pruning* as a contract; a future implementation that compacted the log would fail a test that has nothing to do with counting. Shared by both arms, so non-discriminating.
3. Note — X's docstring argues `max(counts) == n` is timing-independent (whoever appends last reads a file containing every append). I checked that reasoning and it holds, which is why X's process test survives its 1.0s alignment window being missed on a loaded machine. This is the single best piece of test design in the bundle.

PACKET fault (both arms) — the objective says it closes an open item in `.planning/STATUS.md`, but STATUS.md is not in Owned files, so the open item stays open either way. Neither arm raised it as a DEVIATION. [both | packet | adjudication]

===============================================================
T2 — tools/savings.py
===============================================================
Source edits are equivalent (context manager; `fh` vs `f`). Entire delta is in the tests.

ARM Y findings
1. MAJOR — `project_of` tests (t2-armY.diff:65-75) cannot catch a substring-match regression. All three pass if the function is rewritten as `if "projects" in path`. X's `test_partial_match_does_not_count_as_the_projects_segment` (path `/home/myprojects/proj/...` → "?") is exactly the discriminator. [Y | implementation | adjudication]
2. MAJOR — `find_journals` has no fixture with a non-`workflows` sibling directory at the correct depth, so changing the glob from `*/*/workflows/wf_*.json` to `*/*/*/wf_*.json` passes every Y assertion. Also untested: non-`.json` extensions, and a missing root. [Y | implementation | adjudication]
3. MINOR — `test_pct_quantiles` uses `range(101)` with q=0.9/0.99, indices that land on exact integers, so it cannot distinguish nearest-rank from linear interpolation. `test_pct_even_length_list` does discriminate (interpolation would give 250, not 300) but the banker's-rounding behavior it silently encodes is never named, so the next reader is likely to "fix" it.

ARM X findings
1. MINOR — `test_projects_as_final_segment_raises_indexerror` (t2-armX.diff:126-131) pins an IndexError as contract. X labels it CHARACTERIZATION and notes unreachability, which is the honest framing, but it is still a test that fails if someone *hardens* the function to return "?". [X | implementation | adjudication]
2. MINOR — `touch()` docstring says "Create an empty file" while writing `"{}"` (t2-armX.diff:31-36). Comment contradicts code.
3. MINOR — `assertIn(sv.pct([0, 100], 0.5), (0, 100))` (line 155) is redundant with the exact assertion on the line above; not vacuous (it fails on 50.0) but it adds nothing.
4. Not tested — the packet says "mirror the style of tests/test_overprov.py"; that file is outside the bundle, so style conformance for both arms is Underdetermined.

===============================================================
T3 — tools/backtest.py
===============================================================
Source edits are byte-identical (both `7bf6991..1483598`).

ARM X findings
1. MAJOR — nothing pins the file-handle closure. Half the packet is "close the two unclosed handles using context managers", and X adds zero coverage of it; a revert to `for line in open(ledger)` passes all of X's tests. Y's `test_ledger_handle_is_closed` (t3-armY.diff:109-120, ResourceWarning under `catch_warnings` + `gc.collect`) would have failed on the pre-fix code. [X | implementation | adjudication]
2. MINOR — `patch.object(B, "ledger_path", ...)` (t3-armX.diff:38) means the env-var resolution path is never exercised, and there is no guard asserting the redirect took effect. Y asserts `B.ledger_path() == os.path.join(self.dir, "backtest-cases.jsonl")` before relying on it — the correct instinct, since without it every assertion in the class could silently be about the developer's real ledger.
3. MINOR — no empty-file case and no final-line-without-trailing-newline case.

ARM Y findings
1. MINOR — `setUp` uses `tempfile.mkdtemp()` and `tearDown` restores the env var but never removes the directory (t3-armY.diff:60-69): eight leaked temp dirs per suite run, in a test file whose subject is resource leaks. X's `TemporaryDirectory` context managers are clean. [Y | implementation | adjudication]
2. MINOR — `test_ints_and_floats_compare_alike` (line 54-56) compares two calls to each other with no absolute expectation; it cannot fail unless the two disagree.
3. MINOR — `warnings.catch_warnings` + `simplefilter("always")` mutates global filter state; harmless in a serial suite, a hazard if the suite is ever parallelized.

===============================================================
T5 — CLI report --format text
===============================================================
ARM X findings
1. MAJOR — `assertIn("held reservations:", output)` / `assertIn("intent orders-db:", output)` (t5-armX.diff:36-37) assert the labels but not the verdicts. A regression flipping affordable↔unaffordable, or dropping "(realized)", passes. Y pins the whole five-line output by equality. [X | implementation | adjudication]
2. MAJOR — the output-file test (t5-armX.diff:39-68) redirects stdout into a throwaway StringIO and never asserts it is empty, so double-emission (file *and* stdout) passes. Y asserts `stdout.getvalue() == ""`. [X | implementation | adjudication]
3. MINOR — no negative control that text output is not JSON. Y's `with self.assertRaises(json.JSONDecodeError)` supplies one.

ARM Y findings
1. MINOR — `test_text_format_redacts_explicit_paths` is near-vacuous under its own mock: `sample_local_capacity` is patched, so the requested path never reaches the renderer and cannot appear in output unless the CLI separately echoes its argv. [Y | implementation | adjudication]
2. MINOR — `test_text_format_stdout_is_deterministic_with_fixed_clock` is largely subsumed by the exact-equality test; three of six tests re-assert `startswith("host: alpha-1\n")`.
3. MINOR (scope) — two of six tests are not about the text path: `test_report_format_defaults_to_json` and `test_text_format_rejects_unknown_format_without_sampling`, the latter pinning an exact stderr string `"storage-advisor: argument-error\n"`. Defensible as dispatch-boundary coverage, but it is over-delivery against "the --format text output path". [Y | implementation | adjudication]

===============================================================
T6 — measure_overhead smoke test
===============================================================
ARM Y findings
1. MAJOR — `test_measure_overhead_with_relative_pythonpath_from_repo_root` (t6-armY.diff:62-93) runs the benchmark with `cwd=REPO_ROOT` and asserts on a before/after diff of the repo root's directory listing. Isolation is the entire point of the "creates no files" clause: if the script ever *does* create a file, this test leaves it in the source tree, and any unrelated concurrent write to the repo root fails the test. The first test already covers the clause correctly in a temp dir. [Y | implementation | adjudication]
2. MINOR — runs the 1000-forecast benchmark twice for redundant assertions; X runs it once in `setUpClass` and shares the result across five tests.
3. MINOR — `assertEqual(result.stderr, "")` in both tests is stricter than the documented contract; any incidental DeprecationWarning turns into a failure. [Y | implementation | adjudication]
4. MINOR — the first test is monolithic, so the first failed clause masks the rest. X's five-way split reports each contract clause independently.

ARM X findings
1. MINOR — asserts `len(splitlines()) == 1` but not the trailing newline; Y's `assertTrue(stdout.endswith("\n"))` is the stricter read of "a single line". Neither is required by the packet's enumeration.
2. MINOR — no type assertions on the three numeric fields (Y has them; also not required).
3. MINOR [UNCERTAIN] — X's test methods carry no `-> None` annotations, while both arms used them in `tests/test_cli.py` for what appears to be the same project (T5, 261-test suite). Weak evidence of local convention; I could not see a pre-existing annotated `def` in the diff context, so this is Underdetermined.

===============================================================
ARM PROFILES — by style signature, not by label
===============================================================
Profiling "arm X across six tasks" is not meaningful given the per-task label shuffle you described. Two consistent authorial signatures are visible instead, and they map cleanly:

SIGNATURE A — narrated-contract. (T1-X, T2-X, T3-Y, T5-Y, T6-X.)
Opens with a docstring naming *why* each behavior is load-bearing and which behaviors are surprising; writes explicit anti-vacuity guards (`assertNotIn(0, counts)` because 0 is fail-open; asserting `ledger_path()` resolves to the redirect before trusting the class); reaches for exact-output equality over substrings; reasons in comments about why an assertion is timing-independent; labels characterization tests as such. Failure mode: over-pinning incidental behavior (the IndexError characterization), redundant near-duplicate tests, and occasional drift past the packet boundary (T5's argparse and json-default tests).

SIGNATURE B — conventional-coverage. (T1-Y, T2-Y, T3-X, T5-X, T6-Y.)
Covers the obvious cases competently in fewer lines, idiomatic library choices (ProcessPoolExecutor, `patch.object`), plain naming. Failure modes cluster tightly and repeat: assertions that stop one step short of the behavior under test (discarded return values T1, substring-only T5, no closure test T3), fixtures too thin to discriminate the regression the packet cares about (T2 project_of and find_journals), weaker hygiene (unbounded joins T1, leaked temp dirs T3, live-repo-root execution T6).

The pattern that matters: signature B's diffs are all *green and defensible in isolation*. Every one of its gaps is a test that passes today and would keep passing through the regression it was written to catch. That is invisible to a green-suite gate by construction.

===============================================================
WOULD ANY FINDING HAVE CHANGED ACCEPTANCE?
===============================================================
Two, both against signature B, both structurally outside the stated gate (suite green + exit 0 + diff scope confined to owned files):

1. T6-Y's repo-root test. This is the one I would have blocked on. The gate checks the *diff*'s scope; this is a runtime effect — a test that executes with cwd inside the working tree and asserts on that tree's contents. Cheap gate addition: reject new tests that pass `cwd=REPO_ROOT` (or any path inside the checkout) to subprocess.
2. T1-Y's module-level helper. The packet said "modify nothing else beyond imports" *within* the owned file; the gate's file-level scope check cannot see intra-file constraints. Not worth a rejection on its own — the ProcessPoolExecutor design forced it — but it should have been a DEVIATION line, and its absence is the reportable failure.

Everything else is fix-forward. The remaining MAJORs (T1-Y's unasserted return values, T3-X's untested closure, T5-X's substring assertions) are exactly the class a green-suite gate cannot reach: they are under-delivery, not defect. If you want the gate to catch them, the lever is a required assertion-target clause in the packet ("the test must fail if <named behavior> regresses"), not a stricter oracle.

===============================================================
WHAT THIS REVIEW DOES NOT CERTIFY
===============================================================
Not tested — I executed nothing. Every claim above is read from the diffs plus the packets; I did not run the suites, did not confirm the arms' reported oracle results, and did not read any repo file outside the bundle (per your constraint), so all claims about *pre-existing* file contents, imports, and local style conventions are inference from diff context only. Specifically Underdetermined: whether `redirect_stderr`/`json` were already imported in tests/test_cli.py (T5-Y depends on it; your oracle-green is the only evidence); whether either T2 arm matches tests/test_overprov.py's style; the multiprocessing start method under which T1-Y's oracle ran; the repo's `-> None` convention in T6.

Probed and found sound — recorded so you know what was examined, not only what failed: the production-code edits in T2/T3/T4 are behavior-preserving context-manager conversions in all six diffs (T3's two blobs are identical, T4's differ only in a handle name), so the entire quality delta in this trial is in test design, not shipped behavior; T1-X's `max(counts) == n` invariant is genuinely interleaving-independent, as its docstring claims; T1-Y's spawn-safety traces clean through `_fixup_main_from_name`; T3-Y's ResourceWarning assertion is load-bearing (it fails on the pre-fix code, not vacuous); T2-X's banker's-rounding index arithmetic checks out at every quantile it asserts (round(0.5)→0, round(1.5)→2, round(4.5)→4, round(8.1)→8, round(8.91)→9); no arm touched a file outside its packet's Owned list.

Lenses NOT applied: performance/runtime cost of the added suites beyond the notes above, security, CI-platform portability beyond the one spawn question, and any assessment of the packets themselves as a benchmark instrument.
