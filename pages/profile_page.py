import time

from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.extensions.keyboard import Keyboard
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from appium.webdriver.extensions.android.network import Network

from pages.base_page import BasePage


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.share_btn = '//android.widget.TextView[@content-desc="Share"]'
        self.edit_btn = '//android.widget.TextView[@content-desc="Edit profile"]'
        self.settings_btn = '//android.widget.TextView[@content-desc="Settings"]'
        self.username = '//android.widget.TextView[@resource-id="org.stepic.droid:id/profileName"]'

        # edit profile
        self.per_info = '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.stepic.droid:id/navigationRecycler"]/android.widget.LinearLayout[1]'
        self.password = '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.stepic.droid:id/navigationRecycler"]/android.widget.LinearLayout[3]'
        self.close_edit_profile_btn = '//android.widget.ImageButton[@content-desc="Navigate up"]'

        # per.info
        self.firstname = '//android.widget.EditText[@resource-id="org.stepic.droid:id/firstNameEditText"]'
        self.lastname = '//android.widget.EditText[@resource-id="org.stepic.droid:id/lastNameEditText"]'
        self.bio = '//android.widget.EditText[@resource-id="org.stepic.droid:id/shortBioEditText"]'
        self.about = '//android.widget.EditText[@resource-id="org.stepic.droid:id/detailsEditText"]'
        self.cancel_btn = '//android.widget.ImageButton[@content-desc="Navigate up"]'
        self.accept_btn = '//android.widget.TextView[@content-desc="Save"]'
        self.message_window = '//android.widget.TextView[@resource-id="org.stepic.droid:id/snackbar_text"]'
        self.message_text = 'Profile info changed'
        self.message_text_error = 'Cannot change info'

        # password
        self.cur_pass = '//android.widget.EditText[@resource-id="org.stepic.droid:id/currentPasswordEditText"]'
        self.new_pass = '//android.widget.EditText[@resource-id="org.stepic.droid:id/newPasswordEditText"]'

        # settings
        self.wifi_only_toggle = '//android.widget.Switch[@content-desc="Wi-Fi only download"]'
        self.downloads = '//android.widget.Switch[@content-desc="Wi-Fi only download"]'
        self.space_management = '//android.widget.TextView[@resource-id="org.stepic.droid:id/storageManagementButton"]'
        self.logout = '//android.widget.TextView[@resource-id="org.stepic.droid:id/logoutSettingsButton"]'
        self.logout_id = 'org.stepic.droid:id/logoutSettingsButton'
        self.confirm_logout_y = '//android.widget.Button[@resource-id="android:id/button1"]'
        self.confirm_logout_n = '//android.widget.Button[@resource-id="android:id/button2"]'

    def edit_profile_main(self, firstname, lastname):
        self.driver.find_element(By.XPATH, self.edit_btn).click()
        self.driver.find_element(By.XPATH, self.per_info).click()
        self.driver.find_element(By.XPATH, self.firstname).send_keys(firstname)
        self.driver.find_element(By.XPATH, self.lastname).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.accept_btn).click()

    def edit_profile_extra(self, bio, about):
        self.driver.find_element(By.XPATH, self.edit_btn).click()
        self.driver.find_element(By.XPATH, self.per_info).click()
        self.driver.find_element(By.XPATH, self.bio).send_keys(bio)
        self.driver.find_element(By.XPATH, self.about).send_keys(about)
        self.driver.find_element(By.XPATH, self.accept_btn).click()

    def is_profile_changed(self):
        return self.driver.find_element(By.XPATH, self.message_window).text == self.message_text

