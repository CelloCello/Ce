# -*- coding: utf-8 -*-
"""
    ceapp
    ~~~~~~


"""

from flask import Flask, url_for
from flask import render_template

import traceback


class ceapp():
    controller_list = {}

    def __init__(self, name):
        self.app = Flask(name)
        self.app.debug = True
        #app.run(host='0.0.0.0')
	
    def run(self, port):
        for k,v in self.controller_list.iteritems():
            print "Start Controller: %s" % (k)
           
        self.app.run(host='0.0.0.0', port=port)

    def add_controller(self, controller):          
        self.controller_list[controller.name] = controller
        for k,v in controller.function_list.iteritems():
            route_path = "/" + controller.name + k
            print "Reg function: %s" % (route_path)
            self.app.add_url_rule(route_path, None, v)