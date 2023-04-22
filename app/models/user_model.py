from sqlalchemy import Column, Integer, String
from app.configs.database import db
from dataclasses import dataclass
from app.models.user_company_table import users_companies


@dataclass
class UserModel(db.Model):
    id: int
    name: str
    email: str
    phone: str
    birth: str
    city: str
    companies: list

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(20))
    birth = Column(String(10))
    city = Column(String(20))

    companies = db.relationship(
        "CompanyModel",
        secondary=users_companies,
        backref="users"
    )
