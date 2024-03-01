import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from WorkingSpace.pages import eazy_life


class RandomGenerator:
    @staticmethod
    def generate_random_string(length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_project_data(self):
        max_length = 10
        generated_combinations = set()

        while True:
            random_name_length = random.randint(1, max_length - 1)
            random_code_length = max_length - random_name_length

            random_name = self.generate_random_string(random_name_length)
            random_code = self.generate_random_string(random_code_length)

            combination = (random_name, random_code)

            if combination not in generated_combinations:
                generated_combinations.add(combination)
                return random_name, random_code


class NewProject:
    def __init__(self, driver):
        self.driver = driver
        self.new_project_btn = (By.ID, "createButton")
        self.project_name_input = (By.ID, "project-name")
        self.project_code_input = (By.ID, "project-code")
        self.description_input = (By.ID, "description-area")
        self.project_access_type_label = (By.XPATH, "//*[@id='modals']/div[2]/div/div/form/div[1]/div[4]/div[2]/div/label")
        self.member_access_checkbox = (By.XPATH, "//*[@id='modals']/div[2]/div/div/form/div[1]/div[4]/div[2]/label[1]/span[1]/input")
        self.choose_group_btn = (By.XPATH, "//*[@id='modals']/div[2]/div/div/form/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div[1]")
        self.create_project_btn = (By.XPATH, "//*[@id='modals']/div[2]/div/div/form/div[2]/button[2]/span")
        self.random_generator = RandomGenerator()
        self.random_name = None
        self.random_code = None

    def open_page(self, url):
        self.driver.get(url)

    def create_project(self, description):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_project_btn)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.new_project_btn)
        ).click()
        self.random_name, self.random_code = self.random_generator.generate_project_data()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.project_name_input)
        ).send_keys(self.random_name)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.project_code_input)
        ).send_keys(self.random_code)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.description_input)
        ).send_keys(description)
        return self.random_name, self.random_code

    def click_project_access_type(self):
        access_type_xpath = eazy_life.Private
        access_type = self.driver.find_element(By.XPATH, access_type_xpath)
        access_type.click()
        return access_type_xpath

    def click_member_access(self):
        member_access_xpath = eazy_life.Option2
        member_access = self.driver.find_element(By.XPATH, member_access_xpath)
        member_access.click()
        return member_access_xpath

    def choose_group(self):
        self.driver.find_element(*self.choose_group_btn).click()
        self.driver.find_element(By.XPATH, "//*[@id='modals']/div[2]/div/div/form/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div[2]/div/div").click()

    def click_create_project(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.create_project_btn)
        ).click()
