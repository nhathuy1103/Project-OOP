from flask import Flask
from config import Config
from database import db
from flask_migrate import Migrate
from app.routes import orderitem_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    # Đăng ký các route (API endpoints)
    app.register_blueprint(orderitem_bp)

    return app
