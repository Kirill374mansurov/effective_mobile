from playwright.sync_api import Page

from pages.home_page import HomePage
from constants.constant_urls import (URL_ABOUT, URL_CASES, URL_CONTACTS,
                                     URL_MOREINFO, URL_REVIEWS)
from constants.constant_locators import (LOCATOR_ABOUT, LOCATOR_CASES, LOCATOR_CONTACTS,
                                         LOCATOR_MOREINFO, LOCATOR_REVIEWS)


def test_about(page: Page):
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_ABOUT)
    home_page.check_url(URL_ABOUT)


def test_moreinfo(page: Page):
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_MOREINFO)
    home_page.check_url(URL_MOREINFO)


def test_cases(page: Page):
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_CASES)
    home_page.check_url(URL_CASES)


def test_reviews(page: Page):
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_REVIEWS)
    home_page.check_url(URL_REVIEWS)


def test_contacts(page: Page):
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_CONTACTS)
    home_page.check_url(URL_CONTACTS)
