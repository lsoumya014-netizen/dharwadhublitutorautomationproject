"""Smoke tests for services catalogue and marketing course offerings."""

import re
from playwright.sync_api import Page, expect

BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_digital_marketing_service_link(page: Page) -> None:
    """Validate Digital Marketing course page loads from services section."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    link = page.get_by_role("link", name=re.compile("Digital Marketing Course", re.I)).first
    expect(link).to_be_visible()


def test_email_marketing_service_link(page: Page) -> None:
    """Validate Email Marketing course page link in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    link = page.get_by_role("link", name=re.compile("Email Marketing", re.I)).first
    expect(link).to_be_visible()


def test_social_media_marketing_service_link(page: Page) -> None:
    """Validate Social Media Marketing link in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    link = page.get_by_role("link", name=re.compile("Social Media Marketing", re.I)).first
    expect(link).to_be_visible()


def test_search_engine_marketing_service_link(page: Page) -> None:
    """Validate Search Engine Marketing link in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    link = page.get_by_role("link", name=re.compile("Search Engine Marketing", re.I)).first
    expect(link).to_be_visible()


def test_whatsapp_marketing_service_link(page: Page) -> None:
    """Validate WhatsApp Marketing link in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    link = page.get_by_role("link", name=re.compile("Whatsapp Marketing", re.I)).first
    expect(link).to_be_visible()


def test_sms_marketing_service_link(page: Page) -> None:
    """Validate SMS Marketing link in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    link = page.get_by_role("link", name=re.compile("SMS Marketing", re.I)).first
    expect(link).to_be_visible()


def test_web_hosting_service_link(page: Page) -> None:
    """Validate Web Hosting service link in services."""
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    link = page.get_by_role("link", name=re.compile("Web Hosting", re.I)).first
    expect(link).to_be_visible()
