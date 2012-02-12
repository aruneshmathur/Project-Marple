#!/usr/bin/python

from format_hash_winnow import hash_lines, winnow, hash_ignore_lines, winnow_ignore
import utils, sys, os, comparison, html_dumper, database


name = "filename"
content = "content"
chars = " \'\";()#\n{}-*|=/"
threshold = 40
k_gram = 50
window = 100

def process_files(files_list, ignore_file_list):

    db = database.WinnowDB()
    db.clear()
    db.setup()

    for f in ignore_file_list:

        lines = ""
        for line in open(f, 'r'):
            lines = lines + utils.stripchars(line, chars)

        hash_list = hash_ignore_lines(lines, k_gram)

        if hash_list is None:
            continue

        winnow_list = winnow_ignore(hash_list, window)

        db.insert_ignore_list(winnow_list)


    for f in files_list:

        print f

        holder = open(f, 'r')

        line_no = 0
        
        lines = []

        for line in holder:
            line_no = line_no + 1
            lines.append([utils.stripchars(line, chars), line_no])

        
        hash_list = hash_lines(lines, k_gram)

        if hash_list is None:
            print f + " is empty?"
            continue

        winnow_list = winnow(hash_list, window)

        db.insert_file_hash(f, winnow_list)



    final_similarity_dict = {}
    
    for f in files_list:

        hash_list = db.get_hashes(f)
        similar_to_file = {}

        for h in hash_list:
            similar_file_list = db.get_filenames(h[0], f)

            for sim in similar_file_list:
                similar_to_file[sim] = similar_to_file.get(sim,0) + 1
                
        final_similarity_dict[f] = [x for x in similar_to_file.keys() 
                                    if similar_to_file[x] > threshold]     

     
    #db.close()

    return final_similarity_dict



if __name__ == '__main__':


    file_list = [x.rstrip('\n') for x in open("list.txt", "r")]
    ignore_file_list = [x.rstrip('\n') for x in open("ignore.txt", "r")]


    output_dict = os.path.abspath("/home/aruneshmathur/major-project/Projects/output/")

    sim_dict = process_files(file_list, ignore_file_list)


    for k in sim_dict.keys():
        print k, sim_dict[k]


    for k in sim_dict.keys():
        a = {}
        (a[comparison.text], a[comparison.line_no]) = utils.file_contents_line_numbers(k)

        for f in sim_dict[k]:
            start = ""
            end = ""
            if k < f:
                start = k
                end = f
            else:
                start = f
                end = k

            path = output_dict + "/" + str(abs(hash(start + end)))
            if os.path.exists(path):
                continue
            else:
                os.makedirs(path)


            b = {}
            (b[comparison.text], b[comparison.line_no]) = utils.file_contents_line_numbers(f)

            res = comparison.LCS(a, b, threshold)
            result = {
                comparison.file_names : [k, f],
                comparison.match_lines : res
            }

            html_dumper.dump_to_HTML(result, path)

