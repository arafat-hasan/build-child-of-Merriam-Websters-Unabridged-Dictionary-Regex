#!/usr/bin/env python3
#
# FILE: main.py
#
# @author: Arafat Hasan Jenin <opendoor.arafat[at]gmail[dot]com>
#
# LINK: https://github.com/arafat-hasan/build-child-of-Merriam-Websters-Unabridged-Dictionary-Regex/
#
# DATE CREATED: 18-07-19 02:09:53 (+06)
# LAST MODIFIED: 04-08-19 17:40:46 (+06)
#
# DEVELOPMENT HISTORY:
# Date         Version     Description
# --------------------------------------------------------------------
# 18-07-19     1.0         Deleted code is debugged code.
#
#               _/  _/_/_/_/  _/      _/  _/_/_/  _/      _/
#              _/  _/        _/_/    _/    _/    _/_/    _/
#             _/  _/_/_/    _/  _/  _/    _/    _/  _/  _/
#      _/    _/  _/        _/    _/_/    _/    _/    _/_/
#       _/_/    _/_/_/_/  _/      _/  _/_/_/  _/      _/
#
##############################################################################

import sys
import io
import re
import csv
import time



startTime = time.time()
data = 'global'

with io.open("dic.txt", mode='r', encoding='utf-8') as f:
    data = f.read()
    f.close()

outputFile = io.open("output.txt", mode='a+', encoding='utf-8')


def fileWrite(matches, word):
    tmp = "\n\n".join(str(v) for v in matches) + "\n\n"
    if(len(matches) == 0):
        tmp = word + "\nNot Found\n\n"
    outputFile.write(tmp)

def processWord(eng, ben):
    regex = "(?:^|\\n\\n)(" + eng.upper() + ".*?)(?=\\n\\n[A-Z]{3,}\\n|$)"
    matches = re.findall(regex, data, flags=re.DOTALL)
    # print(*matches, sep="\n\n#####################\n\n")
    # print(len(matches))
    fileWrite(matches, eng)




with open('word.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            # print(f'Column names are {", ".join(row)}')
            lineCount += 1
        else:
            lineCount += 1
            if len(row) != 2:
                continue
            processWord(row[0], row[1])
        sys.stdout.write("\r%d lines processed so far..." % lineCount)
        sys.stdout.flush()
    print(f'\nProcessed {lineCount} lines total')


outputFile.close()

print("Process Completed\n")
print("--- %s seconds ---" % (time.time() - startTime))

