#!/usr/bin/env python
import query as q
from model import Model

class LoginModel(Model):
    def __init__(self, conf):
        super(LoginModel, self).__init__(conf)

    def getRole(self, login, pw):
        self.cur.execute(q.role(login, pw))
        roles = list(self.cur.fetchall())
        if len(roles) > 1:
            pass #raise dberror
        if len(roles) == 0:
            return "#ERROR"
        else:
            return roles[0][0]
