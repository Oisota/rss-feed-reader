"""Post Service"""

from app.models.feed import PostModel
from app.exts.sqla import db

def get_all(user):
    """Get all posts for a user"""
    return user.posts

def insert(**kwargs):
    """Insert post into DB

    kwargs:
        user_id - id of user post belongs to
        subscription_id - id of subscription post belongs to
        pub_date - date post was published
        title - title of post
        url - url of post
        feed_title - title of feed
        content - text content of post
    """
    post = PostModel(**kwargs)
    db.session.add(post)
    db.session.commit()