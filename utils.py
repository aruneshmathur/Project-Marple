#!/usr/bin/python

import os, yaml

maxsize = 2048
ignore_dirs=[".svn", ".git", ".hg", ".gitignore"]
ignore_ext=[".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pps", ".ppsx",
            ".pptx", ".bmp", ".png", ".gif", ".jpeg", ".jpg", ".bin", ".exe",
            ".html", ".o", ".pyc", ".class", ".ico", ".mp3", ".avi", ".mkv",
            ".wav", ".flv", ".mpg", ".mpeg", ".wma", ".3gp", ".mp4", ".ogg",
            ".svg", ".htm", ".vcproj", ".vcxproj", ".cache", ".fnt", ".fon",
            ".otf", ".ttf"]

folder="DIR"
files="FILES"

yaml_sep = "---"

def check_url(url):

    try:
        url.decode('ascii')
    except UnicodeDecodeError:
        return False


    for ext in ignore_ext:
        if url.lower().endswith(ext):
            return False

    return True


def stripchars(s, chars):
    return s.translate(None, chars).lower()


def unique_elements(ele_list):
    dic = {}
    for ele in ele_list:
        dic[ele] = 1

    return dic.keys()


def record_files(path, dest_path, compare = False):

    stream = open(dest_path, "a+")
    path = os.path.abspath(path)

    file_count = 0

    for ele in os.listdir(path):
        innerpath = path + '/' + ele
        if os.path.isdir(innerpath):

            dirlist = get_subdirs(innerpath)
            file_count = file_count + len(dirlist)

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
        
            if check_url(innerpath):
                stream.write(yaml_sep + '\n')
                yaml.dump(innerpath, stream)
                file_count = file_count + 1

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
            if os.path.getsize(innerpath) < maxsize and check_url(innerpath):
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
