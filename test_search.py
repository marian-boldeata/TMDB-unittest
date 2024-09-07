import time
from unittest import TestCase
from base_data import Base_Data
from locators import HomePageLocators, SearchPageLocators

class Test_Search(TestCase, Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()
        self.accept_cookies(HomePageLocators.ACCEPT_COOKIES_BUTTON)


    def test_search_results_validated(self):
        search_term = "garfield"
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR,search_term)
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.validate_search_results(search_term)

    def test_no_search_results(self):
        search_term = "asdasdasdasdqqqqqqqqqqqqq"
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR, search_term)
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.validate_no_search_results()



    def tearDown(self):
        self.driver.quit()