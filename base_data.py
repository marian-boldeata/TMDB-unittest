import unittest

from selenium.webdriver.common.by import By
from seleniumbase import Driver
import locators

class Base_Data():

    def setup_actions(self):
        self.driver = Driver()
        self.driver.get("https://www.themoviedb.org/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver

    def insert_text(self, locator, text):
        if text == "N/A":
            pass
        else:
            self.driver.find_element(*locator).send_keys(text)

    def insert_login_actions(self,username, password):
        self.driver.find_element(*locators.LoginPageLocators.LOGIN_PAGE_USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*locators.LoginPageLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*locators.LoginPageLocators.LOGIN_PAGE_SUBMIT_LOGIN_BUTTON).click()

    def click_on(self,locator):
        self.driver.find_element(*locator).click()

    def check_if_logged_in(self):
        element = self.driver.find_element(*locators.HomePageLocators.NAV_BAR_USER_ICON)
        if element.is_displayed():
            return True
        else:
            return False

    def check_error_message(self, expected_message, locator):
        is_error_correct = False
        actual_error_message = self.driver.find_element(*locator).text
        if expected_message == actual_error_message:
            is_error_correct = True
        return is_error_correct

