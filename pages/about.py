"""About page object for DharwadHubballiTutor."""

from playwright.sync_api import Page


class aboutPage:
    """Page Object for About Page."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.dharwadhubballitutor.com/about/"
        self.about_link = self.page.get_by_role("link", name="About", exact=True)
        self.about_heading = self.page.get_by_role(
            "heading", name="About DharwadHubballiTutor"
        )
        self.our_expertise_heading = self.page.get_by_role(
            "heading", name="Our Expertise"
        )
        self.our_vision_heading = self.page.get_by_role("heading", name="Our Vision")
        self.our_mission_heading = self.page.get_by_role("heading", name="Our Mission")
        self.core_values_heading = self.page.get_by_role("heading", name="Core Values")
        self.governance_heading = self.page.get_by_role(
            "heading", name="Governance Philosophy"
        )

    def navigate(self) -> None:
        """Navigate directly to the About page."""
        self.page.goto(self.url, wait_until="domcontentloaded")