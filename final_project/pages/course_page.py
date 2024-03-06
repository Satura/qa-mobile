import time

import timer
from selenium.webdriver.common.by import By
from appium.webdriver.connectiontype import ConnectionType

from final_project.pages.base_page import BasePage


class CoursePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.join_btn = '//android.widget.Button[@resource-id="org.stepic.droid:id/courseEnrollAction"]'
        self.fav_btn = '//android.widget.TextView[@content-desc="Remove from Wishlist"]'
        self.info = '//android.widget.TextView[@text="Info"]'
        self.reviews = '//android.widget.TextView[@text="Reviews"]'
        self.news = '//android.widget.LinearLayout[@content-desc="News"]'
        self.modules = '//android.widget.LinearLayout[@content-desc="Modules"]'
        self.navigate_up_btn = '//android.widget.ImageButton[@content-desc="Navigate up"]'

        self.download_module_btn = '(//android.widget.ImageView[@resource-id="org.stepic.droid:id/statusNotCached"])[1]'
        self.download_settings_high_quality = '//android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="High"]'
        self.download_settings_ok = '//android.widget.Button[@resource-id="android:id/button1"]'
        self.error_notification = 'org.stepic.droid:id/snackbar_text'
        self.error_text = 'Mobile downloading is disabled. Turn on in settings'

        # урок с видео
        self.video_lesson = '(//android.widget.ImageView[@resource-id="org.stepic.droid:id/tabIconDrawable"])[3]'
        self.play_video = '//android.widget.ImageView[@resource-id="org.stepic.droid:id/videoPlayButton"]'
        self.panel = '//android.widget.FrameLayout[@resource-id="org.stepic.droid:id/exo_subtitles"]/android.view.View'
        self.minimize_video = '//android.widget.ImageView[@resource-id="org.stepic.droid:id/exo_pip_icon"]'
        self.video_miniplayer = ''

    def join_course(self):
        self.driver.find_element(By.XPATH, self.join_btn).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.navigate_up_btn).click()

    def add_to_fav(self):
        self.driver.find_element(By.XPATH, self.fav_btn).click()

    def download_with_mobile(self):
        self.driver.find_element(By.XPATH, self.modules).click()
        self.driver.find_element(By.XPATH, self.download_module_btn).click()
        self.driver.find_element(By.XPATH, self.download_settings_high_quality).click()
        self.driver.find_element(By.XPATH, self.download_settings_ok).click()

    def is_error_mobile(self):
        error = self.driver.find_element(By.ID, self.error_notification)
        return error.text == self.error_text

    def wifi_off_mobile_on(self):
        self.driver.set_network_connection(ConnectionType.DATA_ONLY)

    def wifi_on_mobile_on(self):
        self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)

    def airplane_on(self):
        self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)

    def wifi_off_mobile_on_2(self):
        self.driver.open_notification()
