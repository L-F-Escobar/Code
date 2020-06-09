import os
if os.environ.get('ENV') == 'TESTING': from tests.db import db
else: from app import app, db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    '''  User information and configuration settings for use throughout the site. '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(200))
    phone = db.Column(db.Text)
    photo = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    # db.relationships
    configuration = db.relationship('UserConfig', backref='user', uselist=False) # 1 user to 1 user_configuation
    roles = db.relationship('Roles', backref='user') # 1 user to many roles

    def __init__(self, email, first_name, last_name, phone, photo):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.photo = photo
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User {self.id}'

class UserConfig(db.Model):
    '''  User information and configuration settings for use throughout the site. '''
    __tablename__ = 'user_config'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    option = db.Column(db.Text)
    vale = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    def __init__(self, user_id, option, vale):
        self.user_id = user_id
        self.option = option
        self.vale = vale
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f'UserConfig {self.id}'

class RolesPermissionsLink(db.Model):
    __tablename__ = 'roles_permissions'

    role_id = db.Column(
        db.Integer,
        db.ForeignKey('roles.id'),
        primary_key = True
    )

    permission_id = db.Column(
        db.Integer,
        db.ForeignKey('permissions.id'),
        primary_key = True
    )

class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    permission = db.relationship('Permissions', secondary = 'roles_permissions') # many roles to many permissions

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f'Role {self.name}'

class Permissions(db.Model):
    __tablename__ = 'permissions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

    role = db.relationship('Roles', secondary='roles_permissions') # many permissions to many roles

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __repr__(self):
        return f'Permission {self.name}'

