#!/usr/bin/python

import string, utils

text = "TEXT"
line_no = "LINE_NO"
threshold = 20


def longest_common_substring(text_dict1, text_dict2):
    if not (text_dict1.has_key(text) and text_dict2.has_key(text)):
        return None

    if not (text_dict1.has_key(line_no) and text_dict2.has_key(line_no)):
        return None

    str1 = text_dict1[text]
    str2 = text_dict2[text]

    m = len(str1)
    n = len(str2)

    result = []
    x_longest, longest = 0, 0

    c = utils.get_matrix(m, n)

    for i in range(0, m):
        for j in range(0, n):
            if str1[i] == str2[j]:
                c[i][j] = c[i-1][j-1] + 1

                if c[i][j] > longest:
                    longest = c[i][j]
                    x_longest = i

            else:
                c[i][j] = 0

    return str1[x_longest - longest + 1: x_longest + 1]


if __name__=='__main__':
    
    a = {}
    b = {}

    (a[text], a[line_no]) = utils.file_contents_line_numbers('a.txt')
    (b[text], b[line_no]) = utils.file_contents_line_numbers('b.txt')

    res = longest_common_substring(a, b)

    while len(res) > threshold:
        print res

        a[text] = string.replace(a[text], res, "")
        b[text] = string.replace(b[text], res, "")
        res = longest_common_substring(a, b)

