from flask import Blueprint,Flask


bp = Blueprint('user', __name__, template_folder='../views')


from user import user_controller