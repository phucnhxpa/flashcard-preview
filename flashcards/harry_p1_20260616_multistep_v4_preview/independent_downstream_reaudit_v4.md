# Independent downstream re-audit v4 — 16 Jun P1 Q6 repair

**Scope:** narrow, read-only verification of the current local `downstream_v2/` Q6 repair. No learner artifact was rebuilt, edited, published, uploaded, indexed, or otherwise changed by this audit. This report is the sole file created.

## Overall disposition: **PASS**

| Check | Result | Independent evidence |
|---|---|---|
| Q6 learner-visible final answer uses the correct substitution variable | **PASS** | Rendered Q6 final panel visibly states `(2u+5)(u-10)=0`; the factor expression and rejection consistently use `u`, not a mixed `x` variable. Static final-section scan found none of `(2x+5)(x-10)`, `(2x+5)(u-10)`, `(2u+5)(x-10)`, or `x=-5/2`. |
| Required factorisation and rejection | **PASS** | Current HTML and rendered PNG state `(2u+5)(u-10)=0` and `reject u=-5/2`. The working also correctly explains that `u=x^2>=0`, so the negative `u` root is discarded. |
| Frozen guide / official-result agreement | **PASS** | Recomputed frozen guide SHA-256: `910d7fca22a783a8433c57ad59c6c5f9585b6b802d7e27be855fc4bb656d66a9`, matching the generator gate. The frozen guide’s Q6 result is `(2x^2+5)(x^2-10)=0`, reject `x^2=-5/2`, with `(sqrt(10),4sqrt(10))` and `(-sqrt(10),-4sqrt(10))`. With `u=x^2`, the card’s `(2u+5)(u-10)=0`, `u=-5/2` rejection and same signed solution pairs are algebraically identical. |
| Q6 local MathJax / no learner-visible literal TeX | **PASS** | Fresh headless Chromium audit found 77 `mjx-container` elements, no console/page errors, and no visible leaf text containing TeX commands (`\tfrac`, `\sqrt`, `\pm`, or `\displaystyle`). Visual PNG review shows typeset fractions, roots, superscripts and ± signs—not literal TeX. |
| Q6 reveal interaction | **PASS** | Fresh browser test: the working panel began hidden; activating the native control revealed it and set `aria-expanded="true"`. The committed `browser_audit.json` likewise records successful desktop and mobile reveal/hide plus Enter/Space keyboard behavior. |
| Q6 landing link and Back navigation | **PASS** | In a fresh local Chromium session, the landing page exposed exactly one `cards/P1_May2022_Q6.html` link; it loaded Q6, and Q6’s **Back to deck** control returned to `index.html`. |
| PNG freshness / equivalence | **PASS** | `P1_May2022_Q6.png` is a valid 2800×5142 PNG (1,082,263 bytes; SHA-256 `c894c1d72b4e11b84dabf74e014f75faf7cb713d2469760201e1235ed0d6f95a`) timestamped after Q6 HTML and build source. A fresh in-memory canonical fully-revealed Chromium capture had the same dimensions and only negligible raster antialiasing variance (per-channel RMS <= 2.534/255); visual content and layout match. The image visibly includes the corrected final answer with no clipping or variable-mixing defect. |
| Existing browser-audit record | **PASS** | `browser_audit.json` status is `pass`; Q6 desktop/mobile records show no errors, 77 MathJax containers, no horizontal overflow or failed images, and all reveal/ARIA assertions passing. |
| Prior navigation / Q9 / Q6-label regressions remain closed | **PASS** | Q6 now renders exactly one **Part (b)** heading and no legacy `Part (a2)`. The landing page’s Q9 link loads `cards/P1_May2022_Q9.html`; Q9 MathJax renders and its source retains safe `0&lt;p&lt;1` encoding, with no unsafe raw `0<p<1` learner text. Current index labels preserve official numbering: Q6 is **Question 6 — Simultaneous equations to a quartic** and Q9 is **Question 9 — Trig values, y = sin 2x, solve sin 2x = p**. |

## Notes

- The source HTML naturally contains TeX delimiters for MathJax; the pass criterion is learner-visible rendering. The fresh browser audit and direct PNG inspection confirm those delimiters/commands are not exposed to the learner.
- No FAIL conditions remain within the requested Q6 repair scope.
