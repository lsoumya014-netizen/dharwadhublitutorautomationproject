import re
from playwright.sync_api import Page, expect


def test_best_digital_marketing_course_online_and_offline(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Best Digital Marketing Course (Online & Offline) ").click()
    page.get_by_text("Digital Marketing Training").click()
    page.get_by_role("paragraph").nth(5).click()
    page.get_by_text("Digital Marketing Training with Guaranteed Placement Assistance. Course").click()
    page.get_by_text("Topic 3: Content Marketing").click()
    page.get_by_text("Topic 2: Blog MarketingÂ").click()
    page.get_by_text("Topic 4: Graphic Designing").click()
    page.locator("div:nth-child(3) > .program-card > .program-footer").click()
    page.locator("#courseModal").click()


def test_email_marketing_course(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Email Marketing ").click()
    page.locator("div").filter(has_text="Email marketingÂ is the act").nth(5).click()


def test_social_media_marketing_course(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Social Media Marketing ").click()
    page.locator("div").filter(has_text="The term social media").nth(5).click()
    page.get_by_role("heading", name="Social media marketing characteristics.").click()


def test_search_engine_optimization_course(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Search Engine Optimization ").click()
    page.get_by_role("heading", name="Why should we use SEO in").click()


def test_search_engine_marketing_course(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Search Engine Marketing ").click()
    page.get_by_role("heading", name="Benefits").click()
    page.get_by_role("heading", name="Increase Traffic Through Ad").click()


def test_whatsapp_marketing_course(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Whatsapp Marketing ").click()
    page.get_by_text("WhatsApp marketing isÂ a type").click()
    page.locator("div").filter(has_text="WhatsApp marketing isÂ a type").nth(5).click()


def test_sms_marketing_course(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" SMS Marketing ").click()
    page.locator("div").filter(has_text="SMS marketing isÂ the").nth(3).click()


def test_digital_marketing_course_dharwad_page(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Best Digital Marketing Course in Dharwad | DharwadHubballiTutor ").click()
    page.locator("#main-content").get_by_role("heading", name="Best Digital Marketing Course").click()
    page.get_by_text("Best Digital Marketing Course in Dharwad | DharwadHubballiTutor Learn Digital").click()
    page.get_by_text("Best Digital Marketing Course in Dharwad | DharwadHubballiTutor Learn Digital").click()


def test_ai_tools_course_for_mba_dharwad(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Best AI Tools Course for MBA Students in Dharwad | DharwadHubballiTutor ").click()
    page.locator("#main-content").get_by_role("heading", name="Best AI Tools Course for MBA").click()
    page.get_by_text("Best AI Tools Course for MBA Students in Dharwad | DharwadHubballiTutor Learn").click()


def test_ai_tools_course_for_mba_hubli(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Best AI Tools Course for MBA Students in Hubli | DharwadHubballiTutor ").click()
    page.locator("#main-content").get_by_role("heading", name="Best AI Tools Course for MBA").click()
    page.get_by_role("heading", name="Why Should MBA Students Learn").click()
    page.get_by_role("heading", name="Skills Covered").click()


def test_digital_marketing_with_generative_ai_course(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Digital Marketing with Generative AI Course in Dharwad | AI Marketing").click()
    page.locator("div").filter(has_text="Digital Marketing with Generative AI Course in Dharwad Learn Digital Marketing").nth(5).click()
    page.get_by_role("heading", name="Why Learn Digital Marketing").click()
    page.get_by_role("heading", name="Tools Covered").click()
    page.get_by_role("heading", name="Generative AI for Digital").click()
    page.get_by_role("heading", name="SEO & AI SEO").click()


def test_digital_marketing_course_curriculum(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Digital Marketing Course").click()
    page.get_by_role("heading", name="Want to Know the Current").click()
    page.get_by_role("heading", name="What Is Included in the").click()
    page.get_by_text("Digital Marketing Course Fees in Dharwad and Hubli – 2026 If you are looking").click()


def test_digital_marketing_course_fees(page: Page) -> None: # type: ignore
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" Digital Marketing Course").click()
    page.get_by_role("heading", name="Digital Marketing Course Fees in Dharwad and Hubli –").click()
    page.get_by_role("heading", name="Digital Marketing Course Fees in Dharwad & Hubli", exact=True).click()
    page.get_by_role("heading", name="Search Engine Optimization (").click()


def test_php_full_stack_development_course(page: Page) -> None:
    page.goto("https://www.dharwadhubballitutor.com/")
    page.get_by_role("button", name="Explore Courses").nth(2).click()
    page.get_by_role("link", name=" PHP Full Stack Development").click()
    page.get_by_text("Looking for PHP Full Stack Development course fees in Dharwad or Hubli? Before").click()
    page.get_by_role("heading", name="PHP Full Stack Development Course Fees", exact=True).click()
    page.get_by_text("HTML5 CSS3 JavaScript").click()
    page.get_by_text("E-Commerce Website Student").click()
    page.get_by_role("heading", name="Who Can Join PHP Full Stack").click()
    page.get_by_role("heading", name="Career Opportunities After").click()
