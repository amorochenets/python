# !/usr/bin/env python3
# coding UTF-8
currentFile = open('file_hw3.txt')
newFile = open('newFile_hw3.txt', 'w')
newList = currentFile.read().split()
newList.sort()
newList = set(newList)
print(newList)
for i in newList:
    newFile.write(i + '\n')
currentFile.close()
newFile.close()
