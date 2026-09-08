"""Shared Playwright fixtures for every browser test module in this project."""

import os
from collections.abc import Iterator
from pathlib import Path

import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture
def page(request: pytest.FixtureRequest) -> Iterator[Page]:
    """Provide an isolated Chromium page and retain a screenshot per test."""
    screenshot_dir = Path(__file__).parent / "screenshot"
    screenshot_dir.mkdir(exist_ok=True)
    headless = os.environ.get("DHB_HEADLESS", "0") == "1"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)
        context = browser.new_context()
        browser_page = context.new_page()
        browser_page.set_default_timeout(10_000)
        browser_page.set_default_navigation_timeout(20_000)
        try:
            yield browser_page
        finally:
            browser_page.screenshot(
                path=screenshot_dir / f"{request.node.name}.png",
                full_page=True,
            )
            context.close()
            browser.close()
