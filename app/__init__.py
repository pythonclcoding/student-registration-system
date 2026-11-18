from flask import Flask
from flask_migrate import Migrate

from app.models import db
from config import Config


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    Migrate(app, db)

    from app.routes import main

    app.register_blueprint(main)

    return app