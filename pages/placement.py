
from playwright.sync_api import Page

class placementPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_placements(self):
        self.page.goto("https://www.dharwadhubballitutor.com/")
        self.page.get_by_label("Primary navigation").get_by_role("link", name="Placements").click()
        self.page.get_by_role("heading", name="Our Amazing Placement Stories").click()
        self.page.get_by_text("Sukhavindersingh Thakur WellSky").click()
        self.page.locator("div").filter(has_text="Placement Success Our Amazing").first.click()

    def click_placement_story(self, story_text):
        self.page.get_by_text(story_text).click()

    def click_placement_company(self, company_text):
        self.page.get_by_text(company_text).click()

    def click_placement_student(self, student_text):
        self.page.get_by_text(student_text).click()