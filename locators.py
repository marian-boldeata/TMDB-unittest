from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_PAGE_LOGIN_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Login')
    NAV_BAR_USER_ICON = (By.XPATH, '//a[@aria-label="Profile and Settings"]')
    ACCEPT_COOKIES_BUTTON = (By.ID, "onetrust-accept-btn-handler")
    HOME_PAGE_SEARCH_BUTTON = (By.XPATH, '//input[@value="Search"]')
    HOME_PAGE_SEARCH_BAR = (By.ID, 'inner_search_v4')

    HOME_PAGE_TRANSLATE_BUTTON = (By.CLASS_NAME, 'translate')
    HOME_PAGE_DEFAULT_LANGUAGE_DROP = (By.XPATH, '//label[@for="default_language_popup"]/span[2]')
    HOME_PAGE_DEFAULT_LANGUAGE_FIELD = (By.XPATH, '//div[@id="default_language_popup-list"]//input')
    HOME_PAGE_LANGUAGE_RELOAD_BUTTON = (By.XPATH, '//a[@class="no_click button rounded upcase"]')
    HOME_PAGE_BANNER_TITLE = (By.XPATH, '//div[@class="title"]/h2')

class SearchPageLocators:
    SEARCH_PAGE_NO_SEARCH_RESULTS = (By.XPATH, '//div[@class="search_results movie "]/div/p')
    SEARCH_RESULT_ITEM_TITLE = (By.XPATH, '//div[@class="content_wrapper"]//div[@class="title"]//a[@class="result"]/h2')
    SEARCH_PAGE_MOVIE_FILTER = (By.ID, 'movie')
    SEARCH_PAGE_PEOPLE_FILTER = (By.ID, 'person')
    SEARCH_PAGE_TV_SHOWS_FILTER = (By.ID, 'tv')
    SEARCH_PAGE_COLLECTIONS_FILTER = (By.ID, 'collection')
    SEARCH_PAGE_ITEM_DATA_TYPE = (By.XPATH, '//a[@data-media-type]')



class LoginPageLocators:
    LOGIN_PAGE_USERNAME_FIELD = (By.ID, "username")
    LOGIN_PAGE_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_PAGE_SUBMIT_LOGIN_BUTTON = (By.ID, "login_button")
    LOGIN_ERRORS = (By.XPATH,'//div[@class="carton"]/div/ul/li[1]')