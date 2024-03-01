from WorkingSpace.tests import values
from WorkingSpace.tests.values import driver
from WorkingSpace.pages.login_page import LoginPage
from WorkingSpace.pages.new_case_page import NewCasePage
from WorkingSpace.pages.projects_page import NewProject
from WorkingSpace.pages import eazy_life
login_page = LoginPage(driver)


def test_login(driver):
    login_page.open_page(values.login_url)
    login_page.login_to_account(values.email, values.pwd)


def test_new_project(driver):
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


def test_new_case(driver):
    new_case_page = NewCasePage(driver)
    new_case_page.open_page(values.projects_url)
    login_page.login_to_account(values.email, values.pwd)
    new_case_page.creat_case(values.title_name, values.description, values.status_option, values.severity_option,
                             values.priority_option, values.type_option, values.layer_option, values.flasky_option,
                             values.behaviour_option, values.automation_option, values.pre_condition_text,
                             values.post_condition_text, values.tags_option, values.parameter_title,
                             values.parameter_values, values.test_case_option, values.step_actions_text)

