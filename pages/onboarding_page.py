from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OnboardingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.close_btn = '//android.widget.ImageView[@content-desc="Close"]'

    def close_onboarding(self):
        self.driver.find_element(By.XPATH, self.close_btn).click()

