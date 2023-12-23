from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_pg = HomePage(self.driver)
        login_pg = home_pg.click_on_login_button()
        login_pg.enter_login_credentials("sainadhreddy", "automation100%")
        account_pg = login_pg.click_on_login_button()
        expected_text = "Your login is successful."
        assert account_pg.retrieve_successful_login_message().__eq__(expected_text)
    
    def test_login_with_invalid_email_and_valid_password(self):
        home_pg = HomePage(self.driver)
        login_pg= home_pg.click_on_login_button()
        login_pg.enter_login_credentials(self.generate_email_with_timestamp(), "automation100%")
        login_pg.click_on_login_button()
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert login_pg.retrieve_login_error_message().__eq__(expected_message)
    
    def test_login_with_valid_email_and_invalid_password(self):
        home_pg = HomePage(self.driver)
        login_pg= home_pg.click_on_login_button()
        login_pg.enter_login_credentials("sainadhreddy", "automation")
        login_pg.click_on_login_button()
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert login_pg.retrieve_login_error_message().__eq__(expected_message)
    
    def test_login_without_entering_credentials(self):
        home_pg = HomePage(self.driver)
        login_pg = home_pg.click_on_login_button()
        login_pg.enter_login_credentials(" ", " ")
        login_pg.click_on_login_button()
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert login_pg.retrieve_login_error_message().__eq__(expected_message)
    
    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "sainadh"+time_stamp+"@gmail.com"
