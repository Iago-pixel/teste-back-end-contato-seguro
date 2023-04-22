from flask import request, current_app, jsonify
from app.models.company_model import CompanyModel
from app.models.user_model import UserModel


def create_company():
    data = request.get_json()

    new_company = CompanyModel(
        name=data["name"],
        cnpj=data["cnpj"],
        address=data["address"],
    )

    current_app.db.session.add(new_company)
    current_app.db.session.commit()

    return jsonify(new_company)


def get_companies():
    companies = (
        CompanyModel
        .query
        .all()
    )

    return jsonify(companies)


def get_company(company_id):
    company = (
        CompanyModel
        .query
        .filter_by(id=company_id)
        .first_or_404(description="Empresa não encontrada")
    )

    return jsonify(company)


def update_company(company_id):
    data = request.get_json()

    company = CompanyModel.query.get_or_404(
        company_id, description="Empresa não encontrada")

    for key, value in data.items():
        setattr(company, key, value)

    current_app.db.session.add(company)
    current_app.db.session.commit()

    return jsonify(company)


def delete_company(company_id):
    query = CompanyModel.query.get_or_404(
        company_id, description="Empresa não encontrada")

    current_app.db.session.delete(query)
    current_app.db.session.commit()

    return "", 204
