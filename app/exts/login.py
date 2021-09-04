"""Login Extension"""

from flask_login import LoginManager

from app.services import user

login_manager = LoginManager()

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    """Load user from id"""
    return user.get_by_id(user_id)