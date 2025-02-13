from playwright.sync_api import expect

from constants.constant_urls import URL_HOME_PAGE


class HomePage:

    def __init__(self, page):
        self.page = page

    def open_home(self):
        self.page.goto(URL_HOME_PAGE)

    def click_locator(self, name):
        self.page.get_by_role('link', name=name).click()

    def check_url(self, url):
        expect(self.page).to_have_url(url)
