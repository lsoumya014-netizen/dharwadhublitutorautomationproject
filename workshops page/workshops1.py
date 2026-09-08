"""Chromium smoke test for the workshops catalogue."""

import re

from playwright.sync_api import Page, expect


BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_machine_learning_workshop_page_loads(page: Page) -> None:
    """The Workshops programme opens the 40-hour machine-learning workshop."""
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page.get_by_role("heading", name="Workshops")).to_be_visible()
    page.get_by_role("button", name="Explore Courses").nth(4).click()

    workshop = page.get_by_role(
        "link",
        name=re.compile(
            "Python with Machine Learning Workshop.*40 Hours", re.IGNORECASE
        ),
    )
    expect(workshop).to_be_visible()
    workshop.click()

    expect(page.get_by_role("heading", name="Workshop Modules")).to_be_visible()
