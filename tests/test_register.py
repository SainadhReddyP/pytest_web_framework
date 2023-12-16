from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_register_with_mandatory_fields():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/register-account.html")
    driver.find_element(By.ID, "firstName").send_keys("Sainadh")
    driver.find_element(By.ID, "lastName").send_keys("Reddy")
    gender = driver.find_element(By.ID, "gender")
    select_gender = Select(gender)
    select_gender.select_by_visible_text("Male")
    driver.find_element(By.NAME, "email").send_keys("sainadhreddy_1@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Python@123")
    driver.find_element(By.NAME, "phoneNumber").send_keys("1234567890")
    driver.find_element(By.ID, "termsCheckbox").click()
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    expected_msg = "Your account has been created successfully."
    wait = WebDriverWait(driver, 10)
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='account-creation']")))\
        .text.__contains__(expected_msg)


def test_register_with_all_fields():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/register-account.html")
    driver.find_element(By.ID, "firstName").send_keys("Sainadh")
    driver.find_element(By.ID, "lastName").send_keys("Reddy")
    gender = driver.find_element(By.ID, "gender")
    select_gender = Select(gender)
    select_gender.select_by_visible_text("Male")
    driver.find_element(By.NAME, "email").send_keys("sainadhreddy_1@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Python@123")
    driver.find_element(By.NAME, "phoneNumber").send_keys("1234567890")
    driver.find_element(By.NAME, "address").send_keys("Hyderabad")
    driver.find_element(By.ID, "termsCheckbox").click()
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    expected_msg = "Your account has been created successfully."
    wait = WebDriverWait(driver, 10)
    assert wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='account-creation']")))\
        .text.__contains__(expected_msg)


def test_register_with_duplicate_email():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/register-account.html")
    driver.find_element(By.ID, "firstName").send_keys("Sainadh")
    driver.find_element(By.ID, "lastName").send_keys("Reddy")
    gender = driver.find_element(By.ID, "gender")
    select_gender = Select(gender)
    select_gender.select_by_visible_text("Male")
    driver.find_element(By.NAME, "email").send_keys("sainadhreddy@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Python@123")
    driver.find_element(By.NAME, "phoneNumber").send_keys("1234567890")
    driver.find_element(By.NAME, "address").send_keys("Hyderabad")
    driver.find_element(By.ID, "termsCheckbox").click()
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    expected_msg = "Duplicate email address. Please choose a different email."
    assert driver.find_element(By.XPATH, "//div[@id='emailError']") \
        .text.__contains__(expected_msg)


def test_register_with_invalid_phone_number():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sdetportal.blogspot.com/p/register-account.html")
    driver.find_element(By.ID, "firstName").send_keys("Sainadh")
    driver.find_element(By.ID, "lastName").send_keys("Reddy")
    gender = driver.find_element(By.ID, "gender")
    select_gender = Select(gender)
    select_gender.select_by_visible_text("Male")
    driver.find_element(By.NAME, "email").send_keys("sainadhreddy_2@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Python@123")
    driver.find_element(By.NAME, "phoneNumber").send_keys("12345")
    driver.find_element(By.ID, "termsCheckbox").click()
    driver.find_element(By.XPATH, "//input[@value='Submit']").click()
    expected_msg = "Please enter a valid 10-digit phone number."
    assert driver.find_element(By.XPATH, "//div[@id='phoneNumberError']") \
        .text.__eq__(expected_msg)


