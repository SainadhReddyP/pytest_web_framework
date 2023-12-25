from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities import excel_utils
import pytest


class TestLogin(BaseTest):

    @pytest.mark.parametrize("username, password", excel_utils.get_data_from_excel("testdata/sdetqa_portal.xlsx","Login"))
    def test_login_with_valid_credentials(self, username, password):
        home_pg = HomePage(self.driver)
        login_pg = home_pg.click_on_login_option()
        account_pg = login_pg.login_to_application(username, password)
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
    
