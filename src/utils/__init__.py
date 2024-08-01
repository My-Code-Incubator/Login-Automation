# AUTHOR: HBFL3Xx

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



def initialize_webdriver():
    """Initialize and return the Chrome WebDriver."""
    service = ChromeService(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def login_to_site(driver, username, password):
    """Perform login action on the site."""
    driver.get(os.environ.get('API_LOGIN_URL'))
    driver.find_element(by=By.ID, value='username').send_keys(username)
    driver.find_element(by=By.ID, value='password').send_keys(password)
    driver.find_element(by=By.CSS_SELECTOR, value='button.radius').click()


def is_login_successful(driver):
    """Check if login was successful."""
    try:
        success_msg_popup = driver.find_element(by=By.CSS_SELECTOR, value='.flash.success')
        return 'You logged into a secure area!' in success_msg_popup.text
    except NoSuchElementException:
        return False


