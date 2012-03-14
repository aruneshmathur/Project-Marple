#!/usr/bin/python

import comparison, os

colors = ['red', 'blue', 'green', 'cyan', 'fuchsia', 'cyan']
c_len = 6

file1 = "match1.html"
file2 = "match2.html"
index = "index.html"


def dump_to_HTML(result, output_dir):

    if not os.path.isdir(output_dir):
        return False

    output_dir = output_dir + "/"


    files = result[comparison.file_names]       
    lines = result[comparison.match_lines]

    lines_one = lines[comparison.lines1][::-1]
    lines_two = lines[comparison.lines2][::-1]

    path_f1 = files[0]
    path_f2 = files[1]

    res = form_HTML(path_f1, lines_one)
    write(res, output_dir, file1)

    res = form_HTML(path_f2, lines_two)
    write(res, output_dir, file2)

    res = "<html><frameset cols=\"50%,50%\"><frame src=\"" + file1 + "\"><frame src=\"" + file2 + "\"></frameset></html>"
    write(res, output_dir, index)

    return True


def write(res, output_dir, filename):
    path = output_dir + "/" + filename
    f = open(path, 'w')
    f.write(res)
    f.close()

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
            html_str = html_str + "<font color=" + color_dict[i] + "><xmp>" + line.rstrip() + "</xmp></font>"

        else:
            html_str = html_str + line.rstrip()

        i = i + 1


    html_str = html_str + "</pre> </p> </body> </html>"

    return html_str


