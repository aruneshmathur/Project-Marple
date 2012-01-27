#!/usr/bin/python

import os

def stripchars(s, chars):
    return s.translate(None, chars)


def unique_elements(ele_list):
    dic = {}
    for ele in ele_list:
        dic[ele] = 1

    return dic.keys()

def list_files(path, dest_path):
    f = open(dest_path, 'a')
    get_file_list_path(path, f)
    f.close()

def get_file_list_path(path, dest_file):    
    for f in os.listdir(path):
        if os.path.isdir(path + '/' + f) == True:
            get_file_list_path(path + '/' + f, dest_file)
        else:
            dest_file.write(path + '/' + f + '\n')


