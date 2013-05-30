#!/usr/bin/env python
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
