# tests/test_ui.py

from pages.employee.login_page import EmployeeLoginPage
from pages.admin.login_page import AdminLoginPage

def test_employee_login_page_ui(driver):
    login_page = EmployeeLoginPage(driver)
    login_page.load()
    
    assert driver.find_element(*login_page.username_input).is_displayed()
    assert driver.find_element(*login_page.password_input).is_displayed()
    assert driver.find_element(*login_page.login_button).is_displayed()

def test_admin_login_page_ui(driver):
    login_page = AdminLoginPage(driver)
    login_page.load()
    
    assert driver.find_element(*login_page.username_input).is_displayed()
    assert driver.find_element(*login_page.password_input).is_displayed()
    assert driver.find_element(*login_page.login_button).is_displayed()
