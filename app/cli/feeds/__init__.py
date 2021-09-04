"""Feed CLI commands"""

from flask.cli import AppGroup

from .load import main as load_feeds

cli = AppGroup('feed', help='feed related tasks')

cli.command('load')(load_feeds)