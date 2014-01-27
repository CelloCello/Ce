# -*- coding: utf-8 -*-
"""
    test_app
    ~~~~~~


"""


import ceapp
import cecontroller

my_admin_ctrl = cecontroller.cecontroller("admin")
        
@my_admin_ctrl.api('/func1')
def func1():
    return "This is admin func1"	


if __name__ == '__main__':
    #app = ceapp("MyGame")
    #app.add_controller(my_ctrl)

    admin_app = ceapp.ceapp("MyAdmin")
    admin_app.add_controller(my_admin_ctrl)
    admin_app.run(5020)
    pass
