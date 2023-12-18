from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    search_box_xpath = "//input[@id='searchQuery']"

    def enter_product_into_search_box(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(product_name)
