from WorkingSpace.tests import values
from WorkingSpace.tests.values import driver
from WorkingSpace.pages.login_page import LoginPage
from WorkingSpace.pages.projects_page import NewProject
from WorkingSpace.pages.new_case_page import NewCasePage
from WorkingSpace.pages import eazy_life


def test_signup(driver):

    login_page = LoginPage(driver)
    project_page = NewProject(driver)
    new_case_page = NewCasePage(driver)
    login_page.open_page("https://app.qase.io/login")
    login_page.login_to_account(values.email, values.pwd)

    project_page.create_project("This is my description")
    project_page.click_project_access_type()
    if project_page.click_project_access_type() != eazy_life.Public:
        project_page.click_member_access()
        if project_page.click_member_access() == eazy_life.Option2:
            project_page.choose_group()
    project_page.click_create_project()
    driver.implicitly_wait(10)

    new_case_page.creat_case(values.title_name, values.description, values.status_option, values.severity_option,
                             values.priority_option, values.type_option, values.layer_option, values.flasky_option,
                             values.behaviour_option, values.automation_option, values.pre_condition_text,
                             values.post_condition_text, values.tags_option, values.parameter_title,
                             values.parameter_values, values.test_case_option, values.step_actions_text)
