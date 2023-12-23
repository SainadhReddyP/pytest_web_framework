from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.account_success_page import AccountSuccessPage
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_register_button()
        register_pg = RegisterPage(self.driver)
        register_pg.enter_first_name("Sainadh")
        register_pg.enter_last_name("Reddy")
        register_pg.select_gender("Male")
        register_pg.enter_email_address("sainadhreddy_1@gmail.com")
        register_pg.enter_password("Python@123")
        register_pg.enter_phone_number("1234567890")
        register_pg.clicks_on_privacy_policy()
        register_pg.clicks_on_submit_button()
        expected_msg = "Your account has been created successfully."
        account_success_pg = AccountSuccessPage(self.driver)
        assert account_success_pg.retrieve_account_creation_message().__contains__(expected_msg)

    def test_register_with_all_fields(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_register_button()
        register_pg = RegisterPage(self.driver)
        register_pg.enter_first_name("Sainadh")
        register_pg.enter_last_name("Reddy")
        register_pg.select_gender("Male")
        register_pg.enter_email_address("sainadhreddy_1@gmail.com")
        register_pg.enter_password("Python@123")
        register_pg.enter_phone_number("1234567890")
        register_pg.enter_address("Hyderabad")
        register_pg.clicks_on_privacy_policy()
        register_pg.clicks_on_submit_button()
        expected_msg = "Your account has been created successfully."
        account_success_pg = AccountSuccessPage(self.driver)
        assert account_success_pg.retrieve_account_creation_message().__contains__(expected_msg)

    def test_register_with_duplicate_email(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_register_button()
        register_pg = RegisterPage(self.driver)
        register_pg.enter_first_name("Sainadh")
        register_pg.enter_last_name("Reddy")
        register_pg.select_gender("Male")
        register_pg.enter_email_address("sainadhreddy@gmail.com")
        register_pg.enter_password("Python@123")
        register_pg.enter_phone_number("1234567890")
        register_pg.enter_address("Hyderabad")
        register_pg.clicks_on_privacy_policy()
        register_pg.clicks_on_submit_button()
        expected_msg = "Duplicate email address. Please choose a different email."
        assert register_pg.retrieve_duplicate_email_message().__contains__(expected_msg)

    def test_register_with_invalid_phone_number(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_register_button()
        register_pg = RegisterPage(self.driver)
        register_pg.enter_first_name("Sainadh")
        register_pg.enter_last_name("Reddy")
        register_pg.select_gender("Male")
        register_pg.enter_email_address("sainadhreddy_2@gmail.com")
        register_pg.enter_password("Python@123")
        register_pg.enter_phone_number("12345")
        register_pg.clicks_on_privacy_policy()
        register_pg.clicks_on_submit_button()
        expected_msg = "Please enter a valid 10-digit phone number."
        assert register_pg.retrieve_invalid_phone_number().__eq__(expected_msg)
    
    
