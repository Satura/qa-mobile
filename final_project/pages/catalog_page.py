from selenium.webdriver.common.by import By

from final_project.pages.base_page import BasePage


class CatalogPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_req = ''
        self.search_field = '//android.widget.AutoCompleteTextView[@resource-id="org.stepic.droid:id/search_src_text"]'
        self.filter_btn = '//android.widget.ImageView[@resource-id="org.stepic.droid:id/filterIcon"]'

        # filters
        self.lang_any = '//android.widget.RadioButton[@resource-id="org.stepic.droid:id/anyRadioButton"]'
        self.lang_ru = '//android.widget.RadioButton[@resource-id="org.stepic.droid:id/rusRadioButton"]'
        self.lang_en = '//android.widget.RadioButton[@resource-id="org.stepic.droid:id/engRadioButton"]'
        self.certificate_switch = '//android.widget.Switch[@resource-id="org.stepic.droid:id/certificatesSwitch"]'
        self.free_switch = '//android.widget.Switch[@resource-id="org.stepic.droid:id/freeSwitch"]'
        self.result_btn = '//android.widget.Button[@resource-id="org.stepic.droid:id/applyFilterAction"]'

        # course's lang
        self.ru_btn = '//android.widget.CompoundButton[@resource-id="org.stepic.droid:id/languageRu"]'
        self.en_btn = '//android.widget.CompoundButton[@resource-id="org.stepic.droid:id/languageEn"]'

        self.stories_len = '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.stepic.droid:id/storiesRecycler"]'

        # search results: courses cards
        self.course_name = '//android.widget.TextView[@resource-id="org.stepic.droid:id/courseItemName"]'
        # self.courseListCourses = '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.stepic.droid:id/courseListCoursesRecycler"]'
        self.card_price = '//android.widget.TextView[@resource-id="org.stepic.droid:id/coursePrice"]'
        self.card_cert = '//android.widget.TextView[@resource-id="org.stepic.droid:id/courseCertificateText"]'
        self.back_btn = '//android.widget.ImageView[@resource-id="org.stepic.droid:id/backIcon"]'

    def search_course(self, request):
        self.search_req = request
        field = self.driver.find_element(By.XPATH, self.search_field)
        self.driver.find_element(By.XPATH, self.ru_btn).click()
        field.send_keys(self.search_req)
        self.driver.find_element(By.XPATH, self.filter_btn).click()
        self.driver.find_element(By.XPATH, self.result_btn).click()
        self.driver.implicitly_wait(20)

        # self.driver.find_element(By.XPATH, self.search_field).send_keys(Keys.ENTER)
        # self.driver.press_keycode(66)
        # ActionChains(self.driver).send_keys(Keys.INSERT)

    def set_filter_free_with_cert(self):
        self.driver.find_element(By.XPATH, self.filter_btn).click()
        self.driver.find_element(By.XPATH, self.free_switch).click()
        self.driver.find_element(By.XPATH, self.certificate_switch).click()
        self.driver.find_element(By.XPATH, self.result_btn).click()

    def is_search_correct(self):
        cards = self.driver.find_elements(By.XPATH, self.course_name)
        result = True
        control = ''

        if len(self.search_req) >= 5:
            control = self.search_req[:-2].lower()
        else:
            control = self.search_req.lower()

        for card in cards:
            if (card.text.lower().find(control)) == -1:
                print(card.text.lower())
                result = False

        return result

    def is_filter_price_work(self):
        prices = self.driver.find_elements(By.XPATH, self.card_price)
        result = True
        for p in prices:
            if p.text.find('Бесплатно') != -1 and p.text.find('Free') != -1:
                result = False
        return result

