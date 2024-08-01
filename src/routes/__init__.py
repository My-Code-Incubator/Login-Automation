from flask import Blueprint

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return {"status": "healthy"}, 200

def register_routes(app):
    app.register_blueprint(health_bp)
