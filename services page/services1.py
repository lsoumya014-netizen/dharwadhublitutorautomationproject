import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Best Digital Marketing Course (Online & Offline) ").click()
    page.get_by_text("Digital Marketing Training").click()
    page.get_by_role("paragraph").nth(5).click()
    page.get_by_role("heading", name="Key Features:").click()
    page.locator("div").filter(has_text="Digital Marketing Training").nth(5).click()

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Email Marketing ").click()
    page.locator("body").click()
    page.locator("div").filter(has_text="Email marketingÂ is the act").nth(5).click()

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Social Media Marketing ").click()
    page.locator("div").filter(has_text="The term social media").nth(5).click()

import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Search Engine Marketing ").click()
    page.get_by_role("heading", name="Reach Your Clients Instantly:").click()
    page.get_by_role("heading", name="Create Geo-Targeted Search").click()

import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Whatsapp Marketing ").click()
    page.locator("div").filter(has_text="WhatsApp marketing isÂ a type").nth(5).click()

import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" SMS Marketing ").click()
    page.get_by_role("list").filter(has_text="E-commerce storesÂ :Â Whether").click()

import re
from playwright.sync_api import Page, expect

def test_example(page: Page) -> None:
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Web Hosting ").click()
    page.get_by_text("Improved Site Performance Technical Support Liberty In Web Design And Templates").click()
