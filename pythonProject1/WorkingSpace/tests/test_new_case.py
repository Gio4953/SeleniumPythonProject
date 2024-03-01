from WorkingSpace.tests import values
from WorkingSpace.tests.values import driver
from WorkingSpace.pages.login_page import LoginPage
from WorkingSpace.pages.new_case_page import NewCasePage


def test_new_case(driver):
    login_page = LoginPage(driver)
    new_case_page = NewCasePage(driver)
    new_case_page.open_page(values.projects_url)
    login_page.login_to_account(values.email, values.pwd)
    new_case_page.creat_case(values.title_name, values.description, values.status_option, values.severity_option,
                             values.priority_option, values.type_option, values.layer_option, values.flasky_option,
                             values.behaviour_option, values.automation_option, values.pre_condition_text,
                             values.post_condition_text, values.tags_option, values.parameter_title,
                             values.parameter_values, values.test_case_option, values.step_actions_text)
