# -*- coding: utf-8 -*-
"""
    ce
    ~~~~~~


"""

from flask import Flask, url_for
from flask import render_template, request

from .globals import req_data

class app():
    """
    """
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
            if v.type == 1:
                route_path = "/" + controller.name + k + "/<path:url_var>"
            print "Reg function: %s" % (route_path)
            
            self.app.add_url_rule(route_path, None, v.func, **v.options)


class controller(object):
    """
    """
    function_list = {}
    name = "none"

    def __init__(self, name):
        self.name = name

    def _on_recv(self, f):
        print "on_recv"
        def func(url_var):
            #print self.name + ":"+data
            #if req_data.is_post():
            #    return f(request.form)
            return f(url_var, req_data)
        func.__name__ = f.__name__
        return func

    def ez_api(self, rule, **options):
        """
        """
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            data = self._func_data(endpoint, 1, self._on_recv(f), **options)
            self.function_list[rule] = data
            return f
        return decorator    

    def api(self, rule, **options):
        """
        """
        def decorator(f):
            endpoint = options.pop('endpoint', None)
            #self.add_url_rule(rule, endpoint, f, **options)
            data = self._func_data(endpoint, 0, f, **options)
            self.function_list[rule] = data
            return f
        return decorator    

    class _func_data:
        def __init__(self, endpoint, type, f, **options):
            """type 1 means ez_api mode, 0 means normal mode
            """
            self.endpoint = endpoint
            self.func = f
            self.options = options
            self.type = type    # function reg type