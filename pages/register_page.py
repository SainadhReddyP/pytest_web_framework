from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.account_success_page import AccountSuccessPage
from pages.base_page import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)

    # Locators
    firstname_id = "firstName"
    lastname_id = "lastName"
    gender_id = "gender"
    email_name = "email"
    password_name = "password"
    phone_number_name = "phoneNumber"
    terms_checkbox_id = "termsCheckbox"
    submit_btn_xpath = "//input[@value='Submit']"
    address_name = "address"
    email_error_xpath = "//div[@id='emailError']"
    phone_number_error_msg_xpath = "//div[@id='phoneNumberError']"

    def enter_first_name(self, firstname):
        self.set_text(self.firstname_id, firstname)

    def enter_last_name(self, lastname):
        self.set_text(self.lastname_id, lastname)

    def select_gender(self, gender):
        gender_dropdown = self.driver.find_element(By.ID, self.gender_id)
        select_gender = Select(gender_dropdown)
        select_gender.select_by_visible_text(gender)

    def enter_email_address(self, email_address):
        self.set_text(self.email_name, email_address)

    def enter_password(self, password):
        self.set_text(self.password_name, password)

    def enter_phone_number(self, phone_number):
        self.set_text(self.phone_number_name, phone_number)

    def clicks_on_privacy_policy(self):
        self.click_element(self.terms_checkbox_id)

    def clicks_on_submit_button(self):
        self.click_element(self.submit_btn_xpath)
        return AccountSuccessPage(self.driver)

    def enter_address(self, location):
        self.driver.find_element(By.NAME, self.address_name).send_keys(location)

    def retrieve_duplicate_email_message(self):
        return self.get_text(self.email_error_xpath)

    def retrieve_invalid_phone_number(self):
        return self.get_text(self.phone_number_error_msg_xpath)

    def register_account(self, first_name, last_name, gender, email_address, password, phone_number, address=None):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.select_gender(gender)
        self.enter_email_address(email_address)
        self.enter_password(password)
        self.enter_phone_number(phone_number)
        if address:
            self.enter_address(address)
        self.clicks_on_privacy_policy()
        self.clicks_on_submit_button()
        return AccountSuccessPage(self.driver)