import time
from unittest import TestCase


from base_data import Base_Data
from locators import HomePageLocators, SearchPageLocators

class Test_Search(TestCase, Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()



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

    def test_search_filter_options(self):
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR, "garfield")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)

        filter_options_list = [SearchPageLocators.SEARCH_PAGE_PEOPLE_FILTER,
                               SearchPageLocators.SEARCH_PAGE_TV_SHOWS_FILTER,
                               SearchPageLocators.SEARCH_PAGE_COLLECTIONS_FILTER,
                               SearchPageLocators.SEARCH_PAGE_MOVIE_FILTER]


        for i in range(len(filter_options_list)):
            self.driver.find_element(*filter_options_list[i]).click()
            filter_option = self.driver.find_element(*filter_options_list[i]).get_attribute('id')
            self.validate_filter_option(SearchPageLocators.SEARCH_PAGE_ITEM_DATA_TYPE ,filter_option)





    def tearDown(self):
        self.driver.quit()