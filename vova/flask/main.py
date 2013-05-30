#!/usr/bin/python2.7
import sys 

from flask import Flask, redirect

from model.login import LoginModel
from view.login import LoginHtmlView

app = Flask(__name__)

@app.route('/login')
        #, methods=['POST', 'GET'])
def login():
    view = LoginHtmlView()
    model = LoginModel('conf')
    login = request.args.get('login', '')
    pw = request.args.get('pw', '')
    print "accepted login", login
    if login != '':
        print 'hello'
        role = model.getRole(login, pw)
        print "role", role
        if role == "ADMIN":
            redirect(redirect(url_for('admin')))
            pass
    return view.draw(role)

@app.route('/admin')
def admin():
    return "Admin page"
if __name__ == "__main__":
    app.run(host="192.168.1.100")
