from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.company_model import CompanyModel
    from app.models.user_model import UserModel
    from app.models.user_company_table import users_companies
