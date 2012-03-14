#!/usr/bin/python

from format_hash_winnow import hash_kgrams, winnow
import utils, sys, os, comparison, html_dumper, database, yaml


name = "filename"
content = "content"
chars = " \'\";()#\n{}-*|=/"
threshold = 00
k_gram = 50
w_window = 100

def compare(db, except_file, not_like):

    hash_list = db.get_hashes(except_file)
    utils.log("Got it's hashes")
    similar = {}

    if not_like is not None:
        except_file = None

    for h in hash_list:
        utils.log("Hash " +str(h))

        for sim in db.get_filenames(h, except_file, not_like):
            similar[sim] = similar.get(sim,0) + 1

                
    return [x for x in similar.keys() 
            if similar[x] > threshold]     


def process(file_path):
        lines = ""
        for line in open(file_path, 'r'):
            lines = lines + utils.stripchars(line, chars)

        hash_list = hash_kgrams(lines, k_gram)

        if hash_list is None:
            return None

        winnow_list = winnow(hash_list, w_window)

        return winnow_list


def process_files(files_yaml, ignore_files_yaml):

    db = database.WinnowDB()
    db.clear()
    db.setup()
    db.add_index()

    #log = 0
    #size = len(ignore_file_list)
    utils.log("Starting to hash Ignore files.")

    for f in yaml.load_all(open(ignore_files_yaml, 'r')):
        
        #sys.stdout.write("\rHashing Ignore files.......%d%%" % ((100 * log) / size))
        #sys.stdout.flush()
        #log = log + 1

        res = process(f)
        if res is not None:
            db.insert_ignore_list(res)

    utils.log("Done hashing Ignore files.")

    #sys.stdout.write("\rHashing Ignore files.......Done\n")
    #sys.stdout.flush()
    
    #log = 0
    #size = len(files_list)

    utils.log("Starting to hash Project files.")

    for ele in yaml.load_all(open(files_yaml, 'r')):

        #sys.stdout.write("\rHashing files.......%d%%" % ((100 * log) / size))
        #sys.stdout.flush()
        #log = log + 1

        if type(ele) is dict:
            for f in ele[utils.files]:
                res = process(f)
                if res is not None:
                    db.insert_file_hash(f, ele[utils.folder], res)
                    utils.log("Hashed "+ f)

        elif type(ele) is str:
            res = process(ele)

            if res is not None:
                db.insert_file_hash(ele, None, res)
                utils.log("Hashed " + ele)



    utils.log("Done hashing Project files.")
    #sys.stdout.write("\rHashing files.......Done\n")
    #sys.stdout.flush

    sim_dict = {}
    
    for ele in yaml.load_all(open(files_yaml, 'r')):

        if type(ele) is dict:
            for f in ele[utils.files]:
                utils.log("Looking for files similar to " + f)
                sim_dict[f] = compare(db, f, ele[utils.folder])
                utils.log("Done looking.")


        elif type(ele) is str:
            utils.log("Looking for files similar to " + ele)
            sim_dict[ele] = compare(db, ele, None)
            utils.log("Done looking.")  
     
    #db.close()

    return sim_dict



if __name__ == '__main__':


    files_yaml = "list.yaml"
    ignore_files_yaml = "ignore.yaml"

    output_dict = os.path.abspath("/home/aruneshmathur/major-project/Projects/output")

    sim_dict = process_files(files_yaml, ignore_files_yaml)

    utils.log("Done comparing, generating output now.")


    for k in sim_dict.keys():
        a = {}
        (a[comparison.text], a[comparison.line_no]) = utils.file_contents_line_numbers(k, chars)

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
            (b[comparison.text], b[comparison.line_no]) = utils.file_contents_line_numbers(f, chars)

            res = comparison.LCS(a, b, threshold)
            result = {
                comparison.file_names : [k, f],
                comparison.match_lines : res
            }

            html_dumper.dump_to_HTML(result, path)

    utils.log("Done!")

