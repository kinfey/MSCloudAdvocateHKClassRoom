from flask import Blueprint,Flask

bp = Blueprint('shop', __name__, template_folder='../views')

from shop import shop_controller