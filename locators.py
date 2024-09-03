from selenium.webdriver.common.by import By


class HomePageLocators:
    HOME_PAGE_LOGIN_BUTTON_NAV_BAR = (By.LINK_TEXT, 'Login')
    NAV_BAR_USER_ICON = (By.XPATH, '//a[@aria-label="Profile and Settings"]')



class LoginPageLocators:
    LOGIN_PAGE_USERNAME_FIELD = (By.ID, "username")
    LOGIN_PAGE_PASSWORD_FIELD = (By.ID, "password")
    LOGIN_PAGE_SUBMIT_LOGIN_BUTTON = (By.ID, "login_button")