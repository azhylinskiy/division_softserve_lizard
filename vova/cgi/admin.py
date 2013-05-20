#!/usr/bin/python2.7
import sys 

from model.adm import AdminModel
from view.admview import AdmHtmlView

def getall(model, **params):
	return model.getAllUsers()

def adduser(model, **params):
	model.addUser(**params)
	model.commit()
	return model.getAllUsers()

def deluser(model, **params):
	model.delUser(params['id'].value)
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

view = AdmHtmlView()
func = action[view.gettype()]
model = AdminModel()
users = func(model, **view.getparams())
view.draw(users)
