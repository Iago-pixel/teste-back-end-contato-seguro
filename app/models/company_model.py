from sqlalchemy import Column, Integer, String
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class CompanyModel(db.Model):
    id: int
    name: str
    cnpj: str
    address: str

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    address = Column(String, nullable=False)
