"""Blueprints"""

import importlib

blueprints = [
    'app.blueprints.auth',
    'app.blueprints.feed',
]

def register_blueprints(app):
    """Register blueprints on app"""
    for bp in blueprints:
        mod = importlib.import_module(bp)
        app.register_blueprint(mod.bp)
