from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def set_text(self, locator_name, locator, send_text):
        element = self.get_element(locator_name, locator)
        element.click()
        element.clear()
        element.send_keys(send_text)

    def click_element(self, locator_name, locator):
        element = self.get_element(locator_name, locator)
        element.click()

    def get_element(self, locator_name, locator):
        element = None
        if locator_name.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator)
        elif locator_name.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator)
        elif locator_name.__contains__("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator)
        elif locator_name.__contains__("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator)
        elif locator_name.__contains__("_xpath"):
            element = self.driver.find_element(By.XPATH, locator)
        elif locator_name.__contains__("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
        return element

    def check_display_status_of_element(self, locator_name, locator):
        element = self.get_element(locator_name, locator)
        return element.is_displayed()

    def get_text(self, locator_name, locator):
        element = self.get_element(locator_name, locator)
        return element.text