#!/usr/bin/python

from format_hash_winnow import hash_lines, winnow
import utils, sys
import database

name = "filename"
content = "content"
chars = " \'\";()#\n{}"

def process_files(files_list):

    db = database.WinnowDB()
    db.clear()
    db.setup()

    for f in files_list:
        holder = open(f, 'r')

        line_no = 0
        
        lines = []

        for line in holder:
            line_no = line_no + 1
            lines.append([utils.stripchars(line, chars), line_no])


        hash_list = hash_lines(lines)
        winnow_list = winnow(hash_list, 12)

        #for win in winnow_list:
            #sys.stdout.write(str(win[0]) + " in lines " + str(win[1]) + "\n")

        db.insert_file_hash(f, winnow_list)
        
    db.close()

if __name__ == '__main__':
    process_files(['large.txt']);
