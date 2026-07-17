# Reveal/hide work-box repair QA v1 — 26 June Harry P4 downstream_v2

## Result: PASS — local-only repair; no publication action

## Implemented behaviour

- `build_clean_downstream.py` now emits one native `button.reveal-control` in each of the seven cards. It starts as **Reveal working**, with `aria-expanded="false"` and a unique `aria-controls` reference to that card's unique `.work-panel`.
- Each panel starts with the HTML `hidden` attribute, so the grey `.work` boxes are not exposed until the learner activates the control. The click handler toggles both `hidden` and `aria-expanded`, and changes the accessible visible label between **Reveal working** and **Hide working** without navigation/reload.
- The standalone prompt, marks strip, status boundary, concept visual, recall answer and study boundary are outside the hidden panel and were required to be visible before reveal.
- `render_clean_assets.py` now activates the control before capturing each literal card PNG. All seven shipped PNGs therefore show the fully revealed grey method boxes; their same-directory `download` anchors remain intact.

## Browser interaction evidence

Local Chromium checks covered every card at **1400×900 desktop** and **390×844 mobile**: **14 card/viewport records** in `browser_audit.json` (SHA-256 `50df812ee92189ff9783d7ec912239be0f164f1f28bbf2206e6c29dbbd6150c1`).

| Check | Evidence/result |
|---|---|
| Initial state | 7/7 cards × 2 viewports began collapsed: `aria-expanded=false`, controlled panel `hidden`, required standalone content visible. |
| Pointer | 14/14 pointer sequences clicked **Reveal working** then **Hide working**; grey work became visible then hidden. |
| Keyboard | 14/14 native-button sequences used **Enter** to reveal and **Space** to hide. |
| ARIA | 14/14 records verified that `aria-controls` exactly named the unique controlled panel and that `aria-expanded` transitioned `false → true → false → true → false`. |
| Reload | 14/14 sequences retained the same navigation entry count. |
| Responsive/rendering | 14/14 records confirmed MathJax rendering and no horizontal overflow while collapsed or revealed. Browser console errors: 0; page errors: 0. |

## Regenerated dependent artifacts

- Seven card HTML files and seven literal same-directory card PNG exports.
- `index.html`, `desktop_landing.png`, `mobile_landing.png`, `cards_contact_sheet.png`, and `recall_pdf_contact_sheet.png`.
- `browser_audit.json`, `qa_report.md`, and `build_manifest.json`.
- The reader-safe recall Markdown/HTML/PDF and two 200-dpi PDF page renders were also rebuilt as part of the deterministic local build chain. The PDF remains two pages and unencrypted.

## Static and visual QA

- Source contract check: each card has exactly one reveal button, one initially hidden controlled panel, and respectively 5, 3, 5, 5, 5, 4 and 4 grey work boxes.
- All 7 PNGs passed Pillow decode/dimension checks. The regenerated `cards_contact_sheet.png` was visually inspected: all grey work boxes are present in fully revealed exports, with no observed clipping, overlap or unreadable rendering.
- The regenerated 390-px landing capture visibly retains “Work from the question, then reveal the grey method boxes” and has no observed clipping or horizontal overflow.
- Learner HTML/Markdown/PDF text scans, local asset/link checks, PDF facts, frozen-guide hash proof, and C0-byte guard all passed in `qa_clean_downstream.py`.

## Scope

This record is local QA, not an independent audit. No publish/upload/Index/Notion/remote write was performed.
