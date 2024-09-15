import time
from unittest import TestCase
from base_data import Base_Data
from locators import HomePageLocators, LoginPageLocators

class Test_Login(Base_Data,TestCase):

    def setUp(self):
        self.driver = self.setup_actions()
        self.accept_cookies()
        self.driver.find_element(*HomePageLocators.HOME_PAGE_LOGIN_BUTTON_NAV_BAR).click()

    def test_login_invalid_username(self):
        self.insert_login_actions('testname_','12345')
        self.check_error_message("We couldn't find your username.", LoginPageLocators.LOGIN_ERRORS)

    def test_login_valid_credentials(self):
        self.insert_text(LoginPageLocators.LOGIN_PAGE_USERNAME_FIELD, "mbx-bx")
        self.insert_text(LoginPageLocators.LOGIN_PAGE_PASSWORD_FIELD,'4231')
        self.click_hold(LoginPageLocators.LOGIN_PAGE_SUBMIT_LOGIN_BUTTON)
        self.check_if_logged_in(), f'User icon not found on nav bar, user not logged in'


    def test_login_blank_password(self):
        self.insert_text(LoginPageLocators.LOGIN_PAGE_USERNAME_FIELD,"mbx-bx")
        self.insert_text(LoginPageLocators.LOGIN_PAGE_PASSWORD_FIELD,"N/A")
        self.click_hold(LoginPageLocators.LOGIN_PAGE_SUBMIT_LOGIN_BUTTON)
        self.check_error_message("We couldn't validate your information. Want to try again?", LoginPageLocators.LOGIN_ERRORS)





    def tearDown(self):
        self.driver.quit()