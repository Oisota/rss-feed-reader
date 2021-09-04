"""Load config"""

import os
import json

from flask import Flask

def configure(app):
    """Configure the app"""
    config = {}

    with app.open_instance_resource('config.json') as f:
        config = json.load(f)

    app.config.from_mapping(config)