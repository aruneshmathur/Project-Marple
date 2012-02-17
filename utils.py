#!/usr/bin/python

import os

maxsize = 2048

def stripchars(s, chars):
    return s.translate(None, chars)


def unique_elements(ele_list):
    dic = {}
    for ele in ele_list:
        dic[ele] = 1

    return dic.keys()


def list_files(path, dest_path):
    f = open(dest_path, 'w')
    get_file_list_path(os.path.abspath(path), f)
    f.close()


def get_file_list_path(path, dest_file):    
    for f in os.listdir(path):
        if f == ".svn":
            continue
        if os.path.isdir(path + '/' + f) == True:
            get_file_list_path(path + '/' + f, dest_file)
        else:
            if os.path.getsize(path + '/' + f) < maxsize:
                dest_file.write(path + '/' + f + '\n')


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
