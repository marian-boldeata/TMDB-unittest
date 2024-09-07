from unittest import TestCase
from base_data import Base_Data
from locators import HomePageLocators, SearchPageLocators

class Test_Search(TestCase, Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()
        self.driver.find_element(*HomePageLocators.ACCEPT_COOKIES_BUTTON).click()

    def test_search_results_validated(self):
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR,"garfield")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        validated = False
        result_items = self.driver.find_elements(*SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        result_titles_text = []
        for item in result_items:
            if item.is_displayed():
                movie_title = item.text
                result_titles_text.append(movie_title.lower())
        for i in range(len(result_titles_text)):
            if "garfield" in result_titles_text[i]:
                validated = True

        assert validated

    def test_no_search_results(self):
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR, "asdasdasdasdqqqqqqqqqqqqq")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        validated = False
        if self.driver.find_element(SearchPageLocators.SEARCH_PAGE_NO_SEARCH_RESULTS).is_displayed():
            validated = True

        assert validated



    def tearDown(self):
        self.driver.quit()