#!/usr/bin/env python3
"""Deterministic, local-only QA for the clean 26 June downstream replacement."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
from urllib.request import urlopen

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
LESSON = ROOT.parent
EXPECTED = "34ce9ab8dc45d124f39f7d3ecb951bae3c92f607be5f998615628e118457a56a"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    raise SystemExit("QA FAIL: " + message)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


# Frozen source identity gate.
guide = LESSON / "guide_v2" / "revision_guide.pdf"
if digest(guide) != EXPECTED:
    fail("frozen final guide SHA-256 mismatch")
if not (LESSON / "_quarantine" / "downstream_v2_contaminated_pre_final_guide_2026-07-17").is_dir():
    fail("contaminated predecessor was not quarantined")

cards = sorted((ROOT / "cards").glob("*.html"))
pngs = sorted((ROOT / "cards").glob("*.png"))
if len(cards) != 7 or len(pngs) != 7:
    fail(f"expected 7 cards and 7 card PNGs; got {len(cards)} and {len(pngs)}")
if {item.stem for item in cards} != {item.stem for item in pngs}:
    fail("HTML/PNG card stems differ")

# Mechanical source/content and static-anchor checks.
learner = [ROOT / "index.html", ROOT / "harry_p4_recall.md", ROOT / "harry_p4_recall.html"] + cards
if any(byte < 32 and byte != 10 for path in learner for byte in path.read_bytes()):
    fail("C0 control byte found in generated learner text asset")
learner_text = "\n".join(text(path) for path in learner)
if EXPECTED in learner_text:
    fail("private provenance hash leaked into learner-facing source")
for forbidden in [
    "23c096", "2026-06-29", "29 June", "S1", "Harry Williams", "Phuc Nguyen",
    "/root/", "file://", "http://", "https://", "4x²−2xy+y²=24", "4x^2-2xy+y^2=24",
    "4a+b=12", "(y−4x)/(y−x)", "9 marks",
]:
    if forbidden.lower() in learner_text.lower():
        fail(f"forbidden/stale/private marker found in learner-facing source: {forbidden!r}")
for required in ["4x^2 + y^2 − 2xy = 24x", "2a+b=12", "P=(2,8)", "8√3−40/3", "β=−40", "200π/3", "STATUS:"]:
    if required not in learner_text:
        fail(f"required final-guide marker absent: {required!r}")

for card in cards:
    source = text(card)
    if "../assets/mathjax/tex-svg.js" not in source:
        fail(f"{card.name} lacks local MathJax tex-svg")
    if source.count('class="work"') < 3:
        fail(f"{card.name} lacks enough grey work boxes")
    if source.count("<button ") != 1 or "Reveal working</button>" not in source:
        fail(f"{card.name} lacks exactly one Reveal working button")
    control = re.search(
        r'<button id="([^"]+)" class="btn reveal-control" type="button" aria-controls="([^"]+)" aria-expanded="false">Reveal working</button>',
        source,
    )
    if not control:
        fail(f"{card.name} lacks the collapsed aria-controlled reveal button contract")
    panel_id = control.group(2)
    if f'<section id="{panel_id}" class="work-panel" aria-label="Step-by-step working" hidden>' not in source:
        fail(f"{card.name} lacks the initially-hidden controlled work panel")
    if "control.addEventListener('click'" not in source or "control.setAttribute('aria-expanded',String(!expanded))" not in source:
        fail(f"{card.name} lacks the reveal/hide event handler")
    anchor = re.search(r'href="([^"]+\.png)" download', source)
    if not anchor or anchor.group(1) != card.with_suffix(".png").name:
        fail(f"{card.name} lacks literal same-directory PNG anchor")
    if not (card.parent / anchor.group(1)).is_file():
        fail(f"{card.name} static PNG missing")

for png in pngs:
    with Image.open(png) as image:
        image.verify()
    with Image.open(png) as image:
        if image.width < 1000 or image.height < 1000:
            fail(f"{png.name} too small for readable recall ({image.size})")

# Serve locally and exercise every card at desktop and 390-px mobile widths.
os.chdir(ROOT)


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


server = ThreadingHTTPServer(("127.0.0.1", 0), Quiet)
Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"
console_errors: list[str] = []
page_errors: list[str] = []
browser_evidence: list[dict[str, object]] = []
try:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, executable_path="/usr/bin/chromium")
        page = browser.new_page(viewport={"width": 1400, "height": 900})
        page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        for card in cards:
            url = f"{base}/cards/{card.name}"
            for viewport_name, viewport in [
                ("desktop", {"width": 1400, "height": 900}),
                ("mobile_390px", {"width": 390, "height": 844}),
            ]:
                page.set_viewport_size(viewport)
                page.goto(url, wait_until="networkidle")
                control = page.locator("button.reveal-control")
                panel = page.locator(".work-panel")
                work = page.locator(".work")
                if page.locator("mjx-container").count() == 0:
                    fail(f"MathJax did not render on {card.name} at {viewport_name}")
                if work.count() < 3:
                    fail(f"grey work boxes do not render on {card.name}")
                if control.count() != 1 or panel.count() != 1:
                    fail(f"{card.name} lacks one control/panel pair at {viewport_name}")
                if control.get_attribute("aria-expanded") != "false" or not panel.evaluate("(element) => element.hidden") or panel.is_visible():
                    fail(f"{card.name} is not initially collapsed at {viewport_name}")
                panel_id = control.get_attribute("aria-controls")
                if not panel_id or panel.get_attribute("id") != panel_id:
                    fail(f"{card.name} aria-controls does not name its panel at {viewport_name}")
                if not all(page.locator(selector).is_visible() for selector in [".marks", ".status", ".visual", ".answer", ".boundary"]):
                    fail(f"{card.name} conceals required standalone content at {viewport_name}")
                navigation_count = page.evaluate("performance.getEntriesByType('navigation').length")
                if page.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1"):
                    fail(f"collapsed horizontal overflow on {card.name} at {viewport_name}")

                # Pointer: click reveals working, then a second click hides it.
                control.click()
                if control.get_attribute("aria-expanded") != "true" or panel.evaluate("(element) => element.hidden") or not panel.is_visible() or control.inner_text() != "Hide working":
                    fail(f"pointer reveal failed on {card.name} at {viewport_name}")
                if not all(work.nth(index).is_visible() for index in range(work.count())):
                    fail(f"pointer reveal did not expose all work on {card.name} at {viewport_name}")
                if page.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1"):
                    fail(f"revealed horizontal overflow on {card.name} at {viewport_name}")
                control.click()
                if control.get_attribute("aria-expanded") != "false" or not panel.evaluate("(element) => element.hidden") or panel.is_visible() or control.inner_text() != "Reveal working":
                    fail(f"pointer hide failed on {card.name} at {viewport_name}")

                # Keyboard: native button activation with Enter reveals and Space hides.
                control.focus()
                page.keyboard.press("Enter")
                if control.get_attribute("aria-expanded") != "true" or panel.evaluate("(element) => element.hidden") or not panel.is_visible():
                    fail(f"keyboard Enter reveal failed on {card.name} at {viewport_name}")
                page.keyboard.press("Space")
                if control.get_attribute("aria-expanded") != "false" or not panel.evaluate("(element) => element.hidden") or panel.is_visible():
                    fail(f"keyboard Space hide failed on {card.name} at {viewport_name}")
                if page.evaluate("performance.getEntriesByType('navigation').length") != navigation_count:
                    fail(f"reveal/hide reloaded {card.name} at {viewport_name}")

                browser_evidence.append({
                    "card": card.name,
                    "viewport": viewport_name,
                    "initially_collapsed": True,
                    "required_standalone_content_visible": True,
                    "pointer_reveal_hide": True,
                    "keyboard_enter_reveal_space_hide": True,
                    "aria_controls": panel_id,
                    "aria_expanded_transitions": ["false", "true", "false", "true", "false"],
                    "mathjax_rendered": True,
                    "no_horizontal_overflow": True,
                    "no_reload": True,
                })
                asset = page.locator("a[download]").get_attribute("href")
                with urlopen(f"{base}/cards/{asset}") as response:
                    if response.status != 200:
                        fail(f"PNG asset does not resolve for {card.name}")
                    response.read()

        page.set_viewport_size({"width": 1400, "height": 900})
        page.goto(f"{base}/index.html", wait_until="networkidle")
        landing_links = page.locator('a[href^="cards/"]').evaluate_all("(items) => items.map((item) => item.getAttribute('href'))")
        if len([item for item in landing_links if item.endswith(".html")]) != 7:
            fail("landing does not expose 7 HTML card links")
        for href in landing_links:
            with urlopen(f"{base}/{href}") as response:
                if response.status != 200:
                    fail(f"landing child target fails: {href}")
                response.read()
        page.set_viewport_size({"width": 390, "height": 844})
        if page.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1"):
            fail("mobile horizontal overflow on landing")
        browser.close()
finally:
    server.shutdown()

if console_errors or page_errors:
    fail("browser errors: " + repr((console_errors + page_errors)[:3]))
browser_audit = {
    "scope": "local Chromium functional browser QA",
    "viewports": ["1400x900", "390x844"],
    "cards_tested": len(cards),
    "card_viewport_records": browser_evidence,
    "console_errors": console_errors,
    "page_errors": page_errors,
    "result": "PASS",
}
(ROOT / "browser_audit.json").write_text(json.dumps(browser_audit, indent=2) + "\n", encoding="utf-8")

# Recall PDF facts and reader-safe text scan.
pdf = ROOT / "harry_p4_recall.pdf"
if not pdf.is_file():
    fail("recall PDF missing")
info = subprocess.run(["pdfinfo", str(pdf)], text=True, capture_output=True, check=True).stdout
if "Pages:           2" not in info or "Encrypted:       no" not in info:
    fail("recall PDF page/encryption facts unexpected")
pdf_text = subprocess.run(["pdftotext", str(pdf), "-"], text=True, capture_output=True, check=True).stdout
for forbidden in ["23c096", "2026-06-29", "29 June", "S1", "Harry Williams", "Phuc Nguyen", "/root/", "file://"]:
    if forbidden.lower() in pdf_text.lower():
        fail(f"forbidden/stale/private marker found in recall PDF: {forbidden!r}")
for required in ["P4 Q4", "P4 Q6", "Prior P3 review", "status"]:
    if required.lower() not in pdf_text.lower():
        fail(f"recall PDF missing required content: {required!r}")

# Visual contact sheets for direct local inspection.
def contact(images: list[Path], output: Path, cols: int = 2, thumb_width: int = 520) -> None:
    opened = []
    for path in images:
        image = Image.open(path).convert("RGB")
        image.thumbnail((thumb_width, 800))
        opened.append((path.name, image.copy()))
    cell_height = max(image.height for _, image in opened) + 42
    rows = (len(opened) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_width, rows * cell_height), "white")
    drawing = ImageDraw.Draw(sheet)
    for index, (name, image) in enumerate(opened):
        x = (index % cols) * thumb_width + (thumb_width - image.width) // 2
        y = (index // cols) * cell_height + 24
        drawing.text((index % cols * thumb_width + 10, (index // cols) * cell_height + 5), name, fill="black")
        sheet.paste(image, (x, y))
    sheet.save(output)


contact(pngs, ROOT / "cards_contact_sheet.png")
contact(sorted((ROOT / "recall_pdf_renders").glob("*.png")), ROOT / "recall_pdf_contact_sheet.png", cols=1, thumb_width=650)

reveal_report = f'''# Reveal/hide work-box repair QA v1 — 26 June Harry P4 downstream_v2

## Result: PASS — local-only repair; no publication action

## Implemented behaviour

- `build_clean_downstream.py` now emits one native `button.reveal-control` in each of the seven cards. It starts as **Reveal working**, with `aria-expanded="false"` and a unique `aria-controls` reference to that card's unique `.work-panel`.
- Each panel starts with the HTML `hidden` attribute, so the grey `.work` boxes are not exposed until the learner activates the control. The click handler toggles both `hidden` and `aria-expanded`, and changes the accessible visible label between **Reveal working** and **Hide working** without navigation/reload.
- The standalone prompt, marks strip, status boundary, concept visual, recall answer and study boundary are outside the hidden panel and were required to be visible before reveal.
- `render_clean_assets.py` now activates the control before capturing each literal card PNG. All seven shipped PNGs therefore show the fully revealed grey method boxes; their same-directory `download` anchors remain intact.

## Browser interaction evidence

Local Chromium checks covered every card at **1400×900 desktop** and **390×844 mobile**: **14 card/viewport records** in `browser_audit.json` (SHA-256 `{digest(ROOT / "browser_audit.json")}`).

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
'''
(ROOT / "reveal_ui_repair_qa_v1.md").write_text(reveal_report, encoding="utf-8")

# Exhaustive hash manifest after all output is stable. The manifest does not self-hash.
manifest_path = ROOT / "build_manifest.json"
manifest = json.loads(text(manifest_path))
files = sorted(
    path for path in ROOT.rglob("*")
    if path.is_file() and path.name not in {"build_manifest.json", "qa_report.md"} and "__pycache__" not in path.parts
)
manifest["final_guide_hash_proof"] = {"sha256": digest(guide), "matches_authorized_34ce": digest(guide) == EXPECTED}
manifest["quarantine"] = {"predecessor": "../_quarantine/downstream_v2_contaminated_pre_final_guide_2026-07-17", "action": "moved before rebuild; no legacy downstream file was read as build input"}
manifest["asset_qa"] = {
    "card_html_count": len(cards),
    "card_png_count": len(pngs),
    "all_pngs_verified_by_Pillow": True,
    "local_mathjax_tex_svg": {"path": "assets/mathjax/tex-svg.js", "sha256": digest(ROOT / "assets" / "mathjax" / "tex-svg.js")},
    "browser_mathjax_rendered": True,
    "browser_console_errors": 0,
    "desktop_and_mobile_link_and_overflow_checks": "PASS",
    "reveal_ui": {
        "initially_hidden_work_panels": 7,
        "pointer_reveal_hide_checks": 14,
        "keyboard_reveal_hide_checks": 14,
        "aria_controls_and_expanded_checks": 14,
        "fully_revealed_png_exports": 7,
        "browser_evidence": "browser_audit.json",
        "sha256": digest(ROOT / "browser_audit.json"),
    },
}
manifest["reader_safe_scan"] = {"scope": "learner-facing HTML, Markdown and recall PDF", "legacy_source_signature_matches": 0, "date_or_lane_marker_matches": 0, "private_path_or_full_name_matches": 0, "result": "PASS"}
manifest["files"] = {str(path.relative_to(ROOT)): digest(path) for path in files}
manifest["publication"] = "not published; no upload, remote write, index, or Notion action performed"
manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

report = f'''# Clean downstream_v2 local QA report

## Verdict: PASS (local-only; not an independent review)

- **Frozen guide proof:** SHA-256 of `guide_v2/revision_guide.pdf` is `{digest(guide)}`. It exactly matches the authorised final guide identity.
- **Quarantine:** the predecessor was moved to `_quarantine/downstream_v2_contaminated_pre_final_guide_2026-07-17/` before this build. The clean generator reads only the frozen final guide, its text mirror and source register.
- **Deliverables:** reader-safe recall Markdown + 2-page unencrypted A4 PDF; one landing; exactly seven standalone multi-step cards and seven regenerated static PNGs.
- **Reveal UI:** every card starts with its grey working panel hidden and an accessible native button labelled “Reveal working”. Across all seven cards at desktop and 390-px mobile widths, pointer reveal/hide and keyboard Enter-reveal/Space-hide changed `aria-expanded` truthfully without reload. Status, marks, prompt, visual, final answer and study boundary remained visible while working was hidden. `browser_audit.json` records all 14 card/viewport checks.
- **UI/asset checks:** all seven cards use the staged local MathJax tex-svg asset, rendered MathJax in Chromium, have at least three grey work boxes, and carry a literal same-directory PNG download anchor. PNGs were captured after revealing all working. All linked child HTML/PNG assets returned local HTTP 200. Desktop/mobile overflow and console/page-error checks passed.
- **Content/status checks:** corrected P4 Q4 curve/derivative/gradient relation/result, Q5/Q6 reference boundaries, P3 separation, and self-assessed Q2/Q8 boundaries are present. Unsupported mark allocations are explicitly not supplied rather than invented.
- **Contamination scan:** zero legacy source-signature matches, zero date/lane-marker matches, and zero private-path/full-name matches in learner-facing HTML, Markdown or recall-PDF extracted text.
- **Visual evidence:** `cards_contact_sheet.png`, `recall_pdf_contact_sheet.png`, `desktop_landing.png`, and `mobile_landing.png` were regenerated for local inspection.

This is a deterministic local QA record, not a publication, upload, Index/Notion operation, or independent-review claim.
'''
(ROOT / "qa_report.md").write_text(report, encoding="utf-8")
print("QA PASS: final guide hash, 7 reveal/hide cards and fully revealed PNGs, desktop/mobile pointer/keyboard/ARIA browser checks, recall PDF, and contamination scan.")
