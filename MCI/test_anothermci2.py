#!/usr/bin/env python

import re
import sys
import os

ansiColors = {"c0" : "30", "c1" : "31", "c2" : "32", "c3" : "33", "c4" : "34",
               "c5" : "35", "c6" : "36", "c7" : "37", "c8" : "30",
               "ca" : "31", "cb" : "32", "cc" : "33", "cd" : "34",
               "ce" : "35", "cf" : "36", "cg" : "37", "Z0" : "40" ,  "Z1" : "41",
               "Z2" : "42", "Z3" : "43", "Z4" : "44", "Z5" : "45", "Z6" : "46",
               "Z7" : "47"}


def repl(m):
    code = ansiColors[m.group(2)]
    if code[0] != "Z":
      ansitextattrib = "0"
    else: ansitextattrib = "1"
    if code == "c8" or code == "c9" or code == "ca" or code == "cb" or code == "cd" or code == "ce" or code == "cf" or code == "cg":
      ansitextattrib = "1"
    return '\033[' + ansitextattrib + ";" + code + "m"

display = open('sys.infox','r')
for lines in display:
    lines = re.sub(r'(\{)(\w+)(\})', repl , lines)
    print lines.strip('\n')
print ("\033[0m")
