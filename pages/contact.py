class contactPage:
    def __init__(self, page):
        self.page = page
        self.username =  page.get_by_role("textbox", name="Name")
        self.email = page.get_by_role("textbox", name="Email")
        self.mobile_number = page.get_by_role("textbox", name="Mobile Number")
        self.training = page.get_by_label("Trainings")
        self.submit_button = page.get_by_role("button", name="Submit Enquiry")
        self.call_us = page.get_by_text("☎ Call Us +91 97412 37334 +91 80079")
        self.email_us = page.get_by_text("✉ Email Us info@")
        self.visit_us = page.get_by_text("Visit Us Dharwad Branch View")
        self.dharwad_branch = page.get_by_label("We're Here to Help").get_by_text("Dharwad Branch")
        self.hubballi_branch = page.get_by_label("We're Here to Help").get_by_text("Hubballi Branch")
        self.belagavi_branch = page.get_by_label("We're Here to Help").get_by_text("Belagavi Branch")

    def fill_contact_form(self, name, email, mobile_number , training):
        self.username.fill(name)
        self.email.fill(email)
        self.mobile_number.fill(mobile_number)
        self.training.select_option(training)
        self.submit_button.click()      
        self.call_us.click()
        self.email_us.click()
        self.visit_us.click()
        self.dharwad_branch.click()
        self.hubballi_branch.click()
        self.belagavi_branch.click()
