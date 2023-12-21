from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        self.driver.find_element(By.ID, "firstName").send_keys("Sainadh")
        self.driver.find_element(By.ID, "lastName").send_keys("Reddy")
        gender = self.driver.find_element(By.ID, "gender")
        select_gender = Select(gender)
        select_gender.select_by_visible_text("Male")
        self.driver.find_element(By.NAME, "email").send_keys("sainadhreddy_2@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Python@123")
        self.driver.find_element(By.NAME, "phoneNumber").send_keys("12345")
        self.driver.find_element(By.ID, "termsCheckbox").click()
        self.driver.find_element(By.XPATH, "//input[@value='Submit']").click()
        expected_msg = "Please enter a valid 10-digit phone number."
        assert self.driver.find_element(By.XPATH, "//div[@id='phoneNumberError']") \
            .text.__eq__(expected_msg)
    
    
