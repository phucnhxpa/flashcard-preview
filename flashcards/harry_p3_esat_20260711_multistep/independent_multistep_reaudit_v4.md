# Independent re-audit v4 — Harry P3 October 2025 + ESAT `multistep_v2`

## PASS — no release blocker

This is a local-only independent re-audit. I made **no** learner-artifact edits and did **not** publish, upload, or index anything. Every claim below was verified against the **actual on-disk bytes / rendered DOM**, not against the manifest's recorded values or the supplied context narrative. The Q3(b) TAB-in-`\text` corruption that blocked v3 is **fixed and confirmed**, and no regression was introduced.

## Q3(b) answer box — PASS (the prior blocker is resolved)

Verified at both the source-byte and rendered-DOM levels:

- **Source bytes** (`P3_Oct2025_Q3.html`): the Q3(b) answer box string is
  `…(10^{0.05})^t;\\ a=100,\\ b=1.12\\text{ (3 s.f.)}}…`
  i.e. **two** literal backslashes before `text` (correct MathJax `\text`), **0 TAB (0x09)**, **0 control bytes** (<0x20 except LF). `grep -c $'\t'` over all `*.html` = 0.
- **On-disk SHA**: `P3_Oct2025_Q3.html` = `724261358e3f2eec413ea0cd71cbc884c273915cc701976f493a18ab7e876951` (10928 bytes). This is the **fixed** file and it is the one the refreshed manifest now pins (see Manifest gate).
- **Rendered DOM** (chromium `--headless --dump-dom` of the shipped file, MathJax tex-svg): the Q3(b) boxed answer renders as
  `V = 100 ( 10 0.05 ) t ; a = 100 , b = 1.12 (3 s.f.)`
  with MathML `<mn>1.12</mn><mtext> (3 s.f.)</mtext>` — i.e. `1.12 (3 s.f.)` with a proper space mtext.
- **Bug signature absent**: literal `ext(` is **NOT FOUND** anywhere in the Q3 rendered DOM; a `[digit]ext[{(` corruption scan across all five rendered DOMs returned **0 hits**.

The v3 defect class (`\t`-escape → TAB → `1.12ext(3 s.f.)`) is gone.

## Q5 answer boxes — PASS (no regression, consistent with the prior v3 fix)

- **Source bytes**: `P3_Oct2025_Q5.html` has **0 TAB**, **0 control bytes**. Correct strings present: `\\boxed{200\\text{ squirrels}}`, `\\boxed{459\\text{ squirrels}}` (doubled backslash, no TAB).
- **Rendered DOM** boxed answers: `200 squirrels`, `459 squirrels`. `ext(` absent.
- **Maths re-derivation (independent)**: with `N(t)=4000 e^{0.1t}/(19+e^{0.2t})`: `N(0)=200` ✓, `e^{0.2T}=19 ⇒ T≈14.72`, `Nmax=458.831…→459` ✓.

## Mark labels — PASS (rechecked, no invented badges)

Rendered part-title / marks badges match QP allocations:
- ESAT: 2, 3. Q2: 2, 2, 3. Q3: 2, 3, 4. Q4: 3, then **one combined (b)(i)–(ii) = 3 marks** with **no invented (b)(ii) badge** (the sub-label "smallest x" appears without its own marks badge). Q5: 1, 2, 2, 3.

## Export parity — PASS

All five cards retain a literal same-directory `href="{slug}.png">Export PNG` anchor and the target PNG exists:
- ESAT_warmup.png ✓, P3_Oct2025_Q2.png ✓, P3_Oct2025_Q3.png ✓, P3_Oct2025_Q4.png ✓, P3_Oct2025_Q5.png ✓.

## Manifest / inventory — PASS (internally consistent and now pins the *fixed* Q3)

- `build_manifest.json` SHA-256 (of the file itself) = `d81ac2585bc1b112ae9de37f1ccd7f3180ff3b5e4ddc6669bed4ce33a843ad3a` — exactly the refreshed hash supplied in context.
- **All 29 manifest entries** matched their recorded `sha256` **and** `bytes` counts (0 mismatches); no unlisted/missing files.
- The pinned `P3_Oct2025_Q3.html` sha (`724261358e…`, 10928 bytes) is the **fixed** file — the manifest no longer pins the corrupted `fe147ed1…` version that v3 flagged.
- Guide provenance SHA-256 = `a7edca885f0234211279ebbf32bd183722264a9788dc7899c0381c9e4fba2dcf` matches the declared authorised hash; the guide file exists.
- Source-bounded inventory is exactly five card/PNG pairs (ESAT + P3 Q2–Q5); Q1 and Q6–Q9 correctly omitted per scope. `independent_review.status = not_recorded`, `publication.status = local_only`.

## Browser gates — PASS

- Existing `browser_audit.json` (Playwright + /usr/bin/chromium; desktop 1280×900@2, mobile 390×844@1): all five cards clean — 0 console warnings/errors, 0 page errors, 0 MathJax errors, no horizontal/element overflow; MathJax containers 35/41/59/48/49; landing 5 tiles / 5 images; asset-resolution failures 0. Recorded desktop screenshot byte counts match the shipped desktop PNGs exactly.
- **Independent chromium render** of every answer box across all five cards found clean output for ESAT, Q2, Q3, Q4, Q5 — specifically **no `[digit]ext` corruption** (the v3 blocker). The browser_audit entry is itself one of the 29 manifest entries and matched.

## Maths / status / privacy — PASS

- **Maths** (independent re-derivation): Q3 `b=10^{0.05}=1.122018…→1.12` (3 s.f.) ✓; Q5 `N(0)=200`, `Nmax=458.831…→459` ✓ (Q5(a)/Q5(d)). Q2/Q4 confirmed in v3 and unchanged here.
- **Status badges** intact: ESAT "Solved on board", Q2 "Reviewed / prompted / deferred", Q3/Q4/Q5 "Solved"; P3 cards carry "official-paper text in passed guide".
- **Privacy**: scan of all learner-facing HTML — **0** email, **0** `http(s)://` URL, **0** absolute `/root` path, **0** token/api-key/password/secret hits. Text-file control-char scan: **0** TAB/CR/0x0b/0x0c/0x00/DEL across all `*.html/*.js/*.py/*.md/*.json/*.css/*.txt`.

## Verdict

**PASS — no release blocker.** The Q3(b) TAB-in-`\text` corruption (`b=1.12\text{ (3 s.f.)}` → `1.12ext(3 s.f.)`) that failed v3 is fixed: the shipped `P3_Oct2025_Q3.html` now renders `1.12 (3 s.f.)` with no TAB/ext (verified source + DOM), and the manifest pins this fixed file with a matching refreshed hash. Q5(a)/Q5(d) remain clean. All other gates — mark labels, export parity, manifest integrity/freshness, browser cleanliness, maths, status, and privacy — pass on independent verification of the actual artifacts.

*This report is the sole new audit write and is not a publication approval.*
