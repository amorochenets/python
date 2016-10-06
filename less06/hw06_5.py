# !/usr/bin/env python3
# coding UTF-8
currentFile = open('file_hw3.txt')
newList = currentFile.read().split()
counter = 0
for i in newList:
    if i.lower() == 'we':
        counter += 1
print(counter)
currentFile.close()
