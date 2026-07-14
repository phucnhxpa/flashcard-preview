#!/usr/bin/env python3
"""Render each card HTML to a full-page PNG with Playwright (MathJax tex-svg)."""
import os, glob
from playwright.sync_api import sync_playwright

OUT = os.path.dirname(os.path.abspath(__file__))
CARDS = sorted(glob.glob(os.path.join(OUT, "*.html")))
CARDS = [c for c in CARDS if os.path.basename(c) != "index.html"]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1120, "height": 900},
                            device_scale_factor=2)
    for card in CARDS:
        page.goto("file://" + card, wait_until="networkidle")
        page.wait_for_timeout(3500)  # let MathJax finish typesetting SVG
        # confirm MathJax rendered
        n = page.eval_on_selector_all("mjx-container", "els => els.length")
        page.evaluate("""() => {
            document.querySelectorAll('.export-btn,.mask-toggle').forEach(e => e.style.display='none');
            document.querySelectorAll('.work.masked').forEach(e => e.classList.remove('masked'));
        }""")
        out = card.replace(".html", ".png")
        page.screenshot(path=out, full_page=True)
        print(f"{os.path.basename(out)}  mjx={n}  {os.path.getsize(out)//1024}KB")
    browser.close()
print("render done")
