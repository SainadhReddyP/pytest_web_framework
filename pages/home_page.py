from selenium.webdriver.common.by import By
from pages.search_page import SearchPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)

    # Locators
    your_store_btn_xpath = "//button[text()='Your Store']"
    search_box_xpath = "//input[@id='searchQuery']"
    search_btn_xpath = "//button[text()='Search']"
    login_btn_xpath = "//button[text()='Login']"
    register_btn_xpath = "//button[text()='Register']"

    def click_on_store_button(self):
        self.click_element("your_store_btn_xpath", self.your_store_btn_xpath)

    def enter_product_into_search_box(self, product_name):
        self.set_text("search_box_xpath", self.search_box_xpath, product_name)

    def click_on_search_button(self):
        self.click_element("search_btn_xpath", self.search_btn_xpath)
        return SearchPage(self.driver)

    def click_on_login_option(self):
        self.click_element("login_btn_xpath", self.login_btn_xpath)
        return LoginPage(self.driver)

    def click_on_register_button(self):
        self.click_element("register_btn_xpath", self.register_btn_xpath)
        return RegisterPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box(product_name)
        self.click_on_search_button()
        return SearchPage(self.driver)
