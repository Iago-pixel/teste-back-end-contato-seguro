from flask import request, current_app, jsonify
from app.models.user_model import UserModel
from app.models.company_model import CompanyModel
from app.models.user_company_table import UserCompanyModel


def create_user():
    data = request.get_json()

    new_user = UserModel(
        name=data["name"],
        email=data["email"],
        phone=data.setdefault("phone", ""),
        birth=data.setdefault("birth", ""),
        city=data.setdefault("city", ""),
    )

    current_app.db.session.add(new_user)
    current_app.db.session.commit()

    return jsonify(new_user), 201


def get_users():
    company_id = request.args.get("company_id")

    if company_id:
        company = (
            CompanyModel
            .query
            .get_or_404(company_id, description="Empresa não encontrada")
        )

        users = company.users
    else:
        users = (
            UserModel
            .query
            .all()
        )

    return jsonify(users)


def get_user(user_id):
    user = (
        UserModel
        .query
        .filter_by(id=user_id)
        .first_or_404(description="Usuário não encontrado")
    )

    return jsonify(user)


def update_user(user_id):
    data = request.get_json()

    user = UserModel.query.get_or_404(
        user_id, description="Usuário não encontrado")

    for key, value in data.items():
        setattr(user, key, value)

    current_app.db.session.add(user)
    current_app.db.session.commit()

    return "", 204


def delete_user(user_id):
    query = UserModel.query.get_or_404(
        user_id, description="Usuário não encontrado")

    current_app.db.session.delete(query)
    current_app.db.session.commit()

    return "", 204


def add_company(user_id, company_id):
    user = UserModel.query.get_or_404(
        user_id, description="Usuário não encontrado")

    company = CompanyModel.query.get_or_404(
        company_id, description="Empresa não encontrada")

    user.companies.append(company)

    current_app.db.session.commit()

    return "", 204


def get_user_companies(user_id):
    user = UserModel.query.get_or_404(
        user_id, description="Usuário não encontrado")

    user_company_filter = UserCompanyModel.query.filter_by(user_id=user_id)

    companies = []

    for user_company in user_company_filter:
        company = CompanyModel.query.filter_by(
            id=user_company.company_id).one_or_none()

        companies.append(company)

    return jsonify(companies)
