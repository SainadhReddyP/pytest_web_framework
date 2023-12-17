from selenium.webdriver.common.by import By
from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/login.html")
        self.driver.find_element(By.ID, "username").send_keys("sainadhreddy")
        self.driver.find_element(By.ID, "password").send_keys("automation100%")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_text = "Your login is successful."
        assert self.driver.find_element(By.XPATH, "//div[@id='loginSuccess']/p").text.__eq__(expected_text)
    
    def test_login_with_invalid_email_and_valid_password(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/login.html")
        self.driver.find_element(By.ID, "username").send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.ID, "password").send_keys("automation100%")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert self.driver.find_element(By.XPATH, "//div[@id='loginError']").text.__eq__(expected_message)
    
    def test_login_with_valid_email_and_invalid_password(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/login.html")
        self.driver.find_element(By.ID, "username").send_keys("sainadhreddy")
        self.driver.find_element(By.ID, "password").send_keys("automation")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert self.driver.find_element(By.XPATH, "//div[@id='loginError']").text.__eq__(expected_message)
    
    def test_login_without_entering_credentials(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/login.html")
        self.driver.find_element(By.ID, "username").send_keys(" ")
        self.driver.find_element(By.ID, "password").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_message = "Incorrect credentials. Please enter valid username and password."
        assert self.driver.find_element(By.XPATH, "//div[@id='loginError']").text.__eq__(expected_message)
    
    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "sainadh"+time_stamp+"@gmail.com"
