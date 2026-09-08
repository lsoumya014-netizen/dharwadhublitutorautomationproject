"""Chromium smoke test for the jobs catalogue."""

import re

from playwright.sync_api import Page, expect


BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_software_testing_job_page_loads(page: Page) -> None:
    """The Jobs programme opens the Software Testing course details."""
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page.get_by_role("heading", name="Jobs", exact=True)).to_be_visible()
    page.get_by_role("button", name="Explore Courses").nth(3).click()

    course = page.get_by_role(
        "link", name=re.compile("Software Testing Course", re.IGNORECASE)
    )
    expect(course).to_be_visible()
    course.click()

    expect(
        page.get_by_role(
            "heading", name=re.compile("Software Testing Course", re.IGNORECASE)
        )
    ).to_be_visible()
    expect(page.get_by_role("heading", name="Tools Covered:")).to_be_visible()
