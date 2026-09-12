"""Smoke tests for the Dharwad Hubballi Tutor training pages."""

import re
from playwright.sync_api import Page, expect

BASE_URL = "https://www.dharwadhubballitutor.com/"


def open_course_menu(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    courses_button = page.get_by_role("button", name=re.compile("Explore Courses", re.I)).first
    expect(courses_button).to_be_visible()
    courses_button.click()


def test_training_menu_displays_courses(page: Page) -> None:
    """The home page exposes a visible list of available training courses."""
    open_course_menu(page)
    courses = page.get_by_role("link").filter(has_text=re.compile("Full Stack", re.I))
    expect(courses.first).to_be_visible()


def test_full_stack_course_page_loads(page: Page) -> None:
    """A course selected from the catalogue opens a page with course content."""
    open_course_menu(page)
    course = page.get_by_role("link").filter(has_text=re.compile("Full Stack", re.I)).first
    course.click()
    expect(page.locator("main, #main-content, body").first).to_contain_text(
        re.compile("Course|Development|Training", re.I)
    )