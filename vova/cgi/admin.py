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
	q_role = "select id_role from tbl_roles where role_name = '%s'" % r
	return """
		INSERT INTO `tbl_users`(`user_first_name`, `user_last_name`, `user_login`, `user_password`, `user_role`, `user_tel`)
		VALUES ('%s', '%s', '%s', '%s', (%s), '%s')
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
        columns = [desc[0] for desc in cur.description]
        users = list(cur.fetchall())
        users.insert(0, columns)
        return users

    def addUsers(self, fn, ln, lg, pw, r, tel):
        query = q_ins_user(fn, ln, lg, pw, r, tel)
        cur.execute(query)

    def delUsers(self, i):
        cur.execute(q_del_i % i)

def gen_html():
    model = AdminModel()
    form = cgi.FieldStorage()
    if 'login' in form:
        r = form['role'].value
        fn = form['fname'].value
        ln = form['lname'].value
        lg = form['login'].value
        tel = form['tel'].value
        pw = '1111'
        model.addUsers(fn, ln, lg, pw, r, tel)
        db.commit()
    users = model.getAllUsers()
 
    output = ''
    output += html_tr("<th>" + "</th><th>".join(users[0]) + "</th>")
    addform = """
    <form>
    <td><input type="text" name="role" value="WAITER" /></td>
    <td>Auto</td>
    <td><input type="text" name="fname" value="" /></td>
    <td><input type="text" name="lname" value="" /></td>
    <td><input type="text" name="login" value="" /></td>
    <td><input type="text" name="tel" value="+380" /></td>
    <td><input type="submit" value="Add" /></td>
    </form>
    """
    output += html_tr(addform)
    for user in users[1:]:
        ref = 'http://192.168.1.103/cgi-bin/admin.py?del=%d' % user[1]
        user += html_a(ref, 'del'),
        output += html_tr("<td>" + "</td><td>".join([str(x) for x in user]) + "</td>")
 
    return html_table(output)

print 'Content-type: text/html\n\n'
ref = 'http://192.168.1.103/cgi-bin/script.py'
html = ""
#html += html_p(html_a(ref, '<H1></H1>'))
form = cgi.FieldStorage()
html += gen_html()
print html_doc(html)


#    output = ''
#    for x in rows:
#        ref = 'http://192.168.1.103/cgi-bin/script.py?g=%d' % x[0]
#        output += html_p(html_a(ref, x[1]))
