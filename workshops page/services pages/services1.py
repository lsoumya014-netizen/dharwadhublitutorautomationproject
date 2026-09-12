"""Services tests for workshops directory."""

import re
from playwright.sync_api import Page, expect

BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_digital_marketing_service_catalogue(page: Page) -> None:
    """Validate digital marketing course option in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    expect(page.get_by_role("link", name=re.compile("Digital Marketing Course", re.I)).first).to_be_visible()


def test_email_marketing_catalogue(page: Page) -> None:
    """Validate email marketing option in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    expect(page.get_by_role("link", name=re.compile("Email Marketing", re.I)).first).to_be_visible()


def test_social_media_marketing_catalogue(page: Page) -> None:
    """Validate social media marketing option in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    expect(page.get_by_role("link", name=re.compile("Social Media Marketing", re.I)).first).to_be_visible()
