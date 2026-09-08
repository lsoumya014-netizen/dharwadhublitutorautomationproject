import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("img", name="NWKRTC BI Dashboard").click()
    page.locator("div").filter(has_text="Public Transport Analytics").nth(2).click()
    page.locator("div").filter(has_text="ERP System ACE DECORS – ERP").nth(2).click()
    page.get_by_role("img", name="ACE DECORS ERP").click()
    page.get_by_role("img", name="RECON Event Analytics").click()
    page.locator("div").filter(has_text="Event Analytics RECON – Event").nth(2).click()
    page.get_by_role("img", name="Oxford Coaching Web App").click()
    page.locator("div").filter(has_text="Education Technology Oxford").nth(2).click()
    page.get_by_role("img", name="Angadi Coaching Web").click()
    page.locator("div").filter(has_text="Education Technology Angadi").nth(2).click()
    page.locator("div").filter(has_text="College Management Anjuman").nth(2).click()
    page.get_by_role("img", name="Anjuman BCA BBA Institute").click()
    
