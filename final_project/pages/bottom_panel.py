from selenium.webdriver.common.by import By

from final_project.pages.base_page import BasePage


class BottomPanel(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.home = '//android.widget.FrameLayout[@content-desc="Home"]'
        self.catalog = '//android.widget.FrameLayout[@content-desc="Catalog"]'
        self.profile = '//android.widget.FrameLayout[@content-desc="Profile"]'
        self.notification = '//android.widget.FrameLayout[@content-desc="Notifications"]'

    def go_to_home(self):
        self.driver.find_element(By.XPATH, self.home).click()

    def go_to_catalog(self):
        self.driver.find_element(By.XPATH, self.catalog).click()

    def go_to_profile(self):
        self.driver.find_element(By.XPATH, self.profile).click()

    def go_to_notification(self):
        self.driver.find_element(By.XPATH, self.notification).click()
