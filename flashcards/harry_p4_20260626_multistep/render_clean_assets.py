#!/usr/bin/env python3
"""Render clean local HTML into static PNGs with the local MathJax asset."""
from __future__ import annotations
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
import contextlib, os
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, format, *args): pass
server = ThreadingHTTPServer(("127.0.0.1", 0), Quiet)
Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"
cards = sorted((ROOT / "cards").glob("*.html"))
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium", args=["--font-render-hinting=none"])
        page = browser.new_page(viewport={"width": 1400, "height": 1000}, device_scale_factor=1)
        for f in cards:
            page.goto(f"{base}/cards/{f.name}", wait_until="networkidle")
            page.wait_for_function("document.querySelectorAll('mjx-container').length > 0")
            control = page.locator("button.reveal-control")
            if control.count() != 1 or control.get_attribute("aria-expanded") != "false":
                raise RuntimeError(f"{f.name}: expected one initially collapsed reveal control")
            control.click()
            if control.get_attribute("aria-expanded") != "true" or not page.locator(".work-panel").is_visible():
                raise RuntimeError(f"{f.name}: reveal control did not expose working for PNG export")
            page.screenshot(path=str(f.with_suffix(".png")), full_page=True)
        # Desktop/mobile landing evidence only; not learner navigation targets.
        page.goto(f"{base}/index.html", wait_until="networkidle")
        page.screenshot(path=str(ROOT / "desktop_landing.png"), full_page=True)
        page.set_viewport_size({"width": 390, "height": 844})
        page.reload(wait_until="networkidle")
        page.screenshot(path=str(ROOT / "mobile_landing.png"), full_page=True)
        browser.close()
finally:
    server.shutdown()
print(f"Rendered {len(cards)} card PNGs with local MathJax.")
