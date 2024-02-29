from appium import webdriver


def initialize_appium_driver():
    return {
        "platformName": "Android",
        "platformVersion": "14.0",
        "deviceName": "Pixel_3a_API_34_extension_level_7_x86_64",
        # "app": ".\app\stepik.apk",
        "app": "d:\\MathsHub_AQA\\06_qa-mobile\\qa-mobile\\app\\stepik.apk",
        "autoGrantPermissions": "true"
    }
