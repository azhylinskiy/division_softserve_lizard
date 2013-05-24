#!/usr/bin/env python

import cgitb
import cgi
import socket

import html

class LoginHtmlView(object):
    _qtype = ""
    _params = {}
    def __init__(self):
        cgitb.enable()

        form = cgi.FieldStorage()
        if 'login' in form:
            self._qtype = 'login'
            self._params['login'] = form['login'].value
            self._params['pw'] = form['pw'].value
        else:
            self._qtype = 'view'

    def gettype(self):
        """docstring for gettype"""
        return self._qtype;

    def getparams(self):
        """docstring for getparams"""
        return self._params.copy()

    def redirect(self, place):
        """Redirect to main page"""
        ipaddr = socket.gethostbyname(socket.gethostname())
        baseref = "http://%s/cgi-bin/%s" % (ipaddr, place)
        #print "Status: 303 See other"
        print "Location: " + baseref
        print

    def draw(self, data):
        print 'Content-type: text/html\n\n'

        ipaddr = socket.gethostbyname(socket.gethostname())
        baseref = 'http://%s/cgi-bin/admin.py' % ipaddr

        output = ''
        if data == "#ERROR":
            output += "<h3>Error: invalid login or password</h3>"
        loginform = """
        <form>
        <p><input type="text" name="login" value="" /></p>
        <p><input type="text" name="pw" value="" /></p>
        <p><input type="submit" value="Login" /></p>
        </form>
        """
        output += html.tr(loginform)
        print html.doc(html.table(output))

