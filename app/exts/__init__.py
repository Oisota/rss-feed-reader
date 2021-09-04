"""Flask Extensions"""

from .sqla import db
from .login import login_manager
from .migrate import migrate
from .debug_toolbar import debug_toolbar

def init_extenions(app):
    """Register extensions"""
    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)
