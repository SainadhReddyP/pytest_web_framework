from pages.home_page import HomePage
from tests.base_test import BaseTest


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_pg = HomePage(self.driver)
        register_pg = home_pg.click_on_register_button()
        account_success_pg = register_pg.register_account("Sainadh", "Reddy", "Male", "sainadhreddy_1@gmail.com",
                                                          "Python@123", "1234567890")
        expected_msg = "Your account has been created successfully."
        assert account_success_pg.retrieve_account_creation_message().__contains__(expected_msg)

    def test_register_with_all_fields(self):
        home_pg = HomePage(self.driver)
        register_pg = home_pg.click_on_register_button()
        account_success_pg = register_pg.register_account("Sainadh", "Reddy", "Male", "sainadhreddy_1@gmail.com",
                                                          "Python@123", "1234567890", "Hyderabad")
        expected_msg = "Your account has been created successfully."
        assert account_success_pg.retrieve_account_creation_message().__contains__(expected_msg)

    def test_register_with_duplicate_email(self):
        home_pg = HomePage(self.driver)
        register_pg = home_pg.click_on_register_button()
        register_pg.register_account("Sainadh", "Reddy", "Male", "sainadhreddy@gmail.com",
                                                          "Python@123", "1234567890", "Hyderabad")
        expected_msg = "Duplicate email address. Please choose a different email."
        assert register_pg.retrieve_duplicate_email_message().__contains__(expected_msg)

    def test_register_with_invalid_phone_number(self):
        home_pg = HomePage(self.driver)
        register_pg = home_pg.click_on_register_button()
        register_pg.register_account("Sainadh", "Reddy", "Male", "sainadhreddy_1@gmail.com",
                                                          "Python@123", "12345")
        expected_msg = "Please enter a valid 10-digit phone number."
        assert register_pg.retrieve_invalid_phone_number().__eq__(expected_msg)
    
    
