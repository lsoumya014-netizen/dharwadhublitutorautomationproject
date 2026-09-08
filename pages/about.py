from playwright.sync_api import Page

class aboutPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.dharwadhubballitutor.com/"
        self.about_link = self.page.get_by_role("link", name="About", exact=True)
        self.about_heading = self.page.get_by_role("heading", name="DharwadHubballiTutor", exact=True)
        self.edtech_text = self.page.get_by_text("EdTech & Digital Solutions")
        self.about_dharwadhubballitutor_heading = self.page.get_by_role("heading", name="About DharwadHubballiTutor")
        self.about_dharwadhubballitutor_text = self.page.get_by_text("ABOUT DHARWADHUBBALLITUTOR About DharwadHubballiTutor DharwadHubballiTutor,")
        self.our_expertise_heading = self.page.get_by_role("heading", name="Our Expertise")
        self.our_expertise_text = self.page.get_by_text("OUR EXPERTISE Our Expertise 01 Corporate & Professional Training 02 Online &")
        