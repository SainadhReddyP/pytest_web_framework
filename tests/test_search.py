from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_for_a_valid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/your-store.html")
    driver.find_element(By.NAME, "searchQuery").send_keys("Galaxy S22")
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    assert driver.find_element(By.XPATH, "//h3[text()='Galaxy S22']").is_displayed()
    driver.quit()


def test_search_for_an_invalid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/your-store.html")
    driver.find_element(By.NAME, "searchQuery").send_keys("Galaxy S23")
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//div[@id='resultsContainer']/p").text.__eq__(expected_text)
    driver.quit()


def test_search_without_entering_any_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/your-store.html")
    driver.find_element(By.NAME, "searchQuery").send_keys(" ")
    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//div[@id='resultsContainer']/p").text.__eq__(expected_text)
    driver.quit()
