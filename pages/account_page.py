from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    login_success_xpath = "//div[@id='loginSuccess']/p"

    def retrieve_successful_login_message(self):
        return self.driver.find_element(By.XPATH, self.login_success_xpath).text
