import time
from unittest import TestCase
from base_data import Base_Data
from locators import HomePageLocators, SearchPageLocators, MyAccountLocators, ItemDetailsPage

class Test_Watchlist(TestCase, Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()
        self.accept_cookies()



    @Base_Data.login_required
    def test_add_to_watchlist(self):
        self.driver.get("https://www.themoviedb.org/")
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR,"ethernal city")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.click_on(SearchPageLocators.SEARCH_PAGE_MOVIE_FILTER)

        item_title = self.driver.find_element(*SearchPageLocators.SEARCH_RESULT_ITEM_TITLE).text

        self.click_on(SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        self.click_on(ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_WATCHLIST)

        self.hover_over_click_chain(MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN, MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN_WATCHLIST)

        self.check_if_added(item_title,MyAccountLocators.MY_ACCOUNT_USER_WATCHLIST_FIRST_TITLE)






    def tearDown(self):
        self.driver.quit()