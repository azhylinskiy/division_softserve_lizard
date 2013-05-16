#!/usr/bin/python2.7
import sys 
import MySQLdb
import cgitb
import cgi

cgitb.enable()

def html_p(text):
    return '<p>%s</a>' % text

def html_a(ref, text):
    return '<a href=%s>%s</a>' % (ref, text)

def html_doc(body):
	return """<!DOCTYPE html>
		<html>
		<body>
		%s
		</body>
		</html>""" % body

def html_table(data):
	return """<table border="1">
		%s
		</table>""" % data

def html_tr(row):
		return "<tr>%s</tr>" % row


db=MySQLdb.connect(user='user', passwd='123456', db='db_cafe')

cur = db.cursor()
q_select_all = """
SELECT role_name, id_user, user_first_name, user_last_name, user_login, user_tel 
FROM tbl_users INNER JOIN tbl_roles ON tbl_users.user_role = tbl_roles.id_role
"""

def q_ins_user(fn, ln, lg, pw, r, tel):
	q_role = "select id_role from tbl_roles where role_name = %s" % r
	return """
		INSERT INTO `tbl_users`(`user_first_name`, `user_last_name`, `user_login`, `user_password`, `user_role`, `user_tel`)
		VALUES (%s, %s, %s, %s, %s, %s)
		""" % (fn, ln, lg, pw, q_role, tel)
 
q_del_i = """
DELETE FROM `tbl_users`
WHERE id_user = %d
"""

class AdminModel(object):
	def __init__(self):
		pass

	def getAllUsers(self):
		cur.execute(q_select_all)
		return cur.fetchall()

	def addUsers(self, fn, ln, lg, pw, r, tel):
		query = q_ins_user(fn, ln, lg, pw, r, tel)
		cur.execute(query)

	def delUsers(self, i):
		cur.execute(q_del_i % i)

def list():
    model = AdminModel()
    users = model.getAllUsers()
 
    output = ''
    for user in users:
        ref = 'http://192.168.1.103/cgi-bin/admin.py?del=%d' % user[1]
        user += html_a(ref, 'del'),
        output += html_tr("<td>" + "</td><td>".join([str(x) for x in user]) + "</td>")
 
    return html_table(output)

print 'Content-type: text/html\n\n'
ref = 'http://192.168.1.103/cgi-bin/script.py'
html = ""
#html += html_p(html_a(ref, '<H1></H1>'))
form = cgi.FieldStorage()
html += list()
print html_doc(html)

#if 'g' not in form:
#    html += list()
#else:
#    html += menu(form['g'].value)

#    output = ''
#    for x in rows:
#        ref = 'http://192.168.1.103/cgi-bin/script.py?g=%d' % x[0]
#        output += html_p(html_a(ref, x[1]))
