import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


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


login_url = "https://app.qase.io/login"
projects_url = "https://app.qase.io/projects"

email = "giorgikvernadze31@gmail.com"
pwd = "P2ssw)rd#132"

title_name = "new case"
description = "this is my test description"
status_option = "Draft"
severity_option = "Major"
priority_option = "High"
type_option = "Smoke"
layer_option = "API"
flasky_option = "Yes"
behaviour_option = "Positive"
automation_option = "Automated"
pre_condition_text = "this is precondition text"
post_condition_text = "this is post condition text"
tags_option = "Example tag"
parameter_title = "some title"
parameter_values = "some value"
test_case_option = "Classic"
step_actions_text = "some actions text"
