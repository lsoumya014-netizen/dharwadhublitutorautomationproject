"""Shared pytest fixtures for the browser test suite."""

import os
import re
from collections.abc import Iterator
from pathlib import Path

import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="function")
def page(request: pytest.FixtureRequest) -> Iterator[Page]:
    """Supply each test with an isolated Chromium page and capture a full-page screenshot."""
    screenshot_dir = Path(__file__).resolve().parents[1] / "screenshot"
    screenshot_dir.mkdir(exist_ok=True)

    headless = os.environ.get("DHB_HEADLESS", "0") == "1"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        browser_page = context.new_page()
        browser_page.set_default_timeout(12_000)
        browser_page.set_default_navigation_timeout(25_000)
        try:
            yield browser_page
        finally:
            # Sanitize filename for Windows safety
            safe_node_name = re.sub(r'[\\/:*?"<>|]', "_", request.node.name)
            screenshot_path = screenshot_dir / f"{safe_node_name}.png"
            try:
                browser_page.screenshot(
                    path=screenshot_path,
                    full_page=True,
                )
            except Exception:
                pass
            context.close()
            browser.close()
