from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/login.html")
    driver.find_element(By.ID, "username").send_keys("sainadhreddy")
    driver.find_element(By.ID, "password").send_keys("automation100%")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_text = "Your login is successful."
    assert driver.find_element(By.XPATH, "//div[@id='loginSuccess']/p").text.__eq__(expected_text)
    driver.quit()


def test_login_with_invalid_email_and_valid_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/login.html")
    driver.find_element(By.ID, "username").send_keys(generate_email_with_timestamp())
    driver.find_element(By.ID, "password").send_keys("automation100%")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_message = "Incorrect credentials. Please enter valid username and password."
    assert driver.find_element(By.XPATH, "//div[@id='loginError']").text.__eq__(expected_message)
    driver.quit()


def test_login_with_valid_email_and_invalid_password():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/login.html")
    driver.find_element(By.ID, "username").send_keys("sainadhreddy")
    driver.find_element(By.ID, "password").send_keys("automation")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_message = "Incorrect credentials. Please enter valid username and password."
    assert driver.find_element(By.XPATH, "//div[@id='loginError']").text.__eq__(expected_message)
    driver.quit()


def test_login_without_entering_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/login.html")
    driver.find_element(By.ID, "username").send_keys(" ")
    driver.find_element(By.ID, "password").send_keys(" ")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_message = "Incorrect credentials. Please enter valid username and password."
    assert driver.find_element(By.XPATH, "//div[@id='loginError']").text.__eq__(expected_message)
    driver.quit()


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "sainadh"+time_stamp+"@gmail.com"