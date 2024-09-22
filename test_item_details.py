import time
from unittest import TestCase
from base_data import Base_Data
from locators import HomePageLocators, SearchPageLocators, MyAccountLocators, ItemDetailsPage

class Test_Item_Details(TestCase, Base_Data):

    def setUp(self):
        self.driver = self.setup_actions()
        self.insert_login_actions('mbx-bx','4231')


    def test_add_to_watchlist(self):
        self.driver.get("https://www.themoviedb.org/")
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR,"ethernal city")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.click_on(SearchPageLocators.SEARCH_PAGE_MOVIE_FILTER)
        item_title = self.driver.find_element(*SearchPageLocators.SEARCH_RESULT_ITEM_TITLE).text
        self.click_on(SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        self.click_on(ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_WATCHLIST)
        self.hover_over_click_chain(MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN, MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN_WATCHLIST)
        self.check_if_added(item_title,MyAccountLocators.MY_ACCOUNT_USER_MOVIE_CARDS_FIRST_TITLE)

    def test_remove_from_watchlist(self):
        self.driver.get("https://www.themoviedb.org/")
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR, "ethernal city")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.click_on(SearchPageLocators.SEARCH_PAGE_MOVIE_FILTER)
        item_title = self.driver.find_element(*SearchPageLocators.SEARCH_RESULT_ITEM_TITLE).text
        self.click_on(SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        self.click_on(ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_WATCHLIST)
        self.hover_over_click_chain(MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN,MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN_WATCHLIST)
        self.check_if_removed(item_title, MyAccountLocators.MY_ACCOUNT_USER_MOVIE_CARDS_FIRST_TITLE)

    def test_add_to_favorites(self):
        self.driver.get("https://www.themoviedb.org/")
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR, "uglies")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.click_on(SearchPageLocators.SEARCH_PAGE_MOVIE_FILTER)
        item_title = self.driver.find_element(*SearchPageLocators.SEARCH_RESULT_ITEM_TITLE).text
        self.click_on(SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        self.click_on(ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_FAVUORITE)
        self.driver.get("https://www.themoviedb.org/u/mbx-bx")
        self.hover_over_click_chain(MyAccountLocators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_DROPDOWN, MyAccountLocators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_DROPDOWN, MyAccountLocators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_MOVIES_DROPDOWN)
        self.check_if_added(item_title, MyAccountLocators.MY_ACCOUNT_USER_MOVIE_CARDS_FIRST_TITLE)

    def test_remove_from_favorites(self):
        self.driver.get("https://www.themoviedb.org/")
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR, "uglies")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.click_on(SearchPageLocators.SEARCH_PAGE_MOVIE_FILTER)
        item_title = self.driver.find_element(*SearchPageLocators.SEARCH_RESULT_ITEM_TITLE).text
        self.click_on(SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        self.click_on(ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_FAVUORITE)
        self.driver.get("https://www.themoviedb.org/u/mbx-bx")
        self.hover_over_click_chain(MyAccountLocators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_DROPDOWN,
                                    MyAccountLocators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_DROPDOWN,
                                    MyAccountLocators.MY_ACCOUNT_USER_SHORTCUTBAR_OVERVIEW_FAVOURITES_MOVIES_DROPDOWN)
        self.check_if_removed(item_title, MyAccountLocators.MY_ACCOUNT_USER_MOVIE_CARDS_FIRST_TITLE)



    def test_add_to_list(self):
        self.driver.get("https://www.themoviedb.org/")
        self.insert_text(HomePageLocators.HOME_PAGE_SEARCH_BAR, "the penguin")
        self.click_on(HomePageLocators.HOME_PAGE_SEARCH_BUTTON)
        self.click_on(SearchPageLocators.SEARCH_PAGE_MOVIE_FILTER)
        item_title = self.driver.find_element(*SearchPageLocators.SEARCH_RESULT_ITEM_TITLE).text
        self.click_on(SearchPageLocators.SEARCH_RESULT_ITEM_TITLE)
        self.hover_over_click_chain(ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_LIST_BUTTON,ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_EXISTING_LIST,ItemDetailsPage.ITEM_DETAILS_PAGE_ADD_TO_TEST_LIST)
        self.hover_over_click_chain(MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN,MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN_LISTS)
        self.click_on(MyAccountLocators.MY_ACCOUNT_USER_LISTS_TEST_LIST)
        self.check_if_added(item_title,MyAccountLocators.MY_ACCOUNT_USER_LISTS_FIRST_ITEM)

    def test_remove_from_list(self):
        pass



    def tearDown(self):
        self.driver.quit()