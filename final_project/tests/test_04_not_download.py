import pytest
from selenium.webdriver.common.by import By

from final_project.pages.onboarding_page import OnboardingPage
from final_project.pages.login_page import LoginPage
from final_project.pages.bottom_panel import BottomPanel
from final_project.pages.catalog_page import CatalogPage
from final_project.pages.home_page import HomePage
from final_project.pages.course_page import CoursePage

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


@pytest.mark.run(order=5)
def test_not_download_with_mobile(driver):
    onboarding.close_onboarding()
    login_p.login_with_email("testmail@mail.org", "testpass")
    home.ok_message()
    home.cancel_notif()

    bottom_panel.go_to_catalog()
    driver.implicitly_wait(10)
    catalog.search_and_goto_first_course('Эффективная презентация проекта')
    course.join_course()
    course.wifi_off_mobile_on()
    course.download_with_mobile()
    assert course.is_error_mobile()
