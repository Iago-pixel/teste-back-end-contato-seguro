from flask import Flask
from os import getenv
from app.configs import migrations, database
from app import routes
from flask_cors import CORS


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    CORS(app)

    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)

    return app
