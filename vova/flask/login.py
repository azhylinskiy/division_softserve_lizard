#!/usr/bin/python2.7
import sys 

from model.login import LoginModel
from view.login import LoginHtmlView

def login(model, **params):
    return model.getRole(**params)

def view(model, **params):
    return '#NO'

action = {
        'view' : view,
        'login' : login,
        }

def draw(view, data):
    view.draw(data)

def redirect(view, place):
    """redirect to another view"""
    view.redirect(place)

responce = {
        '#NO' : ('#NO', draw),
        '#ERROR' : ('#ERROR', draw),
        'ADMIN' : ('admin.py', redirect),
        'WAITER' : ('login.py', redirect),
        'MANAGER' : ('login.py', redirect),
        'DIRECTOR' : ('login.py', redirect),
        'COOCK' : ('login.py', redirect)
        }

view = LoginHtmlView()
qtype = view.gettype()
func = action[qtype]
model = LoginModel('conf')
role = func(model, **view.getparams())
arg, resp = responce[role]
resp(view, arg)
