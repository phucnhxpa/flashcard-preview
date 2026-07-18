# Independent downstream re-audit v2 — 16 Jun P1 May 2022

**Disposition: FAIL — release remains blocked.**

## Prior-v1 blocker closure matrix

| Prior blocker | Result | Independent evidence |
|---|---|---|
| Q5 false `+28/3` algebra | **PASS** | Live recomputation: `12 − (4/3)(x+2)^2 = −(4/3)x^2 − (16/3)x + 20/3 = −(4/3)(x−1)(x+5)`. Q5 HTML/PNG show `+20/3`; no `28/3` occurrence. The stated line is `y=−(5/4)x−25/4`. |
| Q5/Q8/Q10 source-limited boundary | **PASS** | Each current card and export visibly state `NOT reviewed live — reference only` and `scored state is unknown`; the three grey panels explicitly prohibit reconstructed step-by-step working and retain only labelled official reference answers. |
| Missing required prompt givens | **PASS** | Q5 includes turning point/intercept/lines/region; Q6 includes both simultaneous equations; Q8 includes radii, angle and arc; Q10 includes curve, normal/tangent relation, `x_A`, intercept and `k` condition. |
| Q1 third masked box | **PASS** | Q1 contains three `.work` boxes, including the visible differentiate-back check. |
| HTML/PNG export parity | **PASS, pair scope** | 10 HTML and 10 PNG stems match. Each card has exactly one same-directory PNG export anchor; all targets exist. Fresh fully-revealed desktop captures were pixel-identical to all ten shipped PNGs. |
| Browser reveal/hide / desktop-mobile / ARIA / MathJax / overflow | **PARTIAL — interaction geometry passes; visual content fails** | Independent local Chromium test at 1400×1000 and 390×844: every card began hidden with one `aria-expanded=false` control; pointer reveal/hide, Enter reveal and Space hide passed; zero console/page errors, `mjx-merror`s, element overflow or document overflow. However Q9 contains visible literal TeX `\(` in its rendered working because `0<p<1` is parsed as HTML rather than math, truncating the rest of that sentence. This is a learner-visible MathJax/source-render failure that the current audit did not detect. |
| Privacy/C0 | **PASS** | All 10 card HTML files have zero C0 bytes other than LF. Scan found no local path, provider/API, token, QA-manifest, or remote-URL leakage in learner HTML. |

## New release blockers

1. **Landing navigation is completely broken.** `index.html` links every one of its 20 card/PNG tile actions as `P1_May2022_Q*.html/png`, but the assets live in `cards/`. All ten “Open multi-step card” and ten landing PNG links resolve to absent root files. The cards' own ten “Back to deck” links use `index.html`, which resolves to absent `cards/index.html`. Thus all 30 learner-navigation links are broken. The static card-pair export anchors themselves are valid.

2. **Q9 has visible malformed math/source text.** The rendered Q9 work panel contains literal `\(` before `0<p<1`; the HTML parser treats `<p<1` as markup, so the intended condition and following prose are not rendered correctly. This is not caught by `mjx-merror` or console checks and is visible in the shipped PNG.

3. **Q6 has a malformed reader-visible subpart label:** `Part (a2)` rather than the intended nested label. The full-resolution shipped PNG confirms the defect.

## Artifact identity and independent checks

- Frozen guide: `guide_v2/revision_guide.pdf` SHA-256 `910d7fca22a783a8433c57ad59c6c5f9585b6b802d7e27be855fc4bb656d66a9`, matching `guide_v2/build_verification.md`; 8 A4 pages, unencrypted.
- Current card inventory: 10 HTML / 10 PNG; every PNG decoded and every card source uses local `../mathjax-tex-svg.js`.
- Fresh browser checks used a local `127.0.0.1` server and system Chromium only. They did not modify bundle artifacts.
- Visual inspection covered all ten PNG exports; Q5/Q8/Q10 boundaries and Q1 third box are visible. Q6 and Q9 defects above are reader-visible.
- No publish, upload, Index, Notion, or learner-asset edit was performed.

**Required release corrections:** repair the landing/card relative hrefs; repair Q9's escaped/HTML-safe `0<p<1` math; repair Q6's part label; regenerate affected artifacts and rerun a fresh independent re-audit.
