#!/usr/bin/python

import string, utils

text = "TEXT"
line_no = "LINE_NO"
threshold = 10


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

    return LCS_string(c, str1, str2, min_length)


def LCS_string(c, str1, str2, min_length):

    i = len(str1) 
    j = len(str2)

    res = ""
    cur_str = ""

    while i != 0 and j != 0:
        if(str1[i-1] == str2[j-1]):
            cur_str = cur_str + str1[i-1]
            i = i-1
            j = j-1

        else:

            if len(cur_str) >= threshold:
                res = res + cur_str
            
            cur_str = ""

            if c[i][j-1] > c[i-1][j]:
                j = j-1

            else:
                i = i-1

    return res + cur_str


if __name__=='__main__':
    
    a = {}
    b = {}

    (a[text], a[line_no]) = utils.file_contents_line_numbers('a.txt')
    (b[text], b[line_no]) = utils.file_contents_line_numbers('b.txt')

    
    res = LCS(a, b, threshold)
    print res[::-1]

