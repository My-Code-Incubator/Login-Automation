# AUTHOR: HBFL3Xx

import os
from flask import Blueprint, request, jsonify

from src.utils import initialize_webdriver, login_to_site, is_login_successful


browser_auth_bp = Blueprint('browser_auth', __name__)


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
            return jsonify({'access_token': os.environ.get('DUMMY_ACCESS_TOKEN'), 'site_name': driver.title}), 200
        else:
            return jsonify({'error': 'Invalid email or password. Try again!'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()  # Ensure the driver is closed after the process

