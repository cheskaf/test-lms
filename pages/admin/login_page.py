# pages/admin/login_page.py

from selenium.webdriver.common.by import By

class AdminLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'admin_username')
        self.password_input = (By.ID, 'admin_password')
        self.login_button = (By.ID, 'admin_login_button')

    def load(self):
        self.driver.get("http://your-url.com/admin-login")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
