# tests/employee/test_employee_login.py

import pytest
from pages.employee.login_page import EmployeeLoginPage

@pytest.mark.parametrize("username, password, expected", [
    ("valid_employee@lms.com", "valid_password", "Dashboard"),  # Positive case
    ("invalid_employee@lms.com", "invalid_password", "Invalid credentials"),  # Negative case
    ("", "", "Fields required"),  # Empty fields test
])
def test_employee_login(driver, username, password, expected):
    # Initialize the page object
    login_page = EmployeeLoginPage(driver)
    
    # Load the page
    login_page.load()
    
    # Perform login
    login_page.login(username, password)
    
    # Example assertion: Check for expected results
    assert expected in driver.page_source  # Modify based on actual page behavior
