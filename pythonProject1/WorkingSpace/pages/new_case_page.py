from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewCasePage:
    def __init__(self, driver):
        self.driver = driver
        self.case_btn = (By.XPATH, "//*[@id='create-case-button']")
        self.title = (By.CLASS_NAME, "DcqLJ3")
        self.status = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[2]/div[2]/div")
        self.Description = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[3]/div/div/div/div["
                                      "2]/div/div[2]/div/div")
        self.severity = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[4]/div[2]/div/div")
        self.priority = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[4]/div[3]/div/div")
        self.type = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[4]/div[4]/div/div")
        self.layer = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[4]/div[5]/div/div")
        self.is_flasky = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[4]/div[6]/div/div")
        self.behavior = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[4]/div[8]/div/div")
        self.automation_status = (
            By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[4]/div[9]/div/div")
        self.pre_conditions = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[6]/div["
                                         "1]/div/div/div/div[2]/div/div[2]/div/div/p")
        self.post_conditions = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[6]/div["
                                          "2]/div/div/div/div[2]/div/div[2]/div/div/p")
        self.tags = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[8]/div/div/div")
        self.attachments = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[10]/div/div/button")
        self.parameters = (By.XPATH, "//*[@id='case-attachments']/div/button/span")
        self.parameter_title = (By.XPATH, "//*[@id='case-attachments']/div/div/div[1]/div[2]/div/input")
        self.parameter_values = (By.XPATH, "//*[@id='case-attachments']/div/div/div[2]/div[2]/div/div/div[2]/input")
        self.test_case_steps = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[13]/div")
        self.add_step = (
            By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[14]/div[2]/button[1]/span")
        self.step_actions = (By.XPATH,
                             "//*[@id='application-content']/div/div[2]/form/div[1]/div[14]/div[1]/div/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/div/div")
        self.data = (By.CSS_SELECTOR, 'p[data-placeholder="Data"].ffKG9K')
        self.expected_result = (By.CSS_SELECTOR, 'p[data-placeholder="Expected result"].ffKG9K')
        self.upload = (By.XPATH, "//*[@id='application-content']/div/div[2]/form/div[1]/div[14]/div["
                                 "1]/div/div/div/button[1]")
        self.save = (By.XPATH, "//*[@id='save-case']/span")

    def open_page(self, url):
        self.driver.get(url)

    def creat_case(self, title_name, description, status_option, severity_option, priority_option, type_option,
                   layer_option, flasky_option, behaviour_option, automation_option, pre_condition_text,
                   post_condition_text, tags_option, parameter_title, parameter_values, test_case_option,
                   step_actions_text):
        self.driver.find_element(By.XPATH, "//*[@id='application-content']/div/table/tbody/tr[2]/td[3]/div/div").click()
        case_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.case_btn)
        )
        case_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.title)
        ).send_keys(title_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.Description)
        ).send_keys(description)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.status)
        ).click()
        status_dict = {
            "Actual": "//*[@id='modals']/div[9]/div/div/div[1]",
            "Draft": "//*[@id='modals']/div[9]/div/div/div[2]",
            "Deprecated": "//*[@id='modals']/div[9]/div/div/div[3]",
        }

        if status_option in status_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, status_dict[status_option]))
            ).click()
        else:
            print(f"Unknown status: {status_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.severity)
        ).click()
        severity_dict = {
            "Not set": "//*[@id='modals']/div[9]/div/div/div[1]",
            "Blocker": "//*[@id='modals']/div[9]/div/div/div[2]",
            "Critical": "//*[@id='modals']/div[9]/div/div/div[3]",
            "Major": "//*[@id='modals']/div[9]/div/div/div[4]",
            "Normal": "//*[@id=''modals']/div[9]/div/div/div[5]",
            "Minor": "//*[@id='modals']/div[9]/div/div/div[6]",
            "Trivial": "//*[@id='modals']/div[9]/div/div/div[7]",
        }

        if severity_option in severity_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, severity_dict[severity_option]))
            ).click()
        else:
            print(f"Unknown severity: {severity_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.priority)
        ).click()
        priority_dict = {
            "Not set": "//*[@id='modals']/div[9]/div/div/div[1]",
            "High": "//*[@id='modals']/div[9]/div/div/div[2]",
            "Medium": "//*[@id='modals']/div[9]/div/div/div[3]",
            "Low": "//*[@id='modals']/div[9]/div/div/div[4]",
        }

        if priority_option in priority_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, priority_dict[priority_option]))
            ).click()
        else:
            print(f"Unknown priority: {priority_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.type)
        ).click()
        type_dict = {
            "Other": "//*[@id='modals']/div[9]/div/div/div[1]",
            "Functional": "//*[@id='modals']/div[9]/div/div/div[2]",
            "Smoke": "//*[@id='modals']/div[9]/div/div/div[3]",
            "Regression": "//*[@id='modals']/div[9]/div/div/div[4]",
            "Security": "//*[@id='modals']/div[9]/div/div/div[5]",
            "Usability": "//*[@id='modals']/div[9]/div/div/div[6]",
            "Performance": "//*[@id='modals']/div[9]/div/div/div[7]",
            "Acceptance": "//*[@id='modals']/div[9]/div/div/div[8]",
            "Compatibility": "//*[@id='modals']/div[9]/div/div/div[9]",
            "Integration": "//*[@id='modals']/div[9]/div/div/div[10]",
            "Exploratory": "//*[@id='modals']/div[9]/div/div/div[11]",
        }

        if type_option in type_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, type_dict[type_option]))
            ).click()
        else:
            print(f"Unknown type: {type_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.layer)
        ).click()
        layer_dict = {
            "Not set": "//*[@id='modals']/div[9]/div/div/div[1]",
            "E2E": "//*[@id='modals']/div[9]/div/div/div[2]",
            "API": "//*[@id='modals']/div[9]/div/div/div[3]",
            "Unit": "//*[@id='modals']/div[9]/div/div/div[4]",
        }

        if layer_option in layer_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, layer_dict[layer_option]))
            ).click()
        else:
            print(f"Unknown layer: {layer_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.is_flasky)
        ).click()
        is_flasky_dict = {
            "Yes": "//*[@id='modals']/div[9]/div/div/div[1]",
            "No": "//*[@id='modals']/div[9]/div/div/div[2]",
        }

        if flasky_option in is_flasky_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, is_flasky_dict[flasky_option]))
            ).click()
        else:
            print(f"Unknown option for is_flasky: {flasky_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.behavior)
        ).click()
        behaviour_dict = {
            "Not set": "//*[@id='modals']/div[9]/div/div/div[1]",
            "Positive": "//*[@id='modals']/div[9]/div/div/div[2]",
            "Negative": "//*[@id='modals']/div[9]/div/div/div[3]",
            "Destructive": "//*[@id='modals']/div[9]/div/div/div[4]",
        }

        if behaviour_option in behaviour_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, behaviour_dict[behaviour_option]))
            ).click()
        else:
            print(f"Unknown option for behaviour: {behaviour_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.automation_status)
        ).click()
        automation_status_dict = {
            "Manual": "//*[@id='modals']/div[9]/div/div/div[1]",
            "Automated": "//*[@id='modals']/div[9]/div/div/div[2]",
        }

        if automation_option in automation_status_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, automation_status_dict[automation_option]))
            ).click()
        else:
            print(f"Unknown status for automation: {automation_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.pre_conditions)
        ).send_keys(pre_condition_text)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.post_conditions)
        ).send_keys(post_condition_text)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.tags)
        ).click()
        tag_dict = {
            "Example tag": "//*[@id='react-select-3-option-0']",
        }

        if tags_option in tag_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, tag_dict[tags_option]))
            ).click()
        else:
            print(f"Unknown tag option: {tags_option}")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.parameters)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.parameter_title)
        ).send_keys(parameter_title)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.parameter_values)
        ).send_keys(parameter_values)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.test_case_steps)
        ).click()
        choose_test_case_dict = {
            "Classic": "//*[@id='application-content']/div/div[2]/form/div[1]/div[13]/div/div/div[2]/div/div/div[1]",
            "Gherkin": "//*[@id='application-content']/div/div[2]/form/div[1]/div[13]/div/div/div[2]/div/div/div[2]",
        }

        if test_case_option in choose_test_case_dict:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, choose_test_case_dict[test_case_option]))
            ).click()
        else:
            print(f"Unknown status for automation: {test_case_option}")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_step)
        ).click()
        self.driver.find_element(*self.step_actions).send_keys(step_actions_text)
        # self.driver.find_element(*self.data).send_keys(data_text)
        # self.driver.find_element(*self.expected_result).send_keys(expected_result_text)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save)
        ).click()
