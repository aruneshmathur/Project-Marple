#!/usr/bin/python

import MySQLdb
import warnings

from DB_settings import *

warnings.filterwarnings("ignore", "Unknown table.*")

file_path_key = "FILE_PATH"
hash_key = "HASH"
lines_key = "LINE_NO"

class WinnowDB:

    def __init__(self):
        self.db = "marple"
        self.host = "localhost"
        self.user = "root"
        self.passwd = DATABASE_PASSWORD
        self.conn = MySQLdb.connect("localhost", "root", self.passwd,
                                      self.db)
        self.cursor = self.conn.cursor()

        self.table1 = "FILE_NAMES"
        self.table2 = "WINNOWED_HASHES"


    def clear(self):

        self.cursor.execute("DROP TABLE IF EXISTS " + self.table2)
        self.cursor.execute("DROP TABLE IF EXISTS " + self.table1)


    def setup(self):
        self.cursor.execute("CREATE TABLE " + self.table1 + 
                            "(" + file_path_key + " VARCHAR(100), PRIMARY KEY("+
                            file_path_key+ ")) ENGINE=INNODB;")

        self.cursor.execute("CREATE TABLE " + self.table2 + "(" + 
                            file_path_key + " VARCHAR(100) NOT NULL, " +
                            hash_key + " BIGINT(20) NOT NULL, " +
                            lines_key + " INTEGER NOT NULL, " +
                            "FOREIGN KEY (" + file_path_key + ") REFERENCES " +
                            self.table1 + "(" + file_path_key + ") ON UPDATE CASCADE ON DELETE CASCADE) ENGINE=INNODB;" );


    def insert_file_hash(self, name, winnow_list):
        self.cursor.execute("INSERT INTO " + self.table1 + " VALUES('" + name +
                            "');")

        for w in winnow_list:
            for line_no in w[1]:
                self.cursor.execute("INSERT INTO " + self.table2 + " VALUES('" +
                                    name + "', " + str(w[0]) + ", " +
                                    str(line_no) +");")

                self.conn.commit()


    def get_filenames(hash_value):

        result_set = []
        self.cursor.execute("SELECT " + file_path_key + ", " + lines_key +
                            "FROM " + self.table2 + " WHERE " + hash_key + " = "
                            + hash_value + ";")

        for row in self.cursor:
            result_set.append(row[0], row[1])

        return result_set


    def get_hashes(file_name):

        result_set = []
        self.cursor.execute("SELECT " + hash_key + ", " + lines_key + "FROM " +
                            self.table2 + " WHERE " + file_path_key + " = " +
                            hash_value + ";")

        for row in self.cursor:
            result_set(row[0], row[1])

        return result_set


    def close(self):
        self.cursor.close()



