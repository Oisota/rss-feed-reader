"""Load config"""

import json
from logging.config import dictConfig

from flask.logging import default_handler

def configure(app):
    """Configure the app"""
    # load config file
    config = {}

    with app.open_instance_resource('config.json') as f:
        config = json.load(f)

    app.config.from_mapping(config)

    # setup logging
    app.logger.removeHandler(default_handler)
    assert app.config['ENV'] in ('dev', 'prod')

    if app.config['ENV'] == 'dev':
        log_config = {
            'version': 1,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s',
                }
            },
            'handlers': {
                'wsgi': {
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://flask.logging.wsgi_errors_stream',
                    'formatter': 'default'
                }
            },
            'root': {
                'level': 'DEBUG',
                'handlers': ['wsgi']
            }
        }
    elif app.config['ENV'] == 'prod':
        log_config = {
            'version': 1,
            'formatters': {
                'default': {
                    'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
                }
            },
            'handlers': {
                'wsgi': {
                    'class': 'logging.StreamHandler',
                    'stream': 'ext://flask.logging.wsgi_errors_stream',
                    'formatter': 'default'
                }
            },
            'root': {
                'level': 'INFO',
                'handlers': ['wsgi']
            }
        }

    dictConfig(log_config)