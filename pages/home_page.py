from playwright.sync_api import expect
import allure

from constants.constant_urls import URL_HOME_PAGE


class HomePage:
    """
    Class home page site
    Класс домашней страницы сайта
    """

    def __init__(self, page):
        self.page = page

    def open_home(self):
        """
        Method open home page
        Метод открытия главной страницы
        """
        with allure.step('Go to home page'):
            self.page.goto(URL_HOME_PAGE)

    def click_locator(self, name):
        """
        Method click button-locator
        Метод нажатия на кнопку перемещения по сайту
        """
        with allure.step(f"Click button '{name}'"):
            self.page.get_by_role('link', name=name).click()

    def check_url(self, url):
        """
        Method check url
        Метод проверки корректного адреса
        """
        with allure.step('Check correct url'):
            expect(self.page).to_have_url(url)
