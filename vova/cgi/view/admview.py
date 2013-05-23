#!/usr/bin/env python

import cgitb
import cgi
import socket

import html

class AdmHtmlView(object):
	_qtype = ""
	_params = {}
	_form = None
	def __init__(self):
		cgitb.enable()

		form = cgi.FieldStorage()
		if 'q' in form and form['q'].value == 'add':
			self._qtype = 'add'
			self._params['r'] = form['role'].value
			self._params['fn'] = form['fname'].value
			self._params['ln'] = form['lname'].value
			self._params['lg'] = form['login'].value
			self._params['tel'] = form['tel'].value
		elif 'q' in form and form['q'].value == 'edit':
			self._qtype = 'edit'
			pass
		elif 'del' in form:
			self._qtype = 'del'
			self._params['id'] = form['del'].value
		elif 'pattern' in form:
			self._qtype = 'search'
			self._params['pattern'] = form['pattern'].value
		else:
			self._qtype = 'all'

	def gettype(self):
		"""docstring for gettype"""
		return self._qtype;

	def getparams(self):
		"""docstring for getparams"""
		return self._params.copy()

	def redirect(self):
		"""Redirect to main page"""
		ipaddr = socket.gethostbyname(socket.gethostname())
		baseref = "http://%s/cgi-bin/admin.py" % ipaddr
		#print "Status: 303 See other"
		print "Location: " + baseref
		print

	def draw(self, users):
		print 'Content-type: text/html\n\n'

		ipaddr = socket.gethostbyname(socket.gethostname())
		baseref = 'http://%s/cgi-bin/admin.py' % ipaddr

		output = ''
		output += """
		<form>
		<td><input type="text" name="pattern" value="" /></td>
		<td><input type="submit" value="Search" /></td>
		</form>
		"""
		output += html.tr("<th>" + "</th><th>".join(users[0]) + "</th>")
		addform = """
		<form>
		<td><input type="text" name="role" value="WAITER" /></td>
		<td>Auto</td>
		<td><input type="text" name="fname" value="" /></td>
		<td><input type="text" name="lname" value="" /></td>
		<td><input type="text" name="login" value="" /></td>
		<td><input type="text" name="tel" value="+380" /></td>
		<td><input type="submit" value="Add" /></td>
		<input type="hidden" name="q" value="add"> 
		</form>
		"""
		output += html.tr(addform)
		baseref
		for user in users[1:]:
			ref = baseref + '?del=%d' % user[1]
			user += html.a(ref, 'del'),
			output += html.tr("<td>" + "</td><td>".join([str(x) for x in user]) + "</td>")
	 
		print html.doc(html.table(output))

