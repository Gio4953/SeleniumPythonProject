from WorkingSpace.pages.login_page import LoginPage
from WorkingSpace.tests import values
from WorkingSpace.tests.values import driver


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page(values.login_url)
    login_page.login_to_account(values.email, values.pwd)
