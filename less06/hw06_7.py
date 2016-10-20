# !/usr/bin/env python3
# coding UTF-8

currentFile = open('newFile.txt')
newFile = open('newFile7.txt', 'w')
newList = []
for line in currentFile:
    newList.append(line)
newList.reverse()
newFile.writelines(newList)
currentFile.close()
newFile.close()
