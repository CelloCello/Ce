# -*- coding: utf-8 -*-
"""
    Test
    ~~~~~~


"""

from flask import Flask, url_for
from flask import render_template

class MyGame():
    gamecode = "Test"

    def do(self, data):
        return "This is MyGame:do:"+data

    def do2(self, data):
        return "This is MyGame:do2:"+data    

    def do3(self, data):
        return "This is MyGame:do3:"+data    

class MyService():
    funcList = {}
    name = ""

    def __init__(self, name):
        # self.callfunc = callback
        # self.route = route
        # print self.callfunc
        self.name = name
        pass

    def on_recv(self, f):
        print "on_recv"
        def func(data):
            print self.name + ":"+data
            return f(data)
        func.__name__ = f.__name__
        return func
        # print self.__class__.__name__ + ": GetData!!"
        # print self.callfunc
        # return self.callfunc(data)

    def reg_func(self, route, callback):
        #self.callfunc.append(callback)
        # self.route = route
        # self.callfunc = self.on_recv(callback)
        self.funcList[route] = self.on_recv(callback)

# def entryExit(f):
#     def new_f():
#         print "Entering", f.__name__
#         f()
#         print "Exited", f.__name__
#     new_f.__name__ = f.__name__
#     return new_f

# @entryExit
# def func1():
#     print "inside func1()"

# @entryExit
# def func2():
#     print "inside func2()"

# func1()
# func2()
# print func1.__name__


class MyApp():
    servList = {}

    def __init__(self, name):
        self.app = Flask(name)
        self.app.debug = True
        #app.run(host='0.0.0.0')
	
    def run(self):
        self.app.run()

    def add_service(self, serv):
        #print serv.on_recv
        #self.reg_func(serv.route, serv.on_recv)
        # for func in serv.callfunc:
        #     self.reg_func(func)
        #self.servList[serv.__name__] = serv
        #route_ = "/" + serv.route + "/<path:data>"
        #print serv.callfunc.__name__
        #self.app.route(route_)(serv.callfunc)
        for k,v in serv.funcList.iteritems():
            route_ = "/" + k + "/<path:data>"
            self.app.route(route_)(v)

    # def reg_func(self, route, callback):
    #     #route_ = "/"+callback.__name__+"/<path:data>"
    #     route_ = "/" + route + "/<path:data>"
    #     print route_
    #     print callback
    #     rst_ = self.app.route(route_)(callback)
    #     # for out in rst_:
    #     #     print out
    #     return rst_

class MyFlask():
    def __init__(self):
        self.app = Flask('Test')
        self.app.debug = True   

        @self.app.route('/<path:str>') 
        def MyTest(str):
            return str

    def run(self):
        self.app.run()

if __name__ == '__main__':

    # myf_ = MyFlask()
    # myf_.run()
    game_ = MyGame()

    myserv1_ = MyService("s1")
    myserv1_.reg_func("do",game_.do)
    myserv1_.reg_func("do3",game_.do3)
    myserv2_ = MyService("s2")
    myserv2_.reg_func("do2",game_.do2)

    myapp_ = MyApp("test")
    myapp_.add_service(myserv1_)
    myapp_.add_service(myserv2_)
    myapp_.run()
    #app.run()