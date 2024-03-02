from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.message_title = '//android.widget.TextView[@resource-id="org.stepic.droid:id/headerTitle"]'
        self.mes_later_btn = '//android.widget.Button[@resource-id="android:id/button2"]'
        self.mes_ok_btn = '//android.widget.Button[@resource-id="android:id/button1"]'
        self.notif_cancel_btn = '//android.widget.Button[@resource-id="android:id/button2"]'
        self.notif_ok_btn = '//android.widget.Button[@resource-id="android:id/button1"]'

    def ok_message(self):
        self.driver.find_element(By.XPATH, self.mes_ok_btn).click()

    def cancel_notif(self):
        self.driver.find_element(By.XPATH, self.notif_cancel_btn).click()

    def is_greetings(self):
        return self.driver.find_element(By.XPATH, self.message_title).text.strip() == 'Greetings!'