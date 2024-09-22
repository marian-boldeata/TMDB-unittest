


from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from functools import wraps


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



    def insert_text(self, locator, text):
        if text == "N/A":
            pass
        else:
            self.driver.find_element(*locator).send_keys(text)

    def insert_login_actions(self,username, password):
        self.driver.find_element(*locators.HomePageLocators.HOME_PAGE_LOGIN_BUTTON_NAV_BAR).click()
        self.driver.find_element(*locators.LoginPageLocators.LOGIN_PAGE_USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*locators.LoginPageLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(password)
        self.click_hold(locators.LoginPageLocators.LOGIN_PAGE_SUBMIT_LOGIN_BUTTON)

    # decorator function for test that require logged in user
    def login_required(fnc):
        @wraps(fnc)
        def wrapper(self, *args, **kwargs):

            self.insert_login_actions(username="mbx-bx",password="4231")
            return fnc(self, *args, **kwargs)

        return wrapper


    def click_on(self,locator):
        self.driver.find_element(*locator).click()


    def wait_ENTER(self,locator):
        element = WebDriverWait(self.driver,3).until(EC.presence_of_element_located(locator))
        element.send_keys(Keys.ENTER)

    def click_hold(self,locator):
        button = self.driver.find_element(*locator)
        self.action.move_to_element(button).pause(0.5).click().perform()

    def hover_over_click_chain(self, locator, locator1='', locator2=''):
        if locator1 == '' and locator2 == '':
            element = self.driver.find_element(*locator)
            self.action.move_to_element(element).click().perform()

        elif locator1 != '' and locator2 == '':
            element = self.driver.find_element(*locator)
            self.action.move_to_element(element).click().perform()

            element1 = self.driver.find_element(*locator1)
            self.action.move_to_element(element1).click().perform()

        elif locator1 != '' and locator2 != '':
            element = self.driver.find_element(*locator)
            self.action.move_to_element(element).click().perform()

            element1 = self.driver.find_element(*locator1)
            self.action.move_to_element(element1).click().perform()

            element2 = self.driver.find_element(*locator2)
            self.action.move_to_element(element2).click().perform()



    def check_if_logged_in(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.HomePageLocators.NAV_BAR_USER_ICON))
            assert True,"User icon visible, user logged in."
        except TimeoutException:
            assert False,"User icon not visible, loggin test failed"

    def check_if_logged_out(self):
        try:
            WebDriverWait(self.driver,5).until(EC.presence_of_element_located(locators.HomePageLocators.HOME_PAGE_LOGGED_OUT_BANNER))
            assert True, "Log out banner visible, user logged out"
        except TimeoutException:
            assert False, "User still logged in"

    def check_if_added(self, item_name, locator):
        verified = False
        actual_item = self.driver.find_element(*locator).text
        if item_name == actual_item:
            verified = True
        assert verified, f'Adeed item {item_name}  not same as item in watchlist {actual_item}'

    def check_if_removed(self, item_name, locator):
        try:
            actual_item = self.driver.find_element(*locator).text
            self.assertNotEqual(item_name,actual_item, f'{item_name} was not deleted')
        except NoSuchElementException:
            self.assertTrue(True,f'{item_name} was removed')
            assert True


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







