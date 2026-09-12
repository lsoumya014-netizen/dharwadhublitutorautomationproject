"""LMS login page object."""

from playwright.sync_api import Page


class LMSPage:
    """Page Object for LMS Login Page."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://dharwadhubballitutor.com/lms/views/login.php"
        self.welcome_back_heading = page.get_by_role("heading", name="Welcome Back")
        self.dharwadhubballitutor_heading = page.get_by_role("heading", name="DharwadHubballiTutor")
        self.sign_in_with_google_link = page.get_by_role("link", name="Sign in with Google")

    def navigate(self) -> None:
        """Navigate to the LMS login page."""
        self.page.goto(self.url, wait_until="domcontentloaded")