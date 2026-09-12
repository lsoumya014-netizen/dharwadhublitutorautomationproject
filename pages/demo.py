"""Demo modal dialog page object."""

from playwright.sync_api import Page


class Demopage:
    """Page Object for the Book Demo modal dialog."""

    def __init__(self, page: Page):
        self.page = page
        self.book_demo_button = page.get_by_role("button", name="Book Demo")
        self.name_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.number_input = page.get_by_role("textbox", name="Enter your number:")
        self.demo_class_select = page.get_by_label("Demo Class For")
        self.submit_button = page.get_by_role("button", name="Submit")

    def open_demo_dialog(self) -> None:
        """Open the Book Demo modal dialog."""
        self.book_demo_button.click()

    def fill_demo_form(
        self,
        name: str,
        email: str,
        number: str,
        demo_class: str | None = None,
    ) -> None:
        """Fill in demo class booking fields."""
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.number_input.fill(number)
        if demo_class:
            try:
                self.demo_class_select.select_option(label=demo_class)
            except Exception:
                pass
