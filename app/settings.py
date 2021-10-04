"""Load config"""

import json

def configure(app):
    """Configure the app"""
    config = {}

    with app.open_instance_resource('config.json') as f:
        config = json.load(f)

    app.config.from_mapping(config)