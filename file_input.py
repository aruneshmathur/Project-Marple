#!/usr/bin/python

from format_hash_winnow import hash_lines, winnow
import utils, sys
import database

name = "filename"
content = "content"
chars = " \'\";()#\n{}"
threshold = 5
k_gram = 10
window = 12

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


        hash_list = hash_lines(lines, k_gram)
        winnow_list = winnow(hash_list, window)

        db.insert_file_hash(f, winnow_list)


    final_similarity_dict = {}
    
    for f in files_list:
        hash_list = db.get_hashes(f)
        similar_to_file = {}

        for h in hash_list:
            similar_file_list = db.get_filenames(h[0], f)

            for sim in similar_file_list:
                similar_to_file[sim[0]] = similar_to_file.get(sim[0],0) + 1
                
        final_similarity_dict[f] = [x for x in similar_to_file.keys() 
                                    if similar_to_file[x] > threshold]     

     
    for k in final_similarity_dict.keys():
        print k, final_similarity_dict[k]

    db.close()



if __name__ == '__main__':
    process_files(['../a.c', '../b.c'])
