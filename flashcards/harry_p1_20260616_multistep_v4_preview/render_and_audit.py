#!/usr/bin/env python3
"""Render clean local HTML into static PNGs with the local MathJax tex-svg asset,
and produce a deterministic browser audit (desktop + mobile) verifying no
console/page errors, no broken images, no horizontal overflow, and that the
reveal/hide control is REAL and accessible.

The reveal control is activated before each card PNG so the shipped export shows
the fully revealed grey method boxes; the literal same-directory PNG anchors stay intact.
"""
from __future__ import annotations
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from threading import Thread
import contextlib, json, os
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):  # noqa: A002
        pass

server = ThreadingHTTPServer(("127.0.0.1", 0), Quiet)
Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{server.server_port}"

cards = sorted((ROOT / "cards").glob("*.html"))
report: dict = {"renderer": "playwright (python) + system Chromium", "cards": {}, "landing": {}, "status": "pending"}

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, executable_path="/usr/bin/chromium",
                                    args=["--no-sandbox", "--disable-dev-shm-usage", "--font-render-hinting=none"])
        for f in cards:
            q = f.stem
            rec = {}
            for mobile in (False, True):
                page = browser.new_page(
                    viewport={"width": 390, "height": 844} if mobile else {"width": 1400, "height": 1000},
                    device_scale_factor=2)
                errors: list[str] = []
                def on_console(m):
                    if m.type == "error":
                        errors.append(f"console: {m.text}")
                def on_pageerror(e):
                    errors.append(f"pageerror: {e.message}")
                page.on("console", on_console)
                page.on("pageerror", on_pageerror)
                page.goto(f"{base}/cards/{f.name}", wait_until="networkidle")
                page.wait_for_function("document.querySelectorAll('mjx-container').length > 0", timeout=15000)
                page.wait_for_timeout(400)
                # Reveal control must be present and initially collapsed.
                control = page.locator("button.reveal-control")
                ctrl_count = control.count()
                init_expanded = control.get_attribute("aria-expanded") if ctrl_count == 1 else None
                init_hidden = page.locator(".work-panel").is_hidden() if ctrl_count == 1 else None
                # Exercise pointer reveal/hide, then native keyboard Enter/Space.
                if ctrl_count == 1:
                    control.click()
                    page.wait_for_timeout(150)
                visible_after = page.locator(".work-panel").is_visible() if ctrl_count == 1 else None
                expanded_after = control.get_attribute("aria-expanded") if ctrl_count == 1 else None
                label_after = control.text_content() if ctrl_count == 1 else None
                if ctrl_count == 1:
                    control.click()
                    page.wait_for_timeout(100)
                hidden_after_second_click = page.locator(".work-panel").is_hidden() if ctrl_count == 1 else None
                if ctrl_count == 1:
                    control.focus()
                    page.keyboard.press("Enter")
                    page.wait_for_timeout(100)
                visible_after_enter = page.locator(".work-panel").is_visible() if ctrl_count == 1 else None
                if ctrl_count == 1:
                    page.keyboard.press("Space")
                    page.wait_for_timeout(100)
                hidden_after_space = page.locator(".work-panel").is_hidden() if ctrl_count == 1 else None
                # Leave the export in its fully revealed state.
                if ctrl_count == 1:
                    control.click()
                    page.wait_for_timeout(100)
                # Metrics: overflow + image completeness + mathjax present.
                metrics = page.evaluate("""() => {
                    const cw = document.documentElement.clientWidth;
                    const bad = [];
                    const sels = 'mjx-container, svg, table, .q-header, .step, .step-body, .given, .source-note, .part-h';
                    document.querySelectorAll(sels).forEach(el => {
                        const b = el.getBoundingClientRect();
                        const left = b.left, right = b.right;
                        const containedFormula = el.closest('.step-body,.q-header,.given');
                        const parentStyle = containedFormula && getComputedStyle(containedFormula);
                        const parentContainsOverflow = containedFormula && (parentStyle.overflowX === 'auto' || parentStyle.overflowX === 'scroll') && containedFormula.scrollWidth >= containedFormula.clientWidth;
                        if (!(left >= -12 && right <= cw + 12) && !parentContainsOverflow) {
                            bad.push({tag: el.tagName, cls: (el.className && el.className.baseVal) || el.className || '', left: Math.round(left), right: Math.round(right)});
                        }
                    });
                    return {
                        mathjax: document.querySelectorAll('mjx-container').length,
                        images: [...document.images].map(i => ({src: i.getAttribute('src'), complete: i.complete, nw: i.naturalWidth})),
                        scrollWidth: document.documentElement.scrollWidth,
                        clientWidth: cw,
                        overflow: bad.slice(0, 20),
                        controlOverlap: (() => {
                            const fixed = document.querySelector('a.export-btn');
                            const meta = document.querySelector('.meta');
                            if (!fixed || !meta) return false;
                            const a=fixed.getBoundingClientRect(), b=meta.getBoundingClientRect();
                            return !(a.right <= b.left || a.left >= b.right || a.bottom <= b.top || a.top >= b.bottom);
                        })(),
                        promptText: document.querySelector('.q-header blockquote')?.innerText || ''
                    };
                }""")
                image_fail = [i for i in metrics["images"] if not i["complete"] or i["nw"] == 0]
                target = f"{q}.png"
                # A desktop (1400 px) fully revealed capture is the canonical PNG export.
                # Export/reveal controls are interactive HTML chrome, not study content, and
                # must never be baked into the static PNG byte set.
                if not mobile:
                    page.evaluate("""() => document.querySelectorAll('a.export-btn,button.reveal-control').forEach(el => el.style.visibility='hidden')""")
                    hidden_controls = page.locator("a.export-btn:visible,button.reveal-control:visible").count() == 0
                    page.screenshot(path=str(ROOT / "cards" / target), full_page=True)
                else:
                    hidden_controls = None
                fail = bool(errors) or bool(image_fail) or metrics["scrollWidth"] > metrics["clientWidth"] or bool(metrics["overflow"]) or metrics["controlOverlap"] or metrics["mathjax"] == 0 or ctrl_count != 1 or init_expanded != "false" or init_hidden is not True or visible_after is not True or expanded_after != "true" or label_after != "Hide working" or hidden_after_second_click is not True or visible_after_enter is not True or hidden_after_space is not True or (not mobile and hidden_controls is not True)
                rec["mobile" if mobile else "desktop"] = {
                    "errors": errors, "mathjax": metrics["mathjax"],
                    "scrollWidth": metrics["scrollWidth"], "clientWidth": metrics["clientWidth"],
                    "overflow": metrics["overflow"], "control_overlap": metrics["controlOverlap"],
                    "prompt_text": metrics["promptText"], "image_failures": image_fail,
                    "canonical_png_controls_hidden": hidden_controls,
                    "reveal": {"control_count": ctrl_count, "initial_aria_expanded": init_expanded,
                               "initial_panel_hidden": init_hidden, "visible_after_click": visible_after,
                               "expanded_after_click": expanded_after, "label_after_click": label_after,
                               "hidden_after_second_click": hidden_after_second_click,
                               "visible_after_enter": visible_after_enter, "hidden_after_space": hidden_after_space},
                    "fail": fail, "target": f"cards/{target}"
                }
                page.close()
            report["cards"][f.name] = rec

        # Landing evidence only (not a learner navigation target).
        for mobile in (False, True):
            page = browser.new_page(
                viewport={"width": 390, "height": 844} if mobile else {"width": 1400, "height": 1000},
                device_scale_factor=2)
            errors = []
            def on_console(m):
                if m.type == "error":
                    errors.append(f"console: {m.text}")
            def on_pageerror(e):
                errors.append(f"pageerror: {e.message}")
            page.on("console", on_console)
            page.on("pageerror", on_pageerror)
            page.goto(f"{base}/index.html", wait_until="networkidle")
            page.evaluate("document.querySelectorAll('img.preview').forEach(i => i.loading='eager')")
            page.wait_for_function("[...document.querySelectorAll('img.preview')].every(i => i.complete && i.naturalWidth > 0)", timeout=30000)
            page.wait_for_timeout(400)
            metrics = page.evaluate("""() => ({ scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth,
                cards: document.querySelectorAll('section.card').length,
                htmlLinks: [...document.querySelectorAll('.links a')].filter(a => a.textContent.includes('HTML')).length,
                pngLinks: [...document.querySelectorAll('.links a')].filter(a => a.textContent.includes('PNG')).length,
                previews: document.querySelectorAll('img.preview').length })""")
            page.screenshot(path=str(ROOT / ("mobile_landing.png" if mobile else "desktop_landing.png")), full_page=True)
            fail = bool(errors) or metrics["scrollWidth"] > metrics["clientWidth"] or any(metrics[k] != 10 for k in ('cards','htmlLinks','pngLinks','previews'))
            report["landing"]["mobile" if mobile else "desktop"] = {"errors": errors, **metrics, "fail": fail}
            page.close()
        browser.close()

    all_ok = all(not c["desktop"]["fail"] and not c["mobile"]["fail"] for c in report["cards"].values()) \
        and not report["landing"]["desktop"]["fail"] and not report["landing"]["mobile"]["fail"]
    report["status"] = "pass" if all_ok else "fail"
finally:
    server.shutdown()

(ROOT / "browser_audit.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": report["status"], "cards": len(report["cards"]),
                  "landing_desktop": report["landing"]["desktop"],
                  "card_sample": {k: {"desktop_fail": v["desktop"]["fail"], "mobile_fail": v["mobile"]["fail"],
                                     "mathjax": v["desktop"]["mathjax"],
                                     "reveal_initial_hidden": v["desktop"]["reveal"]["initial_panel_hidden"],
                                     "reveal_visible_after": v["desktop"]["reveal"]["visible_after_click"]}
                              for k, v in list(report["cards"].items())[:3]}}, indent=2))
if report["status"] != "pass":
    raise SystemExit(2)
