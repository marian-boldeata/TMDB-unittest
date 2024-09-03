from unittest import TestCase
from selenium.webdriver.common.by import By

import locators
from base_data import Base_Data
from locators import HomePageLocators

class Test_Login(Base_Data,TestCase):

    def setUp(self):
        self.driver = self.setup_actions()
        self.driver.find_element(*HomePageLocators.HOME_PAGE_LOGIN_BUTTON_NAV_BAR).click()


    def test_login_valid_credentials(self):
        self.insert_login_credentials('mbx-bx',4231)
        assert self.check_if_logged_in()



    def tearDown(self):
        self.driver.quit()