#!/usr/bin/python

import comparison

colors = ['red', 'blue', 'green', 'cyan', 'fuchsia', 'cyan']
c_len = 6

def dump_to_HTML(result, output):

    files = result[comparison.file_names]       
    lines = result[comparison.match_lines]

    lines_one = lines[comparison.lines1][::-1]
    lines_two = lines[comparison.lines2][::-1]

    path_f1 = files[0]
    path_f2 = files[1]

    form_HTML(path_f1, lines_one)

    form_HTML(path_f2, lines_two)


def form_HTML(path, lines):

    i = 1
    c = 0

    color_dict = {}

    for line in lines:
        curr_color = colors[c % c_len]
        c = c + 1
        for num in line:
            color_dict[num] = curr_color


    html_str = "<html> <head> <title>" + path + "</title> </head> <body>  <h6> " + path + " </h6> <hr> <p> <pre> \n"

    
    for line in open(path, 'r'):
        if color_dict.has_key(i):
            html_str = html_str + "<font color=" + color_dict[i] + ">" + line + "</font>"

        else:
            html_str = html_str + line

        i = i + 1


    html_str = html_str + "</pre> </p> </body> </html>"

    print html_str

