#!/usr/bin/env python
import query as q
import MySQLdb

class AdminModel(object):
    def __init__(self):
        self.db=MySQLdb.connect(user='user', passwd='123456', db='db_cafe')   
        self.cur = self.db.cursor()
        pass

    def getAllUsers(self):
        self.cur.execute(q.selectall())
        columns = [desc[0] for desc in self.cur.description]
        users = list(self.cur.fetchall())
        users.insert(0, columns)
        return users

    def searchUsers(self, pattern):
        self.cur.execute(q.search(pattern))
        columns = [desc[0] for desc in self.cur.description]
        users = list(self.cur.fetchall())
        users.insert(0, columns)
        return users

    def addUser(self, fn, ln, lg, pw, r, tel):
        query = q.insert(fn, ln, lg, pw, r, tel)
        self.cur.execute(query)

    def delUser(self, i):
        self.cur.execute(q.delete(i))

    def commit(self):
        self.db.commit()
