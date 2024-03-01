import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from WorkingSpace.pages.login_page import LoginPage


@pytest.fixture()
def driver(request):
    print("Starting test setup...")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)

    def teardown():
        print("Cleaning up after test...")
        try:
            if driver:
                driver.close()
                driver.quit()
        except Exception as e:
            print(f"Failed to close the browser: {e}")
    request.addfinalizer(teardown)
    return driver


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://app.qase.io/login")
    login_page.login_to_account("giorgikvernadze31@gmail.com", "P2ssw)rd#132")
