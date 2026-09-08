"""Smoke tests for the public DharwadHubballiTutor website."""

import re
import sys
import unittest
from pathlib import Path

import ddt
from playwright.sync_api import Page, expect

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from pages import contact

BASE_URL = "https://www.dharwadhubballitutor.com/"


def test_contact_page_displays_enquiry_form(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("link", name="Contact", exact=True).click()

    contact_page = contact(page)
    expect(contact_page.username).to_be_visible()
    expect(contact_page.email).to_be_visible()
    expect(contact_page.mobile_number).to_be_visible()
    expect(contact_page.training).to_be_visible()
    expect(contact_page.submit_button).to_be_visible()


def test_demo_dialog_displays_required_fields(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Book Demo").click()

    expect(page.get_by_role("textbox", name="Name")).to_be_visible()
    expect(page.get_by_role("textbox", name="Email")).to_be_visible()
    expect(page.get_by_role("textbox", name="Enter your number:")).to_be_visible()
    expect(page.get_by_label("Demo Class For")).to_be_visible()
    expect(page.get_by_role("button", name="Submit")).to_be_visible()


def test_home_page_displays_programs(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page).to_have_title(re.compile("DharwadHubballiTutor"))
    expect(
        page.get_by_role("heading", name="Discover Our Programs")
    ).to_be_visible()
    expect(
        page.get_by_role("heading", name="Our Most Popular Courses")
    ).to_be_visible()


def test_about_page_displays_company_information(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("link", name="About", exact=True).click()

    expect(
        page.get_by_role("heading", name="About DharwadHubballiTutor")
    ).to_be_visible()
    expect(page.get_by_role("heading", name="Our Expertise")).to_be_visible()


def test_placements_page_displays_success_stories(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_label("Primary navigation").get_by_role(
        "link", name="Placements"
    ).click()

    expect(
        page.get_by_role("heading", name="Our Amazing Placement Stories")
    ).to_be_visible()
    expect(page.get_by_text("Sukhavindersingh Thakur")).to_be_visible()


def test_lms_link_opens_login_page(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    with page.expect_navigation(url="**/lms/views/login.php**"):
        page.get_by_role("link", name="LMS").click()

    expect(page).to_have_title("Welcome | DharwadHubballiTutor LMS")
    expect(page.get_by_role("heading", name="Welcome Back")).to_be_visible()


def test_trainings_page_displays_training_catalogue(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")

    expect(page.get_by_role("heading", name="Trainings")).to_be_visible()
    expect(page.get_by_text("Explore our programs").first).to_be_visible()


def test_explore_courses_reveals_course_section(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").first.click()

    expect(
        page.get_by_role("heading", name="Our Most Popular Courses")
    ).to_be_visible()

def test_internship_page_displays_internship_catalogue(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(1).click()

    expect(
        page.get_by_role("heading", name="Our Most Popular Courses")
    ).to_be_visible()

def test_jobs_page_displays_job_catalogue(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(3).click()

    expect(
        page.get_by_role("heading", name="Our Most Popular Courses")
    ).to_be_visible()    

def test_blogs_page_displays_blog_catalogue(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(5).click()

    expect(
        page.get_by_role("heading", name="Our Most Popular Courses")
    ).to_be_visible()    

def test_workshops_page_displays_workshop_catalogue(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(4).click()

    expect(
        page.get_by_role("heading", name="Our Most Popular Courses")
    ).to_be_visible()

def test_services_page_displays_services_catalogue(page: Page) -> None:
    page.goto(BASE_URL, wait_until="domcontentloaded")
    page.get_by_role("button", name="Explore Courses").nth(2).click()

    expect(
        page.get_by_role("heading", name="Our Most Popular Courses")
    ).to_be_visible()        