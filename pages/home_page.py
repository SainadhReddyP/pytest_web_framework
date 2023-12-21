from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    your_store_btn_xpath = "//button[text()='Your Store']"
    search_box_xpath = "//input[@id='searchQuery']"
    search_btn_xpath = "//button[text()='Search']"
    login_btn_xpath = "//button[text()='Login']"

    def click_on_store_button(self):
        self.driver.find_element(By.XPATH, self.your_store_btn_xpath).click()

    def enter_product_into_search_box(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box_xpath).click()
        self.driver.find_element(By.XPATH, self.search_box_xpath).clear()
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()