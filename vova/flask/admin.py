#!/usr/bin/python2.7
import sys 

from model.admin import AdminModel
from view.admin import AdmHtmlView

def getall(model, **params):
	return model.getAllUsers()

def adduser(model, **params):
	model.addUser(**params)
	model.commit()
	return model.getAllUsers()

def deluser(model, **params):
	model.delUser(params['id'])
	model.commit()
	return model.getAllUsers()

def search(model, **params):
	return model.searchUsers(params['pattern'])

action = {
		'add' : adduser,
		'edit' : None,
		'del' : deluser,
		'search' : search,
		'all' : getall
		}

def draw(view, data):
	view.draw(data)

def redirect(view, data):
	"""docstring for redirect"""
	view.redirect()

response = {
		'add' : redirect,
		'edit' : redirect,
		'del' : redirect,
		'search' : draw,
		'all' : draw
		}

view = AdmHtmlView()
qtype = view.gettype()
func = action[qtype]
model = AdminModel('conf')
data = func(model, **view.getparams())
response[qtype](view, data)
