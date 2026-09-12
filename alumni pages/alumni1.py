"""Alumni page and carousel test."""

import re
from playwright.sync_api import Page, expect


def test_alumni_carousel_interaction(page: Page) -> None:
    """Validate alumni section, carousel interaction, and partner logos."""
    page.goto("https://www.dharwadhubballitutor.com/", wait_until="domcontentloaded")
    expect(page.get_by_role("heading", name="Our Alumni Work At")).to_be_visible()
    expect(page.locator("#alumniCfCarousel")).to_be_visible()

    next_btn = page.get_by_role("button", name="Next alumni")
    if next_btn.is_visible():
        next_btn.click()

    expect(page.locator("img[alt*='TVG Agency']").first).to_be_attached()
    expect(page.locator("img[alt*='Ken Gen']").first).to_be_attached()