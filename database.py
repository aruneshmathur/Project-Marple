#!/usr/bin/python

import MySQLdb
import warnings

from DB_settings import *

warnings.filterwarnings("ignore", "Unknown table.*")

file_path_key = "FILE_PATH"
hash_key = "HASH"
ignore_key = "IGNOREH"

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
        self.table3 = "IGNORE_HASHES"

    def clear(self):

        self.cursor.execute("DROP TABLE IF EXISTS " + self.table2)
        self.cursor.execute("DROP TABLE IF EXISTS " + self.table1)
        self.cursor.execute("DROP TABLE IF EXISTS " + self.table3)


    def setup(self):
        self.cursor.execute("CREATE TABLE " + self.table1 + 
                            "(" + file_path_key + " VARCHAR(500), PRIMARY KEY("+
                            file_path_key+ ")) ENGINE=INNODB;")

        self.cursor.execute("CREATE TABLE " + self.table2 + "(" + 
                            file_path_key + " VARCHAR(500) NOT NULL, " +
                            hash_key + " BIGINT(20) NOT NULL, " +
                            "FOREIGN KEY (" + file_path_key + ") REFERENCES " +
                            self.table1 + "(" + file_path_key + ") ON UPDATE CASCADE ON DELETE CASCADE) ENGINE=INNODB;" )


        self.cursor.execute("CREATE TABLE " + self.table3 + 
                            "(" + ignore_key + " BIGINT(20), PRIMARY KEY("+
                            ignore_key+ ")) ENGINE=INNODB;")


    def insert_ignore_list(self, winnow_list):
        for w in winnow_list:
            #self.cursor.execute("INSERT IGNORE INTO " + self.table3 + " VALUES('" +
            #                    str(w) + "');")

            self.cursor.execute("""INSERT IGNORE INTO """ + self.table3  + """ VALUES(%s);""",
                                (w))

            self.conn.commit()


    def insert_file_hash(self, name, winnow_list):
        #self.cursor.execute("INSERT INTO " + self.table1 + " VALUES('" + name +
        #                    "');")

        self.cursor.execute("""INSERT INTO """ + self.table1  + """ VALUES(%s);""", (name))

        self.conn.commit()

        for w in winnow_list:

            #self.cursor.execute("INSERT INTO " + self.table2 + " VALUES('" +
            #                   name + "', " + str(w) + ");")

            self.cursor.execute("""INSERT INTO """ + self.table2  + """ VALUES(%s, %s);""",
                                (name, w))

            self.conn.commit()


    def get_filenames(self, hash_value, except_file, not_like):

        result_set = []
        add_q = ""

        if not_like is not None:
            self.cursor.execute("""SELECT DISTINCT """ + file_path_key +
                                """ FROM """ + self.table2 + """ WHERE """ +
                                hash_key + """ = %s AND """ + file_path_key +
                                """NOT LIKE %s%;""", (hash_value, not_like))

            #add_q = " AND " + file_path_key + " NOT LIKE '" + not_like + "%'"

        else:
            self.cursor.execute("""SELECT DISTINCT """ + file_path_key +
                                """ FROM """ + self.table2 + """ WHERE """ +
                                hash_key + """ = %s;""", (hash_value))
            

        #self.cursor.execute("SELECT DISTINCT " + file_path_key +
        #                    " FROM " + self.table2 + " WHERE " + hash_key + " = "
        #                    + str(hash_value) + add_q + ";")

        #self.cursor.execute("""SELECT DISTINCT """ + file_path_key +
        #                    """ FROM """ + self.table2 + """ WHERE """ +
        #                    hash_key + """ = %s;""", (hash_value))


        for row in self.cursor:
            if row[0] != except_file:
               result_set.append(row[0])

        return result_set


    def get_hashes(self, file_name):

        result_set = []

        #self.cursor.execute("SELECT " + hash_key + " FROM " + self.table2 + " WHERE " + file_path_key + 
        #                    " = '" + file_name + "' AND " +  hash_key + " NOT IN (SELECT * FROM " + self.table3 + ");")

        self.cursor.execute("""SELECT """ + hash_key + """ FROM """ +
                            self.table2 + """ WHERE """ + file_path_key + 
                            """ = %s AND """ +  hash_key + """ NOT IN (SELECT *
                            FROM """ + self.table3 + """);""", (file_name))

        for row in self.cursor:
            result_set.append(row[0])

        return result_set


    def close(self):
        self.cursor.close()



