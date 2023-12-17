from selenium import webdriver
import pytest


@pytest.fixture()
def setup_and_teardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver = driver # class level using the fixture
    yield
    driver.quit()
