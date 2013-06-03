#!/usr/bin/python2.7
import sys 

from flask import Flask, redirect, request, url_for

from model.login import LoginModel
from view.login import LoginHtmlView

from model.admin import AdminModel
from view.admin import AdmHtmlView

app = Flask(__name__)

@app.route('/login')
def login():
    view = LoginHtmlView()
    model = LoginModel('conf')
    login = request.args.get('login', '')
    pw = request.args.get('pw', '')
    role = "#NO"
    if login != '':
        role = model.getRole(login, pw)
        if role == "ADMIN":
            return redirect(url_for('admin'))
    return view.draw(role)

@app.route('/udel')
def udel():
    view = AdmHtmlView()
    id = request.args.get('id', '')
    model = AdminModel('conf')
    model.delUser(id)
    model.commit()
    return redirect(url_for('admin'))

@app.route('/admin')
def admin():
    view = AdmHtmlView()
    model = AdminModel('conf')
    return view.draw(model.getAllUsers())

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
