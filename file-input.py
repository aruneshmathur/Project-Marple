#!/usr/bin/python

import format_hash_winnow

def process_files(files_list):

    for f in files_list:
        holder = open(f, 'r')
        line_no = 0
        for line in holder.read():
            line_no = line_no + 1
            winnow_list = winnow(gen_hash_list([line, line_no])
	    
