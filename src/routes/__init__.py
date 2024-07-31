from flask import Blueprint
from src.routes.session_registration_route import reg_session_bp
health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return {"status": "healthy"}, 200

def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(reg_session_bp)
