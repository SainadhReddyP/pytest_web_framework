from selenium import webdriver
from utilities import ReadConfigurations
import pytest


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic_info", "browser")
    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list : chrome/firefox/edge")

    driver.maximize_window()
    url = ReadConfigurations.read_configuration("basic_info", "url")
    driver.get(url)
    request.cls.driver = driver # class level using the fixture
    yield
    driver.quit()
