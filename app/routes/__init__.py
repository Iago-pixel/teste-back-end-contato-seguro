from flask import Flask
from app.routes.user_blueprint import bp_user
from app.routes.company_blueprint import bp_company


def init_app(app: Flask) -> None:
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_company)
