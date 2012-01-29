#!/usr/bin/python

text = "TEXT"
line_no = "LINE_NO"

import sys
sys.setrecursionlimit(2000)

def get_matrix(*shape):
    if len(shape) == 0:
        return 0

    car = shape[0]
    cdr = shape[1:]

    return [get_matrix(*cdr) for i in range(car)]


def LCS_matrix(text_dict1, text_dict2):
    if not (text_dict1.has_key(text) and text_dict2.has_key(text)):
        return None

    #if not (text_dict1.has_key(line_no) and text_dict2.has_key(line_no)):
        #return None

    str1 = text_dict1[text]
    str2 = text_dict2[text]

    m = len(str1)
    n = len(str2)

    c = get_matrix(m + 1, n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])

    return c

def LCS_string(matrix, str1, str2, i, j):
    if i == 0 or j == 0:
        return ""

    elif str1[i-1] == str2[j-1]:
        return LCS_string(matrix, str1, str2, i - 1, j - 1) + str1[i-1]
    
    else:
        if matrix[i][j-1] > matrix[i-1][j]:
            return LCS_string(matrix, str1, str2, i, j - 1)
        else:
            return LCS_string(matrix, str1, str2, i - 1, j)


if __name__=='__main__':
    
    a = {}
    b = {}
    f = open('a', 'r')
    a[text] = f.read()
    f = open('b', 'r')
    b[text] = f.read()

    print LCS_string(LCS_matrix(a, b), a[text], b[text], len(a[text]),
                     len(b[text]))

