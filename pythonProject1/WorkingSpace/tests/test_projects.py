import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from WorkingSpace.pages.login_page import LoginPage
from WorkingSpace.pages.projects_page import NewProject
from WorkingSpace.pages import eazy_life


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


def test_new_project(driver):
    login_page = LoginPage(driver)
    project_page = NewProject(driver)
    project_page.open_page("https://app.qase.io/projects?status=%5B%22active%22%5D")
    login_page.login_to_account("giorgikvernadze31@gmail.com", "P2ssw)rd#132")
    project_page.click_new_project()
    project_page.create_project("Description")
    project_page.click_project_access_type()
    if project_page.click_project_access_type() != eazy_life.Public:
        project_page.click_member_access()
        if project_page.click_member_access() == eazy_life.Option2:
            project_page.choose_group()
    project_page.click_create_project()
    driver.implicitly_wait(10)


