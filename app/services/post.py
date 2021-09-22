"""Post Service"""
import logging

from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from app.models.feed import PostModel
from app.exts.sqla import db

log = logging.getLogger(__name__)

def get_all(user, page=1, per_page=20):
    """Get all posts for a user"""
    return user.posts \
        .order_by(PostModel.pub_date.desc()) \
        .paginate(page, per_page, error_out=False)

def get_saved(user, page=1, per_page=20):
    """Get all posts for a user"""
    return user.posts \
        .filter(PostModel.saved == True) \
        .order_by(PostModel.pub_date.desc()) \
        .paginate(page, per_page, error_out=False)

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
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        log.debug('Duplicate post, skipping')

def toggle_save(post_id):
    """Mark post as saved"""
    post = PostModel.query.get(post_id)
    if post.saved:
        post.saved = False
    else:
        post.saved = True
    db.session.commit()
    return post

def delete(post_id):
    """Delete post"""
    post = PostModel.query.get(post_id)
    if not post:
        raise NotFound('Post {} Not Found'.format(post_id))
    db.session.delete(post)
    db.session.commit()