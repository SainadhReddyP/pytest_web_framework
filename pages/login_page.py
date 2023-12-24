from selenium.webdriver.common.by import By
from pages.account_page import AccountPage
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)

    # Locators
    username_id = "username"
    password_id = "password"
    login_btn_xpath = "//input[@value='Login']"
    login_error_msg_xpath = "//div[@id='loginError']"

    def enter_login_credentials(self, username, password):
        self.set_text("username_id", self.username_id, username)
        self.set_text("password_id", self.password_id, password)

    def click_on_login_button(self):
        self.click_element("login_btn_xpath", self.login_btn_xpath)
        return AccountPage(self.driver)

    def retrieve_login_error_message(self):
        return self.get_text("login_error_msg_xpath", self.login_error_msg_xpath)

    def login_to_application(self, username, password):
        self.enter_login_credentials(username, password)
        return self.click_on_login_button()
