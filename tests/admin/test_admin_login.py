# tests/admin/test_admin_login.py

import pytest
from pages.admin.login_page import AdminLoginPage

@pytest.mark.parametrize("username, password, expected", [
    ("valid_admin@lms.com", "valid_password", "Admin Dashboard"),  # Positive case
    ("invalid_admin@lms.com", "invalid_password", "Invalid credentials"),  # Negative case
    ("", "", "Fields required"),  # Empty fields test
])
def test_admin_login(driver, username, password, expected):
    # Initialize the page object
    login_page = AdminLoginPage(driver)
    
    # Load the page
    login_page.load()
    
    # Perform login
    login_page.login(username, password)
    
    # Example assertion: Check for expected results
    assert expected in driver.page_source  # Modify based on actual page behavior
