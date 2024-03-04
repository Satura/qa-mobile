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

@pytest.mark.run(order=1)
def test_reg(driver):
    onboarding.close_onboarding()
    login_p.registry_new_user("Вилланель", "testmail@mail.org", "testpass")
    driver.implicitly_wait(15)
    home.is_greetings()
