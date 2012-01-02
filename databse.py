#!/usr/bin/python

import MySQLdb

class Database:

    def __init__(self, db, host, user, passwd):
        self.db = db
        self.host = host
        self.user = user
        self.passwd = passwd
        self.cursor = MySQLdb.connect(host, user, passwd, db)

