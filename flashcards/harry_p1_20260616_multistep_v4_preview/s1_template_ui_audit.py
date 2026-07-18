#!/usr/bin/env python3
"""Local-only S1 template re-audit for the P1 May 2022 multi-step rebuild."""
from __future__ import annotations

import hashlib
import json
import os
import re
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from urllib.parse import quote

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
LESSON = ROOT.parent.parent
S1_LANDING = Path("/root/fc_publish/repo/papers/s1_jan2023.html")
S1_CARD = Path("/root/fc_publish/repo/papers/multistep/S1/s1_jan2023_Q1.html")
OUT = ROOT / "s1_template_evidence"
OUT.mkdir(exist_ok=True)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def style_text(text: str) -> str:
    match = re.search(r"<style>(.*?)</style>", text, flags=re.S)
    if not match:
        raise ValueError("missing style block")
    return match.group(1).strip()


def has(text: str, value: str) -> bool:
    return value in text


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        pass


def main() -> int:
    s1_landing = S1_LANDING.read_text(encoding="utf-8")
    s1_card = S1_CARD.read_text(encoding="utf-8")
    p1_landing_path = ROOT / "index.html"
    p1_landing = p1_landing_path.read_text(encoding="utf-8")
    card_paths = sorted((ROOT / "cards").glob("P1_May2022_Q*.html"), key=lambda p: int(re.search(r"Q(\d+)", p.stem).group(1)))
    p1_q1 = (ROOT / "cards" / "P1_May2022_Q1.html").read_text(encoding="utf-8")

    landing_style_equal = style_text(s1_landing) == style_text(p1_landing)
    reference_tokens = [
        "--ink:#1d1d1f", "--muted:#6e6e73", "--line:#d2d2d7", "--soft:#f5f5f7", "--work:#fafafa", "--paper:#fff",
        ".export-btn{position:fixed;top:16px;right:16px", ".card{max-width:1260px", ".q-header{background:var(--soft);border-radius:12px",
        ".part-h{font:650 14.5px", ".steps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))",
        ".step{border:1px solid #c7c7cc;background:var(--work)", ".step-num{background:var(--ink);color:#fff",
        ".step-result{margin-top:8px", ".index-body{max-width:1040px",
    ]
    token_check = {token: has(p1_q1, token) for token in reference_tokens}
    # The P1 builder extends only the S1 card grammar for native reveal/hide, responsive formula containment and four source-grounded SVG diagrams.
    extension_markers = ["work-panel[hidden]", "reveal-control", ".diagram", "aria-controls", "aria-expanded"]
    skeleton_checks = {
        "export_anchor": bool(re.search(r'<a class="export-btn" href="P1_May2022_Q1\.png"', p1_q1)),
        "card_wrapper": '<div class="card">' in p1_q1,
        "card_meta": '<div class="meta">' in p1_q1,
        "question_header": '<div class="q-header"><span class="label">Question</span><blockquote>' in p1_q1,
        "marks": '<p class="q-marks">[4 marks]</p>' in p1_q1,
        "part_grammar": all(x in p1_q1 for x in ['class="parts"', 'class="part-h"', 'class="given"', 'class="steps"']),
        "grey_work_grammar": all(x in p1_q1 for x in ['class="step"', 'class="step-top"', 'class="step-tag"', 'class="step-num"', 'class="step-body"']),
        "native_reveal_only_extension": all(x in p1_q1 for x in extension_markers),
    }
    landing_checks = {
        "literal_s1_landing_css": landing_style_equal,
        "1040_main": "main{max-width:1040px;margin:0 auto}" in p1_landing,
        "ten_cards": p1_landing.count('<section class="card">') == 10,
        "ten_html_links": len(re.findall(r'href="cards/P1_May2022_Q\d+\.html"', p1_landing)) == 10,
        "ten_png_links": len(re.findall(r'href="cards/P1_May2022_Q\d+\.png"', p1_landing)) == 10,
        "ten_previews": len(re.findall(r'<img class="preview"', p1_landing)) == 10,
        "no_reconciled_29_75_claim": "29/75" not in p1_landing,
    }
    content_checks = {
        "ten_html_cards": len(card_paths) == 10,
        "ten_static_pngs": len(list((ROOT / "cards").glob("P1_May2022_Q*.png"))) == 10,
        "q5_reference_unknown": all(v in (ROOT / "cards" / "P1_May2022_Q5.html").read_text(encoding="utf-8") for v in ["NOT reviewed live — reference only", "scored state is unknown"]),
        "q8_reference_unknown": all(v in (ROOT / "cards" / "P1_May2022_Q8.html").read_text(encoding="utf-8") for v in ["NOT reviewed live — reference only", "scored state is unknown"]),
        "q10_reference_unknown": all(v in (ROOT / "cards" / "P1_May2022_Q10.html").read_text(encoding="utf-8") for v in ["NOT reviewed live — reference only", "scored state is unknown"]),
        "no_reconciled_29_75": all("29/75" not in p.read_text(encoding="utf-8") for p in card_paths),
        "required_diagrams": all('class="diagram"' in (ROOT / "cards" / f"P1_May2022_Q{q}.html").read_text(encoding="utf-8") for q in (4, 5, 8, 9)),
    }

    os.chdir(ROOT)
    server = ThreadingHTTPServer(("127.0.0.1", 0), Quiet)
    Thread(target=server.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{server.server_port}"
    browser_records: dict[str, dict] = {}
    visual_paths: list[str] = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--no-sandbox", "--disable-dev-shm-usage", "--font-render-hinting=none"])
            for card in card_paths:
                q = re.search(r"Q(\d+)", card.stem).group(1)
                browser_records[q] = {}
                for name, viewport in (("desktop", {"width": 1400, "height": 1000}), ("mobile_390", {"width": 390, "height": 844})):
                    page = browser.new_page(viewport=viewport, device_scale_factor=2)
                    errors: list[str] = []
                    page.on("console", lambda msg: errors.append(f"console: {msg.text}") if msg.type == "error" else None)
                    page.on("pageerror", lambda err: errors.append(f"pageerror: {err.message}"))
                    page.goto(f"{base}/cards/{quote(card.name)}", wait_until="networkidle")
                    page.wait_for_function("document.querySelectorAll('mjx-container').length > 0")
                    control = page.locator("button.reveal-control")
                    panel = page.locator(".work-panel")
                    initial = {
                        "button_count": control.count(),
                        "expanded": control.get_attribute("aria-expanded"),
                        "controls": control.get_attribute("aria-controls"),
                        "panel_hidden": panel.is_hidden(),
                        "question_visible": page.locator(".q-header").is_visible(),
                        "final_visible": page.locator(".part").last.is_visible(),
                    }
                    control.click()
                    page.wait_for_timeout(100)
                    revealed = page.evaluate("""() => {
                        const html = document.documentElement, body = document.body, p = document.querySelector('.work-panel');
                        const overflow = [...document.querySelectorAll('mjx-container')].filter(el => {
                          const s = getComputedStyle(el), b = el.getBoundingClientRect();
                          const parent = el.closest('.final-reference');
                          const parentContained = parent && (getComputedStyle(parent).overflowX === 'auto' || getComputedStyle(parent).overflowX === 'scroll') && parent.scrollWidth >= parent.clientWidth;
                          return b.right > innerWidth + 1 && !((s.overflowX === 'auto' || s.overflowX === 'scroll') && el.scrollWidth >= el.clientWidth) && !parentContained;
                        }).length;
                        return {expanded: document.querySelector('.reveal-control').getAttribute('aria-expanded'), visible: !p.hidden,
                          html_scroll_width: html.scrollWidth, html_client_width: html.clientWidth,
                          body_scroll_width: body.scrollWidth, body_client_width: body.clientWidth,
                          mathjax: document.querySelectorAll('mjx-container').length, uncontrolled_formula_overflow: overflow};
                    }""")
                    if q in {"1", "5", "8", "10"}:
                        screenshot = OUT / f"P1_Q{q}_{name}_revealed.png"
                        page.screenshot(path=str(screenshot), full_page=True)
                        visual_paths.append(str(screenshot))
                    browser_records[q][name] = {"errors": errors, "initial": initial, "revealed": revealed}
                    page.close()
            for name, viewport in (("desktop", {"width": 1400, "height": 1000}), ("mobile_390", {"width": 390, "height": 844})):
                page = browser.new_page(viewport=viewport, device_scale_factor=2)
                errors: list[str] = []
                page.on("console", lambda msg: errors.append(f"console: {msg.text}") if msg.type == "error" else None)
                page.goto(f"{base}/index.html", wait_until="networkidle")
                page.evaluate("document.querySelectorAll('img.preview').forEach(i => i.loading='eager')")
                page.wait_for_function("[...document.querySelectorAll('img.preview')].every(i => i.complete && i.naturalWidth > 0)", timeout=30000)
                page.wait_for_timeout(300)
                landing = page.evaluate("""() => ({html_scroll_width: document.documentElement.scrollWidth, html_client_width: document.documentElement.clientWidth,
                  body_scroll_width: document.body.scrollWidth, body_client_width: document.body.clientWidth,
                  cards: document.querySelectorAll('section.card').length, html_links: document.querySelectorAll('.links a[href$=".html"]').length,
                  png_links: document.querySelectorAll('.links a[href$=".png"]').length,
                  previews: [...document.querySelectorAll('img.preview')].map(i => ({complete:i.complete,nw:i.naturalWidth}))})""")
                browser_records[f"landing_{name}"] = {"errors": errors, "metrics": landing}
                page.close()
            browser.close()
    finally:
        server.shutdown()

    browser_pass = True
    for q in map(str, range(1, 11)):
        for name in ("desktop", "mobile_390"):
            rec = browser_records[q][name]
            initial, revealed = rec["initial"], rec["revealed"]
            browser_pass &= not rec["errors"] and initial["button_count"] == 1 and initial["expanded"] == "false" and initial["panel_hidden"] is True and initial["controls"] == f"working-panel-Q{q}" and initial["question_visible"] is True and initial["final_visible"] is True
            browser_pass &= revealed["expanded"] == "true" and revealed["visible"] is True and revealed["mathjax"] > 0 and revealed["html_scroll_width"] <= revealed["html_client_width"] and revealed["body_scroll_width"] <= revealed["body_client_width"] and revealed["uncontrolled_formula_overflow"] == 0
    for name in ("landing_desktop", "landing_mobile_390"):
        rec = browser_records[name]
        metrics = rec["metrics"]
        browser_pass &= not rec["errors"] and metrics["html_scroll_width"] <= metrics["html_client_width"] and metrics["body_scroll_width"] <= metrics["body_client_width"] and metrics["cards"] == 10 and metrics["html_links"] == 10 and metrics["png_links"] == 10 and all(i["complete"] and i["nw"] > 0 for i in metrics["previews"])

    result = {
        "status": "pass" if all(token_check.values()) and all(skeleton_checks.values()) and all(landing_checks.values()) and all(content_checks.values()) and browser_pass else "fail",
        "references": {"s1_landing": str(S1_LANDING), "s1_card": str(S1_CARD), "p1_root": str(ROOT)},
        "reference_sha256": {"s1_landing": sha(S1_LANDING), "s1_card": sha(S1_CARD), "p1_landing": sha(p1_landing_path)},
        "structural": {"card_tokens": token_check, "card_skeleton": skeleton_checks, "landing": landing_checks, "extensions": extension_markers},
        "content_boundary": content_checks,
        "browser": browser_records,
        "visual_evidence": visual_paths + [str(ROOT / "desktop_landing.png"), str(ROOT / "mobile_landing.png")],
        "existing_keyboard_audit": {"path": str(ROOT / "browser_audit.json"), "sha256": sha(ROOT / "browser_audit.json")},
        "local_only": True,
    }
    audit_path = ROOT / "s1_template_structural_audit.json"
    audit_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "audit": str(audit_path), "visuals": len(visual_paths), "browser_pass": browser_pass}, indent=2))
    return 0 if result["status"] == "pass" else 2

if __name__ == "__main__":
    raise SystemExit(main())
