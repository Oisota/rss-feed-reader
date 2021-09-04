"""Feed service"""

from flask_login import current_user

from app.exts.sqla import db
from app.models.feed import SubscriptionModel

def get_all(user=None):
    """Get all feeds for a user"""
    if user:
        return user.subscriptions
    return SubscriptionModel.query.all()

def add(user, url):
    """Add feed for a user"""
    sub = SubscriptionModel(url=url, user_id=user.id)
    db.session.add(sub)
    db.session.commit()

def remove(user_id, subscription_id):
    """Remove feed for a user"""
    SubscriptionModel.query.get(subscription_id).delete()
    db.session.commit()