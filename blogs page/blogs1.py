"""Chromium smoke test for the blogs catalogue."""

import re

from playwright.sync_api import Page, expect


BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_blogs_catalogue_displays_digital_marketing_article(page: Page) -> None:
    """The Blogs programme reveals the Digital Marketing article card."""
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page.get_by_role("heading", name="Blogs")).to_be_visible()
    page.get_by_role("button", name="Explore Courses").nth(5).click()

    article = page.get_by_role(
        "link", name=re.compile("Digital Marketing Course", re.IGNORECASE)
    )
    expect(article).to_be_visible()
    expect(article).to_have_attribute(
        "href", re.compile("digital-marketing-course", re.IGNORECASE)
    )
