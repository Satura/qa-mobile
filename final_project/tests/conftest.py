import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from final_project.capabilities import get_capabilities


@pytest.fixture()
def driver():
    host = "http://localhost:4723/wd/hub"
    options = UiAutomator2Options().load_capabilities((get_capabilities()))
    driver = webdriver.Remote(host, options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()
