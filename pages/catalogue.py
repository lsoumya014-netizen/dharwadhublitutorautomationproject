"""Catalogue page object for exploring programs and course offerings."""

import re
from playwright.sync_api import Locator, Page


class CataloguePage:
    """Page Object for program catalogues (Trainings, Internships, Jobs, Workshops, Services, Blogs)."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.dharwadhubballitutor.com/"

    def navigate(self) -> None:
        """Navigate to home page."""
        self.page.goto(self.url, wait_until="domcontentloaded")

    def get_program_heading(self, program_name: str) -> Locator:
        """Get heading for a program section."""
        return self.page.get_by_role("heading", name=program_name, exact=True)

    def explore_program(self, index: int) -> None:
        """Click on Explore Courses button for a specific program index."""
        self.page.get_by_role("button", name="Explore Courses").nth(index).click()

    def get_course_link(self, pattern: str) -> Locator:
        """Get link to a specific course or article."""
        return self.page.get_by_role("link", name=re.compile(pattern, re.I))

    def get_popular_courses_heading(self) -> Locator:
        """Get Our Most Popular Courses heading."""
        return self.page.get_by_role("heading", name="Our Most Popular Courses")
