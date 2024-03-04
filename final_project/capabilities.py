from appium import webdriver


def get_capabilities():
    return {
        "platformName": "Android",
        "platformVersion": "14.0",
        "deviceName": "Pixel_3a_API_34_extension_level_7_x86_64",
        # "app": ".\app\stepik.apk",
        "app": "d:\\MathsHub_AQA\\06_qa-mobile\\qa-mobile\\final_project\\app\\stepik.apk",
        "autoGrantPermissions": "true"
    }
