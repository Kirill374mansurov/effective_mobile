from playwright.sync_api import Page
import allure

from pages.home_page import HomePage
from constants.constant_urls import (URL_ABOUT, URL_CASES, URL_CONTACTS,
                                     URL_MOREINFO, URL_REVIEWS)
from constants.constant_locators import (LOCATOR_ABOUT, LOCATOR_CASES, LOCATOR_CONTACTS,
                                         LOCATOR_MOREINFO, LOCATOR_REVIEWS)


@allure.feature('Home page')
@allure.story('About locator')
def test_about(page: Page):
    """
    This test tests about locator
    Этот тест тестирует перемещение в область 'О нас'
    """
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_ABOUT)
    home_page.check_url(URL_ABOUT)


@allure.feature('Home page')
@allure.story('Moreinfo locator')
def test_moreinfo(page: Page):
    """
    This test tests moreinfo locator
    Этот тест тестирует перемещение в область 'Услуги'
    """
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_MOREINFO)
    home_page.check_url(URL_MOREINFO)


@allure.feature('Home page')
@allure.story('Cases locator')
def test_cases(page: Page):
    """
    This test tests cases locator
    Этот тест тестирует перемещение в область 'Проекты'
    """
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_CASES)
    home_page.check_url(URL_CASES)


@allure.feature('Home page')
@allure.story('Reviews locator')
def test_reviews(page: Page):
    """
    This test tests reviews locator
    Этот тест тестирует перемещение в область 'Отзывы'
    """
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_REVIEWS)
    home_page.check_url(URL_REVIEWS)


@allure.feature('Home page')
@allure.story('Contacts locator')
def test_contacts(page: Page):
    """
    This test tests contacts locator
    Этот тест тестирует перемещение в область 'Контакты'
    """
    home_page = HomePage(page)
    home_page.open_home()
    home_page.click_locator(LOCATOR_CONTACTS)
    home_page.check_url(URL_CONTACTS)
