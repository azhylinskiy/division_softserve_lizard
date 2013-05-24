#!/usr/bin/env python
import query as q
import MySQLdb

class LoginModel(object):
    def __init__(self):
        self.db=MySQLdb.connect(user='user', passwd='123456', db='db_cafe')
        self.cur = self.db.cursor()
        pass

    def getRole(self, login, pw):
        self.cur.execute(q.role(login, pw))
        roles = list(self.cur.fetchall())
        if len(roles) > 1:
            pass #raise dberror
        if len(roles) == 0:
            return "#ERROR"
        else:
            return roles[0][0]
