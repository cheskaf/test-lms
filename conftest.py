# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Set implicit wait time
    driver.implicitly_wait(10)
    
    # Return driver for use in tests
    yield driver
    
    # Teardown: Close the browser after each test
    driver.quit()
