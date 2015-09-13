from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % self.username


class UserSettings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    randomized = db.Column(db.Boolean())
    last_photo = db.Column(db.Integer())

    def __init__(self, user_id, randomized, last_photo):
        self.user_id = user_id
        self.randomized = randomized
        self.last_photo = last_photo

    @property
    def __repr__(self):
        return '<User Settings %r>' % self.user_id


class Photo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    filename = db.Column(db.String())
    deleted = db.Column(db.Boolean())

    def __init__(self, filename, deleted):
        self.filename = filename
        self.deleted = deleted

    @property
    def __repr__(self):
        return '<Photo %r>' % self.filename
