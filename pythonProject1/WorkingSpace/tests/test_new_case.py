import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from WorkingSpace.pages.login_page import LoginPage
from WorkingSpace.pages.new_case_page import NewCasePage


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


def test_new_case(driver):
    login_page = LoginPage(driver)
    new_case_page = NewCasePage(driver)
    new_case_page.open_page(f"https://app.qase.io/projects/")
    login_page.login_to_account("giorgikvernadze31@gmail.com", "P2ssw)rd#132")
    new_case_page.click_project()
    new_case_page.click_case_btn()
    new_case_page.enter_info("My Case Title", "My Case Description")
    new_case_page.choose_status("Draft")
    new_case_page.choose_severity("Blocker")
    new_case_page.choose_priority("High")
    new_case_page.choose_type("Functional")
    new_case_page.choose_layer("API")
    new_case_page.choose_is_flasky("Yes")
    new_case_page.choose_behaviour("Positive")
    new_case_page.choose_automation_status("Automated")
    new_case_page.enter_conditions("Some Precondition", "Some Post condition")
    new_case_page.choose_tags("Example tag")
    new_case_page.enter_parameters("Example title", "Example Value")
    new_case_page.choose_test_case_steps("Classic")
    new_case_page.enter_step_info("some text")
    new_case_page.click_save()
