from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username_id = "username"
    password_id = "password"
    login_btn_xpath = "//input[@value='Login']"
    login_error_msg_xpath = "//div[@id='loginError']"

    def enter_login_credentials(self, username, password):
        self.driver.find_element(By.ID, self.username_id).click()
        self.driver.find_element(By.ID, self.password_id).click()

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def retrieve_login_error_message(self):
        return self.driver.find_element(By.XPATH, self.login_error_msg_xpath).text
