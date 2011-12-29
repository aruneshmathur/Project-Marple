#!/usr/bin/python

import format_hash_winnow
import utils

name = "filename"
content = "content"
chars = " \'\";()#"

def process_files(files_list):

    for f in files_list:
        holder = open(f, 'r')
        line_no = 0

	    lines = []

        for line in holder.read():
            line_no = line_no + 1
	        lines.append([stripchars(line, chars), line_no])


        hash_list = hash_lines(lines)
        winnow_list = winnow(hash_list)

        #record_into_database(winnow_list)
    

	    
