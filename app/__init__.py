"""App Package"""

from flask import Flask

from .settings import configure
from .exts import init_extenions
from .blueprints import register_blueprints

def create_app():
    """App factory function"""
    app = Flask(__name__)
    configure(app)
    init_extenions(app)
    register_blueprints(app)
    return app