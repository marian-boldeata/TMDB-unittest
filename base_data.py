


from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC

import locators

class Base_Data():

    def setup_actions(self):
        self.driver = Driver()
        self.driver.get("https://www.themoviedb.org/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.action = ActionChains(self.driver)
        return self.driver

    def accept_cookies(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()


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


    def wait_ENTER(self,locator):
        element = WebDriverWait(self.driver,3).until(EC.presence_of_element_located(locator))
        element.send_keys(Keys.ENTER)

    def click_hold(self,locator):
        button = self.driver.find_element(*locator)
        self.action.move_to_element(button).pause(0.5).click().perform()



    def check_if_logged_in(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.HomePageLocators.NAV_BAR_USER_ICON))
            assert True,"User icon visible, user logged in."
        except TimeoutException:
            assert False,"User icon not visible, loggin test failed"


    def check_error_message(self, expected_message, locator):
        is_error_correct = False
        actual_error_message = self.driver.find_element(*locator).text
        if expected_message == actual_error_message:
            is_error_correct = True
        assert is_error_correct, f'expected error : {expected_message}, received : {actual_error_message}'

    def validate_search_results(self,search_term):
        validated = False
        result_items = self.driver.find_elements(*locators.SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        result_titles_text = []
        for item in result_items:
            if item.is_displayed():
                movie_title = item.text
                result_titles_text.append(movie_title.lower())
        for i in range(len(result_titles_text)):
            if search_term in result_titles_text[i]:
                validated = True
        assert validated

    def validate_no_search_results(self):
        validated = False
        if self.driver.find_element(*locators.SearchPageLocators.SEARCH_PAGE_NO_SEARCH_RESULTS).is_displayed():
            validated = True

        assert validated

    def validate_filter_option(self, locator, filter_option):
        validated = False

        result_list = self.driver.find_elements(*locator)
        for item in result_list:
            if item.is_displayed():
                item_type = item.get_attribute('data-media-type')
                if item_type == filter_option:
                    validated = True
                elif item_type != filter_option:
                    validated = False
                    break

        assert validated, f'filter option {filter_option} failed validation'


    def validate_language_select(self,language, locator):
        main_page_banner_welcome = {
            '(es-ES)': 'Te damos la bienvenida.',
            '(ro-RO)': 'Bun venit.',
            '(de-DE)': 'Willkommen.'
        }

        if language in main_page_banner_welcome:
            element = self.driver.find_element(*locator)
            banner_welcome_text = element.text

        assert banner_welcome_text == main_page_banner_welcome[language], f'Expected : {main_page_banner_welcome[language]}, got {banner_welcome_text}'







