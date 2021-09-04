"""User Model"""

from app.exts.sqla import db

class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    hash = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '{}, {}'.format(self.id, self.email)

    # Flask-Login compatibility
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
