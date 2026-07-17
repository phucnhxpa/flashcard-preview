# Independent re-audit — Harry P3 October 2025 + ESAT `multistep_v2`

## FAIL — do not release

This is a local-only independent re-audit after the mark-label repair. I made no learner-artifact edits and did not publish, upload, or index anything. The repaired official marks, manifest integrity/freshness, five-card inventory, literal-export parity, and desktop/mobile layout all pass. Release remains blocked by a newly observed reader-visible Q5 TeX/text rendering regression that corrupts two final-answer units.

## Official QP mark-label repair — PASS

Official QP text was checked directly:

- **Q2:** QP lines 288–305 allocate **(a) 2, (b) 2, (c) 3**. Rendered HTML at desktop/mobile and the literal `P3_Oct2025_Q2.png` show exactly `2 marks`, `2 marks`, `3 marks`.
- **Q4:** QP lines 641–660 allocate **(a) 3** and one combined **(b)(i)–(ii) 3**. Rendered HTML at desktop/mobile and literal `P3_Oct2025_Q4.png` show `Part (a) … 3 marks`, then one `Part (b)(i)–(ii) … 3 marks`; the later (b)(ii) working section has **no** invented individual mark badge.
- **Q5:** QP lines 745–758 allocate **(a) 1, (b) 2, (c) 2, (d) 3**. Rendered HTML at desktop/mobile and literal `P3_Oct2025_Q5.png` show exactly `1`, `2`, `2`, `3` marks.

The repaired allocations agree with the card totals (Q2 7, Q4 6, Q5 8).

## Manifest, inventory, and export parity — PASS

- `build_manifest.json` SHA-256 is exactly `0b28080e59546d02e49a0781f670c5e3bea1a77ecf045104103cede0a9f60973`.
- All **26** manifest entries existed and matched their recorded byte counts and SHA-256 values; there were no unlisted pre-audit files and no missing files. The passed-guide SHA-256 also matched the declared `a7edca885f0234211279ebbf32bd183722264a9788dc7899c0381c9e4fba2dcf`.
- The source-bounded inventory is exactly five card/PNG pairs: ESAT warm-up plus P3 Q2–Q5. Each HTML card retains a literal same-directory Export-PNG anchor.
- A fresh independent Chromium desktop `#card` capture for **each of the five cards** was pixel-identical to its shipped PNG. PNGs opened successfully for comparison.
- Landing page inventory is five tiles/five loaded previews at desktop and mobile.

## Browser gates — PASS

Independent Chromium runs used 1280×900 desktop (scale 2) and 390×844 mobile (scale 1):

- all five cards: no console warnings/errors, page errors, failed requests, MathJax errors, horizontal overflow, element overflow, or failed images;
- MathJax rendered on every card (35/41/59/48/49 containers respectively);
- landing page: no errors/overflow and five loaded tiles/previews in both viewports.

## Earlier maths, status, privacy, and source boundary — FAIL (Q5 rendering regression)

Independent numerical checks still confirm the prior mathematical results: Q2 endpoint signs and fixed-point residual; Q3 `T=12.755686… → 13`; Q4 `R=2√3`, `α=π/3`, minimum `√3` at `5π/36`; and Q5 `e^(0.2T)=19`, maximum `458.831467… → 459`. Q2(b)'s prompted/conflicting evidence disclosure and Q2(c)'s deferred boundary remain present. The deck still omits Q1 and Q6–Q9 according to the passed-guide scope. Learner-facing HTML has no external URLs, absolute `/root` path, source-register identifier, email, token/API-key, password, or card-number hit.

However, **P3 Q5's reader-visible final answers are malformed**:

- In `P3_Oct2025_Q5.html`, the source bytes contain a literal TAB (`0x09`) in each intended `\text{ squirrels}` command—two tabs total. The affected answer source is at the Q5(a) and Q5(d) builder strings (lines 100 and 103).
- The literal PNG visibly renders the answers as **`200ext squirrels`** and **`459ext squirrels`**, rather than `200 squirrels` and `459 squirrels`. Thus the numeric values are right, but both units/text commands are wrong in the learner artifact.
- `python3 -W error::SyntaxWarning -m py_compile build_deck.py` passes because `\t` is a legal Python tab escape; that command does not catch this TeX corruption.

### Required remediation

In the non-raw Q5 builder strings, represent the TeX command as `\\text{ squirrels}` (two source backslashes), then regenerate the affected HTML/PNG and all dependent audit/manifest artifacts. Re-run browser-body/PNG verification explicitly for the two Q5 answer boxes as well as the existing mark-label, parity, manifest, and viewport gates.

This report is the sole new audit write and is not a publication approval.
