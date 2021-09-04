"""User service module"""

from passlib.hash import argon2

from app.exts.sqla import db
from app.models.user import UserModel

def get_by_id(user_id):
    """Get user by id"""
    return UserModel.query.get(user_id)

def get_all():
    """Get all users"""
    return UserModel.query.all()

def validate(email, password):
    """Validate user login"""
    user = UserModel.query.filter(UserModel.email == email).first()
    print(user)
    if not user:
        return None

    if argon2.verify(password, user.hash):
        return user

    return None
    
def register(email, password):
    """Register user account"""
    pw_hash = argon2.hash(password)
    user = UserModel(email=email, hash=pw_hash)
    db.session.add(user)
    db.session.commit()
    return user