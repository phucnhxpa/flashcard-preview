# Independent release audit — Harry P3 October 2025 + ESAT `multistep_v2`

## FAIL — do not release

Audited the local five-card deck, landing page, literal PNG exports, diagrams, source labels/status, maths, privacy boundary, and fresh desktop/mobile behaviour. No learner artifact was edited, published, uploaded, or indexed.

The release is blocked by **incorrect reader-visible official mark allocations** on P3 Q2 and Q5, and by an unsupported subdivision of the single printed Q4(b) allocation. The cards preserve the correct question totals, but that does not cure incorrect part labels.

## Frozen-source and provenance gate — PASS

- The current final-guide TEX SHA-256 is `a7edca885f0234211279ebbf32bd183722264a9788dc7899c0381c9e4fba2dcf`.
- It exactly matches `build_manifest.json`’s declared `guide_provenance.sha256` and the frozen TEX SHA recorded by `audits/evidence_reaudit.md`, whose verdict is PASS.
- Therefore the deck’s claim to derive from the **passed 11 July guide** is correct for the current local candidate. The manifest correctly keeps P3 Q1 out because the passed guide retains no full standalone prompt, and Q6–Q9 out because they were not discussed.

## Blocking findings and exact remediation

| ID | Current learner-visible claim / authority | Result | Exact remediation and acceptance test |
|---|---|---|---|
| M1 | `P3_Oct2025_Q2.html`: part (b) is labelled **3 marks** and part (c) **2 marks**. Official QP `WMA13_Oct2025_QP.txt` lines 290–305 assigns (b) **2** and (c) **3**. | **FAIL** | In `build_deck.py` lines 79–80, change the `part(..., 3, ...)` argument for Q2(b) to `2` and the Q2(c) argument from `2` to `3`; regenerate `P3_Oct2025_Q2.html` and its literal PNG. Acceptance: the displayed three labels are Q2(a) 2, Q2(b) 2, Q2(c) 3, total 7. |
| M2 | `P3_Oct2025_Q4.html` labels (b)(i) **1 mark** and (b)(ii) **2 marks**. The QP prints Q4(a) 3 marks and a single combined Q4(b) allocation of **3 marks** (QP lines 641–660); it does not print separate (i)/(ii) allocations. | **FAIL** | In `build_deck.py` lines 93–94, remove the unqualified individual official-mark badges. Use one reader-visible heading such as `Part (b)(i)–(ii) · minimum and smallest x — 3 marks`, retaining internal subheadings without marks; alternatively visibly label any 1/2 split as an editorial practice split rather than an official allocation. Regenerate HTML/PNG. Acceptance: no learner-facing string presents 1 and 2 as official Q4(b) part marks; the card shows the QP’s combined b = 3 allocation. |
| M3 | `P3_Oct2025_Q5.html`: part (b) is labelled **3 marks** and part (d) **2 marks**. Official QP lines 745–758 assigns (a) 1, (b) 2, (c) 2, (d) 3. | **FAIL** | In `build_deck.py` lines 100 and 102, change Q5(b) from `3` to `2` and Q5(d) from `2` to `3`; regenerate `P3_Oct2025_Q5.html` and its literal PNG. Acceptance: the displayed labels are Q5(a) 1, Q5(b) 2, Q5(c) 2, Q5(d) 3, total 8. |

## Passed gates

- **Inventory and scope:** exactly five cards/tiles/exports are present: ESAT warm-up and P3 Q2–Q5. The landing’s Q1 and Q6–Q9 scope explanation matches the passed guide coverage map.
- **Maths and source/status boundaries:** checked working is correct: ESAT `R=r(10+√105)`; Q2 IVT values and cube-root rearrangement; Q3 `b=10^0.05`, `T=12.755686…→13`; Q4 `R=2√3`, `α=π/3`, minimum `√3` at `5π/36`; Q5 derivative, `A=19`, and `4000√19/38=458.831467…→459`. Q2(b) is locally disclosed as completed-with-prompting with the transcript/ledger conflict; Q2(c) remains deliberately deferred rather than falsely tutor-attributed.
- **Standalone/UI contract:** all cards have complete headers, question data, part/carry-in structure, grey maskable work, local MathJax SVG, source/status text, a relevant visual where used, and a same-directory Export PNG anchor. No MathJax error text, `mjx-merror`, console/page errors, failed images, or horizontal/element overflow occurred in independent clean Chromium runs at 1280×900 and 390×844.
- **Literal exports and assets:** all 11 learner PNGs decoded successfully. For every card, a fresh desktop `#card` capture with only the Export button suppressed was pixel-identical to the shipped PNG; all manifest-listed release files still matched their recorded SHA-256 values at inspection.
- **Landing, diagrams and privacy:** five local-only landing tiles resolve to the five cards with five loaded preview PNGs on desktop and mobile. Diagram inspections found correct labelled IVT signs/crossing, Q3 line points, R-form/horizontal-compression semantics, surface-area components, and Q5 maximum. The reachable HTML has only local relative asset references; no credentials, paths, external URLs, model/provider/debug terms, or implementation handles were found.

## Required post-fix re-audit

After the three mark-label repairs and regenerated literal PNGs, rerun an independent check of: QP mark labels, manifest hashes/freshness, pixel identity of each PNG export, five-card/landing inventory, and desktop/mobile browser gates. This report is the sole audit write; it is not a publication approval.
