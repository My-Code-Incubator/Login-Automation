from flask import Flask
from src.config.config import configure_app
from src.routes import register_routes

app = Flask(__name__)
configure_app(app)
register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
