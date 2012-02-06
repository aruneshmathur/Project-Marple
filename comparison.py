#!/usr/bin/python

import string, utils, html_dumper

text = "TEXT"
line_no = "LINE_NO"
lines1 = "LINES1"
lines2 = "LINES2"
file_names = "FILENAMES"
match_lines = "MATCH_LINES"

threshold = 30


def LCS(text_dict1, text_dict2, min_length):
    
    if not (text_dict1.has_key(text) and text_dict2.has_key(text)):
        return None

    if not (text_dict1.has_key(line_no) and text_dict2.has_key(line_no)):
        return None

    str1 = text_dict1[text]
    str2 = text_dict2[text]

    m = len(str1)
    n = len(str2)

    c = utils.get_matrix(m + 1, n + 1)

    res = ""

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                c[i][j] = c[i-1][j-1] + 1

            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

    return LCS_string(c, text_dict1, text_dict2, min_length)


def LCS_string(c, text_dict1, text_dict2, min_length):

    str1 = text_dict1[text]
    str2 = text_dict2[text]

    i = len(str1) 
    j = len(str2)

    str_lines1 = text_dict1[line_no]
    str_lines2 = text_dict2[line_no]

    res = cur_str = ""
    res_line1 = [] 
    cur_line1 = []
    res_line2 = []
    cur_line2 = []

    while i != 0 and j != 0:
        if(str1[i-1] == str2[j-1]):
            cur_str = cur_str + str1[i-1]
            cur_line1.append(str_lines1[i-1])
            cur_line2.append(str_lines2[j-1])
            i = i-1
            j = j-1

        else:

            if len(cur_str) >= threshold:
                res = res + cur_str
                res_line1.append(cur_line1)
                res_line2.append(cur_line2)
            
            cur_str = ""
            cur_line1 = []
            cur_line2 = []

            if c[i][j-1] > c[i-1][j]:
                j = j-1

            else:
                i = i-1


    res_line1.append(cur_line1)
    res_line2.append(cur_line2)

    return {
        lines1 : [sorted(utils.unique_elements(x)) for x in res_line1], 
        lines2 : [sorted(utils.unique_elements(x)) for x in res_line2]
    }
    #return res + cur_str


if __name__=='__main__':
    
    a = {}
    b = {}

    (a[text], a[line_no]) = utils.file_contents_line_numbers('a.txt')
    (b[text], b[line_no]) = utils.file_contents_line_numbers('b.txt')

    
    res = LCS(a, b, threshold)

    result = {
        file_names : ['a.txt', 'b.txt'],
        match_lines : res
    }

    html_dumper.dump_to_HTML(result, "")

