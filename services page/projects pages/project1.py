"""Live projects catalogue tests."""

import re
from playwright.sync_api import Page, expect

BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_live_projects_cards_displayed(page: Page) -> None:
    """Validate client live projects on homepage."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    expect(page.get_by_role("heading", name="Our Live Projects")).to_be_visible()
    expect(page.get_by_role("heading", name=re.compile("NWKRTC", re.I))).to_be_visible()
    expect(page.get_by_role("heading", name=re.compile("ACE DECORS", re.I))).to_be_visible()
    expect(page.get_by_role("heading", name=re.compile("RECON", re.I))).to_be_visible()
    expect(page.get_by_role("heading", name=re.compile("Oxford Coaching", re.I))).to_be_visible()
    expect(page.get_by_role("heading", name=re.compile("Angadi Coaching", re.I))).to_be_visible()
    expect(page.get_by_role("heading", name=re.compile("Anjuman BCA", re.I))).to_be_visible()
