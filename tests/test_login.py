# tests/test_login.py

import os
from dotenv import load_dotenv
from pages.employee.login_page import LoginPage
import pytest

# Load environment variables from .env file
load_dotenv()

@pytest.mark.parametrize("username, password", [
    (os.getenv('USERNAME_1'), os.getenv('PASSWORD_1')),
    (os.getenv('USERNAME_2'), os.getenv('PASSWORD_2')),
])
def test_login_with_multiple_users(driver, username, password):
    # Initialize the login page object
    login_page = LoginPage(driver)
    
    # Load the login page
    login_page.load()
    
    # Perform login action
    login_page.login(username, password)
    
    # Example: Check if login was successful by verifying page title or URL
    assert "MGENius - LMS" in driver.title  # Modify based on what happens after login