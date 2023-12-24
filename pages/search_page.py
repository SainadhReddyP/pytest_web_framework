from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)

    # Locators
    galaxy_product_xpath = "//h3[text()='Galaxy S22']"
    invalid_product_msg_xpath = "//div[@id='resultsContainer']/p"

    def display_status_of_valid_product(self):
        return self.check_display_status_of_element("galaxy_product_xpath", self.galaxy_product_xpath)

    def retrieve_invalid_product_message(self):
        return self.get_text("invalid_product_msg_xpath", self.invalid_product_msg_xpath)
