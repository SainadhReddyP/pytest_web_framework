from selenium.webdriver.common.by import By
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/your-store.html")
        self.driver.find_element(By.XPATH, "//input[@id='searchQuery']").send_keys("Galaxy S22")
        self.driver.find_element(By.XPATH, "//button[text()='Search']").click()
        assert self.driver.find_element(By.XPATH, "//h3[text()='Galaxy S22']").is_displayed()
        
    def test_search_for_an_invalid_product(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/your-store.html")
        self.driver.find_element(By.XPATH, "//input[@id='searchQuery']").send_keys("Galaxy S23")
        self.driver.find_element(By.XPATH, "//button[text()='Search']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//div[@id='resultsContainer']/p").text.__eq__(expected_text)
    
    def test_search_without_entering_any_product(self):
        self.driver.get("https://sdetqaportal.blogspot.com/p/your-store.html")
        self.driver.find_element(By.XPATH, "//input[@id='searchQuery']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//button[text()='Search']").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//div[@id='resultsContainer']/p").text.__eq__(expected_text)
