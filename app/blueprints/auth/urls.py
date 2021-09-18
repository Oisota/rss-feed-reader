"""Register Blueprint URLS"""

from flask import Blueprint

from . import views

bp = Blueprint('auth', __name__, template_folder='templates')

bp.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'])
bp.add_url_rule('/logout', view_func=views.logout, methods=['GET', 'POST'])
bp.add_url_rule('/register', view_func=views.register, methods=['GET', 'POST'])