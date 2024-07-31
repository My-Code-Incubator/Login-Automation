from flask import Blueprint
from src.controllers.reg_session_controller import register_session

reg_session_bp = Blueprint('register_session', __name__)

@reg_session_bp.route('/register_session', methods=['POST'])
def register_session_handler():
    """
    This function acts as a handler for the POST request to '/register_session' endpoint.
    It calls the 'register_session' function from 'src.controllers.reg_session_controller' module.

    Parameters:
    None

    Returns:
    The result of the 'register_session' function.
    """
    return register_session()