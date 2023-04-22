from flask import Blueprint
from app.controllers.company_controller import create_company, get_company, get_companies, update_company, delete_company

bp_company = Blueprint("bp_company", __name__, url_prefix="/company")

bp_company.post("")(create_company)
bp_company.get("")(get_companies)
bp_company.get("<company_id>")(get_company)
bp_company.patch("<company_id>")(update_company)
bp_company.delete("<company_id>")(delete_company)
