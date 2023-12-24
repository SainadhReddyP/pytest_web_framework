from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    account_creation_msg_xpath = "//div[@class='account-creation']"

    def retrieve_account_creation_message(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.account_creation_msg_xpath))).text
