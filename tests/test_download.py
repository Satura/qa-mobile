import pytest
from selenium.webdriver.common.by import By

from pages.onboarding_page import OnboardingPage
from pages.login_page import LoginPage
from pages.bottom_panel import BottomPanel
from pages.catalog_page import CatalogPage
from pages.home_page import HomePage
from pages.course_page import CoursePage

onboarding: OnboardingPage
login_p: LoginPage
bottom_panel: BottomPanel
catalog: CatalogPage
home: HomePage
course: CoursePage

@pytest.fixture(autouse=True)
def init_pages(driver):
    global onboarding, login_p, bottom_panel, catalog, home, course
    onboarding = OnboardingPage(driver)
    login_p = LoginPage(driver)
    bottom_panel = BottomPanel(driver)
    catalog = CatalogPage(driver)
    home = HomePage(driver)
    course = CoursePage(driver)

def test_download(driver):

    onboarding.close_onboarding()
    login_p.login_with_email("testmail@mail.com", "testpass")
    home.ok_message()
    home.cancel_notif()

    bottom_panel.go_to_catalog()
    driver.implicitly_wait(10)
    catalog.search_course('Эффективная презентация проекта')
    driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="org.stepic.droid:id/courseListCoursesRecycler"]/androidx.cardview.widget.CardView[1]/android.view.ViewGroup/android.view.View').click()
    course.join_course()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, course.navigate_up_btn).click()

    course.download_with_mobile()
    assert course.is_error_mobile()
