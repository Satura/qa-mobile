from selenium.webdriver.common.by import By

from final_project.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.signup_link = '//android.widget.Button[@resource-id="org.stepic.droid:id/launchSignUpButton"]'
        self.signin_with_email_link = '//android.widget.Button[@resource-id="org.stepic.droid:id/signInWithEmail"]'
        self.close_lp_btn = '//android.widget.ImageView[@resource-id="org.stepic.droid:id/dismissButton"]'

        # signup form
        self.username_field = '//android.widget.EditText[@resource-id="org.stepic.droid:id/firstNameField"]'
        self.email_field = '//android.widget.EditText[@resource-id="org.stepic.droid:id/emailField"]'
        self.pass_field = '//android.widget.EditText[@resource-id="org.stepic.droid:id/passwordField"]'
        self.signup_btn = '//android.widget.Button[@resource-id="org.stepic.droid:id/signUpButton"]'

        # signin with email form
        self.login_field = '//android.widget.EditText[@resource-id="org.stepic.droid:id/loginField"]'
        self.password_field = '//android.widget.EditText[@resource-id="org.stepic.droid:id/passwordField"]'
        self.signin_btn = '//android.widget.Button[@resource-id="org.stepic.droid:id/loginButton"]'

    def registry_new_user(self, name, email, password):
        self.driver.find_element(By.XPATH, self.signup_link).click()
        self.driver.find_element(By.XPATH, self.username_field).send_keys(name)
        self.driver.find_element(By.XPATH, self.email_field).send_keys(email)
        self.driver.find_element(By.XPATH, self.pass_field).send_keys(password)
        self.driver.find_element(By.XPATH, self.signup_btn).click()

    def login_with_email(self, email, password):
        self.driver.find_element(By.XPATH, self.signin_with_email_link).click()
        self.driver.find_element(By.XPATH, self.login_field).send_keys(email)
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)
        self.driver.find_element(By.XPATH, self.signin_btn).click()

    def close_login_page(self):
        self.driver.find_element(By.XPATH, self.close_lp_btn).click()