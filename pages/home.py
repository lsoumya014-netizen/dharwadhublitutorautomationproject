"""Home page object for DharwadHubballiTutor."""

import re
from playwright.sync_api import Locator, Page


class HomePage:
    """Page Object for DharwadHubballiTutor Home Page."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.dharwadhubballitutor.com/"

        # Navigation Links
        self.primary_nav = self.page.get_by_label("Primary navigation")
        self.nav_about = self.primary_nav.get_by_role("link", name="About")
        self.nav_placements = self.primary_nav.get_by_role("link", name="Placements")
        self.nav_contact = self.primary_nav.get_by_role("link", name="Contact")
        self.nav_lms = self.primary_nav.get_by_role("link", name="LMS")
        self.book_demo_btn = self.page.get_by_role("button", name="Book Demo")

        # Headings
        self.discover_programs_heading = self.page.get_by_role(
            "heading", name="Discover Our Programs"
        )
        self.popular_courses_heading = self.page.get_by_role(
            "heading", name="Our Most Popular Courses"
        )
        self.live_projects_heading = self.page.get_by_role(
            "heading", name="Our Live Projects"
        )
        self.alumni_heading = self.page.get_by_role(
            "heading", name="Our Alumni Work At"
        )
        self.accreditations_heading = self.page.get_by_role(
            "heading", name="Our Official Accreditations"
        )

        # Program Explore Buttons
        self.explore_buttons = self.page.get_by_role("button", name="Explore Courses")

        # Live Projects Locators
        self.nwkrtc_heading = self.page.get_by_role("heading", name=re.compile("NWKRTC", re.I))
        self.ace_decors_heading = self.page.get_by_role("heading", name=re.compile("ACE DECORS", re.I))
        self.recon_heading = self.page.get_by_role("heading", name=re.compile("RECON", re.I))
        self.oxford_heading = self.page.get_by_role("heading", name=re.compile("Oxford Coaching", re.I))
        self.angadi_heading = self.page.get_by_role("heading", name=re.compile("Angadi Coaching", re.I))
        self.anjuman_heading = self.page.get_by_role("heading", name=re.compile("Anjuman BCA", re.I))

    def navigate(self) -> None:
        """Navigate to the home page."""
        self.page.goto(self.url, wait_until="domcontentloaded")

    def click_explore_courses(self, index: int = 0) -> None:
        """Click on an explore courses button by index."""
        self.explore_buttons.nth(index).click()

    def get_project_locator(self, project_name: str) -> Locator:
        """Retrieve locator for a live project card."""
        return self.page.get_by_role("heading", name=re.compile(re.escape(project_name), re.I))