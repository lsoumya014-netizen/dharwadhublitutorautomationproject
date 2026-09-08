"""Chromium smoke test for the internship catalogue."""

import re

from playwright.sync_api import Page, expect


BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_django_internship_page_loads(page: Page) -> None:
    """The internship programme exposes its Django training details."""
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page.get_by_role("heading", name="Internships")).to_be_visible()
    page.get_by_role("button", name="Explore Courses").nth(1).click()

    internship = page.get_by_role(
        "link", name=re.compile("Django Internship Training", re.IGNORECASE)
    )
    expect(internship).to_be_visible()
    internship.click()

    expect(page.get_by_text("This session was conducted")).to_be_visible()
