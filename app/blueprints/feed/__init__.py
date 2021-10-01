"""Main Blueprint"""

from flask import Blueprint

from .urls import register_urls
from .cli import register_commands
from .template_filters import register_filters

bp = Blueprint('feed', __name__, template_folder='templates')

register_urls(bp)
register_commands(bp)
register_filters(bp)