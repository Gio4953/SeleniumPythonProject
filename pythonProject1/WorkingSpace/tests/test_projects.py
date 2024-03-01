from WorkingSpace.pages.login_page import LoginPage
from WorkingSpace.pages.projects_page import NewProject
from WorkingSpace.pages import eazy_life
from WorkingSpace.tests import values
from WorkingSpace.tests.values import driver


def test_new_project(driver):
    login_page = LoginPage(driver)
    project_page = NewProject(driver)
    project_page.open_page(values.projects_url)
    login_page.login_to_account(values.email, values.pwd)
    project_page.create_project("Description")
    project_page.click_project_access_type()
    if project_page.click_project_access_type() != eazy_life.Public:
        project_page.click_member_access()
        if project_page.click_member_access() == eazy_life.Option2:
            project_page.choose_group()
    project_page.click_create_project()
    driver.implicitly_wait(10)


