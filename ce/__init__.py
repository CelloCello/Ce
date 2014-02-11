# -*- coding: utf-8 -*-
"""
    ce
    ~~~~~~
    ce init

"""

__version__ = '0.01-dev'  

from .globals import req_data
from .templating import render
from .auth import auth_manager, user_base, login_required