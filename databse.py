#!/usr/bin/python

import MySQLdb

cursor = None

def connect_to_db(db, host, user, passwd):
    conn = MySQLdb.connect(host, user, passwd, db)


create_table()
