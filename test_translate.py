import time
from unittest import TestCase

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base_data import Base_Data
from locators import HomePageLocators, SearchPageLocators

class Test_Translate(TestCase, Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()
        self.accept_cookies(HomePageLocators.ACCEPT_COOKIES_BUTTON)


    def test_language_switch_to(self):
        language = ["(de-DE)","(ro-RO)","(es-ES)"]
        for item in language:
            self.click_on(HomePageLocators.HOME_PAGE_TRANSLATE_BUTTON)
            self.click_on(HomePageLocators.HOME_PAGE_DEFAULT_LANGUAGE_DROP)
            self.insert_text(HomePageLocators.HOME_PAGE_DEFAULT_LANGUAGE_FIELD, item)
            time.sleep(0.5)
            self.wait_ENTER(HomePageLocators.HOME_PAGE_DEFAULT_LANGUAGE_FIELD)
            time.sleep(0.5)
            self.click_hold(HomePageLocators.HOME_PAGE_LANGUAGE_RELOAD_BUTTON)
            time.sleep(0.5)
            self.validate_language_select(item, HomePageLocators.HOME_PAGE_BANNER_TITLE)

    """
    Need to verify why this does not run properly without time.sleep()
    Implicit wait ruled out
    """
    def tearDown(self):
        self.driver.quit()

