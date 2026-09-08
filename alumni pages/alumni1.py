
import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("heading", name="Our Alumni Work At").click()
    page.locator(".alumni-cf-item.left").click()
    page.locator(".alumni-cf-item.active").click()
    page.locator(".alumni-cf-item").first.click()
    page.locator("#alumniCfCarousel").click()
    page.get_by_role("button", name="Next alumni").click()
    page.get_by_role("img", name="TVG Agency —").click()
    page.get_by_role("img", name="Ken Gen —").click()
    page.locator("div").filter(has_text="DharwadHubballiTutor DharwadHubballiTutor is one of the fastest-growing and").first.click()
    page.get_by_text("Contact & Locations +").click()
    page.get_by_text("Useful Links Terms and").click()