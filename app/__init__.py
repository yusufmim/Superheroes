from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    mail.init_app(app)

    from app.routes import init_routes
    init_routes(app)

    return app