#!/usr/bin/env python

import re
import sys
import os

ansiColors = {"c0" : "[0;30m", "c1" : "[31m", "c2" : "[0;32m", "c3" : "[0;33m", "c4" : "[0;34m",
               "c5" : "[0;35m", "c6" : "[0;36m", "c7" : "[0;37m", "c8" : "[1;30m",
               "ca" : "[1;31m", "cb" : "[1;32m", "cc" : "[1;33m", "cd" : "[1;34m",
               "ce" : "[1;35m", "cf" : "[1;36m", "cg" : "[1;37m", "R1" : "[0;41m",
               "R2" : "[0;42m", "R3" : "[0;43m", "R4" : "[0;44m", "R5" : "[0;45m", "R6" : "[0;46m",
               "R7" : "[0;47m"}


def repl(m):
    code = ansiColors[m.group(2)]
    return '\033' + code

display = open('sys.infox','r')
for lines in display:
    lines = re.sub(r'(\{)(\w+)(\})', repl , lines)
    print lines.strip('\n')