# AUTHOR: HBFL3Xx


from flask import Blueprint, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

browser_auth_bp = Blueprint('browser_auth', __name__)

# API endpoint URL
API_LOGIN_URL = 'https://the-internet.herokuapp.com/login'

# Dummy access token for testing purposes since the site we are testing doesnt provide access tokens
# This will change later after we have incorporated all functionalities to use real-world tokens
DUMMY_ACCESS_TOKEN = 'eyJhbGciOiAiSFMyNTYiLCAiaWF0IjoxNjg2NzUyMzEyLCJleHBpIjoxNjg2NzU1OTEyLCJ1c2VyX2lkIjogImR1bW15X3VzZXJfMTIzIn0.eyJhbGciOiAiSFMyNTYiLCAiaWF0IjoxNjg2NzUyMzEyLCJleHBpIjoxNjg2NzU1OTEyLCJ1c2VyX2lkIjogImR1bW15X3VzZXJfMTIzIn0.7nTvlbgPQeRoe4eK5LBqvH60J3_eU1owXaFpm7mMi0s'

def initialize_webdriver():
    """Initialize and return the Chrome WebDriver."""
    service = ChromeService(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def login_to_site(driver, username, password):
    """Perform login action on the site."""
    driver.get(API_LOGIN_URL)
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

@browser_auth_bp.route('/authenticate_browser', methods=['POST'])
def authenticate_browser():
    data = request.json
    device_id = data.get('device_id')
    username = data.get('username')
    password = data.get('password')

    if not all([device_id, username, password]):
        return jsonify({'error': 'Missing required fields. Make sure you include [device_id, username, password]'}), 400

    try:
        driver = initialize_webdriver()
        login_to_site(driver, username, password)

        if is_login_successful(driver):
            return jsonify({'access_token': DUMMY_ACCESS_TOKEN, 'site_name': driver.title}), 200
        else:
            return jsonify({'error': 'Invalid email or password. Try again!'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()  # Ensure the driver is closed after the process

