from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/div[1]/div/input")
        self.password_textbox = (By.NAME, "password")
        self.rem_btn = (By.XPATH, "//*[@id='app']/div/div[1]/section[2]/form/label/span[1]/input")
        self.login_btn = (By.CLASS_NAME, "CAunhU")

    def open_page(self, url):
        self.driver.get(url)

    def login_to_account(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.email_textbox)
        ).send_keys(email)
        self.driver.find_element(*self.password_textbox).send_keys(password)
        # self.driver.find_element(*self.rem_btn).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_btn)
        ).click()


