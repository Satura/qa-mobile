import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from utils.appium_utils import initialize_appium_driver


@pytest.fixture()
def driver():
    host = "http://localhost:4723/wd/hub"
    options = UiAutomator2Options().load_capabilities((initialize_appium_driver()))
    driver = webdriver.Remote(host, options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
