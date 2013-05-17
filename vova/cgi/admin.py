#!/usr/bin/python2.7
import sys 
import cgitb
import cgi
import socket

from adm import AdminModel
import html

cgitb.enable()

def gen_html():
    model = AdminModel()
    form = cgi.FieldStorage()
    users = []
    if 'q' in form and form['q'].value == 'add':
        r = form['role'].value
        fn = form['fname'].value
        ln = form['lname'].value
        lg = form['login'].value
        tel = form['tel'].value
        pw = '1111'
        model.addUser(fn, ln, lg, pw, r, tel)
        model.commit()
    elif 'q' in form and form['q'].value == 'edit':
        pass
        model.commit()
    elif 'del' in form:
        model.delUser(form['del'].value)
        model.commit()
    elif 'pattern' in form:
        users = model.searchUsers(form['pattern'].value)

    if users == []:
        users = model.getAllUsers()
 
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
    global baseref
    for user in users[1:]:
        ref = baseref + '?del=%d' % user[1]
        user += html.a(ref, 'del'),
        output += html.tr("<td>" + "</td><td>".join([str(x) for x in user]) + "</td>")
 
    return html.table(output)

print 'Content-type: text/html\n\n'

ipaddr = socket.gethostbyname(socket.gethostname())
baseref = 'http://%s/cgi-bin/admin.py' % ipaddr
form = cgi.FieldStorage()

print html.doc(gen_html())
