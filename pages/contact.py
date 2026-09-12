"""Contact page object for DharwadHubballiTutor."""

from playwright.sync_api import Page


class contactPage:
    """Page Object for Contact Page and Enquiry Form."""

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.dharwadhubballitutor.com/contact/"

        # Form fields
        self.username = page.get_by_role("textbox", name="Name")
        self.email = page.get_by_role("textbox", name="Email")
        self.mobile_number = page.get_by_role("textbox", name="Mobile Number")
        self.training = page.get_by_label("Trainings")
        self.submit_button = page.get_by_role("button", name="Submit Enquiry")

        # Contact information locators
        self.call_us = page.get_by_text("☎ Call Us")
        self.email_us = page.get_by_text("✉ Email Us")
        self.visit_us = page.get_by_text("Visit Us")

        # Branch locators
        self.dharwad_branch = page.get_by_text("Dharwad Branch").first
        self.hubballi_branch = page.get_by_text("Hubballi Branch").first
        self.belagavi_branch = page.get_by_text("Belagavi Branch").first

    def navigate(self) -> None:
        """Navigate to the contact page."""
        self.page.goto(self.url, wait_until="domcontentloaded")

    def fill_contact_form(
        self,
        name: str,
        email: str,
        mobile_number: str,
        training: str | None = None,
    ) -> None:
        """Fill in contact enquiry form fields."""
        self.username.fill(name)
        self.email.fill(email)
        self.mobile_number.fill(mobile_number)
        if training:
            try:
                self.training.select_option(label=training)
            except Exception:
                pass
