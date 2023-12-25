from pages.home_page import HomePage
from datetime import datetime
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self):
        home_pg = HomePage(self.driver)
        login_pg = home_pg.click_on_login_option()
        account_pg = login_pg.login_to_application("sainadhreddy", "automation100%")
        expected_text = "Your login is successful."
        assert account_pg.retrieve_successful_login_message().__eq__(expected_text)
    
    def test_login_with_invalid_email_and_valid_password(self):
        home_pg = HomePage(self.driver)
        login_pg= home_pg.click_on_login_option()
        login_pg.login_to_application(self.generate_email_with_timestamp(), "automation100%")
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert login_pg.retrieve_login_error_message().__eq__(expected_message)
    
    def test_login_with_valid_email_and_invalid_password(self):
        home_pg = HomePage(self.driver)
        login_pg= home_pg.click_on_login_option()
        login_pg.login_to_application("sainadhreddy", "automation")
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert login_pg.retrieve_login_error_message().__eq__(expected_message)
    
    def test_login_without_entering_credentials(self):
        home_pg = HomePage(self.driver)
        login_pg = home_pg.click_on_login_option()
        login_pg.login_to_application(" ", " ")
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert login_pg.retrieve_login_error_message().__eq__(expected_message)
    
