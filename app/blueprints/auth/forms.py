"""Auth Forms"""

from flask_wtf import FlaskForm
from wtforms.fields import PasswordField
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    """Login Form"""
    email = EmailField('Email')
    password = PasswordField('Password')

class RegisterForm(FlaskForm):
    """Account Creation Form"""
    email = EmailField('Email')
    password = PasswordField('Password')