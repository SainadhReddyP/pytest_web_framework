from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/register-account.html")
        self.driver.find_element(By.ID, "firstName").send_keys("Sainadh")
        self.driver.find_element(By.ID, "lastName").send_keys("Reddy")
        gender = self.driver.find_element(By.ID, "gender")
        select_gender = Select(gender)
        select_gender.select_by_visible_text("Male")
        self.driver.find_element(By.NAME, "email").send_keys("sainadhreddy_1@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Python@123")
        self.driver.find_element(By.NAME, "phoneNumber").send_keys("1234567890")
        self.driver.find_element(By.ID, "termsCheckbox").click()
        self.driver.find_element(By.XPATH, "//input[@value='Submit']").click()
        expected_msg = "Your account has been created successfully."
        wait = WebDriverWait(self.driver, 10)
        assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='account-creation']")))\
            .text.__contains__(expected_msg)

    def test_register_with_all_fields(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/register-account.html")
        self.driver.find_element(By.ID, "firstName").send_keys("Sainadh")
        self.driver.find_element(By.ID, "lastName").send_keys("Reddy")
        gender = self.driver.find_element(By.ID, "gender")
        select_gender = Select(gender)
        select_gender.select_by_visible_text("Male")
        self.driver.find_element(By.NAME, "email").send_keys("sainadhreddy_1@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Python@123")
        self.driver.find_element(By.NAME, "phoneNumber").send_keys("1234567890")
        self.driver.find_element(By.NAME, "address").send_keys("Hyderabad")
        self.driver.find_element(By.ID, "termsCheckbox").click()
        self.driver.find_element(By.XPATH, "//input[@value='Submit']").click()
        expected_msg = "Your account has been created successfully."
        wait = WebDriverWait(self.driver, 10)
        assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='account-creation']")))\
            .text.__contains__(expected_msg)

    def test_register_with_duplicate_email(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/register-account.html")
        self.driver.find_element(By.ID, "firstName").send_keys("Sainadh")
        self.driver.find_element(By.ID, "lastName").send_keys("Reddy")
        gender = self.driver.find_element(By.ID, "gender")
        select_gender = Select(gender)
        select_gender.select_by_visible_text("Male")
        self.driver.find_element(By.NAME, "email").send_keys("sainadhreddy@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("Python@123")
        self.driver.find_element(By.NAME, "phoneNumber").send_keys("1234567890")
        self.driver.find_element(By.NAME, "address").send_keys("Hyderabad")
        self.driver.find_element(By.ID, "termsCheckbox").click()
        self.driver.find_element(By.XPATH, "//input[@value='Submit']").click()
        expected_msg = "Duplicate email address. Please choose a different email."
        assert self.driver.find_element(By.XPATH, "//div[@id='emailError']") \
            .text.__contains__(expected_msg)

    def test_register_with_invalid_phone_number(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/register-account.html")
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
    
    
