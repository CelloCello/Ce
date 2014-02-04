# -*- coding: utf-8 -*-
"""
    global
    ~~~~~~


"""

from flask import request
from flask import render_template

class ce_request:
    def __init__(self):
        #self.req_src = request
        pass

    def data(self, name):
        if self.is_post():
            return self.post_data(name)

        return self.get_data(name)

    def post_data(self, name):
        if request.form:
            return request.form[name]
        return "no post val"

    def get_data(self, name):
        if request.args:
            return request.args.get(name, '')
        return "no get val"

    def method(self):
        return request.method

    def is_post(self):
        if request.method == "POST":
            return True
        return False

    def is_get(self):
        if request.method == "GET":
            return True
        return False        
  

#req_data = request.form
req_data = ce_request()