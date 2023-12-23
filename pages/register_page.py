from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.account_success_page import AccountSuccessPage


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
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
        self.driver.find_element(By.ID, self.firstname_id).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(By.ID, self.lastname_id).send_keys(lastname)

    def select_gender(self, gender):
        gender_dropdown = self.driver.find_element(By.ID, self.gender_id)
        select_gender = Select(gender_dropdown)
        select_gender.select_by_visible_text(gender)

    def enter_email_address(self, email_address):
        self.driver.find_element(By.NAME, self.email_name).send_keys(email_address)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_name).send_keys(password)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.NAME, self.phone_number_name).send_keys(phone_number)

    def clicks_on_privacy_policy(self):
        self.driver.find_element(By.ID, self.terms_checkbox_id).click()

    def clicks_on_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_btn_xpath).click()
        return AccountSuccessPage(self.driver)

    def enter_address(self, location):
        self.driver.find_element(By.NAME, self.address_name).send_keys(location)

    def retrieve_duplicate_email_message(self):
        return self.driver.find_element(By.XPATH, self.email_error_xpath).text

    def retrieve_invalid_phone_number(self):
        return self.driver.find_element(By.XPATH, self.phone_number_error_msg_xpath).text

