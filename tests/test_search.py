import pytest

from pages.onboarding_page import OnboardingPage
from pages.login_page import LoginPage
from pages.bottom_panel import BottomPanel
from pages.catalog_page import CatalogPage
from pages.home_page import HomePage

onboarding: OnboardingPage
login_p: LoginPage
bottom_panel: BottomPanel
catalog: CatalogPage
home: HomePage


@pytest.fixture(autouse=True)
def init_pages(driver):
    global onboarding, login_p, bottom_panel, catalog, home
    onboarding = OnboardingPage(driver)
    login_p = LoginPage(driver)
    bottom_panel = BottomPanel(driver)
    catalog = CatalogPage(driver)
    home = HomePage(driver)


def test_search(driver):
    onboarding.close_onboarding()
    login_p.login_with_email("testmail@mail.com", "testpass")
    home.ok_message()
    home.cancel_notif()
    bottom_panel.go_to_catalog()
    driver.implicitly_wait(10)
    catalog.search_course('тестирование')

    assert catalog.is_search_correct()


def test_price_filter(driver):
    onboarding.close_onboarding()
    login_p.close_login_page()
    bottom_panel.go_to_catalog()
    driver.implicitly_wait(10)
    catalog.set_filter_free_with_cert()
    assert catalog.is_filter_price_work()


def test_certificate_filter(driver):
    onboarding.close_onboarding()
    login_p.close_login_page()
    bottom_panel.go_to_catalog()
    driver.implicitly_wait(10)
    catalog.set_filter_free_with_cert()
    assert catalog.is_filter_certificate_work()
