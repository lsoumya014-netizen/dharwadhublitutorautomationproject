"""Shared pytest fixtures for the browser test suite."""

import os
from collections.abc import Iterator
from pathlib import Path

import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="function")
def page(request: pytest.FixtureRequest) -> Iterator[Page]:
    """Supply each test with an isolated Chromium page (visible by default)."""
    screenshot_dir = Path(__file__).resolve().parents[1] / "screenshot"
    screenshot_dir.mkdir(exist_ok=True)

    # Set DHB_HEADLESS=1 in the terminal to run without a visible browser window.
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
            # A screenshot is useful when a live-site selector changes, but it
            # must be captured before the browser context is closed.
            browser_page.screenshot(
                path=screenshot_dir / f"{request.node.name}.png",
                full_page=True,
            )
            context.close()
            browser.close()
