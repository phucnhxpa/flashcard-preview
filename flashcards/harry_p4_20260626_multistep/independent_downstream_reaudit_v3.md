# Independent downstream_v2 release re-audit v3 — 26 June 2026 Harry P4

## Release verdict: **FAIL**

The repaired reveal/hide interaction is independently verified and **passes** across every card at both required viewports. The candidate is nevertheless **not release-ready** because the reader-facing two-page recall PDF has a visible page-fragment defect: the P4 Q4 section begins on page 1, but its final `Official reference answer: P=(2,8); reject (6,0) because b>0.` bullet is stranded at the top of page 2 with no repeated section heading or continuation label. This contradicts the prior claim of no page-fragment defect and fails the full visual-layout release gate.

No learner artifact, source, build file, publication target, upload, Index/Notion record, or remote system was modified. This report is the only persistent write.

## 1. Repaired reveal/hide UI — PASS

I did not rely on `reveal_ui_repair_qa_v1.md` or `browser_audit.json`. I served the retained artifact locally and independently exercised all seven card pages in Chromium at **1400×900** and **390×844**: **14 card/viewport records**, with zero failed assertions and zero console/page errors.

| Requirement | Independent result |
|---|---|
| Initial state | **PASS.** Each card has exactly one native `button.reveal-control`, labelled `Reveal working`, with `aria-expanded="false"`; its uniquely matched `aria-controls` panel starts `hidden`, not visible, and exposes no work box. |
| Required pre-reveal content | **PASS.** Marks, status, standalone prompt, concept visual, recall answer, and study boundary remained visible on all 14 records. |
| Pointer interaction | **PASS.** All 14 controls changed to `Hide working`, `aria-expanded="true"`, exposed the controlled panel and every work box, then returned correctly to the hidden/reveal state on a second click. |
| Keyboard interaction | **PASS.** All 14 controls responded to **Enter** for reveal and **Space** for hide, with the same truthful state transition. |
| ARIA and navigation | **PASS.** Every control's `aria-controls` exactly matched its panel ID; each no-reload sequence had `false → true → false → true → false` expanded states. |
| Render/responsiveness | **PASS.** MathJax rendered on every card; neither collapsed nor revealed state had horizontal overflow at either viewport. The 390px landing also visibly retains the learner instruction: “Work from the question, then reveal the grey method boxes.” |

Static source cross-check: all seven retained cards have one unique control/panel pair and respectively **5, 3, 5, 5, 5, 4, 4** grey working boxes, plus the click handler that toggles `hidden`, `aria-expanded`, and the visible label.

## 2. Retained non-interaction gates

| Gate | Independent result |
|---|---|
| Frozen guide identity and authorised inputs | **PASS.** SHA-256 values directly recomputed: final guide PDF `34ce9ab8dc45d124f39f7d3ecb951bae3c92f607be5f998615628e118457a56a`; guide-text mirror `f3a4b9efe89d5aaf6d8dbf5a119e63d72698ad7acbf11e13f8c42ff5f2fb7f9d`; source register `45ae38a110fad15fbe877da4309fa900ce6b0d81a8b3536eefb8af509b724f72`. Each matches `build_manifest.json`. I read the retained guide text and source register directly; their P4 question/status crosswalk supports the supplied Q1/Q2/Q4/Q5/Q6/Q8 and separated prior-P3 content. |
| Manifest integrity / candidate freshness | **PASS.** All **32/32** manifest-listed file hashes matched current bytes. The manifest identifies exactly seven P4/P3 card HTML derivatives and seven corresponding PNG exports, with no publication action. |
| Maths, marks, and status boundaries | **PASS.** Learner surfaces retain the final-guide markers: corrected Q4 curve and `2a+b=12`, `P=(2,8)`, Q5 `β=−40`, Q6 `8√3−40/3`, Q2 `200π/3`, self-assessed/reference-only labels, and the separate prior-P3 status. The stale Q4 equation, `4a+b=12`, old derivative, invented nine marks, and contamination/private markers were absent from learner surfaces. |
| Local assets and reachable surface | **PASS.** All landing/card local href/src targets resolve; no external runtime reference is present. Landing exposes seven HTML and seven PNG links at desktop and mobile without overflow. |
| Literal PNG exports | **PASS.** Exactly seven decodable RGB PNGs exist, each at least 1400px wide. Fresh fully revealed Chromium captures were pixel-identical to each shipped PNG for all 7/7 cards, proving the downloadable exports include the grey working rather than the collapsed state. The contact-sheet review found the grey boxes present and no apparent clipping, overlap, unreadable maths, or broken card layout. |
| Privacy / contamination | **PASS.** Learner-facing HTML/Markdown scans found no 29-June/S1 lane marker, private path, full name, external URL/runtime dependency, legacy wrong-Q4 marker, old derivative, or unsupported nine-mark claim. |
| Recall PDF technical integrity | **PASS.** `harry_p4_recall.pdf` is an unencrypted two-page A4 PDF with no JavaScript, forms, URI annotations, or embedded files. Its extracted text had no scanned private/stale markers. |

## 3. Blocking visual-layout regression — FAIL

**Artifact:** `harry_p4_recall.pdf`, transition from page 1 to page 2.

A fresh visual inspection of the retained rendered PDF pages shows:

- Page 1 opens the P4 Q4 section and displays its heading plus the first three bullets.
- Page 2 begins directly with the remaining bullet: **“Official reference answer: P=(2,8); reject (6,0) because b>0.”**
- That bullet has no P4 Q4 heading, repeated context, or continuation indication on page 2.

Nothing is clipped or overlapping, but the split leaves a structurally orphaned answer at the top of the next page. Under the full release gate, this is a reader-visible page-fragment defect. It must be repaired (for example, keep the complete Q4 list together or move the Q4 heading/list to page 2) and then re-rendered and independently re-audited. Do not release the current candidate.

## Scope

The repaired reveal/hide requirement is closed **PASS**. The overall downstream_v2 release decision is **FAIL** solely because of the retained recall-PDF page fragmentation. No publish/upload/Index action was performed.
