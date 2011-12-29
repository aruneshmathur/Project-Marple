#!/usr/bin/python

def stripchars(s, chars):
    return s.translate(None, chars)


def unique_elements(ele_list):
    dic = {}
    for ele in ele_list:
        dic[ele] = 1

    return dic.keys()
