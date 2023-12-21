from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    galaxy_product_xpath = "//h3[text()='Galaxy S22']"
    invalid_product_msg_xpath = "//div[@id='resultsContainer']/p"

    def display_status_of_valid_product(self):
        return self.driver.find_element(By.XPATH, self.galaxy_product_xpath).is_displayed()

    def retrieve_invalid_product_message(self):
        return self.driver.find_element(By.XPATH, self.invalid_product_msg_xpath).text
