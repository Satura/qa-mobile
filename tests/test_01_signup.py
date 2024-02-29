from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

from utils.appium_utils import initialize_appium_driver

host = "http://localhost:4723/wd/hub"
options = UiAutomator2Options().load_capabilities((initialize_appium_driver()))
driver = webdriver.Remote(host, options=options)


def test_close_onboarding():
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="Close"]').click()
    assert driver.find_element(By.XPATH,
                               '//android.widget.Button[@resource-id="org.stepic.droid:id/launchSignUpButton"]').is_displayed()


def test_signup():
    driver.find_element(By.XPATH,
                        '//android.widget.Button[@resource-id="org.stepic.droid:id/launchSignUpButton"]').click()
    driver.find_element(By.XPATH,
                        '//android.widget.EditText[@resource-id="org.stepic.droid:id/firstNameField"]').send_keys(
        'TestUser')
    driver.find_element(By.XPATH, '//android.widget.EditText[@resource-id="org.stepic.droid:id/emailField"]').send_keys(
        'testmail@mail.com')
    driver.find_element(By.XPATH,
                        '//android.widget.EditText[@resource-id="org.stepic.droid:id/passwordField"]').send_keys(
        'testpass')
    driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="org.stepic.droid:id/signUpButton"]').click()
    driver.implicitly_wait(15)
    assert driver.find_element(By.XPATH,
                               '//android.widget.TextView[@resource-id="org.stepic.droid:id/headerTitle"]').text.strip() == 'Greetings!'
    driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]').click()
    driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="android:id/button2"]').click()
