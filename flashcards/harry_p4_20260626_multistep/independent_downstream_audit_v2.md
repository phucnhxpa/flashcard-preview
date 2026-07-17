# Independent downstream_v2 release audit v2 — 26 June 2026 Harry P4

## Release verdict: **FAIL**

The rebuild is bound to the authorised final P4 guide and passes the content, provenance, export, privacy, asset, PDF, and responsive-layout checks below. Release is nevertheless blocked by one learner-facing functional/UI defect: the landing tells the learner to **“reveal the grey method boxes”**, but none of the seven cards implements a reveal/hide control. Every work box is already permanently visible.

## Blocking finding — required multi-step reveal UI is absent

- **Reader-visible location:** `index.html`, learner instruction immediately below **“Seven standalone multi-step recall cards”**: “Work from the question, then reveal the grey method boxes.”
- **Current implementation evidence:** `index.html` and all seven `cards/*.html` contain **0** `<button>`, `<details>`, `<input>`, `aria-expanded`, or event-handler elements. Each card has static `.work` elements only (respectively 5, 3, 5, 5, 5, 4, and 4 boxes). Browser exercise confirmed all work is visible without any learner action.
- **Why this fails:** the stated interaction is unavailable, so the landing gives a false learner workflow and the advertised multi-step UI cannot be used for unrevealed recall.

### Exact remediation

Implement an accessible reveal/hide affordance in the generator for every card, then regenerate all seven HTML cards, all seven literal PNG exports, the landing, manifest, and local QA evidence.

1. Give each card a keyboard-operable **Reveal working** control with `aria-controls` and truthful `aria-expanded`; it must reveal and hide that card’s `.work` content without a page reload. Start with the method content hidden if the landing continues to say “then reveal”.
2. Keep the standalone prompt, status boundary, visual, marks/status strip, and final answer readable before reveal; do not use the control to conceal the source-status warning.
3. Capture each literal shipped PNG in the intended fully revealed state (or explicitly change the export label/instruction to describe a prompt-only export). Update the download anchor to the regenerated same-directory PNG.
4. Re-run desktop and 390-px mobile checks for all seven cards: reveal then hide works with keyboard and pointer, `aria-expanded` changes correctly, MathJax remains rendered, no console/page errors occur, and neither state has horizontal overflow.
5. If reveal-on-demand is deliberately out of scope, the alternative minimal correction is to replace the landing instruction with **“Work from the question, then use the grey method boxes to check each step.”** Re-audit the landing and PNGs after that wording change. Do not retain “reveal” without an actual control.

## Passed gates (non-blocking)

| Gate | Independent result |
|---|---|
| Frozen source identity | **PASS.** Current `guide_v2/revision_guide.pdf` SHA-256 is `34ce9ab8dc45d124f39f7d3ecb951bae3c92f607be5f998615628e118457a56a`, exactly the authorised value. The current guide text mirror and source-register hashes are `f3a4b9efe89d5aaf6d8dbf5a119e63d72698ad7acbf11e13f8c42ff5f2fb7f9d` and `45ae38a110fad15fbe877da4309fa900ce6b0d81a8b3536eefb8af509b724f72`. |
| Freshness/provenance | **PASS.** All 29 manifest-listed candidate files match their recorded SHA-256 values; no unlisted candidate files were found. The build has the expected seven P4/P3 targets and the quarantined predecessor is not an input to the current generator. |
| P4 maths, marks and local status boundaries | **PASS.** The recall surface and cards retain the final-guide Q1 expansion/validity/marks, Q2 `200π/3` reference-only boundary, Q4 curve/derivative/two-equation/result and 5+5 marks, Q5 6-mark reference-completion boundary, Q6 7 marks/substitution/result, separate prior-P3 status, and Q8 self-assessed/reference-only status. The sampled full-resolution PNGs for Q1, Q4, Q6 and prior P3 matched the guide mathematics and visible status labels; the remaining cards were independently recomputed from the generated current source. |
| Recall Markdown/HTML/PDF | **PASS.** The current PDF SHA-256 is `c45d1bf589404c8194bff57d5c6bfb23648309a195fa115518eaec5b44fc9d5a`; it is an unencrypted, two-page A4 PDF with embedded fonts, no JavaScript, no links, and no text blocks outside either MediaBox. A fresh 200-dpi two-page render showed no clipping, overlap, broken maths, or page-fragment defect. |
| Seven cards and literal PNG exports | **PASS.** Exactly seven HTML cards and seven corresponding PNGs exist. Each card has a local MathJax asset, local status strip, at least three grey work boxes, and a literal same-directory `download` PNG link. Fresh browser captures at the export viewport were pixel-identical to all seven shipped PNGs. |
| Local assets and reachable surface | **PASS.** All landing and card `href`/`src` targets resolve inside `downstream_v2`; no external runtime asset is required. All seven card pages rendered MathJax, had no browser console/page errors, and had no desktop or 390-px mobile horizontal overflow. The landing exposes seven HTML-card links and seven PNG links without overflow. |
| No 29 June/S1 contamination or public-surface leak | **PASS.** Learner-facing Markdown/HTML and recall-PDF text/raw-byte scans found no `2026-06-29`, `29 June`, `S1`, ESAT, full names, `/root/`, `file://`, URLs, Loom/Slack IDs, source-register/build/QA handles, hashes, or model/provider/debug identifiers. The two generic scanner term hits were ordinary source code colour literals (`#e4f0e9`, `#f0f2f4`) and learner maths prose (`model` in Q8), not public provenance leakage. |
| Desktop/mobile visual inspection | **PASS apart from the reveal defect.** Fresh PDF pages and the shipped desktop/mobile landing renders show legible content, no clipping or overlap, and the seven cards are clearly represented. |

## Scope

No learner artifact, publication target, upload, Index/Notion record, or existing QA/build file was edited. This audit created only `downstream_v2/independent_downstream_audit_v2.md`.
