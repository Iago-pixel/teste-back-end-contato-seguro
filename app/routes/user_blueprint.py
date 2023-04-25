from flask import Blueprint
from app.controllers.user_controller import create_user, get_users, get_user, update_user, delete_user, add_company, get_user_companies

bp_user = Blueprint("bp_user", __name__, url_prefix="/user")

bp_user.post("")(create_user)
bp_user.get("")(get_users)
bp_user.get("/<user_id>")(get_user)
bp_user.patch("/<user_id>")(update_user)
bp_user.delete("/<user_id>")(delete_user)
bp_user.patch("/<user_id>/<company_id>")(add_company)
bp_user.get("/<user_id>/companies")(get_user_companies)
