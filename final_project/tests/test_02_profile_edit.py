import pytest
from selenium.webdriver.common.by import By

from final_project.pages.onboarding_page import OnboardingPage
from final_project.pages.login_page import LoginPage
from final_project.pages.bottom_panel import BottomPanel
from final_project.pages.catalog_page import CatalogPage
from final_project.pages.home_page import HomePage
from final_project.pages.course_page import CoursePage
from final_project.pages.profile_page import ProfilePage

onboarding: OnboardingPage
login_p: LoginPage
bottom_panel: BottomPanel
catalog: CatalogPage
home: HomePage
course: CoursePage
profile: ProfilePage


@pytest.fixture(autouse=True)
def init_pages(driver):
    global onboarding, login_p, bottom_panel, catalog, home, course, profile
    onboarding = OnboardingPage(driver)
    login_p = LoginPage(driver)
    bottom_panel = BottomPanel(driver)
    catalog = CatalogPage(driver)
    home = HomePage(driver)
    course = CoursePage(driver)
    profile = ProfilePage(driver)


@pytest.mark.run(order=2)
def test_profile_edit(driver):
    onboarding.close_onboarding()
    login_p.login_with_email("testmail@mail.org", "testpass")
    home.ok_message()
    home.cancel_notif()

    bottom_panel.go_to_profile()
    profile.edit_profile_main("Ольга", "Анварова")
    assert profile.is_profile_changed()
    profile.close_profile_editor()

