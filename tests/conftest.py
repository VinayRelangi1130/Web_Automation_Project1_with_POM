import pytest
from selenium import webdriver

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations('basic info', 'browser')
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Provided browser is not supported")
    driver.maximize_window()
    app_url=ReadConfigurations.read_configurations('basic info', 'url')
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
