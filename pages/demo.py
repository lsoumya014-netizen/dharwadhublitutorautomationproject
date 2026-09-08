from playwright.sync_api import Page


class Demopage:
    def __init__(self, page: Page):
        self.page = page
        self.title = "Demo Page"
        self.url = "https://www.dharwadhubballitutor.com/"
        self.book_demo_button = page.get_by_role("button", name="Book Demo")
        self.name_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.number_input = page.get_by_role("textbox", name="Enter your number:")
        self.demo_class_select = page.get_by_label("Demo Class For")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.csrf_error = page.get_by_text("CSRF token validation failed")
