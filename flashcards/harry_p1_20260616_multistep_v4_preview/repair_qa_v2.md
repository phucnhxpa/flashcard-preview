# Repair QA v2 — 16 Jun P1 May 2022 downstream_v2

**Disposition: PASS — all three re-audit-v2 blockers repaired locally.** No publish, upload, Index, Notion, guide, or other lesson artifact was changed.

## Scope and frozen-guide gate

- Edited only this `downstream_v2/` directory.
- Recomputed `guide_v2/revision_guide.pdf` SHA-256: `910d7fca22a783a8433c57ad59c6c5f9585b6b802d7e27be855fc4bb656d66a9`.
- The value matches the generator gate and `guide_v2/build_verification.md`; `pdfinfo` reports 8 pages and `Encrypted: no`.
- `build_deck.py` and `render_and_audit.py` compile with `PYTHONDONTWRITEBYTECODE=1 python3 -W error::SyntaxWarning -B -m py_compile`.

## Repairs

1. **Learner navigation**
   - Landing tile card actions now use `cards/P1_May2022_Q*.html`.
   - Landing tile PNG actions now use `cards/P1_May2022_Q*.png`.
   - Every card Back to deck action now uses `../index.html`.
2. **Q9 HTML-safe math**
   - The literal mathematical condition is authored as `\(0&lt;p&lt;1\)`, so HTML parses the entities safely before local MathJax renders the condition.
   - The regenerated HTML contains the safe entity form and no raw `0<p<1` sequence.
3. **Q6 reader label**
   - The second section is now `Part (b)`, not `Part (a2)`.
   - This follows the frozen official prompt and source manifest, which specify Q6 as `(a) show ...` then `(b) hence solve ...` (marks `(a2, b5)`); a nested `(a)(ii)` label would not be source-supported.

## Regeneration and checks

- Regenerated `index.html`, all 10 `cards/P1_May2022_Q*.html`, all 10 canonical fully-revealed `cards/P1_May2022_Q*.png`, `desktop_landing.png`, `mobile_landing.png`, and `browser_audit.json`.
- Static link check: **PASS** — 20 landing actions + 10 card back links = **30/30 resolved local targets**.
- Browser audit: **PASS** — 10 cards × desktop/mobile = 20 card records, plus two landing records; no console/page errors, failed images, horizontal/document overflow, MathJax errors, or reveal/ARIA failures.
- Export validation: 10/10 PNGs decode and each is not older than its matching HTML.
- Strict-clean scan: 11 learner HTML files have no C0 controls other than LF and no checked internal-path/provider/token markers.
- Visual review of regenerated exports: Q9 visibly renders `0 < p < 1` as math with the complete sentence present (no literal TeX or truncation); Q6 visibly shows `Part (b)` and is readable.

## Selected resulting hashes

- `browser_audit.json`: `89836e0d7a42cffa758059e377811df82ae86ff6e87656c8471eff909a9df065`
- `index.html`: `c5f507925ec44a06bbd23958c8b8a95afcd5976873f5bd18fec32356a37e5fbf`
- `cards/P1_May2022_Q6.html`: `46c74ebdaba4f547ee930434b4f15ac4e3a27989911bfc3eb31c0cebb2cf85b6`
- `cards/P1_May2022_Q6.png`: `576753194fbdfade41b0553d42d8c038b56f3eab036383b220c16bf0019cc534`
- `cards/P1_May2022_Q9.html`: `1add5e956f24ebbce3369acb18327484024b73bfa78abe897895383ad266bb63`
- `cards/P1_May2022_Q9.png`: `03b0c500a11b8cd100baf94e4f1ea3a29a16971d11dd722829a90d448ebb401a`
