#!/usr/bin/python

from format_hash_winnow import hash_lines, winnow
import utils, sys
import database

name = "filename"
content = "content"
chars = " \'\";()#\n{}"
threshold = 10

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

        db.insert_file_hash(f, winnow_list)

    
    for f in file_list:
        hash_list = get_hashes(f)
        similar_to_this_file = {}

        for h in hash_list:
            similar_file_list = get_filenames(h[0])

            for sim in similar_file_list:
                similar_to_this_file[sim[0]] =
                similar_to_this_file.get(sim[0],0) + 1



        
    db.close()

if __name__ == '__main__':
    process_files(['a.txt']);
