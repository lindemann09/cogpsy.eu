#!/usr/bin/bash python3

# convert rst file (as used for tex cv) into html
#
# Workflow: (see makefile)
# 1. convert rst -> converted rst
# 2. rst2html
# 3. convert html -> new html that can be included

import os
import sys


def print_text_array(txt_array):
    for x in txt_array:
        print(x, end="")

def convert4rst(filename):
    """converts code for rst, that is, include doi and pdf links
    """

    rtn = []
    fl = open(filename, "r")
    for l in fl:
        if l.find("doi:")>=0:
            tmp = l.split(" ")
            for x in range(len(tmp)):
                if tmp[x].startswith("doi:"):
                    tmp[x] = "`doi  <http://dx.doi.org/" + tmp[x][4:].strip() + \
                            ">`__: " + tmp[x][4:].strip()
            l = " ".join(tmp)


        if l.find("pdf:")>=0:
            tmp = l.split(" ")
            for x in range(len(tmp)):
                if tmp[x].startswith("pdf:"):
                    tmp[x] = "[`pdf <" + tmp[x][4:].strip() + ">`__]" + "\n"
            l = " ".join(tmp)

        if len(l)>0:
            rtn.append(l.rstrip()+ "\n")

    fl.close()
    return rtn

def convert_nolinks(filename):
    """converts code for rst, that is, removes pdf
    """

    rtn = []
    fl = open(filename, "r")
    for l in fl:
        if l.find("pdf:")>=0:
            tmp = l.split(" ")
            for x in range(len(tmp)):
                if tmp[x].startswith("pdf:"):
                    tmp[x] = " "
            l = " ".join(tmp)

        if len(l)>0:
            rtn.append(l.rstrip()+ "\n")
    fl.close()
    return rtn



def get_html_body(string_array):
    """returns the body of an html file (i.e. array of strings)"""

    BEGIN_TAG = '<body>'
    END_TAG = '</body>'

    rtn = []
    isbody = False
    for l in string_array:
        if l.find(BEGIN_TAG)>=0:
            isbody = True
        elif l.find(END_TAG)>=0:
            isbody = False
        elif isbody:
            rtn.append(l)

    return rtn


def replace_all(string_array, old, new):
    """replace in a string array"""

    return map(lambda x:x.replace(old, new), string_array)


def include_html(incl_html_file_name):
    """appends the content (body only) of the html file"""
    string_array = []
    with open(incl_html_file_name) as flin:
        in_array = flin.readlines()

    incl_array = get_html_body(in_array)
    # remove first and last line
    incl_array.pop()
    incl_array.pop(0)
    # adapt headings
    incl_array = replace_all(incl_array, "<h1>", "<h3>")
    incl_array = replace_all(incl_array, "</h1>", "</h3>")
    string_array.extend(incl_array)

    return string_array

if __name__ == "__main__":
    filename = sys.argv[1]

    if os.path.splitext(filename)[1] == ".rst":
        # RST FILE
        print_text_array(convert4rst(filename))

    if os.path.splitext(filename)[1] == ".html":
        # HTML FILE
        print_text_array(include_html(filename))
