# pages/employee/login_page.py

from selenium.webdriver.common.by import By

class EmployeeLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'username')
        self.password_input = (By.ID, 'password')
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def load(self):
        self.driver.get("http://172.16.6.42/login")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
