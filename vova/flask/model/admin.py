#!/usr/bin/env python
import query as q
import MySQLdb
import ConfigParser

class Model(object):
    def __init__(self, conf):
        config = ConfigParser.SafeConfigParser()
        config.read(conf)

        db = config.get('mysql', 'db')
        user = config.get('mysql', 'user')
        passwd = config.get('mysql', 'passwd')

        self.db=MySQLdb.connect(user=user, passwd=passwd, db=db)
        self.cur = self.db.cursor()

class AdminModel(Model):
    def __init__(self, conf):
        super(AdminModel, self).__init__(conf)

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

    def addUser(self, fn, ln, lg, r, tel):
        pw = '1234'
        query = q.insert(fn, ln, lg, pw, r, tel)
        self.cur.execute(query)

    def delUser(self, i):
        self.cur.execute(q.delete(i))

    def commit(self):
        self.db.commit()
