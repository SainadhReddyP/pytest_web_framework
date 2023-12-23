from selenium.webdriver.common.by import By
from pages.account_page import AccountPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    # Locators
    username_id = "username"
    password_id = "password"
    login_btn_xpath = "//input[@value='Login']"
    login_error_msg_xpath = "//div[@id='loginError']"

    def enter_login_credentials(self, username, password):
        self.driver.find_element(By.ID, self.username_id).send_keys(username)
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
        return AccountPage(self.driver)

    def retrieve_login_error_message(self):
        return self.driver.find_element(By.XPATH, self.login_error_msg_xpath).text

    def login_to_application(self, username, password):
        self.enter_login_credentials(username, password)
        return self.click_on_login_button()
