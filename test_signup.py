import time
from unittest import TestCase
from base_data import Base_Data
from locators import HomePageLocators, SignupPageLocators

class Test_Signup(TestCase, Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()
        self.accept_cookies()
        self.click_hold(HomePageLocators.HOME_PAGE_JOIN_TMDB_BUTTON_NAV_BAR)

    def test_signup_without_username(self):
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_USERNAME_FIELD, "N/A")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_PASSWORD_FIELD,"1234")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD,"1234")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_EMAIL_FIELD,"Rando_email@yahoo.com")
        self.click_hold(SignupPageLocators.SIGNUP_PAGE_SUBMIT_BUTTON)
        input("Solve CAPTCHA and press ENTER to continue")
        self.check_error_message("Username is required",SignupPageLocators.SIGNUP_ERRORS)

    def test_signup_without_password(self):
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_USERNAME_FIELD, "retest_na")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_PASSWORD_FIELD, "N/A")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD, "N/A")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_EMAIL_FIELD, "Rando_email@yahoo.com")
        self.click_hold(SignupPageLocators.SIGNUP_PAGE_SUBMIT_BUTTON)
        input("Solve CAPTCHA and press ENTER to continue")
        self.check_error_message("Password is required",SignupPageLocators.SIGNUP_ERRORS)

    def test_signup_without_email(self):
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_USERNAME_FIELD, "retest_na")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_PASSWORD_FIELD, "1234")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_PASSWORD_CONFIRM_FIELD, "1234")
        self.insert_text(SignupPageLocators.SIGNUP_PAGE_EMAIL_FIELD, "N/A")
        self.click_hold(SignupPageLocators.SIGNUP_PAGE_SUBMIT_BUTTON)
        input("Solve CAPTCHA and press ENTER to continue")
        self.check_error_message("Email is required",SignupPageLocators.SIGNUP_ERRORS)


    def tearDown(self):
        self.driver.quit()