from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def set_text(self, locator, send_text):
        element = self.get_element(locator)
        element.click()
        element.clear()
        element.send_keys(send_text)

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def get_element(self, locator):
        element = None
        if locator.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator)
        elif locator.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator)
        elif locator.__contains__("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator)
        elif locator.__contains__("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator)
        elif locator.__contains__("_xpath"):
            element = self.driver.find_element(By.XPATH, locator)
        elif locator.__contains__("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
        return element