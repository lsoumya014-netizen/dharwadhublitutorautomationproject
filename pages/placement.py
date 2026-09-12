"""Placements page object for DharwadHubballiTutor."""

from playwright.sync_api import Locator, Page


class placementPage:
    """Page Object for Placements Page."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.dharwadhubballitutor.com/placements/"
        self.placements_heading = self.page.get_by_role(
            "heading", name="Our Amazing Placement Stories"
        )
        self.sukhavindersingh_thakur = self.page.get_by_text("Sukhavindersingh Thakur")

    def navigate(self) -> None:
        """Navigate to the Placements page."""
        self.page.goto(self.url, wait_until="domcontentloaded")

    def get_student_story(self, student_name: str) -> Locator:
        """Get locator for a placed student story."""
        return self.page.get_by_text(student_name)