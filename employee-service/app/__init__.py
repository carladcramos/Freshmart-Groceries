from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db
from app.routes import employee_bp
import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(employee_bp, url_prefix='/api')

    return app
