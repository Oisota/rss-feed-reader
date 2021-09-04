"""Register cli commands"""

from .feeds import cli as feed_cli

def register_commands(app):
    """Register commands"""
    app.cli.add_command(feed_cli)