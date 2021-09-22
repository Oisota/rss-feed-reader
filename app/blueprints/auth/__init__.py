"""Auth Blueprint"""

from flask import Blueprint

from .urls import register_urls

bp = Blueprint('auth', __name__, template_folder='templates')

register_urls(bp)