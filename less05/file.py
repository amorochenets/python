# !/usr/bin/env python3
# coding UTF-8
newFile = open('file.txt')
for elem in newFile.readlines():
    print(elem.strip() + '!')