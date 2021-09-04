"""Main Forms"""

from flask_wtf import FlaskForm
from wtforms.fields import TextField
from wtforms.fields.html5 import URLField

class SubscriptionForm(FlaskForm):
    """Login Form"""
    url = URLField('URL')