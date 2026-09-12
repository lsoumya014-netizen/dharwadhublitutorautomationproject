"""Data-Driven End-to-End Tests for DharwadHubballiTutor Website.

This test suite utilizes external JSON test data from the `testdata/` directory
and leverages the Page Object Model (POM) from the `pages/` package.
"""

import json
import re
import sys
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pages import (
    CataloguePage,
    Demopage,
    HomePage,
    LMSPage,
    aboutPage,
    contactPage,
    placementPage,
)

BASE_URL = "https://www.dharwadhubballitutor.com/"
TESTDATA_DIR = PROJECT_ROOT / "testdata"


def load_test_data(filename: str) -> dict:
    """Helper to load JSON test data file."""
    with open(TESTDATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


# Load all JSON datasets
CONTACT_DATA = load_test_data("contact.json")
DEMO_DATA = load_test_data("demo.json")
HOME_DATA = load_test_data("home.json")
ABOUT_DATA = load_test_data("about.json")
PLACEMENT_DATA = load_test_data("placement.json")
LMS_DATA = load_test_data("lms.json")
TRAININGS_DATA = load_test_data("trainings.json")
INTERNSHIPS_DATA = load_test_data("internships.json")
JOBS_DATA = load_test_data("jobs.json")
WORKSHOPS_DATA = load_test_data("workshops.json")
SERVICES_DATA = load_test_data("services.json")
BLOGS_DATA = load_test_data("blogs.json")
PROJECTS_DATA = load_test_data("projects.json")
ALUMNI_DATA = load_test_data("alumni.json")


def test_contact_page_displays_enquiry_form(page: Page) -> None:
    """Validate that Contact page displays all enquiry form controls and branch locations."""
    data = CONTACT_DATA["test_enquiry_form"]
    contact = contactPage(page)
    contact.navigate()

    expect(contact.username).to_be_visible()
    expect(contact.email).to_be_visible()
    expect(contact.mobile_number).to_be_visible()
    expect(contact.training).to_be_visible()
    expect(contact.submit_button).to_be_visible()

    # Fill form with DDT data
    contact.fill_contact_form(
        name=data["name"],
        email=data["email"],
        mobile_number=data["mobile_number"],
    )

    for branch in data["expected_branches"]:
        expect(page.get_by_text(branch).first).to_be_visible()


def test_demo_dialog_displays_required_fields(page: Page) -> None:
    """Validate that Book Demo modal dialog displays all required inputs and submits data."""
    data = DEMO_DATA["test_book_demo_valid"]
    home = HomePage(page)
    home.navigate()

    demo = Demopage(page)
    demo.open_demo_dialog()

    expect(demo.name_input).to_be_visible()
    expect(demo.email_input).to_be_visible()
    expect(demo.number_input).to_be_visible()
    expect(demo.demo_class_select).to_be_visible()
    expect(demo.submit_button).to_be_visible()

    # Fill demo modal with DDT data
    demo.fill_demo_form(
        name=data["name"],
        email=data["email"],
        number=data["mobile_number"],
    )


def test_home_page_displays_programs(page: Page) -> None:
    """Validate home page title, core program headings, and accreditations."""
    data = HOME_DATA["test_home_metadata"]
    home = HomePage(page)
    home.navigate()

    expect(page).to_have_title(re.compile(data["title_keyword"], re.I))
    expect(home.discover_programs_heading).to_be_visible()
    expect(home.popular_courses_heading).to_be_visible()


def test_about_page_displays_company_information(page: Page) -> None:
    """Validate company background, vision, mission, and expertise on About page."""
    data = ABOUT_DATA["test_about_page"]
    about = aboutPage(page)
    about.navigate()

    expect(about.about_heading).to_be_visible()
    expect(about.our_expertise_heading).to_be_visible()
    expect(about.our_vision_heading).to_be_visible()
    expect(about.our_mission_heading).to_be_visible()


def test_placements_page_displays_success_stories(page: Page) -> None:
    """Validate placement stories and student details on Placements page."""
    data = PLACEMENT_DATA["test_placement_stories"]
    placements = placementPage(page)
    placements.navigate()

    expect(placements.placements_heading).to_be_visible()

    for student in data["placed_students"]:
        expect(placements.get_student_story(student)).to_be_visible()


def test_lms_link_opens_login_page(page: Page) -> None:
    """Validate that LMS link successfully navigates to LMS authentication portal."""
    data = LMS_DATA["test_lms_navigation"]
    lms = LMSPage(page)
    lms.navigate()

    expect(page).to_have_title(data["expected_title"])
    expect(lms.welcome_back_heading).to_be_visible()


def test_trainings_page_displays_training_catalogue(page: Page) -> None:
    """Validate that Trainings section on home page displays catalogue information."""
    data = TRAININGS_DATA["test_trainings_catalogue"]
    home = HomePage(page)
    home.navigate()

    expect(page.get_by_role("heading", name=data["program_heading"])).to_be_visible()
    expect(page.get_by_text(data["expected_text"]).first).to_be_visible()


def test_explore_courses_reveals_course_section(page: Page) -> None:
    """Validate clicking Explore Courses reveals popular courses section."""
    home = HomePage(page)
    home.navigate()
    home.click_explore_courses(0)

    expect(home.popular_courses_heading).to_be_visible()


def test_internship_page_displays_internship_catalogue(page: Page) -> None:
    """Validate exploring Internship programme reveals course catalogue."""
    data = INTERNSHIPS_DATA["test_internships_catalogue"]
    catalogue = CataloguePage(page)
    catalogue.navigate()
    catalogue.explore_program(data["explore_button_index"])

    expect(catalogue.get_popular_courses_heading()).to_be_visible()


def test_jobs_page_displays_job_catalogue(page: Page) -> None:
    """Validate exploring Jobs programme reveals job-oriented course options."""
    data = JOBS_DATA["test_jobs_catalogue"]
    catalogue = CataloguePage(page)
    catalogue.navigate()
    catalogue.explore_program(data["explore_button_index"])

    expect(catalogue.get_popular_courses_heading()).to_be_visible()


def test_blogs_page_displays_blog_catalogue(page: Page) -> None:
    """Validate exploring Blogs programme reveals articles list."""
    data = BLOGS_DATA["test_blogs_catalogue"]
    catalogue = CataloguePage(page)
    catalogue.navigate()
    catalogue.explore_program(data["explore_button_index"])

    expect(catalogue.get_popular_courses_heading()).to_be_visible()


def test_workshops_page_displays_workshop_catalogue(page: Page) -> None:
    """Validate exploring Workshops programme reveals workshop modules."""
    data = WORKSHOPS_DATA["test_workshops_catalogue"]
    catalogue = CataloguePage(page)
    catalogue.navigate()
    catalogue.explore_program(data["explore_button_index"])

    expect(catalogue.get_popular_courses_heading()).to_be_visible()


def test_services_page_displays_services_catalogue(page: Page) -> None:
    """Validate exploring Services programme reveals services catalogue."""
    data = SERVICES_DATA["test_services_catalogue"]
    catalogue = CataloguePage(page)
    catalogue.navigate()
    catalogue.explore_program(data["explore_button_index"])

    expect(catalogue.get_popular_courses_heading()).to_be_visible()


def test_alumni_section_displays_partner_companies(page: Page) -> None:
    """Validate Our Alumni Work At section and hiring partner logos on home page."""
    data = ALUMNI_DATA["test_alumni_section"]
    home = HomePage(page)
    home.navigate()

    expect(home.alumni_heading).to_be_visible()
    expect(page.locator("#alumniCfCarousel, .alumni-cf-container, #alumni").first).to_be_attached()
    for company in data["companies"]:
        expect(page.locator(f"img[alt*='{company}']").first).to_be_attached()


def test_projects_section_displays_live_projects(page: Page) -> None:
    """Validate Our Live Projects section and real-time client projects."""
    data = PROJECTS_DATA["test_projects_section"]
    home = HomePage(page)
    home.navigate()

    expect(home.live_projects_heading).to_be_visible()
    for project in data["projects"]:
        expect(home.get_project_locator(project["title"]).first).to_be_visible()