#!/usr/bin/python

import MySQLdb
import warnings

from DB_settings import *

warnings.filterwarnings("ignore", "Unknown table.*")

file_path_key = "FILE_PATH"

class Database:

    def __init__(self):
        self.db = "marple"
        self.host = "localhost"
        self.user = "root"
        self.passwd = DATABASE_PASSWORD
        self.cursor = MySQLdb.connect("localhost", "root", self.passwd,
                                      self.db).cursor()

        self.table1 = "FILE_NAMES"
        self.table2 = "WINNOWED"


    def clear(self):

        self.cursor.execute("DROP TABLE IF EXISTS " + self.table1)
        self.cursor.execute("DROP TABLE IF EXISTS " + self.table2)

        return

    def setup(self):
        self.cursor.execute("CREATE TABLE " + self.table1 + 
                            "(" + file_path_key + " varchar(100) PRIMARY KEY);")

if __name__ == "__main__":

    db = Database()
    db.clear()
    db.setup()
