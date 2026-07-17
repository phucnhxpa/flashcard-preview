# Independent re-audit v3 — Harry P3 October 2025 + ESAT `multistep_v2`

## FAIL — do not release

This is a local-only independent re-audit. I made **no** learner-artifact edits and did **not** publish, upload, or index anything. I verified the Q5 TeX fix requested by this audit **and** independently rendered *every* answer box across all five cards (not just Q5), which surfaced a second, previously-unflagged corruption of the identical root cause. The Q5 fix itself is good; the deck is still blocked by a sibling regression in Q3(b).

## Q5 answer-box TeX fix — PASS (as requested)

Independent checks at both the source-byte and rendered-DOM levels confirm the Q5 fix:

- `P3_Oct2025_Q5.html` source bytes: **0 TAB (0x09)**, **0 control bytes** (<0x20 excl. LF/CR).
- Source strings present and correct: `\boxed{200\text{ squirrels}}` and `\boxed{459\text{ squirrels}}` (doubled backslash, no TAB).
- Rendered DOM (actual MathJax output, chromium `--dump-dom` of the current shipped file):
  - `ANSWER BOX: '200 squirrels'` ✔
  - `ANSWER BOX: '459 squirrels'` ✔
  - Bug signature `'ext squirrels'` **absent** from the rendered DOM.
- A standalone MathJax render of the exact source TeX produced verbatim `200 squirrels` and `459 squirrels` with no stray `ext`.

The Q5(a)/Q5(d) regression from v2 is fixed.

## NEW regression — Q3(b) answer box — FAIL (release blocker)

The v2 reaudit only re-checked Q5 and so missed this. The same `\t`-in-`\text` bug class corrupts Q3(b):

- `P3_Oct2025_Q3.html` source bytes contain a literal **TAB (0x09)** at offset 6423, immediately before `ext{`:
  `…b=1.12<TAB>ext{ (3 s.f.)}…`
- Rendered DOM of the current shipped `P3_Oct2025_Q3.html` answer box:
  - `ANSWER BOX: 'V=100(10^{0.05})^t; a=100, b=1.12ext(3 s.f.)'` — renders as **`1.12ext(3 s.f.)`** instead of `1.12 (3 s.f.)`. ✘
- Root cause located in `build_deck.py` line 87 (Q3 part b builder string):
  `…\\\\ b=1.12\text{ (3 s.f.)}…`
  The `\text` here uses a **single** backslash, so `\t` is a Python TAB escape → TAB byte in the HTML → MathJax emits the literal `ext` text. The v2 fix doubled the backslash for Q5(a)/Q5(d) (`\\\\text{`) but **missed Q3(b)**.
- This is reader-visible corruption in a learner artifact (same defect class that blocked v2). The deck is not release-ready.

### Required remediation (not applied — audit only)
In `build_deck.py` line 87, change `b=1.12\text{ (3 s.f.)}` → `b=1.12\\text{ (3 s.f.)}` (two source backslashes), then regenerate the Q3 card HTML/PNG, the dependent `browser_audit.json`/contact sheets, and the manifest; re-verify Q3(b) render and re-run all parity/manifest gates.

## Mark labels — PASS (rechecked)

Rendered part-titles / marks badges match the QP allocations and the v2 repair held:
- ESAT: 2, 3. Q2: 2, 2, 3. Q3: 2, 3, 4. Q4: 3, then one combined (b)(i)–(ii) 3, with **no invented (b)(ii) badge**. Q5: 1, 2, 2, 3.

## Export parity — PASS

All five cards retain a literal same-directory `href="{slug}.png"` Export-PNG anchor and the target PNG exists with the shipped byte counts (ESAT 922127, Q2 1119291, Q3 1117039, Q4 1219347, Q5 1220700).

## Manifest / inventory — PASS (internally consistent, but pins the *corrupted* Q3)

- `build_manifest.json` SHA-256 is exactly `6aa8a403371b0cbbf53e05741847be80cc8400edb69ebb7328f6d9ff146347cd` (matches expected).
- All **26** manifest entries existed and matched their recorded byte counts and SHA-256 values; no unlisted/missing files.
- Guide provenance SHA-256 `a7edca885f0234211279ebbf32bd183722264a9788dc7899c0381c9e4fba2dcf` matches the declared authorised hash.
- Source-bounded inventory is exactly five card/PNG pairs (ESAT + P3 Q2–Q5); Q1 and Q6–Q9 correctly omitted per scope.
- Caveat: the manifest currently pins the *corrupted* Q3 file (sha `fe147ed1…`, 10927 bytes), so it is internally consistent with a bad artifact — it must be regenerated after the Q3(b) fix.

## Browser gates — PASS except the Q3(b) corruption

- Existing `browser_audit.json` (Playwright + /usr/bin/chromium, desktop 1280×900@2, mobile 390×844@1): all five cards clean — 0 console warnings/errors, 0 page errors, 0 MathJax errors, no horizontal/element overflow, MathJax containers 35/41/59/48/49, landing 5 tiles / 5 images, asset-resolution failures 0.
- My own independent chromium render of every answer box across all five cards found clean output for ESAT, Q2, Q4, Q5 — **except Q3(b)** (the corruption above). Desktop screenshot byte counts recorded in `browser_audit.json` match the shipped desktop PNGs exactly.

## Maths / status / privacy — PASS

- Independent numerical re-derivation confirms all results: Q2 f(1)<0, f(2)>0; Q3 T=12.755686→13, b=10^0.05=1.122→1.12 (3 s.f.); Q4 R=2√3, α=π/3, min g=√3 at x=5π/36; Q5 N(0)=200, e^{0.2T}=19, Nmax=458.831467→459. Q2(b) prompted/conflicting-evidence disclosure and Q2(c) deferred boundary remain present.
- Status badges intact: ESAT "Solved on board", Q2 "Reviewed / prompted / deferred", Q3/Q4/Q5 "Solved", all "official-paper text in passed guide".
- Privacy: no `http(s)://` URLs, no absolute `/root` path, no email, no token/api-key/password, no card-number hit in any learner-facing HTML.

## Verdict

**FAIL — do not release.** The requested Q5(a)/Q5(d) TeX fix is confirmed clean (renders `200 squirrels` / `459 squirrels`, no TAB/control byte). However, the re-audit's "no regression" condition fails: a sibling TAB-in-`\text` corruption in **Q3(b)** (`b=1.12\text{ (3 s.f.)}` → renders `1.12ext(3 s.f.)`) — the same root cause v2 fixed only in Q5 — remains in the shipped artifact. All other gates (mark labels, exports, manifest integrity/freshness, browser cleanliness, maths, status, privacy) pass. Remediate Q3(b) in `build_deck.py`, regenerate Q3 + manifest, and re-run verification before release.

*This report is the sole new audit write and is not a publication approval.*
