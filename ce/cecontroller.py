# -*- coding: utf-8 -*-
"""
    cecontroller
    ~~~~~~


"""


class cecontroller(object):
    function_list = {}
    name = "none"

    def __init__(self, name):
        self.name = name

    def api(self, rule, **options):
        """
        """
        def decorator(f):
            #self.add_url_rule(rule, endpoint, f, **options)
            self.function_list[rule] = f
            return f
        return decorator    
