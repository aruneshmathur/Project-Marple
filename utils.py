#!/usr/bin/python

import os, yaml

maxsize = 4096
ignore_dirs=[".svn", ".git", ".hg", ".gitignore"]

folder="DIR"
files="FILES"

yaml_sep = "---"

def stripchars(s, chars):
    return s.translate(None, chars)


def unique_elements(ele_list):
    dic = {}
    for ele in ele_list:
        dic[ele] = 1

    return dic.keys()


def record_files(path, dest_path, compare = False):
    
    stream = open(dest_path, 'a')
    path = os.path.abspath(path)
    
    for ele in os.listdir(path):
        innerpath = path + '/' + ele
        if os.path.isdir(innerpath):

            dirlist = get_subdirs(innerpath)

            if compare is False:
                datadir = {
                    folder:innerpath, 
                    files:dirlist
                }
                
                stream.write(yaml_sep + '\n')
                yaml.dump(datadir, stream)

            else:
                for e in dirlist:
                    stream.write(yaml_sep + '\n')
                    yaml.dump(e, stream)

        else:
            stream.write(yaml_sep + '\n')
            yaml.dump(innerpath, stream)

    stream.close()


def get_subdirs(path):  

    returnlist = []
    for f in os.listdir(path):
        if f in ignore_dirs:
            continue

        innerpath = path + '/' + f
        if os.path.isdir(innerpath) == True:
           returnlist.extend(get_subdirs(innerpath))
       
        else:
            if os.path.getsize(innerpath) < maxsize:
                returnlist.append(innerpath)
    
    return returnlist
            

def get_matrix(*shape):
    if len(shape) == 0:
        return 0

    car = shape[0]
    cdr = shape[1:]

    return [get_matrix(*cdr) for i in range(car)]


def file_contents_line_numbers(filename):

    i = 1
    line_content = ""
    line_numbers = []

    for line in open(filename, 'r'):
        line = stripchars(line, " \n	")    
        line_content = line_content + line
	line_numbers.extend([i for char in line])
        i = i + 1    
     
    return (line_content, line_numbers)

def log(string):
    print string
