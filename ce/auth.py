# -*- coding: utf-8 -*-
"""
    auth
    ~~~~


"""

from flask import current_app

from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user
from functools import wraps

class user_base(UserMixin):
    
    def __init__(self, name, id, active=True):
        self.id = id
        self.name = name
        self.active = active

    def get_id(self):
        return self.id

    def is_active(self):
        return self.active

    def get_auth_token(self):
        return make_secure_token(self.name, key='deterministic')



class auth_manager(object):

    def __init__(self, app):
        self.login_mgr = LoginManager()
        self.login_mgr.init_app(app.app)

    def set_app(self, app):
        self.login_mgr.init_app(app.app)

    #def register(self, )

    def login(self, user):
        login_user(user)
        
    def logout(self):
        logout_user()

    def user_loader(self, callback):
        self.login_mgr.user_callback = callback
        return callback


def login_required(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.login_manager._login_disabled:
            return func(*args, **kwargs)
        elif not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()

        return func(*args, **kwargs)

    return decorated_view