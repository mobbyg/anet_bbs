#!/usr/bin/env python

import sys
import re

""" A new attempt to get an MCI Interpretor working for ANet """

def mciInterpret(filename):
    fileToRead = open(filename, 'r')
    for lines in fileToRead:
        mciTemp = re.split("(\{)(\w+)(\})", ',')
        print(mciTemp)


mciInterpret("sys.infox")
