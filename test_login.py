import time
from unittest import TestCase
from base_data import Base_Data
from locators import HomePageLocators, LoginPageLocators, MyAccountLocators

class Test_Login(Base_Data,TestCase):

    def setUp(self):
        self.driver = self.setup_actions()



    def test_login_invalid_username(self):
        self.insert_login_actions('testname_','12345')
        self.check_error_message("We couldn't find your username.", LoginPageLocators.LOGIN_ERRORS)

    def test_login_valid_credentials(self):
        self.insert_login_actions("mbx-bx","4231")
        self.check_if_logged_in(), f'User icon not found on nav bar, user not logged in'

    def test_logout(self):
        self.insert_login_actions(username="mbx-bx",password="4231")
        self.hover_over_click_chain(MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN, MyAccountLocators.MY_ACCOUNT_USER_NAV_DROPDOWN_LOGOUT)
        self.check_if_logged_out()


    def test_login_blank_password(self):
        self.insert_login_actions("mbx-bx","N/A")
        self.check_error_message("We couldn't validate your information. Want to try again?", LoginPageLocators.LOGIN_ERRORS)





    def tearDown(self):
        self.driver.quit()