#!/usr/bin/env python

import re
import sys
import os

def mciInterp(m):
    ansiBkGColor = "0"
    ansiFgColor = "c"
    ansiBold = "0"
    mciTemp = m.group(2)
    mciTemp = mciTemp.split(",")
    mciCMD1 = mciTemp[0]
    try:
        stringCMD2 = mciTemp[1]
    except IndexError:
        stringCMD2 = "None"
        pass

    if mciCMD1[0] != "Z":
        pass
    elif mciCMD1[0] == "Z":
        if mciCMD1[1] == "0":
            ansiBkGColor == "40" # Black
        elif mciCMD1[1] == "1":
            ansiBkGColor == "41" # Red
        elif mciCMD1[1] == "2":
            ansiBkGColor == "42" # Green
        elif mciCMD1[1] == "3":
            ansiBkGColor == "43" # Yellow
        elif mciCMD1[1] == "4":
            ansiBkGColor == "44" # Blue
        elif mciCMD1[1] == "5":
            ansiBkGColor == "45" # Purple
        elif mciCMD1[1] == "6":
            ansiBkGColor == "46" # Cyan
        elif mciCMD1[1] == "7":
            ansiBkGColor == "47" # White

    if mciCMD1[0] != "C":
        pass
    elif mciCMD1[0] == "C":
        if mciCMD1[1] == "0":
            ansiFgColor == "30" # Black
        elif mciCMD1[1] == "1":
            ansiFgColor == "31" # Red
        elif mciCMD1[1] == "2":
            ansiFgColor == "32" # Green
        elif mciCMD1[1] == "3":
            ansiFgColor == "33" # Yellow
        elif mciCMD1[1] == "4":
            ansiFgColor == "34" # Blue
        elif mciCMD1[1] == "5":
            ansiFgColor == "35" # Purple
        elif mciCMD1[1] == "6":
            ansiFgColor == "36" # Cyan
        elif mciCMD1[1] == "7":
            ansiFgColor == "37" # White
        elif mciCMD1[1] == "8":
            ansiFgColor == "30"
            ansiBold == "1"     #From here down will turn on bold for the respected color
        elif mciCMD1[1] == "9":
            ansiFgColor == "31"
            ansiBold == "1"
        elif mciCMD1[1] == "a":
            ansiFgColor == "32"
            ansiBold == "1"
        elif mciCMD1[1] == "b":
            ansiFgColor == "33"
            ansiBold == "1"
        elif mciCMD1[1] == "c":
            ansiFgColor == "34"
            ansiBold == "1"
        elif mciCMD1[1] == "d":
            ansiFgColor == "35"
            ansiBold == "1"
        elif mciCMD1[1] == "e":
            ansiFgColor == "36"
            ansiBold == "1"
        elif mciCMD1[1] == "f":
            ansiFgColor == "37"
            ansiBold == "1"

    return '\033[' + ansiBold + ";" + ansiBkGColor + ";" + ansiFgColor + "m"
    #return ansi


display = open('sys.infox','r')
for lines in display:
    lines = re.sub(r'(\{)(\w+)(\})', mciInterp, lines)
    print lines.strip('\n')
