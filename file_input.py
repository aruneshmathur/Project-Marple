#!/usr/bin/python

from format_hash_winnow import hash_lines, winnow
import utils

name = "filename"
content = "content"
chars = " \'\";()#\n"

def process_files(files_list):

    for f in files_list:
        holder = open(f, 'r')

        line_no = 0
        
        lines = []

        for line in holder:
            line_no = line_no + 1
            lines.append([utils.stripchars(line, chars), line_no])


        hash_list = hash_lines(lines)
        winnow_list = winnow(hash_list, 12)

        print len(winnow_list)

        #record_into_database(winnow_list)
    

if __name__ == '__main__':
    process_files(['a.txt']);
