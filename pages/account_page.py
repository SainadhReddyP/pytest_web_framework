from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)

    # Locators
    login_success_xpath = "//div[@id='loginSuccess']/p"

    def retrieve_successful_login_message(self):
        return self.get_text(self.login_success_xpath)
