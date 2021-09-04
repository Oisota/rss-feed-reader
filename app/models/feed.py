"""Feed Models"""

from sqlalchemy import UniqueConstraint

from app.exts.sqla import db

class SubscriptionModel(db.Model):
    """RSS Feed Subscription"""
    __tablename__ = 'subscription'
    __table_args__ = (
        UniqueConstraint('url', 'user_id', name='uc_user_url'),
    )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String(255), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('subscriptions', lazy=True))

class PostModel(db.Model):
    """Individual Feed Post"""
    __tablename__ = 'post'
    __table_args__ = (
        UniqueConstraint('url', 'user_id', name='uc_user_url'),
    )
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('posts', lazy=True))
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    subscription = db.relationship(SubscriptionModel, backref=db.backref('posts', lazy=True))
    pub_date = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    feed_title = db.Column(db.String(255), nullable=False)
    saved = db.Column(db.Boolean, default=False)
    content = db.Column(db.Text, nullable=False)