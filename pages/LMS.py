class LMSPage:
    def __init__(self, page):
        self.page = page
        self.title = "LMS Page"
        self.url = "https://www.dharwadhubballitutor.com/"
        self.lms_login_link = page.get_by_role("link", name="LMS Login")
        self.welcome_back_heading = page.get_by_role("heading", name="Welcome Back")
        self.logo_img = page.get_by_role("img", name="DharwadHubballiTutor Logo")
        self.dharwadhubballitutor_heading = page.get_by_role("heading", name="DharwadHubballiTutor")
        self.empowering_text = page.get_by_text("Empowering the next")
        self.sign_in_with_google_link = page.get_by_role("link", name="Sign in with Google")
        self.sign_in_heading = page.get_by_role("heading", name="Sign in")
        self.email_or_phone_input = page.get_by_role("textbox", name="Email or phone")
        self.next_button = page.get_by_role("button", name="Next")
        self.try_again_link = page.get_by_role("link", name="Try again")